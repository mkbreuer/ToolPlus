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


bl_info = {
    "name": "T+ Origin",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 5),
    "blender": (2, 7, 9),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] or Menu",
    "description": "Origin Tools Collection",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #
from toolplus_origin.origin_panel   import (VIEW3D_TP_Origin_Panel_UI)
from toolplus_origin.origin_panel   import (VIEW3D_TP_Origin_Panel_TOOLS)

from toolplus_origin.origin_batch   import (View3D_TP_Origin_Batch)

# LOAD CUSTOM ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons

# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_origin'))

if "bpy" in locals():
    import imp
    imp.reload(origin_action)
    imp.reload(origin_align)
    imp.reload(origin_batch)
    imp.reload(origin_bbox)
    imp.reload(origin_center)
    imp.reload(origin_distribute)
    imp.reload(origin_modal)
    imp.reload(origin_operators)
    imp.reload(origin_zero)

else:
    from . import origin_action         
    from . import origin_align         
    from . import origin_batch               
    from . import origin_bbox               
    from . import origin_center                 
    from . import origin_distribute                 
    from . import origin_modal         
    from . import origin_operators                 
    from . import origin_zero         


# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*
from toolplus_origin.origin_keymap  import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY # 
def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        VIEW3D_TP_Origin_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category

        bpy.utils.register_class(VIEW3D_TP_Origin_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Origin_Panel_UI)
  


# TOOLS TOGGLE # 
def update_tools(self, context):

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass
    

# ADDON PREFERNECES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)

    tab_display_tools = EnumProperty(name = 'Batch Menu',  description = 'on / off', items=(('on', 'Batch on', 'enable tools in panel'),  ('off', 'Batch off', 'disable tools in panel')), default='off', update = update_tools)
    tab_display_advanced = EnumProperty(name = 'Advanced',  description = 'on / off', items=(('on', 'Advanced on', 'enable tools in panel'),  ('off', 'Advanced off', 'disable tools in panel')), default='off', update = update_tools)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)


    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Origin Collection!")  
            row.label(text="The addon set allows you to:") 
            row.label(text="1. set your origin to center, cursor or selected")   
            row.label(text="2. or to a point on the object bounding box")   
            row.label(text="3. or zero the origin to an 3d view axis")      
            row.label(text="Have Fun! :)")         


        # TOOLS #
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_display_tools', expand=True)
            row.prop(self, 'tab_display_advanced', expand=True)

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 
            

        # LOCATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location Origin:")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            row = layout.row()
            row.label(text="! please reboot blender after changing the panel location !", icon ="INFO")

            box.separator() 


        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Origin Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: CTRL+D ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
                
            box.separator() 

            if self.tab_menu_view == 'off':
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            else:      
                row = box.row(1) 
                row.operator("tp_ops.keymap_origin", text = 'Open KeyMap (Text Editor)')
                row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
                
              
            # TIP #
            box.separator()
            
            row = layout.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

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
            row.operator('wm.url_open', text = 'Distribute', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Oscurart_Tools"
            row.operator('wm.url_open', text = 'Modal Origin', icon = 'HELP').url = "http://blenderlounge.fr/forum/viewtopic.php?f=18&t=1438"
            row.operator('wm.url_open', text = 'Advance Align', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?256114-Add-on-Advanced-align-tools"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?410351-Addon-T-Origin&p=3119318#post3119318"


# PROPERTIES # 
class DropdownOriginToolProps(bpy.types.PropertyGroup):

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)




# REGISTRY #

import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.bbox_origin_window = bpy.props.PointerProperty(type = DropdownOriginToolProps)
    
    update_tools(None, bpy.context)
    update_menu(None, bpy.context)
    update_panel_position(None, bpy.context)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    del bpy.types.WindowManager.bbox_origin_window
 
if __name__ == "__main__":
    register()
        
        




              
