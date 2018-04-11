# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "T+ Header",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 1),
    "blender": (2, 79, 0),
    "location": "3D View > Header",
    "description": "tools for 3d view header",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus/wiki/TP-Header",
    "category": "ToolPlus",
}

# LOAD MANUAL #
from toolplus_header.header_manual   import (VIEW3D_TP_Header_Manual)

# LOAD PROPS #
from toolplus_header.station.np_point_align  import (NPPLRestoreContext)

# LOAD CUSTOM ICONS #
from . icons.icons    import load_icons
from . icons.icons    import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_header'))

if "bpy" in locals():
    import imp
     
    imp.reload(header_center)                                     
    imp.reload(header_display)                                     
    imp.reload(header_ruler)         
    imp.reload(header_shading)                                
    imp.reload(header_snap)                                
    imp.reload(header_text)                                

    imp.reload(header_point_align)
    imp.reload(header_point_distance)
    imp.reload(header_point_move)
    imp.reload(header_point_scale)
    imp.reload(header_roto_move)                              

    imp.reload(header_snapline)                              

    imp.reload(origin_action)
    imp.reload(origin_active)
    imp.reload(origin_align)
    imp.reload(origin_bbox)
    imp.reload(origin_bbox_modal)
    imp.reload(origin_center)
    imp.reload(origin_distribute)
    imp.reload(origin_modal)
    imp.reload(origin_operators)
    imp.reload(origin_transform)
    imp.reload(origin_zero)

    print("Reloaded file")


else:

    from .operator import  header_center 
    from .operator import  header_display 
    from .operator import  header_ruler 
    from .operator import  header_shading         
    from .operator import  header_snap         
    from .operator import  header_text         

    from .station import np_point_align           
    from .station import np_point_distance   
    from .station import np_point_move                   
    from .station import np_point_scale           
    from .station import np_roto_move          

    from . import header_snapline          
   
    from .origin import origin_action         
    from .origin import origin_active        
    from .origin import origin_align                     
    from .origin import origin_bbox               
    from .origin import origin_bbox_modal               
    from .origin import origin_center                 
    from .origin import origin_distribute                 
    from .origin import origin_modal         
    from .origin import origin_operators                 
    from .origin import origin_transform                 
    from .origin import origin_zero  

    print("Imported file")



# LOAD MODULS #
import bpy
from bpy import *
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup

# LOAD MAPS #
from toolplus_header.header_append  import*


