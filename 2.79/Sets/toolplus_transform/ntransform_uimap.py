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

# LOAD UI #
from toolplus_transform.ntransform_panel        import (VIEW3D_TP_Transform_Panel_TOOLS)
from toolplus_transform.ntransform_panel        import (VIEW3D_TP_Transform_Panel_UI)


# UI REGISTRY #
panels_ntransform = (VIEW3D_TP_Transform_Panel_TOOLS,  VIEW3D_TP_Transform_Panel_UI)
def update_panel_ntransform(self, context):
    try:
        for panel in panels_ntransform:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels_ntransform:
            if context.user_preferences.addons[__package__].preferences.tab_location == 'tools':                
                                       
                VIEW3D_TP_Transform_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category                
                bpy.utils.register_class(VIEW3D_TP_Transform_Panel_TOOLS)

            if context.user_preferences.addons[__package__].preferences.tab_location == 'ui':
                    bpy.utils.register_class(VIEW3D_TP_Transform_Panel_UI)        

            if context.user_preferences.addons[__package__].preferences.tab_location == 'off':
                pass
    except:
        pass


