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
    "name": "T+ Menu Switch",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "Editor: 3D Viewport > Menu / Batch / Pie",
    "description": "Addon Template for different kinds of customizeable 3d viewport menus",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# Import UI #----------------------------------------------------------------------------------------

from toolplus_menus.toolplus_menu           import (VIEW3D_ToolPus_Menu)
from toolplus_menus.toolplus_batch          import (VIEW3D_ToolPus_Batch)
from toolplus_menus.toolplus_pie            import (VIEW3D_ToolPus_Pie)

from . icons.icons                          import load_icons
from . icons.icons                          import clear_icons


# Import Operators #----------------------------------------------------------------------------------------

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_menus'))

if "bpy" in locals():
    import imp

    imp.reload(toolplus_batch)
    imp.reload(toolplus_zero)

else:
         
    from . import toolplus_batch                
    from . import toolplus_zero                   
      

# Import Moduls #----------------------------------------------------------------------------------------

import bpy
from bpy import *
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



# Menu Tools #----------------------------------------------------------------------------------------
def update_tool_display(self, context):

    # Tools on #

    #Menu
    if context.user_preferences.addons[__name__].preferences.tab_menu_tools == 'on':
        return

    #Batch
    elif context.user_preferences.addons[__name__].preferences.tab_batch_tools == 'on':
        return

    #Pie
    elif context.user_preferences.addons[__name__].preferences.tab_pie_tools == 'on':
        return


    # Tools off #

    #Menu 
    if context.user_preferences.addons[__name__].preferences.tab_menu_tools == 'off':
        return

    #Batch 
    elif context.user_preferences.addons[__name__].preferences.tab_batch_tools == 'off':
        pass

    #Pie
    elif context.user_preferences.addons[__name__].preferences.tab_pie_tools == 'off':
        pass



# Keymapping #----------------------------------------------------------------------------------------
addon_keymaps_menu = []

def update_menu_display(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_ToolPus_Menu)
                
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_display_menu == 'menu':
     
        VIEW3D_ToolPus_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_ToolPus_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'ONE', 'PRESS', alt=True)
        kmi.properties.name = "tp_menu.tp_menu"


    if context.user_preferences.addons[__name__].preferences.tab_display_menu == 'off':
        pass



def update_batch_display(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_ToolPus_Batch)
        
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_display_batch == 'menu':
     
        VIEW3D_ToolPus_Batch.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_ToolPus_Batch)
    
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('tp_menu.tp_batch', 'TWO', 'PRESS', alt=True) 
        #kmi.properties.name = ''

    if context.user_preferences.addons[__name__].preferences.tab_display_batch == 'off':
        pass



def update_pie_display(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_ToolPus_Pie)
        
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_display_pie == 'menu':
     
        VIEW3D_ToolPus_Pie.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_ToolPus_Pie)
    
        # Keymapping 
        wm = bpy.context.window_manager       
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu_pie', 'THREE', 'PRESS', alt=True) 
        kmi.properties.name = "tp_menu.tp_pie"


    if context.user_preferences.addons[__name__].preferences.tab_display_pie == 'off':
        pass




# Addon Preferences #----------------------------------------------------------------------------------------
class TP_Addon_Preferences(AddonPreferences):
    bl_idname = __name__
    

    #Tab Prop
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('keymap',     "Keymap",     "Keymap"),  
               ('url',        "URLs",       "URLs")),
               default='info')

    #----------------------------------------------------------------------------------------

    #Menu
    tab_display_menu = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_display)

    #Batch
    tab_display_batch = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_batch_display)
    
    #Pie
    tab_display_pie = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_pie_display)
               

    #----------------------------------------------------------------------------------------


    #Menu  
    tab_menu_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'zero on', 'enable tools in panel'), ('off', 'zero off', 'disable tools in panel')), default='on', update = update_tool_display)

    #Batch 
    tab_batch_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'zero on', 'enable tools in panel'), ('off', 'zero off', 'disable tools in panel')), default='on', update = update_tool_display)

    #Pie
    tab_pie_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'zero on', 'enable tools in panel'), ('off', 'zero off', 'disable tools in panel')), default='on', update = update_tool_display)


    #----------------------------------------------------------------------------------------


    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Menu", description = "enable or disable menu", default=True, update = update_menu_display)
    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Batch", description = "enable or disable menu", default=True, update = update_batch_display)
    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Pie", description = "enable or disable menu", default=True, update = update_pie_display)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome Dear Experimental User!")    
            row.label(text="You can add 3 different kind of menus:")   
            row.label(text="> Default Menu ")   
            row.label(text="> Batch Menu")   
            row.label(text="> Pie Menu")
            
            row.separator()            
                        
            row.label(text="Have Fun! :)")
               


        #Tools
        if self.prefs_tabs == 'toolsets':

            
            #Menu
            box = layout.box().column(1)
            
            row = box.row()
            row.label("Menu: [ALT+ONE]")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_batch_tools', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 
                        
           
            #Batch    
            box = layout.box().column(1)
            
            row = box.row()
            row.label("Batch: [ALT+TWO]")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_batch_tools', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 
            
            
            #Pie
            box = layout.box().column(1)
            
            row = box.row()
            row.label("Pie: [ALT+THREE]")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_pie_tools', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 

 
       #Keymap
        if self.prefs_tabs == 'keymap':



            #Menu
            box = layout.box().column(1)
             
            row = box.column(1)          
            row.label("Menu: '[ALT+ONE]", icon ="COLLAPSEMENU")

            row = box.row(1)          
            row.prop(self, 'tab_display_menu', expand=True)
            
            if self.tab_display_menu == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")



            #Batch
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Batch: [ALT+TWO]", icon ="COLLAPSEMENU")   

            row = box.row(1)          
            row.prop(self, 'tab_display_batch', expand=True)

            if self.tab_display_batch == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")


            #Pie
            box = layout.box().column(1)
             
            row = box.column(1)           
            row.label("Pie: [ALT+THREE]", icon ="COLLAPSEMENU")  

            row = box.row(1)          
            row.prop(self, 'tab_display_pie', expand=True)

            if self.tab_display_pie == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

           
            #Tip
            box.separator()  
            
            row = layout.column(1) 
            row.label(text="! for key change go to > User Preferences > TAB: Input !", icon ="INFO")
            row.operator('wm.url_open', text = '!Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"




        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'GitHub', icon = 'INFO').url = "https://github.com/mkbreuer"






# Registry #----------------------------------------------------------------------------------------s

import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_menu_display(None, bpy.context)
    update_batch_display(None, bpy.context)
    update_pie_display(None, bpy.context)

def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    

if __name__ == "__main__":
    register()
        
        







