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
    "name": "T+ Transform",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 1),
    "blender": (2, 7, 9),
    "location": "3D View, UV Image, Graph & Node Editor",
    "description": "transform tools for 3d view",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_transform.ntransform_manual   import (VIEW3D_TP_Transform_Manual)

# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_transform'))

if "bpy" in locals():
    import imp
    imp.reload(ntransform_action)
    imp.reload(ntransform_pivot)
    imp.reload(ntransform_ops)
    imp.reload(ntransform_snapset)
else:
    from . import ntransform_action         
    from . import ntransform_pivot         
    from . import ntransform_ops         
    from . import ntransform_snapset         
            



# LOAD MODULS #

import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup

# LOAD KEYMAP # 
from toolplus_transform.ntransform_keymap  import*
from toolplus_transform.ntransform_item    import*
from toolplus_transform.ntransform_uimap   import*

import rna_keymap_ui
def get_keymap_item(km, kmi_name, kmi_value):
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_name:
            if km.keymap_items[i].properties.name == kmi_value:
                return km_item
    return None

def draw_keymap_item(km, kmi, kc, layout):
    if kmi:
        layout.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, layout, 0)


# TOOL REGISTRY #
def update_display_tools(self, context):

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return 
    else:        
        if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
            pass
  

# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",     "Info"),
               ('location',   "Panel",    "Location"),
               ('keymap',     "Menu",     "Keymap"),   
               ('url',        "URLs",     "URLs")),
               default='info')

    #----------------------------

    # LOCATIONS #          
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=[('tools', 'Tool Shelf [T]', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf [N]', 'place panel in the property shelf [N]'),
               ('off', 'Panel off', 'disable the panel')],
               default='tools', update = update_panel_ntransform)

    tools_category = StringProperty(name = "TAB", description = "add name for a new category tab", default = 'T+', update = update_panel_ntransform)
  
    tab_pivot = bpy.props.BoolProperty(name="Pivot", description="on/off", default=True)  
    tab_normal = bpy.props.BoolProperty(name="N-Transform ", description="on/off", default=True)  
    tab_normal_menu = bpy.props.BoolProperty(name="N-Transform", description="on/off", default=True)  
    tab_use_menu = bpy.props.BoolProperty(name="Menus", description="on/off", default=True)  
    tab_align = bpy.props.BoolProperty(name="AlignTo", description="on/off", default=True)  
    tab_snapset = bpy.props.BoolProperty(name="SnapSet", description="on/off", default=True)  
    tab_transform = bpy.props.BoolProperty(name="Transform", description="on/off", default=True)  
    tab_transform_n = bpy.props.BoolProperty(name="AlignTo", description="on/off", default=True)  

    #----------------------------

    # ALIGNTO #
    types_align_to = [("location"  ,"Align Location"  ,"" ,0),
                      ("rotation"  ,"Align Rotation"  ,"" ,1), 
                      ("scale"     ,"Align Scale"     ,"" ,2)]         

    tn_align_to = bpy.props.EnumProperty(name = "Align To", default = "location", items = types_align_to)

    #----------------------------

      
    # MODIFIER PROPERTIES #      
    tab_submenu_ntransform = EnumProperty(
        name = 'Panel Location',
        description = 'tool switch',
        items=(('insert', 'Append', 'append functions to transform panel'),
               ('remove', 'Remove', 'remove functions from transform panel')),
               default='remove', update = update_submenu_ntransform)

    #----------------------------

    # 3D VIEW MENU # 
    tab_menu_ntransform = EnumProperty(
        name = '3d View Menu',
        description = 'location switch',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'disable menu for 3d view')),
               default='off', update = update_menu_ntransform)

    #----------------------------
    
    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(align=True)
            
            row = box.column(align=True)   
            row.label(text="Welcome to T+ Transform!")  
            row.label(text="This addon comes with advanced transform tools in an adaptable panel and menu.")
          
            row.separator()    

            row.label(text="Transform: normal orientation move for objects and mesh. Fast way to create hotkey.")
            row.label(text="Align: match location, rotation & scale or in edit: align vertices, handles, points...")
            row.label(text="SnapSet: apply pivot and orientation preset for fast align")
            row.label(text="Append: add tools to transform panel in tab: tools")
            row.label(text="Menu: [CTRL+SHIFT+X] > to align in 3D View, UV Image, Graph & Node Editor")
           
            row.separator()        
                        
            row.label(text="Have Fun! :)")         


        # LOCATION #
        if self.prefs_tabs == 'location':
            
            ### 
            box = layout.box().column(align=True)
             
            box.separator() 

            row = box.row(align=True) 
            row.label("Location: Panel")
            
            row = box.row(align=True)
            row.prop(self, 'tab_location', expand=True)

            box.separator()

            row = box.row(align=True)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            box.separator()  
            box.separator()             
           
            row = box.row(align=True)             
            row.prop(self, 'tab_pivot')
            row.prop(self, 'tab_transform')

            row = box.row(align=True)       
            row.prop(self, 'tab_align')

            row = box.row(align=True)   
            row.prop(self, 'tab_normal')           
            if panel_prefs.tab_normal == True:            
                row.prop(self, 'tab_use_menu')

            box.separator()   
  
        
            box = layout.box().column(align=True)             
          
            box.separator() 
           
            row = box.row(align=True) 
            row.label("Append to Transform Panel")
            
            row = box.row(align=True)
            row.prop(self, 'tab_submenu_ntransform', expand=True)

            box.separator()





        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(align=True)

            box.separator() 
             
            row = box.row(align=True)  
            row.label("Menu", icon ="COLLAPSEMENU") 
         
            row = box.row(align=True)           
            row.prop(self, 'tab_menu_ntransform', expand=True) 
            row.prop(self, 'tab_normal_menu')   

            box.separator() 
            box.separator() 

            row = box.row(align=True) 

            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            km = kc.keymaps['3D View']
            kmi = get_keymap_item(km, 'wm.call_menu', "VIEW3D_TP_Transform_Menu")
            draw_keymap_item(km, kmi, kc, row) 
           
            box.separator() 
            box.separator() 


            # TIP #        
            row = layout.row(align=True)             
            row.label(text="! For key change you can also go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(align=True) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. menu: ctrl shift x", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Transform_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            box.separator()  

            row = layout.row(align=True)             
            row.label(text="! Or change the key in the keymap!", icon ="INFO")
            row.operator("tp_ops.keymap_ntransform", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"            

            box.separator() 
            
            row = layout.row(align=True)               
            row.label(text="! Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="INFO")
        
            box.separator()  
            

        # WEB #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(align=True)
            
            row = box.row()
            row.operator('wm.url_open', text = 'GitHub', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus/wiki"




# PROPERTY GROUP #
class Dropdown_TP_Transform_Props(bpy.types.PropertyGroup):

    display_settings = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

          



# REGISTRY #
import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_collapse_ntransform = bpy.props.PointerProperty(type = Dropdown_TP_Transform_Props)
       
    update_menu_ntransform(None, bpy.context)
    update_panel_ntransform(None, bpy.context)
    update_submenu_ntransform(None, bpy.context)
   

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Transform_Manual)

def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    del bpy.types.WindowManager.tp_collapse_ntransform

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Transform_Manual)
    
if __name__ == "__main__":
    register()
        
        




              

