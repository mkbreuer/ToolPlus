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
#

# -*- coding: utf-8 -*-

#bl_info = {  
 #    "name": "Circle Array",  
  #   "author": "Antonis Karvelas",  
   #  "version": (1, 0),  
    # "blender": (2, 6, 7),  
     #"location": "View3D > Object > Circle_Array",  
     #"description": "Uses an existing array and creates an empty,rotates it properly and makes a Circle Array ",  
     #"warning": "You must have an object and an array, or two objects, with only the first having an array",  
     #"wiki_url": "",  
     #"tracker_url": "",  
     #"category": ""}  

import bpy
from math import radians
    
class Circle_ArrayA(bpy.types.Operator):
    """add an empty with array modifier / Z axis"""
    bl_label = "1/4 Circle Array"
    bl_idname = "objects.circle_array_operator1"   
    
    def execute(self, context):
        
       
        for obj in bpy.context.selected_objects:
	        
            bpy.context.scene.objects.active = obj
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array"].count = 4
            
           
        if len(bpy.context.selected_objects) == 2:
            list = bpy.context.selected_objects
            active = list[0]
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            active.select = False
            bpy.context.scene.objects.active = list[0]
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object                
            bpy.context.scene.objects.active = active            
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            return {'FINISHED'}     
        
        
        else:
            active = context.active_object
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object
            bpy.context.scene.objects.active = active
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            return {'FINISHED'} 



class ObjectCursorArray(bpy.types.Operator):
    """Array the active object to the cursor location"""
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        for i in range(self.total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event) 
    





class Circle_ArrayB(bpy.types.Operator):
    """add an empty with array modifier to cursor / Z axis"""
    bl_label = "1/6 Circle Array"
    bl_idname = "objects.circle_array_operator2"   
    
    def execute(self, context):

        for obj in bpy.context.selected_objects:
	        
            bpy.context.scene.objects.active = obj
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array"].count = 6            
           
        if len(bpy.context.selected_objects) == 2:
            list = bpy.context.selected_objects
            active = list[0]
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            active.select = False
            bpy.context.scene.objects.active = list[0]
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object                
            bpy.context.scene.objects.active = active            
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            return {'FINISHED'}             
        
        else:
            active = context.active_object
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object
            bpy.context.scene.objects.active = active
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            return {'FINISHED'} 


class Circle_ArrayC(bpy.types.Operator):
    """add an empty with array modifier to cursor / Z axis"""
    bl_label = "1/8 Circle Array"
    bl_idname = "objects.circle_array_operator3"   
    
    def execute(self, context):

        for obj in bpy.context.selected_objects:
	        
            bpy.context.scene.objects.active = obj
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array"].count = 8   
           
        if len(bpy.context.selected_objects) == 2:
            list = bpy.context.selected_objects
            active = list[0]
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            active.select = False
            bpy.context.scene.objects.active = list[0]
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object                
            bpy.context.scene.objects.active = active            
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            return {'FINISHED'}             
        
        else:
            active = context.active_object
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object
            bpy.context.scene.objects.active = active
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            
            
            

class Circle_ArrayD(bpy.types.Operator):
    """add an empty with array modifier to cursor / Z axis"""
    bl_label = "1/12 Circle Array"
    bl_idname = "objects.circle_array_operator4"   
    
    def execute(self, context):        
       
        for obj in bpy.context.selected_objects:
	        
            bpy.context.scene.objects.active = obj
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array"].count = 12            
           
        if len(bpy.context.selected_objects) == 2:
            list = bpy.context.selected_objects
            active = list[0]
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            active.select = False
            bpy.context.scene.objects.active = list[0]
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object                
            bpy.context.scene.objects.active = active            
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            return {'FINISHED'}             
        
        else:
            active = context.active_object
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object
            bpy.context.scene.objects.active = active
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            return {'FINISHED'}         
  

def register():

    bpy.utils.register_class(Circle_ArrayA)
    bpy.utils.register_class(Circle_ArrayB)
    bpy.utils.register_class(Circle_ArrayC)
    bpy.utils.register_class(Circle_ArrayD)

    
if __name__ == "__main__":
    register() 

