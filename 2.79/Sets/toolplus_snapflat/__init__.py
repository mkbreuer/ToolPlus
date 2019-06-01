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
    "name": "SnapFlat",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 0, 4),
    "blender": (2, 79, 0),
    "location": "3D View > Tool- or Propertyshelf Panel [N], Menus [SHIFT+W], Special Menu [W], Header",
    "description": "flat linked face",
    "warning": "/",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "category": "ToolPlus",
}


# LOAD MODULES #
import bpy
from bpy.props import *


# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

# LOAD CUSTOM ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons

from .ot_flatten        import *
from .ot_editor         import *
from .ui_panel          import *
from .ui_menu           import *
from .ui_menu_pie       import *
from .ui_menu_special   import *
from .ui_keymap         import *

importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())


# PANEL TO CONTAINING THE TOOLS #
class VIEW3D_PT_SnapFlat_Panel_TOOLS(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'T+'
    bl_context = 'mesh_edit'
    bl_label = "SnapFlat"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_snapflat_ui(self, context, layout)


class VIEW3D_PT_SnapFlat_Panel_UI(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = 'mesh_edit'
    bl_label = "SnapFlat"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_snapflat_ui(self, context, layout)



# UPDATE TAB CATEGORY FOR PANEL IN THE TOOLSHELF #
panels = (VIEW3D_PT_SnapFlat_Panel_UI, VIEW3D_PT_SnapFlat_Panel_TOOLS)

def update_panel(self, context):
    message = "Template: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_snapflat_location == 'tools':
         
            VIEW3D_PT_SnapFlat_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.category
            bpy.utils.register_class(VIEW3D_PT_SnapFlat_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_snapflat_location == 'ui':
            
            bpy.utils.register_class(VIEW3D_PT_SnapFlat_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_snapflat_location == 'off':  
            return None

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass




# ADDON PREFERENCES PANEL #
class Addon_Preferences_SnapFlat(bpy.types.AddonPreferences):
    bl_idname = __name__

    # INFO LIST #
    prefs_tabs=EnumProperty(
        items=(('info',  "Info",   "Info"),
               ('panel', "Panel",  "Panel"),
               ('menus', "Menus",  "Menus"),
               ('tools', "Tools",  "Tools")),
        default='info')

    #------------------------------

    # PANEL #          
    tab_snapflat_location = EnumProperty(
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

    show_snapflat_buttons = bpy.props.BoolProperty(name="Show Button in Panel", description="on / off", default=True)   


    #------------------------------

    # MENU #
    tab_snapflat_menu=EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Use Menu', 'enable menu for 3D View'),
               ('pie',    'Use Pie',  'enable pie for 3D View'),
               ('remove', 'Disable',  'disable menus for 3D View')),
        default='menu', update = update_snapflat_menu)


    # SUBMENUS #    
    tab_snapflat_special=EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('prepend', 'Menu Top',    'add menus to default special menus'),
               ('append',  'Menu Bottom', 'add menus to default special menus'),
               ('remove',  'Menu Remove', 'remove menus from default menus')),
        default='remove', update = update_snapflat_special)               

    toggle_special_snapflat_separator = bpy.props.BoolProperty(name="Toggle SubSeparator", description="on / off", default=True)   
    toggle_special_snapflat_icon = bpy.props.BoolProperty(name="Toggle SubMenu Icon", description="on / off", default=False)   
   
  
    #----------------------------


    # KEYMAP #
      
    use_hotkey=bpy.props.StringProperty(name = 'Key', default="TWO", description = 'change hotkey / only capital letters allowed') 
    use_ctrl=BoolProperty(name= 'use Ctrl', description = 'enable ctrl for button m', default=False) 
    use_alt=BoolProperty(name= 'use Alt', description = 'enable ctrl for button m', default=False) 
    use_shift=BoolProperty(name= 'use Shift', description = 'enable ctrl for button m', default=True) 
    use_event = EnumProperty(
        items=[('DOUBLE_CLICK',  "DOUBLE CLICK", "key event"),
               ('CLICK',         "CLICK",        "key event"),
               ('RELEASE',       "RELEASE",      "key event"),
               ('PRESS',         "PRESS",        "key event"),
               ('ANY',           "ANY",          "key event"),],
        name="key event",
        default='PRESS')

    #----------------------------


    # TOOLS #

    # 1°= 0.0174533
    # 180°= 3.14159

    threshold = bpy.props.FloatProperty(name="Threshold",  description="angle value to select linked face", default=0.0174533, min=0.0174533, max=3.14159, subtype='ANGLE')

    mesh_select_mode = bpy.props.EnumProperty(
      items = [("vertices", "Vertex", "enable vertex selection", 1),
               ("edges",    "Edge",   "enable edge selection"  , 2), 
               ("faces",    "Face",   "enable face selection"  , 3)], 
               name = "Mesh Select Mode",
               default = "vertices",
               description="type of mesh select mode when finish")


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
            row.label(text="Welcome to SnapFlat Modal!") 

            box.separator() 
            
            row = box.column(align=False)
            row.label(text="This addon contains modal operators to flatten mesh or")   
            row.label(text="creating sharp edges or uvs seam on the selection boundary.")   
            row.label(text="Useful to straighten the mesh surface after bevel.")   
            
            row = box.column(align=False)
            row.label(text="Order of tools in the menu")  
            box.separator() 
            
            row = box.column(align=False)                         
            row.label(text="Flatten LPT > flatten with looptools flatten")   
            row.label(text="Flatten XYZ-Axis > flatten to x, y or z axis")   
            row.label(text="Flatten Normal > flatten in normal axis direction")   
            row.label(text="Boundary Sharp Edges > select linked face and create sharp edges")   
            row.label(text="Boundary UV Seams > select linked face and create uvs seams")   
           
            box.separator() 
 
            row = box.column(align=False)
            row.label(text="When running:")   
            row.label(text="> The select mode switch to face selection.")   
            row.label(text="> After selecting a face, the face selection grows,")   
            row.label(text="> dependent to the threshold for select linked faces.")   
            row.label(text="> The spread can be limitd by the threshold slider in the panel.")   
            row.label(text="> When finished: a choosen mesh selection mode will be enabled.")   
 
            box.separator()       



        # TOOLS #
        if self.prefs_tabs == 'tools':
            
            box = layout.box().column(align=True)
            box.separator() 
 
            row = box.column(align=False)
            row.label(text="Settings are available in the panel")   

            box.separator() 

            row = box.column(align=True)
            row.prop(self, "threshold", text="Threshold select linked face")           
            box.separator() 

            row = box.column(align=True)
            row.prop(self, "mesh_select_mode", text ='Mode')           
         
            box.separator() 



        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(align=True)
             
            row = box.row(align=True) 
            row.label("Panel Location:")
         
            box.separator()             
         
            row = box.row(align=True)
            row.prop(self, 'tab_snapflat_location', expand=True)
          
            box.separator() 
        
            row = box.row(align=True)            
            if self.tab_snapflat_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "category")

            box.separator() 
            box.separator() 

            box.separator() 

            row = box.column(align=True)
            row.prop(self, "show_snapflat_buttons")           
         
            box.separator() 
    
    
    
        # APPEND #
        if self.prefs_tabs == 'menus':

            col = layout.column(align=True)   

            box = col.box().column(align=True)

            box.separator()
            
            row = box.row(align=True)  
            row.label(text="Cascade Menu:", icon ="COLLAPSEMENU")        

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snapflat_menu', expand=True)
         
            if self.tab_snapflat_menu == 'pie': 
               
                box.separator()   
              
                row = box.column(align=True)                                                  
                row.label(text="> This menu is always a proposal.")
                row.label(text="> Left or right, up or down, there are too many preferences,")
                row.label(text="> to create a pie menu for everyone.")
                row.label(text="> But it would be handy if you work with a bigger screen.")


            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'use_hotkey')
            row.prop(self, 'use_event')
            row.prop(self, 'use_ctrl')
            row.prop(self, 'use_alt')
            row.prop(self, 'use_shift')
 
            box.separator()
            box.separator()

            #-----------------------------------------------------

            box = col.box().column(align=True)
         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="Add Menu to Special Menu [W]", icon ="COLLAPSEMENU")         

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snapflat_special', expand=True)

            if self.tab_snapflat_special == 'remove':
                pass
            else:

                box.separator() 

                row = box.column(align=True)  
                row.prop(self, 'toggle_special_snapflat_separator')
                row.prop(self, 'toggle_special_snapflat_icon')


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
            row.label(text="1 > change search to key-bindig and insert the hotkey: shift 2", icon ="BLANK1")
            row.label(text="2 > go to 3D View > Call Menu [SHIFT+2]: VIEW3D_TP_SnapFlat_Menu /_Pie!", icon ="BLANK1")
            row.label(text="3 > choose a new key configuration and save preferences !", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)             
            row.label(text="Or edit the keymap script directly:", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)  
            row.label(text="", icon ="BLANK1")
            row.operator("tpc_ops.keymap_snapflat", text = 'Open KeyMap in Text Editor')
            row.operator('wm.url_open', text = 'Type of Events').url = "https://github.com/mkbreuer/Misc-Share-Archiv/blob/master/images/SHORTCUTS_Type%20of%20key%20event.png?raw=true"
            
            box.separator()



# REGISTER #
classes = (
    VIEW3D_OT_KeyMap_SnapFlat,
    VIEW3D_OT_SnapFlat_Modal,
    VIEW3D_MT_SnapFlat_Menu_Special,
    Addon_Preferences_SnapFlat,
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
    update_snapflat_menu(None, bpy.context)
    update_snapflat_special(None, bpy.context)



def unregister():
    try:
        for cls in classes:
            bpy.utils.unregister_class(cls)
    except:
        traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))

if __name__ == "__main__":
    register()



