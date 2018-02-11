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
"name": "ReCoPlanar", 
"author": "marvink.k.breuer (MKB)",
"version": (1, 1),
"blender": (2, 7, 9),
"location": "View3D > Panel: Recenter",
"description": "center and reposition an selected object",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "ToolPlus"
}


# LOAD MANUAL #
from toolplus_recoplanar.re_manual  import (VIEW3D_TP_ReCoPlanar_Manual)

# LOAD UI #
from toolplus_recoplanar.re_panel    import (VIEW3D_TP_ReCoPlanar_TOOLS)
from toolplus_recoplanar.re_panel    import (VIEW3D_TP_ReCoPlanar_UI)

# LOAD MENU #
from toolplus_recoplanar.re_menu  import (VIEW3D_TP_ReCoPlanar_Menu)

# LOAD ICONS #
from . icons.icons              import load_icons
from . icons.icons              import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_recoplanar'))
   
if "bpy" in locals():
    import imp

    imp.reload(re_action)    
    imp.reload(re_copy)    
    imp.reload(re_coplanar)    
    imp.reload(re_local)    
else:                                                                              
    from . import re_action                                                                                                                       
    from . import re_copy                                                                                                                       
    from . import re_coplanar                                                                                                                       
    from . import re_local                                                                                                                       
                               

# LOAD MODULS #   
import bpy
from bpy import*
from bpy.props import* 
from toolplus_recoplanar.re_keymap  import*
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
def update_panel_location(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_ReCoPlanar_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_ReCoPlanar_TOOLS)   
    except:
        pass    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_ReCoPlanar_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_ReCoPlanar_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category        
        bpy.utils.register_class(VIEW3D_TP_ReCoPlanar_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_ReCoPlanar_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass


# TOOLS REGISTRY  # 
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None  


# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('url',        "URLs",       "URLs")),
               default='info')


    # TAB LOACATION #           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location)
               

    # MENU # 
    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu)

    # PANEL #
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)

    tab_display_recoplanar_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ReCoplanar on', 'enable tools default special menu > [W]'), ('off', 'ReCoplanar off', 'disable tools in default special menu > [W]')), default='off', update = update_display_tools)


    def draw(self, context):
        layout = self.layout
        

        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="Welcome to T+ ReCoPlanar!")

            row = layout.column()
            row.label(text="This addons allows you to center an selectd object,")
            row.label(text="and place it back to the previous location with previous rotation as well.")
            row.label(text="You can locate the panel in toolshelf [T] or property shelf [N].")
            row.label(text="Or use only the Operators in the default Special Menu [W]")
            row.label(text="Have Fun! ;)")


        # LOACATION #
        if self.prefs_tabs == 'location':
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location: Panel ")
            
            row= box.row(1)
            row.prop(self, 'tab_location', expand=True)

            box.separator()
                                               
            if self.tab_location == 'tools':
                
                row = box.row(1)                                                
                row.prop(self, "tools_category")
         
            box.separator()


        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu [CTRL+SHIFT+X]", icon ="COLLAPSEMENU") 

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)

            if self.tab_menu_view == 'off':
                row = box.row(1) 
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")
                
            box.separator()                      
            box.separator()                      

            row = box.row()        
            row.label(text="Add Tools to Special Menu [W]", icon ="INFO")        
           
            row = box.row(1)
            row.prop(self, 'tab_display_recoplanar_menu', expand=True)    

          
            # TIP #
            box.separator()
            
            row = layout.row(1)             
            row.label(text="! For default key change > go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey: ctrl shift x", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_ReCoPlanar_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > You can use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = layout.row(1)             
            row.label(text="! Other way to change the default key is to edit the keymap script !", icon ="INFO")
             
            row = layout.row(1) 
            row.operator("tp_ops.keymap_recoplanar", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()  


        # WEB #
        if self.prefs_tabs == 'url':
            row = layout.row()
            row.operator('wm.url_open', text = 'GitHub', icon = 'SCRIPTWIN').url = "https://github.com/mkbreuer/ToolPlus"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?435147-Addon-T-Bounding&p=3221535#post3221535"




# PROPS FOR PANEL #
class Dropdown_ReCoPlanar_Panel_Props(bpy.types.PropertyGroup):

    display_alter = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    



# ADD TO DEFAULT SPECIAL MENU [W] # 
from .icons.icons import load_icons 
 
class VIEW3D_TP_ReCoplanar_Menu(bpy.types.Menu):
    bl_label = "ReCoplanar"
    bl_idname = "VIEW3D_TP_ReCoplanar_Menu"

    def draw(self, context):
        layout = self.layout
        
        icons = load_icons()

        button_relocal = icons.get("icon_relocal") 
        layout.operator("tp_ops.set_new_local", icon_value=button_relocal.icon_id) 

        button_recenter = icons.get("icon_recenter") 
        layout.operator("tp_ops.recenter", icon_value=button_recenter.icon_id)  

        button_reposition = icons.get("icon_reposition") 
        layout.operator("tp_ops.reposition", icon_value=button_reposition.icon_id)
      
        button_center = icons.get("icon_center") 
        layout.operator("tp_ops.relocate", text="ReLocate", icon_value=button_center.icon_id)

        button_bloc = icons.get("icon_bloc") 
        layout.operator("tp_ops.copy_local_transform", text="ReTransform", icon_value=button_bloc.icon_id ) 


def draw_recoplanar_item(self, context):
    layout = self.layout

    icons = load_icons()
  
    display_recoplanar_menu = context.user_preferences.addons[__package__].preferences.tab_display_recoplanar_menu
    if display_recoplanar_menu == 'on':

        if context.mode == 'OBJECT':
            
            layout.separator()    

            button_relocal = icons.get("icon_relocal") 
            layout.menu("VIEW3D_TP_ReCoplanar_Menu", text="ReCoplanar", icon_value=button_relocal.icon_id)   



# REGISTRY #
import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    # UI # 
    update_panel_location(None, bpy.context)
    update_display_tools(None, bpy.context)

    # PROPS # 
    bpy.types.WindowManager.tp_recoplanar = bpy.props.PointerProperty(type = Dropdown_ReCoPlanar_Panel_Props)   

    # TO SPECIAL MENU #
    bpy.types.VIEW3D_MT_object_specials.append(draw_recoplanar_item) 
   
    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_ReCoPlanar_Manual)

def unregister():

    # PROPS #    
    del bpy.types.WindowManager.tp_recoplanar

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_ReCoPlanar_Manual)

if __name__ == "__main__":
    register()
        
        











