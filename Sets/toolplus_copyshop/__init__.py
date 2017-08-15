# ##### BEGIN GPL LICENSE BLOCK #####
#
#Copyright (C) 2017  Marvin.K.Breuer (MKB)]
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
    "name": "T+ CopyShop",
    "author": "MKB",
    "version": (1, 3, 0),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "CopyShop Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #

from .copy_ui_menu     import (View3D_TP_Copy_Menu)

from .copy_ui_panel     import (VIEW3D_TP_Copy_Panel_UI)
from .copy_ui_panel     import (VIEW3D_TP_Copy_Panel_TOOLS)
from .copy_ui_panel     import (VIEW3D_TP_Copy_Panel_PROPS)

# LOAD PROPS #
from toolplus_copyshop.copy_mifthcloning    import (MFTProperties)

# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_copyshop'))

if "bpy" in locals():
    import imp
    imp.reload(copy_action)
    imp.reload(copy_attributes)
    imp.reload(copy_mifthcloning)
    imp.reload(copy_pivot)
    imp.reload(copy_replicator)
    imp.reload(copy_fpath)
    imp.reload(copy_display)
    imp.reload(copy_to_all)
    imp.reload(copy_origin)
    imp.reload(copy_to_mesh)

else:
    from . import copy_action         
    from . import copy_attributes                          
    from . import copy_mifthcloning          
    from . import copy_pivot       
    from . import copy_replicator           
    from . import copy_fpath            
    from . import copy_display       
    from . import copy_to_all       
    from . import copy_origin       
    from . import copy_to_mesh       
    

# LOAD MODULS #

import bpy
from bpy import *
from bpy.props import* 

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #

