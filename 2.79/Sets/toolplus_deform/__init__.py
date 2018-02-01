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
    "name": "T+ Deform",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 6),
    "blender": (2, 7, 9),
    "location": "View3D > Panel: Deform",
    "description": "collection of deform tools",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus/wiki",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_deform.deform_manual  import (VIEW3D_TP_Deform_Manual)

# LOAD UI #
from toolplus_deform.deform_ui_panel    import (VIEW3D_TP_Deform_Panel_TOOLS)
from toolplus_deform.deform_ui_panel    import (VIEW3D_TP_Deform_Panel_UI)

# LOAD CUSTOM ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons

# LOAD OPERATOR #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_deform'))


if "bpy" in locals():
    import imp
   
    imp.reload(deform_action)     
    imp.reload(deform_bounding)    
    imp.reload(deform_easylattice)    
    imp.reload(deform_modifier)  

    print("Reloaded multifiles")
    
else:
   
    from . import deform_action
    from . import deform_bounding    
    from . import deform_easylattice    
    from . import deform_modifier

    print("Imported multifiles")


import deform_bounding    
import deform_easylattice    
import deform_modifier



# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*
from toolplus_deform.deform_keymap  import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Deform_Panel_UI)        
        bpy.utils.unregister_class(VIEW3D_TP_Deform_Panel_TOOLS)        
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Deform_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_deform == 'tools':
        
        VIEW3D_TP_Deform_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_deform       
        bpy.utils.register_class(VIEW3D_TP_Deform_Panel_TOOLS)

    else:
        bpy.utils.register_class(VIEW3D_TP_Deform_Panel_UI)



# REGISTRY TOOLS #
def update_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None    

    


#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('toolsets',   "Tools",      "Tools"),
               ('keymap',     "Keymap",     "Keymap"),
               ('url',        "URLs",       "URLs")),
               default='info')
           
    tab_location_deform = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position)

    tab_menu_deform = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)


    tab_vertgrp = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'VertexGroup on', 'enable tools in panel'), ('off', 'VertexGroup off', 'disable tools in panel')), default='on', update = update_tools)

    tab_hook = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Hook on', 'enable tools in menu'), ('off', 'Hook off', 'disable tools in menu')), default='off', update = update_tools)
 
    tab_vertgrp_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'VertexGroup on', 'enable tools in panel'), ('off', 'VertexGroup off', 'disable tools in panel')), default='on', update = update_tools)

    tab_hook_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Hook on', 'enable tools in menu'), ('off', 'Hook off', 'disable tools in menu')), default='off', update = update_tools)


    tools_category_deform = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)


    def draw(self, context): 

        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="Welcome to T+ Deform")
            
            row = layout.column()
            row.label(text="This setup helps to adjust a mesh a bit easier.")                                                     
            row.label(text="Have Fun! :) ")     
            

        # TOOLS #
        if self.prefs_tabs == 'toolsets':

            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_vertgrp', expand=True)
            row.prop(self, 'tab_hook', expand=True)

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        # LOCATION #
        if self.prefs_tabs == 'location':
          
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location Deform:")
            
            row = box.row(1)
            row.prop(self, 'tab_location_deform', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location_deform == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_deform")

            box.separator() 

            row = layout.row()
            row.label(text="! please reboot blender after changing the panel location !", icon ="INFO")
            
            
        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Deform Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: [CTRL+SHIFT+D]")

            row = box.row(1)          
            row.prop(self, 'tab_menu_deform', expand=True)
            
            if self.tab_menu_deform == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
        
            row = box.row()  
            row.prop(self, 'tab_vertgrp_menu', expand=True)
            row.prop(self, 'tab_hook_menu', expand=True)

  
            # TIP #
            box.separator()
            
            row = layout.row(1)             
            row.label(text="! For default key change > go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey: ctrl shift d ", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: 'tp_menu.batch_deform' !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > You can use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = layout.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = layout.row(1) 
            row.operator("tp_ops.keymap_deform", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()  

       
        # WEB #
        if self.prefs_tabs == 'url':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="The list of auxiliary addons that a belong to this collection:")      

            row.separator() 
                                    
            row = box.row()
            row.operator('wm.url_open', text = 'Easy Lattice', icon = 'INFO').url = "http://wiki.blender.org/index.php/Easy_Lattice_Editing_Addon"
            row.operator('wm.url_open', text = 'THREAD', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?409575-Addon-T-Deform&p=3114846#post3114846"




# PROPS #
class Dropdown_Deform_Tool_Props(bpy.types.PropertyGroup):

    display_mod_hook = bpy.props.BoolProperty(name="Hook Props", description="open / close", default=False)




# REGISTRY #        

def register():
    
    deform_easylattice.register()    
    deform_modifier.register()

    bpy.utils.register_module(__name__)
    
    # PROPS #
    bpy.types.WindowManager.tp_props_defom_window = bpy.props.PointerProperty(type = Dropdown_Deform_Tool_Props)

    update_tools(None, bpy.context)
    update_menu(None, bpy.context)
    update_panel_position(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Deform_Manual)



def unregister():

    deform_easylattice.unregister()    
    deform_modifier.unregister()

    bpy.utils.unregister_module(__name__)
   
    # PROPS #
    del bpy.types.WindowManager.tp_props_defom
 
    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Deform_Manual)
 
    
if __name__ == "__main__":
    register()
        
        



            



