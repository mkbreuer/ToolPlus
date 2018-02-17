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
    "name": "T+ SymDim",
    "author": "marvin.k.breuer (MKB)",
    "version": (1, 2),
    "blender": (2, 7, 9),
    "location": "VIEW3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "Addon for symmetrizing objects",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_symdim.sym_manual  import (VIEW3D_TP_SymDim_Manual)


# LOAD UI #
from toolplus_symdim.sym_panel       import (VIEW3D_TP_SymDim_Panel_TOOLS)
from toolplus_symdim.sym_panel       import (VIEW3D_TP_SymDim_Panel_UI)


# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_symdim'))

if "bpy" in locals():
    import imp
    imp.reload(sym_cut)
    imp.reload(sym_dim)
    imp.reload(sym_mods)

else:       
    from . import sym_cut                                          
    from . import sym_dim                            
    from . import sym_mods                
          

# LOAD MODULS #
import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# LOAD MAPS #
from toolplus_symdim.sym_keymap  import*
from toolplus_symdim.sym_uimap   import*

# REGISTRY TOOLS # 
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
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


    # LOCATION #           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)


    # MENU #
    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_symdim)

    # TOOLS #
    tab_vertical_menu = EnumProperty(name = 'Display Tools', description = 'switch ui in menu',
                  items=(('on', 'Vertical Menu', 'switch ui'), ('off', 'Horziontal Menu', 'switch ui')), default='on', update = update_display_tools)


    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="T+ SymDim!")  
            row.label(text="Addon for symmetrizing objects (origin=pivot)")
            row.label(text="Functions:")
            row.label(text="1 > cut mesh and delete choosen side")
            row.label(text="2 > cut mesh and add mirror modifier")
            row.label(text="3 > cut mesh, add and apply mirror modifier continuous")
            row.label(text="4 > switch in and stay in editmode")
            row.label(text="5 > switch in and stay in sculptmode")
            row.label(text="6 > copy dimension from axis to axis")
            row.label(text="7 > delete both sides to get a profil loopcut")
           
            row.separator()
                        
            row.label(text="Happy Blending! :)")         


        # LOCATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Symmetry Panel")
            
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




        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu: [ALT+SHIFT+Y]", icon ="COLLAPSEMENU") 

            row = box.row()          
            row.prop(self, 'tab_menu_view', expand=True)
            row.prop(self, 'tab_vertical_menu', expand=True)             


            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

  
 
            box.separator()
      
            # TIP #            
            row = layout.row(1)             
            row.label(text="! For default key change > go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey: ctrl v", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_SymDim_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > You can use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = layout.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = layout.row(1) 
            row.operator("tp_ops.keymap_symdim", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()  
            

        # WEB #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column_flow(2)
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?427208-Addon-T-SymDim"
            row.operator('wm.url_open', text = 'GitHub', icon = 'SCRIPT').url = "https://github.com/mkbreuer/ToolPlus"




# PROPERTY: SYMDDIM #
class Dropdown_TP_Symmetry_Props(bpy.types.PropertyGroup):

    display_dim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    




# REGISTRY #

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_collapse_menu_symmetry = bpy.props.PointerProperty(type = Dropdown_TP_Symmetry_Props)
       
    update_panel_location(None, bpy.context)
    update_menu_symdim(None, bpy.context)
    update_display_tools(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_SymDim_Manual)




def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    del bpy.types.WindowManager.tp_collapse_menu_symmetry
    
    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_SymDim_Manual)


if __name__ == "__main__":
    register()
        
        




              
