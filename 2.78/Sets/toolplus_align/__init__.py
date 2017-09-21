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
    "name": "T+ Align",
    "author": "MKB",
    "version": (0, 2, 0),
    "blender": (2, 7, 8),
    "location": "Editor 3D Viewport > Tool Shelf [T] / Property Shelf [N] / Header / Menus",
    "description": "Collection of Align Tools, see TAB URLs for Tools Authors: wiki/downloads",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



from toolplus_align.align_menu_align        import (View3D_TP_Align_Menu)
from toolplus_align.align_menu_relax        import (VIEW3D_TP_Relax_Menu)
from toolplus_align.align_menu_space        import (VIEW3D_TP_Space_Menu)
from toolplus_align.align_menu_origin       import (VIEW3D_TP_Origin_Menu)

from toolplus_align.align_ui_main           import (VIEW3D_TP_Align_Panel_TOOLS)
from toolplus_align.align_ui_main           import (VIEW3D_TP_Align_Panel_UI)

from toolplus_align.align_ui_widget         import (VIEW3D_TP_Align_Widget_Panel_TOOLS)
from toolplus_align.align_ui_widget         import (VIEW3D_TP_Align_Widget_Panel_UI)

from toolplus_align.align_ui_navi           import (VIEW3D_TP_Align_Navi_Panel_TOOLS)
from toolplus_align.align_ui_navi           import (VIEW3D_TP_Align_Navi_Panel_UI)

from toolplus_align.align_ui_relax          import (VIEW3D_TP_Align_Relax_Panel_TOOLS)
from toolplus_align.align_ui_relax          import (VIEW3D_TP_Align_Relax_Panel_UI)

from toolplus_align.origin_batch            import (View3D_TP_Origin_Batch)

from toolplus_align.align_looptools         import (Align_LoopToolsProps)
from toolplus_align.align_1d_scripts        import (paul_managerProps)

from toolplus_align.np_point_align          import (NPPLRestoreContext)

from . icons.icons                          import load_icons
from . icons.icons                          import clear_icons

##################################

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_align'))

if "bpy" in locals():
    import imp
    imp.reload(align_1d_scripts)
    imp.reload(align_advanced)
    imp.reload(align_automirror)
    imp.reload(align_by_normal)
    imp.reload(align_con_rotation)
    imp.reload(align_cursor_center)
    imp.reload(align_display)
    imp.reload(align_distribute_obj)
    imp.reload(align_face_to_face)
    imp.reload(align_lookatit)
    imp.reload(align_looptools)
    imp.reload(align_menu_align)
    imp.reload(align_mirror)
    imp.reload(align_pivot)
    imp.reload(align_setups)
    imp.reload(align_shrinksmooth)
    imp.reload(align_simple)
    imp.reload(align_simple_transform)
    imp.reload(align_snap_offset)
    imp.reload(align_snap_set)
    imp.reload(align_snap_to)
    imp.reload(align_straighten)
    imp.reload(align_to_ground)
    imp.reload(align_transform)
    imp.reload(align_vertices) 
    imp.reload(align_view) 
    imp.reload(align_xoffsets) 
    imp.reload(origin_action)
    imp.reload(origin_batch)
    imp.reload(origin_modal)
    imp.reload(origin_bbox)
    imp.reload(origin_operators)
    imp.reload(origin_zero)
    imp.reload(np_point_move)
    imp.reload(np_point_distance)
    imp.reload(np_point_align)
    imp.reload(np_point_scale)
    imp.reload(np_roto_move)
    imp.reload(header_main)
    imp.reload(header_menu)
    imp.reload(header_ops)


else:
    from . import align_1d_scripts         
    from . import align_advanced                     
    from . import align_automirror          
    from . import align_by_normal          
    from . import align_con_rotation       
    from . import align_cursor_center       
    from . import align_display     
    from . import align_distribute_obj     
    from . import align_face_to_face       
    from . import align_lookatit           
    from . import align_looptools          
    from . import align_menu_align          
    from . import align_mirror             
    from . import align_pivot              
    from . import align_setups             
    from . import align_shrinksmooth       
    from . import align_simple             
    from . import align_simple_transform                         
    from . import align_snap_offset         
    from . import align_snap_set         
    from . import align_snap_to         
    from . import align_straighten          
    from . import align_to_ground           
    from . import align_transform           
    from . import align_vertices          
    from . import align_view          
    from . import align_xoffsets          
    from . import origin_action                
    from . import origin_batch                              
    from . import origin_modal         
    from . import origin_bbox         
    from . import origin_bbox         
    from . import origin_operators                 
    from . import origin_zero                    
    from . import np_point_move           
    from . import np_point_distance           
    from . import np_point_scale           
    from . import np_roto_move           
    from . import header_main           
    from . import header_menu           
    from . import header_ops           


##################################

import bpy
from bpy import *
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



