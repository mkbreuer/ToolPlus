43# ##### BEGIN GPL LICENSE BLOCK #####
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
# Contributed to by
# testscreenings, Alejandro Omar Chocano Vasquez, Jimmy Hazevoet, Adam Newgas, meta-androcto, 
# MarvinkBreuer (MKB)

bl_info = {
    "name": "T+ Curves",
    "author": "Marvin.K.Breuer (MKB) / Multiple Addon Authors (see URLs)",
    "version": (1, 3, 2),
    "blender": (2, 78, 0),
    "location": "View3D > Toolshelf [T] > TAB > Curves",
    "description": "collection of curve object and tools",
    "warning": "",
    "wiki_url": "",
    "category": "ToolPlus"}





#from toolplus_curve.ui_menu                 import (View3D_TP_Align_Menu)


from toolplus_curve.curve_ui_convert        import (VIEW3D_TP_Curve_Convert_Panel_TOOLS)
from toolplus_curve.curve_ui_convert        import (VIEW3D_TP_Curve_Convert_Panel_UI)

from toolplus_curve.curve_ui_add            import (VIEW3D_TP_Add_Curve_Panel_TOOLS)
from toolplus_curve.curve_ui_add            import (VIEW3D_TP_Add_Curve_Panel_UI)

from toolplus_curve.curve_ui_info           import (VIEW3D_TP_Curve_Info_Panel_TOOLS)
from toolplus_curve.curve_ui_info           import (VIEW3D_TP_Curve_Info_Panel_UI)

from toolplus_curve.curve_ui_display        import (VIEW3D_TP_Curve_Display_Panel_TOOLS)
from toolplus_curve.curve_ui_display        import (VIEW3D_TP_Curve_Display_Panel_UI)

from toolplus_curve.curve_ui_edit           import (VIEW3D_TP_Curve_Edit_Panel_TOOLS)
from toolplus_curve.curve_ui_edit           import (VIEW3D_TP_Curve_Edit_Panel_UI)

from toolplus_curve.curve_ui_bevel          import (VIEW3D_TP_Curve_Bevel_Panel_TOOLS)
from toolplus_curve.curve_ui_bevel          import (VIEW3D_TP_Curve_Bevel_Panel_UI)

from toolplus_curve.curve_ui_utils          import (VIEW3D_TP_Curve_Utility_Panel_TOOLS)
from toolplus_curve.curve_ui_utils          import (VIEW3D_TP_Curve_Utility_Panel_UI)

from toolplus_curve.curve_ui_set            import (VIEW3D_TP_Curve_Set_Panel_TOOLS)
from toolplus_curve.curve_ui_set            import (VIEW3D_TP_Curve_Set_Panel_UI)

from toolplus_curve.curve_ui_taper          import (VIEW3D_TP_Taper_Curve_Panel_TOOLS)
from toolplus_curve.curve_ui_taper          import (VIEW3D_TP_Taper_Curve_Panel_UI)

from toolplus_curve.curve_ui_view           import (VIEW3D_TP_Curve_View_Panel_TOOLS)
from toolplus_curve.curve_ui_view           import (VIEW3D_TP_Curve_View_Panel_UI)

from toolplus_curve.curve_ui_custom          import (VIEW3D_TP_Custom_Panel_TOOLS)
from toolplus_curve.curve_ui_custom          import (VIEW3D_TP_Custom_Panel_UI)


from toolplus_curve.preview_utils           import register_TP_Curve_pcoll, unregister_TP_Curve_pcoll

from . icons.icons                          import load_icons
from . icons.icons                          import clear_icons


##################################
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_curve'))


