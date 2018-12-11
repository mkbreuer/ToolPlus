# ##### BEGIN GPL LICENSE BLOCK #####
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

import bpy
from bpy import *
from bpy.props import *

#from . icons.buttons.icons import load_icons

# BRUSH MENU #
class VIEW3D_TP_AssetFlinger_Menu(bpy.types.Menu):
    bl_label = "Asset Library"
    bl_idname = "VIEW3D_TP_AssetFlinger_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = 1.5   

        layout.operator("view3d.asset_flinger_project", text="Open Project")

        layout.operator("export.asset_flinger_project", text="Save to Project")                      

        layout.separator()           

        layout.operator("view3d.asset_flinger", text="Open Library")

        layout.operator("export.asset_flinger", text="Save to Library")



# PIE MENU #

#        icons = load_icons()  
    
#        button_open_project = icons.get("icon_open_project")
#        layout.operator("view3d.asset_flinger_project", text="Open Project", icon_value=button_open_project.icon_id)               
#      
#        button_save_project = icons.get("icon_save_project")
#        layout.operator("export.asset_flinger_project", text="Save to Project", icon_value=button_save_project.icon_id)
#        
#        layout.separator()   
#      
#        button_open_library = icons.get("icon_open_library")
#        layout.operator("view3d.asset_flinger", text="Open Library", icon_value=button_open_library.icon_id)
#     
#        button_save_library = icons.get("icon_save_library")
#        layout.operator("export.asset_flinger", text="Save to Library", icon_value=button_save_library.icon_id)        