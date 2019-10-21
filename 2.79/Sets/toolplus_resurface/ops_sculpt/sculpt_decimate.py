# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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
import bpy
from bpy import *
from bpy.props import *    
import mathutils, bmesh




class VIEW3D_TP_Paint_Decimate_Mask(bpy.types.Operator):
    """paint the decimate mask"""
    bl_idname = "tp_ops.decimate_mask_paint"
    bl_label = "Paint Decimate Mask"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
       
        obj = context.active_object
        paint = context.tool_settings.image_paint
        bpy.context.object.modifiers["Decimate"].show_viewport = False
        bpy.ops.paint.brush_select(sculpt_tool='MASK')           

        return {"FINISHED"}

        
class VIEW3D_TP_Decimate_Mask(bpy.types.Operator):
    """decimate the masking areas"""
    bl_idname = "tp_ops.decimate_mask_areas"
    bl_label = "Decimate Mask"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        bpy.context.object.modifiers["Decimate"].show_viewport = False          
       
        bpy.ops.object.mode_set(mode='OBJECT')    
        
        obj_list = [obj for obj in bpy.context.selected_objects]
        obj = context.active_object
        for obj in obj_list:  
            bpy.context.scene.objects.active = obj
            obj.select = True

            for vgroup in obj.vertex_groups:
                if vgroup.name.startswith("M"):
                    obj.vertex_groups.remove(vgroup)
            
            bpy.ops.object.mode_set(mode='SCULPT')
            bpy.ops.paint.hide_show(action='HIDE', area='MASKED')

            bpy.ops.object.mode_set(mode='EDIT')
            
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.reveal()                           
            
            obj.vertex_groups.new("Mask_Group")
            for vgroup in obj.vertex_groups:
                if vgroup.name.startswith("M"):
                    bpy.ops.object.vertex_group_assign()
                    
            bpy.ops.object.mode_set(mode='OBJECT')        
            bpy.context.object.modifiers["Decimate"].vertex_group = "Mask_Group"
            bpy.context.object.modifiers["Decimate"].ratio = 0.9

        bpy.context.object.modifiers["Decimate"].show_viewport = True  

        bpy.ops.sculpt.sculptmode_toggle()   
        return {"FINISHED"}   
  


class VIEW3D_TP_Remove_Decimate_Mask(bpy.types.Operator):
    """remove decimate mask"""
    bl_idname = "tp_ops.decimate_mask_remove"
    bl_label = "Remove Decimate Mask"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        obj = context.active_object
        
        # remove groups with m as first letter
        for vgroup in obj.vertex_groups:
            if vgroup.name.startswith("M"):
                obj.vertex_groups.remove(vgroup)
        bpy.context.object.modifiers["Decimate"].vertex_group = ""
        
        return {"FINISHED"}
 

# REGISTRY #        

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()