# BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Mira Tools (T+)",
    "author": "Paul Geraskin, Marvin K. Breuer, Graham Held",
    "version": (2, 0, 0),
    "blender": (2, 78, 0),
    "location": "3D Viewport",
    "description": "Mira Tools > T+ Version > choose between Compact or single Panel UI / Batch Menu",
    "warning": "",
    "wiki_url": "https://github.com/mifth/mifthtools/wiki/Mira-Tools",
    "tracker_url": "https://github.com/mifth/mifthtools/issues",
    "category": "ToolPlus"}


#batch
from mira_tools.mi_batch import (View3D_Batch_MiraTools)

#ui compact
from mira_tools.mi_gui_compact import (VIEW3D_MIRA_Panel_TOOLS)
from mira_tools.mi_gui_compact import (VIEW3D_MIRA_Panel_UI)

from mira_tools.mi_gui_compact import (VIEW3D_Wrap_Panel_TOOLS)
from mira_tools.mi_gui_compact import (VIEW3D_Wrap_Panel_UI)


#ui main
from mira_tools.mi_gui_main import (MI_Arc_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Arc_Panel_UI)

from mira_tools.mi_gui_main import (MI_Surface_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Surface_Panel_UI)

from mira_tools.mi_gui_main import (MI_Extrude_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Extrude_Panel_UI)

from mira_tools.mi_gui_main import (MI_Curve_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Curve_Panel_UI)

from mira_tools.mi_gui_main import (MI_Deform_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Deform_Panel_UI)

from mira_tools.mi_gui_main import (MI_Setting_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Setting_Panel_UI)

from mira_tools.mi_gui_main import (MI_Wrap_Panel_TOOLS)
from mira_tools.mi_gui_main import (MI_Wrap_Panel_UI)

from mira_tools.mi_gui_main import register_icons, unregister_icons


if "bpy" in locals():
    import imp

    imp.reload(mi_batch)

    imp.reload(mi_color_manager)

    imp.reload(mi_curve_guide)
    imp.reload(mi_curve_main)
    imp.reload(mi_curve_stretch)
    imp.reload(mi_curve_surfaces)    
    imp.reload(mi_curve_test)

    imp.reload(mi_deform)
    imp.reload(mi_draw_extrude)
    imp.reload(mi_inputs)
    imp.reload(mi_linear_deformer)
    imp.reload(mi_linear_widget)
    imp.reload(mi_looptools)
    imp.reload(mi_make_arc)
    imp.reload(mi_noise)
    imp.reload(mi_poly_loop)
    imp.reload(mi_settings)
    imp.reload(mi_utils_base)

    imp.reload(mi_widget_curve)
    imp.reload(mi_widget_linear_deform)
    imp.reload(mi_widget_select)

    imp.reload(mi_wrap_master)

else:
    from . import mi_batch

    from . import mi_curve_guide
    from . import mi_curve_main
    from . import mi_curve_stretch
    from . import mi_curve_surfaces
    from . import mi_curve_test

    from . import mi_deform
    from . import mi_draw_extrude
    from . import mi_inputs
    from . import mi_linear_deformer
    from . import mi_linear_widget
    from . import mi_looptools
    from . import mi_make_arc
    from . import mi_noise
    from . import mi_poly_loop
    from . import mi_settings
    from . import mi_utils_base

    from . import mi_widget_curve
    from . import mi_widget_linear_deform
    from . import mi_widget_select

    from . import mi_wrap_master


import bpy, os
from bpy.props import *

import rna_keymap_ui

from bpy import*
from bpy.types import AddonPreferences, PropertyGroup


