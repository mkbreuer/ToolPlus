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

from toolplus_resurface.ui_menus.menu_boolean    import (VIEW3D_TP_Boolean_Menu)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_menu_boolean(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Boolean_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_boolean == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Boolean_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'T', 'PRESS', shift=True) #add here your new key event

        #example
        #kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True, shift=True) 
       
        kmi.properties.name = "tp_menu.boolean_menu"


    if context.user_preferences.addons[__package__].preferences.tab_menu_boolean == 'off':
        pass





# KEY REGISTRY # 
addon_keymaps_direct_bool = []

# DIRECT BOOLEAN # hotkeys for objectmode and editmode #
def update_key_direct_bool(self, context):

    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_direct_bool:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_direct_bool[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_direct_keys == 'on':

        wm = bpy.context.window_manager

        # objectmode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new("btool.direct_union", 'NUMPAD_PLUS', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.direct_difference", 'NUMPAD_MINUS', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.direct_intersect", 'NUMPAD_ASTERIX', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.direct_slice", 'NUMPAD_SLASH', 'PRESS', ctrl=True)
               
        # editmode
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new("tp_ops.bool_union", 'NUMPAD_PLUS', 'PRESS', shift=True)
        kmi = km.keymap_items.new("tp_ops.bool_difference", 'NUMPAD_MINUS', 'PRESS', shift=True)
        kmi = km.keymap_items.new("tp_ops.bool_intersect", 'NUMPAD_ASTERIX', 'PRESS', shift=True)
        kmi = km.keymap_items.new("bpt.boolean_2d_union", 'NUMPAD_SLASH', 'PRESS', shift=True)

    if context.user_preferences.addons[__package__].preferences.tab_direct_keys == 'off':
        pass




# KEY REGISTRY # 
addon_keymaps_brush_bool = []

# BRUSH BOOLEAN # hotkeys for objectmode #
def update_key_brush_bool(self, context):

    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_brush_bool:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_brush_bool[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_brush_keys == 'on':

        wm = bpy.context.window_manager

        # objectmode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')        
        kmi = km.keymap_items.new("btool.boolean_union", 'NUMPAD_PLUS', 'PRESS', ctrl=True, shift=True)
        kmi = km.keymap_items.new("btool.boolean_diff", 'NUMPAD_MINUS', 'PRESS', ctrl=True, shift=True)
        kmi = km.keymap_items.new("btool.boolean_inters", 'NUMPAD_ASTERIX', 'PRESS', ctrl=True, shift=True)
        kmi = km.keymap_items.new("btool.boolean_slice", 'NUMPAD_SLASH', 'PRESS', ctrl=True, shift=True)

        kmi = km.keymap_items.new("btool.brush_to_mesh", 'NUMPAD_ENTER', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.to_mesh", 'NUMPAD_ENTER', 'PRESS', ctrl=True, shift=True)


    if context.user_preferences.addons[__package__].preferences.tab_brush_keys == 'off':
        pass




# KEY REGISTRY # 
addon_keymaps_bool_fast = []

# BOOLTOOL # Fast Transform HotKeys #
def update_key_bool_fast(self, context):

    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_bool_fast:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_bool_fast[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_brush_fast == 'on':

        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

        kmi = km.keymap_items.new("btool.fast_transform", 'G', 'PRESS')
        kmi.properties.operator = "Translate"
        addon_keymapsFastT.append((km, kmi))

        kmi = km.keymap_items.new("btool.fast_transform", 'R', 'PRESS')
        kmi.properties.operator = "Rotate"
        addon_keymapsFastT.append((km, kmi))

        kmi = km.keymap_items.new("btool.fast_transform", 'S', 'PRESS')
        kmi.properties.operator = "Scale"
        addon_keymapsFastT.append((km, kmi))

    if context.user_preferences.addons[__package__].preferences.tab_brush_fast == 'off':
        pass