# UPDATE TOOLS #
def update_tools_header(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None    




# ADDON PREFERNECES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__

    #Tab Prop
    prefs_tabs = EnumProperty(
        items=(('info',     "Info",       "Info"),
               ('menus',    "Append",     "Append"),
               ('tools',    "Tools",      "Tools"),
               ('snapline', "Snapline",   "Snapline"), 
               ('station',  "NP Station", "NP Station"),
               ('url',      "URLs",       "URLs")),
               default='info')


    #------------------------------


    # MENU #
    tab_menu_header = EnumProperty(
        name = 'Header Menu',
        description = 'enable or disable menu for Header',
        items=(('add', 'Menu on', 'enable menu for Header'),
               ('remove', 'Menu off', 'disable menu for Header')),
        default='add', update = update_menu_header)

    # SUBMENUS #    
    tab_menu_append_view = EnumProperty(
        name = 'Append to View',
        description = 'menu for header view menu',
        items=(('add',    'To Header View Menu',  'add menus to default menus'),
               ('remove', 'Remove Tools', 'remove menus from default menus')),
        default='remove', update = update_submenu_header_view)               

    tab_menu_append_select = EnumProperty(
        name = 'Append to Select',
        description = 'menu for header select menu',
        items=(('add',    'To Header Select Menu', 'add menus to default menus'),
               ('remove', 'Remove Tools', 'remove menus from default menus')),
        default='remove', update = update_submenu_header_select)   

    tab_menu_append_add = EnumProperty(
        name = 'Append to Add',
        description = 'menu for header add menu',
        items=(('add',    'To Header Add Menu', 'add menus to default menus'),
               ('remove', 'Remove Tools', 'remove menus from default menus')),
        default='remove', update = update_submenu_header_add)   

    tab_menu_append_objects = EnumProperty(
        name = 'Append to Object',
        description = 'menu for header object menu',
        items=(('add',    'To Header Objects Menu', 'add menus to default menus'),
               ('remove', 'Remove Tools', 'remove menus from default menus')),
        default='remove', update = update_submenu_header_objects)   


    #----------------------------

    # TOOLS UI #    
    expand_panel_tools = bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)    

    tab_display_options = EnumProperty(
        name = 'Options', 
        description = 'on / off',
        items=(('on',  'Show Options', 'enable option menu in header'), 
               ('off', 'Hide Options', 'disable option menu in header')), 
        default='on', update = update_tools_header)

    tab_display_buttons = EnumProperty(
        name = 'Buttons or Menus', 
        description = 'on = only butttons / off = use menus',
        items=(('on',  'Use Buttons', 'enable tools in header'), 
               ('off', 'Use Menus', 'disable tools in header')), 
        default='off', update = update_tools_header)

    tab_display_bottom = EnumProperty(
        name = 'Top or Bottom', 
        description = 'use menus for bottom or top header',
        items=(('bottom', 'Type Bottom', 'use menus for bottom header'), 
               ('top',    'Type Top',    'use menus for top header')), 
        default='bottom', update = update_tools_header)

    tab_display_name = EnumProperty(
        name = 'Name & Icon Toggle', 
        description = 'on / off',
        items=(('both_id', 'Show Name & Icon', 'keep names and icons visible in header menus'), 
               ('icon_id', 'Show only Icons',   'disable icons in header menus'), 
               ('text_id', 'Show only Names', 'disable names in header menus')), 
        default='both_id', update = update_tools_header)


    # TOOLS #       
    tab_display_ruler = EnumProperty(
        name = 'Ruler Display', 
        description = 'on / off',
        items=(('on', 'Ruler on', 'enable tools in header'), 
               ('off', 'Ruler off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_objects = EnumProperty(
        name = 'Object Display', 
        description = 'on / off',
        items=(('on', 'Obj-Display on', 'enable tools in header'), 
               ('off', 'Obj-Display off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_snap = EnumProperty(
        name = 'SnapTo Display', 
        description = 'on / off',
        items=(('on', 'SnapTo on', 'enable tools in header'), 
               ('off', 'SnapTo off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_snapset = EnumProperty(
        name = 'SnapSet Display', 
        description = 'on / off',
        items=(('on', 'SnapSet on', 'enable tools in header'), 
               ('off','SnapSet off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_shading = EnumProperty(
        name = 'Shading Tools', 
        description = 'on / off',
        items=(('on', 'Shading on', 'enable tools in header'), 
               ('off', 'Shading off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_history = EnumProperty(
        name = 'History Tools', 
        description = 'on / off',
        items=(('on', 'History on', 'enable tools in header'), 
               ('off', 'History off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_save = EnumProperty(
        name = 'Save Tools', 
        description = 'on / off',
        items=(('on', 'Save on', 'enable tools in header'), 
               ('off', 'Save off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_view = EnumProperty(
        name = 'View Tools', 
        description = 'on / off',
        items=(('on', 'View on', 'enable tools in header'), 
               ('off', 'View off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_window = EnumProperty(
        name = 'Window Tools', 
        description = 'on / off',
        items=(('on', 'Window on', 'enable tools in header'), 
               ('off', 'Window off', 'disable tools in header')), 
        default='on', update = update_tools_header)


    #----------------------------


    # CUSTOM #
    
    tab_display_custom = EnumProperty(
        name = 'Custom Menu', 
        description = 'on / off',
        items=(('on', 'Custom on', 'enable custom menu in header'), 
               ('off', 'Custom off', 'disable custom menu in header')), 
        default='off', update = update_tools_header)


    #----------------------------


    # ORIGIN #

    tab_display_origin = EnumProperty(
        name = 'Origin', 
        description = 'on / off',
        items=(('on', 'Origin on', 'enable tools in header'), 
               ('off', 'Origin off', 'disable tools in header')), 
        default='on', update = update_tools_header)

    tab_display_advanced = EnumProperty(
        name = 'Align Advanced', 
        description = 'on / off',
        items=(('on', 'Advanced on', 'enable tools in header'), 
               ('off', 'Advanced off', 'disable tools in header')), 
        default='on', update = update_tools_header)



    #----------------------------


    # SNAPLINE #

    tab_display_snapline = EnumProperty(
        name = 'SnapLine', 
        description = 'on / off',
        items=(('on', 'SnapLine on', 'enable tools in header'), 
               ('off', 'SnapLine off', 'disable tools in header')), 
        default='off', update = update_tools_header)


    expand_snap_settings = bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)      

    intersect = bpy.props.BoolProperty(name="Intersect", description="intersects created line with the existing edges, even if the lines do not intersect.", default=True)
    create_new_obj = bpy.props.BoolProperty(name="Create a new object", description="If have not a active object, or the active object is not in edit mode, it creates a new object.", default=False)
    create_face = bpy.props.BoolProperty(name="Create faces", description="Create faces defined by enclosed edges.", default=False)
    outer_verts = bpy.props.BoolProperty(name="Snap to outer vertices", description="The vertices of the objects are not activated also snapped.", default=True)      
    increments_grid = bpy.props.BoolProperty(name="Increments of Grid", description="Snap to increments of grid", default=False)
    incremental = bpy.props.FloatProperty(name="Incremental", description="Snap in defined increments", default=0, min=0, step=1, precision=3)
    relative_scale = bpy.props.FloatProperty(name="Relative Scale", description="Value that divides the global scale.", default=1, min=0, step=1, precision=3)

    out_color = bpy.props.FloatVectorProperty(name="OUT", default=(0.0, 0.0, 0.0, 0.5), size=4, subtype="COLOR", min=0, max=1)
    face_color = bpy.props.FloatVectorProperty(name="FACE", default=(1.0, 0.8, 0.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    edge_color = bpy.props.FloatVectorProperty(name="EDGE", default=(0.0, 0.8, 1.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    vert_color = bpy.props.FloatVectorProperty(name="VERT", default=(1.0, 0.5, 0.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    center_color = bpy.props.FloatVectorProperty(name="CENTER", default=(1.0, 0.0, 1.0, 1.0), size=4, subtype="COLOR", min=0, max=1)
    perpendicular_color = bpy.props.FloatVectorProperty(name="PERPENDICULAR", default=(0.1, 0.5, 0.5, 1.0), size=4, subtype="COLOR", min=0, max=1)
    constrain_shift_color = bpy.props.FloatVectorProperty(name="SHIFT CONSTRAIN", default=(0.8, 0.5, 0.4, 1.0), size=4, subtype="COLOR", min=0, max=1)


    #------------------------------


    # NP STATION #

    tab_display_station = EnumProperty(name = 'NP Station', description = 'on / off',
                  items=(('on', 'NP Station on', 'enable tools in header'), 
                         ('off', 'NP Station off', 'disable tools in header')), 
                         default='off', update = update_tools_header)

    tab_display_point_distance = EnumProperty(name = 'NP Station', description = 'on / off',
                  items=(('on', 'NP Distance on', 'enable tools in header'), 
                         ('off', 'NP Distance off', 'disable tools in header')), 
                         default='on', update = update_tools_header)

    tab_display_point_move = EnumProperty(name = 'NP Station', description = 'on / off',
                  items=(('on', 'NP Move on', 'enable tools in header'), 
                         ('off', 'NP Move off', 'disable tools in header')), 
                         default='on', update = update_tools_header)

    tab_display_roto_move = EnumProperty(name = 'NP Station', description = 'on / off',
                  items=(('on', 'NP Rotation on', 'enable tools in header'), 
                         ('off', 'NP Rotation off', 'disable tools in header')), 
                         default='on', update = update_tools_header)

    tab_display_point_scale = EnumProperty(name = 'NP Station', description = 'on / off',
                  items=(('on', 'NP Scale on', 'enable tools in header'), 
                         ('off', 'NP Scale off', 'disable tools in header')), 
                         default='on', update = update_tools_header)

    tab_display_point_align = EnumProperty(name = 'NP Station', description = 'on / off',
                  items=(('on', 'NP Align on', 'enable tools in header'), 
                         ('off', 'NP Align off', 'disable tools in header')), 
                         default='on', update = update_tools_header)


    #------------------------------

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
 

    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Header !")  
            row.label(text="> This addon append functions to the 3d view header as menus or button tools")   
            row.label(text="> The menu look can be adjusted directly in the addon preferences or in header")                      
            row.label(text="> Gear Button: open the options for text or icons in the menus")  
            row.label(text="> Save user setting to apply the changes durably.")  
            row.label(text="> Have Fun! ;)")  


        # APPEND #
        if self.prefs_tabs == 'menus':
          
            box = layout.box().column(1)
            
            row = box.column(1)  
            row.label("Append to Header", icon ="COLLAPSEMENU") 

            row = box.row(1)          
            row.prop(self, 'tab_menu_header', expand=True)
                
            box.separator() 

            if self.tab_menu_header == 'remove':
                row = box.row(1) 
                row.label(text="! The menu hidden with next reboot durably!", icon ="INFO")
           
            box.separator()
            box.separator() 
            box.separator()

            row = box.row(1)  
            row.label("(Template) Append to Header Menus ", icon ="COLLAPSEMENU") 
            row.operator("tp_ops.append_map_header", text = 'Open Map to add Functions (Text Editor)')

            box.separator() 
            
            row = box.row()          
            row.prop(self, 'tab_menu_append_view', expand=True)
            row.prop(self, 'tab_menu_append_select', expand=True)

            box.separator() 
            
            row = box.row() 
            row.prop(self, 'tab_menu_append_add', expand=True)
            row.prop(self, 'tab_menu_append_objects', expand=True)
            
            box.separator() 
            box.separator()



        # TOOLS #
        if self.prefs_tabs == 'tools':
      
            box = layout.box().column(1)
          
            box.separator() 
            box.separator()             
           
            row = box.column_flow(4)  
            row.label("Header UI", icon ="COLLAPSEMENU") 

            box.separator() 
            box.separator() 

            row = box.row().column_flow(4)          
            #row.prop(self, 'tab_display_options',  expand=True)
            row.prop(self, 'tab_display_buttons',  expand=True)
            #row.prop(self, 'tab_display_bottom',  expand=True)
            row.prop(self, 'tab_display_name',  expand=True)

            box.separator() 

            display_button_menu = context.user_preferences.addons[__name__].preferences.tab_display_buttons
            if display_button_menu == 'on':  

                box.separator() 
                
                row = box.column_flow(4)  
                row.label("Buttons Type", icon ="COLLAPSEMENU") 

                box.separator() 
                box.separator() 

                row = box.row().column_flow(4)   
                row.prop(self, 'tab_display_ruler',  expand=True)
                row.prop(self, 'tab_display_objects',  expand=True)
                row.prop(self, 'tab_display_snap', expand=True)
                row.prop(self, 'tab_display_snapset', expand=True)
                row.prop(self, 'tab_display_shading', expand=True)
                row.prop(self, 'tab_display_origin', expand=True)
                row.prop(self, 'tab_display_advanced', expand=True)

                box.separator() 
                box.separator() 
                
                row = box.row().column_flow(4)   
                row.prop(self, 'tab_display_station',  expand=True)
                row.prop(self, 'tab_display_point_distance',  expand=True)
                row.prop(self, 'tab_display_point_move',  expand=True)
                row.prop(self, 'tab_display_roto_move',  expand=True)
                row.prop(self, 'tab_display_point_scale',  expand=True)
                row.prop(self, 'tab_display_point_align',  expand=True)
                row.prop(self, 'tab_display_snapline', expand=True)

                box.separator() 
                box.separator() 
                
                row = box.row().column_flow(4)    
                row.prop(self, 'tab_display_history', expand=True)
                row.prop(self, 'tab_display_save', expand=True)
                row.prop(self, 'tab_display_view', expand=True)
                row.prop(self, 'tab_display_window', expand=True)

                box.separator() 
                box.separator() 
 
            else:

                box.separator() 
                
                row = box.column_flow(4)  
                row.label("Menu Type", icon ="COLLAPSEMENU") 

                box.separator() 
                box.separator() 

                row = box.row().column_flow(4)              
                row.prop(self, 'tab_display_custom',  expand=True)
                row.prop(self, 'tab_display_ruler',  expand=True)
                row.prop(self, 'tab_display_snap', expand=True)
                row.prop(self, 'tab_display_snapset', expand=True)
                row.prop(self, 'tab_display_origin', expand=True)
                row.prop(self, 'tab_display_advanced', expand=True)
                row.prop(self, 'tab_display_station', expand=True)
                row.prop(self, 'tab_display_objects',  expand=True)
                row.prop(self, 'tab_display_shading', expand=True)

          
                box.separator() 
                box.separator() 


      
        # SNAPLINE #
        if self.prefs_tabs == 'snapline':

            box = layout.box().column(1)

            row = box.row()
            row.label("Snapline Colors", icon ="LINE_DATA")    
            row.prop(self, "out_color")

            split = box.split()

            col = split.column()
            col.prop(self, "constrain_shift_color")
        
            col = split.column()
            col.prop(self, "face_color")
          
            col = split.column()
            col.prop(self, "edge_color")        
          
            col = row.column()

            col = split.column()
            col.prop(self, "vert_color")
          
            col = split.column()
            col.prop(self, "center_color")
          
            col = split.column()
            col.prop(self, "perpendicular_color")

            row = box.row()
           
            col.separator()
           
            col = row.column()
            
            col.prop(self, "incremental")
            col.prop(self, "increments_grid")
         
            if self.increments_grid:
                col.prop(self, "relative_scale")

            col.prop(self, "outer_verts")
            row.separator()

            col = row.column()
            col.label(text="Line Tool:")
            col.prop(self, "intersect")
            col.prop(self, "create_face")
            col.prop(self, "create_new_obj")



        # NP STATION #
        if self.prefs_tabs == 'station':
            
            layout = self.layout
            
            box = layout.box().column(1)
           
            box.separator()             
           
            row = box.column(1)  
            row.label("ABC Point Align / GRS Snap Transform Tools", icon ="COLLAPSEMENU")   

            box.separator()
            
            row = box.row(1)  
            row.label(text='Main color scheme:')
            row.prop(self, "np_col_scheme")

            box.separator()
           
            row = box.row(1)  
            row.label(text='Size of the numerics:')
            row.prop(self, "np_size_num")
           
            box.separator()          
          
            row = box.row(1)  
            row.label(text='Unit scale for distance:')
            row.prop(self, "np_scale_dist")
           
            box.separator()           
          
            row = box.row(1)  
            row.label(text='Unit suffix for distance:')
            row.prop(self, "np_suffix_dist")
          
            box.separator()
                     
            row = box.row(1)  
            row.label(text='Mouse badge:')
            row.prop(self, "np_display_badge")
           
            if self.np_display_badge == True:
                row.prop(self, "np_size_badge")

            box.separator()

           
            box = layout.box().column(1)

            box.separator()
                         
            row = box.column(1)  
            row.label("Point Distance Settings:", icon ="COLLAPSEMENU")   

            box.separator()            
 
           
            row = box.row(1)
            row.prop(self, "nppd_scale")
            row.prop(self, "nppd_suffix")          
            row.prop(self, "nppd_step")
            row.prop(self, "nppd_info") 

            box.separator()
           
            row = box.row(1) 
            row.prop(self, "nppd_badge")         
            row.prop(self, "nppd_hold")
            row.prop(self, "nppd_gold")
            row.prop(self, "nppd_clip")


            box.separator()

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
          
            box.separator()

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
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus/wiki"
            #row.operator('wm.url_open', text = 'Blenderartist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?346610-Addon-Function-to-Header&highlight="



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


# ORIGIN PROPs # 
class Dropdown_Origin_ToolProps(bpy.types.PropertyGroup):

    display_origin_editbox = bpy.props.BoolProperty(name="Origin BBox", description="align origin to the boundtyp: box (4x vertice / 12x edge / 6x face)", default=False)
    display_origin_bbox = bpy.props.BoolProperty(name="Origin BBox", description="align origin to the boundtyp: box (4x vertice / 12x edge / 6x face)", default=False)
    display_origin_zero = bpy.props.BoolProperty(name="Zero Axis", description="align origin, object or cursor to an axis", default=False)
    display_origin_zero_edm = bpy.props.BoolProperty(name="Zero Axis", description="align only origin, object or cursor to an axis", default=False)
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



# HEADER PROPS #
class Dropdown_Header_Props(bpy.types.PropertyGroup):

    display_tools = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = True) 


    
# REGISTRY #
import traceback

def register():
 
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_menu_header(None, bpy.context)
    update_tools_header(None, bpy.context)
    update_submenu_header_view(None, bpy.context)
    update_submenu_header_select(None, bpy.context)
    update_submenu_header_add(None, bpy.context)
    update_submenu_header_objects(None, bpy.context)

    # PROPS #
    bpy.types.WindowManager.tp_props_header = bpy.props.PointerProperty(type = Dropdown_Header_Props)
    bpy.types.WindowManager.tp_props_origin = bpy.props.PointerProperty(type = Dropdown_Origin_ToolProps)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Header_Manual)

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



def unregister():  

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # PROPS #
    del bpy.types.WindowManager.tp_props_header
    del bpy.types.WindowManager.tp_props_origin

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Header_Manual)    

if __name__ == "__main__":
    register()
        
        