def update_panel_position_cmp(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MIRA_Panel_UI)        
        bpy.utils.unregister_class(VIEW3D_Wrap_Panel_UI)     
           
        bpy.utils.unregister_class(VIEW3D_MIRA_Panel_TOOLS)        
        bpy.utils.unregister_class(VIEW3D_Wrap_Panel_TOOLS)        

    except:
        pass    
    try:
        bpy.utils.unregister_class(VIEW3D_MIRA_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_Wrap_Panel_UI)

    except:
        pass
        
    if context.user_preferences.addons[__name__].preferences.tab_location_cmp == 'tools':        

        VIEW3D_MIRA_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_cmp       
        VIEW3D_Wrap_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_cmp       
        
        bpy.utils.register_class(VIEW3D_MIRA_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_Wrap_Panel_TOOLS)

    if context.user_preferences.addons[__name__].preferences.tab_location_cmp == 'ui':        
       
        bpy.utils.register_class(VIEW3D_MIRA_Panel_UI)
        bpy.utils.register_class(VIEW3D_Wrap_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_cmp == 'off':
        pass      



def update_panel_position_main(self, context):
    try:

        bpy.utils.unregister_class(MI_Arc_Panel_UI)
        bpy.utils.unregister_class(MI_Surface_Panel_UI)
        bpy.utils.unregister_class(MI_Curve_Panel_UI)
        bpy.utils.unregister_class(MI_Extrude_Panel_UI)
        bpy.utils.unregister_class(MI_Deform_Panel_UI)
        bpy.utils.unregister_class(MI_Setting_Panel_UI)
        bpy.utils.unregister_class(MI_Wrap_Panel_UI)
        
        bpy.utils.unregister_class(MI_Arc_Panel_TOOLS)
        bpy.utils.unregister_class(MI_Surface_Panel_TOOLS)
        bpy.utils.unregister_class(MI_Curve_Panel_TOOLS)
        bpy.utils.unregister_class(MI_Extrude_Panel_TOOLS)
        bpy.utils.unregister_class(MI_Deform_Panel_TOOLS)
        bpy.utils.unregister_class(MI_Setting_Panel_TOOLS)
        bpy.utils.unregister_class(MI_Wrap_Panel_TOOLS)
        
    except:
        pass
    
    try:
        bpy.utils.unregister_class(MI_Arc_Panel_UI)
        bpy.utils.unregister_class(MI_Surface_Panel_UI)
        bpy.utils.unregister_class(MI_Curve_Panel_UI)
        bpy.utils.unregister_class(MI_Extrude_Panel_UI)
        bpy.utils.unregister_class(MI_Deform_Panel_UI)
        bpy.utils.unregister_class(MI_Setting_Panel_UI)
        bpy.utils.unregister_class(MI_Wrap_Panel_UI)

    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_main == 'tools':
        
        MI_Arc_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_Surface_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_Curve_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_Extrude_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_Deform_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_Setting_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_Wrap_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main       

        bpy.utils.register_class(MI_Arc_Panel_TOOLS)
        bpy.utils.register_class(MI_Surface_Panel_TOOLS)
        bpy.utils.register_class(MI_Curve_Panel_TOOLS)
        bpy.utils.register_class(MI_Extrude_Panel_TOOLS)
        bpy.utils.register_class(MI_Deform_Panel_TOOLS)
        bpy.utils.register_class(MI_Setting_Panel_TOOLS)
        bpy.utils.register_class(MI_Wrap_Panel_TOOLS)


    if context.user_preferences.addons[__name__].preferences.tab_location_main == 'ui':
        
        bpy.utils.register_class(MI_Arc_Panel_UI)
        bpy.utils.register_class(MI_Surface_Panel_UI)
        bpy.utils.register_class(MI_Curve_Panel_UI)
        bpy.utils.register_class(MI_Extrude_Panel_UI)
        bpy.utils.register_class(MI_Deform_Panel_UI)
        bpy.utils.register_class(MI_Setting_Panel_UI)
        bpy.utils.register_class(MI_Wrap_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_main == 'off':
        pass


#Panel 
addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(View3D_Batch_MiraTools)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        View3D_Batch_MiraTools.bl_category = context.user_preferences.addons[__name__].preferences.tab_menu_view

        bpy.utils.register_class(View3D_Batch_MiraTools)
    
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('tp_ops.miratools', 'BACK_SLASH', 'PRESS') #, shift=True, alt=True, 
        #kmi.properties.name = 'View3D_Batch_MiraTools'

    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass




#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    key_inputs = EnumProperty(
        name = "Key Inputs Style",
        items = (('Blender', 'Blender', ''),
                ('Maya', 'Maya', '')
                ),
        default = 'Blender')


    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location_cmp = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'disable panel')),
               default='off', update = update_panel_position_cmp)

    tab_location_main = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'disable panel')),
               default='tools', update = update_panel_position_main)


    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)


    tools_category_cmp = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Mira', update = update_panel_position_cmp)
    tools_category_main = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Mira', update = update_panel_position_main)


    def draw(self, context):
        layout = self.layout
        

        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            box = layout.box()
          
            row = box.row(1)            
            row.label(text="Welcome to MiraTools!")

            row = box.column(1)
            row.label(text="This addon includes modern modeling and retopology tools.")
            row.label(text="They allows you to create, deform and drawing mesh")
            row.label(text="Have Fun! :) ")


        #Location
        if self.prefs_tabs == 'location':
            box = layout.box()
          
            row = box.row(1)  
            row.label("Location Main: ")
            
            row = box.row(1)  
            row.prop(self, 'tab_location_main', expand=True)

            if self.tab_location_main == 'tools':

                row = box.row(1)                  
                row.prop(self, "tools_category_main")

            box.separator()
            
            row = box.row(1)  
            row.label("Location Compact: ")
            
            row = box.row(1)  
            row.prop(self, 'tab_location_cmp', expand=True)

            if self.tab_location_cmp == 'tools':

                row = box.row(1)                  
                row.prop(self, "tools_category_cmp")
            

            box.separator()
            
            row = box.row(1) 
            row.label(text="please restart blender after changing the panel location", icon ="INFO")       
         

        #Keymap
        if self.prefs_tabs == 'keymap':
            
            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("MiraTools Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: 'BACKSLASH + ALT")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
             
            row.operator('wm.url_open', text = 'recommended: is key free addon', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"

            box.separator() 
            
            row = box.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")


        #Weblinks
        if self.prefs_tabs == 'url':
            box = layout.box()
          
            row = box.row(1)
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mifth/mifthtools/wiki/Mira-Tools"
            row.operator('wm.url_open', text = 'Issues', icon = 'ERROR').url = "https://github.com/mifth/mifthtools/issues"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "http://blenderartists.org/forum/showthread.php?366107-MiraTools"




class DropdownMiraToolProps(bpy.types.PropertyGroup):

    display_mira_arc = bpy.props.BoolProperty(name="Make Arc", description="UI Make Arc Tools", default=False)
    display_mira_stretch = bpy.props.BoolProperty(name="Curve Stretch", description="UI Curve Stretch Tools", default=False)
    display_mira_sface = bpy.props.BoolProperty(name="Curve Surface", description="UI Curve Surface Tools", default=False)
    display_mira_guide = bpy.props.BoolProperty(name="Curve Guide", description="UI Curve Guide Tools", default=False)
    display_mira_modify = bpy.props.BoolProperty(name="Modify Tools", description="UI Modify Tools", default=False)
    display_mira_deform = bpy.props.BoolProperty(name="Deform Tools", description="UI Deform Tools", default=False)
    display_mira_extrude = bpy.props.BoolProperty(name="Draw Extrude", description="UI Draw Extrude", default=False)
    display_mira_settings = bpy.props.BoolProperty(name="Settings", description="UI Settings", default=False)
    display_help = bpy.props.BoolProperty(name="Help", description="Open/Close Help", default=False)

    display_mira_wrap = bpy.props.BoolProperty(name="Wrap", description="UI Wrap", default=False)

class Dropdown_Batch_MiraToolProps(bpy.types.PropertyGroup):

    display_batch_surface = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_curves = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)
    display_batch_deform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_extrude = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_arc = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_batch_settings = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)




