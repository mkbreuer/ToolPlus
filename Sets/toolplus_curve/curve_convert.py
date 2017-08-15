"""
bl_info = {
    "name" : "Curve Conversion",
    "description" : "Converts Curve To Mesh To Allow Updating Of Mesh",
    "author" : "Jacob Morris",
    "blender" : (2, 72, 0),
    "location" : "Properties > Modifiers > Curve Conversion",
    "versoin" : (0, 1),
    "category" : "Object"
    }
"""
import bpy
from bpy.props import StringProperty, BoolProperty
bpy.types.Object.names = StringProperty(name = "", default = "")
bpy.types.Object.rscale = BoolProperty(name = "Respect Scale?", default = False)

class CurveConversionUpdate(bpy.types.Operator):
    """Update Mesh from Non-Destructive-Curve"""
    bl_label = "Update Mesh"
    bl_idname = "mesh.convert_update"
    
    def execute(self, context):
        o = context.object
        if o.names in bpy.data.objects:
            curve = bpy.data.objects[o.names]
            bpy.context.scene.objects.active = curve
            if curve.type == "CURVE":
                mesh = curve.data.copy()
                ob = bpy.data.objects.new("mesh", mesh)
                context.scene.objects.link(ob)
                ob.select = True; o.select = False; bpy.context.scene.objects.active = ob; bpy.ops.object.convert(target = "MESH")
                for i in o.data.materials:
                    ob.data.materials.append(i)
                o.data = ob.data
                if o.rscale == True:
                    o.scale = curve.scale
                bpy.ops.object.delete()
                bpy.context.scene.objects.active = o; o.select = True
            else:
                self.report({"ERROR"}, "Object Not Curve")
        else:
            self.report({"ERROR"}, "Object Not Found")
        return {"FINISHED"}
"""                
class CurveConversionPanel(bpy.types.Panel):
    bl_label = "Curve Conversion"
    bl_idname = "OBJECT_PT_convert"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "modifier"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout; 
        
        o = context.object
        if o.type == "MESH":
            layout.label("Curve Name:")
            layout.prop(o, "names"); layout.prop(o, "rscale", icon = "MAN_SCALE")
            layout.operator("mesh.convert_update")
        else:
            layout.label("Base Object Needs To Be Mesh Object", icon = "ERROR")
"""

def register():
    bpy.utils.register_class(CurveConversionUpdate)
    #bpy.utils.register_class(CurveConversionPanel)
def unregister():
    bpy.utils.unregister_class(CurveConversionUpdate)
    #bpy.utils.unregister_class(CurveConversionPanel)

if __name__ == "__main__":
    register()
