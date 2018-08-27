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

class VIEW3D_TP_Apply_Modifier_Array(bpy.types.Operator):
    """apply modifier array"""
    bl_idname = "tp_ops.apply_mods_array"
    bl_label = "Apply Array Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    tp_axis = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"All"  ,"04")],
               name = "Apply Array",
               default = "tp_a",    
               description = "apply modifier array")


    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        row = box.row()
        row.prop(self, 'tp_axis', expand=True)
        
        box.separator()


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
                    if (modifier.type == 'ARRAY'):
                        is_mod = True     
                                        
                        if self.tp_axis == "tp_x": 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_X")
                        
                        if self.tp_axis == "tp_y":  
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Y")
                      
                        if self.tp_axis == "tp_z": 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Z")

                        if self.tp_axis == "tp_a": 

                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_X")
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Y")
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Z")
                             
 
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode
                bpy.ops.object.mode_set(mode='OBJECT')   
                                  
                for modifier in obj.modifiers:                   
                    if (modifier.type == 'ARRAY'):
                        is_mod = True     
                                        
                        if self.tp_axis == "tp_x": 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_X")
                        
                        if self.tp_axis == "tp_y":  
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Y")
                      
                        if self.tp_axis == "tp_z": 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Z")

                        if self.tp_axis == "tp_a": 

                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_X")
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Y")
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array_Z")
 
                bpy.ops.object.mode_set(mode=oldmode)      
            


        if is_select:
            if is_mod:
                message_a = "removing only array modifier"
            else:
                message_a = "no modifier on selected object"
        else:
            self.report(type={"INFO"}, message="No Selection. No changes applied")
        return {'CANCELLED'}

        self.report(type={"INFO"}, message=message_a)

        return {'FINISHED'} 


    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)



class VIEW3D_TP_Remove_Modifier_Array(bpy.types.Operator):
    """remove modifier array"""
    bl_idname = "tp_ops.remove_mods_array"
    bl_label = "Remove Array Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    tp_axis = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"All"  ,"04")],
               name = "Remove Array",
               default = "tp_a",    
               description = "remove modifier array")


    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        row = box.row()
        row.prop(self, 'tp_axis', expand=True)
        
        box.separator()


    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        oldmode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'ARRAY'):
                   
                    if self.tp_axis == "tp_x": 
                        bpy.ops.object.modifier_remove(modifier="Array_X")
                    
                    if self.tp_axis == "tp_y":  
                        bpy.ops.object.modifier_remove(modifier="Array_Y")
                  
                    if self.tp_axis == "tp_z": 
                        bpy.ops.object.modifier_remove(modifier="Array_Z")

                    if self.tp_axis == "tp_a": 
                        
                        bpy.ops.tp_ops.remove_mods_array()

        bpy.ops.object.mode_set(mode=oldmode)
        return {'FINISHED'}

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)




class VIEW3D_TP_Remove_Modifier_Array(bpy.types.Operator):
    """remove modifier array"""
    bl_idname = "tp_ops.remove_mods_array"
    bl_label = "Remove Array Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'ARRAY'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'ARRAY'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}






class VIEW3D_TP_X_Array(bpy.types.Operator):
    bl_label = 'X Array'
    bl_idname = 'tp_ops.x_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            bpy.context.object.modifiers["Array"].name = "Array_X"  
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY":
                          
                    bpy.context.object.modifiers["Array_X"].count = 5
                    bpy.context.object.modifiers["Array_X"].relative_offset_displace[0] = 1
                    bpy.context.object.modifiers["Array_X"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array_X"].relative_offset_displace[2] = 0                 
                    bpy.context.object.modifiers["Array_X"].use_merge_vertices = True
                    bpy.context.object.modifiers["Array_X"].use_merge_vertices_cap = True

        return {'FINISHED'}


class VIEW3D_TP_Y_Array(bpy.types.Operator):
    bl_label = 'Y Array'
    bl_idname = 'tp_ops.y_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            bpy.context.object.modifiers["Array"].name = "Array_Y"  
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY":  
                    bpy.context.object.modifiers["Array_Y"].count = 5
                    bpy.context.object.modifiers["Array_Y"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array_Y"].relative_offset_displace[1] = 1
                    bpy.context.object.modifiers["Array_Y"].relative_offset_displace[2] = 0  
                    bpy.context.object.modifiers["Array_Y"].use_merge_vertices = True
                    bpy.context.object.modifiers["Array_Y"].use_merge_vertices_cap = True
                                 
        return {'FINISHED'}


class VIEW3D_TP_Z_Array(bpy.types.Operator):
    bl_label = 'Z Array'
    bl_idname = 'tp_ops.z_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            bpy.context.object.modifiers["Array"].name = "Array_Z" 
                        
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY":                      
                    bpy.context.object.modifiers["Array_Z"].count = 5
                    bpy.context.object.modifiers["Array_Z"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array_Z"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array_Z"].relative_offset_displace[2] = 1   
                    bpy.context.object.modifiers["Array_Z"].use_merge_vertices = True
                    bpy.context.object.modifiers["Array_Z"].use_merge_vertices_cap = True                    
      
        return {'FINISHED'}



class VIEW3D_TP_XY_Array(bpy.types.Operator):
    bl_label = 'XY Array'
    bl_idname = 'tp_ops.xy_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY":          

                    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1
                    bpy.context.object.modifiers["Array"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array"].relative_offset_displace[2] = 0        
                    bpy.context.object.modifiers["Array"].count = 5

            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 

                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[2] = 0
        
        return {'FINISHED'}


class VIEW3D_TP_XZ_Array(bpy.types.Operator):
    bl_label = 'XZ Array'
    bl_idname = 'tp_ops.xz_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1
                    bpy.context.object.modifiers["Array"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array"].relative_offset_displace[2] = 0        
                    bpy.context.object.modifiers["Array"].count = 5
            
            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[2] = 1

        return {'FINISHED'}


class VIEW3D_TP_YZ_Array(bpy.types.Operator):
    bl_label = 'YZ Array'
    bl_idname = 'tp_ops.yz_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array"].relative_offset_displace[1] = 1
                    bpy.context.object.modifiers["Array"].relative_offset_displace[2] = 0

            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[2] = 1
           
        return {'FINISHED'}


class VIEW3D_TP_XYZ_Array(bpy.types.Operator):
    bl_label = 'XYZ Array'
    bl_idname = 'tp_ops.xyz_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 
        
        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1
                    bpy.context.object.modifiers["Array"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array"].relative_offset_displace[2] = 0
                    bpy.context.object.modifiers["Array"].count = 5

            
            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1
                    bpy.context.object.modifiers["Array.001"].relative_offset_displace[2] = 0

            object.modifier_add(type = "ARRAY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "ARRAY": 
                    bpy.context.object.modifiers["Array.002"].relative_offset_displace[0] = 0
                    bpy.context.object.modifiers["Array.002"].relative_offset_displace[1] = 0
                    bpy.context.object.modifiers["Array.002"].relative_offset_displace[2] = 1

        return {'FINISHED'}


    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()