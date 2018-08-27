# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


#bl_info = {
#    "name": "Sculpt Tools",
#    "author": "Ian Lloyd Dela Cruz, Nicholas Bishop, Roberto Roch, Bartosz Styperek, Piotr Adamowicz",
#    "version": (1, 0),
#    "blender": (2, 7, 0),
#    "location": "3d View > Tool shelf, Shift-Ctrl-B",
#    "description": "Simple UI for Boolean and Remesh operators",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Sculpting"}



# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *    
import mathutils, bmesh



class VIEW3D_TP_ReSphere_Operator(bpy.types.Operator):
    '''resphere the remesh'''
    bl_idname = "tp_ops.resphere"
    bl_label = "Sculpt ReSphere"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context): 
        layout = self.layout

        col = layout.column(1)

        box = col.box().column(1) 

        row = box.column(1)  
        row.label("Value 0.2")
    
        box.separator() 

    def execute(self, context):

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.tosphere(value=0.2, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
        bpy.ops.object.mode_set(mode=oldmode)
        return {'FINISHED'}


def objDuplicate(obj):

    activeObj = bpy.context.active_object

    # store mode
    oldMode = activeObj.mode    
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action = 'DESELECT')
    bpy.ops.object.select_pattern(pattern = obj.name)

    bpy.ops.object.duplicate()

    objCopy = bpy.context.selected_objects[0]

    bpy.context.scene.objects.active = activeObj    

    # reload mode
    bpy.ops.object.mode_set(mode=oldMode)
    return objCopy


    
class VIEW3D_TP_Remesh_Operator(bpy.types.Operator):
    '''Remesh an object at the given octree depth'''
    bl_idname = "tp_ops.remesh"
    bl_label = "Sculpt Remesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    remeshDepthInt = IntProperty(min = 2, max = 10, default = 4)
    remeshSubdivisions = IntProperty(min = 0, max = 6, default = 0)
    remeshPreserveShape = BoolProperty(default = True)

    def draw(self, context): 
        layout = self.layout

        col = layout.column(1)

        box = col.box().column(1) 

        row = box.column(1)                                 
        row.prop(self, "remeshDepthInt", text="Depth")
        row.prop(self, "remeshSubdivisions", text="Subdivisions")
        row.prop(self, "remeshPreserveShape", text="Preserve Shape")
    
        box.separator() 


    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):

        settings_write(self) 

        ob = context.active_object
        oldMode = ob.mode
        
        dyntopoOn = False;
        if context.active_object.mode == 'SCULPT': 
            if context.sculpt_object.use_dynamic_topology_sculpting:
                dyntopoOn = True
                bpy.ops.sculpt.dynamic_topology_toggle()
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        if self.remeshPreserveShape:            
            obCopy = objDuplicate(ob)
        
        md = ob.modifiers.new('sculptremesh', 'REMESH')
        md.mode = 'SMOOTH'
        md.octree_depth = self.remeshDepthInt
        md.scale = .99
        md.use_remove_disconnected = False

        # apply the modifier
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="sculptremesh")
        
        if self.remeshSubdivisions > 0:
            mdsub = ob.modifiers.new('RemeshSubSurf', 'SUBSURF')
            mdsub.levels = self.remeshSubdivisions
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="RemeshSubSurf")
        
        
        if self.remeshPreserveShape:            
            md2 = ob.modifiers.new('RemeshShrinkwrap', 'SHRINKWRAP')
            md2.wrap_method = 'PROJECT'
            md2.use_negative_direction = True
            md2.use_positive_direction = True
            md2.target = obCopy
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="RemeshShrinkwrap")
            
            bpy.data.scenes[0].objects.unlink(obCopy)
            bpy.data.objects.remove(obCopy)
        
        bpy.ops.object.mode_set(mode=oldMode)
        
        if dyntopoOn == True:
            bpy.ops.sculpt.dynamic_topology_toggle()
        
        ob.select = True
        return {'FINISHED'}
        



