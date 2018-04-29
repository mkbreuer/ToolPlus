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
    "name": "T+ Modifier",
    "author": "marvin.k.breuer (MKB)",
    "version": (1, 5, 1),
    "blender": (2, 7, 9),
    "location": "Editor: 3D View",
    "description": "collection of modifier tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_modifier.mods_manual   import (VIEW3D_TP_Modifier_Manual)

# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_modifier'))

if "bpy" in locals():
    import imp
    imp.reload(mods_action)
    imp.reload(mods_array)
    imp.reload(mods_attributes)
    imp.reload(mods_batch)
    imp.reload(mods_batch_atm)
    imp.reload(mods_bevel)
    imp.reload(mods_cast)
    imp.reload(mods_decimate)
    imp.reload(mods_display)
    imp.reload(mods_easylattice)
    imp.reload(mods_mirror)
    imp.reload(mods_multires)
    imp.reload(mods_normals)
    imp.reload(mods_pivot)
    imp.reload(mods_remesh)
    imp.reload(mods_remove)
    imp.reload(mods_screw)
    imp.reload(mods_sdeform)
    imp.reload(mods_show)
    imp.reload(mods_smooth)
    imp.reload(mods_solidifiy)
    imp.reload(mods_subsurf)
    imp.reload(mods_switch)
    imp.reload(mods_sym)
    imp.reload(mods_symcut)
    imp.reload(mods_toall)
    imp.reload(mods_tools)


else:       
    from .operators import mods_action
    from .operators import mods_array
    from .operators import mods_attributes
    from .operators import mods_batch
    from .operators import mods_batch_atm
    from .operators import mods_bevel
    from .operators import mods_cast
    from .operators import mods_decimate
    from .operators import mods_display
    from .operators import mods_easylattice
    from .operators import mods_mirror
    from .operators import mods_multires
    from .operators import mods_normals
    from .operators import mods_pivot
    from .operators import mods_remesh
    from .operators import mods_remove
    from .operators import mods_screw
    from .operators import mods_sdeform
    from .operators import mods_show
    from .operators import mods_smooth
    from .operators import mods_solidifiy
    from .operators import mods_subsurf
    from .operators import mods_switch
    from .operators import mods_sym
    from .operators import mods_symcut
    from .operators import mods_toall
    from .operators import mods_tools


# LOAD MODULS #

import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup

