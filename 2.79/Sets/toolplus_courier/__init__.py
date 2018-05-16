# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2018 MKB
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
#

bl_info = {
    "name": "T+Courier",
    "author": "marvin.k.breuer (MKB)",
    "version": (1, 0, 1),
    "blender": (2, 7, 9),
    "location": "View3D",
    "description": "text draw on 3D viewport",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MANUAL #
from toolplus_courier.courier_manual   import (VIEW3D_TP_Courier_Manual)

# LOAD ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_courier'))

if "bpy" in locals():
    import imp

    imp.reload(courier_draw)
    imp.reload(courier_draw_mkb)
    imp.reload(courier_menu)

else:       
    from . import courier_draw
    from . import courier_draw_mkb
    from . import courier_menu
    

# LOAD MODULS #
import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup

from toolplus_courier.courier_keymap  import*

import rna_keymap_ui
def get_keymap_item(km, kmi_value):
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_value:
            return km_item
    return None

def draw_keymap_item(km, kmi, kc, layout):
    if kmi:
        layout.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, layout, 0)


# ADDON PREFERNECES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__

    # INFO LIST #
    prefs_tabs = EnumProperty(
        items=(('info',     "Info",     "Info"),
               ('keymap',   "Keymap",   "Keymap"), 
               ('url',      "URLs",     "URLs")),
               default='info')

    #----------------------------

    # LOCATIONS #          
    tab_location_courier = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool [T]',            'panel to shelf [T]'),
               ('ui',    'Property [N]',        'panel to property shelf [N]'),
               ('props', 'Properties: Scene',   'panel to propertise: scene'),
               ('off',   'off',                 'panel off')),
               default='tools', update = update_panel_courier)

    tools_category_courier = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_courier)
  

    #------------------------------

    # 3D VIEW MENU # 
    tab_menu_courier = EnumProperty(
        name = '3d View Menu',
        description = 'location switch',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off',  'Menu off','disable menu for 3d view')),
               default='off', update = update_menu_courier)

    #------------------------------

    # HEADER #
    tab_header_courier = EnumProperty(
        name = 'Add to Header', 
        description = 'function to header',
        items=(('add',    'Add',    'enable tools in header'), 
               ('remove', 'Remove', 'disable tools in header')), 
        default='remove', update = update_to_header)

    #----------------------------

    # SPECIAL #
    tab_special_courier = EnumProperty(
        name = 'Add to Special Menu', 
        description = 'function to header',
        items=(('add',    'Add',    'enable tools in header'), 
               ('remove', 'Remove', 'disable tools in header')), 
        default='remove', update = update_to_special)

    #----------------------------
   
    # TEXT: UI SWITCH #

    tab_button_layout = BoolProperty(name= 'Layout Switch', description = 'toggle layout between display buttons and preferences', default=False)

    tab_title_or_sublines = EnumProperty(
        name = 'Layout Switch', 
        description = 'switch between title or block layout',
        items=(('title',   'Title',  'layout for title'), 
               ('subline', 'Block',  'layout for blocks')), 
        default='title')
   
    tab_icon_switch = BoolProperty(name= 'Icon Switch', description = 'property for icon switch', default=False)
    
    dodraw = bpy.props.EnumProperty(
      items = [("ZERO",  "T0", "Text 0", "", 0),
               ("ONE",   "T1", "Text 1", "", 1),
               ("TWO",   "T2", "Text 2", "", 2),
               ("THREE", "T3", "Text 3", "", 3), 
               ("FOUR",  "T4", "Text 4", "", 4), 
               ("FIVE",  "T5", "Text 5", "", 5), 
               ("SIX",   "T6", "Text 6", "", 6), 
               ("SEVEN", "T7", "Text 7", "", 7),
               ("EMPTY", " ",  "hide ",  "RESTRICT_VIEW_ON", 8)], 
               name = "Draw Title",
               default = "ZERO") 
 

    subline_draw = bpy.props.EnumProperty(
      items = [("ZERO_LINE",  "L0", "Line 0", "", 0),
               ("ONE_LINE",   "L1", "Line 1", "", 1),
               ("TWO_LINE",   "L2", "Line 2", "", 2),
               ("THREE_LINE", "L3", "Line 3", "", 3), 
               ("FOUR_LINE",  "L4", "Line 4", "", 4), 
               ("FIVE_LINE",  "L5", "Line 5", "", 5), 
               ("SIX_LINE",   "L6", "Line 6", "", 6), 
               ("SEVEN_LINE", "L7", "Line 7", "", 7),
               ("EMPTY_LINE", " ",  "hide ",  "RESTRICT_VIEW_ON", 8)], 
               name = "Draw SubRows",
               default = "ZERO_LINE")


    #----------------------------
  
    # TEXT: DROPSHADOW  #

    text_shadow = BoolProperty(name= 'DropShadow', description = 'show/hide dropshadow for text', default=False)
    text_shadow_color = FloatVectorProperty(name="DS C", default=(0.0, 0.0, 0), min=0, max=1, subtype='COLOR', description = 'color for dropshadow')
    text_shadow_alpha = FloatProperty(name="DS A", default=1, min=0, max=1, description = 'alpha for dropshadow')     
    text_shadow_x = IntProperty(name="DS X", default= 2, min=-5, max=5, description = 'offset x for dropshadow')     
    text_shadow_y = IntProperty(name="DS Y", default=-2, min=-5, max=5, description = 'offset y for dropshadow')

    #----------------------------
   
    # TEXT: ALIGN #
    
    tab_center       = bpy.props.EnumProperty(items = [("free", "Left", "align block left / considered [T] shelf", "", 1), ("middle", "Middle", "align to center / considered [T] and [N] shelfes", "", 2)], name = "Align Block", default = "middle")
    tab_center_mkb = bpy.props.EnumProperty(items = [("free", "Left", "align block left / considered [T] shelf", "", 1), ("middle", "Middle", "align to center / considered [T] and [N] shelfes", "", 2)], name = "Align Block", default = "middle")

    tab_center_left_mkb = BoolProperty(name= 'Center', description = 'align to center / align rows left / considered [T] and [N] shelfes', default=False)

    #----------------------------

    # TEXT: TITLE #   

    tab_permanent = BoolProperty(name= 'Draw Variations', description = 'run permanet til undo [CTRL+Z] or cancle with [ESC] or [RIGHTMOUSE]', default=False)   

    tab_scal_link = BoolProperty(name= '(Un)Link Scale', description = '(un)link > use same or different scale', default=False)
    tab_pos_link = BoolProperty(name= '(Un)Link Position', description = '(un)link > use same or different position', default=False)

    tab_font_external = BoolProperty(name= 'External Fonts', description = 'use internal fonts instate of imported fonts', default=False)
    tab_font_pathes = BoolProperty(name= 'Fonts Pathes', description = 'shows path field for each text', default=False)
    tab_font_unit = BoolProperty(name= '(Un)Link Font', description = '(un)link > use same or different font', default=False)

    filepath_all = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_0 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_1 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_2 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_3 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_4 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_5 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_6 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_7 = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")

    tab_color_link = BoolProperty(name= '(Un)Link Color', description = '(un)link > use same or different color', default=False)
    tab_color_unit = BoolProperty(name= 'Unit Color', description = 'use same color for all text', default=False)

    # TEXT ALL #
    text_color = FloatVectorProperty(name="",  default=(0.5, 1, 1),  min=0, max=1, subtype='COLOR')     
    text_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_pos_x = IntProperty(name="Pos X", description = 'x axis for all lines', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_pos_y = IntProperty(name="Pos Y", description = 'y axis for all lines', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
   
    # TEXT 0 #     
    text_0_color = FloatVectorProperty(name="",  default=(1, 0, 0),  min=0, max=1, subtype='COLOR') 
    text_0_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_0_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_0_pos_x = IntProperty(name="Pos X", description = 'x axis for line 0', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_0_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 0', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_0_text =  bpy.props.StringProperty(name='', default="...T+Courier ...")

    # TEXT 1 #     
    text_1_color = FloatVectorProperty(name="",  default=(0.9, 0, 1),  min=0, max=1, subtype='COLOR') 
    text_1_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_1_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_1_pos_x = IntProperty(name="Pos X", description = 'x axis for line 1', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_1_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 1', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_1_text =  bpy.props.StringProperty(name='', default="1. Sub Title")

    # TEXT 2 #     
    text_2_color = FloatVectorProperty(name="",  default=(0, 0, 1),  min=0, max=1, subtype='COLOR') 
    text_2_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_2_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_2_pos_x = IntProperty(name="Pos X", description = 'x axis for line 2', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_2_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 2', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_2_text =  bpy.props.StringProperty(name='', default="2. Sub Title")

    # TEXT 3 #     
    text_3_color = FloatVectorProperty(name="",  default=(0, 1, 1),  min=0, max=1, subtype='COLOR') 
    text_3_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_3_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_3_pos_x = IntProperty(name="Pos X", description = 'x axis for line 3', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_3_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 3', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_3_text =  bpy.props.StringProperty(name='', default="3. Sub Title")

    # TEXT 4 #     
    text_4_color = FloatVectorProperty(name="",  default=(0, 1, 0),  min=0, max=1, subtype='COLOR') 
    text_4_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_4_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_4_pos_x = IntProperty(name="Pos X", description = 'x axis for line 4', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_4_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 4', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_4_text =  bpy.props.StringProperty(name='', default="4. Sub Title")

    # TEXT 5 #     
    text_5_color = FloatVectorProperty(name="",  default=(1, 1, 0),  min=0, max=1, subtype='COLOR') 
    text_5_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_5_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_5_pos_x = IntProperty(name="Pos X", description = 'x axis for line 5', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_5_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 5', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_5_text =  bpy.props.StringProperty(name='', default="5. Sub Title")

    # TEXT 6 #     
    text_6_color = FloatVectorProperty(name="",  default=(1, 0.5, 0),  min=0, max=1, subtype='COLOR') 
    text_6_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_6_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_6_pos_x = IntProperty(name="Pos X", description = 'x axis for line 6', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_6_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 6', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_6_text =  bpy.props.StringProperty(name='', default="6. Sub Title")

    # TEXT 7 #     
    text_7_color = FloatVectorProperty(name="",  default=(1, 0.5, 1),  min=0, max=1, subtype='COLOR') 
    text_7_width_title = IntProperty(name="Width", default=50, min=20, max=100)
    text_7_height_title = IntProperty(name="Height", default=50, min=20, max=500)
    text_7_pos_x = IntProperty(name="Pos X", description = 'x axis for line 7', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_7_pos_y = IntProperty(name="Pos Y", description = 'y axis for line 7', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_7_text =  bpy.props.StringProperty(name='', default="7. Sub Title")

    #----------------------------

    # TEXT: SUB 0 #   
   
    tab_permanent_mkb = BoolProperty(name= 'Draw Variations', description = 'run permanet til undo [CTRL+Z] or cancle with [ESC] or [RIGHTMOUSE]', default=False)   
    tab_view_mkb = BoolProperty(name= 'Refresh Draw', description = 'on-off-draw-refresh: to avoid clicking into the viewport', default=False)   
                 
    tab_scal_link_mkb = BoolProperty(name= '(Un)Link Scale', description = '(un)link > use same or different font size', default=False)
    tab_array_link_mkb = BoolProperty(name= '(Un)Link Array', description = '(un)link > use same or different position', default=False)
    tab_offset_link_mkb = BoolProperty(name= '(Un)Link Offset', description = '(un)link > use same or different offset', default=False)

    tab_font_external_mkb = BoolProperty(name= 'External Fonts', description = 'switch external to internal', default=False)
    tab_font_pathes_mkb = BoolProperty(name= 'Fonts Pathes', description = 'shows path field for each text', default=False)
    tab_font_text_mkb = BoolProperty(name= 'Text Field', description = 'show text field for each line', default=False)
    tab_font_unit_mkb = BoolProperty(name= '(Un)Link Font', description = 'use same or different font', default=False)

    filepath_all_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_0_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_1_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_2_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_3_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_4_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_5_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_6_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")
    filepath_7_mkb = StringProperty(name="File Path", description="Filepath used for importing .ttf files", maxlen= 1024, default= "C:\Windows\Fonts\calibri.ttf")

    tab_color_link_mkb = BoolProperty(name= '(Un)Link Color', description = '(un)link > use same or different color', default=False)
    tab_color_unit_mkb = BoolProperty(name= 'Unit Color', description = 'use same color for all text', default=False)

    text_l0_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l1_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l2_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l3_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l4_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l5_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l6_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
    text_l7_mkb = BoolProperty(name= '', description = 'toggle subline text', default=True)
 
    # TEXT ALL #
    text_color_mkb = FloatVectorProperty(name="",  default=(0.5, 1, 1),  min=0, max=1, subtype='COLOR')     
    text_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for all lines', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for all lines', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for all lines', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for all lines', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_spread_y_mkb = IntProperty(name="Spread Y", description = 'spread lines on y axis', subtype='PERCENTAGE', default=50, min=1, max=100)
    text_all_x_mkb = IntProperty(name="All X", description = 'x axis for all lines', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_all_y_mkb = IntProperty(name="All Y", description = 'y axis for all lines', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
 
    # TEXT 0 #     
    text_0_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Title")
    text_0_color_mkb = FloatVectorProperty(name="",  default=(1, 0, 0),  min=0, max=1, subtype='COLOR') 
    text_0_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_0_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_0_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 0', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_0_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 0', subtype='PERCENTAGE', default=20, min=-1300, max=1300)
    text_0_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 0', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_0_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 0', subtype='PERCENTAGE', default=20, min=-1300, max=1300)

    # TEXT 1 #     
    text_1_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 1") 
    text_1_color_mkb = FloatVectorProperty(name="",  default=(0.9, 0, 1),  min=0, max=1, subtype='COLOR') 
    text_1_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_1_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_1_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 1', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_1_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 1', subtype='PERCENTAGE', default=15, min=-1300, max=1300)
    text_1_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 1', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_1_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 1', subtype='PERCENTAGE', default=15, min=-1300, max=1300)

    # TEXT 2 #     
    text_2_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 2")
    text_2_color_mkb = FloatVectorProperty(name="",  default=(0, 0, 1),  min=0, max=1, subtype='COLOR') 
    text_2_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_2_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_2_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 2', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_2_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 2', subtype='PERCENTAGE', default=10, min=-1300, max=1300)
    text_2_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 2', subtype='PERCENTAGE', default=0, min=-1000, max=1000) 
    text_2_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 2', subtype='PERCENTAGE', default=10, min=-1300, max=1300)

    # TEXT 3 #     
    text_3_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 3")
    text_3_color_mkb = FloatVectorProperty(name="",  default=(0, 1, 1),  min=0, max=1, subtype='COLOR') 
    text_3_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_3_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_3_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 3', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_3_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 3', subtype='PERCENTAGE', default=5, min=-1300, max=1300)
    text_3_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 3', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_3_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 3', subtype='PERCENTAGE', default=5, min=-1300, max=1300)

    # TEXT 4 #     
    text_4_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 4")
    text_4_color_mkb = FloatVectorProperty(name="",  default=(0, 1, 0),  min=0, max=1, subtype='COLOR') 
    text_4_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_4_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_4_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 4', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_4_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 4', subtype='PERCENTAGE', default=0, min=-1300, max=1300)
    text_4_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 4', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_4_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 4', subtype='PERCENTAGE', default=0, min=-1300, max=1300)

    # TEXT 5 #     
    text_5_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 5")
    text_5_color_mkb = FloatVectorProperty(name="",  default=(1, 1, 0),  min=0, max=1, subtype='COLOR') 
    text_5_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_5_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_5_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 5', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_5_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 5', subtype='PERCENTAGE', default=-5, min=-1300, max=1300)
    text_5_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 5', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_5_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 5', subtype='PERCENTAGE', default=-0, min=-1300, max=1300)

    # TEXT 6 #     
    text_6_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 6")
    text_6_color_mkb = FloatVectorProperty(name="",  default=(1, 0.5, 0),  min=0, max=1, subtype='COLOR') 
    text_6_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_6_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_6_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 6', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_6_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 6', subtype='PERCENTAGE', default=-10, min=-1300, max=1300)
    text_6_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 6', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_6_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 6', subtype='PERCENTAGE', default=-10, min=-1300, max=1300)


    # TEXT 7 #     
    text_7_text_mkb =  bpy.props.StringProperty(name='', default="Block 0 - Line 7")
    text_7_color_mkb = FloatVectorProperty(name="",  default=(1, 0.5, 1),  min=0, max=1, subtype='COLOR') 
    text_7_width_mkb = IntProperty(name="Width", default=50, min=20, max=100)
    text_7_height_mkb = IntProperty(name="Height", default=50, min=20, max=500)
    text_7_array_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 7', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_7_array_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 7', subtype='PERCENTAGE', default=-15, min=-1300, max=1300)
    text_7_offset_x_mkb = IntProperty(name="Pos X", description = 'x axis for line 7', subtype='PERCENTAGE', default=0, min=-1000, max=1000)
    text_7_offset_y_mkb = IntProperty(name="Pos Y", description = 'y axis for line 7', subtype='PERCENTAGE', default=-15, min=-1300, max=1300)


    #----------------------------

    
    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout
                 
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        col = layout.column(1)       
        if self.prefs_tabs == 'info':

            box = col.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+Courier!") 
            row.separator()           
            row.label(text="This addon allows to draw text to the 3D viewport as an real time modal operator with", icon = "LAYER_USED")                                                         
            row.separator()                                            
            row.label(text="Each text block can shown separately or togehter", icon = "LAYER_USED")                               
            row.label(text="The rows can be revealed one by one", icon = "LAYER_USED")                               
            row.label(text="Fonts and colors are variable.", icon = "LAYER_USED")                                                             
            row.separator()                                             
            row.label(text="All addon preferences are available in the panel or property menu", icon = "LAYER_USED")                               
            row.label(text="After creating a new layout, just save user settings.", icon = "LAYER_USED")                               
            row.label(text="This make it possible to use the adjustments as new preferences.", icon = "LAYER_USED")                                                                                         
            row.separator()    
            row.label(text="The modal can run in two different ways:", icon = "LAYER_USED")                               
            row.label(text="1. cancle: finish draw with [ESC] or [RIGHTMOUSE]", icon = "LAYER_USED")                               
            row.label(text="2. permanent: finish draw with undo [CTRL+Z]", icon = "LAYER_USED")                                                       
            row.separator()   
            row.label(text="Tip: Make adjustments from outside!", icon = "LAYER_USED")                               
            row.label(text="Go to: Info Header > Windows > Duplicate Window or press [CTRL+ALT+W]", icon = "LAYER_USED")                               
            row.label(text="Close everything until only the panel is left.", icon = "LAYER_USED")                                                       
            row.label(text="Move it aside or to another monitor.", icon = "LAYER_USED")                                                       
            row.label(text="This allows to reveal the text from a invisible panel.", icon = "LAYER_USED")                                                       
            row.separator()             
            row.separator()             
            row.label(text="> At least Have Fun! ;)")  


        # KEYMAP #
        if self.prefs_tabs == 'keymap':
            
            box = col.box().column(1)
             
            box.separator() 

            row = box.row(1) 
            row.label("Location: Panel")
            
            row = box.row(1)
            row.prop(self, 'tab_location_courier', expand=True)        
            
            box.separator()

            row = box.row(1)            
            if self.tab_location_courier == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_courier")

            box.separator()
            box = col.box().column(1)
            box.separator() 
             
            row = box.row(1)  
            row.label("Batch Menu", icon ="COLLAPSEMENU")          
            row.prop(self, 'tab_menu_courier', expand=True)

            box.separator() 
            box.separator() 

            row = box.row(1) 

            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            km = kc.keymaps['3D View']
            kmi = get_keymap_item(km, 'tp_ops.tp_courier_batch')
            draw_keymap_item(km, kmi, kc, row) 

            box.separator()
            box = col.box().column(1)
            box.separator() 
             
            row = box.row(1)  
            row.label("To Special Menu", icon ="COLLAPSEMENU")          
            row.prop(self, 'tab_special_courier', expand=True)

            box.separator()
            box = col.box().column(1)
            box.separator() 
             
            row = box.row(1)  
            row.label("To Header", icon ="COLLAPSEMENU")          
            row.prop(self, 'tab_header_courier', expand=True)

            box.separator() 
            box.separator() 


        # WEB #
        if self.prefs_tabs == 'url':
           
            box = col.box().column(1)
            
            row = box.row(1)
            row.operator('wm.url_open', text = 'ToolPlus on GitHub', icon = 'HELP').url = "https://github.com/mkbreuer/ToolPlus"



