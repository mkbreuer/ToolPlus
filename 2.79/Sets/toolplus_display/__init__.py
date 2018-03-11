# ##### BEGIN GPL LICENSE BLOCK #####
#
#Copyright (C) 2017  Marvin.K.Breuer (MKB)]
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
    "name": "Display",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 1, 2),
    "blender": (2, 7, 9),
    "location": "VIEW 3D",
    "description": "alternate and advanced display tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #

from toolplus_display.display_ui_menu       import (VIEW3D_TP_Display_OSD_MENU)
from toolplus_display.display_ui_menu       import (VIEW3D_TP_Selection_Menu)
from toolplus_display.display_ui_menu       import (VIEW3D_TP_Selection_Menu_Main)
from toolplus_display.display_ui_menu       import (VIEW3D_TP_MultiMode)

from toolplus_display.display_ui_compact    import (VIEW3D_TP_Display_Compact_Panel_TOOLS)
from toolplus_display.display_ui_compact    import (VIEW3D_TP_Display_Compact_Panel_UI)

from toolplus_display.display_ui_delete     import (VIEW3D_TP_Delete_Panel_TOOLS)
from toolplus_display.display_ui_delete     import (VIEW3D_TP_Delete_Panel_UI)

from toolplus_display.display_ui_display    import (VIEW3D_TP_Display_Panel_TOOLS)
from toolplus_display.display_ui_display    import (VIEW3D_TP_Display_Panel_UI)

from toolplus_display.display_ui_modifier   import (VIEW3D_TP_Modifier_Panel_TOOLS)
from toolplus_display.display_ui_modifier   import (VIEW3D_TP_Modifier_Panel_UI)

from toolplus_display.display_ui_normals    import (VIEW3D_TP_Normals_Panel_TOOLS)
from toolplus_display.display_ui_normals    import (VIEW3D_TP_Normals_Panel_UI)

from toolplus_display.display_ui_screen     import (VIEW3D_TP_Screen_Panel_TOOLS)
from toolplus_display.display_ui_screen     import (VIEW3D_TP_Screen_Panel_UI)

from toolplus_display.display_ui_shade      import (VIEW3D_TP_Shade_Panel_TOOLS)
from toolplus_display.display_ui_shade      import (VIEW3D_TP_Shade_Panel_UI)

from toolplus_display.display_ui_sharpen    import (VIEW3D_TP_Sharpen_Panel_TOOLS)
from toolplus_display.display_ui_sharpen    import (VIEW3D_TP_Sharpen_Panel_UI)

from toolplus_display.display_ui_smooth     import (VIEW3D_TP_Smooth_Panel_TOOLS)
from toolplus_display.display_ui_smooth     import (VIEW3D_TP_Smooth_Panel_UI)

from toolplus_display.display_ui_uvs        import (VIEW3D_TP_UVS_Panel_TOOLS)
from toolplus_display.display_ui_uvs        import (VIEW3D_TP_UVS_Panel_UI)

from toolplus_display.display_ui_select     import (VIEW3D_TP_Select_Panel_TOOLS)
from toolplus_display.display_ui_select     import (VIEW3D_TP_Select_Panel_UI)




# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons

# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_display'))

if "bpy" in locals():
    import imp

    imp.reload(autowire)
    imp.reload(delete)     
    imp.reload(display)
    imp.reload(fastnavi)
    imp.reload(navigation)
    imp.reload(material)
    imp.reload(matswitch)
    imp.reload(normals)
    imp.reload(normals_transfer)
    imp.reload(normals_weighted)
    imp.reload(opengl)
    imp.reload(orphan) 
    imp.reload(pivot)
    imp.reload(restrictor)
    imp.reload(selection)
    imp.reload(silhouette)
    imp.reload(snapset)

    imp.reload(select_action)
    imp.reload(select_ktools)
    imp.reload(select_meshlint)
    imp.reload(select_meshorder)
    imp.reload(select_sorting)
    imp.reload(select_topokit2)
    imp.reload(select_vismaya)

    imp.reload(uv_equalize)
    imp.reload(uv_hardedges)
    imp.reload(uv_tube)

    imp.reload(sym_cut)
    imp.reload(sym_dim)
    imp.reload(sym_mods)

    imp.reload(mods_display)
    imp.reload(mods_remove)
    imp.reload(mods_toall)
    imp.reload(mods_tools)

    imp.reload(cpuv_menu)
    imp.reload(cpuv_common)
    imp.reload(cpuv_properties)
    imp.reload(cpuv_default_operation)
    imp.reload(cpuv_selseq_operation)
    imp.reload(cpuv_uvmap_operation)
    imp.reload(cpuv_fliprot_operation)
    imp.reload(cpuv_transfer_uv_operation)

