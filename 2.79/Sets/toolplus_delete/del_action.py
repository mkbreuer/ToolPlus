# ##### BEGIN GPL LICENSE BLOCK #####
#
# 2017 MKB
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODUL #    
import bpy, bmesh 
from bpy import *
from bpy.props import *


from os.path import dirname
from . import del_keymap

class View3D_TP_KeyMap(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_delete"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = del_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


class VIEW3D_TP_Remove_Doubles(bpy.types.Operator): 
    """Removes doubles on selected objects."""
    bl_idname = "tp_ops.remove_double"
    bl_label = "Remove Doubles off Selected"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.object.join()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        return {'FINISHED'}


class VIEW3D_TP_Visual_Delete_Materials(bpy.types.Operator):
    """Remove all materials slots / Value Slider"""
    bl_idname = "tp_ops.remove_all_material"
    bl_label = "Delete all Material"
    bl_options = {'REGISTER', 'UNDO'}

    deleteMat = bpy.props.IntProperty(name="Delete Material-Slots", description="Value", default=1, min=1, soft_max=1000, step=1)
    
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(1)   

        row = box.row(1)                
        row.prop(self,'deleteMat', text="Delete Material Slots")         

        
    def execute(self, context):                

        if context.object.mode == 'EDIT':
                bpy.ops.object.editmode_toggle()      
                bpy.ops.object.material_slot_remove()
                bpy.ops.object.editmode_toggle()
        else:
            for i in range(self.deleteMat):
                bpy.ops.object.material_slot_remove()

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)  



class VIEW3D_TP_Ring_Dissolve(bpy.types.Operator):
    """select edge ring > checker deselect > select loop > dissolve"""
    bl_idname = "tp_ops.dissolve_ring"
    bl_label = "Ring Dissolve"
    bl_options = {'REGISTER', 'UNDO'}

    loop = bpy.props.BoolProperty(name="Ring or Loop",  description="select ring or edge loop", default=True, options={'SKIP_SAVE'})    
    checker = bpy.props.IntProperty(name="Nth Checker",  description="deselect every nth selected", min=1, max=50, default=1) 
    offset = bpy.props.IntProperty(name="Offset Nth",  description="offset nth", min=0, max=50, default=0) 
    grow = bpy.props.IntProperty(name="Grow Loop", description="How much to grow selection", default= 0, min=0, soft_max=50)   

    def draw(self, context):
        layout = self.layout   
        
        col = layout.column(1)   
        box = col.box().column(1)   

        row = box.column(1)                
        row.prop(self,'loop', text="Ring or Loop")     
        row.prop(self,'checker', text="Nth Checker")     
        row.prop(self,'offset', text="Offset Nth")     
        row.prop(self,'grow', text="Grow Loop")     

        box.separator() 


    def execute(self, context):

        #check for mesh selections
        object = context.object
        object.update_from_editmode()

        mesh_bm = bmesh.from_edit_mesh(object.data)

        selected_faces = [f for f in mesh_bm.faces if f.select]
        selected_edges = [e for e in mesh_bm.edges if e.select]
        selected_verts = [v for v in mesh_bm.verts if v.select]

        # check wich select mode is active  
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True): 
            # check verts selection value  
            self.report({'WARNING'}, "Only EdgeMode!")
            return {'CANCELLED'}
              
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False): 
            self.report({'WARNING'}, "Only EdgeMode!")
            return {'CANCELLED'}

      
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):   
            # to be sure that only edge are selectable
            #bpy.ops.mesh.select_mode(type="EDGE") 
         
            if len(selected_edges) == 1:   
               
                bpy.ops.mesh.loop_multi_select(ring=self.loop)  
                bpy.ops.mesh.select_nth(nth=self.checker, skip=1, offset=self.offset)
                
                # used ktools loop grow
                bpy.ops.tp_ops.grow_loop_for_dissolve(grow=self.grow)

                #bpy.ops.mesh.loop_multi_select(ring=False)                
                bpy.ops.mesh.delete_edgeloop()

            else:
                self.report({'WARNING'}, "Select only 1 Edge!")
                return {'CANCELLED'}


        return {'FINISHED'}




class VIEW3D_TP_GRP_Purge(bpy.types.Operator):
    """purge grease pencil layer"""
    bl_idname = "tp_ops.grp_purge"
    bl_label = "Purge"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):        
        bpy.ops.gpencil.data_unlink()
        bpy.context.scene.mod_list = 'grease_pencil'
        bpy.ops.ba.delete_data_obs()

        return {'FINISHED'}


class VIEW3D_TP_Purge_Mesh(bpy.types.Operator):
    '''Purge orphaned mesh'''
    bl_idname="tp_ops.purge_unused_mesh_data"
    bl_label="Purge Mesh"
    bl_options = {"REGISTER", 'UNDO'}    

    def execute(self, context):

        target_coll = eval("bpy.data.meshes")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}


class Purge_Materials(bpy.types.Operator):
    '''Purge orphaned materials'''
    bl_idname="tp_ops.purge_unused_material_data"
    bl_label="Purge Materials"
    
    def execute(self, context):

        target_coll = eval("bpy.data.materials")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()