def update_panel_position_align(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_align == 'tools':
        
        VIEW3D_TP_Align_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_align
        bpy.utils.register_class(VIEW3D_TP_Align_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_align == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Align_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_align == 'off':
        pass
  

def update_panel_position_widget(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Widget_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Widget_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Widget_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_widget == 'tools':
        VIEW3D_TP_Align_Widget_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_widget
        bpy.utils.register_class(VIEW3D_TP_Align_Widget_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_widget == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Align_Widget_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_widget == 'off':
        pass


def update_panel_position_navi(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Navi_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Navi_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Navi_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_navi == 'tools':
        VIEW3D_TP_Align_Navi_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_navi
        bpy.utils.register_class(VIEW3D_TP_Align_Navi_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_navi == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Align_Navi_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_navi == 'off':
        pass


def update_panel_position_relax(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Relax_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Align_Relax_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Align_Relax_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_relax == 'tools':
        VIEW3D_TP_Align_Relax_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_relax
        bpy.utils.register_class(VIEW3D_TP_Align_Relax_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_relax == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Align_Relax_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_relax == 'off':
        pass



def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass 


def update_header_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.update_header_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.update_header_tools == 'off':
        pass 




addon_keymaps_menu = []

def update_menu_align(self, context):
    try:
        bpy.utils.unregister_class(View3D_TP_Align_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view_align == 'menu':
     
        View3D_TP_Align_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(View3D_TP_Align_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('tp_batch.align_menu', 'ONE', 'PRESS', alt=True) #,ctrl=True, shift=True, 
        #kmi.properties.name = ''

    if context.user_preferences.addons[__name__].preferences.tab_menu_view_align == 'off':
        pass


def update_menu_relax(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Relax_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view_relax == 'menu':
     
        VIEW3D_TP_Relax_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Relax_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=True, shift=True) #,alt=True
        kmi.properties.name = "tp_menu.relax_base"


    if context.user_preferences.addons[__name__].preferences.tab_menu_view_relax == 'off':
        pass


def update_menu_space(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Space_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view_space == 'menu':
     
        VIEW3D_TP_Space_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Space_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('wm.call_menu', 'BACK_SLASH', 'PRESS')#, ctrl=True, alt=True)
        kmi.properties.name = "tp_menu.align_main"


    if context.user_preferences.addons[__name__].preferences.tab_menu_view_space == 'off':
        pass


def update_menu_origin(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Origin_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view_origin == 'menu':
     
        VIEW3D_TP_Origin_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Origin_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('wm.call_menu', 'D', 'PRESS', ctrl=True) #,alt=True, shift=True, 
        kmi.properties.name = "tp_menu.origin_base"


    if context.user_preferences.addons[__name__].preferences.tab_menu_view_origin == 'off':
        pass


#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    #Tab Prop
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),  
               ('header',     "Header",     "Header"),  
               ('view',       "NP",         "NP"),  
               ('url',        "URLs",       "URLs")),
               default='info')


#----------------------------------------------------------------------------------------


    #Panel Location           
    tab_location_align = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position_align)

    tab_location_widget = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelfs')),
               default='off', update = update_panel_position_widget)

    tab_location_navi = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelfs')),
               default='off', update = update_panel_position_navi)

    tab_location_relax = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelfs')),
               default='off', update = update_panel_position_relax)


    #Menu Props
    tab_menu_view_align = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_align)

    tab_menu_view_space = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_space)

    tab_menu_view_relax = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_relax)

    tab_menu_view_origin = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_origin)



#----------------------------------------------------------------------------------------


    #Panel All

    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_pivot = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pivot on', 'enable tools in panel'), ('off', 'Pivot off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_snap_to = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapTo on', 'enable tools in panel'), ('off', 'SnapTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_align_to_axis = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AlignTo on', 'enable tools in panel'), ('off', 'AlignTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_shade = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Display on', 'enable tools in panel'), ('off', 'Display off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_history_align = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_origin_to = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'OriginTo on', 'enable tools in panel'), ('off', 'OriginTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_snap_set = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapSet on', 'enable tools in panel'), ('off', 'SnapSet off', 'disable tools in panel')), default='on', update = update_display_tools)


    #Panel ObjectMode

    tab_zero_to = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ZeroTo on', 'enable tools in panel'), ('off', 'ZeroTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_snap_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapTools on', 'enable tools in panel'), ('off', 'SnapTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_mirror_obm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_automirror = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in panel'), ('off', 'AutoMirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_ylook_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Y-Look on', 'enable tools in panel'), ('off', 'Y-Look off', 'disable tools in panel')), default='on', update = update_display_tools)
 
    tab_transform = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Apply on', 'enable tools in panel'), ('off', 'Apply off', 'disable tools in panel')), default='on', update = update_display_tools)


    #Panel Editmode

    tab_align_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AlignTools on', 'enable tools in panel'), ('off', 'AlignTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_looptools_edm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Looptools on', 'enable tools in panel'), ('off', 'Looptols off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_relax = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Relax on', 'enable tools in panel'), ('off', 'Relax off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_mirror_edm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_automirror_edm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in panel'), ('off', 'AutoMirror off', 'disable tools in panel')), default='on', update = update_display_tools)


    tab_edge_align = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'EdgeAlign on', 'enable tools in panel'), ('off', 'EdgeAlign off', 'disable tools in panel')), default='on', update = update_display_tools)

    #Panel Curve & Surface

    tab_mirror_curve = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)


    #Panel Lattice

    tab_mirror_lat = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)


    #Panel Widget
    
    tab_snap = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Manipulator on', 'enable tools in panel'), ('off', 'Manipulator off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_snapset = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapSet on', 'enable tools in menu'), ('off', 'SnapSet off', 'disable tools in menu')), default='on', update = update_display_tools)

    tab_normals = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'NormalsAxis on', 'enable tools in panel'), ('off', 'NormalsAxis off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_propedit = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'PropEdit on', 'enable tools in panel'), ('off', 'PropEdit off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_orientation = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Orientation on', 'enable tools in panel'), ('off', 'Orientation off', 'disable tools in panel')), default='on', update = update_display_tools)
 
    tab_cursor = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', '3D Cursor on', 'enable tools in panel'), ('off', '3D Cursor off', 'disable tools in panel')), default='on', update = update_display_tools)


    #Panel Relax

    tab_history_relax = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)

    #Panel Curve & Surface

    tab_mirror_curve = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)



    #Align Menu  [GRESS]

    tab_menu_advance = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Advance on', 'enable tools in panel'), ('off', 'Advance off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_snap = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Snap on', 'enable tools in panel'), ('off', 'Snap off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_np = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'NP Station on', 'enable tools in panel'), ('off', 'NP Station off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_flat = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Select L-Flat on', 'enable tools in panel'), ('off', 'Select L-Flat off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_align_face = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Align Face on', 'enable tools in panel'), ('off', 'Align Face off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_align_loop = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Align Loop on', 'enable tools in panel'), ('off', 'Align Loop off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_lpt = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'LoopTools on', 'enable tools in panel'), ('off', 'LoopTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_offset = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Offsets on', 'enable tools in panel'), ('off', 'Offsets off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_ruler = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Ruler on', 'enable tools in panel'), ('off', 'Ruler off', 'disable tools in panel')), default='on', update = update_display_tools)



    #Align Batch Menu all [ALT+1]

    tab_batch_snap_to = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapTo on', 'enable tools in panel'), ('off', 'SnapTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_align_to_axis = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AlignTo on', 'enable tools in panel'), ('off', 'AlignTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_shade = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Display on', 'enable tools in panel'), ('off', 'Display off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_history_align = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_origin_to = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'OriginTo on', 'enable tools in panel'), ('off', 'OriginTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_snap_set = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapSet on', 'enable tools in panel'), ('off', 'SnapSet off', 'disable tools in panel')), default='on', update = update_display_tools)



    #Align Batch Menu ObjectMode [ALT+1]

    tab_batch_zero_to = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ZeroTo on', 'enable tools in panel'), ('off', 'ZeroTo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_snap_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SnapTools on', 'enable tools in panel'), ('off', 'SnapTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_mirror_obm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_automirror = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in panel'), ('off', 'AutoMirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_ylook_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Y-Look on', 'enable tools in panel'), ('off', 'Y-Look off', 'disable tools in panel')), default='on', update = update_display_tools)
 
    tab_batch_transform = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Apply on', 'enable tools in panel'), ('off', 'Apply off', 'disable tools in panel')), default='on', update = update_display_tools)


    #Align Batch Menu Editmode [ALT+1]

    tab_batch_align_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AlignTools on', 'enable tools in panel'), ('off', 'AlignTools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_looptools_edm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Looptools on', 'enable tools in panel'), ('off', 'Looptols off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_relax = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Relax on', 'enable tools in panel'), ('off', 'Relax off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_mirror_edm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_batch_automirror_edm = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in panel'), ('off', 'AutoMirror off', 'disable tools in panel')), default='on', update = update_display_tools)


    tab_batch_edge_align = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'EdgeAlign on', 'enable tools in panel'), ('off', 'EdgeAlign off', 'disable tools in panel')), default='on', update = update_display_tools)



    #Function to Header

    tab_header_custom_a = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Custom on', 'enable tools in panel'), ('off', 'Custom off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_custom_b = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Custom on', 'enable tools in panel'), ('off', 'Custom off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_select = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'SnapTo on', 'enable tools in panel'), ('off', 'SnapTo off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_mirror = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_automirror = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in panel'), ('off', 'AutoMirror off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_origin = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Origin on', 'enable tools in panel'), ('off', 'Origin off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_object = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Display on', 'enable tools in panel'), ('off', 'Display off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_align = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'SnapTools on', 'enable tools in panel'), ('off', 'SnapTools off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_np = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'NP Station on', 'enable tools in panel'), ('off', 'NP Station off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_zero = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Align Advance on', 'enable tools in panel'), ('off', 'Align Advance off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_history = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_save = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'Save on', 'enable tools in panel'), ('off', 'Save off', 'disable tools in panel')), default='off', update = update_header_tools)

    tab_header_view = EnumProperty(name = 'Header Tools', description = 'on / off',
                  items=(('on', 'View on', 'enable tools in panel'), ('off', 'View off', 'disable tools in panel')), default='off', update = update_header_tools)


#----------------------------------------------------------------------------------------

    tools_category_align = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_align)
    tools_category_widget = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_widget)
    tools_category_relax = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_relax)
    tools_category_navi = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_navi)

    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Align", description = "enable or disable menu", default=True, update = update_menu_align)
    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Relax", description = "enable or disable menu", default=True, update = update_menu_relax)
    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Space", description = "enable or disable menu", default=True, update = update_menu_space)
    tools_category_menu = bpy.props.BoolProperty(name = "Menu: Origin", description = "enable or disable menu", default=True, update = update_menu_origin)


