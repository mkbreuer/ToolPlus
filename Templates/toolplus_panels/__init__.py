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
    "name": "T+ Panel Switch",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "Editor 3D View / Editor: Properties",
    "description": "Addon Template for a customizeable panels",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #
from toolplus_panels.toolplus_panels          import (VIEW3D_TP_Template_Panel_TOOLS)
from toolplus_panels.toolplus_panels          import (VIEW3D_TP_Template_Panel_UI)
from toolplus_panels.toolplus_panels          import (VIEW3D_TP_Template_Panel_PROPS)


# LOAD ICONS #
from . icons.icons                        import load_icons
from . icons.icons                        import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_panels'))

if "bpy" in locals():
    import imp

    imp.reload(toolplus_operator)

else:   
    from . import toolplus_operator           
        


# LOAD MODULS #
import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



# PANEL REGISTRY #
panels = (VIEW3D_TP_Template_Panel_TOOLS, VIEW3D_TP_Template_Panel_UI, VIEW3D_TP_Template_Panel_PROPS, menu_func)
def update_panel(self, context):
    message = "Template: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':            
            #CATEGORY CHANGE
            VIEW3D_TP_Template_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_tab            
            bpy.utils.register_class(VIEW3D_TP_Template_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Template_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'props':
            bpy.utils.register_class(VIEW3D_TP_Template_Panel_PROPS)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'win':
            bpy.types.DATA_PT_modifiers.prepend(menu_func)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
            pass

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



# TOOLS REGISTRY #
def update_panel_tools(self, context):

    # TOOLS ON

    if context.user_preferences.addons[__name__].preferences.tab_panel_custom_a == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_panel_custom_b == 'on':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_panel_history == 'on':
        return


    # TOOLS OFF 
    
    if context.user_preferences.addons[__name__].preferences.tab_panel_custom_a == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_panel_custom_b == 'off':
        return

    elif context.user_preferences.addons[__name__].preferences.tab_panel_history == 'off':
        return




# ADDON PREFERENCES #

class TP_Addon_Preferences(AddonPreferences):
    bl_idname = __name__
    
    # THEME TABS
    prefs_tabs = bpy.props.EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('url',        "URLs",       "URLs")),
         default='info')


    # PANEL LOCATION                    
    tab_location = bpy.props.EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('props', 'Properties Object', 'place panel in the object properties tab'),
               ('win', 'Property Modifier', 'place operators in the modifier properties tab'),
               ('off', 'Off', 'hide panel')),
               default='tools', update = update_panel_location)


    # TOOLS PROPS
    tab_panel_custom_a = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Custom A on', 'enable tools in panel'), ('off', 'Custom A off', 'disable tools in panel')), default='on', update = update_panel_tools)

    tab_panel_custom_b = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Custom B on', 'enable tools in panel'), ('off', 'Custom B off', 'disable tools in panel')), default='on', update = update_panel_tools)

    tab_panel_history = bpy.props.EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_panel_tools)



    # NEW LOCATION BY NAME
    tools_category_tab = bpy.props.StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)


    # LAYOUT
    def draw(self, context):
        layout = self.layout        
        
        # INFO
        row= layout.row(1)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome Dear Experimental User!")    
            row.label(text="You can add the panel to:")   
            row.label(text="> Tools Shelf [T] ")   
            row.label(text="> Property Shelf [N]")   
            row.label(text="> Properties: Object or Modifier")   

            row.separator()            
                        
            row.label(text="Have Fun! :)")
            

        # LOCATION
        if self.prefs_tabs == 'location':
            box = layout.box().column(1) 
            
            row = box.row(1) 
            row.label("Panel Location: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location', expand=True)
            
            if self.tab_location == 'tools':

                box.separator()

                row = box.row(1) 
                row.prop(self, "tools_category_tab")

            box.separator()  

            
            # TIP
            box.separator()  
            
            row = layout.column(1) 
            row.operator('wm.url_open', text = '!Tip: Tune Up!', icon = 'PLUGIN').url = "https://sites.google.com/site/aleonserra/home/scripts/tuneup"



        # TOOLS
        if self.prefs_tabs == 'toolsets':

            box = layout.box().column(1)

            row = box.row()
            row.label("Panel")            
            
            row = box.column_flow(3)
            row.prop(self, 'tab_panel_custom_a', expand=True)
            row.prop(self, 'tab_panel_custom_b', expand=True)
            row.prop(self, 'tab_panel_history', expand=True)
        
            box.separator()


            # TIP
            box.separator()  
            
            row = layout.column(1) 
            row.label(text="! key change: go to > User Preferences > TAB: Input !", icon ="INFO")
            row.operator('wm.url_open', text = '!Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"


        # WEBLINKS
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'GitHub', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus-Templates"





#PROPERTY GROUP 
class Dropdown_TP_Template_Props(bpy.types.PropertyGroup):

    display_collapse = bpy.props.BoolProperty(name = "collapse", description = "open/close", default = False) 



# MODIFIER PROPERTIES #  
def menu_func(self, context):
    layout = self.layout
    
    icons = load_icons()
    
    obj = context.active_object
    if obj:                       
        mod_list = obj.modifiers
        if mod_list:
                                           
            row = layout.row(1)  

            button_custom_a = icons.get("icon_custom_a")
            row.label(text="Custom Tools", icon_value=button_custom_a.icon_id)                             

            button_custom_b = icons.get("icon_custom_b")
            row.label(text="Custom Tools", icon_value=button_custom_b.icon_id)  

        else:
            box = layout.box().column(1)    
 
            row = box.row(1)                    
           
            box.label('No Modifier active' , icon ="ERROR")
            
            box.separator()



# REGISTRY #
import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_location(None, bpy.context)
    update_panel_tools(None, bpy.context)

    bpy.types.WindowManager.tp_collapse_template = bpy.props.PointerProperty(type = Dropdown_TP_Template_Props)



def unregister():
    try:
        del bpy.types.WindowManager.tp_collapse_template
    except:
        pass

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    

if __name__ == "__main__":
    register()
        
        







