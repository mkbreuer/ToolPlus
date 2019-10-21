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


# KEY REGISTRY # 
addon_keymaps_quickset = []

# BOOLTOOL # Fast Transform HotKeys #
def update_key_quickset(self, context):

    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_quickset:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_quickset[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_brush_quickset == 'on':
       
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='Sculpt', space_type='EMPTY', region_type='WINDOW')
                                                
        kmi = km.keymap_items.new('brush.modal_quickset', 'RIGHTMOUSE', 'PRESS')



    if context.user_preferences.addons[__package__].preferences.tab_brush_quickset == 'off':
        pass








