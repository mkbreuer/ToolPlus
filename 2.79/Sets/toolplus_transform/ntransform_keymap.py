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
from toolplus_transform.ntransform_menu      import (VIEW3D_TP_Transform_Menu)


# KEY REGISTRY # 
addon_keymaps = []
keymaps_list = [
    {
        'name_view': "3D View",
        'space_type': "VIEW_3D",
        'prop_name': "VIEW3D_TP_Transform_Menu"
    },
    {
        'name_view': "Image",
        'space_type': "IMAGE_EDITOR",
        'prop_name': "VIEW3D_TP_Transform_Menu"
    },
    {
        'name_view': "Graph Editor",
        'space_type': "GRAPH_EDITOR",
        'prop_name': "VIEW3D_TP_Transform_Menu"
    },
    {
        'name_view': "Node Editor",
        'space_type': "NODE_EDITOR",
        'prop_name': "VIEW3D_TP_Transform_Menu"
    }
]


def update_menu_ntransform(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Transform_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        if wm.keyconfigs.addon:
            for km in addon_keymaps:
                for kmi in km.keymap_items:
                    km.keymap_items.remove(kmi)
        addon_keymaps.clear()
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_ntransform == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Transform_Menu)
    
        # Keymapping 
        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
            for keym in keymaps_list:
                km = kc.keymaps.new(name=keym['name_view'], space_type=keym['space_type'])
                kmi = km.keymap_items.new('wm.call_menu', 'X', 'PRESS', ctrl=True, shift=True)
                kmi.properties.name = keym['prop_name']
                addon_keymaps.append(km)


    if context.user_preferences.addons[__package__].preferences.tab_menu_ntransform == 'off':
        pass