else:
    
    from .ops_visuals import autowire
    from .ops_visuals import delete   
    from .ops_visuals import display
    from .ops_visuals import fastnavi
    from .ops_visuals import navigation
    from .ops_visuals import material
    from .ops_visuals import matswitch
    from .ops_visuals import normals
    from .ops_visuals import normals_transfer
    from .ops_visuals import normals_weighted
    from .ops_visuals import opengl    
    from .ops_visuals import orphan  
    from .ops_visuals import pivot                          
    from .ops_visuals import restrictor                          
    from .ops_visuals import selection                          
    from .ops_visuals import silhouette                          
    from .ops_visuals import snapset                          

    from .ops_select import select_action                 
    from .ops_select import select_ktools         
    from .ops_select import select_meshlint         
    from .ops_select import select_meshorder            
    from .ops_select import select_sorting                            
    from .ops_select import select_topokit2                
    from .ops_select import select_vismaya  

    from .ops_uv import uv_equalize               
    from .ops_uv import uv_hardedges               
    from .ops_uv import uv_tube                           

    from .ops_sym import sym_cut                                          
    from .ops_sym import sym_dim                            
    from .ops_sym import sym_mods      

    from .ops_mods import mods_display                                          
    from .ops_mods import mods_remove                              
    from .ops_mods import mods_toall    
    from .ops_mods import mods_tools    

    from .uv_magic import cpuv_menu
    from .uv_magic import cpuv_common
    from .uv_magic import cpuv_properties
    from .uv_magic import cpuv_default_operation
    from .uv_magic import cpuv_selseq_operation
    from .uv_magic import cpuv_uvmap_operation
    from .uv_magic import cpuv_fliprot_operation
    from .uv_magic import cpuv_transfer_uv_operation


# LOAD MODULS #

import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



# UI REGISTRY #

panels_compact = (VIEW3D_TP_Display_Compact_Panel_UI, VIEW3D_TP_Display_Compact_Panel_TOOLS)

# UI COMPACT #
def update_panel_location_compact(self, context):
    try:
        for panel in panels_compact:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels_compact:
            if context.user_preferences.addons[__name__].preferences.tab_location_compact == 'tools':
             
                VIEW3D_TP_Display_Compact_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_compact
                bpy.utils.register_class(VIEW3D_TP_Display_Compact_Panel_TOOLS)
            
            if context.user_preferences.addons[__name__].preferences.tab_location_compact == 'ui':
                bpy.utils.register_class(VIEW3D_TP_Display_Compact_Panel_UI)

            if context.user_preferences.addons[__name__].preferences.tab_location_compact == 'off':  
                pass
    except:
        pass