if "bpy" in locals():
    
    import importlib    

    importlib.reload(add_curve_aceous_galore)
    importlib.reload(add_curve_beveled)
    importlib.reload(add_curve_spirals)
    importlib.reload(add_curve_taper)
    importlib.reload(add_curve_torus_knots)
    importlib.reload(add_curve_braid)
    importlib.reload(add_curve_curly)
    importlib.reload(add_curve_celtic_links)
    importlib.reload(add_curve_spirofit_bouncespline)
    importlib.reload(add_curve_formulacurves)
    importlib.reload(add_curve_tubetool)
    importlib.reload(add_curve_wires)
    importlib.reload(add_curve_ivygen)
    importlib.reload(add_surface_plane_cone)
    importlib.reload(add_nikitron_curve)
    importlib.reload(add_iterative_tree)  
    importlib.reload(add_curve_dialscale)
    importlib.reload(add_curve_simple)  

    importlib.reload(curve_display)
    importlib.reload(curve_insert)
    importlib.reload(curve_action)
    importlib.reload(curve_align)
    importlib.reload(curve_beveltaper)
    importlib.reload(curve_convert)
    importlib.reload(curve_copies)
    importlib.reload(curve_extend)
    importlib.reload(curve_first_points)
    importlib.reload(curve_material)
    importlib.reload(curve_spline_points)
    importlib.reload(curve_simplify)
    importlib.reload(curve_split)
    importlib.reload(curve_trim)
    importlib.reload(curve_silhouette)
    importlib.reload(curve_outline)  
    importlib.reload(curve_remove_doubles) 
     
    importlib.reload(align_advanced)  

    importlib.reload(Properties)    
    importlib.reload(Operators)    
    importlib.reload(auto_loft)    

    print("Reloaded multifiles")

else:

    from . import add_curve_aceous_galore
    from . import add_curve_beveled
    from . import add_curve_spirals
    from . import add_curve_taper
    from . import add_curve_torus_knots
    from . import add_curve_braid
    from . import add_curve_curly
    from . import add_curve_celtic_links
    from . import add_curve_spirofit_bouncespline
    from . import add_curve_formulacurves
    from . import add_curve_tubetool
    from . import add_curve_wires
    from . import add_curve_ivygen
    from . import add_surface_plane_cone
    from . import add_curve_dialscale
    from . import add_nikitron_curve
    from . import add_iterative_tree
    from . import add_curve_simple

    from . import curve_display
    from . import curve_insert
    from . import curve_action
    from . import curve_align
    from . import curve_beveltaper
    from . import curve_convert
    from . import curve_copies
    from . import curve_extend
    from . import curve_first_points
    from . import curve_material
    from . import curve_spline_points
    from . import curve_outline
    from . import curve_simplify
    from . import curve_split
    from . import curve_trim
    from . import curve_silhouette
    from . import curve_remove_doubles
    
    from . import align_advanced

    from .pipe_or_tube import __init__
    from .pipe_or_tube import Makemesh
    from .pipe_or_tube import Pipe
    from .pipe_or_tube import Tube

    from .pipe import __init__
    from .pipe import config
    from .pipe import interface
    from .pipe import interface
    from .pipe import utils
    
    from .curvetools import Properties
    from .curvetools import Operators
    from .curvetools import auto_loft
    
    from .add_curve_sapling import __init__
    from .add_curve_sapling import utils  

    print("Imported multifiles")


import add_simple_curve
import add_curve_beveled
import curve_action


import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup
from bpy.types import WindowManager
from bpy.types import Scene

# Panel Position #####################################

def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Info_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Display_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Edit_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Bevel_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Convert_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Utility_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Set_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Taper_Curve_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_View_Panel_UI)
        
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Info_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Display_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Edit_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Bevel_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Convert_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Utility_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Set_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Taper_Curve_Panel_TOOLS)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_View_Panel_TOOLS)

    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Info_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Display_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Edit_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Bevel_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Convert_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Utility_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_Set_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Taper_Curve_Panel_UI)
        bpy.utils.unregister_class(VIEW3D_TP_Curve_View_Panel_UI)

    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':

        VIEW3D_TP_Curve_Info_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_Display_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_Edit_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_Bevel_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_Convert_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_Utility_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_Set_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Taper_Curve_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        VIEW3D_TP_Curve_View_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category

        bpy.utils.register_class(VIEW3D_TP_Curve_Info_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_Display_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_Edit_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_Bevel_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_Convert_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_Utility_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_Set_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Taper_Curve_Panel_TOOLS)
        bpy.utils.register_class(VIEW3D_TP_Curve_View_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Curve_Info_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_Display_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_Edit_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_Bevel_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_Convert_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_Utility_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_Set_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Taper_Curve_Panel_UI)
        bpy.utils.register_class(VIEW3D_TP_Curve_View_Panel_UI)



