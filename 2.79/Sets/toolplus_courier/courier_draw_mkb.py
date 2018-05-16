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
from math import degrees
import sys
import blf
import bgl
    

   
def draw_callback_px_text_mkb(self, context):
    scene = bpy.context.scene    

    panel_prefs = bpy.context.user_preferences.addons[__package__].preferences 
   
    font_path_mkb   = blf.load(panel_prefs.filepath_all_mkb)
    font_path_0_mkb = blf.load(panel_prefs.filepath_0_mkb)
    font_path_1_mkb = blf.load(panel_prefs.filepath_1_mkb)
    font_path_2_mkb = blf.load(panel_prefs.filepath_2_mkb)
    font_path_3_mkb = blf.load(panel_prefs.filepath_3_mkb)
    font_path_4_mkb = blf.load(panel_prefs.filepath_4_mkb)
    font_path_5_mkb = blf.load(panel_prefs.filepath_5_mkb)
    font_path_6_mkb = blf.load(panel_prefs.filepath_6_mkb)
    font_path_7_mkb = blf.load(panel_prefs.filepath_7_mkb)
   
    #--------------------------------------------------------------------------------------------   
   
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
    
    #--------------------------------------------------------------------------------------------   
   
    text_width_mkb  = panel_prefs.text_width_mkb
    text_height_mkb = panel_prefs.text_height_mkb
    text_array_x_mkb = panel_prefs.text_array_x_mkb
    text_array_y_mkb = panel_prefs.text_array_y_mkb 
    text_array_y_mkb = panel_prefs.text_array_y_mkb 
    text_offset_x_mkb = panel_prefs.text_offset_x_mkb 
    text_offset_y_mkb = panel_prefs.text_offset_y_mkb     
    text_spread_y_mkb = panel_prefs.text_spread_y_mkb 

    text_all_x_mkb = panel_prefs.text_all_x_mkb 
    text_all_y_mkb = panel_prefs.text_all_y_mkb 

    text_shadow = panel_prefs.text_shadow
    text_shadow_color = panel_prefs.text_shadow_color
    text_shadow_alpha = panel_prefs.text_shadow_alpha
    text_shadow_x = panel_prefs.text_shadow_x
    text_shadow_y = panel_prefs.text_shadow_y
             
    if panel_prefs.text_l0_mkb == True:
                                              
        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_0_color_mkb = panel_prefs.text_0_color_mkb           
            bgl.glColor3f(*text_0_color_mkb)  

        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_0_width_mkb  = panel_prefs.text_0_width_mkb
            text_0_height_mkb = panel_prefs.text_0_height_mkb
        else:
            text_0_width_mkb  = panel_prefs.text_width_mkb
            text_0_height_mkb = panel_prefs.text_height_mkb      
    

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_0_array_x_mkb = panel_prefs.text_0_offset_x_mkb
            text_0_array_y_mkb = panel_prefs.text_0_offset_y_mkb              
        else:            
            text_0_array_x_mkb = panel_prefs.text_array_x_mkb
            text_0_array_y_mkb = panel_prefs.text_array_y_mkb    


        # FILEPATH #
        text_0_text_mkb = panel_prefs.text_0_text_mkb
 
        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_0_mkb = font_path_mkb
            else:
                font_id_0_mkb = font_path_0_mkb      
        else:
            font_id_0_mkb = 0                
        
        # length and height of the text line         
        fontline_0_width_mkb  = blf.dimensions(font_id_0_mkb, text_0_text_mkb)[0]/2
        fontline_0_height_mkb = blf.dimensions(font_id_0_mkb, text_0_text_mkb)[1]/2
        
        self.line_0_width_mkb = fontline_0_width_mkb     
        self.line_0_height_mkb = fontline_0_height_mkb     

        #   

        # APPLY PREFERENCES #          
        if panel_prefs.tab_center_mkb == 'middle':                
                blf.position(font_id_0_mkb, (self.REALx/2-self.line_0_width_mkb/2 +text_0_array_x_mkb+text_all_x_mkb),
                                              (self.REALy/2-self.line_0_height_mkb/2+text_0_array_y_mkb+text_all_y_mkb), 0)                                                         
                                                     
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_0_mkb, (self.REALx/2-text_0_array_x_mkb+text_all_x_mkb),
                                              (self.REALy/2+text_0_array_y_mkb+text_all_y_mkb), 0)                                  
            else:
                blf.position(font_id_0_mkb, (text_0_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_0_array_y_mkb+text_all_y_mkb), 0)            
                   
        blf.size(font_id_0_mkb, text_0_width_mkb, text_0_height_mkb)     
        blf.draw(font_id_0_mkb, text_0_text_mkb)           

        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_0_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_0_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_0_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_0_mkb, blf.SHADOW)

   
    #--------------------------------------------------------------------------------------------   


    if panel_prefs.text_l1_mkb == True:

        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_1_color_mkb = panel_prefs.text_1_color_mkb           
            bgl.glColor3f(*text_1_color_mkb)  
          

        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_1_width_mkb  = panel_prefs.text_1_width_mkb
            text_1_height_mkb = panel_prefs.text_1_height_mkb
        else:
            text_1_width_mkb  = panel_prefs.text_width_mkb
            text_1_height_mkb = panel_prefs.text_height_mkb                            


        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_1_array_x_mkb = panel_prefs.text_1_offset_x_mkb
            text_1_array_y_mkb = panel_prefs.text_1_offset_y_mkb              
        else:            
            text_1_array_x_mkb = panel_prefs.text_array_x_mkb
            text_1_array_y_mkb = panel_prefs.text_array_y_mkb                    


        # FILEPATH #
        text_1_text_mkb = panel_prefs.text_1_text_mkb   

        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_1_mkb = font_path_mkb
            else:
                font_id_1_mkb = font_path_1_mkb      
        else:
            font_id_1_mkb = 0                
        
        # length and height of the text line         
        fontline_1_width_mkb  = blf.dimensions(font_id_1_mkb, text_1_text_mkb)[0]/2
        fontline_1_height_mkb = blf.dimensions(font_id_1_mkb, text_1_text_mkb)[1]
        
        self.line_1_width_mkb = fontline_1_width_mkb     
        self.line_1_height_mkb = fontline_1_height_mkb                                    


        # APPLY PREFERENCES #          
        if panel_prefs.tab_center_mkb == 'middle':                
            blf.position(font_id_1_mkb, (self.REALx/2-self.line_1_width_mkb/2+text_1_array_x_mkb+text_all_x_mkb),        
                                          (self.REALy/2-self.line_1_height_mkb/2+text_1_array_y_mkb-text_spread_y_mkb+text_all_y_mkb), 0)         
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_1_mkb, (self.REALx/2-text_1_array_x_mkb+text_all_x_mkb),            
                                              (self.REALy/2+text_1_array_y_mkb-text_spread_y_mkb+text_all_y_mkb), 0)   
            else:
                blf.position(font_id_1_mkb, (text_1_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_1_array_y_mkb-text_spread_y_mkb+text_all_y_mkb), 0)      
                
        blf.size(font_id_1_mkb, text_1_width_mkb, text_1_height_mkb)      
        blf.draw(font_id_1_mkb, text_1_text_mkb)
  
        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_1_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_1_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_1_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_1_mkb, blf.SHADOW)


    #--------------------------------------------------------------------------------------------   
 
   
    if panel_prefs.text_l2_mkb == True:
        
        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_2_color_mkb = panel_prefs.text_2_color_mkb           
            bgl.glColor3f(*text_2_color_mkb)  
             

        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_2_width_mkb  = panel_prefs.text_2_width_mkb
            text_2_height_mkb = panel_prefs.text_2_height_mkb
        else:
            text_2_width_mkb  = panel_prefs.text_width_mkb
            text_2_height_mkb = panel_prefs.text_height_mkb                            
              

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_2_array_x_mkb = panel_prefs.text_2_offset_x_mkb
            text_2_array_y_mkb = panel_prefs.text_2_offset_y_mkb              
        else:            
            text_2_array_x_mkb = panel_prefs.text_array_x_mkb
            text_2_array_y_mkb = panel_prefs.text_array_y_mkb   


        # FILEPATH #
        text_2_text_mkb = panel_prefs.text_2_text_mkb  

        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_2_mkb = font_path_mkb
            else:
                font_id_2_mkb = font_path_2_mkb      
        else:
            font_id_2_mkb = 0                
        
        # length and height of the text line         
        fontline_2_width_mkb  = blf.dimensions(font_id_2_mkb, text_2_text_mkb)[0]/2
        fontline_2_height_mkb = blf.dimensions(font_id_2_mkb, text_2_text_mkb)[1]
        
        self.line_2_width_mkb = fontline_2_width_mkb     
        self.line_2_height_mkb = fontline_2_height_mkb                                      


        # APPLY PREFERENCES #               
        if panel_prefs.tab_center_mkb == 'middle':                    
            blf.position(font_id_2_mkb, (self.REALx/2-self.line_2_width_mkb/2+text_2_array_x_mkb+text_all_x_mkb),     
                                          (self.REALy/2-self.line_2_height_mkb/2+text_2_array_y_mkb-text_spread_y_mkb*2+text_all_y_mkb), 0)   

        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_2_mkb, (self.REALx/2-text_2_array_x_mkb+text_all_x_mkb),
                                              (self.REALy/2+text_2_array_y_mkb-text_spread_y_mkb*2+text_all_y_mkb), 0)                                                                                
            else:
                blf.position(font_id_2_mkb, (text_2_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_2_array_y_mkb-text_spread_y_mkb*2+text_all_y_mkb), 0)      
  
        blf.size(font_id_2_mkb, text_2_width_mkb, text_2_height_mkb)           
        blf.draw(font_id_2_mkb, text_2_text_mkb)

        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_2_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_2_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_2_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_2_mkb, blf.SHADOW)
            
            
    #--------------------------------------------------------------------------------------------   
  
   
    if panel_prefs.text_l3_mkb == True:

        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_3_color_mkb = panel_prefs.text_3_color_mkb           
            bgl.glColor3f(*text_3_color_mkb)  
        

        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_3_width_mkb  = panel_prefs.text_3_width_mkb
            text_3_height_mkb = panel_prefs.text_3_height_mkb
        else:
            text_3_width_mkb  = panel_prefs.text_width_mkb
            text_3_height_mkb = panel_prefs.text_height_mkb                            
              

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_3_array_x_mkb = panel_prefs.text_3_offset_x_mkb
            text_3_array_y_mkb = panel_prefs.text_3_offset_y_mkb              
        else:            
            text_3_array_x_mkb = panel_prefs.text_array_x_mkb
            text_3_array_y_mkb = panel_prefs.text_array_y_mkb    
            
       
        # FILEPATH #
        text_3_text_mkb = panel_prefs.text_3_text_mkb   

        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_3_mkb = font_path_mkb
            else:
                font_id_3_mkb = font_path_3_mkb     
        else:
            font_id_3_mkb = 0                
        
        # length and height of the text line         
        fontline_3_width_mkb  = blf.dimensions(font_id_3_mkb, text_3_text_mkb)[0]/2
        fontline_3_height_mkb = blf.dimensions(font_id_3_mkb, text_3_text_mkb)[1]
        
        self.line_3_width_mkb = fontline_3_width_mkb     
        self.line_3_height_mkb = fontline_3_height_mkb     
        

        # APPLY PREFERENCES #               
        if panel_prefs.tab_center_mkb == 'middle':                
            blf.position(font_id_3_mkb, (self.REALx/2-self.line_3_width_mkb/2+text_3_array_x_mkb+text_all_x_mkb),     
                                          (self.REALy/2-self.line_3_height_mkb/2+text_3_array_y_mkb-text_spread_y_mkb*3+text_all_y_mkb), 0)   
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_3_mkb, (self.REALx/2-text_3_array_x_mkb+text_all_x_mkb),          
                                              (self.REALy/2+text_3_array_y_mkb-text_spread_y_mkb*3+text_all_y_mkb), 0)   
            else:
                blf.position(font_id_3_mkb, (text_3_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_3_array_y_mkb-text_spread_y_mkb*3+text_all_y_mkb), 0)     
                    
        blf.size(font_id_3_mkb, text_3_width_mkb, text_3_height_mkb)
        blf.draw(font_id_3_mkb, text_3_text_mkb)
       
        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_3_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_3_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_3_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_3_mkb, blf.SHADOW)


    #--------------------------------------------------------------------------------------------   


    if panel_prefs.text_l4_mkb == True:

       
        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_4_color_mkb = panel_prefs.text_4_color_mkb           
            bgl.glColor3f(*text_4_color_mkb)  
  

        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_4_width_mkb  = panel_prefs.text_4_width_mkb
            text_4_height_mkb = panel_prefs.text_4_height_mkb
        else:
            text_4_width_mkb  = panel_prefs.text_width_mkb
            text_4_height_mkb = panel_prefs.text_height_mkb                            
              

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_4_array_x_mkb = panel_prefs.text_4_offset_x_mkb
            text_4_array_y_mkb = panel_prefs.text_4_offset_y_mkb              
        else:            
            text_4_array_x_mkb = panel_prefs.text_array_x_mkb
            text_4_array_y_mkb = panel_prefs.text_array_y_mkb  

                    
        # FILEPATH #
        text_4_text_mkb = panel_prefs.text_4_text_mkb   

        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_4_mkb = font_path_mkb
            else:
                font_id_4_mkb = font_path_4_mkb     
        else:
            font_id_4_mkb = 0                

        # length and height of the text line         
        fontline_4_width_mkb  = blf.dimensions(font_id_4_mkb, text_4_text_mkb)[0]/2
        fontline_4_height_mkb = blf.dimensions(font_id_4_mkb, text_4_text_mkb)[1]
        
        self.line_4_width_mkb = fontline_4_width_mkb     
        self.line_4_height_mkb = fontline_4_height_mkb     
      

        # APPLY PREFERENCES #                      
        if panel_prefs.tab_center_mkb == 'middle':                
            blf.position(font_id_4_mkb, (self.REALx/2-self.line_4_width_mkb/2+text_4_array_x_mkb+text_all_x_mkb),        
                                          (self.REALy/2-self.line_4_height_mkb/2+text_4_array_y_mkb-text_spread_y_mkb*4+text_all_y_mkb), 0)   
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_4_mkb, (self.REALx/2-text_4_array_x_mkb+text_all_x_mkb),           
                                              (self.REALy/2+text_4_array_y_mkb-text_spread_y_mkb*4+text_all_y_mkb), 0)   
            else:
                blf.position(font_id_4_mkb, (text_4_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_4_array_y_mkb-text_spread_y_mkb*4+text_all_y_mkb), 0)       

        blf.size(font_id_4_mkb, text_4_width_mkb, text_4_height_mkb)
        blf.draw(font_id_4_mkb, text_4_text_mkb)

        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_4_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_4_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_4_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_4_mkb, blf.SHADOW)
 
  
    #--------------------------------------------------------------------------------------------   


    if panel_prefs.text_l5_mkb == True:
        

        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_5_color_mkb = panel_prefs.text_5_color_mkb           
            bgl.glColor3f(*text_5_color_mkb)  
            

        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_5_width_mkb  = panel_prefs.text_5_width_mkb
            text_5_height_mkb = panel_prefs.text_5_height_mkb
        else:
            text_5_width_mkb  = panel_prefs.text_width_mkb
            text_5_height_mkb = panel_prefs.text_height_mkb                            
              

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_5_array_x_mkb = panel_prefs.text_5_offset_x_mkb
            text_5_array_y_mkb = panel_prefs.text_5_offset_y_mkb              
        else:            
            text_5_array_x_mkb = panel_prefs.text_array_x_mkb
            text_5_array_y_mkb = panel_prefs.text_array_y_mkb    


        # FILEPATH #
        text_5_text_mkb = panel_prefs.text_5_text_mkb   

        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_5_mkb = font_path_mkb
            else:
                font_id_5_mkb = font_path_5_mkb      
        else:
            font_id_5_mkb = 0                
        
        # length and height of the text line         
        fontline_5_width_mkb  = blf.dimensions(font_id_5_mkb, text_5_text_mkb)[0]/2
        fontline_5_height_mkb = blf.dimensions(font_id_5_mkb, text_5_text_mkb)[1]
        
        self.line_5_width_mkb = fontline_5_width_mkb     
        self.line_5_height_mkb = fontline_5_height_mkb     

                                           
        # APPLY PREFERENCES #          
        if panel_prefs.tab_center_mkb == 'middle':                
            blf.position(font_id_5_mkb, (self.REALx/2-self.line_5_width_mkb/2+text_5_array_x_mkb+text_all_x_mkb),        
                                          (self.REALy/2-self.line_5_height_mkb/2+text_5_array_y_mkb-text_spread_y_mkb*5+text_all_y_mkb), 0)   
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_5_mkb, (self.REALx/2-text_5_array_x_mkb+text_all_x_mkb),           
                                              (self.REALy/2+text_5_array_y_mkb-text_spread_y_mkb*5+text_all_y_mkb), 0)   
            else:
                blf.position(font_id_5_mkb, (text_5_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_5_array_y_mkb-text_spread_y_mkb*5+text_all_y_mkb), 0)    

        blf.size(font_id_5_mkb, text_5_width_mkb, text_5_height_mkb)
        blf.draw(font_id_5_mkb, text_5_text_mkb)

        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_5_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_5_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_5_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_5_mkb, blf.SHADOW)

 
    #--------------------------------------------------------------------------------------------   

  
    if panel_prefs.text_l6_mkb == True:


        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_6_color_mkb = panel_prefs.text_6_color_mkb           
            bgl.glColor3f(*text_6_color_mkb)  


        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_6_width_mkb  = panel_prefs.text_6_width_mkb
            text_6_height_mkb = panel_prefs.text_6_height_mkb
        else:
            text_6_width_mkb  = panel_prefs.text_width_mkb
            text_6_height_mkb = panel_prefs.text_height_mkb                            
              

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_6_array_x_mkb = panel_prefs.text_6_offset_x_mkb
            text_6_array_y_mkb = panel_prefs.text_6_offset_y_mkb              
        else:            
            text_6_array_x_mkb = panel_prefs.text_array_x_mkb
            text_6_array_y_mkb = panel_prefs.text_array_y_mkb    

        
        # FILEPATH #
        text_6_text_mkb = panel_prefs.text_6_text_mkb   

        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_6_mkb = font_path_mkb
            else:
                font_id_6_mkb = font_path_6_mkb
        else:
            font_id_6_mkb = 0                

        # length and height of the text line         
        fontline_6_width_mkb  = blf.dimensions(font_id_6_mkb, text_6_text_mkb)[0]/2
        fontline_6_height_mkb = blf.dimensions(font_id_6_mkb, text_6_text_mkb)[1]
        
        self.line_6_width_mkb = fontline_6_width_mkb     
        self.line_6_height_mkb = fontline_6_height_mkb     


        # APPLY PREFERENCES #          
        if panel_prefs.tab_center_mkb == 'middle':                
            blf.position(font_id_6_mkb, (self.REALx/2-self.line_6_width_mkb/2+text_6_array_x_mkb+text_all_x_mkb),         
                                          (self.REALy/2-self.line_6_height_mkb/2+text_6_array_y_mkb-text_spread_y_mkb*6+text_all_y_mkb), 0)   
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_6_mkb, (self.REALx/2-text_6_array_x_mkb+text_all_x_mkb),            
                                              (self.REALy/2+text_6_array_y_mkb-text_spread_y_mkb*6+text_all_y_mkb), 0)   
            else:
                blf.position(font_id_6_mkb, (text_6_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_6_array_y_mkb-text_spread_y_mkb*6+text_all_y_mkb), 0)    

        blf.size(font_id_6_mkb, text_6_width_mkb, text_6_height_mkb)
        blf.draw(font_id_6_mkb, text_6_text_mkb)


        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_6_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_6_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_6_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_6_mkb, blf.SHADOW)


    #--------------------------------------------------------------------------------------------


    if panel_prefs.text_l7_mkb == True:


        # COLOR #   
        if panel_prefs.tab_color_link_mkb == False:            
            text_color_mkb = panel_prefs.text_color_mkb           
            bgl.glColor3f(*text_color_mkb)  
        else:
            text_7_color_mkb = panel_prefs.text_7_color_mkb           
            bgl.glColor3f(*text_7_color_mkb)  


        # SCALE #      
        if panel_prefs.tab_scal_link_mkb == True:
            text_7_width_mkb  = panel_prefs.text_7_width_mkb
            text_7_height_mkb = panel_prefs.text_7_height_mkb
        else:
            text_7_width_mkb  = panel_prefs.text_width_mkb
            text_7_height_mkb = panel_prefs.text_height_mkb                            
              

        # POSITION #    
        if panel_prefs.tab_array_link_mkb == True:            
            text_7_array_x_mkb = panel_prefs.text_7_offset_x_mkb
            text_7_array_y_mkb = panel_prefs.text_7_offset_y_mkb              
        else:            
            text_7_array_x_mkb = panel_prefs.text_array_x_mkb
            text_7_array_y_mkb = panel_prefs.text_array_y_mkb    

        
        # FILEPATH #
        text_7_text_mkb = panel_prefs.text_7_text_mkb  
        
        # FONT #
        if panel_prefs.tab_font_external_mkb == False:
            if panel_prefs.tab_font_unit_mkb == False: 
                font_id_7_mkb = font_path_mkb
            else:
                font_id_7_mkb = font_path_7_mkb
        else:
            font_id_7_mkb = 0                
 
        # length and height of the text line         
        fontline_7_width_mkb  = blf.dimensions(font_id_7_mkb, text_7_text_mkb)[0]/2
        fontline_7_height_mkb = blf.dimensions(font_id_7_mkb, text_7_text_mkb)[1]
        
        self.line_7_width_mkb = fontline_7_width_mkb     
        self.line_7_height_mkb = fontline_7_height_mkb     

        # APPLY PREFERENCES #          
        if panel_prefs.tab_center_mkb == 'middle':                
            blf.position(font_id_7_mkb, (self.REALx/2-self.line_7_width_mkb/2+text_7_array_x_mkb+text_all_x_mkb),        
                                          (self.REALy/2-self.line_7_height_mkb/2+text_7_array_y_mkb-text_spread_y_mkb*7+text_all_y_mkb), 0)   
        else:
            if panel_prefs.tab_center_left_mkb == True:                 
                blf.position(font_id_7_mkb, (self.REALx/2-text_7_array_x_mkb+text_all_x_mkb),          
                                              (self.REALy/2+text_7_array_y_mkb-text_spread_y_mkb*7+text_all_y_mkb), 0)   
            else:
                blf.position(font_id_7_mkb, (text_7_array_x_mkb+20+text_all_x_mkb), 
                                              (self.REALy/2+text_7_array_y_mkb-text_spread_y_mkb*7+text_all_y_mkb), 0)       

        blf.size(font_id_7_mkb, text_7_width_mkb, text_7_height_mkb)
        blf.draw(font_id_7_mkb, text_7_text_mkb)

        # DROPSHADOW # 
        if panel_prefs.text_shadow == True:                
            blf.enable(font_id_7_mkb, blf.SHADOW)
            blf.shadow_offset(font_id_7_mkb, text_shadow_x, text_shadow_y)
            blf.shadow(font_id_7_mkb, 5, text_shadow_color[0], text_shadow_color[1], text_shadow_color[2], text_shadow_alpha)
        else:
            blf.disable(font_id_7_mkb, blf.SHADOW)

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


