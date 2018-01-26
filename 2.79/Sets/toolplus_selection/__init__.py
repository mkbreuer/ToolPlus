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
    "name": "T+ Selection",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 1, 2),
    "blender": (2, 7, 9),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "collection of selection tools",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD MANUAL #
from toolplus_selection.select_manual   import (View3D_TP_Select_Manual)

# LOAD UI #
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
    imp.reload(select_surface)
    imp.reload(select_topokit2)
    imp.reload(select_vismaya)

else:
    from . import select_action                
    from . import select_ktools         
    from . import select_meshlint         
    from . import select_meshorder                         
    from . import select_surface                
    from . import select_topokit2                
    from . import select_vismaya                



# LOAD MODUL # 
import bpy
from bpy import*
from bpy.props import* 
from toolplus_selection.select_keymap  import*

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
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Panel off', 'disable the panel')),
               default='tools', update = update_panel_selection)

    tab_display_menu = EnumProperty(
        name = '3d View Menu',
        description = 'on or off for 3D view menu',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'disable menu for 3d view')),
               default='off', update = update_menu_select)

    tools_category_select = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_selection)

    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            row = layout.column()
            row.label(text="Welcome T+ Selection!")
            row.label(text="This collection includes all default and some advanced selection tools")
            row.label(text="")

            
        # LOCATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.column(1)   
            row.label("Location: ")
            
            row= box.row(align=True)
            row.prop(self, 'tab_location_select', expand=True)
            
            if self.tab_location_select == 'tools':

                box.separator()           
               
                row = box.row()
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
           
            box.separator()
        
           
            # TIP #            
            row = layout.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: alt q", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Select_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = layout.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = layout.row(1) 
            row.operator("tp_ops.keymap_select", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            layout.separator()  
            

        # WEB #
        if self.prefs_tabs == 'url':
          
          row = layout.row()
          row.operator('wm.url_open', text = 'Meshlint', icon = 'PACKAGE').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Modeling/MeshLint"
          row.operator('wm.url_open', text = 'Topokit v2', icon = 'PACKAGE').url = "https://blenderartists.org/forum/showthread.php?237618-UPDATED-Topokit-v2-cleaned-up-reorganized-the-ui-a-caching-mechanism"
          row.operator('wm.url_open', text = 'KTools', icon = 'PACKAGE').url = "http://www.kjartantysdal.com/scripts/"
          row.operator('wm.url_open', text = 'GitHub', icon = 'PACKAGE').url = "https://github.com/mkbreuer/ToolPlus"




# PROBERTIES #
class Dropdown_TP_Select_Props(bpy.types.PropertyGroup):

    display_meshlint_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_check_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
     



# REGISTRY #

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    
    # UI #            
    update_panel_selection(None, bpy.context)
    update_menu_select(None, bpy.context)
 
    # PROBERTIES #
    bpy.types.WindowManager.tp_props_select = bpy.props.PointerProperty(type = Dropdown_TP_Select_Props)

    # MANUAL #
    bpy.utils.register_manual_map(View3D_TP_Select_Manual)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # PROBERTIES #
    del bpy.types.WindowManager.tp_props_select
 
    # MANUAL #
    bpy.utils.register_manual_map(View3D_TP_Select_Manual)

if __name__ == "__main__":
    register()
        
        
                                   
             