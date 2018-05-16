# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2018 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    

# LOAD UI: PANEL #
def draw_main_title_layout(self, context, layout):

    icons = load_icons()

    panel_prefs = context.user_preferences.addons[__package__].preferences

    col = layout.column(align=True)
 
    box = col.box().column(1) 

    box.separator()

    row = box.row(1)          
    row.scale_x = 1.3   
    row.prop(panel_prefs, 'dodraw', expand =True) 
   
    box.separator()     
   
    row = box.row(1)          
    row.scale_x = 1.3   
    row.prop(panel_prefs, "tab_center", expand =True) 

    box.separator()

    box = col.box().column(1) 
    
    box.separator()
  
    row = box.row(1)           
    if context.user_preferences.addons[__package__].preferences.tab_font_unit == True:
        ico="UNLINKED"
    else:
        ico="LINKED" 
    row.prop(panel_prefs, "tab_font_unit", text="", icon=ico)                  
    button_shadow = icons.get("icon_shadow")         
    row.prop(panel_prefs, 'text_shadow', text ="", icon_value=button_shadow.icon_id)  

    if panel_prefs.dodraw == "EMPTY":          
        row.label(text="", icon="RESTRICT_VIEW_ON")       
        row.label(text="hidden permanet draw")       
        row.label(text="", icon="RESTRICT_VIEW_ON")       

    else:
       
        if panel_prefs.dodraw == "ZERO":    
            row.prop(panel_prefs, 'text_0_text')    

        if panel_prefs.dodraw == "ONE":
            row.prop(panel_prefs, 'text_1_text') 

        if panel_prefs.dodraw == "TWO": 
            row.prop(panel_prefs, 'text_2_text') 
       
        if panel_prefs.dodraw == "THREE":   
            row.prop(panel_prefs, 'text_3_text') 

        if panel_prefs.dodraw == "FOUR":   
            row.prop(panel_prefs, 'text_4_text') 

        if panel_prefs.dodraw == "FIVE":   
            row.prop(panel_prefs, 'text_5_text') 
   
        if panel_prefs.dodraw == "SIX":                 
            row.prop(panel_prefs, 'text_6_text') 
  
        if panel_prefs.dodraw == "SEVEN": 
            row.prop(panel_prefs, 'text_7_text') 

    row.prop(panel_prefs, "tab_font_external", text="", icon="LAYER_USED")      
    row.operator("tp_ops.reset_ops_courier",text="", icon="RECOVER_AUTO") 
  
    box.separator()
   
    row = box.row(1)                
    row.scale_y = 1       
    if context.user_preferences.addons[__package__].preferences.tab_color_link == True:
        ico="UNLINKED"
    else:
        ico="LINKED" 
    row.prop(panel_prefs, "tab_color_link", text="", icon=ico)    
    row.prop(panel_prefs, "tab_font_pathes", text="", icon="COLLAPSEMENU")              

    if panel_prefs.dodraw == "EMPTY":          
        row.label(text="", icon="RESTRICT_VIEW_ON")       
        row.label(text="hidden permanet draw")       
        row.label(text="", icon="RESTRICT_VIEW_ON")       
    else:
        if context.user_preferences.addons[__package__].preferences.tab_font_unit == True:

            if panel_prefs.dodraw == "ZERO":  
                row.prop(panel_prefs, 'filepath_0', text="")  

            if panel_prefs.dodraw == "ONE":
                row.prop(panel_prefs, 'filepath_1', text="") 
  
            if panel_prefs.dodraw == "TWO":
                row.prop(panel_prefs, 'filepath_2', text="") 
            
            if panel_prefs.dodraw == "THREE":
                row.prop(panel_prefs, 'filepath_3', text="")      

            if panel_prefs.dodraw == "FOUR":
                row.prop(panel_prefs, 'filepath_4', text="")     

            if panel_prefs.dodraw == "FIVE":   
                row.prop(panel_prefs, 'filepath_5', text="") 

            if panel_prefs.dodraw == "SIX":                
                row.prop(panel_prefs, 'filepath_6', text="") 
      
            if panel_prefs.dodraw == "SEVEN": 
                row.prop(panel_prefs, 'filepath_7', text="") 
            
        else:

            row.prop(panel_prefs, "filepath_all", text="")           

      
        if context.user_preferences.addons[__package__].preferences.tab_color_link == True:
            
            if panel_prefs.dodraw == "ZERO":  
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_0_color')    
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='ZERO'  

            if panel_prefs.dodraw == "ONE":
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_1_color')    
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='ONE'  

            if panel_prefs.dodraw == "TWO":
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_2_color')  
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='TWO'             

            if panel_prefs.dodraw == "THREE":
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_3_color')     
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='THREE'  

            if panel_prefs.dodraw == "FOUR":
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_4_color')     
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='FOUR'  

            if panel_prefs.dodraw == "FIVE":   
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_5_color') 
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='FIVE'  

            if panel_prefs.dodraw == "SIX":                
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_6_color') 
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='SIX'        

            if panel_prefs.dodraw == "SEVEN": 
                sub = row.row(1)
                sub.scale_x = 0.1
                sub.prop(panel_prefs, 'text_7_color')  
                row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='SEVEN'        

        else:
            sub = row.row(1)          
            sub.scale_x = 0.1         
            sub.prop(panel_prefs, 'text_color')
            row.operator("tp_ops.path_courier_font", text="", icon="FILESEL") 
 
    box.separator()
          
    if context.user_preferences.addons[__package__].preferences.tab_font_pathes == True:

        box.separator()          
        
        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="T0")  
        sub.prop(panel_prefs, 'text_0_color')                                
        row.prop(panel_prefs, "filepath_0", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='ZERO'  

        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="T1")         
        sub.prop(panel_prefs, 'text_1_color')     
        row.prop(panel_prefs, "filepath_1", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='ONE'  
        
        row = box.row(1)                           
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label( text="T2")         
        sub.prop(panel_prefs, 'text_2_color')     
        row.prop(panel_prefs, "filepath_2", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='TWO'             
       
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="T3")         
        sub.prop(panel_prefs, 'text_3_color')     
        row.prop(panel_prefs, "filepath_3", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='THREE'  

        row = box.row(1)               
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="T4")         
        sub.prop(panel_prefs, 'text_4_color')     
        row.prop(panel_prefs, "filepath_4", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='FOUR'              
       
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="T5")         
        sub.prop(panel_prefs, 'text_5_color')    
        row.prop(panel_prefs, "filepath_5", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='FIVE'  
        
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="T6")         
        sub.prop(panel_prefs, 'text_6_color')     
        row.prop(panel_prefs, "filepath_6", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='SIX'  
       
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="T7")         
        sub.prop(panel_prefs, 'text_7_color')     
        row.prop(panel_prefs, "filepath_7", text="")         
        row.operator("tp_ops.path_courier_font",text="", icon="FILESEL").mode='SEVEN'  
        
        box.separator()      
  

    box.separator() 

    box = col.box().column(1) 
        
    box.separator() 

    if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:

        row = box.row(1)         
        row.scale_y = 1.3   
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:
            ico="UNLINKED"
        else:
            ico="LINKED"     
        row.prop(panel_prefs, "tab_pos_link", text="", icon=ico)
      
        if panel_prefs.dodraw == "ZERO":
                                     
            row.prop(panel_prefs, 'text_0_pos_x') 
            row.prop(panel_prefs, 'text_0_pos_y')    

        if panel_prefs.dodraw == "ONE":
            row.prop(panel_prefs, 'text_1_pos_x') 
            row.prop(panel_prefs, 'text_1_pos_y')   

        if panel_prefs.dodraw == "TWO":
            row.prop(panel_prefs, 'text_2_pos_x') 
            row.prop(panel_prefs, 'text_2_pos_y') 

        if panel_prefs.dodraw == "THREE":
            row.prop(panel_prefs, 'text_3_pos_x') 
            row.prop(panel_prefs, 'text_3_pos_y') 
  

        if panel_prefs.dodraw == "FOUR":
            row.prop(panel_prefs, 'text_4_pos_x') 
            row.prop(panel_prefs, 'text_4_pos_y')  

        if panel_prefs.dodraw == "FIVE":
            row.prop(panel_prefs, 'text_5_pos_x') 
            row.prop(panel_prefs, 'text_5_pos_y')     

        if panel_prefs.dodraw == "SIX":
            row.prop(panel_prefs, 'text_6_pos_x') 
            row.prop(panel_prefs, 'text_6_pos_y') 

        if panel_prefs.dodraw == "SEVEN":
            row.prop(panel_prefs, 'text_7_pos_x') 
            row.prop(panel_prefs, 'text_7_pos_y')    

    else: 
        row = box.row(1)         
        row.scale_y = 1.3
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:
            ico="UNLINKED"
        else:
            ico="LINKED"              
        row.prop(panel_prefs, "tab_pos_link", text="", icon=ico)                
        row.prop(panel_prefs, 'text_pos_x') 
        row.prop(panel_prefs, 'text_pos_y')   


    if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:

        row = box.row(1)         
        row.scale_y = 1.3
        row.prop(panel_prefs, "tab_scal_link", text="", icon=ico) 

        if panel_prefs.dodraw == "ZERO":                  
            row.prop(panel_prefs, 'text_0_width_title') 
            row.prop(panel_prefs, 'text_0_height_title')     

        if panel_prefs.dodraw == "ONE":  
            row.prop(panel_prefs, 'text_1_width_title') 
            row.prop(panel_prefs, 'text_1_height_title')     

        if panel_prefs.dodraw == "TWO":
            row.prop(panel_prefs, 'text_2_width_title') 
            row.prop(panel_prefs, 'text_2_height_title')     
       
        if panel_prefs.dodraw == "THREE":  
            row.prop(panel_prefs, 'text_3_width_title') 
            row.prop(panel_prefs, 'text_3_height_title')     

        if panel_prefs.dodraw == "FOUR":  
            row.prop(panel_prefs, 'text_4_width_title') 
            row.prop(panel_prefs, 'text_4_height_title')     

        if panel_prefs.dodraw == "FIVE":
            row.prop(panel_prefs, 'text_5_width_title') 
            row.prop(panel_prefs, 'text_5_height_title')     

        if panel_prefs.dodraw == "SIX":    
            row.prop(panel_prefs, 'text_6_width_title') 
            row.prop(panel_prefs, 'text_6_height_title')     

        if panel_prefs.dodraw == "SEVEN":  
            row.prop(panel_prefs, 'text_7_width_title') 
            row.prop(panel_prefs, 'text_7_height_title')   

    else:        
        row = box.row(1)         
        row.scale_y = 1.3
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            ico="UNLINKED"
        else:
            ico="LINKED"         
        row.prop(panel_prefs, "tab_scal_link", text="", icon=ico)                
        row.prop(panel_prefs, 'text_width_title') 
        row.prop(panel_prefs, 'text_height_title')      
 
        
    if context.user_preferences.addons[__package__].preferences.text_shadow == True:
      
        box.separator()
       
        row = box.row(1)          
        sub = row.row(1)
        sub.scale_y = 1.3
        sub.scale_x = 0.52    
        sub.prop(panel_prefs, 'text_shadow_alpha')

        sub1 = row.row(1)
        sub1.scale_y = 1.3
        sub1.scale_x = 0.5     
        sub1.prop(panel_prefs, 'text_shadow_color',text="")
        row.prop(panel_prefs, 'tab_view_mkb', text="", icon="SAVE_AS") 

        row = box.row(1)          
        row.scale_y = 1.3 
        row.prop(panel_prefs, 'text_shadow_x')
        row.prop(panel_prefs, 'text_shadow_y')

    box.separator() 

    box = col.box().column(1) 

    box.separator() 

    row = box.row(1)                
    row.scale_y = 1.4       

    if context.user_preferences.addons[__package__].preferences.tab_permanent == True:
        ico="UNLINKED"
    else:
        ico="LINKED" 
    row.prop(panel_prefs, "tab_permanent", text="", icon=ico)                  
    button_run = icons.get("icon_run")   
    row.operator('tp_ops.dotextdraw', text="Do Text Draw", icon_value=button_run.icon_id) 
    row.operator("wm.save_userpref", text="", icon='SAVE_PREFS') 
  
    box.separator()  