class VIEW3D_TP_Do_Text_Draw_Modal_mkb(bpy.types.Operator):
    """Draw Text to 3D View"""
    bl_idname = "tp_ops.do_text_draw_mkb"
    bl_label = "DoTextDraw"
    bl_options = {'REGISTER', 'UNDO'}  

    def modal(self, context, event):
        context.area.tag_redraw()

        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences     
      

        bpy.ops.tp_ops.do_nothing

        if event.type in {'ESC', 'RIGHTMOUSE'}:
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


        if panel_prefs.tab_permanent_mkb == False:           
            return {'FINISHED'}              
        else:
            return {'RUNNING_MODAL'}


    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
           
            args = (self, context)
                           
            self.handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_text_mkb, args, 'WINDOW', 'POST_PIXEL')
            
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}



class VIEW3D_TP_Reset_Menu(bpy.types.Menu):
    bl_label = "Presets"
    bl_idname = "tp_menu.reset_ops_courier_mkb"

    def draw(self, context):
        layout = self.layout


        split = layout.split()


        col = split.column()
        col.scale_y = 1.3
     
        col.operator("tp_ops.courier_preset_mkb", text="Reset").mode='default'         
   
        col.separator()  
       
        col.operator("tp_ops.courier_preset_mkb", text="Text").mode='text'
        col.operator("tp_ops.courier_preset_mkb", text="Color").mode='colors'

        col.separator()
      
        col.operator("tp_ops.courier_preset_mkb", text="Pie").mode='pie'
        col.operator("tp_ops.courier_preset_mkb", text="Checker").mode='checker'
        col.label("")  
     
        col.separator()    

        col.operator("tp_ops.courier_preset_mkb", text="Wave L").mode='wave_l'
        col.operator("tp_ops.courier_preset_mkb", text="Arrow L").mode='arrow_lr'
        col.operator("tp_ops.courier_preset_mkb", text="Diagonal L").mode='diagonal_lr'        

       

        col = split.column()   
        col.scale_y = 1.3        
            
        col.label("")    

        col.separator()  

        col.operator("tp_ops.courier_preset_mkb", text="Position").mode='position'
        col.operator("tp_ops.courier_preset_mkb", text="Sizes").mode='sizes'   
       
        col.separator()       
    
        col.operator("tp_ops.courier_preset_mkb", text="Zip").mode='zip'        
        col.operator("tp_ops.courier_preset_mkb", text="Columns").mode='columns'        
        col.operator("tp_ops.courier_preset_mkb", text="Cascade").mode='cascade'   
        
        col.separator()    

        col.operator("tp_ops.courier_preset_mkb", text="Wave R").mode='wave_r'
        col.operator("tp_ops.courier_preset_mkb", text="Arrow R").mode='arrow_rl'
        col.operator("tp_ops.courier_preset_mkb", text="Diagonal R").mode='diagonal_rl'




