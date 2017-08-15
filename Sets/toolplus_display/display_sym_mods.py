__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import*
from bpy.props import *

bpy.types.Scene.tp_sculpt = bpy.props.BoolProperty(name="SculptToggle", description="switch to or stay in sculptmode", default=False)  


class VIEW3D_TP_Apply_Mirror_Modifier(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mod_mirror"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        is_select, is_mod = False, False
        message_a = ""


        if bpy.context.mode == 'OBJECT':       

            bpy.ops.object.mode_set(mode = 'OBJECT')
            
            selected = bpy.context.selected_objects 
            for obj in selected:
                is_select = True
                
                for modifier in obj.modifiers:
                    is_mod = True    
                    if (modifier.type == 'MIRROR'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")

        else:       

            bpy.ops.object.mode_set(mode = 'OBJECT')
            
            selected = bpy.context.selected_objects 
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'MIRROR'):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")


            if not bpy.context.scene.tp_sculpt:
                bpy.ops.object.mode_set(mode="EDIT")
            else:
                bpy.ops.sculpt.sculptmode_toggle() 


        if is_select:
            if is_mod:
                message_a = "removing only mirror modifier"
            else:
                message_a = "no modifier on selected object"
        else:
            self.report(type={"INFO"}, message="No Selection. No changes applied")
        return {'CANCELLED'}

        self.report(type={"INFO"}, message=message_a)
        return {'FINISHED'}



class VIEW3D_TP_Remove_Modifier_Mirror(bpy.types.Operator):
    """remove modifier mirror"""
    bl_idname = "tp_ops.remove_mod_mirror"
    bl_label = "Remove Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'MIRROR'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'MIRROR'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}


    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


