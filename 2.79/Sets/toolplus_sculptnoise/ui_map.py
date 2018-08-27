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


# LOAD UI #
from toolplus_sculptnoise.ui_panel    import (VIEW3D_TP_SculptNoise_Panel_TOOLS)
from toolplus_sculptnoise.ui_panel    import (VIEW3D_TP_SculptNoise_Panel_UI)


# UI REGISTRY #
panels_sculpt = (VIEW3D_TP_SculptNoise_Panel_UI, VIEW3D_TP_SculptNoise_Panel_TOOLS)

def update_panel_sculptnoise(self, context):
    try:
        for panel in panels_sculpt:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_location_sculptnoise == 'tools':
         
            VIEW3D_TP_SculptNoise_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_sculptnoise
            bpy.utils.register_class(VIEW3D_TP_SculptNoise_Panel_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_location_sculptnoise == 'ui':
            bpy.utils.register_class(VIEW3D_TP_SculptNoise_Panel_UI)


    except:
        pass


