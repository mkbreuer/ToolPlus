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
from bpy import*
from bpy.props import *

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class VIEW3D_TP_Apply_Modifier_Subsurf(bpy.types.Operator):
    """apply modifier subsurf"""
    bl_idname = "tp_ops.apply_mods_subsurf"
    bl_label = "Apply Subsurf Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        for obj in selected:
 
            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()  

                for modifier in obj.modifiers:    
                    if (modifier.type == 'SUBSURF'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.003")
                             
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  

                for modifier in obj.modifiers:    
                    if (modifier.type == 'SUBSURF'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.003")
           
                bpy.ops.object.mode_set(mode=oldmode) 
                                       
        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Subsurf(bpy.types.Operator):
    """remove modifier subsurf"""
    bl_idname = "tp_ops.remove_mods_subsurf"
    bl_label = "Remove Subsurf Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'SUBSURF'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SUBSURF'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}
        


 
 
#    "name": "Subsurf Level from Display Tools",
#    "author": "Jordi Vall-llovera Medina, Jhon Wallace",       
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

