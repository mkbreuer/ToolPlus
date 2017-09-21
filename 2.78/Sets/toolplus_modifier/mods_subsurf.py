__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *

class VIEW3D_TP_Apply_Modifier_Subsurf(bpy.types.Operator):
    """apply modifier subsurf"""
    bl_idname = "tp_ops.apply_mods_subsurf"
    bl_label = "Apply Subsurf Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'SUBSURF'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.003")
                        
        return {'FINISHED'}




class VIEW3D_TP_Apply_Modifier_Subsurf_EDM(bpy.types.Operator):
    """apply modifier subsurf"""
    bl_idname = "tp_ops.apply_mods_subsurf_edm"
    bl_label = "Apply Subsurf Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'SUBSURF'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
        return {'FINISHED'}




class VIEW3D_TP_Remove_Modifier_Subsurf(bpy.types.Operator):
    """remove modifier subsurf"""
    bl_idname = "tp_ops.remove_mods_subsurf"
    bl_label = "Remove Subsurf Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'SUBSURF'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'SUBSURF'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}
        

    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


