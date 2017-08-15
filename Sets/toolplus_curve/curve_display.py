# ##### BEGIN GPL LICENSE BLOCK #####
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
__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import*
from bpy.props import *


class View3D_TP_Wire_All(bpy.types.Operator):
    """Wire on all objects in the scene"""
    bl_idname = "tp_ops.wire_all"
    bl_label = "Wire on All Objects"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        
        for obj in bpy.data.objects:
            if obj.show_wire:
                obj.show_all_edges = False
                obj.show_wire = False            
            else:
                obj.show_all_edges = True
                obj.show_wire = True
                             
        return {'FINISHED'} 


class View3D_TP_Wire_On(bpy.types.Operator):
    '''Wire on'''
    bl_idname = "tp_ops.wire_on"
    bl_label = "Wire on"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        selection = bpy.context.selected_objects  
         
        if not(selection): 
            for obj in bpy.data.objects:
                obj.show_wire = True
                obj.show_all_edges = True
                
        else:
            for obj in selection:
                obj.show_wire = True
                obj.show_all_edges = True 
        return {'FINISHED'}


class View3D_TP_Wire_Off(bpy.types.Operator):
    '''Wire off'''
    bl_idname = "tp_ops.wire_off"
    bl_label = "Wire off"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        selection = bpy.context.selected_objects  
        
        if not(selection): 
            for obj in bpy.data.objects:
                obj.show_wire = False
                obj.show_all_edges = False
                
        else:
            for obj in selection:
                obj.show_wire = False
                obj.show_all_edges = False   

        return {'FINISHED'}
    

class View3D_TP_Display_DrawWire(bpy.types.Operator):
    """Draw Type Wire"""
    bl_idname = "tp_ops.draw_wire"
    bl_label = "Draw Type Wire"

    def execute(self, context):
        bpy.context.object.draw_type = 'WIRE'       
        return {'FINISHED'}


class View3D_TP_Display_DrawSolid(bpy.types.Operator):
    """Draw Type Solid"""
    bl_idname = "tp_ops.draw_solid"
    bl_label = "Draw Type Solid"

    def execute(self, context):
        bpy.context.object.draw_type = 'SOLID'       
        return {'FINISHED'}


class View3D_TP_Normals(bpy.types.Operator):
    """Recalculate Normals for all selected Objects in Objectmode"""
    bl_idname = "tp_ops.rec_normals"
    bl_label = "Recalculate Normals"     

    def execute(self, context):
        print(self)
        self.report({'INFO'}, "Recalculate Normals")   
                        
        for obj in bpy.context.selected_objects:
            
            obj = bpy.context.scene.objects.active                
           
            if obj:
                
                if obj.type in {'MESH'}:                 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent()
                    bpy.ops.object.editmode_toggle()            
      
        return {'FINISHED'}        




def register():   
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    

