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
  
class VIEW3D_TP_Apply_Modifier_SimpleDeform(bpy.types.Operator):
    """apply modifier sdeform"""
    bl_idname = "tp_ops.apply_mods_sdeform"
    bl_label = "Apply SimpleDeform Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 

        for obj in selected:

            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()  
            
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SIMPLE_DEFORM'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.003")
                  
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  
            
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SIMPLE_DEFORM'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.003")

                bpy.ops.object.mode_set(mode=oldmode)  
                                      
        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_SimpleDeform(bpy.types.Operator):
    """remove modifier sdeform"""
    bl_idname = "tp_ops.remove_mods_sdeform"
    bl_label = "Remove SimpleDeform Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'SIMPLE_DEFORM'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SIMPLE_DEFORM'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}
        


class VIEW3D_TP_SDeform_Mod_Mirror(bpy.types.Operator):
    """Add a simple deform modifier"""
    bl_idname = "tp_ops.mod_sdeform"
    bl_label = "Simple Deform"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        for obj in selected: 
            scene.objects.active = obj 
            
            sdeform = bpy.context.object.modifiers.get("SimpleDeform")   
            if not sdeform:               
               
                object.modifier_add(type = "SIMPLE_DEFORM")
  
        bpy.ops.object.mode_set(mode=oldmode)   
        return {'FINISHED'}   



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()