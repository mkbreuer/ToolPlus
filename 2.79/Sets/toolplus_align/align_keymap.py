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




# LOAD MENUS #
from toolplus_align.menus.menu_align             import (VIEW3D_TP_Align_Menu)
from toolplus_align.menus.menu_editors           import (VIEW3D_TP_Align_Menu_Graph)
from toolplus_align.menus.menu_editors           import (VIEW3D_TP_Align_Menu_UV)
from toolplus_align.menus.menu_editors           import (VIEW3D_TP_Align_Menu_Node)
from toolplus_align.menus.menu_pie               import (VIEW3D_TP_Align_PIE)

# KEY MENU #
addon_keymaps = []
keymaps_list = [
    {
        'name_view': "3D View",
        'space_type': "VIEW_3D",
        'prop_name': "tp_menu.align_main"
    },
    {
        'name_view': "Image",
        'space_type': "IMAGE_EDITOR",
        'prop_name': "tp_menu.align_main_uv"
    },
    {
        'name_view': "Graph Editor",
        'space_type': "GRAPH_EDITOR",
        'prop_name': "tp_menu.align_main_graph"
    },
    {
        'name_view': "Node Editor",
        'space_type': "NODE_EDITOR",
        'prop_name': "tp_menu.align_main_node"
    }
]

keymaps_list_pie = [
    {
        'name_view': "Image",
        'space_type': "IMAGE_EDITOR",
        'prop_name': "tp_menu.align_main_uv"
    },
    {
        'name_view': "Graph Editor",
        'space_type': "GRAPH_EDITOR",
        'prop_name': "tp_menu.align_main_graph"
    },
    {
        'name_view': "Node Editor",
        'space_type': "NODE_EDITOR",
        'prop_name': "tp_menu.align_main_node"
    },
    {
        'name_view': "3D View",
        'space_type': "VIEW_3D",
        'prop_name': "tp_pie.align_pie_menu"
    }

]


def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Menu)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Menu_Graph)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Menu_UV)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Menu_Node)
        bpy.utils.unregister_class(VIEW3D_TP_Align_PIE)
        
        wm = bpy.context.window_manager
        if wm.keyconfigs.addon:
            for km in addon_keymaps:
                for kmi in km.keymap_items:
                    km.keymap_items.remove(kmi)
        addon_keymaps.clear()
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_align == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Align_Menu)
        bpy.utils.register_class(VIEW3D_TP_Align_Menu_Graph)
        bpy.utils.register_class(VIEW3D_TP_Align_Menu_UV)
        bpy.utils.register_class(VIEW3D_TP_Align_Menu_Node)
    
        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
            for keym in keymaps_list:
                km = kc.keymaps.new(name=keym['name_view'], space_type=keym['space_type'])
                kmi = km.keymap_items.new('wm.call_menu', 'Y', 'PRESS', shift=True)
                kmi.properties.name = keym['prop_name']
                addon_keymaps.append(km)

    if context.user_preferences.addons[__package__].preferences.tab_menu_align == 'pie':
       
        bpy.utils.register_class(VIEW3D_TP_Align_Menu_Graph)
        bpy.utils.register_class(VIEW3D_TP_Align_Menu_UV)
        bpy.utils.register_class(VIEW3D_TP_Align_Menu_Node)
        bpy.utils.register_class(VIEW3D_TP_Align_PIE)
    
        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
            for keym in keymaps_list_pie:
                km = kc.keymaps.new(name=keym['name_view'], space_type=keym['space_type'])
                kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=True)
                kmi = km.keymap_items.new('wm.call_menu_pie', 'Y', 'PRESS', shift=True)
                kmi.properties.name = keym['prop_name']
                addon_keymaps.append(km)


    if context.user_preferences.addons[__package__].preferences.tab_menu_align == 'off':
        pass



# LOAD MENU #
from toolplus_align.menus.menu_relax import (VIEW3D_TP_Relax_Menu)

def update_menu_relax(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Relax_Menu)
        
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_view_relax == 'menu':
         
        bpy.utils.register_class(VIEW3D_TP_Relax_Menu)

        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=True, shift=True) #,alt=True
        kmi.properties.name = "tp_menu.relax_base"

    if context.user_preferences.addons[__package__].preferences.tab_menu_view_relax == 'off':
        pass



# LOAD MENU #
from toolplus_align.menus.menu_origin    import (VIEW3D_TP_Origin_Menu)

def update_menu_origin(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Menu)

        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_view_origin == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Origin_Menu)

        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS', ctrl=True) #,alt=True, shift=True, 
        kmi.properties.name = "tp_menu.origin_base"

    if context.user_preferences.addons[__package__].preferences.tab_menu_view_origin == 'off':
        pass



# LOAD MENU #
from toolplus_align.menus.menu_machine    import (VIEW3D_TP_Machine_Menu)

def update_menu_machine(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Machine_Menu)

        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_machine == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Machine_Menu)

        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'X', 'PRESS', shift=True) #,alt=True, ctrl=True, 
        kmi.properties.name = "VIEW3D_TP_Machine_Menu"

    if context.user_preferences.addons[__package__].preferences.tab_menu_machine == 'off':
        pass