class VIEW3D_TP_Do_Cascade(bpy.types.Operator):
    """do cascade for further presets"""
    bl_idname = "tp_ops.do_cascade"
    bl_label = " Do Cascade" 
    bl_options = {'INTERNAL'}        

    def execute(self, context):
        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences    

        # BLOCK LINE 0 #                      
        panel_prefs.text_0_array_x_mkb = 0
        panel_prefs.text_0_array_y_mkb = 0                   
        panel_prefs.text_0_offset_x_mkb = 0                   
        panel_prefs.text_0_offset_y_mkb = 0                   

        # BLOCK LINE 1 #          
        panel_prefs.text_1_array_x_mkb = 0
        panel_prefs.text_1_array_y_mkb = 0          
        panel_prefs.text_1_offset_x_mkb = 0                   
        panel_prefs.text_1_offset_y_mkb = 0  

        # BLOCK LINE 2 #    
        panel_prefs.text_2_array_x_mkb = 0
        panel_prefs.text_2_array_y_mkb = 0          
        panel_prefs.text_2_offset_x_mkb = 0                   
        panel_prefs.text_2_offset_y_mkb = 0  

        # BLOCK LINE 3 #          
        panel_prefs.text_3_array_x_mkb = 0
        panel_prefs.text_3_array_y_mkb = 0          
        panel_prefs.text_3_offset_x_mkb = 0                   
        panel_prefs.text_3_offset_y_mkb = 0  
      
        # BLOCK LINE 4 #        
        panel_prefs.text_4_array_x_mkb = 0
        panel_prefs.text_4_array_y_mkb = 0          
        panel_prefs.text_4_offset_x_mkb = 0                   
        panel_prefs.text_4_offset_y_mkb = 0            
       
        # BLOCK LINE 5 #           
        panel_prefs.text_5_array_x_mkb = 0
        panel_prefs.text_5_array_y_mkb = 0          
        panel_prefs.text_5_offset_x_mkb = 0                   
        panel_prefs.text_5_offset_y_mkb = 0            
        
        # BLOCK LINE 6 #        
        panel_prefs.text_6_array_x_mkb = 0
        panel_prefs.text_6_array_y_mkb = 0          
        panel_prefs.text_6_offset_x_mkb = 0                   
        panel_prefs.text_6_offset_y_mkb = 0                    
       
        # BLOCK LINE 7 #         
        panel_prefs.text_7_array_x_mkb = 0
        panel_prefs.text_7_array_y_mkb = 0          
        panel_prefs.text_7_offset_x_mkb = 0                   
        panel_prefs.text_7_offset_y_mkb = 0  

        return {'FINISHED'}


