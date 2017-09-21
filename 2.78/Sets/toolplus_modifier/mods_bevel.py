__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *

class VIEW3D_TP_Apply_Modifier_Bevel(bpy.types.Operator):
    """apply modifier bevel"""
    bl_idname = "tp_ops.apply_mods_bevel"
    bl_label = "Apply Bevel Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'BEVEL'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel.003")
                        
        return {'FINISHED'}




class VIEW3D_TP_Apply_Modifier_Bevel_EDM(bpy.types.Operator):
    """apply modifier bevel"""
    bl_idname = "tp_ops.apply_mods_bevel_edm"
    bl_label = "Apply Bevel Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'BEVEL'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
        return {'FINISHED'}




class VIEW3D_TP_Remove_Modifier_Bevel(bpy.types.Operator):
    """remove modifier bevel"""
    bl_idname = "tp_ops.remove_mods_bevel"
    bl_label = "Remove Bevel Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'BEVEL'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'BEVEL'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}


class VIEW3D_TP_Bevel(bpy.types.Operator):
    bl_label = 'Bevel '
    bl_idname = 'tp_ops.mods_bevel'
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "BEVEL")
            
            for mod in obj.modifiers: 
               
                if mod.type == "BEVEL":
                    
                    bpy.context.object.modifiers["Bevel"].width = 0.2
                    bpy.context.object.modifiers["Bevel"].segments = 2
                    bpy.context.object.modifiers["Bevel"].profile = 1
                    bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
                    bpy.context.object.modifiers["Bevel"].angle_limit = 0.7   
     
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
            
            object.modifier_add(type = "SOLIDIFY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "SOLIDIFY":
                    bpy.context.object.modifiers["Solidify"].thickness = 0.25
                    bpy.context.object.modifiers["Solidify"].use_even_offset = True
     
        return {'FINISHED'}


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
    

    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


