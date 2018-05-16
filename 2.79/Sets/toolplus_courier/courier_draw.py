# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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

import blf
import bgl

# load external *.ttf file
#font_path = 'C:\Windows\Fonts\Alfredo_.ttf'
# store the font indice
#font_id = blf.load(font_path)


def draw_callback_px_text(self, context):
    scene = bpy.context.scene    

    panel_prefs = bpy.context.user_preferences.addons[__package__].preferences 
   
    font_path   = blf.load(panel_prefs.filepath_all)
    font_path_0 = blf.load(panel_prefs.filepath_0)
    font_path_1 = blf.load(panel_prefs.filepath_1)
    font_path_2 = blf.load(panel_prefs.filepath_2)
    font_path_3 = blf.load(panel_prefs.filepath_3)
    font_path_4 = blf.load(panel_prefs.filepath_4)
    font_path_5 = blf.load(panel_prefs.filepath_5)
    font_path_6 = blf.load(panel_prefs.filepath_6)
    font_path_7 = blf.load(panel_prefs.filepath_7)
   
    text_width_title  = panel_prefs.text_width_title
    text_height_title = panel_prefs.text_height_title
    text_pos_x = panel_prefs.text_pos_x
    text_pos_y = panel_prefs.text_pos_y 

    # HEADER AND SHELFS #
    hheader = context.area.regions[0].height # 26px
    tpanel = context.area.regions[1].width
    npanel = context.area.regions[3].width
    
    # zero out tpanel width, if region overlap it turned on
    if context.user_preferences.system.use_region_overlap:
        tpanel = 0

    # fetch real space in between 
    self.REALx = context.area.width  - npanel - tpanel 
    self.REALy = context.area.height + hheader    

    text_shadow = panel_prefs.text_shadow
    text_shadow_color = panel_prefs.text_shadow_color
    text_shadow_alpha = panel_prefs.text_shadow_alpha
    text_shadow_x = panel_prefs.text_shadow_x
    text_shadow_y = panel_prefs.text_shadow_y

    # TITLE 0 # 
    if panel_prefs.dodraw == "ZERO":

        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_0_pos_x = panel_prefs.text_0_pos_x
            text_0_pos_y = panel_prefs.text_0_pos_y              
        else:            
            text_0_pos_x = panel_prefs.text_pos_x
            text_0_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_0_width_title  = panel_prefs.text_0_width_title
            text_0_height_title = panel_prefs.text_0_height_title
        else:
            text_0_width_title  = panel_prefs.text_width_title
            text_0_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_0_color = panel_prefs.text_0_color           
            bgl.glColor3f(*text_0_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_0 = font_path
            else:
                font_id_0 = font_path_0      
        else:
            font_id_0 = 0                
             
        # FILEPATH FIELD #
        text_0_text = panel_prefs.text_0_text   

        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_0, text_0_text)
        
        self.line_0_width = line_width     
        self.line_0_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_0, (self.REALx/2-self.line_0_width/2+text_0_pos_x), (self.REALy/2-self.line_0_height+text_0_pos_y), 0)            
        else:
            blf.position(font_id_0, (text_0_pos_x+20), (self.REALy/2-self.line_0_height+text_0_pos_y), 0) 

        blf.size(font_id_0, text_0_width_title, text_0_height_title+10)        
        blf.draw(font_id_0, text_0_text)
                   
        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_0, blf.SHADOW)
            blf.shadow_offset(font_id_0, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_0, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_0, blf.SHADOW)



    # TITLE 1 # 
    if panel_prefs.dodraw == "ONE":

        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_1_pos_x = panel_prefs.text_1_pos_x
            text_1_pos_y = panel_prefs.text_1_pos_y              
        else:            
            text_1_pos_x = panel_prefs.text_pos_x
            text_1_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_1_width_title  = panel_prefs.text_1_width_title
            text_1_height_title = panel_prefs.text_1_height_title
        else:
            text_1_width_title  = panel_prefs.text_width_title
            text_1_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_1_color = panel_prefs.text_1_color           
            bgl.glColor3f(*text_1_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_1 = font_path
            else:
                font_id_1 = font_path_1      
        else:
            font_id_1 = 0                

        # FILEPATH FIELD #
        text_1_text = panel_prefs.text_1_text 
        
        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_1, text_1_text)
        
        self.line_1_width = line_width     
        self.line_1_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_1, (self.REALx/2-self.line_1_width/2+text_1_pos_x), (self.REALy/2-self.line_1_height+text_1_pos_y), 0)            
        else:
            blf.position(font_id_1, (text_1_pos_x+20), (self.REALy/2-self.line_1_height+text_1_pos_y), 0)       


        blf.size(font_id_1, text_1_width_title, text_1_height_title+10)      
        blf.draw(font_id_1, text_1_text)
      
        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_1, blf.SHADOW)
            blf.shadow_offset(font_id_1, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_1, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_1, blf.SHADOW)



    # TITLE 2 # 
    if panel_prefs.dodraw == "TWO":       
       
        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_2_pos_x = panel_prefs.text_2_pos_x
            text_2_pos_y = panel_prefs.text_2_pos_y              
        else:            
            text_2_pos_x = panel_prefs.text_pos_x
            text_2_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_2_width_title  = panel_prefs.text_2_width_title
            text_2_height_title = panel_prefs.text_2_height_title
        else:
            text_2_width_title  = panel_prefs.text_width_title
            text_2_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_2_color = panel_prefs.text_2_color           
            bgl.glColor3f(*text_2_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_2 = font_path
            else:
                font_id_2 = font_path_2      
        else:
            font_id_2 = 0                

        # FILEPATH FIELD #
        text_2_text = panel_prefs.text_2_text 

        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_2, text_2_text)
        
        self.line_2_width = line_width     
        self.line_2_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_2, (self.REALx/2-self.line_2_width/2+text_2_pos_x), (self.REALy/2-self.line_2_height+text_2_pos_y), 0)            
        else:
            blf.position(font_id_2, (text_2_pos_x+20), (self.REALy/2-self.line_2_height+text_2_pos_y), 0)   
             
        blf.size(font_id_2, text_2_width_title, text_2_height_title+10)
        blf.draw(font_id_2, text_2_text)

        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_2, blf.SHADOW)
            blf.shadow_offset(font_id_2, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_2, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_2, blf.SHADOW)



    # TITLE 3 # 
    if panel_prefs.dodraw == "THREE":       
       
        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_3_pos_x = panel_prefs.text_3_pos_x
            text_3_pos_y = panel_prefs.text_3_pos_y              
        else:            
            text_3_pos_x = panel_prefs.text_pos_x
            text_3_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_3_width_title  = panel_prefs.text_3_width_title
            text_3_height_title = panel_prefs.text_3_height_title
        else:
            text_3_width_title  = panel_prefs.text_width_title
            text_3_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_3_color = panel_prefs.text_3_color           
            bgl.glColor3f(*text_3_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_3 = font_path
            else:
                font_id_3 = font_path_3     
        else:
            font_id_3 = 0                

        # FILEPATH FIELD #
        text_3_text = panel_prefs.text_3_text 
              
        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_3, text_3_text)
        
        self.line_3_width = line_width     
        self.line_3_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_3, (self.REALx/2-self.line_3_width/2+text_3_pos_x), (self.REALy/2-self.line_3_height+text_3_pos_y), 0)            
        else:
            blf.position(font_id_3, (text_3_pos_x+20), (self.REALy/2-self.line_3_height+text_3_pos_y), 0)  

        blf.size(font_id_3, text_3_width_title, text_3_height_title+10)
        blf.draw(font_id_3, text_3_text)

        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_3, blf.SHADOW)
            blf.shadow_offset(font_id_3, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_3, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_3, blf.SHADOW)
            


    # TITLE 4 # 
    if panel_prefs.dodraw == "FOUR":

        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_4_pos_x = panel_prefs.text_4_pos_x
            text_4_pos_y = panel_prefs.text_4_pos_y              
        else:            
            text_4_pos_x = panel_prefs.text_pos_x
            text_4_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_4_width_title  = panel_prefs.text_4_width_title
            text_4_height_title = panel_prefs.text_4_height_title
        else:
            text_4_width_title  = panel_prefs.text_width_title
            text_4_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_4_color = panel_prefs.text_4_color           
            bgl.glColor3f(*text_4_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_4 = font_path
            else:
                font_id_4 = font_path_4      
        else:
            font_id_4 = 0                

        # FILEPATH FIELD #
        text_4_text = panel_prefs.text_4_text 
              
        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_4, text_4_text)
        
        self.line_4_width = line_width     
        self.line_4_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_4, (self.REALx/2-self.line_4_width/2+text_4_pos_x), (self.REALy/2-self.line_4_height+text_4_pos_y), 0)            
        else:
            blf.position(font_id_4, (text_4_pos_x+20), (self.REALy/2-self.line_4_height+text_4_pos_y), 0)   

        blf.size(font_id_4, text_4_width_title, text_4_height_title+10)
        blf.draw(font_id_4, text_4_text)

        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_4, blf.SHADOW)
            blf.shadow_offset(font_id_4, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_4, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_4, blf.SHADOW)
            


    # TITLE 5 # 
    if panel_prefs.dodraw == "FIVE":

        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_5_pos_x = panel_prefs.text_5_pos_x
            text_5_pos_y = panel_prefs.text_5_pos_y              
        else:            
            text_5_pos_x = panel_prefs.text_pos_x
            text_5_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_5_width_title = panel_prefs.text_5_width_title
            text_5_height_title = panel_prefs.text_5_height_title
        else:
            text_5_width_title  = panel_prefs.text_width_title
            text_5_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_5_color = panel_prefs.text_5_color           
            bgl.glColor3f(*text_5_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_5 = font_path
            else:
                font_id_5 = font_path_5      
        else:
            font_id_5 = 0                

        # FILEPATH FIELD #
        text_5_text = panel_prefs.text_5_text 
              
        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_5, text_5_text)
        
        self.line_5_width = line_width     
        self.line_5_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_5, (self.REALx/2-self.line_5_width/2+text_5_pos_x), (self.REALy/2-self.line_5_height+text_5_pos_y), 0)            
        else:
            blf.position(font_id_5, (text_5_pos_x+20), (self.REALy/2-self.line_5_height+text_5_pos_y), 0)   
  
        blf.size(font_id_5, text_5_width_title, text_5_height_title+10)
        blf.draw(font_id_5, text_5_text)

        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_5, blf.SHADOW)
            blf.shadow_offset(font_id_5, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_5, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_5, blf.SHADOW)



    # TITLE 6 # 
    if panel_prefs.dodraw == "SIX":      
      
        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_6_pos_x = panel_prefs.text_6_pos_x
            text_6_pos_y = panel_prefs.text_6_pos_y              
        else:            
            text_6_pos_x = panel_prefs.text_pos_x
            text_6_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_6_width_title  = panel_prefs.text_6_width_title
            text_6_height_title = panel_prefs.text_6_height_title
        else:
            text_6_width_title  = panel_prefs.text_width_title
            text_6_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_6_color = panel_prefs.text_6_color           
            bgl.glColor3f(*text_6_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_6 = font_path
            else:
                font_id_6 = font_path_6
        else:
            font_id_6 = 0                

        # FILEPATH FIELD #
        text_6_text = panel_prefs.text_6_text 
              
        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_6, text_6_text)
        
        self.line_6_width = line_width     
        self.line_6_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_6, (self.REALx/2-self.line_6_width/2+text_6_pos_x), (self.REALy/2-self.line_6_height+text_6_pos_y), 0)            
        else:
            blf.position(font_id_6, (text_6_pos_x+20), (self.REALy/2-self.line_6_height+text_6_pos_y), 0)   
                 
        blf.size(font_id_6, text_6_width_title, text_6_height_title+10)
        blf.draw(font_id_6, text_6_text)

        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_6, blf.SHADOW)
            blf.shadow_offset(font_id_6, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_6, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_6, blf.SHADOW)



    # TITLE 7 #
    if panel_prefs.dodraw == "SEVEN":

        # POSITION #    
        if context.user_preferences.addons[__package__].preferences.tab_pos_link == True:            
            text_7_pos_x = panel_prefs.text_7_pos_x
            text_7_pos_y = panel_prefs.text_7_pos_y              
        else:            
            text_7_pos_x = panel_prefs.text_pos_x
            text_7_pos_y = panel_prefs.text_pos_y    

        # SCALE #      
        if context.user_preferences.addons[__package__].preferences.tab_scal_link == True:
            text_7_width_title  = panel_prefs.text_7_width_title
            text_7_height_title = panel_prefs.text_7_height_title
        else:
            text_7_width_title  = panel_prefs.text_width_title
            text_7_height_title = panel_prefs.text_height_title                            
              
        # COLOR #   
        if context.user_preferences.addons[__package__].preferences.tab_color_link == False:            
            text_color = panel_prefs.text_color           
            bgl.glColor3f(*text_color)  
        else:
            text_7_color = panel_prefs.text_7_color           
            bgl.glColor3f(*text_7_color)  

        # FONT #
        if context.user_preferences.addons[__package__].preferences.tab_font_external == False:
            if context.user_preferences.addons[__package__].preferences.tab_font_unit == False: 
                font_id_7 = font_path
            else:
                font_id_7 = font_path_7
        else:
            font_id_7 = 0                

        # FILEPATH FIELD #
        text_7_text = panel_prefs.text_7_text 
              
        # length of the text line 
        line_width, line_height = blf.dimensions(font_id_7, text_7_text)
        
        self.line_7_width = line_width     
        self.line_7_height = line_height   
                                           
        # APPLY PREFERENCES #          
        if context.user_preferences.addons[__package__].preferences.tab_center == 'middle':                
            blf.position(font_id_7, (self.REALx/2-self.line_7_width/2+text_7_pos_x), (self.REALy/2-self.line_7_height+text_7_pos_y), 0)            
        else:
            blf.position(font_id_7, (text_7_pos_x+20), (self.REALy/2-self.line_7_height+text_7_pos_y), 0)   
              
        blf.size(font_id_7, text_7_width_title, text_7_height_title+10)
        blf.draw(font_id_7, text_7_text )

        # DROPSHADOW # 
        if context.user_preferences.addons[__package__].preferences.text_shadow == True:                
            blf.enable(font_id_7, blf.SHADOW)
            blf.shadow_offset(font_id_7, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_7, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_7, blf.SHADOW)


    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0)




