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
    "name": "T+ Delete",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 9),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] or Menu",
    "description": "collection of delete tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_delete.del_manual  import (VIEW3D_TP_Delete_Manual)

# LOAD UI #
from toolplus_delete.del_panel   import (VIEW3D_TP_Delete_Panel_UI)
from toolplus_delete.del_panel   import (VIEW3D_TP_Delete_Panel_TOOLS)


# LOAD CUSTOM ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_delete'))

if "bpy" in locals():
    import imp
    imp.reload(del_action)
    imp.reload(del_all_scenes)
    imp.reload(del_clear_all)
    imp.reload(del_ktools)
    imp.reload(del_orphan)

else:
    from . import del_action                
    from . import del_all_scenes                 
    from . import del_clear_all                 
    from . import del_ktools                 
    from . import del_orphan                 
     


# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*
from toolplus_delete.del_keymap  import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY # 
def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Delete_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Delete_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Delete_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        VIEW3D_TP_Delete_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category

        bpy.utils.register_class(VIEW3D_TP_Delete_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Delete_Panel_UI)
  

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

    tab_display_tools = EnumProperty(name = 'History Tools',  description = 'on / off', items=(('on', 'History on', 'enable tools in panel'),  ('off', 'History off', 'disable tools in panel')), default='off', update = update_tools)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)

    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Delete!")  
            row.label(text="The addon includes all default and some advanced delete tools.") 

            row.label(text="Have Fun! :)")         


        # TOOLS #
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_display_tools', expand=True)

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 
            

        # LOCATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location Panel:")
            
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
            row.label("Delete Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: [X]")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)


            if self.tab_menu_view == 'off':
                row = box.row(1) 
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")

            else:            
                row = box.column(1)             
                row.label(text="! To use the delete menu > go to TAB: Input !", icon ="INFO")
                row.label(text="! Change search to key-bindig and insert the hotkey: [x] !", icon ="BLANK1")
                row.label(text="! now disable all the delete menus you not want to use !", icon ="BLANK1")
                row.label(text="! recommended: object, editmode and maybe curvemode, etc. !", icon ="BLANK1")

                
            box.separator()               
          
          
            # TIP #
            box.separator()
            
            row = layout.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: alt q", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Delete_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = layout.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = layout.row(1) 
            row.operator("tp_ops.keymap_delete", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()  
            

        # WEB #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="The list of auxiliary addons that a belong to this collection:")      

            row.separator() 
                                    
            row = box.row()
            row.operator('wm.url_open', text = 'Distribute', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Oscurart_Tools"
            row.operator('wm.url_open', text = 'Modal Origin', icon = 'HELP').url = "http://blenderlounge.fr/forum/viewtopic.php?f=18&t=1438"
            row.operator('wm.url_open', text = 'Advance Align', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?256114-Add-on-Advanced-align-tools"
            row.operator('wm.url_open', text = 'Mesh TinyCad', icon = 'HELP').url = "https://github.com/zeffii/mesh_tiny_cad"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?410351-Addon-T-Origin&p=3119318#post3119318"


# PROPERTIES # 
class Dropdown_Delete_ToolProps(bpy.types.PropertyGroup):

    display_del_bbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_del_zero = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)


# ORPHAN #    
mod_data = [tuple(["meshes"]*3), tuple(["armatures"]*3), 
                 tuple(["cameras"]*3), tuple(["curves"]*3),
                 tuple(["fonts"]*3), tuple(["grease_pencil"]*3),
                 tuple(["groups"]*3), tuple(["images"]*3),
                 tuple(["lamps"]*3), tuple(["lattices"]*3),
                 tuple(["libraries"]*3), tuple(["materials"]*3),
                 tuple(["actions"]*3), tuple(["metaballs"]*3),
                 tuple(["node_groups"]*3), tuple(["objects"]*3),
                 tuple(["sounds"]*3), tuple(["texts"]*3), 
                 tuple(["textures"]*3),]
if bpy.app.version[1] >= 60:
    mod_data.append( tuple(["speakers"]*3), )


# REGISTRY #

import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
  
    # PROPERTIES #    
    bpy.types.WindowManager.tp_delete_window = bpy.props.PointerProperty(type = Dropdown_Delete_ToolProps)

    # ORPHAN #    
    bpy.types.Scene.mod_list = bpy.props.EnumProperty(name="Target", items=mod_data, description="Module choice made for orphan deletion")
    
    # UI #        
    update_tools(None, bpy.context)
    update_menu(None, bpy.context)
    update_panel_position(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Delete_Manual)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
   
    # PROPERTIES #
    del bpy.types.WindowManager.tp_delete_window

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Delete_Manual)

if __name__ == "__main__":
    register()
        
        



              