# RESET PROPERTIES #
class VIEW3D_TP_Courier_Preset_mkb(bpy.types.Operator):
    """block layout presets"""
    bl_idname = "tp_ops.courier_preset_mkb"
    bl_label = "Layout Presets"
    bl_options = {'REGISTER', 'UNDO'}

    mode = bpy.props.StringProperty(default="")

    def execute(self, context):

        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences     


        if "text" in self.mode:
                        
            # BLOCK LINE 0 #  
            panel_prefs.text_0_text_mkb = "Block 0 - Title"
           
            # BLOCK LINE 1 #             
            panel_prefs.text_1_text_mkb = "Block 0 - Line 1"
           
            # BLOCK LINE 2 #             
            panel_prefs.text_2_text_mkb = "Block 0 - Line 2"    
           
            # BLOCK LINE 3 #             
            panel_prefs.text_3_text_mkb = "Block 0 - Line 3"    
          
            # BLOCK LINE 4 #            
            panel_prefs.text_4_text_mkb = "Block 0 - Line 4"    
           
            # BLOCK LINE 5 #             
            panel_prefs.text_5_text_mkb = "Block 0 - Line 5"
           
             # BLOCK LINE 6 #            
            panel_prefs.text_6_text_mkb = "Block 0 - Line 6"
           
             # BLOCK LINE 7 #             
            panel_prefs.text_7_text_mkb = "Block 0 - Line 7"            
            
            # LINK #  
            panel_prefs.tab_font_unit_mkb = False 


        if "sizes" in self.mode:

            # ALL #                        
            panel_prefs.text_width_mkb = 50
            panel_prefs.text_height_mkb = 50
        
            # BLOCK LINE 0 #                      
            panel_prefs.text_0_width_mkb = 50
            panel_prefs.text_0_height_mkb = 50                  

            # BLOCK LINE 1 #          
            panel_prefs.text_1_width_mkb = 50
            panel_prefs.text_1_height_mkb = 50

            # BLOCK LINE 2 #    
            panel_prefs.text_2_width_mkb = 50
            panel_prefs.text_2_height_mkb = 50
            
            # BLOCK LINE 3 #          
            panel_prefs.text_3_width_mkb = 50
            panel_prefs.text_3_height_mkb = 50
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_width_mkb = 50
            panel_prefs.text_4_height_mkb = 50         
           
            # BLOCK LINE 5 #           
            panel_prefs.text_5_width_mkb = 50
            panel_prefs.text_5_height_mkb = 50        
            
            # BLOCK LINE 6 #        
            panel_prefs.text_6_width_mkb = 50
            panel_prefs.text_6_height_mkb = 50                 
           
            # BLOCK LINE 7 #         
            panel_prefs.text_7_width_mkb = 50                
            panel_prefs.text_7_height_mkb = 50

            # LINK #   
            panel_prefs.tab_scal_link_mkb = False


        if "colors" in self.mode:
            
            # ALL #         
            panel_prefs.text_color_mkb = (0.5, 1, 1)   
          
            # BLOCK LINE 0 #              
            panel_prefs.text_0_color_mkb = (1, 0, 0)  
            
            # BLOCK LINE 1 #             
            panel_prefs.text_1_color_mkb = (0.9, 0, 1)  
           
            # BLOCK LINE 2 #             
            panel_prefs.text_2_color_mkb = (0, 0, 1)  
           
            # BLOCK LINE 3 #             
            panel_prefs.text_3_color_mkb = (0, 1, 1)     
          
            # BLOCK LINE 4 #             
            panel_prefs.text_4_color_mkb = (0, 1, 0)        
           
            # BLOCK LINE 5 #             
            panel_prefs.text_5_color_mkb = (1, 1, 0)  
          
            # BLOCK LINE 6 #             
            panel_prefs.text_6_color_mkb = (1, 0.5, 0)       
          
            # BLOCK LINE 7 #  
            panel_prefs.text_7_color_mkb = (1, 0.5, 1)    

        
            # LINK #   
            panel_prefs.tab_color_link_mkb = False    

        
        if "position" in self.mode:
                     
            # ALL #                        
            panel_prefs.text_array_x_mkb = 0
            panel_prefs.text_array_y_mkb = 0                 
            panel_prefs.text_all_x_mkb = 0
            panel_prefs.text_all_y_mkb = 0

        
            # BLOCK LINE 0 #                      
            panel_prefs.text_0_array_x_mkb = 0
            panel_prefs.text_0_array_y_mkb = 0                   
            panel_prefs.text_0_offset_x_mkb = 0                   
            panel_prefs.text_0_offset_y_mkb = 0                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_mkb = 0
            panel_prefs.text_1_array_y_mkb = 0          
            panel_prefs.text_1_offset_x_mkb = 0                   
            panel_prefs.text_1_offset_y_mkb = 0  

            # BLOCK LINE 2 #    
            panel_prefs.text_2_array_x_mkb = 0
            panel_prefs.text_2_array_y_mkb = 0          
            panel_prefs.text_2_offset_x_mkb = 0                   
            panel_prefs.text_2_offset_y_mkb = 0  

            # BLOCK LINE 3 #          
            panel_prefs.text_3_array_x_mkb = 0
            panel_prefs.text_3_array_y_mkb = 0          
            panel_prefs.text_3_offset_x_mkb = 0                   
            panel_prefs.text_3_offset_y_mkb = 0  
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_array_x_mkb = 0
            panel_prefs.text_4_array_y_mkb = 0          
            panel_prefs.text_4_offset_x_mkb = 0                   
            panel_prefs.text_4_offset_y_mkb = 0            
           
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_mkb = 0
            panel_prefs.text_5_array_y_mkb = 0          
            panel_prefs.text_5_offset_x_mkb = 0                   
            panel_prefs.text_5_offset_y_mkb = 0            
            
            # BLOCK LINE 6 #        
            panel_prefs.text_6_array_x_mkb = 0
            panel_prefs.text_6_array_y_mkb = 0          
            panel_prefs.text_6_offset_x_mkb = 0                   
            panel_prefs.text_6_offset_y_mkb = 0                    
           
            # BLOCK LINE 7 #         
            panel_prefs.text_7_array_x_mkb = 0
            panel_prefs.text_7_array_y_mkb = 0          
            panel_prefs.text_7_offset_x_mkb = 0                   
            panel_prefs.text_7_offset_y_mkb = 0  
            
            # LINK #              
            panel_prefs.tab_array_link_mkb = False


        if "default" in self.mode:
 
            panel_prefs.tab_permanent_mkb = False            
            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_center_left_mkb = False
            panel_prefs.tab_scal_link_mkb = False
            panel_prefs.text_offset_y_mkb = 0
            panel_prefs.tab_font_unit_mkb = False
            panel_prefs.tab_color_link_mkb = False
            panel_prefs.tab_scal_link_mkb = False
            panel_prefs.tab_array_link_mkb = False

            # TEXT #  
            panel_prefs.text_0_text_mkb = "Block 0 - Title"
            panel_prefs.text_1_text_mkb = "Block 0 - Line 1"
            panel_prefs.text_2_text_mkb = "Block 0 - Line 2"    
            panel_prefs.text_3_text_mkb = "Block 0 - Line 3"    
            panel_prefs.text_4_text_mkb = "Block 0 - Line 4"    
            panel_prefs.text_5_text_mkb = "Block 0 - Line 5"
            panel_prefs.text_6_text_mkb = "Block 0 - Line 6"
            panel_prefs.text_7_text_mkb = "Block 0 - Line 7"     

            # COLORS #  
            panel_prefs.text_color_mkb = (0.5, 1, 1)   
            panel_prefs.text_0_color_mkb = (1, 0, 0)  
            panel_prefs.text_1_color_mkb = (0.9, 0, 1)  
            panel_prefs.text_2_color_mkb = (0, 0, 1)  
            panel_prefs.text_3_color_mkb = (0, 1, 1)     
            panel_prefs.text_4_color_mkb = (0, 1, 0)        
            panel_prefs.text_5_color_mkb = (1, 1, 0)  
            panel_prefs.text_6_color_mkb = (1, 0.5, 0)       
            panel_prefs.text_7_color_mkb = (1, 0.5, 1)    

            # BLOCK ALL #                        
            panel_prefs.text_width_mkb = 50
            panel_prefs.text_height_mkb = 50
            panel_prefs.text_array_x_mkb = 0
            panel_prefs.text_array_y_mkb = 0          
       
            panel_prefs.text_all_x_mkb = 0
            panel_prefs.text_all_y_mkb = 0
            panel_prefs.tab_view_mkb = False
        
            # BLOCK LINE 0 #                      
            panel_prefs.text_0_width_mkb = 50
            panel_prefs.text_0_height_mkb = 50
            panel_prefs.text_0_array_x_mkb = 0
            panel_prefs.text_0_array_y_mkb = 0                   
            panel_prefs.text_0_offset_x_mkb = 0                   
            panel_prefs.text_0_offset_y_mkb = 0                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_width_mkb = 50
            panel_prefs.text_1_height_mkb = 50
            panel_prefs.text_1_array_x_mkb = 0
            panel_prefs.text_1_array_y_mkb = 0          
            panel_prefs.text_1_offset_x_mkb = 0                   
            panel_prefs.text_1_offset_y_mkb = 0  

            # BLOCK LINE 2 #    
            panel_prefs.text_2_width_mkb = 50
            panel_prefs.text_2_height_mkb = 50
            panel_prefs.text_2_array_x_mkb = 0
            panel_prefs.text_2_array_y_mkb = 0          
            panel_prefs.text_2_offset_x_mkb = 0                   
            panel_prefs.text_2_offset_y_mkb = 0  

            # BLOCK LINE 3 #          
            panel_prefs.text_3_width_mkb = 50
            panel_prefs.text_3_height_mkb = 50
            panel_prefs.text_3_array_x_mkb = 0
            panel_prefs.text_3_array_y_mkb = 0          
            panel_prefs.text_3_offset_x_mkb = 0                   
            panel_prefs.text_3_offset_y_mkb = 0  
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_width_mkb = 50
            panel_prefs.text_4_height_mkb = 50
            panel_prefs.text_4_array_x_mkb = 0
            panel_prefs.text_4_array_y_mkb = 0          
            panel_prefs.text_4_offset_x_mkb = 0                   
            panel_prefs.text_4_offset_y_mkb = 0            
           
            # BLOCK LINE 5 #           
            panel_prefs.text_5_width_mkb = 50
            panel_prefs.text_5_height_mkb = 50
            panel_prefs.text_5_array_x_mkb = 0
            panel_prefs.text_5_array_y_mkb = 0          
            panel_prefs.text_5_offset_x_mkb = 0                   
            panel_prefs.text_5_offset_y_mkb = 0            
            
            # BLOCK LINE 6 #        
            panel_prefs.text_6_width_mkb = 50
            panel_prefs.text_6_height_mkb = 50
            panel_prefs.text_6_array_x_mkb = 0
            panel_prefs.text_6_array_y_mkb = 0          
            panel_prefs.text_6_offset_x_mkb = 0                   
            panel_prefs.text_6_offset_y_mkb = 0                    
           
            # BLOCK LINE 7 #         
            panel_prefs.text_7_width_mkb = 50                
            panel_prefs.text_7_height_mkb = 50
            panel_prefs.text_7_array_x_mkb = 0
            panel_prefs.text_7_array_y_mkb = 0          
            panel_prefs.text_7_offset_x_mkb = 0                   
            panel_prefs.text_7_offset_y_mkb = 0  
            

        if "cascade" in self.mode:
                     
            # BLOCK LINE 0 #                      
            panel_prefs.text_0_array_x_mkb = 0
            panel_prefs.text_0_array_y_mkb = 0                   
            panel_prefs.text_0_offset_x_mkb = 0                   
            panel_prefs.text_0_offset_y_mkb = 0                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_mkb = 0
            panel_prefs.text_1_array_y_mkb = 0          
            panel_prefs.text_1_offset_x_mkb = 0                   
            panel_prefs.text_1_offset_y_mkb = 0  

            # BLOCK LINE 2 #    
            panel_prefs.text_2_array_x_mkb = 0
            panel_prefs.text_2_array_y_mkb = 0          
            panel_prefs.text_2_offset_x_mkb = 0                   
            panel_prefs.text_2_offset_y_mkb = 0  

            # BLOCK LINE 3 #          
            panel_prefs.text_3_array_x_mkb = 0
            panel_prefs.text_3_array_y_mkb = 0          
            panel_prefs.text_3_offset_x_mkb = 0                   
            panel_prefs.text_3_offset_y_mkb = 0  
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_array_x_mkb = 0
            panel_prefs.text_4_array_y_mkb = 0          
            panel_prefs.text_4_offset_x_mkb = 0                   
            panel_prefs.text_4_offset_y_mkb = 0            
           
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_mkb = 0
            panel_prefs.text_5_array_y_mkb = 0          
            panel_prefs.text_5_offset_x_mkb = 0                   
            panel_prefs.text_5_offset_y_mkb = 0            
            
            # BLOCK LINE 6 #        
            panel_prefs.text_6_array_x_mkb = 0
            panel_prefs.text_6_array_y_mkb = 0          
            panel_prefs.text_6_offset_x_mkb = 0                   
            panel_prefs.text_6_offset_y_mkb = 0                    
           
            # BLOCK LINE 7 #         
            panel_prefs.text_7_array_x_mkb = 0
            panel_prefs.text_7_array_y_mkb = 0          
            panel_prefs.text_7_offset_x_mkb = 0                   
            panel_prefs.text_7_offset_y_mkb = 0  
            

        if "diagonal_lr" in self.mode:

            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = -110                 

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = -90      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = -60       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = -30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = 30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = 90


        if "diagonal_rl" in self.mode:
            
            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = 110                 

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = 90      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = 60       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = 30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = -30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = -60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = -90


        if "wave_l" in self.mode:

            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = -60                

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = -30      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = 0       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = -30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = -60       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = -30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 0        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = -30

        
        if "wave_r" in self.mode:

            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = 60                

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = 30      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = 0       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = 30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 60       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = 30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 0        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = 30


        if "arrow_lr" in self.mode:
            
            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = -90               

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = -60      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = -30       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = 0        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = -30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = -60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = -90



        if "arrow_rl" in self.mode:
            
            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = 90               

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = 60      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = 30       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = 0        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = 30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = 90



        if "checker" in self.mode:
            
            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = -150                        

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = -150      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = -150           

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = -150             
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 150     
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = 150         
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 150             
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = 150            
         

            
        if "columns" in self.mode:            

            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = -130                        
            panel_prefs.text_0_offset_y_mkb = 0                                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = -130      
            panel_prefs.text_1_offset_y_mkb = 0      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = -130           
            panel_prefs.text_2_offset_y_mkb = 0           

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = -130             
            panel_prefs.text_3_offset_y_mkb = 0             
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 130     
            panel_prefs.text_4_offset_y_mkb = 205     
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = 130        
            panel_prefs.text_5_offset_y_mkb = 200        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 130        
            panel_prefs.text_6_offset_y_mkb = 200       
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = 130            
            panel_prefs.text_7_offset_y_mkb = 200  
            

            
        if "zip" in self.mode:

            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_offset_x_mkb = -60                                    
            panel_prefs.text_0_offset_y_mkb = 20                        

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = -60      
            panel_prefs.text_1_offset_y_mkb = 0      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = -60           
            panel_prefs.text_2_offset_y_mkb = -20           

            # BLOCK LINE 3 #         
            panel_prefs.text_3_offset_x_mkb = -60             
            panel_prefs.text_3_offset_y_mkb = -40             
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_offset_x_mkb = 60     
            panel_prefs.text_4_offset_y_mkb = 185     
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_offset_x_mkb = 60        
            panel_prefs.text_5_offset_y_mkb = 165        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = 60        
            panel_prefs.text_6_offset_y_mkb = 145       
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_offset_x_mkb = 60            
            panel_prefs.text_7_offset_y_mkb = 125  



        if "pie" in self.mode:

            bpy.ops.tp_ops.do_cascade()

            panel_prefs.tab_center_mkb = 'middle'
            panel_prefs.tab_array_link_mkb = True
        
            # BLOCK LINE 0 #              
            panel_prefs.text_0_offset_x_mkb = -250
            panel_prefs.text_0_offset_y_mkb = 0                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_offset_x_mkb = 250
            panel_prefs.text_1_offset_y_mkb = 55          

            # BLOCK LINE 2 #   
            panel_prefs.text_2_offset_x_mkb = 0
            panel_prefs.text_2_offset_y_mkb = -50         

            # BLOCK LINE 3 #            
            panel_prefs.text_3_offset_x_mkb = 0
            panel_prefs.text_3_offset_y_mkb = 300          
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_offset_x_mkb = -160
            panel_prefs.text_4_offset_y_mkb = 275          
          
            # BLOCK LINE 5 #        
            panel_prefs.text_5_offset_x_mkb = 140
            panel_prefs.text_5_offset_y_mkb = 325          
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_offset_x_mkb = -160
            panel_prefs.text_6_offset_y_mkb = 235          
                  
            # BLOCK LINE 7 #        
            panel_prefs.text_7_offset_x_mkb = 140
            panel_prefs.text_7_offset_y_mkb = 285
               

        return {"FINISHED"}




