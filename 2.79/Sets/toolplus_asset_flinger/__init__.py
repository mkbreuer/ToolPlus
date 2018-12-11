# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright (C) 2014-2017 script authors.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "T+ Asset Flinger",
    "author": "Manu Jarvinen/BlenderAid, h0bB1T, MKB",
    "version": (0, 3, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Hotkeys / Panel / Menu / Header",
    "description": "Object/Asset collection manager ",
    "category": "T+",
    "wiki_url": "https://github.com/BlenderAid/Asset-Flinger", 
}


# LOAD MODULS FROM PHYTON LIBS. #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_asset_flinger'))

# LOAD ICONS #
from . icons.buttons.icons   import load_icons
from . icons.buttons.icons   import clear_icons

# LOAD OPERATORS #
if "bpy" in locals():
    import importlib
    importlib.reload(ops_help)
    importlib.reload(ops_main)
    importlib.reload(ops_project)
else:
    from . import ops_help    
    from . import ops_main    
    from . import ops_project    


# LOAD MODULS FROM BLENDER LIBS. #
import bpy
from bpy import*
from bpy.props import*
from bpy.types import AddonPreferences, PropertyGroup
import bpy.utils.previews

# LOAD UI #
from toolplus_asset_flinger.ui_keymap   import*
from toolplus_asset_flinger.ops_main    import*
from toolplus_asset_flinger.ops_project import*


# LOAD KEYMAP #
import rna_keymap_ui
def get_hotkey_entry_item(km, kmi_name, kmi_value, properties):
 
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_name:
            if properties == 'name':
                if km.keymap_items[i].properties.name == kmi_value:
                    return km_item
            elif properties == 'none':
            	return km_item
    return None 