#----------------------------------------------------------------------------------------

    np_col_scheme = bpy.props.EnumProperty(
        name ='',
        items = (
            ('csc_default_grey', 'Blender_Default_NP_GREY',''),
            ('csc_school_marine', 'NP_school_paper_NP_MARINE','')),
        default = 'csc_default_grey',
        description = 'Choose the overall addon color scheme, according to your current Blender theme')

    np_size_num = bpy.props.FloatProperty(
            name='',
            description='Size of the numerics that display on-screen dimensions, the default is 18',
            default=18,
            min=10,
            max=30,
            step=100,
            precision=0)

    np_scale_dist = bpy.props.FloatProperty(
            name='',
            description='Distance multiplier (for example, for cm use 100)',
            default=100,
            min=0,
            step=100,
            precision=2)

    np_suffix_dist = bpy.props.EnumProperty(
        name='',
        items=(("'", "'", ''), ('"', '"', ''), ('thou', 'thou', ''),
               ('km', 'km', ''), ('m', 'm', ''), ('cm', 'cm', ''),
               ('mm', 'mm', ''), ('nm', 'nm', ''), ('None', 'None', '')),
        default='cm',
        description='Add a unit extension after the numerical distance ')

    np_display_badge = bpy.props.BoolProperty(
            name='Display badge',
            description='Use the graphical badge near the mouse cursor',
            default=True)

    np_size_badge = bpy.props.FloatProperty(
            name='badge_size',
            description='Size of the mouse badge, the default is 2.0',
            default=2,
            min=0.5,
            step=10,
            precision=1)


    op_prefs = bpy.props.EnumProperty(
        name ='Individual operator settings',
        items = (
            ('nppd', 'NP Point Distance',''),
            ('nppl', 'NP Point Align',''),
            ('npps', 'NP Point Scale',''),
            ('nprm', 'NP Roto Move',''),
            ('nppm', 'NP Point Move','')),
        default = 'nppd',
        description = 'Choose which settings would you like to access')
        