class VIEW3D_TP_Do_Nothing(bpy.types.Operator):
    """Do Nothing"""
    bl_idname = "tp_ops.do_nothing"
    bl_label = " DoNothing"
    bl_options = {'INTERNAL'}        

    def execute(self, context):
        print("Do Nothing")
        return {'FINISHED'}


class VIEW3D_TP_Do_Text_Draw_Modal(bpy.types.Operator):
    """Draw Text to 3D View"""
    bl_idname = "tp_ops.dotextdraw"
    bl_label = "DoTextDraw"
    bl_options = {'REGISTER', 'UNDO'}  

    def modal(self, context, event):
        context.area.tag_redraw()

        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences     
      
        if panel_prefs.dodraw == "EMPTY":
            bpy.ops.tp_ops.do_nothing
    
        if panel_prefs.dodraw == "ZERO":
            bpy.ops.tp_ops.do_nothing
       
        if panel_prefs.dodraw == "ONE":
            bpy.ops.tp_ops.do_nothing

        if panel_prefs.dodraw == "TWO":
            bpy.ops.tp_ops.do_nothing

        if panel_prefs.dodraw == "THREE":
            bpy.ops.tp_ops.do_nothing
            
        if panel_prefs.dodraw == "FOUR":
            bpy.ops.tp_ops.do_nothing

        if panel_prefs.dodraw == "FIVE":
            bpy.ops.tp_ops.do_nothing

        if panel_prefs.dodraw == "SIX":
            bpy.ops.tp_ops.do_nothing

        if panel_prefs.dodraw == "SEVEN":
            bpy.ops.tp_ops.do_nothing
        
        if event.type in {'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self.handle, 'WINDOW')
            return {'CANCELLED'}

            #How to disable a running modal without event type?
            #alternative
#            ev = []
#            ev.append("Click")  
#            if event.shift:
#                ev.append("Shift")
#                return {'FINISHED'}              
#            else:
#            return {'RUNNING_MODAL'}


        if context.user_preferences.addons[__package__].preferences.tab_permanent == False:           
            return {'FINISHED'}              
        else:
            return {'RUNNING_MODAL'}


    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
           
            args = (self, context)
         
            self.handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_text, args, 'WINDOW', 'POST_PIXEL')
            
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}




