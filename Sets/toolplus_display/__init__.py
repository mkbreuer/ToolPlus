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
    "name": "T+ Display Tools",
    "author": "MKB",
    "version": (1, 0, 0),
    "blender": (2, 7, 8),
    "location": "VIEW3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "panels and menu for alternate display tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #
from toolplus_display.display_ui_menu       import (VIEW3D_TP_Display_OSD_MENU)

from toolplus_display.display_ui_normals    import (VIEW3D_TP_Normals_Panel_TOOLS)
from toolplus_display.display_ui_normals    import (VIEW3D_TP_Normals_Panel_UI)

from toolplus_display.display_ui_opengl     import (VIEW3D_TP_OpenGL_Panel_TOOLS)
from toolplus_display.display_ui_opengl     import (VIEW3D_TP_OpenGL_Panel_UI)

from toolplus_display.display_ui_shading    import (VIEW3D_TP_3D_Shade_Panel_TOOLS)
from toolplus_display.display_ui_shading    import (VIEW3D_TP_3D_Shade_Panel_UI)

from toolplus_display.display_ui_sharpen    import (ToolPlus_Sharpen_Panel_TOOLS)
from toolplus_display.display_ui_sharpen    import (ToolPlus_Sharpen_Panel_UI)

from toolplus_display.display_ui_smooth     import (VIEW3D_TP_Smooth_Panel_TOOLS)
from toolplus_display.display_ui_smooth     import (VIEW3D_TP_Smooth_Panel_UI)

from toolplus_display.display_ui_uvs        import (VIEW3D_TP_UVS_Panel_TOOLS)
from toolplus_display.display_ui_uvs        import (VIEW3D_TP_UVS_Panel_UI)

from toolplus_display.display_ui_modifier   import (VIEW3D_TP_Modifier_Panel_TOOLS)
from toolplus_display.display_ui_modifier   import (VIEW3D_TP_Modifier_Panel_UI)

from toolplus_display.display_ui_compact    import (VIEW3D_TP_Display_Compact_Panel_TOOLS)
from toolplus_display.display_ui_compact    import (VIEW3D_TP_Display_Compact_Panel_UI)



# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_display'))

if "bpy" in locals():
    import imp
    imp.reload(display_action)
    imp.reload(display_display)
    imp.reload(display_fast_navigate)
    imp.reload(display_normals)
    imp.reload(display_normals)
    imp.reload(display_normals_transfer)
    imp.reload(display_normals_weighted)
    imp.reload(display_opengl)
    imp.reload(display_shading)
    imp.reload(display_show)
    imp.reload(display_silhouette)
    imp.reload(display_tools)
    imp.reload(display_uv_equalize)
    imp.reload(display_uv_hardedges)
    imp.reload(display_uv_tube)
    imp.reload(display_view)

    imp.reload(display_sym_cut)
    imp.reload(display_sym_dim)
    imp.reload(display_sym_mods)

    imp.reload(display_mods_display)
    imp.reload(display_mods_remove)
    imp.reload(display_mods_toall)
    imp.reload(display_mods_tools)

    imp.reload(cpuv_menu)
    imp.reload(cpuv_common)
    imp.reload(cpuv_properties)
    imp.reload(cpuv_default_operation)
    imp.reload(cpuv_selseq_operation)
    imp.reload(cpuv_uvmap_operation)
    imp.reload(cpuv_fliprot_operation)
    imp.reload(cpuv_transfer_uv_operation)

else:
    from . import display_action                                                                                        
    from . import display_display                                   
    from . import display_fast_navigate                                   
    from . import display_normals                                                  
    from . import display_normals_transfer                                                  
    from . import display_normals_weighted                                                  
    from . import display_opengl                                                   
    from . import display_shading                           
    from . import display_show                           
    from . import display_silhouette                                                      
    from . import display_tools                            
    from . import display_uv_equalize               
    from . import display_uv_hardedges               
    from . import display_uv_tube               
    from . import display_view               

    from . import display_sym_cut                                          
    from . import display_sym_dim                            
    from . import display_sym_mods      

    from . import display_mods_display                                          
    from . import display_mods_remove                            
    from . import display_mods_toall    
    from . import display_mods_tools    

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

