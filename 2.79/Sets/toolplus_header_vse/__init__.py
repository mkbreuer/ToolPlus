# ##### BEGIN GPL LICENSE BLOCK #####
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
    "name": "T+ VSE (Header)",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 5),
    "blender": (2, 7, 9),
    "location": "Video Sequences Editing (VSE):  Header",
    "description": "add Functions as Icon Buttons to the VSE Header",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"
    }




# LOAD CUSTOM ICONS #
from . icons.icons    import load_icons
from . icons.icons    import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_header_vse'))

if "bpy" in locals():
    import imp
 
    imp.reload(vse_append)    
else:
    from . vse_append  import*


# LOAD MODULS #
import bpy
from bpy import *
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



# ADDON PREFERNECES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__

    #THEME TABS
    prefs_tabs = bpy.props.EnumProperty(
        items=(('info',   "Info",   "Info"),
               ('tools',  "Tools",  "Tools"),
               ('urls',   "URLs",   "URLs")),
         default='info')


    #----------------------------------------------------------------------------------------
 
    # MENU #
    tab_menu_vse = EnumProperty(
        name = 'Header Menu',
        description = 'enable or disable menu for Header',
        items=(('add', 'Menu on', 'enable menu for Header'),
               ('remove', 'Menu off', 'disable menu for Header')),
        default='add', update = update_menu_vse)


    # TOOLS #  
    tab_vse_view = bpy.props.BoolProperty(name="View", description="show or hide tools in the header", default=True)    
    tab_vse_add = bpy.props.BoolProperty(name="Add", description="show or hide tools in the header", default=True)    
    tab_vse_select = bpy.props.BoolProperty(name="Select", description="show or hide tools in the header", default=True)    
    tab_vse_move = bpy.props.BoolProperty(name="Move", description="show or hide tools in the header", default=True)    
    tab_vse_edit = bpy.props.BoolProperty(name="Edit", description="show or hide tools in the header", default=True)    
    tab_vse_marker = bpy.props.BoolProperty(name="Marker", description="show or hide tools in the header", default=True)    
    tab_vse_history = bpy.props.BoolProperty(name="History", description="show or hide tools in the header", default=True)    
    tab_vse_custom = bpy.props.BoolProperty(name="Custom", description="show or hide tools in the header", default=False)    

    #----------------------------------------------------------------------------------------
 

    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome T+ Header VSE!")    
            
            row.separator()                            
            row.label(text="> This addon appends functions to the vse header as button tools")                    
            row.label(text="> open the Gear Button to enable or disable tools in the header")  
            row.label(text="> Save user setting to apply the changes durably.")         

            row.separator()    
            row.label(text="Have Fun! ;)")



        # TOOLS #
        if self.prefs_tabs == 'tools':
      
            box = layout.box().column(1)

            row = box.row()             
            row.label("Header UI", icon ="COLLAPSEMENU") 
            row.prop(self, 'tab_menu_vse', expand=True)          
           
           
            box.separator() 
            box.separator()             
           
            row = box.column()  
            row.label("Header Tools", icon ="COLLAPSEMENU") 

            row = box.column_flow(3)
            row.prop(self, 'tab_vse_view')
            row.prop(self, 'tab_vse_add')
            row.prop(self, 'tab_vse_select')
            row.prop(self, 'tab_vse_move')
            row.prop(self, 'tab_vse_edit')
            row.prop(self, 'tab_vse_marker')
            row.prop(self, 'tab_vse_history')
            row.prop(self, 'tab_vse_custom')
        
            box.separator()
            box.separator()
            
            row = box.column(1)              
            row.operator('tp_ops.keymap_custom_vse', text = 'Open Layout in Text Editor')

            box.separator()      

      
        # WEB #
        if self.prefs_tabs == 'urls':

            row = layout.column(1)
            row.operator('wm.url_open', text = 'DemoVideo', icon = 'CLIP').url = "https://www.youtube.com/watch?v=Hz2dCXEI9aU"
            row.operator('wm.url_open', text = 'GitHub', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?394914-Addon-VSE-IconTools&highlight="




# OPEN FILE IN TEXT EDITOR #
from os.path import dirname
from . import vse_menu

class View3D_TP_KeyMap_Custom_VSE(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_custom_vse"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = vse_menu.__file__
        bpy.data.texts.load(path)    
        return {"FINISHED"}

    
# REGISTRY #
import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_menu_vse(None, bpy.context)

def unregister():  

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()


if __name__ == "__main__":
    register()
        
        



