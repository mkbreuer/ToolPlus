bl_info = {
    "name": "Curve Conversion",
    "description": "Converts Curve To Mesh To Allow Updating Of Mesh",
    "author": "Jacob Morris",
    "blender": (2, 76, 0),
    "location": "View 3D > Tools > Tools > Curve Conversion",
    "version": (0, 8),
    "category": "Object"
}

import bpy
from bpy.props import StringProperty, BoolProperty
bpy.types.Object.names = StringProperty(name="", default="")
bpy.types.Object.rscale = BoolProperty(name="Respect Scale?", default=False)


def CurveConvert(self, context):
    o = context.object
    na = []
    jna = []

    if "," in o.names:
        na = o.names.split(",")
        del na[len(na) - 1]
    else:
        na.append(o.names)

    # get materials names from mesh object before update
    mats = []
    for mat in o.data.materials:
        mats.append(mat.name)

    for i in na:
        if i in bpy.data.objects:
            curve = bpy.data.objects[i]
            if curve.type == "CURVE":
                o.select = False
                curve.select = True
                context.scene.objects.active = curve
                bpy.ops.object.duplicate()
                bpy.ops.object.convert(target="MESH")
                temp = context.object
                # if first mesh
                if len(na) == 1:
                    for mat in curve.data.materials:
                        if mat.name not in o.data.materials:
                            o.data.materials.append(mat)
                    o.data = context.object.data.copy()
                    o.select = False
                    temp.select = True
                    context.scene.objects.active = temp
                    bpy.ops.object.delete()
                    o.select = True
                    context.scene.objects.active = o
                    if o.rscale == True or len(na) >= 2:
                        o.scale = curve.scale
                # other objects
                else:
                    jna.append(temp.name)
                # clean up geometry
                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.remove_doubles(threshold=0.0001)
                bpy.ops.mesh.normals_make_consistent()
                bpy.ops.object.mode_set()
                for mat in mats:
                    if mat not in o.data.materials:
                        o.data.materials.append(bpy.data.materials[mat])
            else:
                self.report({"ERROR"}, "Object Not Curve")
        else:
            self.report({"ERROR"}, "Object Not Found")
    # join multiple objects
    o.select = False
    for i in jna:
        temp = bpy.data.objects[jna[0]]
        if i != jna[0]:
            bpy.data.objects[i].select = True
            temp.select = True
            context.scene.objects.active = temp
            bpy.ops.object.join()
    if jna != []:
        o.data = temp.data.copy()
        temp.select = True
        context.scene.objects.active = temp
        bpy.ops.object.delete()
    o.select = True
    context.scene.objects.active = o


class CurveConversionAdd(bpy.types.Operator):
    bl_label = "Add Mesh Object"
    bl_idname = "mesh.curve_convert_add"
    bl_options = {"UNDO"}

    def execute(self, context):
        na = context.object.name
        out = ""
        if len(context.selected_objects) == 1:
            out = na
        else:
            for i in context.selected_objects:
                out += i.name + ","
        loc = list(context.object.location.copy())
        loc[2] += 0.5
        bpy.ops.mesh.primitive_cube_add(location=loc)
        context.object.names = out
        CurveConvert(self, context)

        return {"FINISHED"}


class CruveConversionAddMultiple(bpy.types.Operator):
    bl_label = "Add Multiple Mesh Objects"
    bl_idname = "mesh.curve_convert_add_multiple"
    bl_options = {"UNDO"}

    def execute(self, context):
        nas = []
        # get names
        for i in context.selected_objects:
            nas.append(i.name)
        # deselect all
        for o in bpy.data.objects:
            o.select = False
        # use name to get objects and convert
        for objs in nas:
            ob = bpy.data.objects[objs]
            loc = list(ob.location)
            loc[2] += 0.5
            bpy.ops.mesh.primitive_cube_add(location=loc)
            context.object.names = objs
            CurveConvert(self, context)

        return {"FINISHED"}


class CurveConversionUpdate(bpy.types.Operator):
    bl_label = "Update Mesh"
    bl_idname = "mesh.curve_convert_update"
    bl_options = {"UNDO"}

    def execute(self, context):
        CurveConvert(self, context)
        return {"FINISHED"}


class CurveConversionUpdateAll(bpy.types.Operator):
    bl_label = "Propagate Changes"
    bl_idname = "mesh.curve_convert_update_all"
    bl_options = {"UNDO"}

    @classmethod
    def poll(self, context):
        return context.object.type == "CURVE"

    def execute(self, context):
        o = context.object
        # change out of editmode if needed
        mode = o.mode
        bpy.ops.object.mode_set(mode="OBJECT")

        na = []
        for obj in bpy.data.objects:
            if o.name in obj.names:
                na.append(obj.name)
        o.select = False

        for n in na:
            temp = bpy.data.objects[n]
            temp.select = True
            context.scene.objects.active = temp
            CurveConvert(self, context)
            temp.select = False
        # tell user number of objects updated
        if na == 0:
            self.report({"INFO"}, "No Objects Updated")
        else:
            self.report({"INFO"}, str(len(na)) + " Objects Updated")

        o.select = True
        context.scene.objects.active = o
        bpy.ops.object.mode_set(mode=mode)

        return {"FINISHED"}


class CurveConversionPanel(bpy.types.Panel):
    bl_label = "Curve Conversion"
    bl_idname = "OBJECT_PT_convert"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        o = context.object
        if o != None:
            if o.type == "MESH":
                layout.label("Curve Name:", icon="OUTLINER_OB_CURVE")
                if "," in o.names:
                    li = o.names.split(",")
                    del li[len(li) - 1]
                    for i in li:
                        layout.label(i)
                else:
                    layout.prop_search(o, "names", context.scene, "objects")
                    layout.prop(o, "rscale", icon="MAN_SCALE")
                layout.operator("mesh.curve_convert_update", icon="FILE_REFRESH")
            elif o.type == "CURVE":
                if context.mode not in ("EDIT_CURVE", "EDIT_MESH"):
                    layout.operator("mesh.curve_convert_add", icon="MESH_CUBE")
                    if len(context.selected_objects) > 1:
                        layout.operator("mesh.curve_convert_add_multiple", icon="GROUP")

                layout.operator("mesh.curve_convert_update_all", icon="FILE_REFRESH")
            else:
                layout.label("Object Needs To Be Curve Or Mesh Object", icon="ERROR")
        else:
            layout.label("Select Curve Or Mesh Object", icon="ERROR")


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