# UI DELETE #
def update_panel_location_delete(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Delete_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Delete_Panel_TOOLS)   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Delete_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_delete == 'tools':
        
        VIEW3D_TP_Delete_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_delete        
        bpy.utils.register_class(VIEW3D_TP_Delete_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_delete == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Delete_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_delete == 'off':
        pass


# UI DISPLAY #
def update_panel_location_display(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Display_Panel_TOOLS)   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_display == 'tools':
        
        VIEW3D_TP_Display_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_display        
        bpy.utils.register_class(VIEW3D_TP_Display_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_display == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Display_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_display == 'off':
        pass


# UI MODIFIER #
def update_panel_location_modifier(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_modifier == 'tools':
        
        VIEW3D_TP_Modifier_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_modifier        
        bpy.utils.register_class(VIEW3D_TP_Modifier_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_modifier == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Modifier_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_modifier == 'off':
        pass


# UI NORMALS # 
def update_panel_location_normals(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Normals_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Normals_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Normals_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_normals == 'tools':
        
        VIEW3D_TP_Normals_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_normals        
        bpy.utils.register_class(VIEW3D_TP_Normals_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_normals == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Normals_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_normals == 'off':
        pass


# UI SELECT #
def update_panel_location_select(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Select_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Select_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Select_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_select == 'tools':
        
        VIEW3D_TP_Select_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_select       
        bpy.utils.register_class(VIEW3D_TP_Select_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_select == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Select_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_select == 'off':
        pass


# UI SCREEN #
def update_panel_location_screen(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Screen_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Screen_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Screen_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_screen  == 'tools':
        
        VIEW3D_TP_Screen_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_screen       
        bpy.utils.register_class(VIEW3D_TP_Screen_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_screen == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Screen_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_screen == 'off':
        pass


# UI SHADE #
def update_panel_location_shade(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Shade_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Shade_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Shade_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_shade == 'tools':
        
        VIEW3D_TP_Shade_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_shade        
        bpy.utils.register_class(VIEW3D_TP_Shade_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_shade == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Shade_Panel_UI)  

    if context.user_preferences.addons[__name__].preferences.tab_location_shade == 'off':
        pass


# UI SHARPEN #
def update_panel_location_sharpen(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Sharpen_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Sharpen_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Sharpen_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_sharpen == 'tools':
        
        VIEW3D_TP_Sharpen_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_sharpen        
        bpy.utils.register_class(VIEW3D_TP_Sharpen_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_sharpen == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Sharpen_Panel_UI)  

    if context.user_preferences.addons[__name__].preferences.tab_location_sharpen == 'off':
        pass


# UI SMOOTH #
def update_panel_location_smooth(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Smooth_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Smooth_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Smooth_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_smooth == 'tools':
        
        VIEW3D_TP_Smooth_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_smooth        
        bpy.utils.register_class(VIEW3D_TP_Smooth_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_smooth == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Smooth_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_smooth == 'off':
        pass



# UI UVs #
def update_panel_location_uvs(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_UVS_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_UVS_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_UVS_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_uvs == 'tools':
        
        VIEW3D_TP_UVS_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_uvs        
        bpy.utils.register_class(VIEW3D_TP_UVS_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_uvs == 'ui':
        bpy.utils.register_class(VIEW3D_TP_UVS_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_uvs == 'off':
        pass




# TOOLS REGISTRY #
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass        
        


# MENU REGISTRY #

addon_keymaps_menu = []

def update_display_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_OSD_MENU)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_osd == 'menu':
     
        VIEW3D_TP_Display_OSD_MENU.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Display_OSD_MENU)
    
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=True,  shift=True)#, alt=True)
        kmi.properties.name = 'tp_menu.display_osd'

    if context.user_preferences.addons[__name__].preferences.tab_menu_osd == 'off':
        pass


def update_menu_select(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Selection_Menu_Main)
                
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_select == 'menu':
     
        VIEW3D_TP_Selection_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu_select
    
        bpy.utils.register_class(VIEW3D_TP_Selection_Menu_Main)
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')        
        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', alt=True)
        kmi.properties.name = "VIEW3D_TP_Selection_Menu_Main"


    if context.user_preferences.addons[__name__].preferences.tab_menu_select == 'off':
        pass



# ADDON PREFERENCES #

class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    

    # TAB Addon Preferences  
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('toolsets',   "Tools",      "Tools"),
               ('url',        "URLs",       "URLs")),
               default='info')


    # TAB Locations 
    tab_location_compact = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_compact) 

    tab_location_delete = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_delete)   

    tab_location_display = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_display)   
         
    tab_location_modifier = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_modifier)    

    tab_location_normals = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_normals)

    tab_location_select = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_select)

    tab_location_screen = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_screen)

    tab_location_shade = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_shade)

    tab_location_sharpen = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_sharpen)

    tab_location_smooth = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_smooth)
               
    tab_location_uvs = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='off', update = update_panel_location_uvs)               


    #TAB Menu
    tab_menu_osd = EnumProperty(
        name = '3d View Menu: Display',
        description = '',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_display_menu)

    tab_menu_select = EnumProperty(
        name = '3d View Menu: Selection',
        description = '',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='off', update = update_menu_select)  


    #TAB Tools Compact
    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_icons = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Icons on', 'enable tools in panel'), ('off', 'Icons off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_pivot = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pivot on', 'enable tools in panel'), ('off', 'Pivot off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_world = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Shade on', 'enable tools in panel'), ('off', 'Shade off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_view = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Screen on', 'enable tools in panel'), ('off', 'Screen off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_restrict = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Restrict on', 'enable tools in panel'), ('off', 'Restrict off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_selection = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Selection on', 'enable tools in panel'), ('off', 'Selection off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_delete = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Delete on', 'enable tools in panel'), ('off', 'Delete off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_display = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Display on', 'enable tools in panel'), ('off', 'Display off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_shade = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Smooth on', 'enable tools in panel'), ('off', 'Smooth off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_material = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Material on', 'enable tools in panel'), ('off', 'Material off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_modifier = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Modifier on', 'enable tools in panel'), ('off', 'Modifier off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_history = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)


    #TAB Location
    tools_category_compact = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_compact)
    tools_category_delete = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_delete)
    tools_category_display = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_delete)
    tools_category_modifier = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_modifier)
    tools_category_select = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_select)
    tools_category_normals = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shading / UVs', update = update_panel_location_normals)
    tools_category_screen = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Screen', update = update_panel_location_shade)
    tools_category_shade = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade', update = update_panel_location_shade)
    tools_category_sharpen = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shading / UVs', update = update_panel_location_sharpen)
    tools_category_smooth = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shading / UVs', update = update_panel_location_smooth)
    tools_category_uvs = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shading / UVs', update = update_panel_location_uvs)

    #TAB Menu
    tools_category_menu = bpy.props.BoolProperty(name = "Display Menu", description = "enable or disable menu", default=True, update = update_display_menu)
    tools_category_menu_select = bpy.props.BoolProperty(name = "Select Menu", description = "enable or disable menu", default = False, update = update_menu_select)
 

    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="T+ Display!")  
            row.label(text="Tools for object and mesh display, shading, uvs, modifier, 3D viewport")  
            row.label(text="Happy Blending!")         

            
        #Location
        if self.prefs_tabs == 'location':               
            
            col = layout.column(align=True)
           
            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Compact")
            
            row = box.row(1)
            row.prop(self, 'tab_location_compact', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_compact == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_compact")

            box.separator()


            box = col.box().column(1)
            
            box.separator() 
            
            row = box.row(1) 
            row.label(text="You can use the 'Ui TuneUp' addon to disable the default panels in blender ui interface!")
            
            row = box.row(1) 
            row.operator('wm.url_open', text = 'Ui TuneUp', icon = 'PLUGIN').url = "https://blenderartists.org/forum/showthread.php?377651-Tune-Up!"
            row.operator('wm.url_open', text = 'DEMO', icon = 'CLIP').url = "https://vimeo.com/135091434"
          
            box.separator()
            box.separator()



            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Delete")
            
            row = box.row(1)
            row.prop(self, 'tab_location_delete', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_delete == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_delete")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Display")
            
            row = box.row(1)
            row.prop(self, 'tab_location_display', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_display == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_display")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Modifier")
            
            row = box.row(1)
            row.prop(self, 'tab_location_modifier', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_modifier == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_modifier")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Normals")
            
            row = box.row(1)
            row.prop(self, 'tab_location_normals', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_normals == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_normals")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Select")
            
            row = box.row(1)
            row.prop(self, 'tab_location_select', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_select == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_select")

            box.separator()
            

            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Screen")
            
            row = box.row(1)
            row.prop(self, 'tab_location_screen', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_screen == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_screen")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Sharpen")
            
            row = box.row(1)
            row.prop(self, 'tab_location_sharpen', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_sharpen == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_sharpen")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Smooth")
            
            row = box.row(1)
            row.prop(self, 'tab_location_smooth', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_smooth == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_smooth")

            box.separator()


            box = col.box().column(1)
             
            row = box.row(1) 
            row.label("Location: UVs")
            
            row = box.row(1)
            row.prop(self, 'tab_location_uvs', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_uvs == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_uvs")

            box.separator()




        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu Display:[CTRL+SHIFT+SPACE]", icon ="COLLAPSEMENU") 
       
            row.separator()                         

            row = box.row(1)          
            row.prop(self, 'tab_menu_osd', expand=True)
            
            if self.tab_menu_osd == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next restart durably!", icon ="INFO")

            box.separator() 
           
            box.separator() 
           
            row = box.column(1)  
            row.label("Menu Select:[ALT+Q]", icon ="COLLAPSEMENU") 
       
            row.separator()                         

            row = box.row(1)          
            row.prop(self, 'tab_menu_select', expand=True)
            
            if self.tab_menu_select == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next restart durably!", icon ="INFO")

            box.separator() 



            # TIP #
            box.separator()  
            
            row = layout.row(1)             
            row.label(text="! For key change go to > User Preferences > TAB: Input !", icon ="INFO")
            sub = row.row(1)
            sub.scale_x = 0.5      
            sub.operator('wm.url_open', text = 'Addon Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. align menu: ctrl d !", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: tp_menu.align_main !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")
        
            box.separator()  


        #Tools
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
            row = box.row()
            row.label("Tools in Compact Panel")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_title', expand=True)         
            row.prop(self, 'tab_icons', expand=True)         
            row.prop(self, 'tab_pivot', expand=True)         
            row.prop(self, 'tab_world', expand=True)
            row.prop(self, 'tab_view', expand=True)
            row.prop(self, 'tab_restrict', expand=True)
            row.prop(self, 'tab_selection', expand=True)
            row.prop(self, 'tab_display', expand=True)
            row.prop(self, 'tab_shade', expand=True)
            row.prop(self, 'tab_material', expand=True)
            row.prop(self, 'tab_modifier', expand=True)
            row.prop(self, 'tab_shade', expand=True)
            row.prop(self, 'tab_history', expand=True)

            box.separator() 
            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 



        #Weblinks
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column_flow(2)
            row.operator('wm.url_open', text = 'GitHub', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus"
            row.label('')
            box.separator() 



# PROPERTY GROUP #
class Dropdown_TP_Display_Props(bpy.types.PropertyGroup):
  
    display_shade = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_display = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_material = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_view = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_world = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_world_set = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_grid = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_aoccl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_overlay = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_overlay_pl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_flymode = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_flymode_pl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_navi = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_lens = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_unwrap = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_uvmagic = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_restrict = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_modifier = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_subsurf = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_dim = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_delete = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_simplify = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_selection = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    mat_mode = bpy.props.StringProperty(default="")
    index_count_sw = bpy.props.IntProperty(name="Slot",  description="set material index", min=0, max=100, default=0)     
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "",
                                       default = "tp_mat_00",  
                                       description="material index switch") 

    new_swatch = FloatVectorProperty(name = "Color", default=[0.0,1.0,1.0], min = 0, max = 1,  subtype='COLOR')
    index_count = bpy.props.IntProperty(name="Slot",  description="set material index", min=0, max=100, default=0)  
    matrandom = bpy.props.BoolProperty(name="ID-Switch / ID-Random", description="enable random material", default=False)  
    
    Delay = BoolProperty(default=False, description="Activate delay return to normal viewport mode")
    DelayTime = IntProperty(default=30, min=0, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    DelayTimeGlobal = IntProperty(default=30, min=1, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    EditActive = BoolProperty(default=True, description="Activate for fast navigate in edit mode too")

    display_meshlint = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)



class Display_Tools_Props(bpy.types.PropertyGroup):
    
    Delay = BoolProperty(default=False, description="Activate delay return to normal viewport mode")
    DelayTime = IntProperty(default=30, min=0, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    DelayTimeGlobal = IntProperty(default=30, min=1, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    EditActive = BoolProperty(default=True, description="Activate for fast navigate in edit mode too")
    FastNavigateStop = BoolProperty(name="Fast Navigate Stop", description="Stop fast navigate mode", default=False)    
    ShowParticles = BoolProperty(name="Show Particles", description="Show or hide particles on fast navigate mode", default=True)  
    ParticlesPercentageDisplay = IntProperty(name="Display", default=25, min=0, max=100, soft_min=0, soft_max=100, subtype='FACTOR', description="Display only a percentage of particles")
    InitialParticles = IntProperty( name="Count for initial particle setting before entering fast navigate", description="Display a percentage value of particles", default=100, min=0, max=100, soft_min=0, soft_max=100)
    ScreenStart = IntProperty(name="Left Limit", default=0, min=0, max=1024, subtype='PIXEL', description="Limit the screen active area width from the left side\n changed values will take effect on the next run")
    ScreenEnd = IntProperty( name="Right Limit", default=0, min=0, max=1024, subtype='PIXEL', description="Limit the screen active area width from the right side\n changed values will take effect on the next run")
    FastMode = EnumProperty(items=[('WIREFRAME', 'Wireframe', 'Wireframe display'), ('BOUNDBOX', 'Bounding Box', 'Bounding Box display')], name="Fast")
    OriginalMode = EnumProperty(items=[('TEXTURED', 'Texture', 'Texture display mode'), ('SOLID', 'Solid', 'Solid display mode')], name="Normal", default='SOLID')

    WT_handler_enable = BoolProperty(default=False)
    WT_handler_previous_object = StringProperty(default="")



class Orphan_Tools_Props(bpy.types.PropertyGroup):
   
    mod_list = bpy.props.EnumProperty(
                       items = [tuple(["meshes"]*3),        tuple(["armatures"]*3), 
                                tuple(["cameras"]*3),       tuple(["curves"]*3),
                                tuple(["fonts"]*3),         tuple(["grease_pencil"]*3),
                                tuple(["groups"]*3),        tuple(["images"]*3),
                                tuple(["lamps"]*3),         tuple(["lattices"]*3),
                                tuple(["libraries"]*3),     tuple(["materials"]*3),
                                tuple(["actions"]*3),       tuple(["metaballs"]*3),
                                tuple(["node_groups"]*3),   tuple(["objects"]*3),
                                tuple(["sounds"]*3),        tuple(["texts"]*3), 
                                tuple(["textures"]*3),      tuple(["speakers"]*3)],
                                name = "",
                                default = "meshes", 
                                description="Target: Module choice made for orphan deletion")



# REGISTRY #

import traceback

def register():    
    restrictor.register()

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    
    # PROPS #  
    bpy.types.WindowManager.tp_props_display = bpy.props.PointerProperty(type = Dropdown_TP_Display_Props)
    bpy.types.Scene.display_props = bpy.props.PointerProperty(type=Display_Tools_Props)
    bpy.types.Scene.orphan_props = bpy.props.PointerProperty(type=Orphan_Tools_Props)
    bpy.types.Scene.cpuv_props = cpuv_properties.CPUVProperties()
       

    update_panel_location_compact(None, bpy.context)
    update_panel_location_delete(None, bpy.context)
    update_panel_location_display(None, bpy.context)
    update_panel_location_modifier(None, bpy.context)
    update_panel_location_normals(None, bpy.context)
    update_panel_location_select(None, bpy.context)
    update_panel_location_screen(None, bpy.context)
    update_panel_location_shade(None, bpy.context)
    update_panel_location_sharpen(None, bpy.context)
    update_panel_location_smooth(None, bpy.context)
    update_panel_location_uvs(None, bpy.context)

    update_display_tools(None, bpy.context)
    update_display_menu(None, bpy.context)
    update_menu_select(None, bpy.context)



def unregister():
    restrictor.unregister()

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    # PROPS #  
    del bpy.types.WindowManager.tp_props_display
    del bpy.types.Scene.display_props
    del bpy.types.Scene.orphan_props
    del bpy.types.Scene.cpuv_props

    
if __name__ == "__main__":
    register()
        
        




              
