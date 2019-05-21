# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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
    "name": "SnapOrigin",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 0, 2),
    "blender": (2, 79, 0),
    "location": "3D View > Tool [T] or Property [N] Shelf Panel, Menus [SHIFT+2], Special Menu [W]",
    "description": "collection of origin modal operators",
    "warning": "/",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "category": "ToolPlus",
}


# LOAD MODULES #
import bpy
from bpy.props import *
import addon_utils

# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

# LOAD CUSTOM ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons

from .ot_bbox           import *
from .ot_check          import *
from .ot_editor         import *
from .ot_helper         import *
from .ot_modal          import *
from .ui_panel          import *
from .ui_menu           import *
from .ui_menu_pie       import *
from .ui_menu_special   import *
from .ui_keymap         import *

importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())


# PANEL TO CONTAINING THE TOOLS #
class VIEW3D_PT_SnapOrigin_Panel_TOOLS(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'T+'
    bl_label = "SnapOrigin"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_snaporigin_ui(self, context, layout)


class VIEW3D_PT_SnapOrigin_Panel_UI(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "SnapOrigin"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_snaporigin_ui(self, context, layout)



# UPDATE TAB CATEGORY FOR PANEL IN THE TOOLSHELF #
panels = (VIEW3D_PT_SnapOrigin_Panel_UI, VIEW3D_PT_SnapOrigin_Panel_TOOLS)

def update_panel(self, context):
    message = "Template: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_snaporigin_location == 'tools':
         
            VIEW3D_PT_SnapOrigin_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.category
            bpy.utils.register_class(VIEW3D_PT_SnapOrigin_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_snaporigin_location == 'ui':
            
            bpy.utils.register_class(VIEW3D_PT_SnapOrigin_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_snaporigin_location == 'off':  
            return None

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass




# ADDON PREFERENCES PANEL #
class Addon_Preferences_SnapOrigin(bpy.types.AddonPreferences):
    bl_idname = __name__

    # INFO LIST #
    prefs_tabs=EnumProperty(
        items=(('info',  "Info",   "Info"),
               ('panel', "Panel",  "Panel"),
               ('menus', "KeyMap", "KeyMap"),
               ('tools', "Tools",  "Tools")),
        default='info')

    #------------------------------

    # PANEL #          
    tab_snaporigin_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf',      'place panel in the tool shelf [T]'),
               ('ui',    'Property Shelf',  'place panel in the property shelf [N]'),
               ('off',   'Remove Panel',    'remove the panel')),
               default='tools', update = update_panel)

    category=StringProperty(
              name="Tab Category",
              description="Choose a name for the category of the panel",
              default="Tools",
              update=update_panel
              )

    #------------------------------

    # MENU #
    tab_snaporigin_menu=EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Use Menu', 'enable menu for 3D View'),
               ('pie',    'Use Pie',  'enable pie for 3D View'),
               ('remove', 'Disable',  'disable menus for 3D View')),
        default='menu', update = update_snaporigin_menu)


    # SUBMENUS #    
    tab_snaporigin_special=EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('prepend', 'Menu Top',    'add menus to default special menus'),
               ('append',  'Menu Bottom', 'add menus to default special menus'),
               ('remove',  'Menu Remove', 'remove menus from default menus')),
        default='remove', update = update_snaporigin_special)               


    #----------------------------


    # TOOLS #

    threshold = bpy.props.FloatProperty(name="Threshold",  description="select linked face", default=0.1, min=0.1, max=10)
      
    #----------------------------
    
    
    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout

        icons = load_icons()        
       
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)


        # INFO #
        if self.prefs_tabs == 'info':

            box = layout.box().column(align=True)
            box.separator() 
 
            row = box.column(align=False)
            row.label(text="Snap Origin Modal Collection")               

            box.separator() 
            
            row.label(text="> Origin to Snap: set origin with a emtpty to snap point [CTRL].")   
            row.label(text="> Origin to Mesh: set origin to selected vertex, edge or face.")   
            row.label(text="> Origin to BBox: set origin to a bounding box.")   
            row.label(text="> Clear Location: set origin to mesh and relocate object to global center.")   

            box.separator()       


        # TOOLS #
        if self.prefs_tabs == 'tools':
            
            box = layout.box().column(align=True)
            box.separator() 

            row = box.row(align=True)
            row.alignment = 'LEFT'
            row.label(text="Select linked face by angle")   
            row.prop(self, "threshold", text="Threshold:")           
           
            box.separator() 
 
            row = box.column(align=False)
            row.label(text="> settings also available in the panel")   

            box.separator() 

            loop_tools_addon = "mesh_looptools" 
            state = addon_utils.check(loop_tools_addon)
            if not state[0]:                         
                
                row = box.column(1) 
                row.operator("tpc_ot.enable_looptools", text="!_Activate Looptools for Flatten LPT_!", icon='BLANK1')    
                
                box.separator()

            else:
                pass




        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(align=True)
             
            row = box.row(1) 
            row.label("Panel Location:")
         
            box.separator()             
         
            row = box.row(1)
            row.prop(self, 'tab_snaporigin_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_snaporigin_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "category")

            box.separator() 
            box.separator() 



        # APPEND #
        if self.prefs_tabs == 'menus':

            col = layout.column(align=True)   

            box = col.box().column(align=True)

            box.separator()
            
            row = box.row(align=True)  
            row.label(text="Cascade Menu: [SHIFT+1] ", icon ="COLLAPSEMENU")        

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snaporigin_menu', expand=True)
         
            if self.tab_snaporigin_menu == 'pie': 
               
                box.separator()   
              
                row = box.column(align=True)                                                  
                row.label(text="> This menu is work in progress and always a proposal.")
                row.label(text="> Left or right, up or down, there are too many preferences,")
                row.label(text="> to create a pie menu for everyone.")
                row.label(text="> But it would be handy if you work with a bigger screen.")

 
            box.separator()
            box.separator()

            #-----------------------------------------------------

            box = col.box().column(align=True)
         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="Special Menu [W]", icon ="COLLAPSEMENU")         

            box.separator()            
         
            row = box.column(align=True)          
            row.label(text="A snaporigin menu will be added to the default special menu.")

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snaporigin_special', expand=True)

            box.separator()
            box.separator()


            #-----------------------------------------------------

            box = col.box().column(align=True)
           
            box.separator()              
            box.separator()              

            # TIP #            
            row = box.row(align=True)             
            row.label(text="! For key change go to > Edit: Preferences > Keymap !", icon ="INFO")

            row = box.column(align=True) 
            row.label(text="1 > change search to key-bindig and insert the hotkey: shift 1", icon ="BLANK1")
            row.label(text="2 > go to 3D View > Call Menu [SHIFT+2]: VIEW3D_TP_SnapOrigin_Menu /_Pie!", icon ="BLANK1")
            row.label(text="3 > choose a new key configuration and save preferences !", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)             
            row.label(text="Or edit the keymap script directly:", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)  
            row.label(text="", icon ="BLANK1")
            row.operator("tpc_ot.keymap_snaporigin", text = 'Open KeyMap in Text Editor')
            row.operator('wm.url_open', text = 'Type of Events').url = "https://github.com/mkbreuer/Misc-Share-Archiv/blob/master/images/SHORTCUTS_Type%20of%20key%20event.png?raw=true"
            
            box.separator()



# REGISTER #
classes = (
    VIEW3D_OT_Snap_Origin_to_BBox,
    VIEW3D_OT_Snap_Origin_to_Helper,
    VIEW3D_OT_Snap_Origin_Modal_Multi,
    VIEW3D_OT_Activate_Looptools,
    VIEW3D_OT_KeyMap_SnapOrigin,
    VIEW3D_MT_SnapOrigin_Menu_Special,
    Addon_Preferences_SnapOrigin,
)

import traceback
import bpy.utils.previews

def register():
    try:
        for cls in classes:
            bpy.utils.register_class(cls)
    except:
        traceback.print_exc()

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))

    update_panel(None, bpy.context)
    update_snaporigin_menu(None, bpy.context)
    update_snaporigin_special(None, bpy.context)



def unregister():
    try:
        for cls in classes:
            bpy.utils.unregister_class(cls)
    except:
        traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))

if __name__ == "__main__":
    register()



