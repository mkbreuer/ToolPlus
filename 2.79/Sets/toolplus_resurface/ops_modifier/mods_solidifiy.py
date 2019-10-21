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

class VIEW3D_TP_Apply_Modifier_Solidify(bpy.types.Operator):
    """apply modifier solidify"""
    bl_idname = "tp_ops.apply_mods_solidify"
    bl_label = "Apply Solidify Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 

        for obj in selected:

            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()  

                for modifier in obj.modifiers:    
                    if (modifier.type == 'SOLIDIFY'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.003")
                       
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  

                for modifier in obj.modifiers:    
                    if (modifier.type == 'SOLIDIFY'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.003")
     
                bpy.ops.object.mode_set(mode=oldmode)    
                                    
        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Solidify(bpy.types.Operator):
    """remove modifier solidify"""
    bl_idname = "tp_ops.remove_mods_solidify"
    bl_label = "Remove Solidify Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'SOLIDIFY'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SOLIDIFY'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}
        


class VIEW3D_TP_Solidify(bpy.types.Operator):
    bl_label = 'Solidify'
    bl_idname = 'tp_ops.mods_solidify'
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 

            solidify = bpy.context.object.modifiers.get("Solidify")   
            if not solidify :   
            
                object.modifier_add(type = "SOLIDIFY")
                
                for mod in obj.modifiers: 
                   
                    if mod.type == "SOLIDIFY":
                        bpy.context.object.modifiers["Solidify"].thickness = 0.25
                        bpy.context.object.modifiers["Solidify"].use_even_offset = True
     
        return {'FINISHED'}


    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()