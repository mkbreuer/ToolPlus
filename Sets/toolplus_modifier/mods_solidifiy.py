__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *

class VIEW3D_TP_Apply_Modifier_Solidify(bpy.types.Operator):
    """apply modifier solidify"""
    bl_idname = "tp_ops.apply_mods_solidify"
    bl_label = "Apply Solidify Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'SOLIDIFY'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.003")
                        
        return {'FINISHED'}




class VIEW3D_TP_Apply_Modifier_Solidify_EDM(bpy.types.Operator):
    """apply modifier solidify"""
    bl_idname = "tp_ops.apply_mods_solidify_edm"
    bl_label = "Apply Solidify Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'SOLIDIFY'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
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
            
            object.modifier_add(type = "SOLIDIFY")
            
            for mod in obj.modifiers: 
               
                if mod.type == "SOLIDIFY":
                    bpy.context.object.modifiers["Solidify"].thickness = 0.25
                    bpy.context.object.modifiers["Solidify"].use_even_offset = True
     
        return {'FINISHED'}


    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