# Panel Position #####################################

def update_panel_position_add(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Add_Curve_Panel_UI)        
        bpy.utils.unregister_class(VIEW3D_TP_Add_Curve_Panel_TOOLS)

    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Add_Curve_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_add == 'tools':

        VIEW3D_TP_Add_Curve_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_add

        bpy.utils.register_class(VIEW3D_TP_Add_Curve_Panel_TOOLS)

    if context.user_preferences.addons[__name__].preferences.tab_location_add == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Add_Curve_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_add == 'off':
        pass
  

def update_panel_position_custom(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Custom_Panel_UI)        
        bpy.utils.unregister_class(VIEW3D_TP_Custom_Panel_TOOLS)

    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Custom_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_custom == 'tools':

        VIEW3D_TP_Custom_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_custom

        bpy.utils.register_class(VIEW3D_TP_Custom_Panel_TOOLS)

    if context.user_preferences.addons[__name__].preferences.tab_location_custom == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Custom_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_custom == 'off':
        pass
  


# AddonPreferences #####################################

class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location = EnumProperty(
        name = 'Panel Location: Curve Tools Panels',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf [T]', 'place panel in the 3d view tool shelf [T]'),
               ('ui', 'Property Shelf [N]', 'place panel in the  3d view property shelf [N]')),
               default='tools', update = update_panel_position)

    tab_location_add = EnumProperty(
        name = 'Panel Location: Add Curve',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf [T]', 'place panel in the 3d view tool shelf [T]'),
               ('ui', 'Property Shelf [N]', 'place panel in the  3d view property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelfs')),
               default='tools', update = update_panel_position_add)

    tab_location_custom = EnumProperty(
        name = 'Panel Location: Custom',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf [T]', 'place panel in the 3d view tool shelf [T]'),
               ('ui', 'Property Shelf [N]', 'place panel in the  3d view property shelf [N]'),
               ('off', 'Off', 'disable panel in the shelfs')),
               default='off', update = update_panel_position_custom)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Curve', update = update_panel_position)
    tools_category_add = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Curve', update = update_panel_position_add)
    tools_category_custom = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Curve', update = update_panel_position_custom)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)        

        if self.prefs_tabs == 'info':

            layout.label(text="T+ Curve")
            layout.label(text="This addon includes spezial curve object and curve tools2")
            layout.label(text="Also some new small function")


        #Location
        if self.prefs_tabs == 'location':

            box = layout.box().column(1)      
                  
            row = box.row(1)
            row.label("Location: Curve Tools Panels")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)

            row = box.row(1)           
            if self.tab_location == 'tools':
                row.prop(self, "tools_category")

            box.separator()
          
            box = layout.box().column(1)  
          
            row = box.row(1)
            row.label("Location: Add Curves Panel")
            
            row = box.row(1)
            row.prop(self, 'tab_location_add', expand=True)

            row = box.row(1)            
            if self.tab_location_add == 'tools':
                row.prop(self, "tools_category_add")

            box.separator()

            box = layout.box().column(1)  
          
            row = box.row(1)
            row.label("Location: Custom Curves Panel")
            
            row = box.row(1)
            row.prop(self, 'tab_location_custom', expand=True)

            row = box.row(1)            
            if self.tab_location_custom == 'tools':
                row.prop(self, "tools_category_custom")

            box.separator()
            
            row = layout.row()
            row.label(text="please reboot blender after changing the panel location")


        #Weblinks
        if self.prefs_tabs == 'url':
            
            row = layout.column_flow(2)             
            row.operator('wm.url_open', text = 'Curve Objects', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Curve_Objects"
            row.operator('wm.url_open', text = 'Curves Galore', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Curves_Galore"
            row.operator('wm.url_open', text = 'Curve Simplify', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Curve_Simplify"
            row.operator('wm.url_open', text = 'Simple Curves', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Simple_curves"
            row.operator('wm.url_open', text = 'Curly Curves', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Curly_Curves"
            row.operator('wm.url_open', text = 'Torus Knot', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Torus_Knot"
            row.operator('wm.url_open', text = 'Sampling Tree', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Sapling_Tree"
            row.operator('wm.url_open', text = 'Taper Curve', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Bevel_-Taper_Curve"
            row.operator('wm.url_open', text = 'Ivy to Mesh', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Ivy_Gen"
            row.operator('wm.url_open', text = 'DialScale', icon = 'HELP').url = "https://github.com/3dbug/blender/blob/master/DialScale.py"
            row.operator('wm.url_open', text = 'Transform', icon = 'HELP').url = "https://github.com/3DMish/Blender-Add-ons-Transform"
            row.operator('wm.url_open', text = 'Spline Points', icon = 'HELP').url = "http://blenderscripting.blogspot.de/2013/06/normalizing-spline-points-make.html"
            row.operator('wm.url_open', text = 'AF Curve Objects', icon = 'HELP').url = "https://github.com/meta-androcto/blenderpython/wiki/AF_Curve_Objects"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?409016-Addon-T-Curves&highlight="



  
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
 

#CurveTools
def run_auto_loft(self, context):
    if self.auto_loft:
        bpy.ops.wm.auto_loft_curve()
    return None




# Define the "Extras" menu
class INFO_MT_curve_plants_add(bpy.types.Menu):
    bl_idname = "curve_plants_add"
    bl_label = "Plants"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        col = layout.column()
        layout.operator("curve.tree_add", text="Sapling Tree", icon="MOD_CURVE")       
        layout.operator("mesh.add_iterative_tree", text="Iterative Tree", icon="MOD_CURVE")

        obj = context.active_object
        if obj:
            obj_type = obj.type                
            if obj.type in {'CURVE'}: 
                
                show = bpy.context.object.data.dimensions
                if show == '3D':
                     
                    active_bevel = bpy.context.object.data.bevel_depth            
                    if active_bevel == 0.0:         
                       pass
                    else:      
                      layout.operator("mesh.addleaves", text="Iterative Leaves", icon="MOD_CURVE")   


        layout.operator("curve.ivy_gen", text="Ivy to Mesh", icon="MOD_CURVE").updateIvy = True   


class INFO_MT_curve_extras_add(bpy.types.Menu):    
    bl_idname = "curve_extra_objects_add"
    bl_label = "Extra Objects"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        col = layout.column()

        layout.operator("mesh.curveaceous_galore", text="Galore", icon="MOD_CURVE")
        layout.operator("curve.spirals", text="Spirals", icon="MOD_CURVE")
        layout.operator("curve.curlycurve", text="Curly", icon="MOD_CURVE")
        layout.operator("curve.formulacurves", text="Formula", icon="MOD_CURVE")
        layout.operator("curve.wires", text="Wires", icon="MOD_CURVE")
        layout.operator("curve.dial_scale", text="Dial/Scale", icon="MOD_CURVE")        
        layout.operator("mesh.primitive_pipe_add", text="Pipe", icon="MOD_CURVE")
        layout.operator("object.pipe_nightmare", text="PipeTech", icon="MOD_CURVE")
  
        layout.separator()
                 
        layout.operator("curve.torus_knot_plus", text="Torus Knot", icon="MOD_CURVE")
        layout.operator("mesh.add_braid", text="Braid Knot", icon="MOD_CURVE")

        layout.separator()
        
        layout.operator("curve.simplify", text="Simplify", icon="MOD_CURVE")



class INFO_MT_curve_mesh_add(bpy.types.Menu):    
    bl_idname = "curve_mesh_add"
    bl_label = "Curve to Mesh"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        col = layout.column()            
    
        layout.operator("curve.celtic_links", text="Celtic Links", icon="FORCE_VORTEX")
        layout.operator("object.add_bounce_spline", icon="FORCE_HARMONIC")
        layout.operator("object.add_spirofit_spline", icon="FORCE_MAGNETIC")            
        layout.operator("object.add_catenary_curve", icon="FORCE_CURVE")
  




class INFO_MT_Surface_Factory_add(bpy.types.Menu):    
    bl_idname = "curve_surface_factory_add"
    bl_label = "Surface Factory"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        col = layout.column()       
            
        layout.operator("object.add_surface_wedge", text="Wedge", icon="MOD_CURVE")
        layout.operator("object.add_surface_cone", text="Cone", icon="MOD_CURVE")
        layout.operator("object.add_surface_star", text="Star", icon="MOD_CURVE")
        layout.operator("object.add_surface_plane", text="Plane", icon="MOD_CURVE")
        layout.operator("curve.smooth_x_times", text="Special Smooth", icon="MOD_CURVE")



def menu_surface(self, context):
    layout = self.layout
    self.layout.separator()
    self.layout.menu("curve_surface_factory_add", icon="MOD_CURVE")    


def menu_curve(self, context):
    layout = self.layout
  
    if context.mode =='OBJECT':
        self.layout.separator()
        self.layout.menu("INFO_MT_simple_menu", text="2D Simple", icon="MOD_CURVE")
        self.layout.menu("curve_extra_objects_add", text="3D Curves", icon="MOD_CURVE")        
        self.layout.menu("curve_mesh_add", text="ToMesh", icon="MOD_CURVE") 
        self.layout.menu("curve_plants_add", text="Plants", icon="MOD_CURVE")  
      
        obj = context.active_object
        if obj:
            obj_type = obj.type                
            if obj.type in {'CURVE'}: 
                self.layout.separator()
                self.layout.operator("curve.simplify", text="Simplify", icon="MOD_CURVE")
                
        self.layout.separator()
        self.layout.operator("tp_ops.bevel_set","Beveled", icon = "MOD_CURVE") 

    if context.mode =='EDIT_CURVE':            
        self.layout.separator()
        self.layout.operator("curve.simplify", text="Simplify", icon="MOD_CURVE")

        self.layout.separator()
        self.layout.operator("tp_ops.bevel_set","Beveled", icon = "MOD_CURVE") 
    



def menu_spezial(self, context):
    layout = self.layout

    self.layout.separator() 
    self.layout.operator("curve.remove_doubles", text='Remove Doubles')
 
           

def menu_mesh(self, context):
    layout = self.layout
    layout = self.layout

    if context.mode == "EDIT_MESH":
        self.layout.separator()    
        self.layout.operator("mesh.add_curvebased_tube", text="Tube 2 Faces", icon="CURVE_DATA") 


def draw_item_SVG(self, context):
    layout = self.layout
    layout.separator()
    layout.operator('wm.url_open',  text = 'Open Online SVG Converter', icon = 'FILESEL').url = "http://image.online-convert.com/convert-to-svg"




# Registry    
import traceback

def register():
    register_TP_Curve_pcoll() 
    add_curve_beveled.register()
    add_simple_curve.register()
    curve_action.register()
          
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position(None, bpy.context)
    update_panel_position_add(None, bpy.context)
    update_panel_position_custom(None, bpy.context)

    #CurveTools  
    bpy.types.Scene.curvetools = bpy.props.PointerProperty(type=CurveTools2Settings)      
    bpy.types.WindowManager.auto_loft = BoolProperty(default=False, name="Auto Loft", update=run_auto_loft)
    bpy.context.window_manager.auto_loft = False

    # Add menus to Add menu
    bpy.types.INFO_MT_curve_add.append(menu_curve)
    bpy.types.VIEW3D_MT_edit_curve_specials.append(menu_spezial)
    bpy.types.INFO_MT_surface_add.append(menu_surface)
    bpy.types.INFO_MT_mesh_add.append(menu_mesh)
    bpy.types.GRAPH_MT_channel.append(curve_simplify.menu_func)
    bpy.types.DOPESHEET_MT_channel.append(curve_simplify.menu_func)
    bpy.types.INFO_MT_file_import.append(draw_item_SVG)   


def unregister():
    unregister_TP_Curve_pcoll()
    add_curve_beveled.unregister()
    add_simple_curve.unregister()
    curve_action.unregister()
    
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    # Remove menus from the Add menu
    bpy.types.INFO_MT_curve_add.remove(menu_curve)
    bpy.types.VIEW3D_MT_edit_curve_specials.remove(menu_spezial)
    bpy.types.INFO_MT_surface_add.remove(menu_surface)
    bpy.types.INFO_MT_mesh_add.remove(menu_mesh)
    bpy.types.GRAPH_MT_channel.remove(curve_simplify.menu_func)
    bpy.types.DOPESHEET_MT_channel.remove(curve_simplify.menu_func)
    bpy.types.INFO_MT_file_import.remove(draw_item_SVG)  


if __name__ == "__main__":
    register()



