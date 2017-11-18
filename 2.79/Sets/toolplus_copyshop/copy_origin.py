# ##### BEGIN GPL LICENSE BLOCK #####
#
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


import bpy
from bpy import*
from bpy.props import *

import math, bmesh, mathutils,re


class View3D_TP_Origin_Plus_Z(bpy.types.Operator):  
    """place origin to top / +z axis""" 
    bl_idname = "tp_ops.origin_plus_z"  
    bl_label = "Origin to Top / +Z Axis"  
    bl_options = {"REGISTER", 'UNDO'}
  
    def draw(self, context):
        layout = self.layout.column(1)
                
        obj = context.active_object     
        if obj:
            obj_type = obj.type
                                                                  
            if obj_type in {'MESH'}: 
                box = layout.box().column(1)

                row = box.row(1)  
                row.label("done", icon ="INFO")

            else:
                box = layout.box().column(1)

                row = box.row(1)  
                row.label("only for mesh", icon ="INFO")            

    def execute(self, context):

        obj = context.active_object     
        if obj:
            obj_type = obj.type
                                                                  
            if obj_type in {'MESH'}: 
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

                for o in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = o 
                    
                    #o=bpy.context.active_object
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
                                     
                    bpy.ops.object.mode_set(mode = 'EDIT')
                    bpy.ops.object.editmode_toggle()        

        else:
            print(self)
            self.report({'INFO'}, "only Mesh")  
        
        return {'FINISHED'}


class View3D_TP_Origin_Minus_Z(bpy.types.Operator):  
    """place origin to bottom / -z axis""" 
    bl_idname = "tp_ops.origin_minus_z"  
    bl_label = "Origin to Bottom / -Z Axis"  
    bl_options = {"REGISTER", 'UNDO'}
      
    def draw(self, context):
        layout = self.layout.column(1)
                
        obj = context.active_object     
        if obj:
            obj_type = obj.type
                                                                  
            if obj_type in {'MESH'}: 
                box = layout.box().column(1)

                row = box.row(1)  
                row.label("done", icon ="INFO")

            else:
                box = layout.box().column(1)

                row = box.row(1)  
                row.label("only for mesh", icon ="INFO")            


    def execute(self, context):
 
        obj = context.active_object     
        if obj:
            obj_type = obj.type
                                                                  
            if obj_type in {'MESH'}: 
                
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob
                     
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

                for o in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = o
                    
                    #o=bpy.context.active_object
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
                    bpy.ops.object.mode_set(mode = 'EDIT')
                    bpy.ops.object.editmode_toggle()

        else:
            print(self)
            self.report({'INFO'}, "only Mesh")  

        return {'FINISHED'}




def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()