def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Copy_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Copy_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Copy_Panel_PROPS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Copy_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Copy_Panel_PROPS)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        VIEW3D_TP_Copy_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        bpy.utils.register_class(VIEW3D_TP_Copy_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Copy_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location == 'props':
        bpy.utils.register_class(VIEW3D_TP_Copy_Panel_PROPS)

    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass




# TOOLS REGISTRY #

def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass 



# MENUS REGISTRY #

addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(View3D_TP_Copy_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        View3D_TP_Copy_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(View3D_TP_Copy_Menu)
    
        # booltool: create the booleanhotkey in opjectmode
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', shift=True, alt=True) #,ctrl=True 
        kmi.properties.name = 'tp_menu.copyshop_menu'

    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass
    


# ADDON PREFERENCES #

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
        items=(('tools',    'Tool Shelf',           'place panel in the tool shelf [T]'),
               ('ui',       'Property Shelf',       'place panel in the property shelf [N]'),
               ('props',    'Properties Object',    'place panel in the object properties tab'),
               ('off',      'Off',                  'hide panel')),
               default='tools', update = update_panel_position)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)



    # Panel
    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_pivot = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pivot on', 'enable tools in panel'), ('off', 'Pivot off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_duplicate = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Duplicate on', 'enable tools in panel'), ('off', 'Duplicate off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_radial = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Radial Clone on', 'enable tools in panel'), ('off', 'Radial Clone off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_cursor = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy to Cursor on', 'enable tools in panel'), ('off', 'Copy to Cursor off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_copy_to_mesh = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy to Mesh on', 'enable tools in panel'), ('off', 'Copy to Mesh off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_dupli = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Dupli on', 'enable tools in panel'), ('off', 'Dupli off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_arewo = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ARewO on', 'enable tools in panel'), ('off', 'ARewO off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_array = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Array on', 'enable tools in panel'), ('off', 'Array off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_advance = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Advance Copy on', 'enable tools in panel'), ('off', 'Advance Copy off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_instances = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Instances on', 'enable tools in panel'), ('off', 'Instances off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_dynamics = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Dymanic on', 'enable tools in panel'), ('off', 'Dymanic off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_transform = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Transform on', 'enable tools in panel'), ('off', 'Transform off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_shade = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Shade on', 'enable tools in panel'), ('off', 'Shade off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_history = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)


    # Menu
    tab_menu_copy = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy on', 'enable tools in panel'), ('off', 'Copy off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_arewo = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Arewo on', 'enable tools in panel'), ('off', 'Arewo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_array = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Array on', 'enable tools in panel'), ('off', 'Array off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_optimize = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Optimize on', 'enable tools in panel'), ('off', 'Optimize off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_origin = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Origin on', 'enable tools in panel'), ('off', 'Origin off', 'disable tools in panel')), default='on', update = update_display_tools)


    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)

    tools_category_menu = bpy.props.BoolProperty(name = "CopyShop Menu", description = "enable or disable menu", default=True, update = update_menu)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ CopyShop!")  
            row.label(text="This addon is for object duplication.")
           
            row.separator()           
           
            row.label(text="The Panels are adaptable can be place in the toolshelf [T] or property shelf [N]")
            row.label(text="Or placed to Properties: 'Object' TAB")
            row.label(text="A included Menu have ALT+SHIFT+Q as shortcut")
           
            row.separator()        
                        
            row.label(text="Have Fun! :)")  
       

        #Tools
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
          
            row = box.row()
            row.label(text="Panel Tools")
           
            row = box.column_flow(5)
            row.prop(self, 'tab_title', expand=True)
            row.prop(self, 'tab_pivot', expand=True)
            row.prop(self, 'tab_duplicate', expand=True)
            row.prop(self, 'tab_radial', expand=True)
            row.prop(self, 'tab_cursor', expand=True)
            row.prop(self, 'tab_copy_to_mesh', expand=True)
            row.prop(self, 'tab_dupli', expand=True)
            row.prop(self, 'tab_arewo', expand=True)
            row.prop(self, 'tab_array', expand=True)
            row.prop(self, 'tab_advance', expand=True)
            row.prop(self, 'tab_instances', expand=True)
            row.prop(self, 'tab_dynamics', expand=True)
            row.prop(self, 'tab_transform', expand=True)
            row.prop(self, 'tab_shade', expand=True)
            row.prop(self, 'tab_history', expand=True)

            box.separator() 
            
            box = layout.box().column(1)
          
            row = box.row()
            row.label(text="Menu Tools")
           
            row = box.column_flow(3)
            row.prop(self, 'tab_menu_copy', expand=True)
            row.prop(self, 'tab_menu_arewo', expand=True)
            row.prop(self, 'tab_menu_array', expand=True)
            row.prop(self, 'tab_menu_optimize', expand=True)
            row.prop(self, 'tab_menu_origin', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for a durably on or off !", icon ="INFO")

            box.separator() 


        #Location
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location CopyShop:")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for a durably new panel location !", icon ="INFO")

            box.separator()  
            
        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu: ALT+SHIFT+Q", icon ="COLLAPSEMENU") 

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
             
            row.operator('wm.url_open', text = '!Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"


            box.separator() 
            
            row = layout.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")


        #Weblinks
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
             
            row = box.column_flow(2) 
            row.operator('wm.url_open', text = 'MifthTools', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?346588-MifthTools-Addon"
            row.operator('wm.url_open', text = 'ARewO', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Animation/ARewO"
            row.operator('wm.url_open', text = 'To All', icon = 'HELP').url = "https://www.artunchained.de/tiny-new-addon-to-all/"
            row.operator('wm.url_open', text = 'Follow Path', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?325179-Follow-Path-Array"
            row.operator('wm.url_open', text = 'Copy2', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?347973-add-on-Copy2-vertices-edges-or-faces"
            row.operator('wm.url_open', text = 'Copy Attributes', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Copy_Attributes_Menu"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?409893-Addon-T-CopyShop&p=3116714#post3116714"


# PROPERTY GROUP #
# containe all properties for the gui in the panel
class Dropdown_TP_CopyShop_Props(bpy.types.PropertyGroup):

    display_copy_to_faces = bpy.props.BoolProperty(name = "Copy to Faces Tools", description = "open / close props", default = False)
    display_toall = bpy.props.BoolProperty(name = "Copy to All", description = "open / close props", default = False)
    display_pfath = bpy.props.BoolProperty(name = "Follow Path Array", description = "open / close props", default = False)
    display_empty = bpy.props.BoolProperty(name = "Empty Array", description = "open / close props", default = False)
    display_array = bpy.props.BoolProperty(name = "Curve Array", description = "open / close props", default = False)
    display_axis_array = bpy.props.BoolProperty(name = "Axis Array", description = "open / close props", default = False)
    display_array_tools = bpy.props.BoolProperty(name = "Array Tools", description = "open / close props", default = False)
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_display = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    





# REGISTRY #

import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position(None, bpy.context)

    ### Tools
    update_menu(None, bpy.context)
    update_display_tools(None, bpy.context)


    ### copyaction
    bpy.types.WindowManager.tp_collapse_copyshop_props = bpy.props.PointerProperty(type = Dropdown_TP_CopyShop_Props)
   
    ### miftthtools
    bpy.types.Scene.mifthTools = PointerProperty(name="Mifth Tools Variables", type=MFTProperties, description="Mifth Tools Properties")


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    ### copyaction
    del bpy.types.WindowManager.tp_collapse_copyshop_props 
 
    ### miftthtools
    del bpy.types.Scene.mifthTools     



if __name__ == "__main__":
    register()
        
        





