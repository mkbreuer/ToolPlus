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


# LOAD UI  #
from toolplus_align.align_panel      import (VIEW3D_TP_Align_TOOLS)
from toolplus_align.align_panel      import (VIEW3D_TP_Align_UI)
from toolplus_align.align_panel      import (VIEW3D_TP_Align_PROPS)


# UI REGISTRY #
panels_main = (VIEW3D_TP_Align_TOOLS, VIEW3D_TP_Align_UI, VIEW3D_TP_Align_PROPS)

def update_panel_position(self, context):
    message = "Align: Updating Panel locations has failed"
    try:
        for panel in panels_main:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_location_align == 'tools':
         
            VIEW3D_TP_Align_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_align
            bpy.utils.register_class(VIEW3D_TP_Align_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_location_align == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Align_UI)

        if context.user_preferences.addons[__package__].preferences.tab_location_align == 'props':
            bpy.utils.register_class(VIEW3D_TP_Align_PROPS)

        if context.user_preferences.addons[__package__].preferences.tab_location_align == 'off':  
            return None

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__package__, message, e))
        pass
