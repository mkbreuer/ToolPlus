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

bpy.types.Scene.tp_apply_remesh = bpy.props.BoolProperty(name="SculptToggle", description="switch to or stay in sculptmode", default=False)  

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class VIEW3D_TP_Apply_Modifier_Remesh(bpy.types.Operator):
    """apply modifier remesh"""
    bl_idname = "tp_ops.apply_mods_remesh"
    bl_label = "Apply Remesh Modifier"
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
                    if (modifier.type == 'REMESH'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh.003")

                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  
                
                for modifier in obj.modifiers:
                    is_mod = True    
                    if (modifier.type == 'REMESH'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh.003")


                if not context.active_object.mode == 'SCULPT':
                    bpy.ops.object.mode_set(mode=oldmode) 
                else:
                    bpy.ops.sculpt.sculptmode_toggle()
              
        if is_select:
            if is_mod:
                message_a = "removing only remesh modifier"
            else:
                message_a = "no modifier on selected object"
        else:
            self.report(type={"INFO"}, message="No Selection. No changes applied")
        return {'CANCELLED'}

        self.report(type={"INFO"}, message=message_a)

        return {'FINISHED'}




class VIEW3D_TP_Remove_Modifier_Remesh(bpy.types.Operator):
    """remove modifier remesh"""
    bl_idname = "tp_ops.remove_mods_remesh"
    bl_label = "Remove Remesh Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'REMESH'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'REMESH'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}




class VIEW3D_TP_Modifier_Remesh(bpy.types.Operator):
    """Add a remesh modifier"""
    bl_idname = "tp_ops.mod_remesh"
    bl_label = "Remesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            remesh = bpy.context.object.modifiers.get("Remesh")   
            if not remesh :   

                object.modifier_add(type = "REMESH")
                bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
                bpy.context.object.modifiers["Remesh"].use_smooth_shade = True

        return {'FINISHED'}   



class VIEW3D_TP_Modifier_Smooth_Remesh(bpy.types.Operator):
    """Add a remesh and smooth modifier"""
    bl_idname = "tp_ops.smooth_remesh"
    bl_label = "Smooth Remesh"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')
      
        remesh = bpy.context.object.modifiers.get("Remesh")   
        if not remesh :   
   
            bpy.ops.object.modifier_add(type='REMESH')
            bpy.context.object.modifiers["Remesh"].octree_depth = 7
            bpy.context.object.modifiers["Remesh"].use_smooth_shade = True

        smooth = bpy.context.object.modifiers.get("Smooth")   
        if not smooth :  
           
            bpy.ops.object.modifier_add(type='SMOOTH')
            bpy.context.object.modifiers["Smooth"].factor = 1
            bpy.context.object.modifiers["Smooth"].iterations = 10
        
        bpy.ops.object.mode_set(mode=oldmode)
        return {"FINISHED"}



EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

class VIEW3D_TP_Apply_Modifier_Smoth_Remesh(bpy.types.Operator):
    """apply modifier smooth remesh"""
    bl_idname = "tp_ops.apply_smooth_remesh"
    bl_label = "Apply Remesh Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        oldmode = bpy.context.mode
        
        for obj in selected:

            if context.mode in EDIT:
                bpy.ops.object.editmode_toggle()  
                  
                for modifier in obj.modifiers:
                    is_mod = True    
                    if (modifier.type == 'REMESH'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")
             
                for modifier in obj.modifiers:
                    is_mod = True                            
                    if (modifier.type == 'SMOOTH'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")

                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  
                
                for modifier in obj.modifiers:
                    is_mod = True    
                    if (modifier.type == 'REMESH'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")
             
                for modifier in obj.modifiers:
                    is_mod = True                            
                    if (modifier.type == 'SMOOTH'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")

                if not context.active_object.mode == 'SCULPT':
                    bpy.ops.object.mode_set(mode=oldmode) 
                else:
                    bpy.ops.sculpt.sculptmode_toggle()
            
        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Smooth_Remesh(bpy.types.Operator):
    """remove smooth remesh"""
    bl_idname = "tp_ops.remove_smooth_remesh"
    bl_label = "Remove Smooth Remesh Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'REMESH'):
                        obj.modifiers.remove(modifier)
               
                for modifier in obj.modifiers:                    
                    if (modifier.type == 'SMOOTH'):
                        obj.modifiers.remove(modifier)
        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'REMESH'):
                        obj.modifiers.remove(modifier)
            
                for modifier in obj.modifiers:                    
                    if (modifier.type == 'SMOOTH'):
                        obj.modifiers.remove(modifier)                        

        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
