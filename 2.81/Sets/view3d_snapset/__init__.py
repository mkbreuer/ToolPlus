# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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
    "name": "SnapSet",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 2, 7),
    "blender": (2, 81, 0),
    "location": "3D View > Sidebar [N], Menu [SHIFT+W], Special Menu [W], Shortcut [F], Header and SnapSettings",
    "description": "full customizable buttons for snapping task",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "category": "3D View",
}


# LOAD MODULES #
import bpy
from bpy.props import *

# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

import bpy.utils.previews

# ADDON CHECK #
import addon_utils   
from . ui_utils import addon_exists


# LOAD CUSTOM ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons

from .ot_custom     import *
from .ot_keymap     import *
from .ot_modal      import *
from .ot_targets    import *
from .ot_cursor     import *

# LOAD UI # 
from .ui_editor     import *
from .ui_keymap     import *
from .ui_menu       import *
from .ui_menu_pie   import *
from .ui_panel      import *
from .ui_snapping   import *
from .ui_utils      import *


importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())

# PANEL TO CONTAINING THE TOOLS #
class VIEW3D_PT_snapset_panel_ui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = "SnapSet"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_snapset_ui(context, layout)


# UPDATE TAB CATEGORY FOR PANEL IN THE TOOLSHELF #
panels = (
        VIEW3D_PT_snapset_panel_ui,
        )

def update_panel(self, context):
    message = "Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            panel.bl_category = context.preferences.addons[__name__].preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



