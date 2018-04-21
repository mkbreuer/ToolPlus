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
    "name": "Align",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 5),
    "blender": (2, 7, 9),
    "location": "VIEW 3D, UV Image-, Graph and Node Editor",
    "description": "align tools collection",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_align.align_manual  import (VIEW3D_TP_Align_Manual)
from toolplus_align.align_manual  import (VIEW3D_TP_Machine_Manual)
from toolplus_align.align_manual  import (VIEW3D_TP_LoopTools_Manual)

# LOAD PROPERTIES #
from toolplus_align.ops_auxiliary.oned_scripts   import (paul_managerProps)
from toolplus_align.ops_station.np_point_align   import (NPPLRestoreContext)

# LOAD CUSTOM ICONS #
from . icons.icons                               import load_icons
from . icons.icons                               import clear_icons

# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_align'))

if "bpy" in locals():
    import imp
    imp.reload(align_action)
    imp.reload(align_mirror)
    imp.reload(align_modifier) 
    imp.reload(align_orientation) 
    imp.reload(align_pencil)    
    imp.reload(align_pivot) 
    imp.reload(align_snap_set)
    imp.reload(align_snap_to)
    imp.reload(align_transform) 
    imp.reload(align_widget)

    imp.reload(advanced)
    imp.reload(center_cursor)
    imp.reload(con_rotation)
    imp.reload(distribute)     
    imp.reload(distribute_obj)
    imp.reload(easylattice)
    imp.reload(face_to_face)
    imp.reload(oned_scripts)
    imp.reload(shrinksmooth) 
    imp.reload(smoothdeform) 
    imp.reload(snap_offset)
    imp.reload(straighten) 
    imp.reload(to_ground)
    imp.reload(xoffsets) 
    imp.reload(xyspread) 
    imp.reload(unbevel) 
    
    imp.reload(origin_action)
    imp.reload(origin_active)
    imp.reload(origin_batch)
    imp.reload(origin_bbox)
    imp.reload(origin_bbox_modal)
    imp.reload(origin_center)
    imp.reload(origin_modal)
    imp.reload(origin_operators)
    imp.reload(origin_transform)
    imp.reload(origin_zero)

    imp.reload(np_point_align)
    imp.reload(np_point_distance)
    imp.reload(np_point_move)
    imp.reload(np_point_scale)
    imp.reload(np_roto_move)


else:
    
    from .ops_main import align_action                                  
    from .ops_main import align_mirror            
    from .ops_main import align_modifier   
    from .ops_main import align_orientation   
    from .ops_main import align_pencil
    from .ops_main import align_pivot        
    from .ops_main import align_snap_set         
    from .ops_main import align_snap_to                
    from .ops_main import align_transform     
    from .ops_main import align_widget  

    from .ops_auxiliary import advanced  
    from .ops_auxiliary import center_cursor  
    from .ops_auxiliary import con_rotation  
    from .ops_auxiliary import distribute
    from .ops_auxiliary import distribute_obj 
    from .ops_auxiliary import easylattice   
    from .ops_auxiliary import face_to_face   
    from .ops_auxiliary import oned_scripts  
    from .ops_auxiliary import snap_offset 
    from .ops_auxiliary import shrinksmooth
    from .ops_auxiliary import smoothdeform
    from .ops_auxiliary import straighten 
    from .ops_auxiliary import to_ground                                 
    from .ops_auxiliary import xoffsets          
    from .ops_auxiliary import xyspread          
    from .ops_auxiliary import unbevel          

    from .ops_origin import origin_action                
    from .ops_origin import origin_active                                      
    from .ops_origin import origin_batch                                      
    from .ops_origin import origin_bbox         
    from .ops_origin import origin_bbox_modal         
    from .ops_origin import origin_center 
    from .ops_origin import origin_modal 
    from .ops_origin import origin_operators                 
    from .ops_origin import origin_transform                    
    from .ops_origin import origin_zero                    

    from .ops_station import np_point_align           
    from .ops_station import np_point_distance   
    from .ops_station import np_point_move                   
    from .ops_station import np_point_scale           
    from .ops_station import np_roto_move           


    # LOAD MAPS #
    from .align_uimap   import *
    from .align_keymap  import *
    from .align_append  import *


# LOAD MODULS #
import bpy
from bpy import *
from bpy.props import*
import addon_utils

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# TOOLS REGISTRY #
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None




# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    # TAP PROPS #
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),  
               ('tools',      "Tools",      "Tools"),  
               ('header',     "Header",     "Header"),  
               ('view',       "NP",         "NP"),  
               ('url',        "URLs",       "URLs")),
               default='info')


    #----------------------------------------------------------------------------------------


    # PANEL LOCATION #           
    tab_location_align = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools',    'Tool Shelf',           'place panel in the tool shelf [T]'),
               ('ui',       'Property Shelf',       'place panel in the property shelf [N]'),
               ('props',    'Properties Data',      'place panel in the data properties tab'),
               ('off',      'Off',                  'hide panel')),
               default='tools', update = update_panel_position)

    tools_category_align = StringProperty(name = "TAB", description = "add name for a new category tab", default = 'Align', update = update_panel_position)

    #----------------------------------------------------------------------------------------


    # MENU PROPS #    
    tab_menu_align = EnumProperty(
        name = 'Align Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on',  'enable menu'),
               ('pie',  'Pie on',   'enable pie menu'),
               ('off',  'Menu off', 'disable menus')),
               default='menu', update = update_menu)

    tab_menu_view_relax = EnumProperty(
        name = 'Relax Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_relax)

    tab_menu_view_origin = EnumProperty(
        name = 'Origin Menu',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_origin)

    tab_origin_adv = bpy.props.BoolProperty(name="Advanced Origin Menu", description="show or hide tools in menu layout", default=True)    


               
    tab_menu_normal = EnumProperty(
        name = 'Translate Normal Menu',
        description = 'add normal translate menus to toolshelf [T] > tools > transform',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_submenu_normal)               


    tab_menu_machine = EnumProperty(
        name = 'MESHmachine',
        description = 'menu for 3d view',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_menu_machine)               

    tab_submenu_machine = EnumProperty(
        name = 'MESHmachine',
        description = 'menu for editmode special [W]',
        items=(('menu', 'Menu on', 'enable menu'),
               ('off', 'Menu off', 'disable menu')),
               default='off', update = update_submenu_machine)  

    #----------------------------------------------------------------------------------------


    # TOOLS PANEL #    
    tab_pivot = bpy.props.BoolProperty(name="Pivot", description="show or hide tools in panel layout", default=True)    
    tab_origin = bpy.props.BoolProperty(name="Origin", description="show or hide tools in panel layout", default=True)    
    tab_align_to = bpy.props.BoolProperty(name="Align to", description="show or hide tools in panel layout", default=True)    
    tab_zero_to = bpy.props.BoolProperty(name="Zero to", description="show or hide tools in panel layout", default=True)    
    tab_aligner = bpy.props.BoolProperty(name="Tools", description="show or hide tools in panel layout", default=True)    
    tab_station = bpy.props.BoolProperty(name="NP Station", description="show or hide tools in panel layout", default=True)    
    tab_interpolate = bpy.props.BoolProperty(name="Interpolate", description="show or hide tools in panel layout", default=True)    
    tab_mirror = bpy.props.BoolProperty(name="Mirror", description="show or hide tools in panel layout", default=True)    
    tab_automirror = bpy.props.BoolProperty(name="AutoMirror", description="show or hide tools in panel layout", default=True)    
    tab_looptools = bpy.props.BoolProperty(name="Looptools", description="show or hide tools in panel layout", default=True)    
    tab_relax = bpy.props.BoolProperty(name="Relax Mesh", description="show or hide tools in panel layout", default=True)    
    tab_edger = bpy.props.BoolProperty(name="Edge Align", description="show or hide tools in panel layout", default=True)    
    tab_space = bpy.props.BoolProperty(name="Space Align", description="show or hide tools in panel layout", default=True)    
    tab_machine = bpy.props.BoolProperty(name="MESHmachine", description="show or hide tools in panel layout", default=True)    

    # TOOLS MENU #    
    tab_pivot_menu = bpy.props.BoolProperty(name="Pivot", description="show or hide tools in panel layout", default=True)    
    tab_origin_menu = bpy.props.BoolProperty(name="Origin", description="show or hide tools in panel layout", default=True)    
    tab_align_to_menu = bpy.props.BoolProperty(name="Align to", description="show or hide tools in panel layout", default=True)    
    tab_zero_to_menu = bpy.props.BoolProperty(name="Zero to", description="show or hide tools in panel layout", default=True)    
    tab_aligner_menu = bpy.props.BoolProperty(name="Tools", description="show or hide tools in panel layout", default=True)    
    tab_station_menu = bpy.props.BoolProperty(name="NP Station", description="show or hide tools in panel layout", default=True)    
    tab_interpolate_menu = bpy.props.BoolProperty(name="Interpolate", description="show or hide tools in panel layout", default=True)    
    tab_mirror_menu = bpy.props.BoolProperty(name="Mirror", description="show or hide tools in panel layout", default=True)    
    tab_automirror_menu = bpy.props.BoolProperty(name="AutoMirror", description="show or hide tools in panel layout", default=True)    
    tab_tinycad_menu = bpy.props.BoolProperty(name="TinyCAD", description="show or hide tools in panel layout", default=True)    
    tab_looptools_menu = bpy.props.BoolProperty(name="Looptools", description="show or hide tools in panel layout", default=True)    
    tab_relax_menu = bpy.props.BoolProperty(name="Relax Mesh", description="show or hide tools in panel layout", default=True)    
    tab_edger_menu = bpy.props.BoolProperty(name="Edge Align", description="show or hide tools in panel layout", default=True)    
    tab_space_menu= bpy.props.BoolProperty(name="Mesh Align", description="show or hide tools in panel layout", default=True)    
    tab_machine_menu= bpy.props.BoolProperty(name="MESHmachine", description="show or hide tools in panel layout", default=True)    


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
            default=1,
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


    nppd_scale = bpy.props.FloatProperty(
            name = 'Scale',
            description = 'Distance multiplier (for example, for cm use 100)',
            default = 1,
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
        
    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Align!")  

            row.label(text="This is a collection of align tools for 3D View, UV Image-, Graph and Node Editor")   
            row.label(text="Location in 3D View: tool shelf [T], property Shelf [N], properties data and header line")   
            row.label(text="Location in UV Image-, Graph and Node Editor: [CTRL+D]")
            
            row.separator()
            
            row.label(text="Advanced: looptools and automirror can be added to the panel and menus.")
            row.label(text="Go to > addon preferences > tools > choose on or off.")
            row.label(text="Activation buttons appears if they are not already actively switched.")                        
            row.label(text="Save user settings for a permant use.")                        
            
            row.separator()

            row.label(text="Have Fun! :)")  


        # LOCATIONS #
        if self.prefs_tabs == 'location':
            box = layout.box().column(1) 
            
            row = box.row(1) 
            row.label("Location: ")
            
            box.separator()

            row = box.row(1) 
            row.prop(self, 'tab_location_align', expand=True)
            
            if self.tab_location_align == 'tools':

                box.separator()

                row = box.row(1) 
                row.prop(self, "tools_category_align")


        # TOOLS #
        if self.prefs_tabs == 'tools':
          
            box = layout.box().column(1)
            
            row = box.row()
            row.label("Panel Tools:", icon ="COLLAPSEMENU")   
            
            row = box.column_flow(2)

            row.prop(self, 'tab_origin')
            row.prop(self, 'tab_align_to')
            row.prop(self, 'tab_aligner')
            row.prop(self, 'tab_zero_to')
            row.prop(self, 'tab_station')
            row.prop(self, 'tab_interpolate')
            row.prop(self, 'tab_mirror')
            row.prop(self, 'tab_automirror')
            row.prop(self, 'tab_looptools')
            row.prop(self, 'tab_relax')
            row.prop(self, 'tab_edger')
            row.prop(self, 'tab_space')
            row.prop(self, 'tab_machine')

            box.separator()  
            box.separator()  
           
           
            row = box.row()
            row.label("Menu Tools:", icon ="COLLAPSEMENU")   
            
            row = box.column_flow(2)

            row.prop(self, 'tab_pivot_menu')
            row.prop(self, 'tab_origin_menu')
            row.prop(self, 'tab_align_to_menu')
            row.prop(self, 'tab_aligner_menu')
            row.prop(self, 'tab_zero_to_menu')
            row.prop(self, 'tab_station_menu')
            row.prop(self, 'tab_interpolate_menu')
            row.prop(self, 'tab_mirror_menu')
            row.prop(self, 'tab_automirror_menu')
            row.prop(self, 'tab_tinycad_menu')
            row.prop(self, 'tab_looptools_menu')
            row.prop(self, 'tab_relax_menu')
            row.prop(self, 'tab_edger_menu')
            row.prop(self, 'tab_space_menu')
            row.prop(self, 'tab_machine_menu')

            box.separator()         


   
        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Align Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: [SHIFT+Y] ")

            row = box.row(1)          
            row.prop(self, 'tab_menu_align', expand=True)
            
            if self.tab_menu_align == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")


            box.separator()  
            

            # ORIGIN #
            box = layout.box().column(1)
                         
            row = box.row(1)   
            row.label("Origin Menu: [CTRL+D] ", icon ="COLLAPSEMENU")       
            row.prop(self, 'tab_menu_view_origin', expand=True)
            
            if self.tab_menu_view_origin == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")
            else:
              
                box.separator()                 
                
                row = box.row(1)          
                row.label(" ", icon ="BLANK1")    
                row.prop(self, 'tab_origin_adv')                
                                    
        
            box.separator()  
          
            # RELAX #
            box = layout.box().column(1)
             
            row = box.row(1)         
            row.label("Relax Menu: [CTRL+SHIFT+W] ", icon ="COLLAPSEMENU")       
            row.prop(self, 'tab_menu_view_relax', expand=True)
            
            if self.tab_menu_view_relax == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")


            box.separator()

            # NORMALS #
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Normal Translate Menu:", icon ="COLLAPSEMENU")              
            row.prop(self, 'tab_menu_normal', expand=True)
            
            if self.tab_menu_normal == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! durably hidden with next reboot!", icon ="INFO")

            row = box.row(1)        
            row.label("Toolshelf [T] > Tools > Transform")   
       
            box.separator()   

            meshmaschine_addon = "MESHmachine" 
            state = addon_utils.check(meshmaschine_addon)
            if not state[0]:
                pass
            else:   

                # MESHmachine #
                box = layout.box().column(1)
                 
                row = box.row(1)         
                row.label("MESHmachine Menu: [SHIFT+X] ", icon ="COLLAPSEMENU")       
                row.prop(self, 'tab_menu_machine', expand=True)
                
                if self.tab_menu_machine == 'off':
                    
                    box.separator() 
                    
                    row = box.row(1) 
                    row.label(text="! durably hidden with next reboot!", icon ="INFO")

                box.separator()         
             
                row = box.row(1)
                row.label("Add to Special-Edit-Menu [W]")
                row.prop(self, 'tab_submenu_machine', expand=True)

            box.separator()
            box.separator()
           
            # TIP #
            row = layout.row(1)             
            row.label(text="! For key change you can go also to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. key: shift y", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Align_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  

            row = layout.row(1)             
            row.label(text="! Or edit the keymap script directly !", icon ="INFO")
            row.operator("tp_ops.keymap_align", text = 'Open KeyMap (Text Editor)')
            row.operator('wm.url_open', text = 'Type of Events (WEB)').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"
            
            box.separator()   


        # HEADER #
        if self.prefs_tabs == 'header':
            
            layout = self.layout
            
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Functions to Header are removed as separated addon :", icon ="INFO")    
            row.operator('wm.url_open', text = 'T+ Header').url = "https://github.com/mkbreuer/ToolPlus/2.79/Sets"



        # NP STATION #
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


        # WEB #
        if self.prefs_tabs == 'url':
            row = layout.row()
            row.label("List of Addon on Wiki Page")
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?409510-Addon-T-Align&p=3114519#post3114519"
            row.operator('wm.url_open', text = 'GitHub', icon = 'BLENDER').url = "https://github.com/mkbreuer/ToolPlus"



# PROPERTIES # 
class Dropdown_Align_Props(bpy.types.PropertyGroup):

    display_align_help = bpy.props.BoolProperty(name = "Help ", description = "open/close help", default = False) 
    display_mirror_auto = bpy.props.BoolProperty(name="AutoMirror", description="open / close", default=False)
    display_display = bpy.props.BoolProperty(name="Display", description="open / close", default=False)
    display_apply = bpy.props.BoolProperty(name="Apply", description="open / close", default=False)

    display_align_options = bpy.props.BoolProperty(name="Open / Close", description="open / close", default=False)
    display_axis_toggle = bpy.props.BoolProperty(name="Open / Close", description="open / close", default=False)
    display_snap_toggle = bpy.props.BoolProperty(name="Open / Close", description="open / close", default=False)
    display_station_toggle = bpy.props.BoolProperty(name="Open / Close", description="open / close", default=False)

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="open / close", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="open / close", default=False)
    display_origin_active = bpy.props.BoolProperty(name="Align to Active", description="align origin to active object", default=False)

    tp_axis_active = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"XYZ"  ,"04")],
               name = "Align to Active",
               default = "tp_x",    
               description = "zero target to choosen axis")

    tp_distance_active = bpy.props.EnumProperty(
        items=[("tp_min"    ,"Min"    ,"01"),
               ("tp_mid"    ,"Mid"    ,"02"),
               ("tp_max"    ,"Max"    ,"03")],
               name = "Align Distance",
               default = "tp_mid",    
               description = "align distance for origin")

    active_too = bpy.props.BoolProperty(name="Active too!",  description="align active origin too", default=False, options={'SKIP_SAVE'})    
    

    types_align =  [("tp_01"    ,"Panel"  ,"panel tools"  ,"" ,0),
                    ("tp_02"    ,"Menus"  ,"menu tools"   ,"" ,1), 
                    ("tp_03"    ,"KeyMap" ,"keymap    "   ,"" ,2)]                   
    bpy.types.Scene.tp_align = bpy.props.EnumProperty(name = " ", default = "tp_01", items = types_align)



