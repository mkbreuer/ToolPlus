import bpy, bmesh, os
from bpy import*
from bpy.props import *

  
class View3D_TP_Modifier_On(bpy.types.Operator):
    '''Display modifier in viewport'''
    bl_idname = "tp_ops.modifier_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:        
                for mod in obj.modifiers:
                    mod.show_viewport = True
        else:
            for obj in selection:        
                for mod in obj.modifiers:
                    mod.show_viewport = True
        return {'FINISHED'}
    


class View3D_TP_Modifier_Off(bpy.types.Operator):
    '''Hide modifier in viewport'''
    bl_idname = "tp_ops.modifier_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:        
                for mod in obj.modifiers:
                    mod.show_viewport = False
        else:
            for obj in selection:        
                for mod in obj.modifiers:
                    mod.show_viewport = False
        return {'FINISHED'}



class View3D_TP_Modifier_Apply(bpy.types.Operator):
    '''apply all modifier'''
    bl_idname = "tp_ops.apply_mod"
    bl_label = "Apply All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            

            if context.mode == 'OBJECT':
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
            else:
                bpy.ops.object.editmode_toggle()
               
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
               
                bpy.ops.object.editmode_toggle()       

        return {"FINISHED"}


class View3D_TP_Modifier_Remove(bpy.types.Operator):
    '''remove all modifier'''
    bl_idname = "tp_ops.remove_mod"
    bl_label = "Remove All"
    bl_options = {'REGISTER', 'UNDO'}
            
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
                                
            if context.mode == 'OBJECT':
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_remove(modifier=mod.name)
            else:
                bpy.ops.object.editmode_toggle()
               
                for obj in bpy.data.objects:
                   for mod in obj.modifiers:
                        bpy.ops.object.modifier_remove(modifier=mod.name)
               
                bpy.ops.object.editmode_toggle()       

        return {"FINISHED"}

    

def register():    
    bpy.utils.register_module(__name__)

def unregister():  
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()