def update_panel_location(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Display_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_Display_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        
        bpy.utils.register_class(VIEW3D_TP_Display_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Display_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass



def update_panel_location_opengl(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_OpenGL_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_OpenGL_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_OpenGL_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_opengl == 'tools':
        
        VIEW3D_TP_OpenGL_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_opengl
        
        bpy.utils.register_class(VIEW3D_TP_OpenGL_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_opengl == 'ui':
        bpy.utils.register_class(VIEW3D_TP_OpenGL_Panel_UI)  

    if context.user_preferences.addons[__name__].preferences.tab_location_opengl == 'off':
        pass



def update_panel_location_shading(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_3D_Shade_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_3D_Shade_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_3D_Shade_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_shading == 'tools':
        
        VIEW3D_TP_3D_Shade_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_shading
        
        bpy.utils.register_class(VIEW3D_TP_3D_Shade_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_shading == 'ui':
        bpy.utils.register_class(VIEW3D_TP_3D_Shade_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_shading == 'off':
        pass



def update_panel_location_sharpen(self, context):
    try:
        bpy.utils.unregister_class(ToolPlus_Sharpen_Panel_UI)     
        bpy.utils.unregister_class(ToolPlus_Sharpen_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(ToolPlus_Sharpen_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_sharpen == 'tools':
        
        ToolPlus_Sharpen_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_sharpen
        
        bpy.utils.register_class(ToolPlus_Sharpen_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_sharpen == 'ui':
        bpy.utils.register_class(ToolPlus_Sharpen_Panel_UI)  

    if context.user_preferences.addons[__name__].preferences.tab_location_sharpen == 'off':
        pass



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



def update_panel_location_compact(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_Compact_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Display_Compact_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Display_Compact_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_compact == 'tools':
        
        VIEW3D_TP_Display_Compact_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_compact
        
        bpy.utils.register_class(VIEW3D_TP_Display_Compact_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_compact == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Display_Compact_Panel_UI)
  
    if context.user_preferences.addons[__name__].preferences.tab_location_compact == 'off':
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




# ADDON PREFERENCES #

class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    

    #TAB Addon Preferences  
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('toolsets',   "Tools",      "Tools"),
               ('url',        "URLs",       "URLs")),
               default='info')


    #TAB Location           
    tab_location_normals = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_normals)

    tab_location_opengl = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_opengl)

    tab_location_shading = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_shading)

    tab_location_sharpen = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_sharpen)

    tab_location_smooth = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_smooth)
               
    tab_location_uvs = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_uvs)               


    tab_location_modifier = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_modifier)    



    #TAB Location
    tools_category_compact = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_compact)
    tools_category_normals = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_normals)
    tools_category_opengl = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_opengl)
    tools_category_shading = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_shading)
    tools_category_sharpen = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_sharpen)
    tools_category_smooth = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_smooth)
    tools_category_uvs = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_uvs)
    tools_category_modifier = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Shade/UVs', update = update_panel_location_modifier)



    #TAB Location Compact 
    tab_location_compact = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_compact) 


    #TAB Tools Compact
    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_world = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Shade on', 'enable tools in panel'), ('off', 'Shade off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_view = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Screen on', 'enable tools in panel'), ('off', 'Screen off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_restrict = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Restrict on', 'enable tools in panel'), ('off', 'Restrict off', 'disable tools in panel')), default='on', update = update_display_tools)

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


    #TAB Menu
    tab_menu_osd = EnumProperty(
        name = '3d View Menu',
        description = 'location switch',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_display_menu)
  
    #TAB Menu
    tools_category_menu = bpy.props.BoolProperty(name = "Display Menu", description = "enable or disable menu", default=True, update = update_display_menu)


    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="T+ Display Tools!")  
            row.label(text="Tools for object and mesh display, shading, uvs, modifier, 3D viewport")  
            row.label(text="Compact panel or single panels for alternate ui.")  
          
            box.separator()
            
            row.label(text="Have Blending!")         

            
        #Location
        if self.prefs_tabs == 'location':               

            box = layout.box().column(1)
             
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


            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location: World")
            
            row = box.row(1)
            row.prop(self, 'tab_location_opengl', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_opengl == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_opengl")

            box.separator()


            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Display")
            
            row = box.row(1)
            row.prop(self, 'tab_location_shading', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_shading == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_shading")

            box.separator()


            box = layout.box().column(1)
             
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


            box = layout.box().column(1)
             
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

            
            box = layout.box().column(1)
             
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


            box = layout.box().column(1)
             
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


            box = layout.box().column(1)
             
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
            box.separator() 
            
            row = box.row(1) 
            row.label(text="You can use the 'Ui TuneUp' addon to disable the default panels in blender ui!")
            
            row = box.row(1) 
            row.operator('wm.url_open', text = 'Ui TuneUp', icon = 'PLUGIN').url = "https://blenderartists.org/forum/showthread.php?377651-Tune-Up!"
            row.operator('wm.url_open', text = 'DEMO', icon = 'CLIP').url = "https://vimeo.com/135091434"
          
            box.separator()




        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu:[CTRL+SHIFT+SPACE]", icon ="COLLAPSEMENU") 
       
            row.separator()                         

            row = box.row(1)          
            row.prop(self, 'tab_menu_osd', expand=True)
            
            if self.tab_menu_osd == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next restart durably!", icon ="INFO")

            box.separator() 
            
            row = box.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")
            row.operator('wm.url_open', text = 'Tip: iskeyfree', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"
          
            box.separator()


        #Tools
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
            row = box.row()
            row.label("Tools in Compact Panel")            
            
            row = box.column_flow(4)
            row.prop(self, 'tab_title', expand=True)         
            row.prop(self, 'tab_world', expand=True)
            row.prop(self, 'tab_view', expand=True)
            row.prop(self, 'tab_restrict', expand=True)
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
            row.operator('wm.url_open', text = 'Display Tools', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Display_Tools"
            row.operator('wm.url_open', text = 'UI TuneUp', icon = 'PLUGIN').url = "https://blenderartists.org/forum/showthread.php?377651-Tune-Up!"
            row.operator('wm.url_open', text = 'iskeyfree', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"
            row.operator('wm.url_open', text = 'GitHub', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus"

    

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




# REGISTRY #

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_collapse_menu_display = bpy.props.PointerProperty(type = Dropdown_TP_Display_Props)

    bpy.types.Scene.cpuv_props = cpuv_properties.CPUVProperties()
       
    update_display_tools(None, bpy.context)
    update_display_menu(None, bpy.context)

    update_panel_location_normals(None, bpy.context)
    update_panel_location_opengl(None, bpy.context)
    update_panel_location_shading(None, bpy.context)
    update_panel_location_sharpen(None, bpy.context)
    update_panel_location_smooth(None, bpy.context)
    update_panel_location_uvs(None, bpy.context)
    update_panel_location_modifier(None, bpy.context)
    update_panel_location_compact(None, bpy.context)



def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    del bpy.types.WindowManager.tp_collapse_menu_display

    del bpy.types.Scene.cpuv_props

    
if __name__ == "__main__":
    register()
        
        




              