# LOAD KEYMAP # 
from toolplus_modifier.mods_keymap  import*
from toolplus_modifier.mods_item    import*
from toolplus_modifier.mods_uimap   import*

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
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('toolsets',   "Tools",      "Tools"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('url',        "URLs",       "URLs")),
               default='info')

    #----------------------------

    # LOCATIONS #          
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool [T]', 'place panel in the tool shelf [T]'),
               ('ui', 'Property [N]', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_location)

    tab_location_icons = EnumProperty(
        name = 'Panel Layout',
        description = 'layout switch',
        items=(('cascade', 'Cascade UI', 'layout type'),
               ('icons',   'Icon UI',    'layout type')),
               default='cascade', update = update_panel_location)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)
  
    tab_title = bpy.props.BoolProperty(name="Title", description="on/off", default=True)  
    tab_pivot = bpy.props.BoolProperty(name="Pivot", description="on/off", default=True)  
    tab_history = bpy.props.BoolProperty(name="History", description="on/off", default=True)  

    tab_autosym = bpy.props.BoolProperty(name="AutoSym", description="on/off", default=True)  
    tap_symdim_lr = bpy.props.BoolProperty(name="AutoSym Axis", description="switch direction of the autosym main button > x-plus or x-minus", default=True) 
    tab_mirror_cut = bpy.props.BoolProperty(name="MirrorCut", description="on/off", default=True)  
    tab_mirror = bpy.props.BoolProperty(name="Mirror", description="on/off", default=True)  
    tab_bevel = bpy.props.BoolProperty(name="Bevel", description="on/off", default=True)  
    tab_subsurf = bpy.props.BoolProperty(name="Subsurf", description="on/off", default=True)  
    tab_solidify = bpy.props.BoolProperty(name="Solidify", description="on/off", default=True)  
    tab_simple = bpy.props.BoolProperty(name="SDeform", description="on/off", default=True)  
    tab_array = bpy.props.BoolProperty(name="Array", description="on/off", default=True)  
    tab_screw = bpy.props.BoolProperty(name="Screw", description="on/off", default=True)  
    tab_lattice = bpy.props.BoolProperty(name="Lattice", description="on/off", default=True)   
    tab_multires = bpy.props.BoolProperty(name="MultiRes", description="on/off", default=True)  
    tab_decimate = bpy.props.BoolProperty(name="Decimate", description="on/off", default=True)  
    tab_remesh = bpy.props.BoolProperty(name="Remesh", description="on/off", default=True)  
    tab_smooth = bpy.props.BoolProperty(name="Smooth", description="on/off", default=True)  
    tab_transform = bpy.props.BoolProperty(name="Transform", description="on/off", default=True)  
    tab_shade = bpy.props.BoolProperty(name="Shading", description="on/off", default=True)  
    tab_remove_type = bpy.props.BoolProperty(name="Remove Type", description="on/off", default=True)   
    tab_cast = bpy.props.BoolProperty(name="Cast", description="on/off", default=True)   
    tab_modcopy = bpy.props.BoolProperty(name="Copy", description="on/off", default=True)   

    #----------------------------

    # MODIFIER STACK #   
    tab_location_stack = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool [T]', 'place panel in the tool shelf [T]'),
               ('ui', 'Property [N]', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_stack)

    tools_category_stack = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_stack)

    tab_stack_copy = bpy.props.BoolProperty(name="Copy 2-All", description="on/off", default=False)  
    tab_stack_remove = bpy.props.BoolProperty(name="Remove Type", description="on/off", default=False)  

 
    #----------------------------
      
    # MODIFIER PROPERTIES #      
    tab_submenu_modifier = EnumProperty(
        name = 'Panel Location',
        description = 'tool switch',
        items=(('win', 'Append', 'append menu to properties: modifier'),
               ('off', 'Remove', 'remove menu to properties: modifier')),
               default='win', update = update_submenu_modifier)

    tab_props_copy = bpy.props.BoolProperty(name="Copy 2-All", description="on/off", default=True)  
    tab_props_remove = bpy.props.BoolProperty(name="Remove Type", description="on/off", default=True)  

    #----------------------------

    # 3D VIEW MENU # 
    tab_menu_modifier = EnumProperty(
        name = '3d View Menu',
        description = 'location switch',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'disable menu for 3d view')),
               default='menu', update = update_menu_modifier)

    tab_add_menu = bpy.props.BoolProperty(name="Add", description="on/off", default=True)  
    tab_modifier_menus = bpy.props.BoolProperty(name="Modifier", description="on/off", default=True)  
    tab_modcopy_menu = bpy.props.BoolProperty(name="Copy", description="on/off", default=True)  
    tab_autosym_menu = bpy.props.BoolProperty(name="AutoMirror", description="on/off", default=True)  
    tab_modstack_menu = bpy.props.BoolProperty(name="ModifierStack", description="on/off", default=True)  
    tab_clear_menu = bpy.props.BoolProperty(name="ClearTools", description="on/off", default=True)  
    tab_hover_menu = bpy.props.BoolProperty(name="HoverTools", description="on/off", default=False)  

    #----------------------------
   
    # AUTOSYM # 
    autosym_mirror = bpy.props.BoolProperty(name="Add Mirror Modifier", description="on/off", default=False)  
    autosym_apply = bpy.props.BoolProperty(name="Apply Modifier", description="on/off", default=False)  
    autosym_edit = bpy.props.BoolProperty(name="Stay in Editmode", description="on/off", default=False)   
    autosym_sculpt = bpy.props.BoolProperty(name="Stay in Sculptmode", description="on/off", default=False)  
    autosym_symmetrize = bpy.props.BoolProperty(name="Use Symmetrize", description="on/off", default=False)  

    #----------------------------
    
    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Modifier!")  
            row.label(text="This addon is for editing objects with modifier.")
           
            row.separator()           
           
            row.label(text="The Panels are adaptable and can be placed in the toolshelf [T] or property shelf [N]")
            row.label(text="A included Menu and Tools for Properties: Modifier can also be activated")
           
            row.separator()        
                        
            row.label(text="Have Fun! :)")         



        # LOCATION #
        if self.prefs_tabs == 'location':
            
            ### 
            box = layout.box().column(1)
             
            box.separator() 

            row = box.row(1) 
            row.label("Location 3D View: Main Panel")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)

            row = box.row(1)
            row.prop(self, "tab_location_icons", expand=True)            
            
            box.separator()

            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            box.separator()


            ###            
            box = layout.box().column(1)     

            box.separator() 

            row = box.row(1) 
            row.label("Location 3D View: Modifier Stack:")            
         
            row = box.row(1)             
            row.prop(self, 'tab_location_stack', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location_stack == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_stack")

            box.separator()

          
            ###            
            box = layout.box().column(1)             
          
            box.separator() 
           
            row = box.row(1) 
            row.label("Tools for Properties: Modifier")
            
            row = box.row(1)
            row.prop(self, 'tab_menu_modifier', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for a durably new panel location !", icon ="INFO")

            box.separator() 



        # TOOLS #
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
           
            box.separator()             
          
            row = box.row(1)             
            row.label("Ui: Main Panel")
           
            row = box.column_flow(4)
            row.prop(self, 'tab_title')
            row.prop(self, 'tab_pivot')
            row.prop(self, 'tab_history')
           
           
            row = box.row(1)             
            row.label("Tools: Main Panel")
           
            row = box.column_flow(4)  
            row.prop(self, 'tab_subsurf')
            row.prop(self, 'tab_autosym')
            row.prop(self, 'tap_symdim_lr')
            row.prop(self, 'tab_mirror_cut')
            row.prop(self, 'tab_mirror')
            row.prop(self, 'tab_bevel')
            row.prop(self, 'tab_solidify')
            row.prop(self, 'tab_simple')
            row.prop(self, 'tab_cast')
            row.prop(self, 'tab_screw')
            row.prop(self, 'tab_lattice')
            row.prop(self, 'tab_multires')
            row.prop(self, 'tab_decimate')
            row.prop(self, 'tab_remesh')
            row.prop(self, 'tab_smooth')
            row.prop(self, 'tab_array')
            row.prop(self, 'tab_transform')
            row.prop(self, 'tab_shade')
            row.prop(self, 'tab_remove_type')
            row.prop(self, 'tab_modcopy')


            box.separator() 
            
            row = box.row(1)             
            row.label("Tools: Modifier Stack")
           
            row = box.column_flow(4)
            row.prop(self, 'tab_stack_copy')
            row.prop(self, 'tab_stack_remove')

            box.separator() 
            
            row = box.row(1)             
            row.label("Tools: Modifier Properties")
           
            row = box.column_flow(4)
            row.prop(self, 'tab_props_copy')
            row.prop(self, 'tab_props_remove')

            box.separator() 
            
            row = box.row(1)             
            row.label("Tools: AutoSym")
           
            row = box.column_flow(4)
            row.prop(self, 'autosym_mirror')
            row.prop(self, 'autosym_apply')
            row.prop(self, 'autosym_edit')
            row.prop(self, 'autosym_sculpt')
            row.prop(self, 'autosym_symmetrize')

            box.separator() 

            row = layout.row()
            row.label(text="! save user settings for a durably activation !", icon ="INFO")

            box.separator() 


        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)

            box.separator() 
             
            row = box.row(1)  
            row.label("Modifier Menu", icon ="COLLAPSEMENU") 
         
            row.prop(self, 'tab_menu_modifier', expand=True)
            
            if self.tab_menu_modifier == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next restart durably!", icon ="INFO")

            box.separator() 
            box.separator() 

            row = box.row(1) 

            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            km = kc.keymaps['3D View']
            kmi = get_keymap_item(km, 'wm.call_menu', "VIEW3D_TP_Modifier_Menu")
            draw_keymap_item(km, kmi, kc, row) 
           
            box.separator() 
            box.separator() 

            box.separator() 

            row = box.column(1)             
            row.label("How to use the Menu in Editmode:", icon = "INFO")
            row.label("> go to TAB: Input > 3D View > Mesh and disable: Vertex Slide!") 
            row.label("> Pressing Transform Grab twice do the same job! > (2xG)") 

            box.separator() 
            box.separator() 

            row = box.row(1)             
            row.label("Tools: Menu")
           
            row = box.column_flow(2)
            row.prop(self, 'tab_add_menu')
            row.prop(self, 'tab_modifier_menus')
            row.prop(self, 'tab_modcopy_menu')
            row.prop(self, 'tab_autosym_menu')
            row.prop(self, 'tab_modstack_menu')
            row.prop(self, 'tab_clear_menu')
            row.prop(self, 'tab_hover_menu')

            box.separator()
            
            row = box.row(1)
            row.label(text="! save user settings for a durably activation !", icon ="INFO")


            # TIP #        
            row = layout.row(1)             
            row.label(text="! For key change you can also go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: shift v", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Modifier_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            box.separator()  

            row = layout.row(1)             
            row.label(text="! Or change the key in the keymap!", icon ="INFO")
            row.operator("tp_ops.keymap_modifier", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"            

            box.separator() 
            
            row = layout.row(1)               
            row.label(text="! Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="INFO")
        
            box.separator()  
            

        # WEB #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.row()
            row.label("List of Addon on Wiki Page")
            row.operator('wm.url_open', text = 'Modifier Tools', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/modifier_tools"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?411265-Addon-T-Modifier&p=3124733#post3124733"




# PROPERTY GROUP: MODIFIER #
class Dropdown_TP_Modifier_Props(bpy.types.PropertyGroup):

    display_display = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    

    display_subsurf = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_symdim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)      
    display_mirror = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_bevel = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_solidify = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_sdeform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_array = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_cast = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True) 
    display_lattice = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True) 
    display_vertgrp = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False) 
    display_addmods = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_modifier = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)   
    display_screw = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_multires = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_decimate = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_remesh = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_smooth = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_options = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_options_panel = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_options_stack = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_options_submenu = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_options_menu = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_displace = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  
    display_displace_opt = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_copy = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)  


# REGISTRY #
import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_collapse_menu_modifier = bpy.props.PointerProperty(type = Dropdown_TP_Modifier_Props)
       
    update_menu_modifier(None, bpy.context)
    update_panel_location(None, bpy.context)
    update_submenu_modifier(None, bpy.context)
    update_panel_location_stack(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Modifier_Manual)

def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    del bpy.types.WindowManager.tp_collapse_menu_modifier

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Modifier_Manual)
    
if __name__ == "__main__":
    register()
        
        




              

