# ##### BEGIN GPL LICENSE BLOCK #####
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
# ##### END GPL LICENSE BLOCK #####
#


bl_info = {
    "name": "T+ Curves",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 5),
    "blender": (2, 79, 0),
    "location": "View3D > Toolshelf [T] > TAB > Curves",
    "description": "collection of curve object and tools",
    "warning": "",
    "wiki_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_curve.cuv_manual  import (VIEW3D_TP_Curve_Manual)

# LOAD ICONS #
from . icons.icons   import load_icons
from . icons.icons   import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_curve'))


if "bpy" in locals():
    
    import importlib    
    
    importlib.reload(cuv_help)    
    importlib.reload(cuv_keyops)

    # INSERTS # 
    importlib.reload(add_beveled)
    importlib.reload(add_celtic)
    importlib.reload(add_curly)
    importlib.reload(add_dialscale)
    importlib.reload(add_draw)
    importlib.reload(add_formula)
    importlib.reload(add_galore)
    importlib.reload(add_iterative_tree)
    importlib.reload(add_ivygen)
    importlib.reload(add_nikitron)
    importlib.reload(add_simple)
    importlib.reload(add_spirals)  
    importlib.reload(add_spirofit_bouncespline)
    importlib.reload(add_surface_plane_cone)   
    importlib.reload(add_torus_knots)  
    importlib.reload(add_tube_edge)  
    importlib.reload(add_tube_face)  
    importlib.reload(add_wires)  

    # GUIDES #         
    importlib.reload(curve_guide_bevel)
    importlib.reload(curve_guide_draw)
    importlib.reload(curve_guide_galore)
    importlib.reload(curve_guide_taper) 
 
    # OPERATORS #
    importlib.reload(curve_actions)
    importlib.reload(curve_bevel)
    importlib.reload(curve_convert)
    importlib.reload(curve_copies)
    importlib.reload(curve_extend)
    importlib.reload(curve_material)
    importlib.reload(curve_merged)
    importlib.reload(curve_normalize) 
    importlib.reload(curve_outline) 
    importlib.reload(curve_overlay)
    importlib.reload(curve_remove) 
    importlib.reload(curve_simplify)
    importlib.reload(curve_split)
    importlib.reload(curve_start)
    importlib.reload(curve_trim)

    importlib.reload(curve_insert)
    importlib.reload(curve_display)
    importlib.reload(curve_material)
    importlib.reload(curve_align)

    importlib.reload(curve_silhouette)
    importlib.reload(curve_pivot)
    importlib.reload(curve_snapset)

    importlib.reload(Properties)    
    importlib.reload(Operators)    
    importlib.reload(auto_loft)    
   
    importlib.reload(__init__) 
    importlib.reload(internal) 
    importlib.reload(svg_export) 

    print("t+ curve files reloaded")

