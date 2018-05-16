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


def draw_mkb_layout(self, context, layout):
  
    icons = load_icons()

    panel_prefs = context.user_preferences.addons[__package__].preferences

    col = layout.column(align=True)

    # BLOCK 0-7#
    box = col.box().column(1) 
          
    box.separator()       

    row = box.row(1)                
    row.scale_y = 1
    if context.user_preferences.addons[__package__].preferences.tab_center_mkb == 'free':
        if context.user_preferences.addons[__package__].preferences.tab_center_left_mkb == True:
            ico="UNLINKED"
        else:
            ico="LINKED"  
        row.prop(panel_prefs, "tab_center_left_mkb", text="", icon=ico)     
    row.prop(panel_prefs, "tab_center_mkb", expand =True) 

    box.separator()


    # SUBLINE 0-7 #
    box = col.box().column(1) 
    box.separator() 
    
    row = box.row(1)          
    row.scale_y = 1.3   
    row.prop(panel_prefs, 'subline_draw', expand =True) 

    box.separator()
 
    row = box.row(1)           
    if context.user_preferences.addons[__package__].preferences.tab_font_unit_mkb == True:
        ico="UNLINKED"
    else:
        ico="LINKED" 
    row.prop(panel_prefs, "tab_font_unit_mkb", text="", icon=ico)                
    row.prop(panel_prefs, "tab_font_text_mkb", text="", icon="COLLAPSEMENU") 
   
    if panel_prefs.subline_draw == "EMPTY_LINE":          
        row.label(text="", icon="RESTRICT_VIEW_ON")       
        row.label(text="hidden permanet draw")       
        row.label(text="", icon="RESTRICT_VIEW_ON")       
    else:
 
        if context.user_preferences.addons[__package__].preferences.tab_color_link_mkb == True:
            
            if panel_prefs.subline_draw == "ZERO_LINE":  
                row.prop(panel_prefs, 'text_0_text_mkb')
   
            if panel_prefs.subline_draw == "ONE_LINE":
                row.prop(panel_prefs, 'text_1_text_mkb') 

            if panel_prefs.subline_draw == "TWO_LINE":
                row.prop(panel_prefs, 'text_2_text_mkb') 
           
            if panel_prefs.subline_draw == "THREE_LINE":
                row.prop(panel_prefs, 'text_3_text_mkb')    

            if panel_prefs.subline_draw == "FOUR_LINE":
                row.prop(panel_prefs, 'text_4_text_mkb') 
 
            if panel_prefs.subline_draw == "FIVE_LINE":   
                row.prop(panel_prefs, 'text_5_text_mkb') 
       
            if panel_prefs.subline_draw == "SIX_LINE":                
                row.prop(panel_prefs, 'text_6_text_mkb') 
      
            if panel_prefs.subline_draw == "SEVEN_LINE": 
                row.prop(panel_prefs, 'text_7_text_mkb') 

        else:  
            
            if panel_prefs.subline_draw == "ZERO_LINE":  
                row.prop(panel_prefs, 'text_0_text_mkb')    

            if panel_prefs.subline_draw == "ONE_LINE":   
                row.prop(panel_prefs, 'text_1_text_mkb') 

            if panel_prefs.subline_draw == "TWO_LINE":
                row.prop(panel_prefs, 'text_2_text_mkb') 
           
            if panel_prefs.subline_draw == "THREE_LINE":   
                row.prop(panel_prefs, 'text_3_text_mkb') 

            if panel_prefs.subline_draw == "FOUR_LINE": 
                row.prop(panel_prefs, 'text_4_text_mkb') 

            if panel_prefs.subline_draw == "FIVE_LINE":   
                row.prop(panel_prefs, 'text_5_text_mkb') 
       
            if panel_prefs.subline_draw == "SIX_LINE":                
                row.prop(panel_prefs, 'text_6_text_mkb') 
      
            if panel_prefs.subline_draw == "SEVEN_LINE": 
                row.prop(panel_prefs, 'text_7_text_mkb') 
    

    row.prop(panel_prefs, "tab_font_external_mkb", text="", icon="LAYER_USED")                         
    row.menu("tp_menu.reset_ops_courier_mkb",text="", icon="RECOVER_AUTO") 

    box.separator() 

    if context.user_preferences.addons[__package__].preferences.tab_font_text_mkb == True:
    
        box.separator()    
       
        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L0")  
        row.prop(panel_prefs, 'text_0_text_mkb', text="")    
        if context.user_preferences.addons[__package__].preferences.text_l0_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l0_mkb", text="", icon=ico_eye)              


        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L1")  
        row.prop(panel_prefs, 'text_1_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l1_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l1_mkb", text="", icon=ico_eye)  


        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L2")  
        row.prop(panel_prefs, 'text_2_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l2_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l2_mkb", text="", icon=ico_eye) 
        

        row = box.row(1)           
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L3")   
        row.prop(panel_prefs, 'text_3_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l3_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l3_mkb", text="", icon=ico_eye) 


        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L4")  
        row.prop(panel_prefs, 'text_4_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l4_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l4_mkb", text="", icon=ico_eye) 


        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L5")  
        row.prop(panel_prefs, 'text_5_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l5_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l5_mkb", text="", icon=ico_eye) 
        
        
        row = box.row(1)       
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L6")             
        row.prop(panel_prefs, 'text_6_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l6_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l6_mkb", text="", icon=ico_eye) 

      
        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L7")  
        row.prop(panel_prefs, 'text_7_text_mkb', text="") 
        if context.user_preferences.addons[__package__].preferences.text_l7_mkb == True:
            ico_eye="RESTRICT_VIEW_OFF"
        else:
            ico_eye="RESTRICT_VIEW_ON" 
        row.prop(panel_prefs, "text_l7_mkb", text="", icon=ico_eye) 
        
        box.separator()

    box.separator()
   

    # FILEPATHES 0-7 #
    row = box.row(1)                
    row.scale_y = 1                  
    if context.user_preferences.addons[__package__].preferences.tab_color_link_mkb == True:
        ico="UNLINKED"
    else:
        ico="LINKED" 
    row.prop(panel_prefs, "tab_color_link_mkb", text="", icon=ico)  
    row.prop(panel_prefs, "tab_font_pathes_mkb", text="", icon="COLLAPSEMENU")             

    if panel_prefs.subline_draw == "EMPTY_LINE": 
        row.label(text="", icon="RESTRICT_VIEW_ON")       
        row.label(text="hidden permanet draw")       
        row.label(text="", icon="RESTRICT_VIEW_ON") 
    else:
        if context.user_preferences.addons[__package__].preferences.tab_font_unit_mkb == True:
               
            if panel_prefs.subline_draw == "ZERO_LINE":  
                row.prop(panel_prefs, 'filepath_0_mkb', text="") 
       
            if panel_prefs.subline_draw == "ONE_LINE":
                row.prop(panel_prefs, 'filepath_1_mkb', text="")     

            if panel_prefs.subline_draw == "TWO_LINE":
                row.prop(panel_prefs, 'filepath_2_mkb', text="") 
           
            if panel_prefs.subline_draw == "THREE_LINE":
                row.prop(panel_prefs, 'filepath_3_mkb', text="") 

            if panel_prefs.subline_draw == "FOUR_LINE":
                row.prop(panel_prefs, 'filepath_4_mkb', text="") 

            if panel_prefs.subline_draw == "FIVE_LINE":   
                row.prop(panel_prefs, 'filepath_5_mkb', text="") 

            if panel_prefs.subline_draw == "SIX_LINE":                
                row.prop(panel_prefs, 'filepath_6_mkb', text="") 

            if panel_prefs.subline_draw == "SEVEN_LINE": 
                row.prop(panel_prefs, 'filepath_7_mkb', text="") 

        else:  
            row.prop(panel_prefs, "filepath_all_mkb", text="")              


    if context.user_preferences.addons[__package__].preferences.tab_color_link_mkb == True:
           
        if panel_prefs.subline_draw == "ZERO_LINE":  
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_0_color_mkb', text="")    
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='ZERO_LINE'  
       
        if panel_prefs.subline_draw == "ONE_LINE":
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_1_color_mkb', text="")    
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='ONE_LINE'  

        if panel_prefs.subline_draw == "TWO_LINE":
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_2_color_mkb', text="")  
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='TWO_LINE'         

        if panel_prefs.subline_draw == "THREE_LINE":
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_3_color_mkb', text="")     
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='THREE_LINE'  

        if panel_prefs.subline_draw == "FOUR_LINE":
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_4_color_mkb', text="")     
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='FOUR_LINE'  

        if panel_prefs.subline_draw == "FIVE_LINE":   
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_5_color_mkb', text="") 
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='FIVE_LINE'         

        if panel_prefs.subline_draw == "SIX_LINE":                
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_6_color_mkb', text="") 
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='SIX_LINE'        

        if panel_prefs.subline_draw == "SEVEN_LINE": 
            sub = row.row(1)
            sub.scale_x = 0.1
            sub.prop(panel_prefs, 'text_7_color_mkb', text="") 
            row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='SEVEN_LINE'  

    else:  
        sub = row.row(1)          
        sub.scale_x = 0.1         
        sub.prop(panel_prefs, 'text_color_mkb', text="") 
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL")  

    box.separator() 

    if context.user_preferences.addons[__package__].preferences.tab_font_pathes_mkb == True:
         
        box.separator()          
        
        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L0")         
        sub.prop(panel_prefs, 'text_0_color_mkb')     
        row.prop(panel_prefs, "filepath_0_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='ZERO_LINE'


        row = box.row(1)
        sub=row.row(1)
        sub.scale_x = 0.15                     
        sub.label(text="L1")         
        sub.prop(panel_prefs, 'text_1_color_mkb')     
        row.prop(panel_prefs, "filepath_1_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='ONE_LINE' 

        
        row = box.row(1)                           
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label( text="L2")         
        sub.prop(panel_prefs, 'text_2_color_mkb')     
        row.prop(panel_prefs, "filepath_2_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='TWO_LINE'            

       
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="L3")         
        sub.prop(panel_prefs, 'text_3_color_mkb')     
        row.prop(panel_prefs, "filepath_3_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='THREE_LINE' 


        row = box.row(1)               
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="L4")         
        sub.prop(panel_prefs, 'text_4_color_mkb')     
        row.prop(panel_prefs, "filepath_4_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='FOUR_LINE'             

       
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="L5")         
        sub.prop(panel_prefs, 'text_5_color_mkb')    
        row.prop(panel_prefs, "filepath_5_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='FIVE_LINE' 

        
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="L6")         
        sub.prop(panel_prefs, 'text_6_color_mkb')     
        row.prop(panel_prefs, "filepath_6_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='SIX_LINE' 

       
        row = box.row(1)   
        sub=row.row(1)
        sub.scale_x = 0.15    
        sub.label(text="L7")         
        sub.prop(panel_prefs, 'text_7_color_mkb')     
        row.prop(panel_prefs, "filepath_7_mkb", text="")         
        row.operator("tp_ops.path_courier_font_mkb",text="", icon="FILESEL").mode='SEVEN_LINE' 
                  
    box.separator()  


    # TRANSFORM # 
    box = col.box().column(1)
    box.separator()     

    if context.user_preferences.addons[__package__].preferences.tab_array_link_mkb == True:

        row = box.row(1)         
        row.scale_y = 1.3   
        if context.user_preferences.addons[__package__].preferences.tab_array_link_mkb == True:
            ico="UNLINKED"
        else:
            ico="LINKED"  
        row.prop(panel_prefs, "tab_array_link_mkb", text="", icon=ico)
      
        if panel_prefs.subline_draw == "ZERO_LINE":
                                     
            row.prop(panel_prefs, 'text_0_offset_x_mkb') 
            row.prop(panel_prefs, 'text_0_offset_y_mkb')    

        if panel_prefs.subline_draw == "ONE_LINE":
         
            row.prop(panel_prefs, 'text_1_offset_x_mkb') 
            row.prop(panel_prefs, 'text_1_offset_y_mkb')   

        if panel_prefs.subline_draw == "TWO_LINE":

            row.prop(panel_prefs, 'text_2_offset_x_mkb') 
            row.prop(panel_prefs, 'text_2_offset_y_mkb') 

        if panel_prefs.subline_draw == "THREE_LINE":

            row.prop(panel_prefs, 'text_3_offset_x_mkb') 
            row.prop(panel_prefs, 'text_3_offset_y_mkb') 
  
        if panel_prefs.subline_draw == "FOUR_LINE":

            row.prop(panel_prefs, 'text_4_offset_x_mkb') 
            row.prop(panel_prefs, 'text_4_offset_y_mkb')  

        if panel_prefs.subline_draw == "FIVE_LINE":

            row.prop(panel_prefs, 'text_5_offset_x_mkb') 
            row.prop(panel_prefs, 'text_5_offset_y_mkb')     

        if panel_prefs.subline_draw == "SIX_LINE":

            row.prop(panel_prefs, 'text_6_offset_x_mkb') 
            row.prop(panel_prefs, 'text_6_offset_y_mkb') 

        if panel_prefs.subline_draw == "SEVEN_LINE":
 
            row.prop(panel_prefs, 'text_7_offset_x_mkb') 
            row.prop(panel_prefs, 'text_7_offset_y_mkb')    

    else: 
        row = box.row(1)         
        row.scale_y = 1.3

        if context.user_preferences.addons[__package__].preferences.tab_array_link_mkb == True:
            ico="UNLINKED"
        else:
            ico="LINKED"  
        row.prop(panel_prefs, "tab_array_link_mkb", text="", icon=ico)                       
        row.prop(panel_prefs, 'text_array_x_mkb') 
        row.prop(panel_prefs, 'text_array_y_mkb')        


    if context.user_preferences.addons[__package__].preferences.tab_scal_link_mkb == True:

        row = box.row(1)         
        row.scale_y = 1.3
        if context.user_preferences.addons[__package__].preferences.tab_scal_link_mkb == True:
            ico="UNLINKED"
        else:
            ico="LINKED"  
        row.prop(panel_prefs, "tab_scal_link_mkb", text="", icon=ico) 

        if panel_prefs.subline_draw == "ZERO_LINE":                  
            row.prop(panel_prefs, 'text_0_width_mkb') 
            row.prop(panel_prefs, 'text_0_height_mkb')     

        if panel_prefs.subline_draw == "ONE_LINE":  
            row.prop(panel_prefs, 'text_1_width_mkb') 
            row.prop(panel_prefs, 'text_1_height_mkb')     

        if panel_prefs.subline_draw == "TWO_LINE":
            row.prop(panel_prefs, 'text_2_width_mkb') 
            row.prop(panel_prefs, 'text_2_height_mkb')     
       
        if panel_prefs.subline_draw == "THREE_LINE":  
            row.prop(panel_prefs, 'text_3_width_mkb') 
            row.prop(panel_prefs, 'text_3_height_mkb')     

        if panel_prefs.subline_draw == "FOUR_LINE":  
            row.prop(panel_prefs, 'text_4_width_mkb') 
            row.prop(panel_prefs, 'text_4_height_mkb')     

        if panel_prefs.subline_draw == "FIVE_LINE":
            row.prop(panel_prefs, 'text_5_width_mkb') 
            row.prop(panel_prefs, 'text_5_height_mkb')     

        if panel_prefs.subline_draw == "SIX_LINE":    
            row.prop(panel_prefs, 'text_6_width_mkb') 
            row.prop(panel_prefs, 'text_6_height_mkb')     

        if panel_prefs.subline_draw == "SEVEN_LINE":  
            row.prop(panel_prefs, 'text_7_width_mkb') 
            row.prop(panel_prefs, 'text_7_height_mkb')   

    else:        
        row = box.row(1)         
        row.scale_y = 1.3       
        if context.user_preferences.addons[__package__].preferences.tab_scal_link_mkb == True:
            ico="UNLINKED"
        else:
            ico="LINKED"  
        row.prop(panel_prefs, "tab_scal_link_mkb", text="", icon=ico)                      
        row.prop(panel_prefs, 'text_width_mkb')
        row.prop(panel_prefs, 'text_height_mkb')           

    box.separator()

    row = box.row(1)          
    row.scale_y = 1.3 
 
    button_shadow = icons.get("icon_shadow")         
    row.prop(panel_prefs, 'text_shadow', text ="", icon_value=button_shadow.icon_id) 
    row.prop(panel_prefs, 'text_spread_y_mkb')   
    row.prop(panel_prefs, 'tab_view_mkb', text="", icon="SAVE_AS") 
  
    if context.user_preferences.addons[__package__].preferences.text_shadow == True:
      
        box.separator()
       
        row = box.row(1)          
        row.scale_y = 1.3 
        row.prop(panel_prefs, 'text_shadow_color',text="")
        row.prop(panel_prefs, 'text_shadow_alpha')

        row = box.row(1)          
        row.scale_y = 1.3 
        row.prop(panel_prefs, 'text_shadow_x')
        row.prop(panel_prefs, 'text_shadow_y')

    
    box.separator()

    row = box.row(1)          
    row.scale_y = 1.3 
    row.prop(panel_prefs, 'text_all_x_mkb') 
    row.prop(panel_prefs, 'text_all_y_mkb') 

    box.separator()

 
    # BASE #
    box = col.box().column(1)    
    box.separator()  

    row = box.row(1)                
    row.scale_y = 1.4       

    if context.user_preferences.addons[__package__].preferences.tab_permanent_mkb == True:
        ico="UNLINKED"
    else:
        ico="LINKED"    
    row.prop(panel_prefs, "tab_permanent_mkb", text="", icon=ico)                  
   
    button_run = icons.get("icon_run")         
    row.operator('tp_ops.do_text_draw_mkb', text="Do Text Draw", icon_value=button_run.icon_id) 
    row.operator("wm.save_userpref", text="", icon='SAVE_PREFS') 
  
    box.separator() 