# NP STATION #
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





# REGISTRY #

import traceback

def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
           
    update_panel_position(None, bpy.context)
    update_display_tools(None, bpy.context)

    update_menu(None, bpy.context) 
    update_menu_relax(None, bpy.context)
    update_menu_origin(None, bpy.context)
    update_menu_machine(None, bpy.context)

    update_submenu_normal(None, bpy.context)
    update_submenu_machine(None, bpy.context)

        
    # ALIGN #
    bpy.types.WindowManager.tp_collapse_align = bpy.props.PointerProperty(type = Dropdown_Align_Props)    
 
    # 1D SCRIPTS #
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

    # NP ROTO MOVE # 
    NP020RotoMove.define('OBJECT_OT_np_rm_get_context')
    NP020RotoMove.define('OBJECT_OT_np_rm_get_selection')
    NP020RotoMove.define('OBJECT_OT_np_rm_get_mouseloc')
    NP020RotoMove.define('OBJECT_OT_np_rm_add_helper')
    NP020RotoMove.define('OBJECT_OT_np_rm_prepare_context')
    NP020RotoMove.define('OBJECT_OT_np_rm_run_translate')
    NP020RotoMove.define('OBJECT_OT_np_rm_bgl_plane')
    NP020RotoMove.define('OBJECT_OT_np_rm_run_translate')
    NP020RotoMove.define('OBJECT_OT_np_rm_prepare_context')
    NP020RotoMove.define('OBJECT_OT_np_rm_run_rotate')
    NP020RotoMove.define('OBJECT_OT_np_rm_restore_context')

    # NP POINT MOVE #  
    NP020PointMove.define('OBJECT_OT_np_pm_get_context')
    NP020PointMove.define('OBJECT_OT_np_pm_get_selection')
    NP020PointMove.define('OBJECT_OT_np_pm_get_mouseloc')
    NP020PointMove.define('OBJECT_OT_np_pm_add_helper')
    NP020PointMove.define('OBJECT_OT_np_pm_prepare_context')
    for i in range(1, 3):
        NP020PointMove.define('OBJECT_OT_np_pm_run_translate')
    NP020PointMove.define('OBJECT_OT_np_pm_restore_context')


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
 
    # NP POINT ALIGN #
    NP020PointAlign.define('OBJECT_OT_np_pl_get_context')
    NP020PointAlign.define('OBJECT_OT_np_pl_get_selection')
    NP020PointAlign.define('OBJECT_OT_np_pl_get_mouseloc')
    NP020PointAlign.define('OBJECT_OT_np_pl_add_helper')
    NP020PointAlign.define('OBJECT_OT_np_pl_prepare_context')
    for i in range(1, 50):
        NP020PointAlign.define('OBJECT_OT_np_pl_run_translate')
    NP020PointAlign.define('OBJECT_OT_np_pl_align_selected')
    NP020PointAlign.define('OBJECT_OT_np_pl_restore_context')

    #NP NP POINT SCALE #
    NP020PointScale.define("OBJECT_OT_np_ps_get_context")
    NP020PointScale.define("OBJECT_OT_np_ps_get_selection")
    NP020PointScale.define("OBJECT_OT_np_ps_prepare_context")
    NP020PointScale.define("OBJECT_OT_np_ps_display_cage")
    NP020PointScale.define("OBJECT_OT_np_ps_prepare_context")
    NP020PointScale.define("OBJECT_OT_np_ps_run_resize")
    NP020PointScale.define("OBJECT_OT_np_ps_restore_context")

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Align_Manual)
    bpy.utils.register_manual_map(VIEW3D_TP_LoopTools_Manual)
    bpy.utils.register_manual_map(VIEW3D_TP_Machine_Manual)



def unregister():
    
    # 1D SCRIPTS #
    del bpy.types.WindowManager.paul_manager

    # ALIGN #
    del bpy.types.WindowManager.tp_collapse_align  

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Align_Manual)
    bpy.utils.unregister_manual_map(VIEW3D_TP_LoopTools_Manual)
    bpy.utils.unregister_manual_map(VIEW3D_TP_Machine_Manual)



if __name__ == "__main__":
    register()
        
        