else:

    from . import cuv_help
    from . import cuv_keyops

    # INSERTS # 
    from .inserts import add_beveled
    from .inserts import add_celtic
    from .inserts import add_curly
    from .inserts import add_dialscale
    from .inserts import add_draw
    from .inserts import add_formula
    from .inserts import add_galore
    from .inserts import add_iterative_tree
    from .inserts import add_ivygen
    from .inserts import add_nikitron
    from .inserts import add_simple
    from .inserts import add_spirals  
    from .inserts import add_spirofit_bouncespline
    from .inserts import add_surface_plane_cone  
    from .inserts import add_torus_knots  
    from .inserts import add_tube_edge  
    from .inserts import add_tube_face  
    from .inserts import add_wires  

    from .inserts.add_curve_braid import add_curve_braid
    from .inserts.add_curve_braid import bpybraid
    from .inserts.add_curve_braid import braid

    from .inserts.add_curve_sapling import __init__
    from .inserts.add_curve_sapling import utils  

    from .inserts.add_mesh_chain_rope import __init__
    from .inserts.add_mesh_chain_rope import oscurart_chain_maker  
    from .inserts.add_mesh_chain_rope import oscurart_rope_maker  

    from .inserts.add_pipe_nightmare import __init__
    from .inserts.add_pipe_nightmare import config
    from .inserts.add_pipe_nightmare import interface
    from .inserts.add_pipe_nightmare import utils

    from .inserts.add_pipe_or_tube import __init__
    from .inserts.add_pipe_or_tube import Makemesh
    from .inserts.add_pipe_or_tube import Pipe
    from .inserts.add_pipe_or_tube import Tube


    # GUIDES # 
    from .guides import curve_guide_bevel
    from .guides import curve_guide_draw
    from .guides import curve_guide_galore
    from .guides import curve_guide_taper


    # OPERATORS #
    from .operators import curve_actions
    from .operators import curve_bevel
    from .operators import curve_convert
    from .operators import curve_copies
    from .operators import curve_extend
    from .operators import curve_material
    from .operators import curve_merged
    from .operators import curve_normalize
    from .operators import curve_outline
    from .operators import curve_overlay
    from .operators import curve_remove
    from .operators import curve_simplify
    from .operators import curve_split    
    from .operators import curve_start
    from .operators import curve_trim

    from .operators import curve_insert
    from .operators import curve_display
    from .operators import curve_align
    from .operators import curve_material
    from .operators import curve_silhouette
    from .operators import curve_pivot
    from .operators import curve_snapset

    from .operators.curvecad import __init__
    from .operators.curvecad import internal
    from .operators.curvecad import svg_export 
    
    from .curvetools import Properties
    from .curvetools import Operators
    from .curvetools import auto_loft

    print("t+ curve files imported")





# LOAD MODULS #
import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# LOAD MAPS #
from toolplus_curve.cuv_keymap  import*
from toolplus_curve.cuv_uimap   import*
from toolplus_curve.cuv_append  import*

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


# REGISTRY TOOLS # 
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass 




