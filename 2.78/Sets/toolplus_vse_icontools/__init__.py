#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#Copyright (C) 2017  Marvin.K.Breuer (MKB)]
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "T+ VSE IconTools",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 3),
    "blender": (2, 7, 8),
    "location": "Video Sequences Editing (VSE):  Header",
    "description": "add Functions as Icon Buttons to the VSE Header",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"
    }





# LOAD ICONS DEF#
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #    

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_vse_icontools'))

 
if "bpy" in locals():
    import imp
    

    imp.reload(vse_header_one)    
    imp.reload(vse_header_two)    
    
    print("Reloaded operators")
        
else:
    from . import  vse_header_one 
    from . import  vse_header_two 
    
    print("Imported operators")



# LOAD MODULS #

import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# TOOLS REGISTRY #

def update_vse_tools(self, context):


    # TOOLS ON

    if context.user_preferences.addons[__name__].preferences.tab_header_view == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_add == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_select == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_move == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_edit == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_marker == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_history == 'on':
        return
    

    # TOOLS OFF 
    
    if context.user_preferences.addons[__name__].preferences.tab_header_view == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_add == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_select == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_move == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_edit == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_marker == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_header_history == 'off':
        return
    
    

# ADDON PREFERENCES #

class TP_Addon_Preferences(AddonPreferences):
    bl_idname = __name__
    
    #THEME TABS
    prefs_tabs = bpy.props.EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('url',        "URLs",       "URLs")),
         default='info')



    #TOOLS PROPS
    tab_header_view = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Header on', 'enable tools in panel'), ('off', 'Header A off', 'disable tools in panel')), default='off', update = update_vse_tools)

    tab_header_add = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Add on', 'enable tools in panel'), ('off', 'Add off', 'disable tools in panel')), default='off', update = update_vse_tools)

    tab_header_select = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Select on', 'enable tools in panel'), ('off', 'Select off', 'disable tools in panel')), default='off', update = update_vse_tools)

    tab_header_move = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Move A on', 'enable tools in panel'), ('off', 'Move A off', 'disable tools in panel')), default='off', update = update_vse_tools)

    tab_header_edit = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Edit on', 'enable tools in panel'), ('off', 'Edit off', 'disable tools in panel')), default='off', update = update_vse_tools)

    tab_header_marker = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Marker on', 'enable tools in panel'), ('off', 'Marker off', 'disable tools in panel')), default='off', update = update_vse_tools)

    tab_header_history = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='off', update = update_vse_tools)



    #PREFERENCE LAYOUT
    def draw(self, context):
        layout = self.layout        
        
        #INFO
        row= layout.row(1)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome T+ VSE Icon Tools!")    
            
            row.separator()  
            
            row.label(text="This Addon adds the VSE Function as Icon Buttons to the Video Sequences Editing (VSE) Header")    
            
            row.separator()  
            
            row.label(text="You can toggle the functions in two ways:")  

            row.separator()  
            
            row.label(text="1: Permanent over the Addon Preferences TAB: Tools")  
            row.label(text="> the tools are visible with each blender start, when the user settings are saved")  

            row.separator()  
            
            row.label(text="2: Dynamical over the VSE Header Menu: View") 
            row.label(text="> the tools are only visible until blender is closed")                        
      
            row.separator()                           
       
            row.label(text="Under URL you find a link to short demo video")   
 
            row.separator()            
                        
            row.label(text="Have Fun! :)")


        #TOOLS
        if self.prefs_tabs == 'toolsets':

            box = layout.box().column(1)

            row = box.row()
            row.label("Header Tools")            
            
            row = box.column_flow(3)
            row.prop(self, 'tab_header_view', expand=True)
            row.prop(self, 'tab_header_add', expand=True)
            row.prop(self, 'tab_header_select', expand=True)
            row.prop(self, 'tab_header_move', expand=True)
            row.prop(self, 'tab_header_edit', expand=True)
            row.prop(self, 'tab_header_marker', expand=True)
            row.prop(self, 'tab_header_history', expand=True)
        
            box.separator()


        #WEBLINKS
        if self.prefs_tabs == 'url':
            row = layout.column_flow(1)
            row.operator('wm.url_open', text = 'DemoVideo', icon = 'CLIP').url = "https://www.youtube.com/watch?v=Hz2dCXEI9aU"
            row.operator('wm.url_open', text = 'GitHub', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?394914-Addon-VSE-IconTools&highlight="




# PROPERTIES: View Menu Buttons #

class Dropdown_FTH_VSE_Props(bpy.types.PropertyGroup):

    display_vse_view = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False) 
    display_vse_select = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False) 
    display_vse_move = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False) 
    display_vse_marker = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False) 
    display_vse_add = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False) 
    display_vse_edit = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False) 




# DRAW: add Button to View Header Menu #

def draw_item(self, context):
    tp = context.window_manager.tp_vse_window
    layout = self.layout
    
    layout.separator()
    
    layout.operator("tp_vse.enable_all", text="Enable All",  icon = "TRIA_RIGHT")
    layout.operator("tp_vse.disable_all", text="Disable All",  icon = "TRIA_LEFT")

    if tp.display_vse_add:
        layout.prop(tp, "display_vse_add", text="Icon Add")
    else:
        layout.prop(tp, "display_vse_add", text="Icon Add")

    if tp.display_vse_view:
        layout.prop(tp, "display_vse_view", text="Icon View")
    else:
        layout.prop(tp, "display_vse_view", text="Icon View")

    if tp.display_vse_select:
        layout.prop(tp, "display_vse_select", text="Icon Select")
    else:
        layout.prop(tp, "display_vse_select", text="Icon Select")

    if tp.display_vse_move:
        layout.prop(tp, "display_vse_move", text="Icon Move")
    else:
        layout.prop(tp, "display_vse_move", text="Icon Move")

    if tp.display_vse_marker:
        layout.prop(tp, "display_vse_marker", text="Icon Marker")
    else:
        layout.prop(tp, "display_vse_marker", text="Icon Marker")

    if tp.display_vse_edit:
        layout.prop(tp, "display_vse_edit", text="Icon Strip")
    else:
        layout.prop(tp, "display_vse_edit", text="Icon Strip")

    layout.label("VSE IconTools")
    
    layout.separator()







# REGISTRY #
import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
   
    bpy.types.SEQUENCER_MT_view.prepend(draw_item)       
   
    bpy.types.WindowManager.tp_vse_window = bpy.props.PointerProperty(type = Dropdown_FTH_VSE_Props)

    update_vse_tools(None, bpy.context)



def unregister():
  
    del bpy.types.WindowManager.tp_vse_window

    bpy.types.SEQUENCER_MT_view.remove(draw_item)  
    
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
     

if __name__ == "__main__":
    register()
        
        
