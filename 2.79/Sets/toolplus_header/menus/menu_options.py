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
 
        layout.prop(panel_prefs, 'tab_display_ruler')
        layout.prop(panel_prefs, 'tab_display_objects')
        layout.prop(panel_prefs, 'tab_display_snap')
        layout.prop(panel_prefs, 'tab_display_snapset')
        layout.prop(panel_prefs, 'tab_display_shading')
        layout.prop(panel_prefs, 'tab_display_advanced')

        layout.prop(panel_prefs, 'tab_display_point_distance')
        layout.prop(panel_prefs, 'tab_display_point_move')
        layout.prop(panel_prefs, 'tab_display_roto_move')
        layout.prop(panel_prefs, 'tab_display_point_scale')
        layout.prop(panel_prefs, 'tab_display_point_align')
        layout.prop(panel_prefs, 'tab_display_snapline')

        layout.prop(panel_prefs, 'tab_display_history')
        layout.prop(panel_prefs, 'tab_display_save')
        layout.prop(panel_prefs, 'tab_display_view')
        layout.prop(panel_prefs, 'tab_display_window')


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
 
        layout.prop(panel_prefs, 'tab_display_custom')
        layout.prop(panel_prefs, 'tab_display_ruler')
        layout.prop(panel_prefs, 'tab_display_snap')
        layout.prop(panel_prefs, 'tab_display_snapset')
        layout.prop(panel_prefs, 'tab_display_origin')
        layout.prop(panel_prefs, 'tab_display_advanced')
        layout.prop(panel_prefs, 'tab_display_station')
        layout.prop(panel_prefs, 'tab_display_objects')
        layout.prop(panel_prefs, 'tab_display_shading')



class VIEW3D_TP_Header_Options_Menu(bpy.types.Menu):
    bl_label = "Header Tools UI"
    bl_idname = "VIEW3D_TP_Header_Options_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5      
     
        #layout.operator("wm.url_open", text="Open Wiki", icon='QUESTION').url = "https://github.com/mkbreuer/ToolPlus/wiki"             

        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')   
        #layout.operator("wm.restart_blender", text="Restart", icon='LOAD_FACTORY')  

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences

        layout.separator() 

        display_button_menu = context.user_preferences.addons[addon_key].preferences.tab_display_buttons
        if display_button_menu == True:  

            layout.menu("VIEW3D_TP_Header_Options_Buttons") 
            
            layout.separator()          

        else:

            layout.prop(panel_prefs, 'tab_display_name', text="")
            
            layout.menu("VIEW3D_TP_Header_Options_Buttons_Menu")            
           
            layout.separator()  
        

        layout.prop(panel_prefs, 'tab_display_buttons')







        
 