class VIEW_3D_TP_Courier_Filepath_mkb(bpy.types.Operator):
    """select *.ttf font files for text"""
    bl_idname = "tp_ops.path_courier_font_mkb"
    bl_label = "Select a *.ttf file"

    filename_ext = ".ttf"
    filter_glob = StringProperty(default="*.ttf", options={'HIDDEN'})    

    filepath = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default="")
    files = CollectionProperty( name="File Path",type=bpy.types.OperatorFileListElement )    
                                   
    mode = bpy.props.StringProperty(default="")

    def execute(self, context):
        
        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences    
      
        if panel_prefs.tab_font_unit_mkb == True: 
            
            if "ZERO_LINE" in self.mode:
                panel_prefs.filepath_0_mkb = self.properties.filepath

            if "ONE_LINE" in self.mode:           
                panel_prefs.filepath_1_mkb = self.properties.filepath

            if "TWO_LINE" in self.mode:
                panel_prefs.filepath_2_mkb = self.properties.filepath

            if "THREE_LINE" in self.mode:
                panel_prefs.filepath_3_mkb = self.properties.filepath

            if "FOUR_LINE" in self.mode:                
                panel_prefs.filepath_4_mkb = self.properties.filepath

            if "FIVE_LINE" in self.mode:
                panel_prefs.filepath_5_mkb = self.properties.filepath

            if "SIX_LINE" in self.mode:
                panel_prefs.filepath_6_mkb = self.properties.filepath
          
            if "SEVEN_LINE" in self.mode:
                panel_prefs.filepath_7_mkb = self.properties.filepath
            
            if "EMPTY_LINE" in self.mode:
                pass

        else:
            panel_prefs.filepath_all_mkb = self.properties.filepath
     
        print("FILEPATH %s"%panel_prefs.filepath_0_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_1_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_2_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_3_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_4_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_5_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_6_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_7_mkb)       
        print("FILEPATH %s"%panel_prefs.filepath_all_mkb)      
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








