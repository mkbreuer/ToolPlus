# ##### BEGIN GPL LICENSE BLOCK #####
#
#  2017 MKB
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

from toolplus_selection.select_ui_menus    import (VIEW3D_TP_Select_Menu)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_menu_select(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Select_Menu)
                
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_display_menu == 'menu':
    
        bpy.utils.register_class(VIEW3D_TP_Select_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', alt=True)
        kmi.properties.name = "VIEW3D_TP_Select_Menu"


    if context.user_preferences.addons[__package__].preferences.tab_display_menu == 'off':
        pass

