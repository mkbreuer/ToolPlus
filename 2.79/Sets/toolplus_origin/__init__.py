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
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 1, 9),
    "blender": (2, 7, 9),
    "location": "Editor: View 3D > Panel or Menu: Origin",
    "description": "set origin",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus/wiki",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_origin.origin_manual   import (VIEW3D_Origin_Manual)


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
    imp.reload(origin_active)
    imp.reload(origin_align)
    imp.reload(origin_batch)
    imp.reload(origin_bbox)
    imp.reload(origin_bbox_modal)
    imp.reload(origin_center)
    imp.reload(origin_distribute)
    imp.reload(origin_modal)
    imp.reload(origin_operators)
    imp.reload(origin_transform)
    imp.reload(origin_zero)

else:
    from . import origin_action         
    from . import origin_active        
    from . import origin_align         
    from . import origin_batch               
    from . import origin_bbox               
    from . import origin_bbox_modal               
    from . import origin_center                 
    from . import origin_distribute                 
    from . import origin_modal         
    from . import origin_operators                 
    from . import origin_transform                 
    from . import origin_zero         


# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*
from toolplus_origin.origin_keymap  import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY # 
def update_panel_origin(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_origin == 'tools':
        VIEW3D_TP_Origin_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_origin

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
    

    # LIST #
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('url',        "URLs",       "URLs")),

               default='info')
    #------------------------------

    # PANEL #          
    tab_location_origin = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_origin)

    tools_category_origin = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_origin)
  
    #------------------------------

    # MENU #
    tab_menu_origin = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_origin)
  
    #------------------------------

    # TOOLS #
    tab_display_tools = EnumProperty(name = 'Advanced',  description = 'on / off', items=(('on', 'Advanced on', 'enable tools in panel'),  ('off', 'Advanced off', 'disable tools in panel')), default='on', update = update_tools)
   
    #------------------------------

    # DRAW LIST #   
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Origin!")  
            row.label(text="This collection allows you to set the origin to new position:")   
            row.label(text="-> to center, cursor, active or selected geometry.")   
            row.label(text="-> to the object bounding box.")   
            row.label(text="-> snap the origin to a point on the geometry.")   
            row.label(text="-> zero the origin to selected active.")      
            row.label(text="-> zero the origin, cursor or object to one of the 3d view axis.")      
            row.label(text="-> distribute object between there origin.")      
            row.label(text="-> or use advanced align tool with a bunch of more options.")      
            row.label(text="-> at least: to Have Fun! :)")         


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
            row.label("Location Origin:")
            
            row = box.row(1)
            row.prop(self, 'tab_location_origin', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location_origin == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_origin")

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
            row.prop(self, 'tab_menu_origin', expand=True)
                
            box.separator() 

            if self.tab_menu_origin == 'off':
                row = box.row(1) 
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")

              
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

            row = layout.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = layout.row(1) 
            row.operator("tp_ops.keymap_origin", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()  
            

        # WEB #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus/wiki"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?410351-Addon-T-Origin&p=3119318#post3119318"
               
            box.separator()  



# PROPERTIES # 
class Dropdown_Origin_ToolProps(bpy.types.PropertyGroup):

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="align origin to the boundtyp: box (4x vertice / 12x edge / 6x face)", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="align origin to the boundtyp: box (4x vertice / 12x edge / 6x face)", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="align origin, object or cursor to an axis", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="align only origin, object or cursor to an axis", default=False)
    display_origin_active = bpy.props.BoolProperty(name="Align to Active", description="align origin to active object", default=False)

    tp_axis_active = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"XYZ"  ,"04")],
               name = "Align to Active",
               default = "tp_x",    
               description = "zero target to choosen axis")

    tp_distance_active = bpy.props.EnumProperty(
        items=[("tp_min"    ,"Min"    ,"01"),
               ("tp_mid"    ,"Mid"    ,"02"),
               ("tp_max"    ,"Max"    ,"03")],
               name = "Align Distance",
               default = "tp_mid",    
               description = "align distance for origin")

    active_too = bpy.props.BoolProperty(name="Active too!",  description="align active origin too", default=False, options={'SKIP_SAVE'})    



# REGISTRY #

import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_props_origin = bpy.props.PointerProperty(type = Dropdown_Origin_ToolProps)
    
    update_tools(None, bpy.context)
    update_menu_origin(None, bpy.context)
    update_panel_origin(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_Origin_Manual)
    
    
def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    del bpy.types.WindowManager.tp_props_origin
 
    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_Origin_Manual) 
 
if __name__ == "__main__":
    register()
        
        




              
