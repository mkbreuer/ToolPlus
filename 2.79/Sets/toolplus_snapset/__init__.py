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
    "name": "SnapSet",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 1),
    "blender": (2, 7, 7),
    "location": "3D View",
    "description": "snap set presets for 3d view",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus/wiki/TP-Header",
    "category": "ToolPlus",
}

# LOAD MANUAL #
from toolplus_snapset.snapset_manual   import (VIEW3D_TP_SnapSet_Manual)


# LOAD CUSTOM ICONS #
from . icons.icons    import load_icons
from . icons.icons    import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_snapset'))

if "bpy" in locals():
    import imp
                                                                      
    imp.reload(snapset_draw)                                                                  
    imp.reload(snapset_ops)                                                                                                                                   
    imp.reload(snapset_targets)                                                                  
    imp.reload(snapset_widget)                                                                  

else:
       
    from . import snapset_draw 
    from . import snapset_ops  
    from . import snapset_targets 
    from . import snapset_widget 
    
    from . snapset_keymap  import*



# LOAD MODULS #
import bpy
from bpy import *
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UPDATE TOOLS #
def update_snapset_tools(self, context):

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

    # INFO LIST #
    prefs_tabs = EnumProperty(
        items=(('info',     "Info",     "Info"),
               ('menus',    "KeyMap",   "KeyMap"),
               ('panel',    "Panel",    "Panel"),
               ('draw',     "Draw",     "Draw"),
               ('url',      "URLs",     "URLs")),
               default='info')


    #------------------------------


    # PANEL #          
    tab_snapset_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf',      'place panel in the tool shelf [T]'),
               ('ui',    'Property Shelf',  'place panel in the property shelf [N]'),
               ('off',   'Remove Panel',    'remove the panel')),
               default='off', update = update_snapset_panel)

    tools_category_snapset = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Tools', update = update_snapset_panel)

    tab_display_buttons_pl = EnumProperty(
        name = 'Buttons or Menus', 
        description = 'on = only butttons / off = use menus',
        items=(('off', 'Use Menus',   'enable tools in header'), 
               ('on',  'Use Buttons', 'disable tools in header')), 
        default='off', update = update_snapset_tools)

    tab_display_name_pl = EnumProperty(
        name = 'Name & Icon Toggle', 
        description = 'on / off',
        items=(('both_id', 'Show Name & Icon', 'keep names and icons visible in header menus'), 
               ('icon_id', 'Show only Icons',   'disable icons in header menus')), 
        default='both_id', update = update_snapset_tools)


    #------------------------------


    # MENU #
    tab_snapset_menu = EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Use Menu', 'enable menu for 3D View'),
               ('pie',    'Use Pie',  'enable pie for 3D View'),
               ('remove', 'Disable',  'disable menus for 3D View')),
        default='menu', update = update_snapset_menu)


    tab_display_modal = EnumProperty(
        name = 'Draw Modal Text', 
        description = 'on / off',
        items=(('on',  'Enable Viewport Infotext',  'use modal operator with OpenGL drawing'), 
               ('off', 'Remove Viewport Infotext',  'use default operator')), 
        default='off', update = update_snapset_tools)


    tab_display_transform = EnumProperty(
        name = 'Transform Orientation', 
        description = 'on / off',
        items=(('on',  'Enable Transform Orientation',  'add tools to pie'), 
               ('off', 'Remove Transform Orientation',  'remove tools from pie')), 
        default='off', update = update_snapset_tools)


    # SUBMENUS #    
    tab_snapset_special = EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('append',   'Menu Bottom', 'add menus to default special menus'),
               ('prepend',  'Menu Top',    'add menus to default special menus'),
               ('remove',   'Menu Remove', 'remove menus from default menus')),
        default='remove', update = update_snapset_special)               


    #----------------------------


    # HEADER #
    expand_panel_tools = bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)    

    tab_snapset_header = EnumProperty(
        name = 'Header Menu',
        description = 'enable or disable menu for Header',
        items=(('add',    'Menu on',  'enable menu for Header'),
               ('remove', 'Menu off', 'disable menu for Header')),
        default='add', update = update_snapset_header)

    tab_display_buttons = EnumProperty(
        name = 'Buttons or Menus', 
        description = 'on = only butttons / off = use menus',
        items=(('off', 'Use Menus',   'enable tools in header'), 
               ('on',  'Use Buttons', 'disable tools in header')), 
        default='off', update = update_snapset_tools)

    tab_display_name = EnumProperty(
        name = 'Name & Icon Toggle', 
        description = 'on / off',
        items=(('both_id', 'Show Name & Icon', 'keep names and icons visible in header menus'), 
               ('icon_id', 'Show only Icons',   'disable icons in header menus')), 
        default='both_id', update = update_snapset_tools)


    #----------------------------

    # DRAW #
 
    text_color = FloatVectorProperty(name="",  default=(0.5, 1, 1),  min=0, max=1, subtype='COLOR')
 
    text_width = IntProperty(name="Width", default=10, min=20, max=50)
    text_height = IntProperty(name="Height", default=10, min=20, max=100)

    text_pos_x = IntProperty(name="Pos X", subtype='PERCENTAGE', default=15, min=1, max=100)
    text_pos_y = IntProperty(name="Pos Y", subtype='PERCENTAGE', default=0, min=1, max=1000)


    #----------------------------
    
    
    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ SnapSet !")  
            row.label(text="> This addon add snap set presets for 3d view to:")       
            row.label(text="> Menu [ALT+W], Special [W], Panel or Header")                              
            row.label(text="> Optional: use modal operator with infotext for the 3d viewport")                              
            row.separator()             
            row.label(text="> Have Fun! ;)")  


        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Panel Location:")
            
            row = box.row(1)
            row.prop(self, 'tab_snapset_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_snapset_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_snapset")

            box.separator() 
            box.separator() 

            row = box.row()           
            row.label(" ")   
            row.prop(self, 'tab_display_buttons_pl',  expand=True)
       
            box.separator() 

            row = box.row()                  
            row.label(" ")   
            row.prop(self, 'tab_display_name_pl',  expand=True)

            box.separator() 
            box.separator() 
            
            

        # APPEND #
        if self.prefs_tabs == 'menus':

            col = layout.column(1)   

            box = col.box().column(1)
           
            box.separator()            
           
            row = box.row(1)    
            row.label("Append to Header", icon ="COLLAPSEMENU")       
            row.prop(self, 'tab_snapset_header', expand=True)
            
            if self.tab_snapset_header == 'remove':

                box.separator() 

                row = box.row(1)
                row.label(" ")   
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
            box.separator() 

            row = box.row()           
            row.label(" ")   
            row.prop(self, 'tab_display_buttons',  expand=True)
       
            box.separator() 

            row = box.row()                  
            row.label(" ")   
            row.prop(self, 'tab_display_name',  expand=True)

            box.separator() 
            box.separator() 
            
            #-----------------------------------------------------

            box = col.box().column(1)

            box.separator()
            
            row = box.row(1)  
            row.label("Snapset Menu: [ALT+2] ", icon ="COLLAPSEMENU")        
            row.prop(self, 'tab_snapset_menu', expand=True)

            if self.tab_snapset_menu == 'menu':

                box.separator() 

                row = box.row(1)                  
                row.label(" ")   
                row.prop(self, 'tab_display_modal',  expand=True)
                row.label(" ")   


            if self.tab_snapset_menu == 'pie':

                box.separator() 

                row = box.row(1)                  
                row.label(" ")   
                row.label(" ")   
                row.prop(self, 'tab_display_modal',  expand=True)                            
          
                box.separator()                
                
                row = box.row(1)                  
                row.label(" ")   
                row.label(" ")   
                row.prop(self, 'tab_display_transform',  expand=True)
                

            if self.tab_snapset_menu == 'off':
                
                box.separator() 
               
                row = box.row(1) 
                row.label(" ")   
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")
                row.label(" ")   
         
            box.separator()
            box.separator()

            #-----------------------------------------------------

            box = col.box().column(1)
         
            box.separator()
         
            row = box.row(1)  
            row.label("SubMenu to Special [W]", icon ="COLLAPSEMENU")         
            row.prop(self, 'tab_snapset_special', expand=True)

            if self.tab_snapset_special == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(" ")   
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")

            box.separator()
            box.separator()

            #-----------------------------------------------------

            box = col.box().column(1)
           
            box.separator()              

            # TIP #            
            row = box.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

            row = box.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: alt 2", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_SnapSet_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            box.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = box.row(1)             
            row.label(text="Or edit the keymap script directly:", icon ="INFO")
            row.operator("tp_ops.keymap_snapset", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()

            layout.separator()


        # VIEW DRAW #
        if self.prefs_tabs == 'draw':

            col = layout.column(1)  
           
            box = col.box().column(1)

            box.separator()

            row = box.row()
            row.label(text="Text Color:")
            row.prop(self, "text_color")
            
            box.separator()              

            row = box.row()
            row.label(text="Text Size:")
            row.prop(self, "text_width")
            row.prop(self, "text_height")

            box.separator()
            
            row = box.row()
            row.label(text="Text Position:")
            row.prop(self, "text_pos_x")
            row.prop(self, "text_pos_y")
          

            layout.separator()


        # WEB #
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus/wiki/TP-SnapSet"
            row.operator('wm.url_open', text = 'Blenderartist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?401729-Addon-T-SnapSets&p=3067342#post3067342"



    
# REGISTRY #
import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_snapset_menu(None, bpy.context)
    update_snapset_special(None, bpy.context)
    update_snapset_header(None, bpy.context)
    update_snapset_tools(None, bpy.context)
    update_snapset_panel(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_SnapSet_Manual)


def unregister():  

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_SnapSet_Manual)    

if __name__ == "__main__":
    register()
        
        


