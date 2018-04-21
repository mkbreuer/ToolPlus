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
from .. icons.icons import load_icons

import addon_utils    
    
def draw_history_tools(context, layout):
    
    icons = load_icons()
   
    scene = context.scene   
    
    tp_props = context.window_manager.tp_collapse_align  
   
    layout.operator_context = 'INVOKE_REGION_WIN'

    col = layout.column(align=True)        

    box = col.box().column(1)  
    
    row = box.row(1)
    if tp_props.display_align_options:            
        row.prop(tp_props, "display_align_options", text="", icon="SCRIPTWIN")
    else:
        row.prop(tp_props, "display_align_options", text="", icon="SCRIPTWIN")      

    button_ruler_triangle = icons.get("icon_ruler_triangle") 
    row.operator("view3d.ruler", text="Ruler", icon_value=button_ruler_triangle.icon_id)  

    row.operator("ed.undo", text="", icon="FRAME_PREV")
    row.operator("ed.undo_history", text="History", icon="COLLAPSEMENU")
    row.operator("ed.redo", text="", icon="FRAME_NEXT") 

    if tp_props.display_align_options: 

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
   

        box.separator() 

        row = box.row(1)  
        row.prop(scene, 'tp_align', expand = True)
    

        if scene.tp_align == "tp_01": 
      
            box.separator() 

            row = box.column(1)
            row.label("Panel Location")                                  
                        
            row = box.column(1)
            row.prop(panel_prefs, 'tab_location_align', expand=True)
          
            box.separator()                         
          
            row = box.row(1)
            row.prop(panel_prefs, "tools_category_align")

            box.separator() 

            row = box.row(1)
            row.label("Panel Tools")
            
            row = box.column_flow(2)

            row.prop(panel_prefs, 'tab_origin')
            row.prop(panel_prefs, 'tab_align_to')
            row.prop(panel_prefs, 'tab_aligner')

            if context.mode =='OBJECT':
                row.prop(panel_prefs, 'tab_zero_to')
                row.prop(panel_prefs, 'tab_station')

            row.prop(panel_prefs, 'tab_interpolate')
            row.prop(panel_prefs, 'tab_mirror')
            row.prop(panel_prefs, 'tab_automirror')

            if context.mode =='EDIT_MESH':
                
                row.prop(panel_prefs, 'tab_looptools')
                row.prop(panel_prefs, 'tab_relax')
                row.prop(panel_prefs, 'tab_edger')
                row.prop(panel_prefs, 'tab_vertices')
                row.prop(panel_prefs, 'tab_machine')


            box.separator() 


        if scene.tp_align == "tp_02": 

            box.separator() 

            row = box.row(1)
            row.label("Menu Tools")
            
            row = box.column_flow(2)

            row.prop(panel_prefs, 'tab_pivot_menu')
            row.prop(panel_prefs, 'tab_origin_menu')
            row.prop(panel_prefs, 'tab_align_to_menu')
            row.prop(panel_prefs, 'tab_aligner_menu')

            if context.mode =='OBJECT':
                row.prop(panel_prefs, 'tab_zero_to_menu')
                row.prop(panel_prefs, 'tab_station_menu')

            row.prop(panel_prefs, 'tab_interpolate_menu')
            row.prop(panel_prefs, 'tab_mirror_menu')
            row.prop(panel_prefs, 'tab_automirror_menu')

            if context.mode =='EDIT_MESH':
                
                row.prop(panel_prefs, 'tab_tinycad_menu')
                row.prop(panel_prefs, 'tab_looptools_menu')
                row.prop(panel_prefs, 'tab_relax_menu')
                row.prop(panel_prefs, 'tab_edger_menu')
                row.prop(panel_prefs, 'tab_space_menu')
                row.prop(panel_prefs, 'tab_machine_menu')


            box.separator() 



        if scene.tp_align == "tp_03": 
                
            box.separator() 

            row = box.row(1)
            row.label("Align Menu [SHIFT+Y]")
            
            row = box.row(1)
            row.prop(panel_prefs, 'tab_menu_align', expand=True)

            box.separator() 
            box.separator() 

            row = box.row(1)
            row.label("Origin Menu [CTRL+D]")

            row = box.row(1)
            row.prop(panel_prefs, 'tab_menu_view_origin', expand=True)

            row = box.row(1)
            row.prop(panel_prefs, 'tab_origin_adv')
           
            box.separator() 
            box.separator() 
                    
            row = box.row(1)
            row.label("Relax Menu [CTRL+SHIFT+W]")

            row = box.row(1)
            row.prop(panel_prefs, 'tab_menu_view_relax', expand=True)

            box.separator() 


            meshmaschine_addon = "MESHmachine" 
            state = addon_utils.check(meshmaschine_addon)
            if not state[0]:
                pass
            else:   
                box.separator() 

                row = box.row(1)
                row.label("MESHmachine [SHIFT+X]")
                
                row = box.row(1)
                row.prop(panel_prefs, 'tab_menu_machine', expand=True)

                row = box.row(1)
                row.label("to special [W]")

                row = box.row(1)
                row.prop(panel_prefs, 'tab_submenu_machine', expand=True)

                box.separator() 

           


 
        box.separator() 
         
        row = box.row(1)        
        wm = context.window_manager    
        row.operator("wm.save_userpref", icon='FILE_TICK')  

        box.separator()   
  