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


from os.path import dirname
from .. import mods_keymap

class View3D_TP_KeyMap_Modifier(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_modifier"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = mods_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}



class VIEW3D_TP_FAKE_OPS(bpy.types.Operator):
    """do nothing"""
    bl_idname = "tp_ops.fake_ops"
    bl_label = "Do Nothing"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print
        return {'FINISHED'}



class Modifier_Apply(bpy.types.Operator):
    '''apply modifiers'''
    bl_idname = "tp_ops.apply_mod"
    bl_label = "Apply All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            if context.mode == 'OBJECT':
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
            
            elif context.mode == 'SCULPT':
                oldmode = bpy.context.mode
                bpy.ops.object.mode_set(mode='OBJECT')
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)                               
                bpy.ops.object.mode_set(mode=oldmode)

            else:
                bpy.ops.object.editmode_toggle()
               
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)               
                bpy.ops.object.editmode_toggle()       

        return {"FINISHED"}


    
class Modifier_Remove(bpy.types.Operator):
    '''remove modifiers'''
    bl_idname = "tp_ops.remove_mod"
    bl_label = "Remove All"
    bl_options = {'REGISTER', 'UNDO'}
            
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
                                
            if context.mode == 'OBJECT':
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_remove(modifier=mod.name)
            
            elif context.mode == 'SCULPT':
                oldmode = bpy.context.mode
                bpy.ops.object.mode_set(mode='OBJECT')
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_remove(modifier=mod.name)                              
                bpy.ops.object.mode_set(mode=oldmode)
           
            else:
                bpy.ops.object.editmode_toggle()
               
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_remove(modifier=mod.name)               
                bpy.ops.object.editmode_toggle()       

        return {"FINISHED"}


class Expand_Mod_Stack(bpy.types.Operator):
    '''Expand all modifier stack'''
    bl_idname = "tp_ops.expand_mod"
    bl_label = "Expand"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
          
        if not(bpy.context.selected_objects): 
            for obj in bpy.data.objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = True
        else:
            for obj in bpy.context.selected_objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = True

        return {'FINISHED'}



class Collapse_Mod_Stack(bpy.types.Operator):
    '''Collapse all modifier stack'''
    bl_idname = "tp_ops.collapse_mod"
    bl_label = "Collapse"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if not(bpy.context.selected_objects): 
            for obj in bpy.data.objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = False
        else:
            for obj in bpy.context.selected_objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = False
                    
        return {'FINISHED'}
    

    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()