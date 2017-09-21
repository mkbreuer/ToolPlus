__status__ = "toolplus"
__author__ = "MKB"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *
from bpy.types import Menu
from . icons.icons import load_icons


class VIEW3D_ToolPus_Pie(Menu):
    bl_idname = "tp_menu.tp_pie"  
    bl_label = "T+ Pie"

    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        pie = layout.menu_pie()

#Pie1 ---- Left ---------------------------------------------------- 

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':
           
            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)     



#Pie2 ---- Right ---------------------------------------------------

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':

            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)   



#Pie3 ---- Bottom -------------------------------------------------- 

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':
           
            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)   



#Pie4 ---- Top ----------------------------------------------------- 

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':
           
            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    



#Pie5 ---- Top_Left ------------------------------------------------ 

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':
           
            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)   



#Pie6 ---- Top_Right -----------------------------------------------

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':

            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    



#Pie7 ---- Bottom_Left ---------------------------------------------

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':

            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    



#Pie8 ---- Bottom_Right --------------------------------------------

        box = pie.split().box().column()
        
        row = box.column(1)  
        button_align_zero = icons.get("icon_align_zero")                
        row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)    
         
        display_zero = context.user_preferences.addons[__package__].preferences.tab_pie_tools
        if display_zero == 'on':

            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)   