#----------------------------------------------------------------------------------------



    nppd_scale = bpy.props.FloatProperty(
            name = 'Scale',
            description = 'Distance multiplier (for example, for cm use 100)',
            default = 100,
            min = 0,
            step = 1,
            precision = 3)

    nppd_suffix = bpy.props.EnumProperty(
        name = 'Suffix',
        items = (
            ("'", "'", ''), ('"', '"', ''), (
                'thou', 'thou', ''), ('km', 'km', ''),
            ('m', 'm', ''), ('cm', 'cm', ''), ('mm', 'mm', ''), ('nm', 'nm', ''), ('None', 'None', '')),
        default = 'cm',
        description = 'Add a unit extension after the number ')

    nppd_badge = bpy.props.BoolProperty(
            name = 'Mouse badge',
            description = 'Use the graphical badge near the mouse cursor',
            default = True)

    nppd_step = bpy.props.EnumProperty(
        name ='Step',
        items = (
            ('simple', 'simple',
             'one-step procedure, stops after the second click'),
            ('continuous', 'continuous', 'continuous repetition of command, ESC or RMB to interrupt (some performance slowdown)')),
        default = 'simple',
        description = 'The way the command behaves after the second click')

    nppd_hold = bpy.props.BoolProperty(
            name = 'Hold result',
            description = 'Include an extra step to display the last measured distance in the viewport',
            default = False)

    nppd_gold = bpy.props.BoolProperty(
            name = 'Golden proportion',
            description = 'Display a marker showing the position of the golden division point (1.61803 : 1)',
            default = True)

    nppd_info = bpy.props.BoolProperty(
            name = 'Value to header info',
            description = 'Display last measured distance on the header',
            default = True)

    nppd_clip = bpy.props.BoolProperty(
            name = 'Value to clipboard',
            description = 'Copy last measured distance to clipboard for later reuse',
            default = True)

    nppd_col_line_main_DEF = bpy.props.BoolProperty(
            name = 'Default',
            description = 'Use the default color',
            default = True)

    nppd_col_line_shadow_DEF = bpy.props.BoolProperty(
            name = 'Default',
            description = 'Use the default color',
            default = True)

    nppd_col_num_main_DEF = bpy.props.BoolProperty(
            name = 'Default',
            description = 'Use the default color',
            default = True)

    nppd_col_num_shadow_DEF = bpy.props.BoolProperty(
            name = 'Default',
            description = 'Use the default color',
            default = True)

    nppd_xyz_lines = bpy.props.BoolProperty(
            name = 'XYZ lines',
            description = 'Display axial distance lines',
            default = True)

    nppd_xyz_distances = bpy.props.BoolProperty(
            name = 'XYZ distances',
            description = 'Display axial distances',
            default = True)

    nppd_xyz_backdrop = bpy.props.BoolProperty(
            name = 'XYZ backdrop',
            description = 'Display backdrop field for xyz distances',
            default = False)

    nppd_stereo_cage = bpy.props.BoolProperty(
            name = 'Stereo cage',
            description = 'Display bounding box that contains the dimension',
            default = True)

    nppd_col_line_main = bpy.props.FloatVectorProperty(
        name = '',
        default = (1.0,
     1.0,
     1.0,
     1.0),
        size = 4,
        subtype = "COLOR",
        min = 0,
        max = 1,
        description = 'Color of the measurement line, to disable it set alpha to 0.0')

    nppd_col_line_shadow = bpy.props.FloatVectorProperty(
        name = '',
        default = (0.1,
     0.1,
     0.1,
     0.25),
        size = 4,
        subtype = "COLOR",
        min = 0,
        max = 1,
        description = 'Color of the line shadow, to disable it set alpha to 0.0')

    nppd_col_num_main = bpy.props.FloatVectorProperty(
        name = '',
        default = (0.1,
     0.1,
     0.1,
     0.75),
        size = 4,
        subtype = "COLOR",
        min = 0,
        max = 1,
        description = 'Color of the number, to disable it set alpha to 0.0')

    nppd_col_num_shadow = bpy.props.FloatVectorProperty(
        name = '',
        default = (1.0,
     1.0,
     1.0,
     0.65),
        size = 4,
        subtype = "COLOR",
        min = 0,
        max = 1,
        description = 'Color of the number shadow, to disable it set alpha to 0.0')


