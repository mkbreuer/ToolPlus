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
from bpy.props import *
from . icons.buttons.icons import load_icons

# REGISTRY: SHORTCUTS # 
addon_keymaps_menu = []

def update_keymap_project(self, context):
    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)

        addon_keymaps.clear()
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_keymap_project == True:

        # Keymapping 
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.addon        
       
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('view3d.asset_flinger_project', 'W', 'PRESS', shift=True, alt=True)#add here your new key event
        kmi = km.keymap_items.new('export.asset_flinger_project', 'E', 'PRESS', shift=True, alt=True)#add here your new key event
        #kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True, shift=True) #example
        addon_keymaps_menu.append((km, kmi))

    if context.user_preferences.addons[__package__].preferences.tab_keymap_project == False:
        pass 



def update_keymap_asset(self, context):
    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)

        addon_keymaps.clear()
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_keymap_asset == True:

        # Keymapping 
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.addon        
       
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('view3d.asset_flinger', 'A', 'PRESS', ctrl=True, shift=True, alt=True)#add here your new key event
        kmi = km.keymap_items.new('export.asset_flinger', 'E', 'PRESS', ctrl=True, shift=True, alt=True)#add here your new key event
        #kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True, shift=True) #example
        addon_keymaps_menu.append((km, kmi))

    if context.user_preferences.addons[__package__].preferences.tab_keymap_asset == False:
        pass 






# REGISTRY: POPUP MENU # 
from toolplus_asset_flinger.ui_menu    import (VIEW3D_TP_AssetFlinger_Menu)

addon_popup_menu = []

def update_popup_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_AssetFlinger_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)

        addon_keymaps.clear()
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_popup_menu == True:

        bpy.utils.register_class(VIEW3D_TP_AssetFlinger_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.addon        
 
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=True, shift=True, alt=True) #add here your new key event

        #example
        #kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True, shift=True) 
       
        kmi.properties.name = "VIEW3D_TP_AssetFlinger_Menu"
        addon_popup_menu.append((km, kmi))

    if context.user_preferences.addons[__package__].preferences.tab_popup_menu == False:
        pass






# REGISTRY: APPEND TO MENU # 

def update_add_menu(self, context):
    layout = self.layout       
    layout.operator_context = 'INVOKE_REGION_WIN'

    addon_key = __package__.split(".")[0]    
    panel_prefs = context.user_preferences.addons[addon_key].preferences
 
    if panel_prefs.tap_display_project: 
        layout.operator('view3d.asset_flinger_project', text ="Project")    
   
    layout.operator('view3d.asset_flinger', text ="Library")    
    layout.separator()


def update_append_menu(self, context):

    try:       
        bpy.types.INFO_MT_add.prepend(update_add_menu) 
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_append == True:      
        bpy.types.INFO_MT_add.prepend(update_add_menu)    

    if context.user_preferences.addons[__package__].preferences.tab_menu_append == False:
        pass 




# REGISTRY: APPEND TO HEADER #

def update_button_project(self, context):
    layout = self.layout       
    layout.operator_context = 'INVOKE_REGION_WIN'
           
    icons = load_icons()  
      
    row = layout.row(1)
    
    row.separator()
    button_open_project = icons.get("icon_open_project")
    row.operator("view3d.asset_flinger_project", text="", icon_value=button_open_project.icon_id)               
  
    button_save_project = icons.get("icon_save_project")
    row.operator("export.asset_flinger_project", text="", icon_value=button_save_project.icon_id)


def update_header_project(self, context):

    try:       
        bpy.types.VIEW3D_HT_header.remove(update_button_project)
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_header_project == True:

        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_HT_header.append(update_button_project)  

        # ADD TO MENUS: BOTTOM #
        #bpy.types.VIEW3D_HT_header.prepend(draw_header_item_view)  


    if context.user_preferences.addons[__package__].preferences.tab_header_project == False:
        pass 



# REGISTRY: APPEND TO HEADER #

def update_button_asset(self, context):
    layout = self.layout       
    layout.operator_context = 'INVOKE_REGION_WIN'
       
    icons = load_icons()  

    row = layout.row(1)
   
    row.separator()
    button_open_library = icons.get("icon_open_library")
    row.operator("view3d.asset_flinger", text="", icon_value=button_open_library.icon_id)
 
    button_save_library = icons.get("icon_save_library")
    row.operator("export.asset_flinger", text="", icon_value=button_save_library.icon_id) 


def update_header_library(self, context):

    try:       
        bpy.types.VIEW3D_HT_header.remove(update_button_asset)
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_header_library == True:

        bpy.types.VIEW3D_HT_header.append(update_button_asset)

    if context.user_preferences.addons[__package__].preferences.tab_header_library == False:
        pass 



# REGISTRY: PANEL #

from toolplus_asset_flinger.ui_panel   import (VIEW3D_TP_AssetFlinger_Panel_TOOLS)
from toolplus_asset_flinger.ui_panel   import (VIEW3D_TP_AssetFlinger_Panel_UI)

panels_main = (VIEW3D_TP_AssetFlinger_Panel_UI, VIEW3D_TP_AssetFlinger_Panel_TOOLS)

def update_panel_location(self, context):
    try:
        for panel in panels_main:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__package__].preferences.tab_location_asset == 'tools':
         
            VIEW3D_TP_AssetFlinger_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_asset
            bpy.utils.register_class(VIEW3D_TP_AssetFlinger_Panel_TOOLS)
        
        if context.user_preferences.addons[__package__].preferences.tab_location_asset == 'ui':
            bpy.utils.register_class(VIEW3D_TP_AssetFlinger_Panel_UI)

        if context.user_preferences.addons[__package__].preferences.tab_location_asset == 'off':  
            return None

    except:
        pass