import os, sys
import subprocess
class TP_COURIER_Restart_Blender(bpy.types.Operator):
    #"(saidenka) meta-androcto",
    bl_idname = "wm.restart_blender_courier"
    bl_label = "Reboot Blender"
    bl_description = "Blender Restart"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        py = os.path.join(os.path.dirname(__file__), "console_toggle.py")
        filepath = bpy.data.filepath
        if (filepath != ""):
            subprocess.Popen([sys.argv[0], filepath, '-P', py])
        else:
            subprocess.Popen([sys.argv[0],'-P', py])
        bpy.ops.wm.quit_blender()
        return {'FINISHED'}


class VIEW3D_TP_RMB_context:
    bl_label = "RMB Context Menu"
    def draw(self, context):
        pass

def add_rmb_menu():
    if not hasattr(bpy.types, "WM_MT_button_context"):
        tp = type("WM_MT_button_context", (VIEW3D_TP_RMB_context, bpy.types.Menu), {})
        bpy.utils.register_class(tp)

    bpy.types.WM_MT_button_context.append(rmb_context_menu)


def rmb_context_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator('wm.url_open', text = 'T+Courier Wiki', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus/wiki/TP-Courier"


# REGISTRY #
import traceback

def register():
    add_rmb_menu()  
      
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_menu_courier(None, bpy.context)
    update_panel_courier(None, bpy.context)
    update_to_header(None, bpy.context)
    update_to_special(None, bpy.context)

    # MANUAL #
    bpy.utils.register_manual_map(VIEW3D_TP_Courier_Manual)


def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    if hasattr(bpy.types, "WM_MT_button_context"):
        bpy.types.WM_MT_button_context.remove(rmb_context_menu)

    # MANUAL #
    bpy.utils.unregister_manual_map(VIEW3D_TP_Courier_Manual)
    
if __name__ == "__main__":
    register()
        
        





















