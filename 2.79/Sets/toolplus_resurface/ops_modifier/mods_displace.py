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

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class VIEW3D_TP_Apply_Modifier_Displace(bpy.types.Operator):
    """apply modifier displace"""
    bl_idname = "tp_ops.apply_mods_displace"
    bl_label = "Apply Displace Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        is_select, is_mod = False, False
        message_a = ""

        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        for obj in selected:
            is_select = True
            
            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()    
  
                for modifier in obj.modifiers:
                    is_mod = True    
                    if (modifier.type == 'DISPLACE'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace.003")
                            
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  
                  
                for modifier in obj.modifiers:
                    is_mod = True    
                    if (modifier.type == 'DISPLACE'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Displace.003")
     
                if not context.active_object.mode == 'SCULPT':
                    bpy.ops.object.mode_set(mode=oldmode) 
                else:
                    bpy.ops.sculpt.sculptmode_toggle()

        if is_select:
            if is_mod:
                message_a = "removing only displace modifier"
            else:
                message_a = "no modifier on selected object"
        else:
            self.report(type={"INFO"}, message="No Selection. No changes applied")
        return {'CANCELLED'}

        self.report(type={"INFO"}, message=message_a)

        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Displace(bpy.types.Operator):
    """remove modifier displace"""
    bl_idname = "tp_ops.remove_mods_displace"
    bl_label = "Remove Decimate Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'DISPLACE'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'DISPLACE'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}



class VIEW3D_TP_Modifier_Displace(bpy.types.Operator):
    """Add a displace modifier"""
    bl_idname = "tp_ops.mod_displace"
    bl_label = "Decimate"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
           
            getmod = bpy.context.object.modifiers.get("Displace")   
            if not getmod:               
                object.modifier_add(type = "DISPLACE")
            
        return {'FINISHED'}   












# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
