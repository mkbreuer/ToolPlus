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
    "version": (0, 4),
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



# UPDATE TOOLS #
def update_tools_vse(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None    




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


    # OPTIONS #    
    expand_panel_tools = bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)    


    # TOOLS #
    tab_vse_view = bpy.props.EnumProperty(name = 'View Tools', description = 'on / off',
                  items=(('on', 'View on', 'enable tools in panel'), ('off', 'View off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_add = bpy.props.EnumProperty(name = 'Add Tools', description = 'on / off',
                  items=(('on', 'Add on', 'enable tools in panel'), ('off', 'Add off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_select = bpy.props.EnumProperty(name = 'Select Tools', description = 'on / off',
                  items=(('on', 'Select on', 'enable tools in panel'), ('off', 'Select off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_move = bpy.props.EnumProperty(name = 'Move Tools', description = 'on / off',
                  items=(('on', 'Move on', 'enable tools in panel'), ('off', 'Move off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_edit = bpy.props.EnumProperty(name = 'Edit Tools', description = 'on / off',
                  items=(('on', 'Edit on', 'enable tools in panel'), ('off', 'Edit off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_marker = bpy.props.EnumProperty(name = 'Marker Tools', description = 'on / off',
                  items=(('on', 'Marker on', 'enable tools in panel'), ('off', 'Marker off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_history = bpy.props.EnumProperty(name = 'History Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_tools_vse)

    tab_vse_custom = bpy.props.EnumProperty(name = 'Custom Tools', description = 'on / off',
                  items=(('on', 'Custom on', 'enable tools in panel'), ('off', 'Custom off', 'disable tools in panel')), default='off', update = update_tools_vse)

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
            row = box.column(1)   
            row.label(text="Welcome T+ VSE!")    
            
            row.separator()                            
            row.label(text="> This addon appends functions to the vse header as button tools")                    
            row.label(text="> open the Gear Button to enable or disable tools in the header")  
            row.label(text="> Save user setting to apply the changes durably.")         

            row.separator()    
            row.label(text="Have Fun! ;)")



        # TOOLS #
        if self.prefs_tabs == 'tools':
      
            box = layout.box().column(1)
          
            box.separator() 
            box.separator()             
           
            row = box.column_flow(4)  
            row.label("Header UI", icon ="COLLAPSEMENU") 

            row = box.column_flow(3)
            row.prop(self, 'tab_vse_view', expand=True)
            row.prop(self, 'tab_vse_add', expand=True)
            row.prop(self, 'tab_vse_select', expand=True)
            row.prop(self, 'tab_vse_move', expand=True)
            row.prop(self, 'tab_vse_edit', expand=True)
            row.prop(self, 'tab_vse_marker', expand=True)
            row.prop(self, 'tab_vse_history', expand=True)
            row.prop(self, 'tab_vse_custom', expand=True)
        
            box.separator()


        # WEB #
        if self.prefs_tabs == 'urls':
            row = layout.column_flow(1)
            row.operator('wm.url_open', text = 'DemoVideo', icon = 'CLIP').url = "https://www.youtube.com/watch?v=Hz2dCXEI9aU"
            row.operator('wm.url_open', text = 'GitHub', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?394914-Addon-VSE-IconTools&highlight="



    
# REGISTRY #
import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_menu_vse(None, bpy.context)
    update_tools_vse(None, bpy.context)


def unregister():  

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()


if __name__ == "__main__":
    register()
        
        



