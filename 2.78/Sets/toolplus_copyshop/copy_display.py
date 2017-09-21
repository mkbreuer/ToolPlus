
import bpy
from bpy import*
from bpy.props import*



class VIEW3D_TP_Normals(bpy.types.Operator):
    """Recalculate Normals for all selected Objects in Objectmode"""
    bl_idname = "tp_ops.rec_normals"
    bl_label = "Recalculate Normals"     

    def execute(self, context):
        print(self)
        self.report({'INFO'}, "Recalculate Normals")   
                        
        for obj in bpy.context.selected_objects:
            
            obj = bpy.context.scene.objects.active                
           
            if obj:
                
                if obj.type in {'MESH'}:                 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent()
                    bpy.ops.object.editmode_toggle()            

      
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
    


class VIEW3D_TP_Wire_On(bpy.types.Operator):
    '''Wire on'''
    bl_idname = "tp_ops.wire_on"
    bl_label = "Wire on"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        selection = bpy.context.selected_objects  
         
        if not(selection): 
            for obj in bpy.data.objects:
                obj.show_wire = True
                obj.show_all_edges = True
                
        else:
            for obj in selection:
                obj.show_wire = True
                obj.show_all_edges = True 
        return {'FINISHED'}


class VIEW3D_TP_Wire_Off(bpy.types.Operator):
    '''Wire off'''
    bl_idname = "tp_ops.wire_off"
    bl_label = "Wire off"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        selection = bpy.context.selected_objects  
        
        if not(selection): 
            for obj in bpy.data.objects:
                obj.show_wire = False
                obj.show_all_edges = False
                
        else:
            for obj in selection:
                obj.show_wire = False
                obj.show_all_edges = False   

        return {'FINISHED'}
    





class View3D_TP_Constraint_On(bpy.types.Operator):
    '''Display constraint in viewport'''
    bl_idname = "tp_ops.constraint_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:        
                for con in obj.constraints:
                    con.mute = True
        else:
            for obj in selection:        
                for con in obj.constraints:
                    con.mute = True
        
        return {'FINISHED'}



class View3D_TP_Constraint_Off(bpy.types.Operator):
    '''Hide constraint in viewport'''
    bl_idname = "tp_ops.constraint_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_objects 
        
        if not(selection):    
            for obj in bpy.data.objects:        
                for con in obj.constraints:
                    con.mute = False
        else:
            for obj in selection:        
                for con in obj.constraints:
                    con.mute = False

        return {'FINISHED'}



class View3D_TP_Expand_Con_Stack(bpy.types.Operator):
    '''Expand constraint stack'''
    bl_idname = "tp_ops.expand_con"
    bl_label = "Expand"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
          
        if not(bpy.context.selected_objects): 
            for obj in bpy.data.objects:        
                for con in obj.constraints:
                    con.show_expanded = True
        else:
            for obj in bpy.context.selected_objects:        
                for con in obj.constraints:
                    con.show_expanded = True

        return {'FINISHED'}


class View3D_TP_Collapse_Con_Stack(bpy.types.Operator):
    '''Collapse constraint stack'''
    bl_idname = "tp_ops.collapse_con"
    bl_label = "Collapse"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if not(bpy.context.selected_objects): 
            for obj in bpy.data.objects:        
                for mod in obj.constraints:
                    mod.show_expanded = False
        else:
            for obj in bpy.context.selected_objects:        
                for mod in obj.constraints:
                    mod.show_expanded = False
                    
        return {'FINISHED'}
    




    



class View3D_TP_Modifier_Apply(bpy.types.Operator):
    '''apply modifier'''
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
    '''remove modifier'''
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



class View3D_TP_Expand_Mod_Stack(bpy.types.Operator):
    '''Expand modifier stack'''
    bl_idname = "tp_ops.expand_mod"
    bl_label = "Expand"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
          
        if not(bpy.context.selected_objects): 
            for obj in bpy.data.objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = True
        else:
            for obj in bpy.context.selected_objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = True

        return {'FINISHED'}



class View3D_TP_Collapse_Mod_Stack(bpy.types.Operator):
    '''Collapse modifier stack'''
    bl_idname = "tp_ops.collapse_mod"
    bl_label = "Collapse"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if not(bpy.context.selected_objects): 
            for obj in bpy.data.objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = False
        else:
            for obj in bpy.context.selected_objects:        
                for mod in obj.modifiers:
                    mod.show_expanded = False
                    
        return {'FINISHED'}


def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__) 


if __name__ == "__main__":
    register()