class VIEW3D_TP_Mask_Extract(bpy.types.Operator):
    """Extracts the masked area into a new mesh"""
    bl_idname = "tp_ops.mask_extract"
    bl_label = "Mask Extract"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'SCULPT'

    extractDepthFloat = FloatProperty(min = -10.0, max = 10.0, default = 0.1)
    extractOffsetFloat = FloatProperty(min = -10.0, max = 10.0, default = 0.0)
    extractSmoothIterationsInt = IntProperty(min = 0, max = 50, default = 5)    
    extractStyleEnum = EnumProperty(name="Extract style", 
               items = (("SOLID","Solid",""), ("SINGLE","Single Sided",""), ("FLAT","Flat","")), default = "SOLID")
    
    def draw(self, context): 
        layout = self.layout

        col = layout.column(align=True)
 
        box = col.box().column(1) 
         
        col = box.column(1)           
        col.prop(self, "extractStyleEnum", text="Style")
        
        col.separator()
        
        col.prop(self, "extractDepthFloat", text="Depth")
        col.prop(self, "extractOffsetFloat", text="Offset")
        col.prop(self, "extractSmoothIterationsInt", text="Smooth Iterations")
  
        box.separator()

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):

        settings_write(self) 

        activeObj = context.active_object
        
        # This is a hackish way to support redo functionality despite sculpt mode having its own undo system.
        # The set of conditions here is not something the user can create manually from the UI.
        # Unfortunately I haven't found a way to make Undo itself work
        if  2>len(bpy.context.selected_objects)>0 and \
            context.selected_objects[0] != activeObj and \
            context.selected_objects[0].name.startswith("Extracted."):
            rem = context.selected_objects[0]
            remname = rem.data.name
            bpy.data.scenes[0].objects.unlink(rem)
            bpy.data.objects.remove(rem)
            # remove mesh to prevent memory being cluttered up with hundreds of high-poly objects
            bpy.data.meshes.remove(bpy.data.meshes[remname])
        
        # For multires we need to copy the object and apply the modifiers
        try:
            if activeObj.modifiers["Multires"]:
                use_multires = True
                objCopy = objDuplicate(activeObj)
                bpy.context.scene.objects.active = objCopy
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.boolean.mod_apply()
        except:
            use_multires = False
            pass
            
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Automerge will collapse the mesh so we need it off.
        if context.scene.tool_settings.use_mesh_automerge:
            automerge = True
            bpy.data.scenes[context.scene.name].tool_settings.use_mesh_automerge = False
        else:
            automerge = False

        # Until python can read sculpt mask data properly we need to rely on the hiding trick
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent();
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='SCULPT')
        bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="FACE")
        bpy.ops.mesh.reveal()
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate=None, TRANSFORM_OT_translate=None)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        
        # For multires we already have a copy, so lets use that instead of separate.
        if use_multires == True:
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.delete(type='FACE')
            bpy.context.scene.objects.active = objCopy;
        else:
            try:
                bpy.ops.mesh.separate(type="SELECTED")
                bpy.context.scene.objects.active = context.selected_objects[0];
            except:
                bpy.ops.object.mode_set(mode='SCULPT')
                bpy.ops.paint.hide_show(action='SHOW', area='ALL')
                return {'FINISHED'}
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Rename the object for disambiguation
        bpy.context.scene.objects.active.name = "Extracted." + bpy.context.scene.objects.active.name
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Solid mode should create a two-sided mesh
        if self.extractStyleEnum == 'SOLID':
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.shrink_fatten(value=-self.extractOffsetFloat) #offset
            bpy.ops.mesh.region_to_loop()
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.vertices_smooth(repeat = self.extractSmoothIterationsInt) #smooth everything but border edges to sanitize normals
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.solidify(thickness = -self.extractDepthFloat)
            bpy.ops.mesh.select_all(action='SELECT')
            if self.extractSmoothIterationsInt>0: bpy.ops.mesh.vertices_smooth(repeat = self.extractSmoothIterationsInt)
            bpy.ops.mesh.normals_make_consistent();

        elif self.extractStyleEnum == 'SINGLE':
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.shrink_fatten(value=-self.extractOffsetFloat) #offset
            bpy.ops.mesh.region_to_loop()
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.vertices_smooth(repeat = self.extractSmoothIterationsInt) #smooth everything but border edges to sanitize normals
            bpy.ops.mesh.select_all(action='SELECT')
            # This is to create an extra loop and prevent the bottom vertices running up too far in smoothing
            # Tried multiple ways to prevent this and this one seemed best
            bpy.ops.mesh.inset(thickness=0, depth=self.extractDepthFloat/1000, use_select_inset=False)
            bpy.ops.mesh.inset(thickness=0, depth=self.extractDepthFloat-(self.extractDepthFloat/1000), use_select_inset=False)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.vertices_smooth(repeat = self.extractSmoothIterationsInt)
            bpy.ops.mesh.normals_make_consistent()

        elif self.extractStyleEnum == 'FLAT':
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            # Offset doesn't make much sense for Flat mode, so let's add it to the depth to make it a single op.
            bpy.ops.transform.shrink_fatten(value=-self.extractDepthFloat-self.extractOffsetFloat) 
            if self.extractSmoothIterationsInt>0: bpy.ops.mesh.vertices_smooth(repeat = self.extractSmoothIterationsInt)
            
        # clear mask on the extracted mesh
        bpy.ops.object.mode_set(mode='SCULPT')
        bpy.ops.paint.hide_show(action='SHOW', area='ALL')
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)
        
        #bpy.ops.object.mode_set(mode='OBJECT')
        
        # make sure to recreate the odd selection situation for redo
        if use_multires:
            bpy.ops.object.select_pattern(pattern=context.active_object.name, case_sensitive=True, extend=False)
        bpy.context.scene.objects.active = activeObj
        
        # restore automerge
        if automerge:
            bpy.data.scenes[context.scene.name].tool_settings.use_mesh_automerge = True

        # restore mode for original object
        bpy.ops.object.mode_set(mode='SCULPT')
        return {'FINISHED'}
    




    

