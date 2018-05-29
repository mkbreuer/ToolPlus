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
from . icons.icons import load_icons


def draw_history_layout(context, layout):          
    tp_props = context.window_manager.bbox_window      
    icons = load_icons()       
  
    layout.operator_context = 'INVOKE_REGION_WIN'

    box = layout.box().column(1)  

    row = box.row(1) 
    if tp_props.display_ui_options:            
        row.prop(tp_props, "display_ui_options", text="", icon="SCRIPTWIN")
    else:
        row.prop(tp_props, "display_ui_options", text="", icon="SCRIPTWIN")                     

    button_ruler = icons.get("icon_ruler") 
    row.operator("view3d.ruler", text="Ruler", icon_value=button_ruler.icon_id)             
    row.operator("ed.undo", text="", icon="FRAME_PREV")  
    row.operator("ed.undo_history", text="", icon="COLLAPSEMENU")
    row.operator("ed.redo", text="", icon="FRAME_NEXT") 
   
    box.separator()                

    if tp_props.display_ui_options:        

        panel_prefs = context.user_preferences.addons[__package__].preferences

        col = layout.column(1)  
        box = col.box().column(1)  

        box.separator()                    

        row = box.row(1)  
        row.label("Panel Location: Shelfs")

        box.separator()
        
        row= box.row(1)
        row.prop(panel_prefs, 'tab_location', expand=True)

        box.separator()
                                           
        if panel_prefs.tab_location == 'tools':
            
            row = box.row(1)                                                
            row.prop(panel_prefs, "tools_category", text="TAB")
     
        box.separator()                    
        box = col.box().column(1) 
        box.separator()      
        
        row = box.row()
        row.label(text="ToolSet in Panel", icon ="TRIA_RIGHT")

        box.separator()

        row = box.row(1)
        row.label(text="(Un-)Hide Selection:")     
        row.prop(panel_prefs, 'tab_display_select', text="") 

        box.separator()                      
      
        row = box.row(1)      
        row.label(text="(Un-)Hide ReCoplanar:")       
        row.prop(panel_prefs, 'tab_display_apply', text="") 

        if panel_prefs.tab_display_apply == True:

            box.separator()                      
          
            row = box.row(1)      
            row.label(text="ReCoplanar UI:")    
            row.prop(panel_prefs, 'tab_recoplanar_ui', text="") 

        box.separator()                    
        box = col.box().column(1) 
        box.separator()      

        row = box.row()        
        row.label(text="Add Tools to default Menus", icon ="TRIA_RIGHT")

        box.separator()   

        row = box.row(1)           
        row.label(text="Add Bounding to Add Menu:")       
        row.prop(panel_prefs, 'tab_display_bbox_menu', text="") 
       
        box.separator()           
       
        row = box.row(1)
        row.label(text="ReCoplanar to Special Menu:")   
        row.prop(panel_prefs, 'tab_display_recoplanar_menu', text="")    
     
        box.separator()                    
        box = col.box().column(1) 
        box.separator()      
        
        row = box.column(1)  
        row.label("Bound Menu [CTRL+SHIFT+D]", icon ="COLLAPSEMENU") 
  
        box.separator()
        
        row = box.row(1)          
        row.prop(panel_prefs, 'tab_menu_bound', expand=True)
  
        box.separator()

        row = box.row(1) 
        row.operator("tp_ops.keymap_bound", text = 'KeyMap')
        row.operator('wm.url_open', text = 'Type of Events').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
        
        box.separator()                    
        box = col.box().column(1) 
        box.separator()              
                       
        row = box.row(1)  
        row.scale_y = 1.3
        wm = context.window_manager 
        row.operator("wm.restart_blender", text="Restart", icon='RECOVER_AUTO')  
        row.operator("wm.save_userpref", text="Save", icon='FILE_TICK')          

        box.separator()  