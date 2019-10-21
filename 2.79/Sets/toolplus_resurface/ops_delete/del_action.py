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