class VIEW3D_TP_Boolean_Freeze(bpy.types.Operator):
    '''Decimates the object temporarily for viewport performance'''
    bl_idname = "tp_ops.bool_freeze"
    bl_label = "Boolean Freeze"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and len(bpy.context.selected_objects)==1 and context.active_object.frozen == False

    def execute(self, context):

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')    
        
        if "Frozen" not in bpy.data.groups:
            bpy.data.groups.new("Frozen")
        
        ob = context.active_object
        obCopy = objDuplicate(ob)
        md = ob.modifiers.new('BoolDecimate', 'DECIMATE')
        md.ratio = 0.1
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="BoolDecimate")
        ob.hide_render = True
        obCopy.select = True
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
        obCopy.name = "Frozen_"+ob.name
        obCopy.hide = True
        obCopy.hide_select = True
        obCopy.select = False
        ob.select = True
        bpy.ops.object.group_link(group='Frozen')
        ob.frozen = True

        bpy.ops.object.mode_set(mode=oldmode)        

        return {'FINISHED'}
        


class VIEW3D_TP_Boolean_Unfreeze(bpy.types.Operator):
    '''Decimates the object temporarily for viewport performance'''
    bl_idname = "tp_ops.bool_unfreeze"
    bl_label = "Boolean Unfreeze"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and len(bpy.context.selected_objects)==1 and context.active_object.frozen == True

    def execute(self, context):

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')    

        ob = bpy.context.active_object
        
        for sceneObj in bpy.context.scene.objects:
            if sceneObj.parent == ob:
                frozen = sceneObj
        
        remname = ob.data.name
        
        ob.data = bpy.context.scene.objects['Frozen_'+ob.name].data
        
        bpy.data.scenes[bpy.context.scene.name].objects.unlink(frozen)
        bpy.data.objects.remove(frozen)

        # remove mesh to prevent memory being cluttered up with hundreds of high-poly objects
        bpy.data.meshes.remove(bpy.data.meshes[remname])
        
        ob.hide_render = False
        
        bpy.data.groups['Frozen'].objects.unlink(bpy.context.object)
        
        ob.frozen = False

        bpy.ops.object.mode_set(mode=oldmode)
        
        return {'FINISHED'}




# PROPERTY GROUP: REMESH #
class Sculpt_Remesh_Properties(bpy.types.PropertyGroup):

    bpy.types.Object.frozen = BoolProperty(name="frozen", default = False)

        
    remeshDepthInt = IntProperty(min = 2, max = 10, default = 4)
    remeshSubdivisions = IntProperty(min = 0, max = 6, default = 0)
    remeshPreserveShape = BoolProperty(default = True)

    extractDepthFloat = FloatProperty(min = -10.0, max = 10.0, default = 0.1)
    extractOffsetFloat = FloatProperty(min = -10.0, max = 10.0, default = 0.0)
    extractSmoothIterationsInt = IntProperty(min = 0, max = 50, default = 5)    
    extractStyleEnum = EnumProperty(name="Extract style", items = (("SOLID","Solid",""), ("SINGLE","Single Sided",""), ("FLAT","Flat","")), default = "SOLID")



# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp = bpy.context.window_manager.tp_props_remesh
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))


# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_remesh
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))



# REGISTRY #        

def register():
    bpy.utils.register_module(__name__)

    bpy.types.WindowManager.tp_props_remesh = PointerProperty(type = Sculpt_Remesh_Properties)   

def unregister():
    bpy.utils.unregister_module(__name__)
    
    try:
        del bpy.types.WindowManager.tp_props_remesh        
    except:
        pass

if __name__ == "__main__":
    register()