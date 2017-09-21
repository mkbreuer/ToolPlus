__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


class VIEW3D_ToolPus_Menu(bpy.types.Menu):
    bl_label = "T+ Menu"
    bl_idname = "tp_menu.tp_menu"   

    def draw(self, context):
        layout = self.layout

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'        
        
        button_align_zero = icons.get("icon_align_zero")                
        layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_menu_tools
        if display_zero == 'on':

            layout.separator()
           
            button_align_zero = icons.get("icon_align_zero")                
            layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)      
