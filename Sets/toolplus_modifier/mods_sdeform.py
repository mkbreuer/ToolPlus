__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *

class VIEW3D_TP_Apply_Modifier_SimpleDeform(bpy.types.Operator):
    """apply modifier sdeform"""
    bl_idname = "tp_ops.apply_mods_sdeform"
    bl_label = "Apply SimpleDeform Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'SIMPLE_DEFORM'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.003")
                        
        return {'FINISHED'}




class VIEW3D_TP_Apply_Modifier_SimpleDeform_EDM(bpy.types.Operator):
    """apply modifier sdeform"""
    bl_idname = "tp_ops.apply_mods_sdeform_edm"
    bl_label = "Apply SimpleDeform Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'SIMPLE_DEFORM'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="SimpleDeform.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
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

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "SIMPLE_DEFORM")


        return {'FINISHED'}   

    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


