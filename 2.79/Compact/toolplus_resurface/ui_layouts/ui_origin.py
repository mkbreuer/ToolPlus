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
from ..icons.icons import load_icons


from toolplus_resurface.ui_menus.menu_origin import (VIEW3D_TP_Origin_Panel_Menu)


def draw_origin_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)

        if not tp_props.display_origin: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_origin", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Origin")     
                      
            button_origin_bbox = icons.get("icon_origin_bbox")             
            row.menu("tp_menu.pl_menu_origin", text="", icon="LAYER_ACTIVE", icon_value=button_origin_bbox.icon_id)

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_origin", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Origin")  

            button_origin_bbox = icons.get("icon_origin_bbox")             
            row.menu("tp_menu.pl_menu_origin", text="", icon="LAYER_ACTIVE", icon_value=button_origin_bbox.icon_id)
           
  
  
  
            if context.mode == 'OBJECT':

                box = col.box().column(1)                         
                
                row = box.column(1)
                
                button_origin_center_view = icons.get("icon_origin_center_view")
                row.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

                button_origin_cursor = icons.get("icon_origin_cursor")
                row.operator("tp_ops.origin_set_cursor", text="Cursor", icon_value=button_origin_cursor.icon_id)

                row.separator()
                
                button_origin_tomesh = icons.get("icon_origin_tomesh")
                row.operator("tp_ops.origin_tomesh", text="Origin to Mesh", icon_value=button_origin_tomesh.icon_id)

                button_origin_meshto = icons.get("icon_origin_meshto")
                row.operator("tp_ops.origin_meshto", text="Mesh to Origin", icon_value=button_origin_meshto.icon_id)

                row.separator()
                
                button_origin_mass = icons.get("icon_origin_mass")           
                row.operator("tp_ops.origin_set_mass", text="Center of Mass", icon_value=button_origin_mass.icon_id)

                box.separator()
                


                box = col.box().column(1)
                row = box.row(1)
                
                if tp_props.display_origin_bbox:                     
                    
                    button_origin_bbox = icons.get("icon_origin_bbox")            
                    row.prop(tp_props, "display_origin_bbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)                     
                   
                    row.operator("object.bbox_origin_modal_ops", text="1-BBox")
              
                else:
                   
                    button_origin_bbox = icons.get("icon_origin_bbox")                
                    row.prop(tp_props, "display_origin_bbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)
                    
                    row.operator("object.bbox_origin_modal_ops", text="1-BBox")
                                
                if bpy.context.object.type == 'MESH':
                    
                    
                    if tp_props.display_origin_bbox: 
                     
                        box = col.box().column(1)     
                        box.scale_x = 0.1
                        
                        row = box.row(1)                                     
                        row.alignment ='CENTER'         
                        row.label(" +Y Axis")
                        row.separator() 
                        row.label("   xY Axis")
                        row.separator()   
                        row.label("--Y Axis")

                        #####                  
                        row = box.row(1)                                     
                        row.alignment ='CENTER'
                         
                        button_origin_left_top = icons.get("icon_origin_left_top")   
                        row.operator('tp_ops.cubeback_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
                       
                        button_origin_top = icons.get("icon_origin_top")  
                        row.operator('tp_ops.cubeback_edgetop_minus_y', text="", icon_value=button_origin_top.icon_id)
                        
                        button_origin_right_top = icons.get("icon_origin_right_top")
                        row.operator('tp_ops.cubeback_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)

                        row.separator()
                        
                        button_origin_left_top = icons.get("icon_origin_left_top")   
                        row.operator('tp_ops.cubefront_edgetop_minus_x', text="", icon_value=button_origin_left_top.icon_id)
                        
                        button_origin_top = icons.get("icon_origin_top")  
                        row.operator('tp_ops.cubefront_side_plus_z', text="", icon_value=button_origin_top.icon_id)
                        
                        button_origin_right_top = icons.get("icon_origin_right_top")
                        row.operator('tp_ops.cubefront_edgetop_plus_x', text="", icon_value=button_origin_right_top.icon_id)

                        row.separator()
                        
                        button_origin_left_top = icons.get("icon_origin_left_top")   
                        row.operator('tp_ops.cubefront_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
                        
                        button_origin_top = icons.get("icon_origin_top")  
                        row.operator('tp_ops.cubeback_edgetop_plus_y', text="", icon_value=button_origin_top.icon_id)
                        
                        button_origin_right_top = icons.get("icon_origin_right_top")
                        row.operator('tp_ops.cubefront_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)
                        
                        #####

                        row = box.row(1)                          
                        row.alignment ='CENTER' 
                        
                        button_origin_left = icons.get("icon_origin_left")
                        row.operator('tp_ops.cubefront_edgemiddle_minus_x', text="", icon_value=button_origin_left.icon_id)
                       
                        button_origin_cross = icons.get("icon_origin_cross")
                        row.operator('tp_ops.cubefront_side_plus_y', text="", icon_value=button_origin_cross.icon_id)
                        
                        button_origin_right = icons.get("icon_origin_right")
                        row.operator('tp_ops.cubefront_edgemiddle_plus_x', text="", icon_value=button_origin_right.icon_id)

                        row.separator()

                        button_origin_left = icons.get("icon_origin_left")
                        row.operator('tp_ops.cubefront_side_minus_x', text="", icon_value=button_origin_left.icon_id)
                       
                        if context.mode == 'OBJECT':
                            button_origin_diagonal = icons.get("icon_origin_diagonal")
                            row.operator('object.origin_set', text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'
                        else:
                            button_origin_diagonal = icons.get("icon_origin_diagonal")
                            row.operator('tp_ops.origin_set_editcenter', text="", icon_value=button_origin_diagonal.icon_id)
                        
                        button_origin_right = icons.get("icon_origin_right")
                        row.operator('tp_ops.cubefront_side_plus_x', text="", icon_value=button_origin_right.icon_id)

                        row.separator()
                        
                        button_origin_left = icons.get("icon_origin_left")
                        row.operator('tp_ops.cubefront_edgemiddle_minus_y', text="", icon_value=button_origin_left.icon_id)
                        
                        button_origin_cross = icons.get("icon_origin_cross")
                        row.operator('tp_ops.cubefront_side_minus_y', text="", icon_value=button_origin_cross.icon_id)
                        
                        button_origin_right = icons.get("icon_origin_right")
                        row.operator('tp_ops.cubefront_edgemiddle_plus_y', text="", icon_value=button_origin_right.icon_id)

                        #####

                        row = box.row(1)
                        row.alignment ='CENTER' 
                        
                        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                        row.operator('tp_ops.cubeback_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                        
                        button_origin_bottom = icons.get("icon_origin_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_plus_y', text="", icon_value=button_origin_bottom.icon_id)
                        
                        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                        row.operator('tp_ops.cubeback_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                        row.separator()
                        
                        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_minus_x', text="", icon_value=button_origin_left_bottom.icon_id)
                        
                        button_origin_bottom = icons.get("icon_origin_bottom")
                        row.operator('tp_ops.cubefront_side_minus_z', text="", icon_value=button_origin_bottom.icon_id)
                        
                        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_plus_x', text="", icon_value=button_origin_right_bottom.icon_id)    

                        row.separator()

                        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                        row.operator('tp_ops.cubefront_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                        
                        button_origin_bottom = icons.get("icon_origin_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_minus_y', text="", icon_value=button_origin_bottom.icon_id)
                        
                        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                        row.operator('tp_ops.cubefront_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                        box.separator()


                box = col.box().column(1) 
                 
                row = box.row(1)
                
                if tp_props.display_origin_zero:                     
                    button_align_zero = icons.get("icon_align_zero")          
                    row.prop(tp_props, "display_origin_zero", text="ZeroAxis", icon_value=button_align_zero.icon_id)                             
               
                else:
                    button_align_zero = icons.get("icon_align_zero")              
                    row.prop(tp_props, "display_origin_zero", text="ZeroAxis", icon_value=button_align_zero.icon_id)               

                if tp_props.display_origin_zero: 

                    box.separator()   

                    row = box.row(1)
                    row.prop(context.scene, 'tp_switch_axis', expand=True)
                    
                    row = box.row(1)
                    row.prop(context.scene, 'tp_switch', expand=True)

                    sub = row.row(1)
                    sub.scale_x = 0.95         
                    button_origin_apply = icons.get("icon_origin_apply")  
                    sub.operator("tp_ops.zero_axis_panel", "RUN")


                box.separator()    

                                  

            else:

                box = col.box().column(1) 
                
                row = box.column(1) 

                button_origin_center_view = icons.get("icon_origin_center_view")
                row.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

                button_origin_cursor = icons.get("icon_origin_cursor")
                row.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

                row.separator()

                button_origin_edm = icons.get("icon_origin_edm")            
                row.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

                button_origin_obj = icons.get("icon_origin_obj")   
                row.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)             

                if context.mode == 'EDIT_MESH':
                
                    row.separator()
             
                    button_origin_ccc = icons.get("icon_origin_ccc")            
                    row.operator("tp_ops.origin_ccc","3P-Center", icon_value=button_origin_ccc.icon_id)    

                    box.separator() 

                    box = col.box().column(1)
                    row = box.row(1)
                    
                    if tp_props.display_origin_editbox:                     
                        button_origin_bbox = icons.get("icon_origin_bbox")            
                        row.prop(tp_props, "display_origin_editbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)                     
                    else:
                        button_origin_bbox = icons.get("icon_origin_bbox")                
                        row.prop(tp_props, "display_origin_editbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)
                        
                    if tp_props.display_origin_editbox:        

                        box = col.box().column(1)     
                        box.scale_x = 0.1
                        
                        row = box.row(1)                                     
                        row.alignment ='CENTER'         
                        row.label(" +Y Axis")
                        row.separator() 
                        row.label("   xY Axis")
                        row.separator()   
                        row.label("--Y Axis")

                        #####                  
                        row = box.row(1)                                     
                        row.alignment ='CENTER'
                         
                        button_origin_left_top = icons.get("icon_origin_left_top")   
                        row.operator('tp_ops.cubeback_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
                       
                        button_origin_top = icons.get("icon_origin_top")  
                        row.operator('tp_ops.cubeback_edgetop_minus_y', text="", icon_value=button_origin_top.icon_id)
                        
                        button_origin_right_top = icons.get("icon_origin_right_top")
                        row.operator('tp_ops.cubeback_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)

                        row.separator()
                        
                        button_origin_left_top = icons.get("icon_origin_left_top")   
                        row.operator('tp_ops.cubefront_edgetop_minus_x', text="", icon_value=button_origin_left_top.icon_id)
                        
                        button_origin_top = icons.get("icon_origin_top")  
                        row.operator('tp_ops.cubefront_side_plus_z', text="", icon_value=button_origin_top.icon_id)
                        
                        button_origin_right_top = icons.get("icon_origin_right_top")
                        row.operator('tp_ops.cubefront_edgetop_plus_x', text="", icon_value=button_origin_right_top.icon_id)

                        row.separator()
                        
                        button_origin_left_top = icons.get("icon_origin_left_top")   
                        row.operator('tp_ops.cubefront_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
                        
                        button_origin_top = icons.get("icon_origin_top")  
                        row.operator('tp_ops.cubeback_edgetop_plus_y', text="", icon_value=button_origin_top.icon_id)
                        
                        button_origin_right_top = icons.get("icon_origin_right_top")
                        row.operator('tp_ops.cubefront_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)
                        
                        #####

                        row = box.row(1)                          
                        row.alignment ='CENTER' 
                        
                        button_origin_left = icons.get("icon_origin_left")
                        row.operator('tp_ops.cubefront_edgemiddle_minus_x', text="", icon_value=button_origin_left.icon_id)
                       
                        button_origin_cross = icons.get("icon_origin_cross")
                        row.operator('tp_ops.cubefront_side_plus_y', text="", icon_value=button_origin_cross.icon_id)
                        
                        button_origin_right = icons.get("icon_origin_right")
                        row.operator('tp_ops.cubefront_edgemiddle_plus_x', text="", icon_value=button_origin_right.icon_id)

                        row.separator()

                        button_origin_left = icons.get("icon_origin_left")
                        row.operator('tp_ops.cubefront_side_minus_x', text="", icon_value=button_origin_left.icon_id)
                       
                        if context.mode == 'OBJECT':
                            button_origin_diagonal = icons.get("icon_origin_diagonal")
                            row.operator('object.origin_set', text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'
                        else:
                            button_origin_diagonal = icons.get("icon_origin_diagonal")
                            row.operator('tp_ops.origin_set_editcenter', text="", icon_value=button_origin_diagonal.icon_id)
                        
                        button_origin_right = icons.get("icon_origin_right")
                        row.operator('tp_ops.cubefront_side_plus_x', text="", icon_value=button_origin_right.icon_id)

                        row.separator()
                        
                        button_origin_left = icons.get("icon_origin_left")
                        row.operator('tp_ops.cubefront_edgemiddle_minus_y', text="", icon_value=button_origin_left.icon_id)
                        
                        button_origin_cross = icons.get("icon_origin_cross")
                        row.operator('tp_ops.cubefront_side_minus_y', text="", icon_value=button_origin_cross.icon_id)
                        
                        button_origin_right = icons.get("icon_origin_right")
                        row.operator('tp_ops.cubefront_edgemiddle_plus_y', text="", icon_value=button_origin_right.icon_id)

                        #####

                        row = box.row(1)
                        row.alignment ='CENTER' 
                        
                        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                        row.operator('tp_ops.cubeback_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                        
                        button_origin_bottom = icons.get("icon_origin_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_plus_y', text="", icon_value=button_origin_bottom.icon_id)
                        
                        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                        row.operator('tp_ops.cubeback_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                        row.separator()
                        
                        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_minus_x', text="", icon_value=button_origin_left_bottom.icon_id)
                        
                        button_origin_bottom = icons.get("icon_origin_bottom")
                        row.operator('tp_ops.cubefront_side_minus_z', text="", icon_value=button_origin_bottom.icon_id)
                        
                        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_plus_x', text="", icon_value=button_origin_right_bottom.icon_id)    

                        row.separator()

                        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                        row.operator('tp_ops.cubefront_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                        
                        button_origin_bottom = icons.get("icon_origin_bottom")
                        row.operator('tp_ops.cubefront_edgebottom_minus_y', text="", icon_value=button_origin_bottom.icon_id)
                        
                        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                        row.operator('tp_ops.cubefront_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                        box.separator()

                else:
                    box.separator()                 


                box = col.box().column(1)
                row = box.row(1)         

                if tp_props.display_origin_zero_edm:                     
                    button_align_zero = icons.get("icon_align_zero")          
                    row.prop(tp_props, "display_origin_zero_edm", text="ZeroAxis", icon_value=button_align_zero.icon_id)                             

                else:
                    button_align_zero = icons.get("icon_align_zero")              
                    row.prop(tp_props, "display_origin_zero_edm", text="ZeroAxis", icon_value=button_align_zero.icon_id)               
                                       
                if tp_props.display_origin_zero_edm: 

                    box.separator()   

                    row = box.row(1)
                    row.prop(context.scene, 'tp_switch_axis', expand=True)       
                
                    row = box.row(1)
                    row.prop(context.scene, 'tp_switch', expand=True)
                    
                    sub = row.row(1)
                    sub.scale_x = 0.95         
                    button_origin_apply = icons.get("icon_origin_apply")  
                    sub.operator("tp_ops.zero_axis_panel", "RUN")#, icon_value=button_origin_apply.icon_id)  

                box.separator()
