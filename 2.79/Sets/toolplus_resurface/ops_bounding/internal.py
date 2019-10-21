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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# MAIN OPERATOR #
class View3D_TP_BBox_Origin_Minus_Z_Axis(bpy.types.Operator):  
    """set origim to minus z > bottom"""
    bl_idname = "tp_ops.bbox_origin_minus_z"  
    bl_label = "Origin to -Z"  
    bl_options = {'INTERNAL'}

    # ONLY OBJECTMODE    
    def execute(self, context):

        for ob in bpy.context.selected_objects:
            bpy.context.scene.objects.active = ob
             
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        for o in bpy.context.selected_objects:
            bpy.context.scene.objects.active = o                

            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z-=a
                             
            o.location.z+=a                   
                    
        return {'FINISHED'}


# MAIN OPERATOR #
class View3D_TP_BBox_Origin_Plus_Z_Axis(bpy.types.Operator):  
    """set origim to plus z > top"""
    bl_idname = "tp_ops.bbox_origin_plus_z"  
    bl_label = "Origin to +Z"  
    bl_options = {'INTERNAL'}
        
    # ONLY OBJECTMODE  
    def execute(self, context):
                
        for ob in bpy.context.selected_objects:
            bpy.context.scene.objects.active = ob 
            
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        for o in bpy.context.selected_objects:
            bpy.context.scene.objects.active = o 
            
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z+=a
                             
            o.location.z-=a                       
       
        return {'FINISHED'}




class View3D_TP_GLOBAL(bpy.types.Operator):
    """Transform Orientation Global"""
    bl_idname = "tp_ops.space_global"
    bl_label = "Transform Orientation GLOBAL"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'GLOBAL'
        return {'FINISHED'}
    

class View3D_TP_LOCAL(bpy.types.Operator):
    """Transform Orientation LOCAL"""
    bl_idname = "tp_ops.space_local"
    bl_label = "Transform Orientation LOCAL"
    bl_options = {'INTERNAL'}
    
    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'LOCAL'
        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()