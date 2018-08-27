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

# LOAD UI # 
from toolplus_resurface.ui_menus.menu_closer          import (VIEW3D_TP_Closer_Menu)
from toolplus_resurface.ui_menus.menu_vert_edit       import (VIEW3D_TP_Menu_Vert_Edit)
from toolplus_resurface.ui_menus.menu_edge_edit       import (VIEW3D_TP_Menu_Edge_Edit)
from toolplus_resurface.ui_menus.menu_edge_visual     import (VIEW3D_TP_Menu_Edge_Visual)
from toolplus_resurface.ui_menus.menu_face_edit       import (VIEW3D_TP_Menu_Face_Edit)
from toolplus_resurface.ui_menus.menu_face_visual     import (VIEW3D_TP_Menu_Face_Visual)
from toolplus_resurface.ui_menus.menu_special_edit    import (VIEW3D_TP_Menu_Special_Edit)

# LOAD MODUL #    
import bpy
from bpy import *


# KEY REGISTRY # 
addon_keymaps_menu = []

def update_menu_closer(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Closer_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_closer == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Closer_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        #km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')#, region_type='WINDOW'
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS', ctrl=True)
        
        #example
        #kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True, shift=True) 

        kmi.properties.name = 'VIEW3D_TP_Closer_Menu'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_closer == 'off':
        pass



def update_menu_vert_edit(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Menu_Vert_Edit)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_vert_edit == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Menu_Vert_Edit)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS', ctrl=True)
        kmi.properties.name = 'tp_menu.vert_edit'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_vert_edit == 'off':
        pass




def update_menu_edge_edit(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Menu_Edge_Edit)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_edge_edit == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Menu_Edge_Edit)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS', ctrl=True)
        kmi.properties.name = 'tp_menu.edge_edit'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_edge_edit == 'off':
        pass


def update_menu_edge_visual(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Menu_Edge_Visual)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_edge_visual == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Menu_Edge_Visual)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS', shift=True)
        kmi.properties.name = 'tp_menu.edge_visual'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_edge_visual == 'off':
        pass




def update_menu_face_edit(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Menu_Face_Edit)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_face_edit == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Menu_Face_Edit)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'F', 'PRESS', ctrl=True)
        kmi.properties.name = 'tp_menu.face_edit'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_face_edit == 'off':
        pass


def update_menu_face_visual(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Menu_Face_Visual)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_face_visual == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Menu_Face_Visual)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'F', 'PRESS', shift=True)
        kmi.properties.name = 'tp_menu.face_visual'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_face_visual == 'off':
        pass



def update_menu_special_edit(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Menu_Special_Edit)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_special_edit == 'menu':

        bpy.utils.register_class(VIEW3D_TP_Menu_Special_Edit)
    
        # Keymapping 
        wm = bpy.context.window_manager
      
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS')
        kmi.properties.name = 'tp_menu.special_edit'

 
    if context.user_preferences.addons[__package__].preferences.tab_menu_special_edit == 'off':
        pass


