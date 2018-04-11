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



class VIEW3D_TP_Header_Options_Buttons(bpy.types.Menu):
    bl_label = "Hide/Show > Buttons"
    bl_idname = "VIEW3D_TP_Header_Options_Buttons"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5     

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        expand = panel_prefs.expand_panel_tools
 
        layout.prop(panel_prefs, 'tab_display_ruler', text="")
        layout.prop(panel_prefs, 'tab_display_objects', text="")
        layout.prop(panel_prefs, 'tab_display_snap', text="")
        layout.prop(panel_prefs, 'tab_display_snapset', text="")
        layout.prop(panel_prefs, 'tab_display_shading', text="")
        layout.prop(panel_prefs, 'tab_display_advanced', text="")

        layout.prop(panel_prefs, 'tab_display_point_distance', text="")
        layout.prop(panel_prefs, 'tab_display_point_move', text="")
        layout.prop(panel_prefs, 'tab_display_roto_move', text="")
        layout.prop(panel_prefs, 'tab_display_point_scale', text="")
        layout.prop(panel_prefs, 'tab_display_point_align', text="")
        layout.prop(panel_prefs, 'tab_display_snapline', text="")

        layout.prop(panel_prefs, 'tab_display_history', text="")
        layout.prop(panel_prefs, 'tab_display_save', text="")
        layout.prop(panel_prefs, 'tab_display_view', text="")
        layout.prop(panel_prefs, 'tab_display_window', text="")


class VIEW3D_TP_Header_Options_Buttons_Menu(bpy.types.Menu):
    bl_label = "Hide/Show > Menus"
    bl_idname = "VIEW3D_TP_Header_Options_Buttons_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5     

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        expand = panel_prefs.expand_panel_tools
 
        layout.prop(panel_prefs, 'tab_display_custom', text="")
        layout.prop(panel_prefs, 'tab_display_ruler', text="")
        layout.prop(panel_prefs, 'tab_display_snap', text="")
        layout.prop(panel_prefs, 'tab_display_snapset', text="")
        layout.prop(panel_prefs, 'tab_display_origin', text="")
        layout.prop(panel_prefs, 'tab_display_advanced', text="")
        layout.prop(panel_prefs, 'tab_display_station', text="")
        layout.prop(panel_prefs, 'tab_display_objects', text="")
        layout.prop(panel_prefs, 'tab_display_shading', text="")



class VIEW3D_TP_Header_Options_Menu(bpy.types.Menu):
    bl_label = "Header Tools UI"
    bl_idname = "VIEW3D_TP_Header_Options_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5      
     
        #layout.prop(tp_props, "display_help", text="View Help", icon='INFO')    
        #layout.operator("wm.url_open", text="Open Wiki", icon='QUESTION').url = "https://github.com/mkbreuer/ToolPlus/wiki"             

        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')   
        #layout.operator("wm.restart_blender", text="Restart", icon='LOAD_FACTORY')  

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        expand = panel_prefs.expand_panel_tools

        layout.separator() 

        display_button_menu = context.user_preferences.addons[addon_key].preferences.tab_display_buttons
        if display_button_menu == 'on':  

            layout.menu("VIEW3D_TP_Header_Options_Buttons") 
            
            layout.separator()          

        else:

            layout.prop(panel_prefs, 'tab_display_name', text="")
            
            layout.menu("VIEW3D_TP_Header_Options_Buttons_Menu")            
           
            layout.separator()  
        
        #layout.prop(panel_prefs, 'tab_display_options', text="")
        layout.prop(panel_prefs, 'tab_display_buttons', text="")
        #layout.prop(panel_prefs, 'tab_display_bottom', text="")








        
 