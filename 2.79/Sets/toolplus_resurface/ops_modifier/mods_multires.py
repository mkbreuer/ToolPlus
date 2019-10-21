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


# LISTS FOR SELECTION #
name_list = []
dummy_list = []

class VIEW3D_TP_ReCopy_Multires(bpy.types.Operator):
    """recopy multires"""
    bl_idname = "tp_ops.multires_recopy"
    bl_label = "ReCopy"
    bl_options = {'REGISTER', 'UNDO'}

    apply_all = bpy.props.BoolProperty(name="Apply MultiRes",  description="apply the multires modifier", default=False, options={'SKIP_SAVE'})    

    def execute(self, context):
        scene = bpy.context.scene 

        oldmode = bpy.context.mode   
 
        selected = bpy.context.selected_objects
        
        for obj in selected:
            # add source to name list
            name_list.append(obj.name)  
            
            bpy.ops.object.duplicate_move()
                                                 
            bpy.context.object.name = obj.name + "_sculpt"
            bpy.context.object.data.name = obj.name + "_sculpt"
            
            # add new object to dummy name list
            new_object_name = obj.name + "_sculpt"
            dummy_list.append(new_object_name)                 

            if self.apply_all == True:
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Multires")
       
            bpy.ops.object.hide_view_set(unselected=False)
            bpy.ops.object.select_all(action='DESELECT')

            # select objects in lists
            bpy.data.objects[new_object_name].select = False 
            
            bpy.context.scene.objects.active = bpy.data.objects[obj.name] 
            bpy.data.objects[obj.name].select = True

        bpy.ops.object.mode_set(mode=oldmode)
      
        return {'FINISHED'}

 
        
     
class VIEW3D_TP_Add_Modifier_Multires(bpy.types.Operator):
    """add modifier multires"""
    bl_idname = "tp_ops.multires_add"
    bl_label = "Multires"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = bpy.context.scene 

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')        
 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            multires = bpy.context.object.modifiers.get("Multires")   
            if not multires:   

                object.modifier_add(type = "MULTIRES")
                
                for mod in obj.modifiers: 
                   
                    if mod.type == "MULTIRES":
                        newLevels = 3
                        while newLevels > 0:
                            bpy.ops.object.multires_subdivide(modifier="Multires")
                            bpy.context.object.modifiers["Multires"].levels += 1 
                            newLevels -= 1
                            for x in range(20):
                                bpy.ops.object.modifier_move_up(modifier="Multires")            

        bpy.ops.object.shade_smooth()
        bpy.ops.object.mode_set(mode=oldmode)
      
        return {'FINISHED'}




class VIEW3D_TP_Multires_SubDiv(bpy.types.Operator):  
    """add new multires with deleted higher resolution"""  
    bl_idname = "tp_ops.multires_subdiv"  
    bl_label = "Reset"
    bl_options = {'REGISTER', 'UNDO'}
   
    mode = bpy.props.StringProperty(default="")    
   
    def execute(self, context):

        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')
                
        selected = bpy.context.selected_objects 
        for obj in selected: 
            for mod in obj.modifiers:    
                if mod.type == "MULTIRES":
                        
                    if "subdiv" in self.mode:
                        bpy.ops.object.multires_subdivide(modifier="Multires")
                        bpy.context.object.modifiers["Multires"].sculpt_levels += 1
                        bpy.context.object.modifiers["Multires"].render_levels = 3
                        bpy.context.object.modifiers["Multires"].levels = 3
                   
                    if "reset" in self.mode:
                        bpy.ops.object.modifier_remove(modifier="Multires")
                        bpy.ops.object.modifier_add(type='MULTIRES')
                        for x in range(20): 
                            bpy.ops.object.modifier_move_up(modifier="Multires")

        bpy.ops.object.mode_set(mode=oldmode)    

        return {'FINISHED'}


EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  
      
class VIEW3D_TP_Apply_Modifier_Multires(bpy.types.Operator):
    """apply modifier multires"""
    bl_idname = "tp_ops.apply_mods_multires"
    bl_label = "Apply Multires Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):

        if context.mode in EDIT:
            bpy.ops.object.editmode_toggle()    
            
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Multires")

            bpy.ops.object.editmode_toggle()   

        else:                   
            oldmode = bpy.context.mode                                 
            bpy.ops.object.mode_set(mode='OBJECT')
            
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Multires")
    
            if not context.active_object.mode == 'SCULPT':
                bpy.ops.object.mode_set(mode=oldmode) 
            else:
                bpy.ops.sculpt.sculptmode_toggle()

        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Multires(bpy.types.Operator):
    """remove modifier multires"""
    bl_idname = "tp_ops.remove_mods_multires"
    bl_label = "Remove Multires Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):

        oldmode = bpy.context.mode   
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        bpy.ops.object.modifier_remove(modifier="Multires")
                      
        bpy.ops.object.mode_set(mode=oldmode)  

        return {'FINISHED'}
        

    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