# ADDON PREFERENCES # 
class VIEW3D_TP_Curve_Addon_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__    

    # LIST #  
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('tools',      "Tools",      "Tools"),
               ('keymap',     "Keymap",     "Keymap"), 
               ('url',        "URLs",       "URLs")),
               default='info')

    #----------------------------

    # OPTIONS # 

    tab_location_option_switch = EnumProperty(
        name = 'Switch Options',
        description = 'switch layout for different option settings',
        items=(('panels', 'Panels', 'options for panels'),
               ('menus',  'Menus',  'options for menus'),
               ('tools',  'Tools',  'options for tools')),
               default='panels')
     
    #----------------------------

    # PANELS #            

    tab_panel_layout = EnumProperty(
        name = 'Layout Switch',
        description = 'layout switch',
        items=(('compact',   'Compact',   'compact panel layout'),
               ('separated', 'Separated', 'separated panel layout')),
               default='compact')


    tab_panel_layout_type = EnumProperty(
        name = 'Layout Switch',
        description = 'layout switch',
        items=(('type_one', 'Type A', 'compact layout'),
               ('type_two', 'Type B', 'compact layout')),
               default='type_one')

    tab_panel_layout_expand = EnumProperty(
        name = 'Layout Switch',
        description = 'layout switch',
        items=(('type_expand',  'Expand',   'enum layout'),
               ('type_dropdown','DropDown', 'enum layout')),
               default='type_expand')


    tab_panel_location = EnumProperty(
        name = 'Panel Location: Curve Compact',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool [T]', 'place panel in the 3d view tool shelf [T]'),
               ('ui', 'Property [N]', 'place panel in the  3d view property shelf [N]')),
               default='tools', update = update_panel_location)

    tools_category_location = StringProperty(name = "TAB Category", description = "create new category tab", default = 'Curve', update = update_panel_location)

    #----------------------------

    # CUSTOM #  

    tab_location_custom = EnumProperty(
        name = 'Panel Location: Custom',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool [T]', 'add panel to tool shelf [T]'),
               ('ui', 'Property [N]', 'add panel to property shelf [N]'),
               ('off', 'Off', 'disable shelf panel')),
               default='off', update = update_panel_custom)

    tab_panel_layout_custom = EnumProperty(
        name = 'Layout Custom',
        description = 'layout toggle',
        items=(('add',    'Add Custom',    'add to compact layout'),
               ('remove', 'Remove Custom', 'remove to compact layout')),
               default='remove') 
 
    tools_category_custom = StringProperty(name = "TAB Category", description = "create new category tab", default = 'Curve', update = update_panel_custom)

    #----------------------------

    # MENUS #  
        
    tab_menu_curve = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu_curve)

    tab_showhide = bpy.props.BoolProperty(name="Select, Delete, Show/Hide", description="toggle  tools", default=True)   

    #----------------------------

    # APPEND MENUS #  

    tab_menu_append = EnumProperty(
        name = '3d View Menu',
        description = 'menu for 3d view',
        items=(('add',    'Add Menus',    'add menus to default menus'),
               ('remove', 'Remove Menus', 'remove menus from default menus')),
               default='add', update = update_append_menus)    
               
    tab_append_add = bpy.props.BoolProperty(name="Add", description="2D, 3D, Knots, Plants, etc", default=True)   
    tab_append_special = bpy.props.BoolProperty(name="Special", description="add menus to default menus", default=True)   
    tab_append_delete = bpy.props.BoolProperty(name="Delete", description="Remove Doubles, Short & Zero Segment", default=True)   
    tab_append_import = bpy.props.BoolProperty(name="Im-/Export", description="Online SVG Converter" , default=True)   
    tab_append_editors = bpy.props.BoolProperty(name="Editors", description="Simplify to Graph & Dopesheet", default=True)   

    #----------------------------

    # TOOLS #    
    
    curve_vertcolor = bpy.props.FloatVectorProperty(name="OUT", default=(0.2, 0.9, 0.9, 1), size=4, subtype="COLOR", min=0, max=1)
    curve_primitiv = bpy.props.BoolProperty(name="Add Primitive", description="layout toggle", default=False)   
    curve_primitiv = bpy.props.BoolProperty(name="Add Primitive", description="layout toggle", default=False)   

    #----------------------------


    # DRAW PREFERNCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)        

        if self.prefs_tabs == 'info':
            
            col = layout.column(1)              
            
            box = col.box().column(1)          
            box.separator()  

            row = box.column(1) 
           
            row.label(text="Welcome to T+ Curves")
            row.label(text="This addon is a collection of curve objects and tools")
           
            row.separator()           
           
            row.label(text="The included shelf panel are adaptable and comes with 3 different types of layouts.")
            row.label(text="The location could be changed to toolshelf [T] or property shelf [N]")
            row.label(text="A shortcuts menu and menus for the add menu can also be activated.")
            row.label(text="And if needed a custom place holder for further tools.")
 
            row.separator()        
 
            row.label(text="Settings could be changed in the addon preferences")
            row.label(text="or at the botton of the shelf panel as well > gear button")

            row.separator()        
                        
            row.label(text="At least: Have Fun! :)")   
            
            box.separator()     
      

        #---------------------------- 
        
        
        # PANEL #
        if self.prefs_tabs == 'location':
          
            col = layout.column(1)              
            
            box = col.box().column(1)          
            box.separator()  
          
            # MAIN #                 
            row = box.row(1)
            row.label( text="Panel Layout", icon="RIGHTARROW_THIN")    
            row.operator("tp_ops.help_curve_prefs", text="", icon='INFO')  

            box.separator()  

            row = box.row(1) 
            row.prop(self, 'tab_panel_layout', expand = True)   

            if context.user_preferences.addons[__name__].preferences.tab_panel_layout == 'compact':
         
                box.separator()  
                
                row = box.row(1) 
                row.prop(self, 'tab_panel_layout_type', expand = True)   
                
               
                if context.user_preferences.addons[__name__].preferences.tab_panel_layout_type == 'type_two':
                
                    box.separator()  
                   
                    row = box.row(1) 
                    row.prop(self, 'tab_panel_layout_expand', expand = True)   
                
                else:                   
                    box.separator()                      
                   
                    row = box.row(1) 
                    row.prop(self, 'tab_panel_layout_custom', expand = True)   


            box.separator()                 
            box = col.box().column(1)          
            box.separator()  
            
            # MAIN LOCATION #                            
            row = box.column(1)
            row.label( text="Panel Location", icon="ARROW_LEFTRIGHT")      

            box.separator()  

            row = box.row(1)
            row.prop(self, 'tab_panel_location', expand = True)          
            
            if self.tab_panel_location == 'tools':
                box.separator()   
                
                row = box.row(1)
                row.prop(self, 'tools_category_location')                       
           
            box.separator()                             
            box = col.box().column(1)          
            box.separator()                              

            # CUSTOM #
            row = box.row()
            row.label( text="", icon="SCRIPT")      
            row.operator("tp_ops.keymap_curve_custom", text="Panel: Custom Layout to Text Editor")    
            row.operator("tp_ops.help_curve_custom", text="", icon='INFO')  
         
            box.separator()  

            row = box.row(1)
            row.prop(self, 'tab_location_custom', expand = True)          

            box.separator()   
            
            row = box.row(1)
            if self.tab_location_custom == 'tools':
                row.prop(self, "tools_category_custom")                     
            
            box.separator()              
           

        #---------------------------- 


        # TOOLS #
        if self.prefs_tabs == 'tools':          

            col = layout.column(1)              
            
            box = col.box().column(1)          
            box.separator() 
            
            row = box.row(1)
            row.label( text="Panel", icon="RIGHTARROW_THIN")                                         
         
            row = box.column()       
            row.prop(self, 'curve_primitiv')
            
            box.separator()  
            box = col.box().column(1)          
            box.separator() 
            
            row = box.row(1)
            row.label( text="Menu", icon="RIGHTARROW_THIN")     
   
            row = box.column()       
            row.prop(self, 'tab_showhide')
            
            box.separator()           
            

        #---------------------------- 

        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            # MENU #
            
            col = layout.column(1)              
            
            box = col.box().column(1)          
            box.separator() 
          
            row = box.row(1)  
            row.label("3D View Menu:", icon ="COLLAPSEMENU")       
            row.prop(self, 'tab_menu_curve', expand=True)
                
            box.separator() 

            if self.tab_menu_curve == 'off':
                row = box.row(1) 
                row.label(text="! save user setting for a durably hide !", icon ="INFO")

            box.separator() 

            row = box.row(1) 

            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            km = kc.keymaps['3D View']
            kmi = get_keymap_item(km, 'wm.call_menu', "VIEW3D_TP_Curve_Menu")
            draw_keymap_item(km, kmi, kc, row) 
           
            box.separator()             
            box = col.box().column(1)           
            box.separator() 

            # APPEND #            
            row = box.row(1)  
            row.label("Append Menus:", icon ="COLLAPSEMENU")        
            row.prop(self, 'tab_menu_append', expand=True)          
          
            box.separator()
                       
            row = box.column_flow(2)          
            row.prop(self, 'tab_append_add')
            #row.prop(self, 'tab_append_special')
            row.prop(self, 'tab_append_delete')
            row.prop(self, 'tab_append_import')
            row.prop(self, 'tab_append_editors')
          
            row = box.row(1)            
            row.label(text="Need restart to see effect!", icon='INFO')     

            box.separator()
            box = col.box().column(1)
            box.separator()
          
            # TIP #     
            box = layout.box().column(1)

            box.separator()
           
            row = box.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

            row = box.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. name field: shift e", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Curve_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            row.label(text="! Or adjust the keymap script directly!", icon ="INFO")            
            row.operator("tp_ops.keymap_curve", text = 'KeyMap to Text Editor')            
            row.operator('wm.url_open', text = 'Type of Events').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            row = box.row(1)             
            row.label(text="> Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="INFO")

            box.separator()  

     
        #---------------------------- 
        
        
        # WEB #
        if self.prefs_tabs == 'url':
            
            row = layout.column_flow(2)             
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus/wiki"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?409016-Addon-T-Curves&highlight="




# CURVETOOLS # 
def UpdateDummy(object, context):
    pass
   
class CurveTools2Settings(bpy.types.PropertyGroup):
    # selection
    SelectedObjects = CollectionProperty(type = Properties.CurveTools2SelectedObject)
    NrSelectedObjects = IntProperty(name = "NrSelectedObjects", default = 0, description = "Number of selected objects", update = UpdateDummy)
    # NrSelectedObjects = IntProperty(name = "NrSelectedObjects", default = 0, description = "Number of selected objects")

    # curve
    CurveLength = FloatProperty(name = "CurveLength", default = 0.0, precision = 6)
        
    #splines
    SplineResolution = IntProperty(name = "SplineResolution", default = 64, min = 2, max = 1024, soft_min = 2, description = "Spline resolution will be set to this value")
    
    SplineRemoveLength = FloatProperty(name = "SplineRemoveLength", default = 0.001, precision = 6, description = "Splines shorter than this threshold length will be removed")
    SplineJoinDistance = FloatProperty(name = "SplineJoinDistance", default = 0.001, precision = 6, description = "Splines with starting/ending points closer to each other than this threshold distance will be joined")
    SplineJoinStartEnd = BoolProperty(name = "SplineJoinStartEnd", default = False, description = "Only join splines at the starting point of one and the ending point of the other")

    splineJoinModeItems = (('At midpoint', 'At midpoint', 'Join splines at midpoint of neighbouring points'), ('Insert segment', 'Insert segment', 'Insert segment between neighbouring points'))
    SplineJoinMode = EnumProperty(items = splineJoinModeItems, name = "SplineJoinMode", default = 'At midpoint', description = "Determines how the splines will be joined")
    
    # curve intersection
    LimitDistance = FloatProperty(name = "LimitDistance", default = 0.0001, precision = 6, description = "Displays the result of the curve length calculation")

    intAlgorithmItems = (('3D', '3D', 'Detect where curves intersect in 3D'), ('From View', 'From View', 'Detect where curves intersect in the RegionView3D'))
    IntersectCurvesAlgorithm = EnumProperty(items = intAlgorithmItems, name = "IntersectCurvesAlgorithm", description = "Determines how the intersection points will be detected", default = '3D')

    intModeItems = (('Insert', 'Insert', 'Insert points into the existing spline(s)'), ('Split', 'Split', 'Split the existing spline(s) into 2'), ('Empty', 'Empty', 'Add empty at intersections'))
    IntersectCurvesMode = EnumProperty(items = intModeItems, name = "IntersectCurvesMode", description = "Determines what happens at the intersection points", default = 'Split')

    intAffectItems = (('Both', 'Both', 'Insert points into both curves'), ('Active', 'Active', 'Insert points into active curve only'), ('Other', 'Other', 'Insert points into other curve only'))
    IntersectCurvesAffect = EnumProperty(items = intAffectItems, name = "IntersectCurvesAffect", description = "Determines which of the selected curves will be affected by the operation", default = 'Both')

def run_auto_loft(self, context):
    if self.auto_loft:
        bpy.ops.wm.auto_loft_curve()
    return None



# PROPERTY DISPLAY: CURVE #
class Dropdown_TP_Curve_Props(bpy.types.PropertyGroup):

    # HELP/DOCU/FILE #
    display_title = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)     
    display_pathes = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_help = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False) 
    display_docu = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_options = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # CONVERT #
    display_convert = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_non_destructiv = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    # CURVE #
    display_curve_bevel = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)     
    display_curve_info = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_insert = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_convert = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_draw = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_edit = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_bevel_reso = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_select = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)
    display_curve_setting = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_taper = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_type = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_utility = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  

    display_curve_options = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_draw = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_curve_custom = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_2d = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_3d = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_plants = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_knots = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_more = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  
    display_curve_material = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  


