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
    "name": "MeshCheck",
    "author": "MKB",
    "version": (0, 1, 1),
    "blender": (2, 7, 9),
    "location": "View3D or Properties",
    "description": "collection of mesh check tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #
from toolplus_meshcheck.ui_panel        import (VIEW3D_TP_MeshCheck_TOOLS)
from toolplus_meshcheck.ui_panel        import (VIEW3D_TP_MeshCheck_UI)
from toolplus_meshcheck.ui_panel        import (VIEW3D_TP_MeshCheck_PROPS)

# LOAD PROPS #
from toolplus_meshcheck.check_meshmat   import (MeshCheckCollectionGroup)

# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_meshcheck'))

if "bpy" in locals():
    import imp
    imp.reload(check_meshlint)
    imp.reload(check_sorting)
    imp.reload(check_operators)
    imp.reload(check_orphan_slayer)
    imp.reload(operators)
    imp.reload(mesh_helpers)

else:   
    from . import check_meshlint         
    from . import check_meshmat                                     
    from . import check_operators                                     
    from . import check_orphan_slayer                                     
    from . import npp_distance                            
    from . import operators                            
    from . import mesh_helpers                            


import bpy
import math
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup



# UI REGISTRY #
panels_main = (VIEW3D_TP_MeshCheck_TOOLS, VIEW3D_TP_MeshCheck_UI, VIEW3D_TP_MeshCheck_PROPS)

def update_panel_position(self, context):
    message = "CopySHop: Updating Panel locations has failed"
    try:
        for panel in panels_main:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
         
            VIEW3D_TP_MeshCheck_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
            bpy.utils.register_class(VIEW3D_TP_MeshCheck_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
            bpy.utils.register_class(VIEW3D_TP_MeshCheck_UI)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'props':
            bpy.utils.register_class(VIEW3D_TP_MeshCheck_PROPS)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'off':  
            return None

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass




# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('tools',      "Tools",      "Tools"),
               ('ruler',      "Ruler",      "Ruler"),
               ('url',        "URLs",       "URLs")),
               default='info')


    # PANEL LOCATION #           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools',    'Tool Shelf',           'place panel in the tool shelf [T]'),
               ('ui',       'Property Shelf',       'place panel in the property shelf [N]'),
               ('props',    'Properties Data',      'place panel in the data properties tab'),
               ('off',      'Off',                  'hide panel')),
               default='tools', update = update_panel_position)


    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)


    #----------------------------------------------------------------------------------------
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

    #----------------------------------------------------------------------------------------
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
            name = 'Golden ratio',
            description = 'Display a marker showing the position of the golden division point (1.61803 : 1)',
            default = False)

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
    #----------------------------------------------------------------------------------------


    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            row = layout.column()
            row.label(text="T+ MeshCheck!")
            row.label(text="This is a collection of tools for checking the mesh")

            
        # LOCATION #
        if self.prefs_tabs == 'location':
            row = layout.row()
            row.separator()
            
            row = layout.row()
            row.label("Location: ")
            
            row= layout.row(align=True)
            row.prop(self, 'tab_location', expand=True)
            row = layout.row()
            
            if self.tab_location == 'tools':
                row.prop(self, "tools_category")


        # TOOLS #
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
          
            row = box.row()
            row.label(text="Panel Tools")
           
            #row = box.column_flow(5)
            

        # RULER #
        if self.prefs_tabs == 'ruler':
            
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


        # WEBLINKS #
        if self.prefs_tabs == 'url':
          
          row = layout.row()
          row.operator('wm.url_open', text = 'GitHub', icon = 'PACKAGE').url = "https://github.com/mkbreuer"



# PROPERTY GROUP #
class Dropdown_TP_MeshCheck_Props(bpy.types.PropertyGroup):

    display_meshlint_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_analsye_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_mcheck_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_print3d_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_measure_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_shade_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
    display_export_toggle = bpy.props.BoolProperty(name = "Open/Close", description = "open / close", default = False)
     

# PROPERTY GROUP #
class Print3DSettings_Props(bpy.types.PropertyGroup):
    
    export_format = EnumProperty(
            name="Format",
            description="Format type to export to",
            items=(('STL', "STL", ""),
                   ('PLY', "PLY", ""),
                   ('WRL', "VRML2", ""),
                   ('X3D', "X3D", ""),
                   ('OBJ', "OBJ", ""),
                   ('FBX', "FBX", "")),
            default='OBJ')
    
    use_export_texture = BoolProperty(
            name="Copy Textures",
            description="Copy textures on export to the output path",
            default=False,
            )
    use_apply_scale = BoolProperty(
            name="Apply Scale",
            description="Apply scene scale setting on export",
            default=False,
            )
    use_apply_transform = BoolProperty(
            name="Apply Transform",
            description="Apply scene transform setting on export",
            default=False,
            )
    export_path = StringProperty(
            name="Export Directory",
            description="Path to directory where the files are created",
            default="//", maxlen=1024, subtype="DIR_PATH",
            )
    thickness_min = FloatProperty(
            name="Thickness",
            description="Minimum thickness",
            subtype='DISTANCE',
            default=0.001,  # 1mm
            min=0.0, max=10.0,
            )
    threshold_zero = FloatProperty(
            name="Threshold",
            description="Limit for checking zero area/length",
            default=0.0001,
            precision=5,
            min=0.0, max=0.2,
            )
    angle_distort = FloatProperty(
            name="Angle",
            description="Limit for checking distorted faces",
            subtype='ANGLE',
            default=math.radians(45.0),
            min=0.0, max=math.radians(180.0),
            )
    angle_sharp = FloatProperty(
            name="Angle",
            subtype='ANGLE',
            default=math.radians(160.0),
            min=0.0, max=math.radians(180.0),
            )
    angle_overhang = FloatProperty(
            name="Angle",
            subtype='ANGLE',
            default=math.radians(45.0),
            min=0.0, max=math.radians(90.0),
            )



# PROPERTY GROUP #
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



# NP POINT DISTANCE # 
class NP020PointDistance(bpy.types.Macro):
    bl_idname = 'tp_ops.np_020_point_distance'
    bl_label = 'NP 020 Point Distance'
    bl_options = {'UNDO'}



# REGISTER #

import traceback

def register():
   
    check_meshmat.register() 

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position(None, bpy.context)

    # PROPS #
    bpy.types.Scene.print_3d = PointerProperty(type=Print3DSettings_Props)
    bpy.types.WindowManager.tp_props_meshcheck = bpy.props.PointerProperty(type = Dropdown_TP_MeshCheck_Props)
    bpy.types.Scene.orphan_props = bpy.props.PointerProperty(type=Orphan_Tools_Props)

    # NP POINT DISTANCE # 
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


def unregister():
      
    check_meshmat.unregister() 
   
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # PROPS #
    del bpy.types.Scene.print_3d    
    del bpy.types.WindowManager.tp_props_meshcheck
    del bpy.types.Scene.orphan_props

if __name__ == "__main__":
    register()
        
        
                                   
             

