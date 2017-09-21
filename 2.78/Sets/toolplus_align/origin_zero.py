__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *


class View3D_TP_Zero_to_Axis(bpy.types.Operator):
    """Zero Axis"""                 
    bl_idname = "tp_ops.zero_axis"          
    bl_label = "ZeroAxis"                 
    bl_options = {'REGISTER', 'UNDO'}   

    tp_switch = bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_obj",    
               description = "zero object or cursor")

    tp_switch_axis = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"All"  ,"04")],
               name = "ZeroAxis",
               default = "tp_x",    
               description = "zero target to choosen axis")


    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        row = box.row()
        row.prop(self, 'tp_switch', expand=True)

        row = box.row()
        row.prop(self, 'tp_switch_axis', expand=True)
        
        box.separator()
        
    def execute(self, context):


            

        if self.tp_switch_axis == "tp_x":  
            
            if self.tp_switch == "tp_obj":        
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[0] = 0     

            if self.tp_switch == "tp_org":                
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 
                                            
                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[0] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[0] = 0 

        if self.tp_switch_axis == "tp_y":  

            if self.tp_switch == "tp_obj":        
                for ob in bpy.context.selected_objects:
                    bpy.context.object.location[1] = 0  

            if self.tp_switch == "tp_org":
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[1] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[1] = 0 

        if self.tp_switch_axis == "tp_z":  

            if self.tp_switch == "tp_obj":     
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[2] = 0  

            if self.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[2] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[2] = 0 


        if self.tp_switch_axis == "tp_a": 
            
            if self.tp_switch == "tp_obj":   
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob                   
                    bpy.context.object.location[0] = 0  
                    bpy.context.object.location[1] = 0  
                    bpy.context.object.location[2] = 0  

            if self.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if self.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[0] = 0 
                bpy.context.space_data.cursor_location[1] = 0 
                bpy.context.space_data.cursor_location[2] = 0 



        return {'FINISHED'} 


    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)



class View3D_TP_Zero_to_Axis_Panel(bpy.types.Operator):
    """Zero Axis"""                 
    bl_idname = "tp_ops.zero_axis_panel"          
    bl_label = "ZeroAxis"                 
    bl_options = {'REGISTER', 'UNDO'}   

    bpy.types.Scene.tp_switch = bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_obj",    
               description = "zero object or cursor")

    bpy.types.Scene.tp_switch_axis = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"All"  ,"04")],
               name = "ZeroAxis",
               default = "tp_x",    
               description = "zero target to choosen axis")
        
    def execute(self, context):
        
        scene = context.scene 
        
        if scene.tp_switch_axis == "tp_x":  
            
            if scene.tp_switch == "tp_obj":        
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[0] = 0  

            if scene.tp_switch == "tp_org":                
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[0] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if scene.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[0] = 0 

        if scene.tp_switch_axis == "tp_y":  

            if scene.tp_switch == "tp_obj":        
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[1] = 0  

            if scene.tp_switch == "tp_org":
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()        
                        bpy.context.space_data.cursor_location[1] = 0 
                        bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if scene.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[1] = 0 

        if scene.tp_switch_axis == "tp_z":  

            if scene.tp_switch == "tp_obj":                    
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[2] = 0  

            if scene.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    for ob in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = ob 

                        bpy.ops.view3d.snap_cursor_to_active()   
                             
                    bpy.context.space_data.cursor_location[2] = 0
                    bpy.ops.tp_ops.origin_set_cursor()       
                                 
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if scene.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[2] = 0 


        if scene.tp_switch_axis == "tp_a": 
            
            if scene.tp_switch == "tp_obj":     
                for ob in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = ob 
                    bpy.context.object.location[0] = 0  
                    bpy.context.object.location[1] = 0  
                    bpy.context.object.location[2] = 0  

            if scene.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    
                    bpy.ops.view3d.snap_cursor_to_active()        
                    bpy.context.space_data.cursor_location[0] = 0 
                    bpy.context.space_data.cursor_location[1] = 0 
                    bpy.context.space_data.cursor_location[2] = 0 
                    bpy.ops.tp_ops.origin_set_cursor()
                    
                    bpy.ops.object.editmode_toggle()

            if scene.tp_switch == "tp_crs":        
                bpy.context.space_data.cursor_location[0] = 0 
                bpy.context.space_data.cursor_location[1] = 0 
                bpy.context.space_data.cursor_location[2] = 0 



        return {'FINISHED'} 




class View3D_TP_Zero_X(bpy.types.Operator):
    """Zero X Axis"""                 
    bl_idname = "tp_ops.zero_x"          
    bl_label = "ZeroX"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        for ob in bpy.context.selected_objects:
            bpy.context.scene.objects.active = ob    
            bpy.context.object.location[0] = 0  

        return {'FINISHED'} 

    
class View3D_TP_Zero_Y(bpy.types.Operator):
    """Zero Y Axis"""                 
    bl_idname = "tp_ops.zero_y"          
    bl_label = "ZeroY"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        for ob in bpy.context.selected_objects:
            bpy.context.scene.objects.active = ob    
            bpy.context.object.location[1] = 0  

        return {'FINISHED'} 


class View3D_TP_Zero_Z(bpy.types.Operator):
    """Zero Z Axis"""                 
    bl_idname = "tp_ops.zero_z"          
    bl_label = "ZeroZ"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        for ob in bpy.context.selected_objects:
            bpy.context.scene.objects.active = ob    
            bpy.context.object.location[2] = 0  

        return {'FINISHED'} 


class View3D_TP_Zero_Cursor(bpy.types.Operator):
    """Zero Cursor"""                 
    bl_idname = "tp_ops.zero_cursor"          
    bl_label = "Zero3DC"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.context.space_data.cursor_location[0] = 0 
        bpy.context.space_data.cursor_location[1] = 0 
        bpy.context.space_data.cursor_location[2] = 0 

        return {'FINISHED'} 


class View3D_TP_Zero_All_Axis(bpy.types.Operator):
    """Zero all Axis"""                 
    bl_idname = "tp_ops.zero_all_axis"          
    bl_label = "ZeroObj"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        for ob in bpy.context.selected_objects:
            bpy.context.scene.objects.active = ob 
            bpy.context.object.location[0] = 0  
            bpy.context.object.location[1] = 0  
            bpy.context.object.location[2] = 0  

        return {'FINISHED'} 




def register():

    bpy.utils.register_module(__name__)
 
    
def unregister():

    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()

