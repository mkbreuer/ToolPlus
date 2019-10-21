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



# LOAD UI #
from toolplus_resurface.rsf_panel    import (VIEW3D_TP_ReSurface_Panel_TOOLS)
from toolplus_resurface.rsf_panel    import (VIEW3D_TP_ReSurface_Panel_UI)

# REGISTRY PANEL #
panels_main_rsf = (VIEW3D_TP_ReSurface_Panel_UI, VIEW3D_TP_ReSurface_Panel_TOOLS)

def update_panel_position(self, context):
    try:
        for panel in panels_main_rsf:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_location == 'tools':
         
            VIEW3D_TP_ReSurface_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category
            bpy.utils.register_class(VIEW3D_TP_ReSurface_Panel_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_location == 'ui':
            bpy.utils.register_class(VIEW3D_TP_ReSurface_Panel_UI)

        if context.user_preferences.addons[__package__].preferences.tab_location == 'off':  
            return None

    except:
        pass



# LOAD UI #
from toolplus_resurface.rsf_panel_sculpt    import (VIEW3D_TP_ReSculpt_Panel_TOOLS)
from toolplus_resurface.rsf_panel_sculpt    import (VIEW3D_TP_ReSculpt_Panel_UI)

# REGISTRY PANEL #
panels_main_sculpt = (VIEW3D_TP_ReSculpt_Panel_UI, VIEW3D_TP_ReSculpt_Panel_TOOLS)

def update_panel_sculpt(self, context):
    try:
        for panel in panels_main_sculpt:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_location_sculpt == 'tools':
         
            VIEW3D_TP_ReSculpt_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_sculpt
            bpy.utils.register_class(VIEW3D_TP_ReSculpt_Panel_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_location_sculpt == 'ui':
            bpy.utils.register_class(VIEW3D_TP_ReSculpt_Panel_UI)

        if context.user_preferences.addons[__package__].preferences.tab_location_sculpt == 'off':  
            return None

    except:
        pass

          

                  