# PROPERTY INSERTS # 
class Insert_Props(bpy.types.PropertyGroup):

    local_z = bpy.props.FloatProperty(name="Local Z",  description="move along local z-axis", default=0, min=-100, max=100)
    local_z_min = bpy.props.FloatProperty(name="Local -Z",  description="move along local minus z-axis", default=0, min=-100, max=0)
    local_z_max = bpy.props.FloatProperty(name="Local +Z",  description="move along local plus z-axis", default=0, min=0, max=100)
    
    local_last = bpy.props.BoolProperty(name="Local Last",  description="go to last location", default=False, options={'SKIP_SAVE'})  

    radius = bpy.props.FloatProperty(name="Radius",  description=" ", default=10, min=0.01, max=1000)
    depth = bpy.props.FloatProperty(name="Bevel",  description=" ", default=1, min=0.00, max=1000)

    ring = bpy.props.IntProperty(name="Ring",  description=" ", min=0, max=100, default=1) 
    nring = bpy.props.IntProperty(name="U Ring",  description=" ", min=0, max=100, default=2) 
    loop = bpy.props.IntProperty(name="Loop",  description=" ", min=0, max=100, default=2) 

    offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    height = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    wire = bpy.props.BoolProperty(name="Wire",  description=" ", default=False, options={'SKIP_SAVE'})    

    curve_type = bpy.props.EnumProperty(
        items=[("tp_bezier"     ,"Bezier Curve"     ,"Bezier Curve"),
               ("tp_circle"     ,"Circle Curve"     ,"Circle Curve"),
               ("tp_nurbs"      ,"Nurbs Curve"      ,"Nurbs Curve"),
               ("tp_ncircle"    ,"Nurbs Circle"     ,"Nurbs Circle")],
               name = "Type",
               default = "tp_bezier",    
               description = "add geometry")

   
    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    add_objmat = bpy.props.BoolProperty(name="Use Object Color",  description="add material and enable object color", default=False)  
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random materials", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)

    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    mode = bpy.props.StringProperty(default="")    
    convert = bpy.props.BoolProperty(name="Convert to Mesh",  description=" ", default=False, options={'SKIP_SAVE'})   