# RESET PROPERTIES #
class VIEW3D_TP_Reset_Courier_Properties(bpy.types.Operator):
    """Reset properties to default values"""
    bl_idname = "tp_ops.reset_ops_courier"
    bl_label = "Reset Values"
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):

        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences     

        panel_prefs.text_width = 50
        panel_prefs.text_height = 50
        panel_prefs.text_pos_x = 0
        panel_prefs.text_pos_y = 0          
        panel_prefs.text_color = (0.5, 1, 1)          

        panel_prefs.text_0_width = 50
        panel_prefs.text_0_height = 50
        panel_prefs.text_0_pos_x = 0
        panel_prefs.text_0_pos_y = 0          
        panel_prefs.text_0_color = (1, 0, 0)          
        panel_prefs.text_0_text = "0. Title"

        panel_prefs.text_1_width = 50
        panel_prefs.text_1_height = 50
        panel_prefs.text_1_pos_x = 0
        panel_prefs.text_1_pos_y = 0          
        panel_prefs.text_1_color = (0.9, 0, 1)          
        panel_prefs.text_1_text = "1. Text"

        panel_prefs.text_2_width = 50
        panel_prefs.text_2_height = 50
        panel_prefs.text_2_pos_x = 0
        panel_prefs.text_2_pos_y = 0          
        panel_prefs.text_2_color = (0, 0, 1)          
        panel_prefs.text_2_text = "2. Text"

        panel_prefs.text_3_width = 50
        panel_prefs.text_3_height = 50
        panel_prefs.text_3_pos_x = 0
        panel_prefs.text_3_pos_y = 0          
        panel_prefs.text_3_color = (0, 1, 1)          
        panel_prefs.text_3_text = "3. Text"

        panel_prefs.text_4_width = 50
        panel_prefs.text_4_height = 50
        panel_prefs.text_4_pos_x = 0
        panel_prefs.text_4_pos_y = 0          
        panel_prefs.text_4_color = (0, 1, 0)          
        panel_prefs.text_4_text = "4. Text"

        panel_prefs.text_5_width = 50
        panel_prefs.text_5_height = 50
        panel_prefs.text_5_pos_x = 0
        panel_prefs.text_5_pos_y = 0          
        panel_prefs.text_5_color = (1, 1, 0)          
        panel_prefs.text_5_text = "5. Text"

        panel_prefs.text_6_width = 50
        panel_prefs.text_6_height = 50
        panel_prefs.text_6_pos_x = 0
        panel_prefs.text_6_pos_y = 0          
        panel_prefs.text_6_color = (1, 0.5, 0)          
        panel_prefs.text_6_text = "6. Text"

        panel_prefs.text_7_width = 50                
        panel_prefs.text_7_height = 50
        panel_prefs.text_7_pos_x = 0
        panel_prefs.text_7_pos_y = 0          
        panel_prefs.text_7_color = (1, 0.5, 1)          
        panel_prefs.text_7_text = "7. Text"

        return {"FINISHED"}




