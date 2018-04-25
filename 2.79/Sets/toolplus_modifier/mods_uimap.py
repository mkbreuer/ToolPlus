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

from toolplus_modifier.mods_stack        import (VIEW3D_TP_Modifier_Stack_Panel_UI)
from toolplus_modifier.mods_stack_tools  import (VIEW3D_TP_Modifier_Stack_Panel_TOOLS)

from toolplus_modifier.mods_panel        import (VIEW3D_TP_Modifier_Panel_TOOLS)
from toolplus_modifier.mods_panel        import (VIEW3D_TP_Modifier_Panel_UI)


# UI REGISTRY #
panels_mod = (VIEW3D_TP_Modifier_Panel_TOOLS,  VIEW3D_TP_Modifier_Panel_UI)
def update_panel_location(self, context):
    try:
        for panel in panels_mod:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels_mod:
            if context.user_preferences.addons[__package__].preferences.tab_location == 'tools':                
                                       
                VIEW3D_TP_Modifier_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category                
                bpy.utils.register_class(VIEW3D_TP_Modifier_Panel_TOOLS)

            if context.user_preferences.addons[__package__].preferences.tab_location == 'ui':
                    bpy.utils.register_class(VIEW3D_TP_Modifier_Panel_UI)        
    except:
        pass



panels_mod_stack = (VIEW3D_TP_Modifier_Stack_Panel_TOOLS,  VIEW3D_TP_Modifier_Stack_Panel_UI)
def update_panel_location_stack(self, context):
    try:
        for panel in panels_mod_stack:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels_mod_stack:    
            if context.user_preferences.addons[__package__].preferences.tab_location_stack == 'tools':                
                VIEW3D_TP_Modifier_Stack_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_stack                
                bpy.utils.register_class(VIEW3D_TP_Modifier_Stack_Panel_TOOLS)
            
            if context.user_preferences.addons[__package__].preferences.tab_location_stack == 'ui':
                bpy.utils.register_class(VIEW3D_TP_Modifier_Stack_Panel_UI)

            if context.user_preferences.addons[__package__].preferences.tab_location_stack == 'off':
                pass 
    except:
        pass


