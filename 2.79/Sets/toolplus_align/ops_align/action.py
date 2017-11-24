# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****

import bpy
from bpy import *
from bpy.props import *
import addon_utils



class VIEW3D_TP_Looptools(bpy.types.Operator):
   """enable looptools (save user settings be required for a permant activation)"""
   bl_label = "Looptools"
   bl_idname = "tp_ops.enable_looptools"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        loop_tools_addon = "mesh_looptools"
        state = addon_utils.check(loop_tools_addon)
        if not state[0]:
            bpy.ops.wm.addon_enable(module=loop_tools_addon)
            print(self)
            self.report({'INFO'}, "LoopTools activated!") 

        return {'FINISHED'}



class VIEW3D_TP_AutoMirror(bpy.types.Operator):
   """enable automirror (save user settings be required for a permant activation)"""
   bl_label = "AutoMirror"
   bl_idname = "tp_ops.enable_automirror"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        auto_mirror_addon = "mesh_auto_mirror"
        state = addon_utils.check(auto_mirror_addon)
        if not state[0]:
            bpy.ops.wm.addon_enable(module=auto_mirror_addon)
            print(self)
            self.report({'INFO'}, "AutoMirror activated!") 

        return {'FINISHED'}



class View3D_TP_Apply_Modifier_Mirror(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mods_mirror"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'MIRROR'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")

                        
        return {'FINISHED'}



class View3D_TP_Apply_Modifier_Mirror_EDM(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mods_mirror_edm"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'MIRROR'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
        return {'FINISHED'}



class View3D_TP_Remove_Modifier_Mirror(bpy.types.Operator):
    """remove modifier mirror"""
    bl_idname = "tp_ops.remove_mods_mirror"
    bl_label = "Remove Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'MIRROR'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'MIRROR'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}




# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()