class VIEW_3D_TP_Courier_Filepath(bpy.types.Operator):
    """select *.ttf font files for text"""
    bl_idname = "tp_ops.path_courier_font"
    bl_label = "Select a *.ttf file"

    filename_ext = ".ttf"
    filter_glob = StringProperty(default="*.ttf", options={'HIDDEN'})    

    filepath = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default="")
    files = CollectionProperty( name="File Path",type=bpy.types.OperatorFileListElement )    
                                   
    mode = bpy.props.StringProperty(default="")

    def execute(self, context):
        
        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences    
      
        if context.user_preferences.addons[__package__].preferences.tab_font_unit == True: 
            
            if "ZERO" in self.mode:
                panel_prefs.filepath_0 = self.properties.filepath

            if "ONE" in self.mode:           
                panel_prefs.filepath_1 = self.properties.filepath

            if "TWO" in self.mode:
                panel_prefs.filepath_2 = self.properties.filepath

            if "THREE" in self.mode:
                panel_prefs.filepath_3 = self.properties.filepath

            if "FOUR" in self.mode:                
               panel_prefs.filepath_4 = self.properties.filepath

            if "FIVE" in self.mode:
                panel_prefs.filepath_5 = self.properties.filepath

            if "SIX" in self.mode:
                panel_prefs.filepath_6 = self.properties.filepath
          
            if "SEVEN" in self.mode:
                panel_prefs.filepath_7 = self.properties.filepath

        else:
            panel_prefs.filepath_all = self.properties.filepath
        
        print("FILEPATH %s"%panel_prefs.filepath_0)       
        print("FILEPATH %s"%panel_prefs.filepath_1)       
        print("FILEPATH %s"%panel_prefs.filepath_2)       
        print("FILEPATH %s"%panel_prefs.filepath_3)       
        print("FILEPATH %s"%panel_prefs.filepath_4)       
        print("FILEPATH %s"%panel_prefs.filepath_5)       
        print("FILEPATH %s"%panel_prefs.filepath_6)       
        print("FILEPATH %s"%panel_prefs.filepath_7)       
        print("FILEPATH %s"%panel_prefs.filepath_all)       
        return {'FINISHED'}


    def draw(self, context):
        self.layout.operator('file.select_all_toggle')        

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
