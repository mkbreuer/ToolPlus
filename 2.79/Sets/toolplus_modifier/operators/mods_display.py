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


#bl_info = {
#    "name": "Display Tools",
#    "author": "Jordi Vall-llovera Medina, Jhon Wallace",
#    "version": (1, 6, 0),
#    "blender": (2, 7, 0),
#    "location": "Toolshelf",
#    "description": "Display tools for fast navigate/interact with the viewport",
#    "warning": "",
#    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Display_Tools",
#    "tracker_url": "",
#    "category": "User Changed"}
#
#    Author Site: http://www.jordiart.com

# LOAD MODUL #    
import bpy
from bpy import*
from bpy.props import *


class VIEW3D_TP_Display_DrawWire(bpy.types.Operator):
    """Draw Type Wire"""
    bl_idname = "tp_ops.draw_wire"
    bl_label = "Draw Type Wire"

    def execute(self, context):
        bpy.context.object.draw_type = 'WIRE'       
        return {'FINISHED'}


class VIEW3D_TP_Display_DrawSolid(bpy.types.Operator):
    """Draw Type Solid"""
    bl_idname = "tp_ops.draw_solid"
    bl_label = "Draw Type Solid"

    def execute(self, context):
        bpy.context.object.draw_type = 'SOLID'       
        return {'FINISHED'}


class VIEW3D_TP_Wire_All(bpy.types.Operator):
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
    


class VIEW3D_TP_Wire_On(bpy.types.Operator):
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


class VIEW3D_TP_Wire_Off(bpy.types.Operator):
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
    

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class VIEW3D_TP_Modifier_Apply_All(bpy.types.Operator):
    '''apply all modifiers'''
    bl_idname = "tp_ops.apply_mod_all"
    bl_label = "Apply All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 
        
        for obj in selected: 
            scene.objects.active = obj        
           
            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()  

                for obj in bpy.data.objects:
                    for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)                  
               
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  
              
                for obj in bpy.data.objects:
                    for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)                    
              
                bpy.ops.object.mode_set(mode=oldmode)    
             
        return {"FINISHED"}


    
class VIEW3D_TP_Modifier_Remove_All(bpy.types.Operator):
    '''remove all modifiers'''
    bl_idname = "tp_ops.remove_mod_all"
    bl_label = "Remove All"
    bl_options = {'REGISTER', 'UNDO'}
            
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for obj in selected: 
            scene.objects.active = obj 
            
            for obj in bpy.data.objects:
               for mod in obj.modifiers:
                    bpy.ops.object.modifier_remove(modifier=mod.name)    
        
        bpy.ops.object.mode_set(mode=oldmode)   
        return {"FINISHED"}
       



class ModifiersSubsurfLevel_0(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_0"
    bl_label = "0"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects  
        
        if not(selection):    
            for obj in bpy.data.objects:  
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 0
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
     
                    
        else:
            # get existing subsurf
            for obj in selection:  
                bpy.ops.object.subdivision_set(level=0, relative=False)  
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    mod.levels = 0

        return {'FINISHED'}
      
      
class ModifiersSubsurfLevel_1(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_1"
    bl_label = "1"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 

        if not(selection):    
            for obj in bpy.data.objects:  
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 1
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
        else:
            # get existing subsurf
            for obj in selection:  
                bpy.ops.object.subdivision_set(level=1, relative=False)       
                for mod in obj.modifiers:
                    if mod.type == 'SUBSURF':
                      mod.levels = 1

        return {'FINISHED'}
      
          
class ModifiersSubsurfLevel_2(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_2"
    bl_label = "2"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:  
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 2
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
        else:
            # get existing subsurf
            for obj in selection:        
                bpy.ops.object.subdivision_set(level=2, relative=False) 
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    mod.levels = 2
        return {'FINISHED'}

      
class ModifiersSubsurfLevel_3(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_3"
    bl_label = "3"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):   
            for obj in bpy.data.objects:   
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 3
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
        else:
            # get existing subsurf
            for obj in selection:          
                bpy.ops.object.subdivision_set(level=3, relative=False) 
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    mod.levels = 3
        return {'FINISHED'}
      
      
class ModifiersSubsurfLevel_4(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_4"
    bl_label = "4"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:  
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 4
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
        else:
            # get existing subsurf
            for obj in selection:        
                bpy.ops.object.subdivision_set(level=4, relative=False) 
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    mod.levels = 4
        return {'FINISHED'}
      
      
class ModifiersSubsurfLevel_5(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_5"
    bl_label = "5"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:  
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 5
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
        else:
            # get existing subsurf
            for obj in selection:        
                bpy.ops.object.subdivision_set(level=5, relative=False) 
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    mod.levels = 5
        return {'FINISHED'}
      
       
class ModifiersSubsurfLevel_6(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "tp_ops.subsurf_6"
    bl_label = "6"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):  
            for obj in bpy.data.objects:    
                bpy.context.scene.objects.active = obj 
                bpy.ops.object.modifier_add(type='SUBSURF')
                value = 0
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    value = value +1
                    mod.levels = 6
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="Subsurf")
        else:
            # get existing subsurf
            for obj in selection:        
                bpy.ops.object.subdivision_set(level=6, relative=False)    
                for mod in obj.modifiers:
                  if mod.type == 'SUBSURF':
                    mod.levels = 6
        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()