# REGISTRY #  
import traceback

def register():
          
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_append_menus(None, bpy.context)

    update_panel_location(None, bpy.context)
    update_panel_custom(None, bpy.context)

    update_menu_curve(None, bpy.context)    

    # CURVE #
    bpy.types.WindowManager.tp_props_curve = bpy.props.PointerProperty(type = Dropdown_TP_Curve_Props)
    bpy.types.Scene.curve_vertcolor = bpy.props.FloatVectorProperty(name="OUT", default=(0.2, 0.9, 0.9, 1), size=4, subtype="COLOR", min=0, max=1)
 
    # CURVETOOLS 2 #
    bpy.types.Scene.curvetools = bpy.props.PointerProperty(type=CurveTools2Settings)      
    bpy.types.WindowManager.auto_loft = BoolProperty(default=False, name="Auto Loft", update=run_auto_loft)
    bpy.context.window_manager.auto_loft = False

    # INSERT #
    bpy.types.Scene.tp_props_insert = bpy.props.PointerProperty(type=Insert_Props)   
    bpy.types.WindowManager.tp_props_insert = bpy.props.PointerProperty(type=Insert_Props)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Curve_Manual)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # CURVE #
    del bpy.types.WindowManager.tp_props_curve
    del bpy.types.Scene.curve_vertcolor   
     
    # CURVETOOLS 2 # 
    del bpy.types.Scene.curvetools     
    del bpy.types.WindowManager.auto_loft

    # INSERT #
    del bpy.types.Scene.tp_props_insert 
    del bpy.types.WindowManager.tp_props_insert 

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Curve_Manual)



if __name__ == "__main__":
    register()