#----------------------------------------------------------------------------------------
        


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Align!")  

            row.label(text="This is a collection of align addons from allover.")   

            row.label(text="There are three ways to execute the tools:")   
            row.label(text="> use the panel function")   
            row.label(text="> included menus with hotkeys")   
            row.label(text="> or add new shortcuts directly to the tools [RMB]")                           
            
            row.label(text="For more information, go to TAB: URLs")   

            row.label(text="Have Fun! :)")  


        #Tools
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
            row = box.row()
            row.label("Panel: Align All")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_title', expand=True)
            row.prop(self, 'tab_pivot', expand=True)            
            row.prop(self, 'tab_snap_to', expand=True)
            row.prop(self, 'tab_align_to_axis', expand=True)
            row.prop(self, 'tab_origin_to', expand=True) 
            row.prop(self, 'tab_snap_set', expand=True) 
            row.prop(self, 'tab_shade', expand=True)
            row.prop(self, 'tab_history_align', expand=True)
            row.prop(self, 'tab_title', expand=True)
            
            box.separator()
      
            row = box.row()
            row.label("Panel: Align Objectmode")
            
            row = box.column_flow(4)
            row.prop(self, 'tab_zero_to', expand=True)
            row.prop(self, 'tab_snap_tools', expand=True)
            row.prop(self, 'tab_mirror_obm', expand=True)
            row.prop(self, 'tab_automirror', expand=True)
            row.prop(self, 'tab_ylook_tools', expand=True)
            row.prop(self, 'tab_transform', expand=True)
            
            box.separator()

            row = box.row()
            row.label("Panel: Align Editmode")
            
            row = box.column_flow(4)
            row.prop(self, 'tab_align_tools', expand=True)
            row.prop(self, 'tab_looptools_edm', expand=True)
            row.prop(self, 'tab_relax', expand=True)
            row.prop(self, 'tab_mirror_edm', expand=True)
            row.prop(self, 'tab_automirror_edm', expand=True)     
            row.prop(self, 'tab_edge_align', expand=True)
            
            box.separator()


            box = layout.box().column(1)
            
            row = box.column_flow(3)

            row.label("Panel: Align Curve & Surface")
            row.prop(self, 'tab_mirror_curve', expand=True)
            
            row.label("Panel: Align Lattice")
            row.prop(self, 'tab_mirror_lat', expand=True)

            row.label("Panel: Relax")
            row.prop(self, 'tab_history_relax', expand=True)           
                        
            box.separator()


            box = layout.box().column(1)      
                  
            row = box.row()
            row.label("Panel: Widget")
            
            row = box.column_flow(5)
            row.prop(self, 'tab_snap', expand=True)    
            row.prop(self, 'tab_snapset', expand=True)    
            row.prop(self, 'tab_normals', expand=True)    
            row.prop(self, 'tab_orientation', expand=True)    
            row.prop(self, 'tab_cursor', expand=True)    
          
            box.separator()


            box = layout.box().column(1)
            
            row = box.row()
            row.label("Menu: Align Menu [GRESS]")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_menu_advance', expand=True)
            row.prop(self, 'tab_menu_snap', expand=True)
            row.prop(self, 'tab_menu_np', expand=True) 
            row.prop(self, 'tab_menu_flat', expand=True) 
            row.prop(self, 'tab_menu_align_face', expand=True)
            row.prop(self, 'tab_menu_align_loop', expand=True)
            row.prop(self, 'tab_menu_lpt', expand=True)
            row.prop(self, 'tab_menu_offset', expand=True)
            row.prop(self, 'tab_menu_ruler', expand=True)
            
            box.separator()


            box = layout.box().column(1)
            
            row = box.row()
            row.label("Menu: Align Batch Menu [ALT+1]")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_batch_snap_to', expand=True)
            row.prop(self, 'tab_batch_align_to_axis', expand=True)
            row.prop(self, 'tab_batch_origin_to', expand=True) 
            row.prop(self, 'tab_batch_snap_set', expand=True) 
            row.prop(self, 'tab_batch_shade', expand=True)
            row.prop(self, 'tab_batch_history_align', expand=True)
            row.prop(self, 'tab_batch_title', expand=True)
            
            box.separator()
        
            row = box.row()
            row.label("Menu: Align Batch Objectmode [ALT+1]")
            
            row = box.column_flow(4)
            row.prop(self, 'tab_batch_zero_to', expand=True)
            row.prop(self, 'tab_batch_snap_tools', expand=True)
            row.prop(self, 'tab_batch_mirror_obm', expand=True)
            row.prop(self, 'tab_batch_automirror', expand=True)
            row.prop(self, 'tab_batch_ylook_tools', expand=True)
            row.prop(self, 'tab_batch_transform', expand=True)
            
            box.separator()

            row = box.row()
            row.label("Menu: Align Batch Editmode [ALT+1]")
            
            row = box.column_flow(4)
            row.prop(self, 'tab_batch_align_tools', expand=True)
            row.prop(self, 'tab_batch_looptools_edm', expand=True)
            row.prop(self, 'tab_batch_relax', expand=True)
            row.prop(self, 'tab_batch_mirror_edm', expand=True)
            row.prop(self, 'tab_batch_automirror_edm', expand=True)     
            row.prop(self, 'tab_batch_edge_align', expand=True)
            
            box.separator()


            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        #Locations
        if self.prefs_tabs == 'location':
            box = layout.box().column(1) 
            
            row = box.row(1) 
            row.label("Location Align: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_align', expand=True)
            
            if self.tab_location_align == 'tools':

                box.separator()

                row = box.row(1) 
                row.prop(self, "tools_category_align")

            box.separator()
        
            box = layout.box().column(1) 

            row = box.row(1) 
            row.label("Location Widget: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_widget', expand=True)

            if self.tab_location_widget == 'tools':
 
                box.separator()

                row = box.row(1) 
                row.prop(self, "tools_category_widget")

            box.separator()
        
            box = layout.box().column(1) 

            row = box.row(1) 
            row.label("Location Navigation: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_navi', expand=True)

            if self.tab_location_navi == 'tools':
 
                box.separator()

                row = box.row(1) 
                row.prop(self, "tools_category_navi")

            box.separator()

            box = layout.box().column(1) 

            row = box.row(1) 
            row.label("Location Relax: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_relax', expand=True)

            if self.tab_location_relax == 'tools':
 
                box.separator()

                row = box.row(1) 
                row.prop(self, "tools_category_relax")

            box.separator()
            
            box = layout.box().column(1) 

            row = box.row(1)            
            row.label(text="...please reboot blender after changing the locations...", icon ="INFO")
            
            box.separator()


        #Keymap
        if self.prefs_tabs == 'keymap':

            #Align Batch Menu
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Align Batch Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: '[ALT+ONE] ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view_align', expand=True)
            
            if self.tab_menu_view_align == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")


            #Align Menu
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Align Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: [BACKSLASH] ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view_space', expand=True)

            if self.tab_menu_view_space == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")


            #Origin Menu
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Origin Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: [CTRL+D] ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view_origin', expand=True)
            
            if self.tab_menu_view_origin == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")


            #Relax Menu
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Relax Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: [CTRL+SHIFT+W] ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view_relax', expand=True)
            
            if self.tab_menu_view_relax == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

           
            #Tip
            box.separator()  
            
            row = layout.column(1) 
            row.label(text="! for key change go to > User Preferences > TAB: Input !", icon ="INFO")
            row.operator('wm.url_open', text = '!Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"


        #Point Distance
        if self.prefs_tabs == 'header':
            
            layout = self.layout
            
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Functions to Header:", icon ="COLLAPSEMENU")   

            row = box.column_flow(3)
            row.prop(self, 'tab_header_select', expand=True)
            row.prop(self, 'tab_header_mirror', expand=True)
            row.prop(self, 'tab_header_automirror', expand=True)
            row.prop(self, 'tab_header_origin', expand=True)
            row.prop(self, 'tab_header_object', expand=True)
            row.prop(self, 'tab_header_align', expand=True)
            row.prop(self, 'tab_header_np', expand=True)
            row.prop(self, 'tab_header_zero', expand=True)
            row.prop(self, 'tab_header_history', expand=True)
            row.prop(self, 'tab_header_save', expand=True)
            row.prop(self, 'tab_header_view', expand=True)
            row.prop(self, 'tab_header_custom_a', expand=True)
            row.prop(self, 'tab_header_custom_b', expand=True)

        #Point Distance
        if self.prefs_tabs == 'view':
            
            layout = self.layout
            
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("NP Station Settings:", icon ="COLLAPSEMENU")   
            row.label("ABC Point Align / GRS Snap Transform Tools", icon ="COLLAPSEMENU")   

            split = box.split()
            
            col = split.column()
            col.label(text='Main color scheme:')
           
            col = split.column()
            col.prop(self, "np_col_scheme")
           
            split = box.split()
          
            col = split.column()
            col.label(text='Size of the numerics:')
            
            col = split.column()
            col.prop(self, "np_size_num")
          
            split = box.split()
           
            col = split.column()
            col.label(text='Unit scale for distance:')
           
            col = split.column()
            col.prop(self, "np_scale_dist")
           
            split = box.split()
           
            col = split.column()
            col.label(text='Unit suffix for distance:')
           
            col = split.column()
            col.prop(self, "np_suffix_dist")
          
            split = box.split()
          
            col = split.column()
            col.label(text='Mouse badge:')
          
            col = split.column()
            col = split.column()
           
            col.prop(self, "np_display_badge")
           
            if self.np_display_badge == True:
                col = split.column()
                col.prop(self, "np_size_badge")
            else:
                col = split.column()
          
            split = box.split()
            split = box.split()
            split = box.split()
           
            #row.prop(self, "op_prefs")

            #split = box.split()


            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Point Distance Settings:", icon ="COLLAPSEMENU")   

            
            split = box.split()
            split = box.split()
           
            col = split.column()
            col.prop(self, "nppd_scale")
            
            col = split.column()
            col.prop(self, "nppd_suffix")
           
            split = box.split()
           
            col = split.column()            
            col.prop(self, "nppd_step")
          
            col = split.column()
            col.prop(self, "nppd_badge")
            
            col = split.column()            
            col.prop(self, "nppd_hold")
          
            col = split.column()
            col.prop(self, "nppd_gold")

            split = box.split()
            col = split.column()
           
            col = split.column()
            col.prop(self, "nppd_info")
           
            col = split.column()
            col.prop(self, "nppd_clip")
           
            split = box.split()
          
            col = split.column()
            col.label(text='Line Main COLOR')
            col.prop(self, "nppd_col_line_main_DEF")
            if self.nppd_col_line_main_DEF == False:
                col.prop(self, "nppd_col_line_main")
            col = split.column()
            col.label(text='Line Shadow COLOR')
            col.prop(self, "nppd_col_line_shadow_DEF")
            if self.nppd_col_line_shadow_DEF == False:
                col.prop(self, "nppd_col_line_shadow")
            col = split.column()
            col.label(text='Numerical Main COLOR')
            col.prop(self, "nppd_col_num_main_DEF")
            if self.nppd_col_num_main_DEF == False:
                col.prop(self, "nppd_col_num_main")
            col = split.column()
            col.label(text='Numerical Shadow COLOR')
            col.prop(self, "nppd_col_num_shadow_DEF")
            if self.nppd_col_num_shadow_DEF == False:
                col.prop(self, "nppd_col_num_shadow")
          
            split = box.split()
          
            col = split.column()
            col.prop(self, "nppd_stereo_cage")
            col = split.column()
            col.prop(self, "nppd_xyz_lines")
            col = split.column()
            col.prop(self, "nppd_xyz_distances")
         
            if self.nppd_xyz_distances == True:
                col = split.column()
                col.prop(self, "nppd_xyz_backdrop")
            else:
                col = split.column()


 


        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'AutoMirror', icon = 'INFO').url = "http://le-terrier-de-lapineige.over-blog.com/2014/07/automirror-mon-add-on-pour-symetriser-vos-objets-rapidement.html"
            row.operator('wm.url_open', text = 'Advanced Align', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?256114-Add-on-Advanced-align-tools"
            row.operator('wm.url_open', text = 'Rotate Constraine', icon = 'INFO').url = "http://blendscript.blogspot.de/2013/05/rotate-constraint-script.html?showComment=1367746477883#c794165451806396278"
            row.operator('wm.url_open', text = 'Distribute Objects', icon = 'INFO').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Oscurart_Tools"
            row.operator('wm.url_open', text = 'Align by Faces', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Align_by_faces"
            row.operator('wm.url_open', text = 'Look at it', icon = 'INFO').url = "http://stonefield.cocolog-nifty.com/higurashi/2013/12/blenderaddonloo.html"
            row.operator('wm.url_open', text = 'LoopTools', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Modeling/LoopTools"
            row.operator('wm.url_open', text = 'Kjartans Scripts', icon = 'INFO').url = "http://www.kjartantysdal.com/scripts"
            row.operator('wm.url_open', text = 'Simple Align', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D%20interaction/Align_Tools"
            row.operator('wm.url_open', text = 'Vertex Tools', icon = 'INFO').url = "http://airplanes3d.net/scripts-254_e.xml"
            row.operator('wm.url_open', text = 'Drop to Ground', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/Drop_to_ground"
            row.operator('wm.url_open', text = '1D_Scripts', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?399882-1D_Scripts-Bargool_1D_tools-main-thread&highlight="
            row.operator('wm.url_open', text = 'NP Station', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?418540-AddOn-NP-Station"
            row.operator('wm.url_open', text = 'NP Point Distance', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?399525-AddOn-NP-Point-Distance-(measuring-tool)&highlight="
            row.operator('wm.url_open', text = '3D Navigation', icon = 'INFO').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/3D_Navigation"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?409510-Addon-T-Align&p=3114519#post3114519"



class Dropdown_TP_Align_Props(bpy.types.PropertyGroup):

    #Transform
    display_align_help = bpy.props.BoolProperty(name = "Help ", description = "open/close help", default = False) 
    display_mirror_auto = bpy.props.BoolProperty(name="AutoMirror", description="open / close", default=False)
    display_display = bpy.props.BoolProperty(name="Display", description="open / close", default=False)
    display_apply = bpy.props.BoolProperty(name="Apply", description="open / close", default=False)

class DropdownOriginToolProps(bpy.types.PropertyGroup):

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)


class NP020PointScale(bpy.types.Macro):
    bl_idname = 'tp_ops.np_020_point_scale'
    bl_label = 'NP 020 Point Scale'
    bl_options = {'UNDO'}

class NP020RotoMove(bpy.types.Macro):
    bl_idname = 'tp_ops.np_020_roto_move'
    bl_label = 'NP 020 Roto Move'
    bl_options = {'UNDO'}

class NP020PointMove(bpy.types.Macro):
    """! Be careful: use return add obj helper > delete it for next use""" 
    bl_idname = 'tp_ops.np_020_point_move'
    bl_label = 'NP 020 Point Move'
    bl_options = {'REGISTER', 'UNDO'}

class NP020PointDistance(bpy.types.Macro):
    bl_idname = 'tp_ops.np_020_point_distance'
    bl_label = 'NP 020 Point Distance'
    bl_options = {'UNDO'}
    
class NP020PointAlign(bpy.types.Macro):
    """! Be careful: use return add obj helper > delete it for next use""" 
    bl_idname = 'tp_ops.np_020_point_align'
    bl_label = 'NP 020 Point Align'
    bl_options = {'REGISTER', 'UNDO'}



# Registration
import traceback

def register():
    #bpy.utils.register_class(TP_Panels_Preferences) 
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position_align(None, bpy.context)
    update_panel_position_widget(None, bpy.context)
    update_panel_position_navi(None, bpy.context)
    update_panel_position_relax(None, bpy.context)

    update_display_tools(None, bpy.context)
    update_header_tools(None, bpy.context)

    update_menu_align(None, bpy.context)
    update_menu_relax(None, bpy.context)
    update_menu_space(None, bpy.context)
    update_menu_origin(None, bpy.context)

    #Align
    bpy.types.WindowManager.tp_collapse_menu_align = bpy.props.PointerProperty(type = Dropdown_TP_Align_Props)

    #Origin
    bpy.types.WindowManager.bbox_origin_window = bpy.props.PointerProperty(type = DropdownOriginToolProps)

    #LoopTools
    bpy.types.WindowManager.tp_align_looptools = bpy.props.PointerProperty(type = Align_LoopToolsProps) 

    #1d_Scripts
    bpy.types.WindowManager.paul_manager = bpy.props.PointerProperty(type = paul_managerProps) 
    bpy.context.window_manager.paul_manager.display_align = False
    bpy.context.window_manager.paul_manager.align_dist_z = True
    bpy.context.window_manager.paul_manager.align_lock_z = False
    bpy.context.window_manager.paul_manager.step_len = 1.0
    bpy.context.window_manager.paul_manager.edge_idx_store = -1
    bpy.context.window_manager.paul_manager.object_name_store = ''
    bpy.context.window_manager.paul_manager.object_name_store_c = ''
    bpy.context.window_manager.paul_manager.object_name_store_v = ''
    bpy.context.window_manager.paul_manager.active_edge1_store = -1
    bpy.context.window_manager.paul_manager.active_edge2_store = -1
    bpy.context.window_manager.paul_manager.coner_edge1_store = -1
    bpy.context.window_manager.paul_manager.coner_edge2_store = -1


    #NP_Roto_Move 
    NP020RotoMove.define('OBJECT_OT_np_rm_get_context_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_get_selection_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_get_mouseloc_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_add_helper_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_prepare_context_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_run_translate_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_bgl_plane_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_run_translate_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_prepare_context_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_run_rotate_np')
    NP020RotoMove.define('OBJECT_OT_np_rm_restore_context_np')

    #NP_Point_Move  
    NP020PointMove.define('OBJECT_OT_np_pm_get_context_np')
    NP020PointMove.define('OBJECT_OT_np_pm_get_selection_np')
    NP020PointMove.define('OBJECT_OT_np_pm_get_mouseloc_np')
    NP020PointMove.define('OBJECT_OT_np_pm_add_helper_np')
    NP020PointMove.define('OBJECT_OT_np_pm_prepare_context_np')
    for i in range(1, 3):
        NP020PointMove.define('OBJECT_OT_np_pm_run_translate_np')
    NP020PointMove.define('OBJECT_OT_np_pm_restore_context_np')


    #NP_Point_Distance 
    for i in range(1, 15):
        NP020PointDistance.define('OBJECT_OT_np_pd_get_selection')
        NP020PointDistance.define('OBJECT_OT_np_pd_read_mouse_loc')
        NP020PointDistance.define('OBJECT_OT_np_pd_add_points')
        for i in range(1, 15):
            NP020PointDistance.define('OBJECT_OT_np_pd_run_translate')
            NP020PointDistance.define('OBJECT_OT_np_pd_run_navigate')
        NP020PointDistance.define('OBJECT_OT_np_pd_change_phase')
        for i in range(1, 15):
            NP020PointDistance.define('OBJECT_OT_np_pd_run_translate')
            NP020PointDistance.define('OBJECT_OT_np_pd_run_navigate')
        NP020PointDistance.define('OBJECT_OT_np_pd_hold_result')
        NP020PointDistance.define('OBJECT_OT_np_pd_delete_points')

 
    #NP_Point_Align
    NP020PointAlign.define('OBJECT_OT_np_pl_get_context_np')
    NP020PointAlign.define('OBJECT_OT_np_pl_get_selection_np')
    NP020PointAlign.define('OBJECT_OT_np_pl_get_mouseloc_np')
    NP020PointAlign.define('OBJECT_OT_np_pl_add_helper_np')
    NP020PointAlign.define('OBJECT_OT_np_pl_prepare_context_np')
    for i in range(1, 50):
        NP020PointAlign.define('OBJECT_OT_np_pl_run_translate_np')
    NP020PointAlign.define('OBJECT_OT_np_pl_align_selected_np')
    NP020PointAlign.define('OBJECT_OT_np_pl_restore_context_np')


    #NP_Point_Scale
    NP020PointScale.define("OBJECT_OT_np_ps_get_context_np")
    NP020PointScale.define("OBJECT_OT_np_ps_get_selection_np")
    NP020PointScale.define("OBJECT_OT_np_ps_prepare_context_np")
    NP020PointScale.define("OBJECT_OT_np_ps_display_cage_np")
    NP020PointScale.define("OBJECT_OT_np_ps_prepare_context_np")
    NP020PointScale.define("OBJECT_OT_np_ps_run_resize_np")
    NP020PointScale.define("OBJECT_OT_np_ps_restore_context_np")


def unregister():
    #bpy.utils.unregister_class(TP_Panels_Preferences) 
        
    #LoopTools
    del bpy.types.WindowManager.tp_align_looptools
    
    #1d_Scripts
    del bpy.types.WindowManager.paul_manager

    #Align
    del bpy.types.WindowManager.tp_collapse_menu_align

    #Origin
    del bpy.types.WindowManager.bbox_origin_window    


    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    

if __name__ == "__main__":
    register()
        
        