def update_snapset(self, context):

    try:     
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.remove(draw_snapset_item_special)  

        bpy.types.VIEW3D_PT_snapping.remove(draw_snapset_snapping)   
        
        bpy.types.VIEW3D_MT_editor_menus.remove(draw_snapset_item_editor) 

    except:
        pass
    
    addon_prefs = context.preferences.addons[__name__].preferences    
  

    # SPECIAL MENU [W] #  
    if addon_prefs.toggle_special_menu == True:  

        if addon_prefs.toggle_special_type == 'append':
           
            # ADD TO MENUS: TOP #
            bpy.types.VIEW3D_MT_object_context_menu.append(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_edit_curve_context_menu.append(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_armature_context_menu.append(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_particle_context_menu.append(draw_snapset_item_special)  

        if addon_prefs.toggle_special_type == 'prepend':

            # ADD TO MENUS: BOTTOM #
            bpy.types.VIEW3D_MT_object_context_menu.prepend(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.prepend(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_edit_curve_context_menu.prepend(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_armature_context_menu.prepend(draw_snapset_item_special)  
            bpy.types.VIEW3D_MT_particle_context_menu.prepend(draw_snapset_item_special)  

    if addon_prefs.toggle_special_menu == False:  
     
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.remove(draw_snapset_item_special)  


    # SNAPPING SETTING #  
    if addon_prefs.toggle_snapping_menu == True:
        bpy.types.VIEW3D_PT_snapping.prepend(draw_snapset_snapping)

    if addon_prefs.toggle_snapping_menu == False:
        bpy.types.VIEW3D_PT_snapping.remove(draw_snapset_snapping)


    # EDITOR MENUS #    
    if addon_prefs.toggle_editor_menu == True:  

        if addon_prefs.toggle_editor_type == 'append':
           
            # ADD TO MENUS: TOP #
            if addon_prefs.toggle_view_type == 'editor': 
                bpy.types.VIEW3D_MT_editor_menus.prepend(draw_snapset_item_editor) 
            else:
                #bpy.types.VIEW3D_HT_tool_header.prepend(draw_snapset_item_editor) 
                #bpy.types.VIEW3D_HT_header.prepend(draw_snapset_item_editor) 
                bpy.utils.register_class(VIEW3D_HT_snapset_header)


        if addon_prefs.toggle_editor_type == 'prepend':

            # ADD TO MENUS: BOTTOM #
            if addon_prefs.toggle_view_type == 'editor': 
                bpy.types.VIEW3D_MT_editor_menus.append(draw_snapset_item_editor) 
            else:
                #bpy.types.VIEW3D_HT_tool_header.append(draw_snapset_item_editor) 
                #bpy.types.VIEW3D_HT_header.append(draw_snapset_item_editor) 
                bpy.utils.register_class(VIEW3D_HT_snapset_header)


    if addon_prefs.toggle_editor_menu == False:  

        if addon_prefs.toggle_view_type == 'editor': 
            bpy.types.VIEW3D_MT_editor_menus.remove(draw_snapset_item_editor)  
        else:
            #bpy.types.VIEW3D_HT_tool_header.remove(draw_snapset_item_editor)  
            #bpy.types.VIEW3D_HT_header.remove(draw_snapset_item_editor)  
            bpy.utils.unregister_class(VIEW3D_HT_snapset_header)






# UPDATE TOOLS # not needed if we used bool properties #
def update_snapset_tools(self, context):

    try:
        return True
    except:
        pass

    if context.preferences.addons[__name__].preferences.toggle_display_tools == 'on':
        return True

    if context.preferences.addons[__name__].preferences.toggle_display_tools == 'off':
        return None    


# ADDON PREFERENCES PANEL #
class Addon_Preferences_Snapset(bpy.types.AddonPreferences):
    bl_idname = __name__
    
    # SIDEBAR LOCATION # 
    category : StringProperty(
              name="Tab Category",
              description="category name for the tab in the sidebar",
              default="Item",
              update=update_panel
              )

    # INFO LIST #
    prefs_tabs : EnumProperty(
        items=(('info',    "Info",    "Info"),
               ('panel',   "Panel",   "Panel"),
               ('menus',   "Menus",   "Menus"),
               ('buttons', "Buttons", "Buttons")),
        default='info')


    #------------------------------
   
    # AUXILIARY #

    toggle_addon_align_tools : BoolProperty(name= 'Align Tools', description = 'on/off', default=True)  
    toggle_align_tools_compact : BoolProperty(name= 'Toogle Title', description = 'on/off', default=False)  

    toggle_addon_alignmesh: BoolProperty(name= 'Align Mesh', description = 'on/off', default=True)  
    toggle_alignmesh_compact : BoolProperty(name= 'Toogle Title', description = 'on/off', default=False)  
  
    threshold : bpy.props.FloatProperty(name="Threshold",  description="threshold: angle value to select linked face", default=0.0174533, min=0.0174533, max=3.14159, subtype='ANGLE')
   
    mesh_select_mode : bpy.props.EnumProperty(
      items = [("vertices", "Vertex", "enable vertex selection", 1),
               ("edges",    "Edge",   "enable edge selection"  , 2), 
               ("faces",    "Face",   "enable face selection"  , 3)], 
               name = "Mesh Select Mode",
               default = "vertices",
               description="type of mesh select mode when finish")
               
    toggle_addon_looptools : BoolProperty(name= 'Looptools', description = 'on/off', default=True)  
    toggle_looptools_menu_type : BoolProperty(name= 'Toggle Menu/Panel', description = 'on/off', default=False)  


    #----------------------------


    # LAYOUT SCALE #
    
    ui_scale_x : FloatProperty(name="Scale X", description="scale layout space for menus", default=1.0, min=1.0, max=2, precision=2)
    ui_scale_y : FloatProperty(name="Scale Y", description="scale layout space for menus", default=1.2, min=1.0, max=2, precision=2)

    toggle_layout_type : BoolProperty(name="Layout Type", description="switch layout type", default=False)   
   
    # PANEL #          
    toggle_display_buttons_pl : EnumProperty(
        name = 'Buttons or Menus', 
        description = 'on = only butttons / off = use menus',
        items=(('off', 'Menus',   'enable tools in header'), 
               ('on',  'Buttons', 'disable tools in header')), 
        default='on', update = update_snapset_tools)

    toggle_display_name_pl : EnumProperty(
        name = 'Name & Icon Toggle', 
        description = 'on / off',
        items=(('both_id', 'Named', 'keep names and icons visible in header menus'), 
               ('icon_id', 'Icons',   'disable icons in header menus')), 
        default='both_id', update = update_snapset_tools)

    ui_scale_y_panel : FloatProperty(name="Scale Y", description="scale layout space for menus", default=1.2, min=1.0, max=2, precision=2)


    #------------------------------

    # MENU #

    toggle_keymap_menus : BoolProperty(name="Toggle", description="enable or disable keymenus for 3D View", default=False, update = update_snapset_menu)   

    toggle_keymap_type : EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Context Menu', 'enable menu for 3D View'),
               ('pie',    'Pie Menu',  'enable pie for 3D View')),
        default='menu', update = update_snapset_menu)

    hotkey_menu : StringProperty(name = 'Key', default="W", description = 'change hotkey / only capital letters allowed') 
    hotkey_menu_ctrl : BoolProperty(name= 'use Ctrl', description = 'enable / disable', default=False) 
    hotkey_menu_alt : BoolProperty(name= 'use Alt', description = 'enable / disable', default=False) 
    hotkey_menu_shift : BoolProperty(name= 'use Shift', description = 'enable / disable', default=True) 

    tpc_use_grid_pie : BoolProperty(name= 'Snap Grid', description = 'botton in menu', default=True)   
    tpc_use_place_pie : BoolProperty(name= 'Snap Place', description = 'botton in menu', default=True)   
    tpc_use_retopo_pie : BoolProperty(name= 'Snap Retopo', description = 'botton in menu', default=True)   
    tpc_use_cursor_pie : BoolProperty(name= 'Snap Cursor', description = 'botton in menu', default=True)   
    tpc_use_closest_pie : BoolProperty(name= 'Snap Closest', description = 'botton in menu', default=True)   
    tpc_use_active_pie : BoolProperty(name= 'Snap Active', description = 'botton in menu', default=True)   
    tpc_use_center_pie : BoolProperty(name= 'Snap MidPoint', description = 'botton in menu', default=True)   
    tpc_use_perpendic_pie : BoolProperty(name= 'Snap Perpendic', description = 'botton in menu', default=True)   
    tpc_use_custom_pie : BoolProperty(name= 'Snap Custom', description = 'botton in menu', default=True)   

    tpc_use_grid_modal_pie : BoolProperty(name= 'Grid Modal*', description = 'botton in menu', default=True)   
    tpc_use_place_modal_pie : BoolProperty(name= 'Place Modal*', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal_pie : BoolProperty(name= 'Retopo Modal*', description = 'botton in menu', default=True)   
    tpc_use_center_modal_pie : BoolProperty(name= 'MidPoint Modal*', description = 'botton in menu', default=True)   
    tpc_use_perpendic_modal_pie : BoolProperty(name= 'Perpendic Modal*', description = 'botton in menu', default=True)   
    tpc_use_custom_modal_pie : BoolProperty(name= 'Custom Modal*', description = 'botton in menu', default=True)   

    tpc_use_settings_pie : BoolProperty(name= 'Settings', description = 'botton in panel', default=True)   

    ui_scale_x_b1 : FloatProperty(name="Scale X", description="scale box in pie menu", default=1.10, min=0.00, max=2.00, precision=2)
    ui_scale_x_b2 : FloatProperty(name="Scale X", description="scale box in pie menu", default=1.02, min=0.00, max=2.00, precision=2)
    ui_scale_x_b3 : FloatProperty(name="Scale X", description="scale box in pie menu", default=1.10, min=0.00, max=2.00, precision=2)
    ui_scale_x_b4 : FloatProperty(name="Scale X", description="scale box in pie menu", default=0.65, min=0.00, max=2.00, precision=2)
    ui_scale_x_b5 : FloatProperty(name="Scale X", description="scale box in pie menu", default=0.65, min=0.00, max=2.00, precision=2)
    ui_scale_x_b6 : FloatProperty(name="Scale X", description="scale box in pie menu", default=0.65, min=0.00, max=2.00, precision=2)
    ui_scale_x_b7 : FloatProperty(name="Scale X", description="scale box in pie menu", default=1.10, min=0.00, max=2.00, precision=2)
    ui_scale_x_b8 : FloatProperty(name="Scale X", description="scale box in pie menu", default=1.10, min=0.00, max=2.00, precision=2)

    ui_scale_y_b1 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b2 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b3 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b4 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b5 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b6 : FloatProperty(name="Scale y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b7 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)
    ui_scale_y_b8 : FloatProperty(name="Scale Y", description="scale box in pie menu", default=1.00, min=0.00, max=2.00, precision=2)


    #------------------------------

    # EDITOR / HEADER #    

    toggle_editor_menu : BoolProperty(name="Toggle", description="enable or disable submenu", default=False, update = update_snapset)   

    toggle_view_type : EnumProperty(
        name = '3D View Type',
        description = 'different layout types',
        items=(('editor',  'Editor',  'add functions to editor menus'),
               ('header',  'Header',  'add functions to header menus')),
        default='editor') 

    toggle_editor_type : EnumProperty(
        name = 'Menu Location',
        description = 'menu location in editor header row',
        items=(('prepend', 'On Top',    'add menus to default special menus'),
               ('append',  'To Bottom', 'add menus to default special menus')),
        default='prepend', update = update_snapset)               

    toggle_editor_layout : EnumProperty(
        name = 'Layout Type',
        description = 'different layout types',
        items=(('menu',    'Context Menu', 'enable menu'),
               ('panel',   'Panel',        'enable panel'),
               ('buttons', 'Buttons',      'enable buttons')),
        default='menu') 

    toggle_editor_menu_name : EnumProperty(
        name = 'Menu Layout',
        description = 'different layout types',
        items=(('icon',   'Icon only', 'show only icon'),
               ('namend', 'Name only', 'show only menu name'),
               ('both',   'Use Both',  'show icon and menu name')),
        default='namend') 

    toggle_editor_separator_prepend : BoolProperty(name="Separator L", description="on / off", default=False)   
    factor_separator_prepend : FloatProperty(name="Factor", description="scale separator", default=1.00, min=0.00, max=100.00, precision=2)

    toggle_editor_separator_append : BoolProperty(name="Separator R", description="on / off", default=False)   
    factor_separator_append  : FloatProperty(name="Factor", description="scale separator", default=1.00, min=0.00, max=100.00, precision=2)

    toggle_editor_layout_scale_x : BoolProperty(name="Use X Scale", description="on / off", default=False)       
    ui_scale_x_editor : FloatProperty(name="Scale X", description="scale layout", default=1.00, min=0.50, max=2.00, precision=2)

    toggle_editor_layout_scale_y : BoolProperty(name="Use Y Scale", description="on / off", default=False)
    ui_scale_y_editor : FloatProperty(name="Scale Y", description="scale layout", default=1.00, min=1.00, max=1.30, precision=2)

    row_align : BoolProperty(name="Keep Buttons separated", description="on / off", default=True)
 
    tpc_use_grid_editor : BoolProperty(name= 'Snap Grid', description = 'botton in menu', default=True)   
    tpc_use_place_editor : BoolProperty(name= 'Snap Place', description = 'botton in menu', default=True)   
    tpc_use_retopo_editor : BoolProperty(name= 'Snap Retopo', description = 'botton in menu', default=True)   
    tpc_use_cursor_editor : BoolProperty(name= 'Snap Cursor', description = 'botton in menu', default=True)   
    tpc_use_closest_editor : BoolProperty(name= 'Snap Closest', description = 'botton in menu', default=True)   
    tpc_use_active_editor : BoolProperty(name= 'Snap Active', description = 'botton in menu', default=True)   
    tpc_use_center_editor : BoolProperty(name= 'Snap MidPoint', description = 'botton in menu', default=True)   
    tpc_use_perpendic_editor : BoolProperty(name= 'Snap Perpendic', description = 'botton in menu', default=True)   
    tpc_use_custom_editor : BoolProperty(name= 'Snap Custom', description = 'botton in menu', default=True)   

    tpc_use_grid_modal_editor : BoolProperty(name= 'Grid Modal*', description = 'botton in menu', default=True)   
    tpc_use_place_modal_editor : BoolProperty(name= 'Place Modal*', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal_editor : BoolProperty(name= 'Retopo Modal*', description = 'botton in menu', default=True)   
    tpc_use_center_modal_editor : BoolProperty(name= 'MidPoint Modal*', description = 'botton in menu', default=True)   
    tpc_use_perpendic_modal_editor : BoolProperty(name= 'Perpendic Modal*', description = 'botton in menu', default=True)   
    tpc_use_custom_modal_editor : BoolProperty(name= 'Custom Modal*', description = 'botton in menu', default=True)   


    #------------------------------

    # SPECIAL MENU [W] #    

    toggle_special_menu : BoolProperty(name="Toggle", description="enable or disable submenu", default=False, update = update_snapset)   
    ui_scale_y_special : FloatProperty(name="Scale Y", description="scale layout space for menus", default=1.2, min=1.0, max=2, precision=2)

    toggle_special_type : EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('prepend', 'On Top',    'add menus to default special menus'),
               ('append',  'To Bottom', 'add menus to default special menus')),
        default='prepend', update = update_snapset)               

    toggle_special_name : EnumProperty(
        name = 'Menu Layout',
        description = 'different layout types',
        items=(('namend', 'Name only', 'show only menu name'),
               ('both',   'Use Both',  'show icon and menu name')),
        default='namend') 


    toggle_special_type_layout : EnumProperty(
        name = '3D View Menu',
        description = 'different layout types',
        items=(('column', 'Column 1', 'use 1 column'),
               ('flow',   'Column 2', 'use 2 columns'),
               ('switch', 'Switch',   'switch between permanent and modal')),
        default='column') 

    toggle_special_separator : BoolProperty(name="Toggle Menu Separator", description="on / off", default=True)   
    toggle_special_icon : BoolProperty(name="Toggle Menu Icon", description="on / off", default=False)   
    row_align_special : BoolProperty(name="Keep Buttons separated", description="on / off", default=True)
    
    tpc_use_grid_special : BoolProperty(name= 'Snap Grid', description = 'botton in menu', default=True)   
    tpc_use_place_special : BoolProperty(name= 'Snap Place', description = 'botton in menu', default=True)   
    tpc_use_retopo_special : BoolProperty(name= 'Snap Retopo', description = 'botton in menu', default=True)   
    tpc_use_cursor_special : BoolProperty(name= 'Snap Cursor', description = 'botton in menu', default=True)   
    tpc_use_closest_special : BoolProperty(name= 'Snap Closest', description = 'botton in menu', default=True)   
    tpc_use_active_special : BoolProperty(name= 'Snap Active', description = 'botton in menu', default=True)   
    tpc_use_center_special : BoolProperty(name= 'Snap MidPoint', description = 'botton in menu', default=True)   
    tpc_use_perpendic_special : BoolProperty(name= 'Snap Perpendic', description = 'botton in menu', default=True)   

    tpc_use_separator_modal_special : BoolProperty(name= 'Separator', description = 'separator line in menu', default=True)   
    tpc_use_separator_settings_special : BoolProperty(name= 'Separator', description = 'separator line in menu', default=True)   

    tpc_use_grid_modal_special : BoolProperty(name= 'Grid Modal*', description = 'botton in menu', default=True)   
    tpc_use_place_modal_special : BoolProperty(name= 'Place Modal*', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal_special : BoolProperty(name= 'Retopo Modal*', description = 'botton in menu', default=True)   
    tpc_use_center_modal_special : BoolProperty(name= 'MidPoint Modal*', description = 'botton in menu', default=True)   
    tpc_use_perpendic_modal_special : BoolProperty(name= 'Perpendic Modal*', description = 'botton in menu', default=True)   
    tpc_use_custom_modal_special : BoolProperty(name= 'Custom Modal*', description = 'botton in menu', default=True)   

    tpc_use_settings_special : BoolProperty(name= 'Settings', description = 'botton in panel', default=True)   


    #----------------------------

    # SNAPPING #
    
    toggle_snapping_menu : BoolProperty(name="Toggle", description="enable or disable submenu", default=False, update = update_snapset)      
    ui_scale_y_snapping : FloatProperty(name="Scale Y", description="scale layout space for menus", default=1.2, min=1.0, max=2, precision=2)
    
    toggle_snapping_type : EnumProperty(
        name = '3D View Menu',
        description = 'different layout types',
        items=(('menu',    'Context Menu', 'enable menu'),
               ('buttons', 'Buttons',      'enable named buttons'),
               ('icons',   'Icons',        'enable icon buttons')),
        default='buttons') 

    toggle_snapping_type_layout : EnumProperty(
        name = '3D View Menu',
        description = 'different layout types',
        items=(('column', 'Column 1', 'enable 1 column'),
               ('flow',   'Column 2', 'enable 2 columns'),
               ('row',    'Row 1',    'enable 1 row'),
               ('rows',   'Row 2',    'enable 2 rows')),
        default='row') 
        
    tpc_use_grid_snapping : BoolProperty(name= 'Snap Grid', description = 'botton in menu', default=True)   
    tpc_use_place_snapping : BoolProperty(name= 'Snap Place', description = 'botton in menu', default=True)   
    tpc_use_retopo_snapping : BoolProperty(name= 'Snap Retopo', description = 'botton in menu', default=True)   
    tpc_use_cursor_snapping : BoolProperty(name= 'Snap Cursor', description = 'botton in menu', default=True)   
    tpc_use_closest_snapping : BoolProperty(name= 'Snap Closest', description = 'botton in menu', default=True)   
    tpc_use_active_snapping : BoolProperty(name= 'Snap Active', description = 'botton in menu', default=True)   
    tpc_use_center_snapping : BoolProperty(name= 'Snap Center', description = 'botton in menu', default=True)   
    tpc_use_perpendic_snapping : BoolProperty(name= 'Snap Perpendic', description = 'botton in menu', default=True)   
    tpc_use_custom_snapping : BoolProperty(name= 'Snap Custom', description = 'botton in menu', default=True)   

    tpc_use_grid_modal_snapping : BoolProperty(name= 'Grid Modal*', description = 'botton in menu', default=True)   
    tpc_use_place_modal_snapping : BoolProperty(name= 'Place Modal*', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal_snapping : BoolProperty(name= 'Retopo Modal*', description = 'botton in menu', default=True)   
    tpc_use_center_modal_snapping : BoolProperty(name= 'MidPoint Modal*', description = 'botton in menu', default=True)   
    tpc_use_perpendic_modal_snapping : BoolProperty(name= 'Perpendic Modal*', description = 'botton in menu', default=True)   
    tpc_use_custom_modal_snapping : BoolProperty(name= 'Custom Modal*', description = 'botton in menu', default=True)   

    tpc_use_settings_snapping : BoolProperty(name= 'Settings', description = 'botton in panel', default=True)   

    row_align_snapping_hor : BoolProperty(name="Keep Buttons separated", description="on / off", default=True)

    #----------------------------

    # CUSTOM BUTTONS #

    toggle_button_type : EnumProperty(
        name = 'Button Menu',
        description = 'choose settings for the buttons',
        items=(('button_a', 'Button A', 'button settings'),
               ('button_b', 'Button B', 'button settings'),
               ('button_c', 'Button C', 'button settings'),
               ('button_d', 'Button D', 'button settings'),
               ('button_e', 'Button E', 'button settings'),
               ('button_f', 'Button F', 'button settings'),
               ('button_g', 'Button G', 'button settings'),
               ('button_h', 'Button H', 'button settings'),
               ('button_m', 'Custom M', 'button settings')),
        default='button_a')

    tpc_use_grid : BoolProperty(name= 'Snap Grid', description = 'botton in menu', default=True)   
    tpc_use_place : BoolProperty(name= 'Snap Place', description = 'botton in menu', default=True)   
    tpc_use_retopo : BoolProperty(name= 'Snap Retopo', description = 'botton in menu', default=True)   
    tpc_use_cursor : BoolProperty(name= 'Snap Cursor', description = 'botton in menu', default=True)   
    tpc_use_closest : BoolProperty(name= 'Snap Closest', description = 'botton in menu', default=True)   
    tpc_use_active : BoolProperty(name= 'Snap Active', description = 'botton in menu', default=True)   
    tpc_use_center : BoolProperty(name= 'Snap Center', description = 'botton in menu', default=True)   
    tpc_use_perpendic : BoolProperty(name= 'Snap Perpendic', description = 'botton in menu', default=True)   
    tpc_use_custom : BoolProperty(name= 'Snap Custom', description = 'botton in menu', default=True)   

    tpc_use_grid_modal : BoolProperty(name= 'Grid Modal*', description = 'botton in menu', default=True)   
    tpc_use_place_modal : BoolProperty(name= 'Place Modal*', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal : BoolProperty(name= 'Retopo Modal*', description = 'botton in menu', default=True)   
    tpc_use_center_modal : BoolProperty(name= 'MidPoint Modal*', description = 'botton in menu', default=True)   
    tpc_use_perpendic_modal : BoolProperty(name= 'Perpendic Modal*', description = 'botton in menu', default=True)   
    tpc_use_custom_modal : BoolProperty(name= 'Custom Modal*', description = 'botton in menu', default=True)   

    tpc_use_grid_modal_panel : BoolProperty(name= 'Grid Modal*', description = 'botton in panel', default=True)   
    tpc_use_place_modal_panel : BoolProperty(name= 'Place Modal*', description = 'botton in panel', default=True)   
    tpc_use_retopo_modal_panel : BoolProperty(name= 'Retopo Modal*', description = 'botton in panel', default=True) 
    tpc_use_center_modal_panel : BoolProperty(name= 'MidPoint Modal*', description = 'botton in panel', default=True)   
    tpc_use_perpendic_modal_panel : BoolProperty(name= 'Perpendic Modal*', description = 'botton in panel', default=True)   
    tpc_use_custom_modal_panel : BoolProperty(name= 'Custom Modal*', description = 'botton in panel', default=True)   

    toggle_snapset_add_tools : BoolProperty(name= 'Append hotkey to the preference keymap', description = 'append to keymap', default=False)   

    tpc_use_snap : BoolProperty(name= 'Toggle permanent Snap', description = 'toggle snap on or off', default=True)    
    tpc_use_emposs : BoolProperty(name= 'Toggle transparent for button backround pie menu.', description = 'toggle emboss for active function', default=False)    


    #----------------------------
    
    # BUTTON A = GRID #

    name_bta : StringProperty(default="Grid") 
    icon_bta : StringProperty(default="BLENDER") 
    use_internal_icon_bta : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_bta_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='BOUNDING_BOX_CENTER') 

    prop_bta_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_bta_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='INCREMENT') 

    prop_bta_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 

    prop_bta_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=True)  
    prop_bta_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_bta_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_bta_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_bta_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_bta_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_bta_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_bta_scale : BoolProperty(name= 'Scale', description = '', default=False)  


    #----------------------------
    

    # BUTTON B = PLACE #
    name_btb : StringProperty(default="Place") 
    icon_btb : StringProperty(default="BLENDER") 
    use_internal_icon_btb : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btb_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btb_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btb_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='FACE') 

    prop_btb_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 

    prop_btb_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btb_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btb_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=True)  
    prop_btb_project : BoolProperty(name= 'Project Individual Elements', description = '', default=True)  
    prop_btb_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btb_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btb_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btb_scale : BoolProperty(name= 'Scale', description = '', default=False)  


    #----------------------------
    

    # BUTTON C = 3D CURSOR #
    name_btc : StringProperty(default="Cursor") 
    icon_btc : StringProperty(default="BLENDER") 
    use_internal_icon_btc : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btc_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='CURSOR') 

    prop_btc_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btc_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='VERTEX') 

    prop_btc_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 

    prop_btc_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btc_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btc_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=True)  
    prop_btc_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btc_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btc_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btc_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btc_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    prop_btc_cursor_use : BoolProperty(name= 'Cursor to Active', description = '', default=False)  
   
    prop_btc_cursor : EnumProperty(
        name = "3d Cursor to...", 
        items=[("tpc_active" ,"Active"   ,"Active"   ,"" , 1),                                     
               ("tpc_select" ,"Selected" ,"Selected" ,"" , 2)],
        default = "tpc_active")


    #----------------------------
    

    # BUTTON D = ACTIVE #
    name_btd : StringProperty(default="Active") 
    icon_btd : StringProperty(default="BLENDER") 
    use_internal_icon_btd : BoolProperty(name= 'Internal Icon', description = '', default=False)  
 
    prop_btd_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btd_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btd_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='VERTEX') 

    prop_btd_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 

    prop_btd_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btd_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=True)  
    prop_btd_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_btd_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btd_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btd_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btd_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btd_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    
    #----------------------------
    

    # BUTTON E = CLOSESET #
    name_bte : StringProperty(default="Closest") 
    icon_bte : StringProperty(default="BLENDER") 
    use_internal_icon_bte : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_bte_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='MEDIAN_POINT') 

    prop_bte_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_bte_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='VERTEX') 

    prop_bte_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 

    prop_bte_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_bte_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=True)  
    prop_bte_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_bte_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_bte_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_bte_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_bte_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_bte_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    #----------------------------
    

    # BUTTON F = RETOPO #
    name_btf : StringProperty(default="Retopo") 
    icon_btf : StringProperty(default="BLENDER") 
    use_internal_icon_btf : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btf_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='BOUNDING_BOX_CENTER') 

    prop_btf_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  


    prop_btf_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='FACE') 

    prop_btf_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 


    prop_btf_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btf_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btf_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_btf_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btf_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btf_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btf_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btf_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    #----------------------------
    

    # BUTTON G = EDGE CENTER #
    name_btg : StringProperty(default="MidPoint") 
    icon_btg : StringProperty(default="BLENDER") 
    use_internal_icon_btg : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btg_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btg_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  


    prop_btg_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='EDGE_MIDPOINT') 

    prop_btg_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 


    prop_btg_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btg_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btg_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_btg_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btg_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btg_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btg_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btg_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    #----------------------------
    

    # BUTTON H = EDGE PERPENDICULAR #
    name_bth : StringProperty(default="Perpendic") 
    icon_bth : StringProperty(default="BLENDER") 
    use_internal_icon_bth : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_bth_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_bth_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  


    prop_bth_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")],
        default='EDGE_PERPENDICULAR') 

    prop_bth_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 


    prop_bth_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_bth_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_bth_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_bth_project : BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_bth_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_bth_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_bth_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_bth_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    #----------------------------
    

    # BUTTON MODAL = HOTKEY = PLACE #
    name_btM : StringProperty(default="Custom*") 
    icon_btM : StringProperty(default="BLENDER") 
    use_internal_icon_btM : BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btM_pivot : EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btM_use_pivot : BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btM_elements : EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=[('INCREMENT'          ,'Increment'           ,'snap elements'), 
               ('VERTEX'             ,'Vertex'              ,'snap elements'), 
               ('EDGE'               ,'Edge'                ,'snap elements'), 
               ('FACE'               ,'Face'                ,'snap elements'), 
               ('VOLUME'             ,'Volume'              ,'snap elements'), 
               ("EDGE_MIDPOINT"      ,"Edge MidPoint"       ,"snap elements"),
               ("EDGE_PERPENDICULAR" ,"Edge Perpendicular"  ,"snap elements")], 
        default='FACE') 

    prop_btM_target : EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 

    prop_btM_absolute_grid : BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btM_snap_self : BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btM_align_rotation : BoolProperty(name= 'Align Rotation to Target', description = '', default=True)  
    prop_btM_project : BoolProperty(name= 'Project Individual Elements', description = '', default=True)  
    prop_btM_peel_object : BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btM_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btM_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btM_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    hotkey_button_m : StringProperty(name = 'Key', default="F", description = 'change hotkey / only capital letters allowed') 
    hotkey_button_m_ctrl : BoolProperty(name= 'use Ctrl', description = 'enable / disable', default=False) 
    hotkey_button_m_alt : BoolProperty(name= 'use Alt', description = 'enable / disable', default=False) 
    hotkey_button_m_shift : BoolProperty(name= 'use Shift', description = 'enable / disable', default=False) 

    #----------------------------
    
    # MIRROR #

    toggle_mirror_func : bpy.props.BoolProperty(name = "Toggle Mirror Tools", description = "toggle tools visibilty in the pie menu", default = True)

    orient : bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View"),
               ("CURSOR"    ,"Cursor"   ,"Cursor")],
               name = "Orientation",
               default = "GLOBAL",    
               description = "change orientation axis")

    #----------------------------

    
    # DRAW PREFENCES #
    def draw(self, context):
        snap_global = context.window_manager.snap_global_props  

        layout = self.layout.column(align=True)

        icons = load_icons()        
       
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)

        # INFO #
        if self.prefs_tabs == 'info':

            box = layout.box().column(align=True)
            box.separator() 
 
            row = box.column(align=False)            
            row.label(text="Welcome to SnapSet!")   
           
            box.separator() 

            row = box.column(align=True)       
            row.label(text="> Customizable snap presets for the 3d view.")       
            row.label(text="> The pivot and snap functions will be changed ")                     
            row.label(text="> for respective task at the same time.")                     
                       
            row.separator()             
          
            row.label(text="> Have Fun! ;)")  
        
            box.separator() 


        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(align=True)
            box.separator()              

            row = box.row(align=True) 
            row.label(text="Panel in Sidebar [N]", icon ="COLLAPSEMENU")           
   
            box.separator()
        
            row = box.row()           
            row.label(text="TAB Category")   
            row.prop(self, "category", text="")

            box.separator() 
            box.separator() 

            row = box.row()           
            row.prop(self, 'toggle_display_buttons_pl',  expand=True)
       
            box.separator() 

            row = box.row()                 
            row.prop(self, 'toggle_display_name_pl',  expand=True)

            box.separator()                          
            box.separator()            

            row = box.row(align=True)  
            row.label(text="Layout Size:", icon ="ORIENTATION_VIEW")                 
            row.prop(self, 'ui_scale_y_panel')      

            box.separator()


        # APPEND #
        if self.prefs_tabs == 'menus':

            box = layout.box().column(align=True)    
            box.separator()
              
            row = box.column(align=True)          
            row.label(text="All Context Menus use in all layout types the same settings", icon='INFO')

            if self.toggle_special_menu == True or \
            self.toggle_keymap_menus == True and self.toggle_keymap_type == 'menu' or \
            self.toggle_editor_menu == True and self.toggle_editor_layout == 'menu' or \
            self.toggle_snapping_menu == True and self.toggle_snapping_type == 'menu':

                box.separator() 
                
                row = box.row(align=True)   
                row.prop(self, 'toggle_special_name', expand=True)
               
                sub = row.row(align=True)
                sub.scale_x = 1   
                sub.prop(self, 'ui_scale_y_special')

                box.separator() 

                row = box.row(align=True) 
                row.prop(self, 'toggle_special_type_layout', expand=True)

                box.separator() 
                
                row = box.row(align=True)  
                row.prop(self, 'toggle_special_icon')
                row.prop(self, 'toggle_special_separator')
            
                box.separator() 
                
                row = box.row(align=True)
                row.prop(snap_global, "toggle_special_buttons")  
                #row.prop(self, 'row_align_special')
     
                box.separator()  
                
                icon_snap_grid = icons.get("icon_snap_grid")  
                icon_snap_place = icons.get("icon_snap_place")                    
                icon_snap_cursor = icons.get("icon_snap_cursor")                     
                icon_snap_closest = icons.get("icon_snap_closest")
                icon_snap_active = icons.get("icon_snap_active")  
                icon_snap_retopo = icons.get("icon_snap_retopo")
                icon_snap_center = icons.get("icon_snap_center")          
                icon_snap_perpendic = icons.get("icon_snap_perpendic")
                icon_snap_custom = icons.get("icon_snap_custom")    

                if snap_global.toggle_special_buttons == True:     

                    box = layout.box().column(align=True)        
                    box.separator()    

                    row = box.column(align=False)              
                    row.label(text="Durable Tools:")   
                    row.label(text="> After execute the snap settings toggle to the needed preferences.")                        

                    box.separator()    

                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_grid_special", text='')                          
                    row.label(text="Grid", icon_value=icon_snap_grid.icon_id)
                    row.label(text="> snap pivot with absolute grid alignment")   
                 
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_place_special", text='')                   
                    row.label(text="Place", icon_value=icon_snap_place.icon_id)             
                    row.label(text="> snap pivot to surface of other objects")   
                
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_cursor_special", text='')           
                    row.label(text="Cursor", icon_value=icon_snap_cursor.icon_id) 
                    row.label(text="> set 3d cursor to active or selected")   
                   
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT' 
                    row.prop(self, "tpc_use_closest_special", text='')  
                    row.label(text="Closest", icon_value=icon_snap_closest.icon_id)            
                    row.label(text="> snap closest point onto target")   
                    
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'  
                    row.prop(self, "tpc_use_active_special", text='')                                
                    row.label(text="Active", icon_value=icon_snap_active.icon_id) 
                    row.label(text="> snap active pivot onto target")   
                   
                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_retopo_special", text='')                        
                    row.label(text="Retopo", icon_value=icon_snap_retopo.icon_id) 
                    row.label(text="> snap selected onto target in editmode")   
                  
                    box.separator() 
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_center_special", text='')  
                    row.label(text="MidPoint", icon_value=icon_snap_center.icon_id) 
                    row.label(text="> snap selected onto target")  

                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_perpendic_special", text='')                        
                    row.label(text="Perpendic", icon_value=icon_snap_perpendic.icon_id) 
                    row.label(text="> snap selected onto target")  

                    if self.toggle_special_type_layout in ['column', 'switch']:

                        box.separator() 
                        box.separator() 

                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_separator_modal_special", text='')                          
                        row.label(text="Separator", icon='REMOVE')
                        row.label(text="> division line")   

                        box.separator() 
                  
                    box.separator()                       
                                  
                    row = box.column(align=False)              
                    row.label(text="(*) Modal Tools:")   
                    row.label(text="> After execute the snap settings toggle to the needed preferences.")   
                    row.label(text="> When finished the settings switch back to the previous one.")                           

                    box.separator()                         
                    
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_grid_modal_special", text='')                          
                    row.label(text="Grid*", icon_value=icon_snap_grid.icon_id)
                    row.label(text="> snap pivot with absolute grid alignment til release")              

                    box.separator() 
                  
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_place_modal_special", text='')                          
                    row.label(text="Place*", icon_value=icon_snap_place.icon_id)             
                    row.label(text="> object mode: snap pivot to surface of other objects til release")   

                    box.separator()           
             
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_retopo_modal_special", text='')                      
                    row.label(text="Retopo*", icon_value=icon_snap_retopo.icon_id) 
                    row.label(text="> edit mode: snap selected onto target til release")  

                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_center_modal_special", text='')  
                    row.label(text="MidPoint*", icon_value=icon_snap_center.icon_id) 
                    row.label(text="> snap selected onto target til release")  

                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_perpendic_modal_special", text='')                        
                    row.label(text="Perpendic*", icon_value=icon_snap_perpendic.icon_id) 
                    row.label(text="> snap selected onto target til release")  

                    box.separator() 
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_custom_modal_special", text='')                      
                    row.label(text="Custom*", icon_value=icon_snap_custom.icon_id) 
                    row.label(text="> snap selected onto target til release")  
                                       
                    if self.toggle_special_type_layout in ['column', 'switch']:

                        box.separator() 
                        box.separator() 

                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_separator_settings_special", text='')                          
                        row.label(text="Separator", icon='REMOVE')
                        row.label(text="> division line")  

                        box.separator() 
                   
                    box.separator() 

                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_settings_special", text='')                      
                    row.label(text="Settings", icon='LAYER_USED') 
                    row.label(text="> open addon preferences")  

                    box.separator() 

            else:
                row.label(text="> settings appear with activation...")


            box.separator() 
            box.separator() 
            box = layout.box().column(align=True)    
            box.separator()

            row = box.row(align=True)  
            if self.toggle_special_menu == True:
                ico = 'CHECKBOX_HLT'
            else:
                ico = 'CHECKBOX_DEHLT'  
            row.prop(self, "toggle_special_menu", text="", icon = ico)
            row.label(text="Context Menu: Key [W]")   

            if self.toggle_special_menu == True:
                row.prop(self, 'toggle_special_type', expand=True)
        

            box.separator() 
            box = layout.box().column(align=True)                 
            box.separator()            

            row = box.row(align=True)   
            if self.toggle_keymap_menus == True:
                ico = 'CHECKBOX_HLT'
            else:
                ico = 'CHECKBOX_DEHLT'  
            row.prop(self, "toggle_keymap_menus", text="", icon = ico)  
            row.label(text="Context Menu: Key [Custom]")

            if self.toggle_keymap_menus == True:                  
   
                box.separator()     

                row = box.row(align=True)  
                row.label(text="Menu Type:")
                row.prop(self, 'toggle_keymap_type', expand=True)
                       
                box.separator()   
                        
                row = box.row(align=True)  
                row.prop(self, 'hotkey_menu')
                row.prop(self, 'hotkey_menu_ctrl')
                row.prop(self, 'hotkey_menu_alt')
                row.prop(self, 'hotkey_menu_shift')
                
                box.separator() 

                if self.toggle_keymap_type == 'pie': 
                                                  
                    row = box.column(align=True)                                                                  
                    row.prop(self, 'tpc_use_emposs')
                 
                    box.separator() 

                    row = box.row(align=True)
                    row.prop(snap_global, "toggle_pie_buttons", text='')  
                    row.label(text="Toggle Pie Buttons")  
         
                    box.separator()  
                    
                    icon_snap_grid = icons.get("icon_snap_grid")  
                    icon_snap_place = icons.get("icon_snap_place")                    
                    icon_snap_cursor = icons.get("icon_snap_cursor")                     
                    icon_snap_closest = icons.get("icon_snap_closest")
                    icon_snap_active = icons.get("icon_snap_active")  
                    icon_snap_retopo = icons.get("icon_snap_retopo")
                    icon_snap_center = icons.get("icon_snap_center")          
                    icon_snap_perpendic = icons.get("icon_snap_perpendic")
                    icon_snap_custom = icons.get("icon_snap_custom")    

                    if snap_global.toggle_pie_buttons == True:     

                        box = layout.box().column(align=True)        
                        box.separator()    

                        row = box.column(align=False)              
                        row.label(text="Durable Tools:")   
                        row.label(text="> After execute the snap settings toggle to the needed preferences.")                        

                        box.separator() 

                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_grid_pie", text='')                          
                        row.label(text="Grid", icon_value=icon_snap_grid.icon_id)
                        row.label(text="> snap pivot with absolute grid alignment")   
                     
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_place_pie", text='')                   
                        row.label(text="Place", icon_value=icon_snap_place.icon_id)             
                        row.label(text="> snap pivot to surface of other objects")   
                    
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_cursor_pie", text='')           
                        row.label(text="Cursor", icon_value=icon_snap_cursor.icon_id) 
                        row.label(text="> set 3d cursor to active or selected")   
                       
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT' 
                        row.prop(self, "tpc_use_closest_pie", text='')  
                        row.label(text="Closest", icon_value=icon_snap_closest.icon_id)            
                        row.label(text="> snap closest point onto target")   
                        
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'  
                        row.prop(self, "tpc_use_active_pie", text='')                                
                        row.label(text="Active", icon_value=icon_snap_active.icon_id) 
                        row.label(text="> snap active pivot onto target")   
                       
                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_retopo_pie", text='')                        
                        row.label(text="Retopo", icon_value=icon_snap_retopo.icon_id) 
                        row.label(text="> snap selected onto target in editmode")   
                      
                        box.separator() 
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_center_pie", text='')  
                        row.label(text="MidPoint", icon_value=icon_snap_center.icon_id) 
                        row.label(text="> snap selected onto target")  

                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_perpendic_pie", text='')                        
                        row.label(text="Perpendic", icon_value=icon_snap_perpendic.icon_id) 
                        row.label(text="> snap selected onto target")  

                        box.separator() 
                        box = layout.box().column(align=True)
                        box.separator() 
                  
                        row = box.column(align=False)              
                        row.label(text="(*) Modal Tools:")   
                        row.label(text="> After execute the snap settings toggle to the needed preferences.")   
                        row.label(text="> When finished the settings switch back to the previous one.")                           

                        box.separator()                         
                        
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_grid_modal_pie", text='')                          
                        row.label(text="Grid*", icon_value=icon_snap_grid.icon_id)
                        row.label(text="> snap pivot with absolute grid alignment til release")              

                        box.separator() 
                      
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_place_modal_pie", text='')                          
                        row.label(text="Place*", icon_value=icon_snap_place.icon_id)             
                        row.label(text="> object mode: snap pivot to surface of other objects til release")   

                        box.separator()           
                 
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_retopo_modal_pie", text='')                      
                        row.label(text="Retopo*", icon_value=icon_snap_retopo.icon_id) 
                        row.label(text="> edit mode: snap selected onto target til release")  

                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_center_modal_pie", text='')  
                        row.label(text="MidPoint*", icon_value=icon_snap_center.icon_id) 
                        row.label(text="> snap selected onto target til release")  

                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_perpendic_modal_pie", text='')                        
                        row.label(text="Perpendic*", icon_value=icon_snap_perpendic.icon_id) 
                        row.label(text="> snap selected onto target til release")  

                        box.separator() 
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_custom_modal_pie", text='')                      
                        row.label(text="Custom*", icon_value=icon_snap_custom.icon_id) 
                        row.label(text="> snap selected onto target til release")  

                        box.separator() 

                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_settings_pie", text='')                      
                        row.label(text="Settings", icon='LAYER_USED') 
                        row.label(text="> open addon preferences")  

                        box.separator() 

                    row = box.row(align=True)
                    row.prop(snap_global, 'toggle_boxes', text="", icon ="ORIENTATION_VIEW")                    
                    row.label(text="Scale Box Size in Pie Menu")                    
                    
                    box.separator() 
                    
                    if snap_global.toggle_boxes == True:                     
                   
                        row = box.row(align=True)                    
                        row.label(text="Box1 Left")                   
                        row.prop(self, 'ui_scale_x_b1')
                        row.prop(self, 'ui_scale_y_b1')
                        
                        row = box.row(align=True)                    
                        row.label(text="Box2 Right")                         
                        row.prop(self, 'ui_scale_x_b2')   
                        row.prop(self, 'ui_scale_y_b2')   

                        row = box.row(align=True)                    
                        row.label(text="Box3 Bottom")      
                        row.prop(self, 'ui_scale_x_b3')   
                        row.prop(self, 'ui_scale_y_b3')   

                        row = box.row(align=True)                    
                        row.label(text="Box4 Top") 
                        row.prop(self, 'ui_scale_x_b4')   
                        row.prop(self, 'ui_scale_y_b4')   

                        row = box.row(align=True)                    
                        row.label(text="Box5 Top/Left") 
                        row.prop(self, 'ui_scale_x_b5')   
                        row.prop(self, 'ui_scale_y_b5')   

                        row = box.row(align=True)                    
                        row.label(text="Box6 Top/Right") 
                        row.prop(self, 'ui_scale_x_b6')   
                        row.prop(self, 'ui_scale_y_b6')   

                        row = box.row(align=True)                    
                        row.label(text="Box7 Bottom/Left") 
                        row.prop(self, 'ui_scale_x_b7')   
                        row.prop(self, 'ui_scale_y_b7')   

                        row = box.row(align=True)                    
                        row.label(text="Box8 Bottom/Right") 
                        row.prop(self, 'ui_scale_x_b8')   
                        row.prop(self, 'ui_scale_y_b8')   

                        box.separator() 


                    box.separator() 
                    box.separator() 
                   
                    row = box.row(align=True)  
                    row.label(text="Recommended Tools: ", icon='TOOL_SETTINGS')

                    row = box.row(align=True)                                
                    row.prop(self, 'toggle_mirror_func', text="")
                    row.label(text="Mirror Tools")                                                           
                    row.label(text="")                                                           
                    row.label(text="Orientation:")                              
                    row.prop(self, 'orient', text="")                  
                
                    box.separator() 
                    box.separator() 
                   
                    row = box.row(align=True)  
                    row.label(text="Recommended Addons: ", icon='PLUGIN')

                    row = box.row(align=True)                                
                    row.prop(self, 'toggle_addon_align_tools')

                    if self.toggle_addon_align_tools == True:
                            
                            #if addon_exists("space_view3d_align_tools"): 
                            
                            align_addon = "space_view3d_align_tools" 
                            align_state = addon_utils.check(align_addon)
                            if not align_state[0]:                 
                                row.operator("tpc_ot.activate_align_tools", text="Activate", icon="ERROR") 
                            else:                                                  
                                row.prop(self, 'toggle_align_tools_compact')                    

                            row.operator("preferences.addon_show", text="", icon="FRAME_NEXT").module="space_view3d_align_tools"                                     
                            row.label(text="", icon='BLENDER')   
                            box.separator() 
 
                    
                    row = box.row(align=True)   
                    row.prop(self, 'toggle_addon_alignmesh')

                    if self.toggle_addon_alignmesh == True:    
                        
                        #if addon_exists("view3d_alignmesh"):   
                                                       
                        alignmesh_addon = "view3d_alignmesh" 
                        alignmesh_state = addon_utils.check(alignmesh_addon)
                        if not alignmesh_state[0]:            
                            row.operator("tpc_ot.activate_align_mesh", text="Activate", icon="ERROR")                 
                        else:                          
                            row.prop(self, 'toggle_alignmesh_compact')                    
                        
                        row.operator("preferences.addon_show", text="", icon="FRAME_NEXT").module="view3d_alignmesh"                                                          
                        row.operator('wm.url_open', text = '', icon = 'PLUGIN').url = "https://github.com/mkbreuer/ToolPlus"
                        box.separator() 
                  

                    row = box.row(align=True)  
                    row.prop(self, 'toggle_addon_looptools')
                   
                    if self.toggle_addon_looptools == True: 

                        #if addon_exists("mesh_looptools"):    
                                                         
                        looptools_addon = "mesh_looptools" 
                        looptools_state = addon_utils.check(looptools_addon)
                        if not looptools_state[0]:                                  
                            row.operator("tpc_ot.activate_looptools", text="Activate", icon="ERROR")
                        else:
                            row.prop(self, 'toggle_looptools_menu_type')                     
                        
                        row.operator("preferences.addon_show", text="", icon="FRAME_NEXT").module="mesh_looptools"                      
                        row.label(text="", icon='BLENDER') 
                        box.separator()                


            #-----------------------------------------------------
   

            box.separator() 
            box = layout.box().column(align=True)        
            box.separator()
                     
            row = box.row(align=True)  
            if self.toggle_editor_menu == True:
                ico = 'CHECKBOX_HLT'
            else:
                ico = 'CHECKBOX_DEHLT'  
            row.prop(self, "toggle_editor_menu", text="", icon = ico)
            row.label(text="Editor / Header")     

            if self.toggle_editor_menu == True:  
                          
                row.prop(self, 'toggle_view_type', expand=True)
               
                box.separator()             
              
                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_type', expand=True)
     
                box.separator()             
              
                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_layout', expand=True) 

                box.separator()            
                box.separator()            

                row = box.row(align=True)  
                row.label(text="Layout Settings for Editor / Header: ", icon ="ORIENTATION_VIEW")     

                box.separator()  
     
                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_menu_name', expand=True)

                box.separator()    

                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_separator_prepend')
                row.prop(self, 'factor_separator_prepend')

                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_separator_append')
                row.prop(self, 'factor_separator_append')
                
                box.separator() 
                
                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_layout_scale_x', text="")  
                row.label(text="Scale X")                    
                row.prop(self, 'ui_scale_x_editor')   

                row = box.row(align=True)  
                row.prop(self, 'toggle_editor_layout_scale_y', text="")  
                row.label(text="Scale Y")                       
                row.prop(self, 'ui_scale_y_editor')      
              
                row = box.row(align=True)  
                row.prop(self, 'row_align', text="")  
                row.label(text="Keep Buttons separated")      

                if self.toggle_editor_layout == 'buttons':

                    row = box.row(align=True)
                    row.prop(snap_global, "toggle_editor_and_header_buttons", text='')  
                    row.label(text="Toggle Buttons")          
                   
                    box.separator()  
                    
                    icon_snap_grid = icons.get("icon_snap_grid")  
                    icon_snap_place = icons.get("icon_snap_place")                    
                    icon_snap_cursor = icons.get("icon_snap_cursor")                     
                    icon_snap_closest = icons.get("icon_snap_closest")
                    icon_snap_active = icons.get("icon_snap_active")  
                    icon_snap_retopo = icons.get("icon_snap_retopo")
                    icon_snap_center = icons.get("icon_snap_center")          
                    icon_snap_perpendic = icons.get("icon_snap_perpendic")
                    icon_snap_custom = icons.get("icon_snap_custom")    


                    if snap_global.toggle_editor_and_header_buttons == True:     

                        box = layout.box().column(align=True)        
                        box.separator()    

                        row = box.column(align=False)              
                        row.label(text="Durable Tools:")   
                        row.label(text="> After execute the snap settings toggle to the needed preferences.")                        

                        box.separator() 

                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_grid_editor", text='')                          
                        row.label(text="Grid", icon_value=icon_snap_grid.icon_id)
                        row.label(text="> snap pivot with absolute grid alignment")   
                     
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_place_editor", text='')                   
                        row.label(text="Place", icon_value=icon_snap_place.icon_id)             
                        row.label(text="> snap pivot to surface of other objects")   
                    
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_cursor_editor", text='')           
                        row.label(text="Cursor", icon_value=icon_snap_cursor.icon_id) 
                        row.label(text="> set 3d cursor to active or selected")   
                       
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT' 
                        row.prop(self, "tpc_use_closest_editor", text='')  
                        row.label(text="Closest", icon_value=icon_snap_closest.icon_id)            
                        row.label(text="> snap closest point onto target")   
                        
                        box.separator()            
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'  
                        row.prop(self, "tpc_use_active_editor", text='')                                
                        row.label(text="Active", icon_value=icon_snap_active.icon_id) 
                        row.label(text="> snap active pivot onto target")   
                       
                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_retopo_editor", text='')                        
                        row.label(text="Retopo", icon_value=icon_snap_retopo.icon_id) 
                        row.label(text="> snap selected onto target in editmode")   
                      
                        box.separator() 
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_center_editor", text='')  
                        row.label(text="MidPoint", icon_value=icon_snap_center.icon_id) 
                        row.label(text="> snap selected onto target")  

                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_perpendic_editor", text='')                        
                        row.label(text="Perpendic", icon_value=icon_snap_perpendic.icon_id) 
                        row.label(text="> snap selected onto target")  

                        box.separator() 


                        box = layout.box().column(align=True)
                        box.separator() 
                  
                        row = box.column(align=False)              
                        row.label(text="(*) Modal Tools:")   
                        row.label(text="> After execute the snap settings toggle to the needed preferences.")   
                        row.label(text="> When finished the settings switch back to the previous one.")                           

                        box.separator()                         
                        
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_grid_modal_editor", text='')                          
                        row.label(text="Grid*", icon_value=icon_snap_grid.icon_id)
                        row.label(text="> snap pivot with absolute grid alignment til release")              

                        box.separator() 
                      
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_place_modal_editor", text='')                          
                        row.label(text="Place*", icon_value=icon_snap_place.icon_id)             
                        row.label(text="> object mode: snap pivot to surface of other objects til release")   

                        box.separator()           
                 
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_retopo_modal_editor", text='')                      
                        row.label(text="Retopo*", icon_value=icon_snap_retopo.icon_id) 
                        row.label(text="> edit mode: snap selected onto target in til release")  

                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_center_modal_editor", text='')  
                        row.label(text="MidPoint*", icon_value=icon_snap_center.icon_id) 
                        row.label(text="> snap selected onto target til release")  

                        box.separator()           
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_perpendic_modal_editor", text='')                        
                        row.label(text="Perpendic*", icon_value=icon_snap_perpendic.icon_id) 
                        row.label(text="> snap selected onto target til release")  

                        box.separator() 
                       
                        row = box.row(align=False)
                        row.alignment = 'LEFT'
                        row.prop(self, "tpc_use_custom_modal_editor", text='')                      
                        row.label(text="Custom*", icon_value=icon_snap_custom.icon_id) 
                        row.label(text="> snap selected onto target til release")  

                        box.separator() 


            #-----------------------------------------------------
          
            box.separator() 
            box = layout.box().column(align=True)        
            box.separator()        
        
            row = box.row(align=True)  
            row.alignment = 'LEFT' 
            if self.toggle_snapping_menu == True:
                ico = 'CHECKBOX_HLT'
            else:
                ico = 'CHECKBOX_DEHLT'  
            row.prop(self, "toggle_snapping_menu", text="", icon = ico)
            row.label(text="Append to Snap Setting")

            if self.toggle_snapping_menu == True:          

                box.separator() 
                
                row = box.row(align=True)   
                row.prop(self, 'toggle_snapping_type', expand=True)
               
                sub = row.row(align=True)
                sub.scale_x = 1   
                sub.prop(self, 'ui_scale_y_snapping')

                box.separator() 

                row = box.row(align=True) 
                row.prop(self, 'toggle_snapping_type_layout', expand=True)
 
                box.separator() 
         
                row = box.row(align=True)  
                row.prop(self, 'row_align_snapping_hor')  

                box.separator() 
                
                row = box.row(align=False)
                row.prop(snap_global, "toggle_snapping_buttons", text='')  
                row.label(text="Toggle Buttons")  
     
                box.separator()  
                
                icon_snap_grid = icons.get("icon_snap_grid")  
                icon_snap_place = icons.get("icon_snap_place")                    
                icon_snap_cursor = icons.get("icon_snap_cursor")                     
                icon_snap_closest = icons.get("icon_snap_closest")
                icon_snap_active = icons.get("icon_snap_active")  
                icon_snap_retopo = icons.get("icon_snap_retopo")
                icon_snap_center = icons.get("icon_snap_center")          
                icon_snap_perpendic = icons.get("icon_snap_perpendic")
                icon_snap_custom = icons.get("icon_snap_custom")    


                if snap_global.toggle_snapping_buttons == True:     

                    box = layout.box().column(align=True)        
                    box.separator() 

                    row = box.column(align=False)              
                    row.label(text="Durable Tools:")   
                    row.label(text="> After execute the snap settings toggle to the needed preferences.")                        

                    box.separator()    
                                           
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_grid_snapping", text='')                          
                    row.label(text="Grid", icon_value=icon_snap_grid.icon_id)
                    row.label(text="> snap pivot with absolute grid alignment")   
                 
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_place_snapping", text='')                   
                    row.label(text="Place", icon_value=icon_snap_place.icon_id)             
                    row.label(text="> snap pivot to surface of other objects")   
                
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_cursor_snapping", text='')           
                    row.label(text="Cursor", icon_value=icon_snap_cursor.icon_id) 
                    row.label(text="> set 3d cursor to active or selected")   
                   
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT' 
                    row.prop(self, "tpc_use_closest_snapping", text='')  
                    row.label(text="Closest", icon_value=icon_snap_closest.icon_id)            
                    row.label(text="> snap closest point onto target")   
                    
                    box.separator()            
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'  
                    row.prop(self, "tpc_use_active_snapping", text='')                                
                    row.label(text="Active", icon_value=icon_snap_active.icon_id) 
                    row.label(text="> snap active pivot onto target")   
                   
                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_retopo_snapping", text='')                        
                    row.label(text="Retopo", icon_value=icon_snap_retopo.icon_id) 
                    row.label(text="> snap selected onto target in editmode")   
                  
                    box.separator() 
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_center_snapping", text='')  
                    row.label(text="MidPoint", icon_value=icon_snap_center.icon_id) 
                    row.label(text="> snap selected onto target")  

                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_perpendic_snapping", text='')                        
                    row.label(text="Perpendic", icon_value=icon_snap_perpendic.icon_id) 
                    row.label(text="> snap selected onto target")  

                    box.separator() 
                    
                    # HIDDEN MODAL TOOLS
                    """
                    box = layout.box().column(align=True)
                    box.separator() 
              
                    row = box.column(align=False)              
                    row.label(text="(*) Modal Tools:")   
                    row.label(text="> After execute the snap settings toggle to the needed preferences.")   
                    row.label(text="> When finished the settings switch back to the previous one.")                           

                    box.separator()                         
                    
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_grid_modal_snapping", text='')                          
                    row.label(text="Grid*", icon_value=icon_snap_grid.icon_id)
                    row.label(text="> snap pivot with absolute grid alignment til release")              

                    box.separator() 
                  
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_place_modal_snapping", text='')                          
                    row.label(text="Place*", icon_value=icon_snap_place.icon_id)             
                    row.label(text="> object mode: snap pivot to surface of other objects til release")   

                    box.separator()           
             
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_retopo_modal_snapping", text='')                      
                    row.label(text="Retopo*", icon_value=icon_snap_retopo.icon_id) 
                    row.label(text="> edit mode: snap selected onto target til release")  

                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_center_modal_snapping", text='')  
                    row.label(text="MidPoint*", icon_value=icon_snap_center.icon_id) 
                    row.label(text="> snap selected onto target til release")  

                    box.separator()           
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_perpendic_modal_snapping", text='')                        
                    row.label(text="Perpendic*", icon_value=icon_snap_perpendic.icon_id) 
                    row.label(text="> snap selected onto target til release")  

                    box.separator() 
                   
                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_custom_modal_snapping", text='')                      
                    row.label(text="Custom*", icon_value=icon_snap_custom.icon_id) 
                    row.label(text="> snap selected onto target til release")  

                    box.separator() 

                    row = box.row(align=False)
                    row.alignment = 'LEFT'
                    row.prop(self, "tpc_use_settings_snapping", text='')                      
                    row.label(text="Settings", icon='LAYER_USED') 
                    row.label(text="> open addon preferences")  
                    
                    """
                    
            box.separator() 



            #-----------------------------------------------------



        # BUTTONS #
        if self.prefs_tabs == 'buttons':
            
            box = layout.box().column(align=True)
            box.separator() 
 
            row = box.column(align=False)
            row.label(text="General Setting")   

            box.separator() 

            row = box.row(align=True)
            row.prop(self, "tpc_use_snap")           
                 
            box.separator() 
            box = layout.box().column(align=True)
            box.separator() 
        
            row = box.column(align=False)
            row.label(text="Custom Snap Setting")   

            box.separator() 

            row = box.column(align=True)
            row.label(text="> the setting for all main buttons are customizable.")  
            row.label(text="> eg.: BT-A = Button A  /  Grid = default Settings")  
            row.label(text="> BT-F replace BT-B in editmode.")  
            row.label(text="> Custom M has it own keyboard shortcut.")  
            
            box.separator() 
            box.separator() 
           
            row = box.row(align=False)
            #row.prop(self, "toggle_button_type", expand=True)             
            row.prop_enum(self, "toggle_button_type", "button_a", text="BT-A / Grid")
            row.prop_enum(self, "toggle_button_type", "button_b", text="BT-B / Place")
            row.prop_enum(self, "toggle_button_type", "button_c", text="BT-C / Cursor")
         
            row = box.row(align=False)
            row.prop_enum(self, "toggle_button_type", "button_d", text="BT-D / Active")
            row.prop_enum(self, "toggle_button_type", "button_e", text="BT-E / Closest")
            row.prop_enum(self, "toggle_button_type", "button_f", text="BT-F / Retopo")

            row = box.row(align=False)
            row.prop_enum(self, "toggle_button_type", "button_g", text="BT-G / MidPoint")
            row.prop_enum(self, "toggle_button_type", "button_h", text="BT-H / Perpendic")
            row.prop_enum(self, "toggle_button_type", "button_m", text="Custom M / Key")

            
            box.separator() 

            if self.toggle_button_type == 'button_a':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_bta", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_bta", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                    
                row = box.row(align=False)                    
                row.prop(self, "icon_bta", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)            
                row.prop(self, "prop_bta_pivot")               
                row.prop(self, "prop_bta_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_bta_target")  
                row.prop(self, "prop_bta_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_bta_elements == "INCREMENT":
                    row.prop(self, "prop_bta_absolute_grid")  

                else:
                    row.prop(self, "prop_bta_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_bta_align_rotation")  

                    if self.prop_bta_elements == "FACE":
                        row.prop(self, "pro_btap_project")  
                   
                    if self.prop_bta_elements == "VOLUME":
                        row.prop(self, "prop_bta_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_bta_translate")  
                row.prop(self, "prop_bta_rotation")  
                row.prop(self, "prop_bta_scale")  

                box.separator() 


            if self.toggle_button_type == 'button_b':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btb", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btb", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                    
                row = box.row(align=False)                    
                row.prop(self, "icon_btb", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_btb_pivot")               
                row.prop(self, "prop_btb_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_btb_target")  
                row.prop(self, "prop_btb_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_btb_elements == "INCREMENT":
                    row.prop(self, "prop_btb_absolute_grid")  

                else:
                    row.prop(self, "prop_btb_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_btb_align_rotation")  

                    if self.prop_btb_elements == "FACE":
                        row.prop(self, "prop_btb_project")  
                   
                    if self.prop_btb_elements == "VOLUME":
                        row.prop(self, "prop_btb_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btb_translate")  
                row.prop(self, "prop_btb_rotation")  
                row.prop(self, "prop_btb_scale")  

                box.separator() 


            if self.toggle_button_type == 'button_c':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btc", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btc", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_btc", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_btc_pivot")               
                row.prop(self, "prop_btc_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_btc_target")  
                row.prop(self, "prop_btc_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_btc_elements == "INCREMENT":
                    row.prop(self, "prop_btc_absolute_grid")  

                else:
                    row.prop(self, "prop_btc_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_btc_align_rotation")  

                    if self.prop_btc_elements == "FACE":
                        row.prop(self, "pro_btc_project")  
                   
                    if self.prop_btc_elements == "VOLUME":
                        row.prop(self, "prop_btc_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btc_translate")  
                row.prop(self, "prop_btc_rotation")  
                row.prop(self, "prop_btc_scale")  

                box.separator() 


            if self.toggle_button_type == 'button_d':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btd", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btd", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_btd", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_btd_pivot")               
                row.prop(self, "prop_btd_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_btd_target")  
                row.prop(self, "prop_btd_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_btd_elements == "INCREMENT":
                    row.prop(self, "prop_btd_absolute_grid")  

                else:
                    row.prop(self, "prop_btd_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_btd_align_rotation")  

                    if self.prop_btd_elements == "FACE":
                        row.prop(self, "pro_btd_project")  
                   
                    if self.prop_btd_elements == "VOLUME":
                        row.prop(self, "prop_btd_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btd_translate")  
                row.prop(self, "prop_btd_rotation")  
                row.prop(self, "prop_btd_scale")  

                box.separator() 


            if self.toggle_button_type == 'button_e':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_bte", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_bte", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_bte", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_bte_pivot")               
                row.prop(self, "prop_bte_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_bte_target")  
                row.prop(self, "prop_bte_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_bte_elements == "INCREMENT":
                    row.prop(self, "prop_bte_absolute_grid")  

                else:
                    row.prop(self, "prop_bte_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_bte_align_rotation")  

                    if self.prop_bte_elements == "FACE":
                        row.prop(self, "pro_bte_project")  
                   
                    if self.prop_bte_elements == "VOLUME":
                        row.prop(self, "prop_bte_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_bte_translate")  
                row.prop(self, "prop_bte_rotation")  
                row.prop(self, "prop_bte_scale")  

                box.separator() 
                


            if self.toggle_button_type == 'button_f':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btf", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btf", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_btf", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_btf_pivot")               
                row.prop(self, "prop_btf_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_btf_target")  
                row.prop(self, "prop_btf_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_btf_elements == "INCREMENT":
                    row.prop(self, "prop_btf_absolute_grid")  

                else:
                    row.prop(self, "prop_btf_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_btf_align_rotation")  

                    if self.prop_btf_elements == "FACE":
                        row.prop(self, "pro_btf_project")  
                   
                    if self.prop_btf_elements == "VOLUME":
                        row.prop(self, "prop_btf_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btf_translate")  
                row.prop(self, "prop_btf_rotation")  
                row.prop(self, "prop_btf_scale")  

                box.separator() 



            if self.toggle_button_type == 'button_g':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btg", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btg", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_btg", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_btg_pivot")               
                row.prop(self, "prop_btg_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_btg_target")  
                row.prop(self, "prop_btg_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_btg_elements == "INCREMENT":
                    row.prop(self, "prop_btg_absolute_grid")  

                else:
                    row.prop(self, "prop_btg_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_btg_align_rotation")  

                    if self.prop_btg_elements == "FACE":
                        row.prop(self, "pro_btg_project")  
                   
                    if self.prop_btg_elements == "VOLUME":
                        row.prop(self, "prop_btg_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btg_translate")  
                row.prop(self, "prop_btg_rotation")  
                row.prop(self, "prop_btg_scale")  

                box.separator() 


            if self.toggle_button_type == 'button_h':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_bth", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_bth", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_bth", text="Icon Name")
                 
                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_bth_pivot")               
                row.prop(self, "prop_bth_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_bth_target")  
                row.prop(self, "prop_bth_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_bth_elements == "INCREMENT":
                    row.prop(self, "prop_bth_absolute_grid")  

                else:
                    row.prop(self, "prop_bth_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_bth_align_rotation")  

                    if self.prop_bth_elements == "FACE":
                        row.prop(self, "pro_bth_project")  
                   
                    if self.prop_bth_elements == "VOLUME":
                        row.prop(self, "prop_bth_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_bth_translate")  
                row.prop(self, "prop_bth_rotation")  
                row.prop(self, "prop_bth_scale")  

                box.separator() 


            if self.toggle_button_type == 'button_m':
             
                box.separator()
             
                row = box.row(align=True)  
                row.label(text="Custom M = Modal Hotkey Operator", icon ="COLLAPSEMENU")         
             
                box.separator() 

                row = box.row(align=True)  
                row.prop(self, 'toggle_snapset_add_tools', expand=True)

                box.separator() 

                row = box.row(align=True)  
                row.prop(self, 'hotkey_button_m')
                row.prop(self, 'hotkey_button_m_ctrl')
                row.prop(self, 'hotkey_button_m_alt')
                row.prop(self, 'hotkey_button_m_shift')

                box.separator() 

                row = box.column(align=True)  
                row.label(text="This modal operator with shortcut keeps the modal close to the selection, while running.")
                row.label(text="This is important, because the modal are dependent to the position of the mouse pointer.")
                row.label(text="Blender need a restart after activation or it has no effect.")  

                box.separator()
                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btM", text="Custom Name")   
                 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btM", text="Use Internal or Custom Icon")     
                row.operator('wm.url_open', text = '', icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
                            
                row = box.row(align=False)                    
                row.prop(self, "icon_btM", text="Icon Name")

                box.separator() 
                box.separator() 

                row = box.column(align=False)
                row.prop(self, "prop_btM_pivot")               
                row.prop(self, "prop_btM_use_pivot")   

                box.separator() 
                
                row = box.column(align=False)

                row.prop(self, "prop_btM_target")  
                row.prop(self, "prop_btM_elements")   
     
                box.separator() 
                
                row = box.column(align=False)

                if self.prop_btM_elements == "INCREMENT":
                    row.prop(self, "prop_btM_absolute_grid")  

                else:
                    row.prop(self, "prop_btM_snap_self", text ="Project onto Self / Editmode")  
                
                    row.prop(self, "prop_btM_align_rotation")  

                    if self.prop_btM_elements == "FACE":
                        row.prop(self, "prop_btM_project")  
                   
                    if self.prop_btM_elements == "VOLUME":
                        row.prop(self, "prop_btM_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btM_translate")  
                row.prop(self, "prop_btM_rotation")  
                row.prop(self, "prop_btM_scale")  

                box.separator() 
            
            
            box.separator()                
            box = layout.box().column(align=True)
            box.separator()
         
            row = box.row(align=True)
            row.prop(snap_global, 'toggle_iconchange', text="", icon ="INFO")
            row.label(text="< Changing Icons !")
            row.operator('wm.url_open', text="", icon='BLENDER').url = "https://raw.githubusercontent.com/mkbreuer/TP-Courier/master/reference%20sheets/blender_internal_icons_2.80.png"
       
            box.separator()            

            if snap_global.toggle_iconchange == True:           
           
                row = box.column(align=True)
                row.label(text="> images in the addon icon folder.")
                row.label(text="> they can be exchanged by other one.")

                row.separator()
             
                row.label(text="> to use internal icons: enable the addon icon viewer for text editor.")
                row.label(text="> it shows all icons that blender use.")
                row.label(text="> attention: the icon names have always to be written as capitalization.")

                box.separator()         
          
          
            box = layout.box().column(align=True)
            box.separator()

            row = box.row(align=True)             
            row.prop(snap_global, 'toggle_keychange', text="", icon ="INFO")
            row.label(text="< Changing Shortcut Key !")
            row.operator('wm.url_open', text="", icon='SCRIPT').url = "https://github.com/mkbreuer/Misc-Share-Archiv/blob/master/images/SHORTCUTS_Type%20of%20key%20event.png?raw=true"
                           
            box.separator()
           
            if snap_global.toggle_keychange == True: 

                row = box.column(align=True)
                row.label(text="Go to: Blender Preferences > Keymap")             
               
                row.separator() 

                row.label(text="Menu / PieMenu", icon ="BLANK1")
                row.label(text="1 > change search to Key-Bindig and insert: shift w ", icon ="BLANK1")
                row.label(text="2a -> 3D View > SnapSet: VIEW3D_MT_snapset_menu!", icon ="BLANK1")
                row.label(text="2b -> 3D View > SnapSet: VIEW3D_MT_snapset_menu_pie!", icon ="BLANK1")
                row.label(text="3 -> choose a new key configuration and save preferences !", icon ="BLANK1")

                row.separator() 
            
                row = box.column(align=True)            
                row.label(text="Custom M Modal", icon ="BLANK1")             
                row.label(text="1 > change search to Key-Bindig and insert: f ", icon ="BLANK1")
                row.label(text="2 ->  Objectmode > Operator [F]: tpc_ot.snapset_modal!", icon ="BLANK1")
                row.label(text="3 -> choose a new key configuration and save preferences !", icon ="BLANK1")

                row.separator()  

                row = box.row(align=True)             
                row.label(text="Or edit the keymap script directly:", icon ="BLANK1")

                row.separator()  

                row = box.row(align=True)  
                row.label(text="", icon ="BLANK1")
                row.operator("tpc_ot.keymap_snapset", text = 'Open KeyMap in Text Editor')
                row.operator('wm.url_open', text = 'Type of Events').url = "https://docs.blender.org/api/blender_python_api_2_77_0/bpy.types.Event.html"
 
                box.separator()


# PROPERTY GROUP #  
class Global_Property_Group(bpy.types.PropertyGroup):
    # use an annotation

    # UI LAYOUT #    
    sel_01_use : BoolProperty(name="RePlace Letter", description="enable/disable", default=False)   
    sel_02_use : BoolProperty(name="ReName Datas", description="enable/disable", default=False)   
    sel_03_use : BoolProperty(name="Create Material", description="enable/disable", default=False)   
    sel_04_use : BoolProperty(name="Object Display", description="enable/disable", default=False)   

    toggle_dropdown : BoolProperty(name="Setting", description="open/close", default=False)  
    toggle_boxes : BoolProperty(name= 'Box Sizes', description = 'open layout scale for boxes in the piemenu', default=False)    
    toggle_iconchange : BoolProperty(name= 'Icon Change', description = 'open info for icon change', default=False)    
    toggle_keychange : BoolProperty(name= 'Key Change', description = 'open info for key change', default=False)    

    toggle_snapping_buttons : BoolProperty(name="Toggle Context Buttons", description="on / off", default=False)
    toggle_special_buttons : BoolProperty(name="Toggle Context Buttons", description="on / off", default=False)
    toggle_pie_buttons : BoolProperty(name="Toggle Context Buttons", description="on / off", default=False)
    toggle_editor_and_header_buttons : BoolProperty(name="Toggle Context Buttons", description="on / off", default=False)




# REGISTER #
classes = (
    VIEW3D_OT_snapset_button_A,
    VIEW3D_OT_snapset_button_B,
    VIEW3D_OT_snapset_button_C,
    VIEW3D_OT_snapset_button_D,
    VIEW3D_OT_snapset_button_E,
    VIEW3D_OT_snapset_button_F,
    VIEW3D_OT_snapset_button_G,
    VIEW3D_OT_snapset_button_H,
    VIEW3D_OT_snapset_modal,
    VIEW3D_OT_pivot_target,
    VIEW3D_OT_orient_axis,
    VIEW3D_OT_snap_target,
    VIEW3D_OT_snap_element,
    VIEW3D_OT_snap_use,
    VIEW3D_MT_snapset_menu,
    VIEW3D_MT_snapset_menu_pie,
    VIEW3D_PT_snapset_panel_ui,
    VIEW3D_MT_snapset_menu_pencil,
    VIEW3D_MT_snapset_menu_editor,
    VIEW3D_PT_snapset_panel_editor,
    VIEW3D_MT_snapset_menu_special,
    VIEW3D_MT_snapset_menu_snapping,
    VIEW3D_OT_align_tools,
    VIEW3D_OT_align_mesh,
    VIEW3D_OT_looptools,
    VIEW3D_OT_3d_cursor_align,
    VIEW3D_OT_keymap_snapset,
    Addon_Preferences_Snapset,
    Global_Property_Group,
)

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.snap_global_props = bpy.props.PointerProperty(type=Global_Property_Group)   

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:   

        addon_prefs = context.preferences.addons[__name__].preferences
        if addon_prefs.toggle_snapset_add_tools == True:

            #km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('tpc_ot.snapset_modal', 
                                       addon_prefs.hotkey_button_m, 'PRESS', 
                                       ctrl=addon_prefs.hotkey_button_m_ctrl, 
                                       alt=addon_prefs.hotkey_button_m_alt, 
                                       shift=addon_prefs.hotkey_button_m_shift)
            kmi.properties.mode = "CUSTOM"                             
            addon_keymaps.append((km,kmi))
            

    update_snapset(None, bpy.context)
    update_snapset_menu(None, bpy.context)
    update_snapset_tools(None, bpy.context)
    update_panel(None, bpy.context)



def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    try:
        del bpy.types.WindowManager.snap_global_props
    except Exception as e:
        print('unregister fail:\n', e)
        pass

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    # clear the list
    addon_keymaps.clear()
    

if __name__ == "__main__":
    register()