# ADDON PREFERENCES #
class AssetFlingerPreferences(AddonPreferences):
    """
    Preferences from addons menu. In addition, contains all information used
    for visualization. So it could easily be enhanced for visual settings.
    """
    bl_idname = __name__

    prefs_tabs = EnumProperty(
        items=(('path',      "Path",       "Path"),
               ('images',    "Thumbnails", "Thumbnails"),
               ('location',  "Location",   "Location"),
               ('keys',      "Keys/Input", "Keys/Input"),
               ('url',       "URLs",       "URLs")),
               default='path')


    # PATH MAIN #        
    custom_library_path = StringProperty(name="Asset library path", subtype='FILE_PATH')     

    # PATH PROJECT #    
    custom_library_path_project = StringProperty(name="Asset library path", subtype='FILE_PATH')


    # THUMBNAILS COLOR #   
    render_scene = EnumProperty(name="Thumbnail scene",
                        items=[( "original", "Original thumbnail scene", "Settings from previous version"),
                               ( "gray",     "Gray thumbnail scene",     "Pure gray style scene"),
                               ( "silver",   "Silver thumbnail scene",   "Asset is rendered in silver metal look"),
                               ( "wire",     "Wired thumbnail scene",    "Asset is rendered in a wire look")],
                               default="original")

    # THUMBNAILS SIZE #       
    thumbnail_render_size = EnumProperty(name="Thumbnail render size",
                                  items=[( "64", "64x64", "Very small" ),
                                         ( "128", "128x128", "Optimal size" ),
                                         ( "256", "256x256", "Slow to render, much details")],
                                         default="128")

    # PANEL #          
    tab_location_asset = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_location)
  
    # PANEL TAB CATEGORY #   
    tools_category_asset = StringProperty(name = "TAB Category", description = "new name creates a new category tab in the toolshelf", default = 'Asset', update = update_panel_location)

    # APPEND TO MENU # 
    tap_display_project = bpy.props.BoolProperty(name="Toogle Project",  description="show/hide project", default=False)   

    # HOTKEYS #  
    tab_keymap_project = bpy.props.BoolProperty(name="Hotkeys Project",  description="enable or disable hotkeys for 3d view", default=False, update = update_keymap_project)    
    tab_keymap_asset = bpy.props.BoolProperty(name="Hotkeys Library",  description="enable or disable hotkeys for 3d view", default=False, update = update_keymap_asset)    

    # MENU #    
    tab_popup_menu = bpy.props.BoolProperty(name="Popup Menu",  description="enable or disable Popup Menu for 3d view", default=False, update = update_popup_menu)    

    # APPEND TO MENU # 
    tab_menu_append = bpy.props.BoolProperty(name="Append to Menu",  description="append or remove from default add menu", default=False, update = update_append_menu)    

    # APPEND TO MENU # 
    tab_header_project = bpy.props.BoolProperty(name="Append Project Button",  description="append or remove header buttons", default=False, update = update_header_project)    

    # APPEND TO MENU # 
    tab_header_library = bpy.props.BoolProperty(name="Append Library Button",  description="append or remove header buttons", default=False, update = update_header_library)    

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(1)   

        box = col.box().column(1)                         

        box.separator()     

        row = box.row(1)
        row.prop(self, "prefs_tabs", expand=True)
       
        box.separator()   
     
        if self.prefs_tabs == 'path':

            box.separator()   
             
            row = box.column(1)
            row.label(text="Asset Library Path", icon="FILE_FOLDER")      
           
            row.separator()  
        
            row.prop(self, 'tap_display_project', text="(Un)Hide Project in 3D View")               
           
            box.separator()  

            row = box.column()                                                    
            row.prop(self, 'custom_library_path', text="")                                                        

            box.separator()   
             
            row = box.column(1)
            row.label(text="Project Library Path", icon="FILE_FOLDER")      
            
            box.separator()  

            row = box.column()                           
            row.prop(self, 'custom_library_path_project', text="")     

            box.separator()   
            box.separator()   


        if self.prefs_tabs == 'images':

            box.separator()   

            row = box.row(1)
            row.label(text="Thumbnail Color", icon="FILE_IMAGE")                     
            row.prop(self, 'render_scene', text="")

            box.separator() 

            row = box.row(1)
            row.label(text="Thumbnail Size", icon="ZOOM_ALL")                      
            row.prop(self, 'thumbnail_render_size', text="")

            box.separator()   
            box.separator()   


        if self.prefs_tabs == 'location':

            box.separator()   
             
            row = box.row(1)
            row.label(text="Panel Location", icon="ARROW_LEFTRIGHT")      
            row.prop(self, 'tab_location_asset', expand = True)          
      
            if self.tab_location_asset == 'tools':

                box.separator()   
                
                row = box.row(1)                     
                row.prop(self, "tools_category_asset", text="TAB")
                   
            box.separator()   
            box.separator()   


        if self.prefs_tabs == 'keys':

            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user

            split = box.split()
            col = split.column()

            col.separator()         
                             
            col.prop(self, 'tab_keymap_project', text="Hotkey for Project")   

            col.separator() 
              
            km = kc.keymaps['3D View']
            kmi = get_hotkey_entry_item(km, 'view3d.asset_flinger_project', 'none', 'none')
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found / restore hotkeys in input tab")            
              
            km = kc.keymaps['3D View']
            kmi = get_hotkey_entry_item(km, 'export.asset_flinger_project', 'none', 'none')
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found / restore hotkeys in input tab")   

          
            col.separator() 
            col.separator()         
                             
       
            col.prop(self, 'tab_keymap_asset', text="Hotkey for Library")   
                          
            col.separator() 

            km = kc.keymaps['3D View']
            kmi = get_hotkey_entry_item(km, 'view3d.asset_flinger', 'none', 'none')
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found / restore hotkeys in input tab")        

            km = kc.keymaps['3D View']
            kmi = get_hotkey_entry_item(km, 'export.asset_flinger', 'none', 'none')
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found / restore hotkeys in input tab")             

 
            col.separator()   
            col.separator()   


            col.prop(self, 'tab_popup_menu', text="Hotkey for Popup Menu")          

            col.separator()   
                 
            km = kc.keymaps['3D View']
            kmi = get_hotkey_entry_item(km, 'wm.call_menu', 'VIEW3D_TP_AssetFlinger_Menu', 'name')
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found / restore hotkeys in input tab")   
 
          
            col.separator()  
            col.separator()  

            col.prop(self, 'tab_menu_append', text="Append to Add Menu [CTRL+A]")

            col.separator()

            col.prop(self, 'tab_header_project', text="Header Buttons: Project")
            col.prop(self, 'tab_header_library', text="Header Buttons: Library")

            col.separator()

        
            # TIP #        

            row = layout.column(1)            
            row.label(text='Do not remove hotkeys, disable them instead.', icon ="INFO")           
            row.label(text="For KeyChange go to > User Preferences > Tab: Input", icon ="BLANK1")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. menu: ctrl shift alt w", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_AssetFlinger_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            box.separator()  

            row = layout.row(1)             
            row.label(text="! Or change the key in the keymap!", icon ="INFO")
            row.operator("tp_ops.keymap_assetflinger", text = 'Open KeyMap (Text Editor)   ')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"            

            box.separator() 
            
            row = layout.row(1)               
            row.label(text="! Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="INFO")
        
            box.separator()  
            box.separator()  
       
       

        if self.prefs_tabs == 'url':        

            box.separator()  
            
            row = box.row()
            row.operator('wm.url_open', text = 'Asset Flinger', icon = 'INFO').url = "https://github.com/BlenderAid/Asset-Flinger"
            row.operator('wm.url_open', text = 'v0.3 Fork', icon = 'INFO').url = "https://github.com/black-h0bB1T/Asset-Flinger"
            row.operator('wm.url_open', text = 'ToolPlus', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus"
        
            box.separator()  
            box.separator()  
        




    def thumbnailScenePostfix(self): return self.render_scene
    def thumbnailRenderSize(self): return self.thumbnail_render_size
        
    # http://blenderscripting.blogspot.de/2012/09/color-changes-in-ui.html
    def currentTheme(self):
        themeName = bpy.context.user_preferences.themes.items()[0][0]
        return bpy.context.user_preferences.themes[themeName]
    
    def currentThemeRadioButton(self):
        return self.currentTheme().user_interface.wcol_radio
    
    def iconSize(self): return 128
    def underlayWidth(self): return 180
    def menuItemMargins(self): return 4
    def menuItemHeight(self): return self.iconSize() + 2 * self.menuItemMargins()
    def menuItemWidth(self): return 400
    def itemTextSize(self): return 20
    def toolTipTextSize(self): return 10

    def bgColor(self): return (0, 0, 0, 0.6)
    
    def menuColor(self): return (*self.currentThemeRadioButton().inner, 1)
    def menuColorSelected(self): return (*self.currentThemeRadioButton().inner_sel, 1)
    def itemTextColor(self): return (*self.currentThemeRadioButton().text, 1)
    def itemTextColorSelected(self): return (*self.currentThemeRadioButton().text_sel, 1)






# PROPERTIES # 
from bpy.types import PropertyGroup

class Dropdown_AssetFlinger_Props(bpy.types.PropertyGroup):

    display_settings = bpy.props.BoolProperty(name="Open/Close",  description="open/close", default=False)    
 
    display_preferences = EnumProperty(name = 'Settings',        
                               items=(('path',      'Pathes',   'path directories'),
                                      ('preview',   'Preview',  'rendered thumnail style'),
                                      ('ui',        'UI',       'interface optionen')),
                                      description = 'addon preferences',
                                      default='path')


# REGISTER #
import traceback     

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()    
    
    # UI #
    update_keymap_project(None, bpy.context)
    update_keymap_asset(None, bpy.context)
    update_popup_menu(None, bpy.context)
    update_append_menu(None, bpy.context)
    update_panel_location(None, bpy.context)
    update_header_project(None, bpy.context)
    update_header_library(None, bpy.context)

    bpy.types.WindowManager.tp_props_assetflinger = bpy.props.PointerProperty(type = Dropdown_AssetFlinger_Props)


def unregister():
    
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()    

    del bpy.types.WindowManager.tp_props_assetflinger 


if __name__ == "__main__":
    register()
    
