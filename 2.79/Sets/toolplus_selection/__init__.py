# ##### BEGIN GPL LICENSE BLOCK #####
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


bl_info = {
    "name": "T+ Select",
    "author": "MKB",
    "version": (0, 1, 1),
    "blender": (2, 7, 9),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "Selection Panel and Menu for 3D View",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}




# LOAD UI #
from toolplus_selection.select_ui_menus        import (VIEW3D_TP_Select_Menu)
from toolplus_selection.select_ui_menus        import (VIEW3D_TP_MultiMode)

from toolplus_selection.select_ui_panel        import (VIEW3D_TP_Selection_Panel_TOOLS)
from toolplus_selection.select_ui_panel        import (VIEW3D_TP_Selection_Panel_UI)


# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_selection'))

if "bpy" in locals():
    import imp
    imp.reload(select_action)
    imp.reload(select_ktools)
    imp.reload(select_meshlint)
    imp.reload(select_meshorder)
    imp.reload(select_sorting)
    imp.reload(select_surface)
    imp.reload(select_topokit2)
    imp.reload(select_vismaya)

else:
    from . import select_action                
    from . import select_ktools         
    from . import select_meshlint         
    from . import select_meshorder            
    from . import select_sorting                
    from . import select_surface                
    from . import select_topokit2                
    from . import select_vismaya                


# LOAD MODUL # 
import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup

# PANEL REGISTRY # 
panels = (VIEW3D_TP_Selection_Panel_UI, VIEW3D_TP_Selection_Panel_TOOLS)

def update_panel_selection(self, context):
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_location_select == 'tools':
         
            VIEW3D_TP_Selection_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_select
            bpy.utils.register_class(VIEW3D_TP_Selection_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_select == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Selection_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_location_select == 'off':  
            return None
        
    except:
        pass



# MENU REGISTRY # 
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
    
    if context.user_preferences.addons[__name__].preferences.tab_display_menu == 'menu':
     
        #VIEW3D_TP_Select_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Select_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', alt=True)
        kmi.properties.name = "VIEW3D_TP_Select_Menu"


    if context.user_preferences.addons[__name__].preferences.tab_display_menu == 'off':
        pass


# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),
               ('url',        "URLs",       "URLs")),
               default='info')
     
    tab_location_select = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_selection)

    tab_display_menu = EnumProperty(
        name = '3d View Menu',
        description = 'on or off for 3D view menu',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'disable menu for 3d view')),
               default='off', update = update_menu_select)

    tools_category_select = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_selection)
    #tools_category_menu = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_menu_select)

    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            row = layout.column()
            row.label(text="T+ Select!")
            row.label(text="This is a collection of selection tools")

            
        # LOCATION #
        if self.prefs_tabs == 'location':
            row = layout.row()
            row.separator()
            
            row = layout.row()
            row.label("Location: ")
            
            row= layout.row(align=True)
            row.prop(self, 'tab_location_select', expand=True)
            row = layout.row()
            
            if self.tab_location_select == 'tools':
                row.prop(self, "tools_category_select")

       # KEYMAP #
        if self.prefs_tabs == 'keymap':

            #Menu
            box = layout.box().column(1)
             
            row = box.column(1)          
            row.label("Menu: '[ALT+Q]", icon ="COLLAPSEMENU")

            row = box.row(1)          
            row.prop(self, 'tab_display_menu', expand=True)
            
            if self.tab_display_menu == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot !", icon ="INFO")
           
            # TIP #
            box.separator()
            
            row = layout.row(1)             
            row.label(text="! For key change go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: alt q", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Boolean_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  



        # WEB #
        if self.prefs_tabs == 'url':
          
          row = layout.row()
          row.operator('wm.url_open', text = 'GitHub', icon = 'PACKAGE').url = "https://github.com/mkbreuer/ToolPlus"




class Dropdown_TP_Select_Props(bpy.types.PropertyGroup):

    display_meshlint_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
     



# REGISTRY #

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_selection(None, bpy.context)
    update_menu_select(None, bpy.context)

    bpy.types.WindowManager.tp_props_select = bpy.props.PointerProperty(type = Dropdown_TP_Select_Props)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    del bpy.types.WindowManager.tp_props_select

if __name__ == "__main__":
    register()
        
        
                                   
             