__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



class VIEW3D_ToolPus_Batch(bpy.types.Operator):
    """T+ Batch """
    bl_label = "T+ Batch"
    bl_idname = "tp_menu.tp_batch"               
    bl_options = {'REGISTER', 'UNDO'}          
    
    def draw(self, context):

        icons = load_icons()
        
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box().column(1) 
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_batch_tools
        if display_zero == 'on':

            row.separator()
           
            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)      
                   


    def execute(self, context):
   
        return {'FINISHED'}

    def check(self, context):
        return True

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)



def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__) 


if __name__ == "__main__":
    register()

   