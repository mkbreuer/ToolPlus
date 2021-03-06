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

from toolplus_courier.courier_ui_main  import draw_main_title_layout
from toolplus_courier.courier_ui_mkb import draw_mkb_layout
from toolplus_courier.courier_ui_button import draw_buttons_mkb_layout                


class VIEW3D_TP_Courier_Batch(bpy.types.Operator):
    """menu operator for toolplus courier"""
    bl_idname = "tp_ops.tp_courier_batch"
    bl_label = " T+Courier"
    bl_options = {'REGISTER', 'UNDO'}
        
    def execute(self, context):
        return {'FINISHED'}


    def draw(self, context):
        layout = self.layout.column(1)  

        icons = load_icons()
        
        panel_prefs = context.user_preferences.addons[__package__].preferences
               
        col = layout.row(align=True)
   
        col = layout.row(1)  

        button_options = icons.get("icon_options")         
        col.prop(panel_prefs, 'tab_button_layout', text ="", emboss = False, icon_value=button_options.icon_id) 
        col.label("Text to 3D View") 
  
        button_restart = icons.get("icon_restart")   
        col.operator('wm.restart_blender_courier', text="", icon_value=button_restart.icon_id)   
   
        layout.separator() 
    
        scene = context.scene
        
        col = layout.column(align=True)
 
        box = col.box().column(1) 

        box.separator()

        # LAYOUT: PREFERENCES #
        if context.user_preferences.addons[__package__].preferences.tab_button_layout == True:

            row = box.row(1)          
            row.scale_x = 1.3   

            row.prop(panel_prefs, 'tab_title_or_sublines', expand =True) 

            box.separator()  

            # TITLE #
            if context.user_preferences.addons[__package__].preferences.tab_title_or_sublines == 'title':

                row = box.row(1)          
                row.scale_x = 1.3 
                  
                draw_main_title_layout(self, context, layout)

            # SUBLINES #
            else:
                draw_mkb_layout(self, context, layout)



        # LAYOUT: BUTTON #
        else:

            row = box.row(1)          
            row.scale_y = 1
            row.label("Main Title", icon ="COLLAPSEMENU")    

            if context.user_preferences.addons[__package__].preferences.tab_permanent == True:
                ico="UNLINKED"
            else:
                ico="LINKED" 
            row.prop(panel_prefs, "tab_permanent", text="", icon=ico)   
            button_run = icons.get("icon_run")         
            row.operator('tp_ops.dotextdraw', text="", icon_value=button_run.icon_id) 

            box.separator()  

            row = box.row(1)          
            row.scale_y = 1.3   
            row.prop(panel_prefs, 'dodraw', expand =True) 


            row = box.row(1)          
            row.scale_x = 1.3   
            row.scale_y = 1.3   
            draw_buttons_mkb_layout(self, context, layout)  

            box.separator()              




    def check(self, context):
        return True


    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*4, height=300)

