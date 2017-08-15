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

__author__ = "mkbreuer"
__status__ = "toolplus"
__version__ = "1.0"
__date__ = "2016"

import bpy
from bpy import *
from bpy.props import *



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



class View3D_TP_Bounding_MeshCage(bpy.types.Operator):
    """add bounding meshcage box / planar axis"""
    bl_idname = "tp_ops.add_bound_meshcage"
    bl_label = "MeshCageBox"
    bl_options = {'REGISTER', 'UNDO'}
       
    def execute(self, context):
        obj = context.active_object
   
        #set cursor to selected
        bpy.ops.view3d.snap_cursor_to_selected()

        #set mode
        bpy.ops.object.mode_set(mode='OBJECT')        
        
        #dummy
        bpy.ops.object.duplicate()
        bpy.ops.object.join()

        #set origin to bounding box center
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
           
        bpy.context.active_object.name = "MCB_Dummy"

        #create box            
        bpy.ops.mesh.primitive_cube_add()
        
        #active box
        bpy.context.active_object.name = "MeshCageBox"
        
        #add dummy to selection
        bpy.ops.object.select_pattern(pattern="*MCB_Dummy")        



        if len(bpy.context.selected_objects) > 1:

            #active box
            first_obj = bpy.context.active_object

            obj_a, obj_b = context.selected_objects

            second_obj = obj_a if obj_b == first_obj else obj_b  
            
            #set dummy as active
            #bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]           
            bpy.context.scene.objects.active = bpy.data.objects["MCB_Dummy"] 
            bpy.data.objects[second_obj.name].select=True


            active = bpy.context.active_object
            selected = bpy.context.selected_objects

            for obj in selected:
                
                #copy dimensions to it
                obj.dimensions = active.dimensions
                obj.location = active.location
                obj.rotation_euler = active.rotation_euler

            bpy.ops.object.select_all(action='DESELECT')
           
            #add dummy to selection and delete                
            bpy.ops.object.select_pattern(pattern="*MCB_Dummy")          
            bpy.ops.object.delete(use_global=False)         

 
        bpy.ops.object.select_pattern(pattern="MeshCageBox")
        bpy.context.scene.objects.active = bpy.data.objects["MeshCageBox"]    
        bpy.context.object.draw_type = 'WIRE'
        
        #toggle mode
        bpy.ops.object.editmode_toggle()
        #select all
        bpy.ops.mesh.select_all(action='SELECT')

        print(self)
        self.report({'INFO'}, "MeshCageBox")  
    
        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()