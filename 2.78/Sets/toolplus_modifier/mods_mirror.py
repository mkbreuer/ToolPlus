__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *



class VIEW3D_TP_Apply_Modifier_Mirror(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mods_mirror"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        is_select, is_mod = False, False
        message_a = ""

        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            is_select = True
            
            for modifier in obj.modifiers:
                is_mod = True    
                if (modifier.type == 'MIRROR'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")
                        

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




class VIEW3D_TP_Apply_Modifier_Mirror_EDM(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mods_mirror_edm"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'MIRROR'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
        return {'FINISHED'}




class VIEW3D_TP_Remove_Modifier_Mirror(bpy.types.Operator):
    """remove modifier mirror"""
    bl_idname = "tp_ops.remove_mods_mirror"
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




class VIEW3D_TP_X_Mod_Mirror(bpy.types.Operator):
    """Add a x mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_x"
    bl_label = "Mirror X"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                         
                    bpy.context.object.modifiers["Mirror"].use_x = True
                    bpy.context.object.modifiers["Mirror"].use_y = False
                    bpy.context.object.modifiers["Mirror"].use_z = False          
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    

class VIEW3D_TP_Y_Mod_Mirror(bpy.types.Operator):
    """Add a y mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_y"
    bl_label = "Mirror Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                    
                    bpy.context.object.modifiers["Mirror"].use_x = False
                    bpy.context.object.modifiers["Mirror"].use_y = True
                    bpy.context.object.modifiers["Mirror"].use_z = False  
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    

class VIEW3D_TP_Z_Mod_Mirror(bpy.types.Operator):
    """Add a z mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_z"
    bl_label = "Mirror Z"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                    
                    bpy.context.object.modifiers["Mirror"].use_x = False
                    bpy.context.object.modifiers["Mirror"].use_y = False
                    bpy.context.object.modifiers["Mirror"].use_z = True         
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}   


class VIEW3D_TP_XY_Mod_Mirror(bpy.types.Operator):
    """Add a xy mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_xy"
    bl_label = "Mirror XY"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                    
                    bpy.context.object.modifiers["Mirror"].use_x = True
                    bpy.context.object.modifiers["Mirror"].use_y = True
                    bpy.context.object.modifiers["Mirror"].use_z = False           
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}


class VIEW3D_TP_Yz_Mod_Mirror(bpy.types.Operator):
    """Add a yz mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_yz"
    bl_label = "Mirror Yz"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                    
                    bpy.context.object.modifiers["Mirror"].use_x = False
                    bpy.context.object.modifiers["Mirror"].use_y = True
                    bpy.context.object.modifiers["Mirror"].use_z = True     
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    

class VIEW3D_TP_Xz_Mod_Mirror(bpy.types.Operator):
    """Add a xz mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_xz"
    bl_label = "Mirror Xz"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                    
                    bpy.context.object.modifiers["Mirror"].use_x = True
                    bpy.context.object.modifiers["Mirror"].use_y = False
                    bpy.context.object.modifiers["Mirror"].use_z = True         
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}   
    

class VIEW3D_TP_XYZ_Mod_Mirror(bpy.types.Operator):
    """Add a xyz mirror modifier with cage and clipping"""
    bl_idname = "tp_ops.mod_mirror_xyz"
    bl_label = "Mirror XYZ"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                    
                    bpy.context.object.modifiers["Mirror"].use_x = True
                    bpy.context.object.modifiers["Mirror"].use_y = True
                    bpy.context.object.modifiers["Mirror"].use_z = True         
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}   



    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


