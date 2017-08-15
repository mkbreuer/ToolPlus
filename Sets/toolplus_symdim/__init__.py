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
    "name": "T+ SymDim",
    "author": "mkbreuer",
    "version": (1, 0, 1),
    "blender": (2, 7, 8),
    "location": "VIEW3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "Addon for symmetrizing objects",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD UI #

from toolplus_symdim.sym_ui_panel       import (VIEW3D_TP_Symmetry_Panel_TOOLS)
from toolplus_symdim.sym_ui_panel       import (VIEW3D_TP_Symmetry_Panel_UI)


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


# UI REGISTRY #

def update_panel_location(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Symmetry_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Symmetry_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Symmetry_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_Symmetry_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        
        bpy.utils.register_class(VIEW3D_TP_Symmetry_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Symmetry_Panel_UI)
  

    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass



# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),  
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)


    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="T+ SimDim!")  
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


        #Location
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


        #Weblinks
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column_flow(2)
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?427208-Addon-T-SymDim"
            row.operator('wm.url_open', text = 'GitHub', icon = 'SCRIPT').url = "https://github.com/mkbreuer/ToolPlus"




# PROPERTY GROUP #
class Dropdown_TP_Symmetry_Props(bpy.types.PropertyGroup):

    display_dim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    




# REGISTRY #

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_collapse_menu_symmetry = bpy.props.PointerProperty(type = Dropdown_TP_Symmetry_Props)
       
    update_panel_location(None, bpy.context)



def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    del bpy.types.WindowManager.tp_collapse_menu_symmetry
    
if __name__ == "__main__":
    register()
        
        




              
