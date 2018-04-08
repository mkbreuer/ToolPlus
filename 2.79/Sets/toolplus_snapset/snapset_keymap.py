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


# ADD 3D VIEW MENU #  
from toolplus_snapset.snapset_menu  import (VIEW3D_TP_SnapSet_Menu)
from toolplus_snapset.snapset_menu  import (VIEW3D_TP_SnapSet_Menu_Pie)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_snapset_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_SnapSet_Menu)
        bpy.utils.unregister_class(VIEW3D_TP_SnapSet_Menu_Pie)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_snapset_menu == 'menu':

        bpy.utils.register_class(VIEW3D_TP_SnapSet_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
                                                        
        kmi = km.keymap_items.new('wm.call_menu', 'TWO', 'PRESS', alt=True) #add here your new key event
        
        # example for new key event:
        # kmi = km.keymap_items.new('wm.call_menu', 'A', 'DOUPLECLICK', ctrl=True, alt=True, shift=True) 
       
        kmi.properties.name = "tp_menu.menu_snapset"


    if context.user_preferences.addons[__package__].preferences.tab_snapset_menu == 'pie':

        bpy.utils.register_class(VIEW3D_TP_SnapSet_Menu_Pie)
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
                                                        
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TWO', 'PRESS', alt=True) 

        kmi.properties.name = "tp_menu.pie_snapset"


    if context.user_preferences.addons[__package__].preferences.tab_snapset_menu == 'remove':
        return None




# ADD TO SPECIAL [W] #  
from toolplus_snapset.snapset_menu  import (draw_snapset_item_special)

def update_snapset_submenu(self, context):

    try:
        bpy.types.VIEW3D_MT_special.remove(draw_snapset_item_special)          

    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_snapset_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_object_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.append(draw_snapset_item_special)  

    if context.user_preferences.addons[__package__].preferences.tab_snapset_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_object_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.prepend(draw_snapset_item_special)  

    if context.user_preferences.addons[__package__].preferences.tab_snapset_special == 'remove':  
        return None




# ADD TO HEADER #  
from toolplus_snapset.snapset_menu  import (VIEW3D_TP_SnapSet_Header_Menu)

def update_snapset_header(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_SnapSet_Header_Menu)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_snapset_header == 'add':

        bpy.utils.register_class(VIEW3D_TP_SnapSet_Header_Menu)

    if context.user_preferences.addons[__package__].preferences.tab_snapset_header == 'remove':
        return None  




# LOAD PANEL UI #
from toolplus_snapset.snapset_panel    import (VIEW3D_TP_SnapSet_Panel_TOOLS)
from toolplus_snapset.snapset_panel    import (VIEW3D_TP_SnapSet_Panel_UI) 

panels_snapset = (VIEW3D_TP_SnapSet_Panel_UI, VIEW3D_TP_SnapSet_Panel_TOOLS)

def update_snapset_panel(self, context):
    try:
        for panel in panels_snapset:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_snapset_location == 'tools':
         
            VIEW3D_TP_SnapSet_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_snapset
            bpy.utils.register_class(VIEW3D_TP_SnapSet_Panel_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_snapset_location == 'ui':
            
            bpy.utils.register_class(VIEW3D_TP_SnapSet_Panel_UI)

        if context.user_preferences.addons[__package__].preferences.tab_snapset_location == 'off':  
            return None

    except:
        pass