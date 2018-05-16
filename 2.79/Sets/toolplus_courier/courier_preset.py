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


# PRESETS #
class VIEW3D_TP_Preset_Courier(bpy.types.Operator):
    """add preset or reset properties to default values"""
    bl_idname = "tp_ops.preset_for_courier"
    bl_label = "Reset Values"
    bl_options = {'REGISTER', 'UNDO'}
 
    mode = bpy.props.StringProperty(default="")

    def execute(self, context):

        panel_prefs = bpy.context.user_preferences.addons[__package__].preferences     


        if "default" in self.mode:
 
            panel_prefs.tab_permanent_sub_0 = False
            
            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_center_left_sub_0 = False
            panel_prefs.tab_array_link_sub_0 = False
            panel_prefs.tab_scal_link_sub_0 = False
            panel_prefs.text_offset_y_sub_0 = 0
            panel_prefs.tab_font_unit_sub_0 = False
            panel_prefs.tab_color_link_sub_0 = False
            panel_prefs.tab_scal_link_sub_0 = False


            # BLOCK ALL #                        
            panel_prefs.text_width_sub_0 = 50
            panel_prefs.text_height_sub_0 = 50
            panel_prefs.text_array_x_sub_0 = 0
            panel_prefs.text_array_y_sub_0 = 0          
            panel_prefs.text_color_sub_0 = (0.5, 1, 1)          
            panel_prefs.text_all_x_sub_0 = False 
            panel_prefs.text_all_y_sub_0 = False
            panel_prefs.tab_view_sub_0 = False
        
            # BLOCK LINE 0 #              
            panel_prefs.text_0_text_sub_0 = "Block 0 - Title"
            panel_prefs.text_0_color_sub_0 = (1, 0, 0)          
            panel_prefs.text_0_width_sub_0 = 50
            panel_prefs.text_0_height_sub_0 = 50
            panel_prefs.text_0_array_x_sub_0 = 0
            panel_prefs.text_0_array_y_sub_0 = 0                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_text_sub_0 = "Block 0 - Line 1"
            panel_prefs.text_1_color_sub_0 = (0.9, 0, 1)  
            panel_prefs.text_1_width_sub_0 = 50
            panel_prefs.text_1_height_sub_0 = 50
            panel_prefs.text_1_array_x_sub_0 = 0
            panel_prefs.text_1_array_y_sub_0 = 0          

            # BLOCK LINE 2 #   
            panel_prefs.text_2_text_sub_0 = "Block 0 - Line 2"
            panel_prefs.text_2_color_sub_0 = (0, 0, 1)   
            panel_prefs.text_2_width_sub_0 = 50
            panel_prefs.text_2_height_sub_0 = 50
            panel_prefs.text_2_array_x_sub_0 = 0
            panel_prefs.text_2_array_y_sub_0 = 0          

            # BLOCK LINE 3 #         
            panel_prefs.text_3_color_sub_0 = (0, 1, 1)   
            panel_prefs.text_3_text_sub_0 = "Block 0 - Line 3"
            panel_prefs.text_3_width_sub_0 = 50
            panel_prefs.text_3_height_sub_0 = 50
            panel_prefs.text_3_array_x_sub_0 = 0
            panel_prefs.text_3_array_y_sub_0 = 0          
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_text_sub_0 = "Block 0 - Line 4"
            panel_prefs.text_4_color_sub_0 = (0, 1, 0)     
            panel_prefs.text_4_width_sub_0 = 50
            panel_prefs.text_4_height_sub_0 = 50
            panel_prefs.text_4_array_x_sub_0 = 0
            panel_prefs.text_4_array_y_sub_0 = 0          
          
            # BLOCK LINE 5 #        
            panel_prefs.text_5_text_sub_0 = "Block 0 - Line 5"
            panel_prefs.text_5_color_sub_0 = (1, 1, 0)     
            panel_prefs.text_5_width_sub_0 = 50
            panel_prefs.text_5_height_sub_0 = 50
            panel_prefs.text_5_array_x_sub_0 = 0
            panel_prefs.text_5_array_y_sub_0 = 0          
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_text_sub_0 = "Block 0 - Line 6"
            panel_prefs.text_6_color_sub_0 = (1, 0.5, 0)  
            panel_prefs.text_6_width_sub_0 = 50
            panel_prefs.text_6_height_sub_0 = 50
            panel_prefs.text_6_array_x_sub_0 = 0
            panel_prefs.text_6_array_y_sub_0 = 0          
                  
            # BLOCK LINE 7 #        
            panel_prefs.text_7_text_sub_0 = "Block 0 - Line 7"
            panel_prefs.text_7_color_sub_0 = (1, 0.5, 1)    
            panel_prefs.text_7_width_sub_0 = 50                
            panel_prefs.text_7_height_sub_0 = 50
            panel_prefs.text_7_array_x_sub_0 = 0
            panel_prefs.text_7_array_y_sub_0 = 0          



        if "diagonal_lr" in self.mode:

            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = -110                 

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -90      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = -60       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = -30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = 30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = 60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = 90


        if "diagonal_rl" in self.mode:
            
            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = 110                 

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -90      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = 60       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = 30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = -30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = -60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = -90


        if "wave" in self.mode:

            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = -60                

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -30      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = 0       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = -30        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = -60       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = -30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = 0        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = -30


        if "arrow_lr" in self.mode:
            
            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = -90               

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -60      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = -30       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = 0        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = -30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = -60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = -90


        if "arrow_rl" in self.mode:
            
            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = 90               

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = 60      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = 30       

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = 0        
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 0       
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = 30        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = 60        
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = 90


        if "checker" in self.mode:
            
            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = -150                        

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -150      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = -150           

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = -150             
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 150     
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = 150         
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = 150             
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = 150            
         
            

        if "two_blocks" in self.mode:            

            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = -155                        

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -150      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = -150           

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = -150             
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 150     
            panel_prefs.text_4_array_y_sub_0 = 226     
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = 150        
            panel_prefs.text_5_array_y_sub_0 = 214        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = 150        
            panel_prefs.text_6_array_y_sub_0 = 210       
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = 150            
            panel_prefs.text_7_array_y_sub_0 = 204  
            
            
        if "zip" in self.mode:

            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #                   
            panel_prefs.text_0_array_x_sub_0 = -60                                    
            panel_prefs.text_0_array_y_sub_0 = 20                        

            # BLOCK LINE 1 #          
            panel_prefs.text_1_array_x_sub_0 = -60      
            panel_prefs.text_1_array_y_sub_0 = 0      

            # BLOCK LINE 2 #   
            panel_prefs.text_2_array_x_sub_0 = -60           
            panel_prefs.text_2_array_y_sub_0 = -20           

            # BLOCK LINE 3 #         
            panel_prefs.text_3_array_x_sub_0 = -60             
            panel_prefs.text_3_array_y_sub_0 = -40             
          
            # BLOCK LINE 4 #          
            panel_prefs.text_4_array_x_sub_0 = 60     
            panel_prefs.text_4_array_y_sub_0 = 185     
          
            # BLOCK LINE 5 #           
            panel_prefs.text_5_array_x_sub_0 = 60        
            panel_prefs.text_5_array_y_sub_0 = 165        
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_array_x_sub_0 = 60        
            panel_prefs.text_6_array_y_sub_0 = 145       
                  
            # BLOCK LINE 7 #          
            panel_prefs.text_7_array_x_sub_0 = 60            
            panel_prefs.text_7_array_y_sub_0 = 125  


        if "pie" in self.mode:

            panel_prefs.tab_center_sub_0 = 'middle'
            panel_prefs.tab_array_link_sub_0 = True
        
            # BLOCK LINE 0 #              
            panel_prefs.text_0_text_sub_0 = "Block 0 - Pie 1"
            panel_prefs.text_0_array_x_sub_0 = -250
            panel_prefs.text_0_array_y_sub_0 = 0                   

            # BLOCK LINE 1 #          
            panel_prefs.text_1_text_sub_0 = "Block 0 - Pie 2"
            panel_prefs.text_1_array_x_sub_0 = 250
            panel_prefs.text_1_array_y_sub_0 = 55          

            # BLOCK LINE 2 #   
            panel_prefs.text_2_text_sub_0 = "Block 0 - Pie 3"
            panel_prefs.text_2_array_x_sub_0 = 0
            panel_prefs.text_2_array_y_sub_0 = -50         

            # BLOCK LINE 3 #         
            panel_prefs.text_3_color_sub_0 = (0, 1, 1)   
            panel_prefs.text_3_text_sub_0 = "Block 0 - Pie 4"
            panel_prefs.text_3_array_x_sub_0 = 0
            panel_prefs.text_3_array_y_sub_0 = 300          
          
            # BLOCK LINE 4 #        
            panel_prefs.text_4_text_sub_0 = "Block 0 - Pie 5"
            panel_prefs.text_4_array_x_sub_0 = -160
            panel_prefs.text_4_array_y_sub_0 = 275          
          
            # BLOCK LINE 5 #        
            panel_prefs.text_5_text_sub_0 = "Block 0 - Pie 6"
            panel_prefs.text_5_array_x_sub_0 = 140
            panel_prefs.text_5_array_y_sub_0 = 325          
          
            # BLOCK LINE 6 #       
            panel_prefs.text_6_text_sub_0 = "Block 0 - Pie 7"
            panel_prefs.text_6_array_x_sub_0 = -160
            panel_prefs.text_6_array_y_sub_0 = 235          
                  
            # BLOCK LINE 7 #        
            panel_prefs.text_7_text_sub_0 = "Block 0 - Pie 8"
            panel_prefs.text_7_array_x_sub_0 = 140
            panel_prefs.text_7_array_y_sub_0 = 285
               

        return {"FINISHED"}