from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper

# This allows you to right click on a button and link to the manual / see templates
def miratool_manual_map():
    url_manual_prefix = "https://blenderartists.org/forum/showthread.php?366107-MiraTools"
    url_manual_mapping = (
        ("bpy.ops.mira.curve_stretch", "MiraTool-Wiki"),               
        ("bpy.ops.mira.curve_guide", "MiraTool-Wiki"),               
        ("bpy.ops.mira.poly_loop", "MiraTool-Wiki"),               
        ("bpy.ops.mira.curve_surfaces", "MiraTool-Wiki"),               
        ("bpy.ops.mira.draw_extrude", "MiraTool-Wiki"),               
        ("bpy.ops.mira.noise", "MiraTool-Wiki"),               
        ("bpy.ops.mira.deformer", "MiraTool-Wiki"),               
        ("bpy.ops.mira.linear_deformer", "MiraTool-Wiki"),               
        ("bpy.ops.mira.make_arc", "MiraTool-Wiki"),               
        )
    return url_manual_prefix, url_manual_mapping



# register

addon_keymaps = []

def register():  
    register_icons()
    
    bpy.utils.register_module(__name__)

    bpy.types.Scene.mi_settings = PointerProperty(
        name="Global Settings",
        type=mi_settings.MI_Settings,
        description="Global Settings."
    )

    bpy.types.Scene.mi_cur_stretch_settings = PointerProperty(
        name="Curve Stretch Settings",
        type=mi_curve_stretch.MI_CurveStretchSettings,
        description="Curve Stretch Settings."
    )

    bpy.types.Scene.mi_cur_surfs_settings = PointerProperty(
        name="Curve Surfaces Settings",
        type=mi_curve_surfaces.MI_CurveSurfacesSettings,
        description="Curve Surfaces Settings."
    )

    bpy.types.Scene.mi_extrude_settings = PointerProperty(
        name="Extrude Variables",
        type=mi_draw_extrude.MI_ExtrudeSettings,
        description="Extrude Settings"
    )

    bpy.types.Scene.mi_ldeformer_settings = PointerProperty(
        name="Linear Deformer Variables",
        type=mi_linear_deformer.MI_LDeformer_Settings,
        description="Linear Deformer Settings"
    )

    bpy.types.Scene.mi_curguide_settings = PointerProperty(
        name="Curve Guide Variables",
        type=mi_curve_guide.MI_CurGuide_Settings,
        description="Curve Guide Settings"
    )

    bpy.types.Scene.mi_makearc_settings = PointerProperty(
        name="Make Arc Variables",
        type=mi_make_arc.MI_MakeArc_Settings,
        description="Make Arc Settings"
    )


    # alternative gui
    bpy.types.WindowManager.mirawindow = bpy.props.PointerProperty(type = DropdownMiraToolProps)
    bpy.types.WindowManager.batchwindow = bpy.props.PointerProperty(type = Dropdown_Batch_MiraToolProps)

    bpy.utils.register_manual_map(miratool_manual_map)

    update_menu(None, bpy.context)     
    update_panel_position_cmp(None, bpy.context)
    update_panel_position_main(None, bpy.context)



def unregister():
    import bpy

    #del bpy.types.Scene.miraTool
    #del bpy.types.Object.mi_curves  # need to investigate if i need to delete it
    del bpy.types.Scene.mi_settings
    del bpy.types.Scene.mi_cur_stretch_settings
    del bpy.types.Scene.mi_cur_surfs_settings
    del bpy.types.Scene.mi_extrude_settings
    del bpy.types.Scene.mi_ldeformer_settings
    del bpy.types.Scene.mi_curguide_settings
    del bpy.types.Scene.mi_makearc_settings

    del bpy.types.WindowManager.mirawindow
    del bpy.types.WindowManager.batchwindow

    bpy.utils.unregister_module(__name__)

    unregister_icons()

    bpy.utils.unregister_manual_map(miratool_manual_map)


if __name__ == "__main__":
    register()




