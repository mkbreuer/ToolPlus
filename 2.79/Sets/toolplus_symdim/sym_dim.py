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


class VIEW3D_TP_Copy_Dimension_Axis_OPs(bpy.types.Operator):
    """make symmetrical: copy the dimension of a choosen axis to other axis"""
    bl_idname = "tp_ops.copy_dimension_axis"
    bl_label = "Copy Dimension Axis"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis = bpy.props.EnumProperty(
        items=[("tp_x_y"    ,"X > Y"   ,""),
               ("tp_x_z"    ,"X > Z"   ,""),
               ("tp_y_x"    ,"Y > X"   ,""),
               ("tp_y_z"    ,"Y > Z"   ,""),
               ("tp_z_x"    ,"Z > X"   ,""),
               ("tp_z_y"    ,"Z > Y"   ,"")],
               name = "Copy Dimension",
               default = "tp_x_y",    
               description = "copy dimension from axis to axis")

    def execute(self, context):

        #obj = context.active_object

        #set mode
        bpy.ops.object.mode_set(mode='OBJECT')           

        active = bpy.context.active_object
        selected = bpy.context.selected_objects

        for obj in selected:
            
            #copy dimensions 
            
            #x-axis to y-axis            
            if self.tp_axis == "tp_x_y":
                obj.dimensions[1] = active.dimensions[0]
                        
            #y-axis to x-axis  
            if self.tp_axis == "tp_y_x":                      
                obj.dimensions[0] = active.dimensions[1]
            
            #x-axis to z-axis            
            if self.tp_axis == "tp_x_z":
                obj.dimensions[2] = active.dimensions[0]
                        
            #y-axis to z-axis            
            if self.tp_axis == "tp_y_z":
                obj.dimensions[2] = active.dimensions[1]
            
            #z-axis to x-axis            
            if self.tp_axis == "tp_z_x":
                obj.dimensions[0] = active.dimensions[2]
                        
            #z-axis to y-axis            
            if self.tp_axis == "tp_z_y":
                obj.dimensions[1] = active.dimensions[2]
                         
            #obj.location = active.location
            #obj.rotation_euler = active.rotation_euler

 
        print(self)
        self.report({'INFO'}, "Done")  
    
        return {'FINISHED'}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()