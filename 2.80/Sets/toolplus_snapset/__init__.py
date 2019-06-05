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
    "version": (0, 2, 6),
    "blender": (2, 80, 0),
    "location": "3D View > Tool- or Propertyshelf Panel [N], Menus [SHIFT+W], Special Menu [W], Shortcut [F], Header",
    "description": "fully customizable buttons for snapping",
    "warning": "/",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "category": "ToolPlus",
}


# LOAD MODULES #
import bpy
from bpy.props import *


# LOAD / RELOAD SUBMODULES #
import importlib
from . import developer_utils

# LOAD CUSTOM ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons

from .ot_custom         import *
from .ot_editor         import *
from .ot_modal          import *
from .ot_targets        import *

# LOAD UI # 
from .ui_panel          import *
from .ui_header         import *
from .ui_menu           import *
from .ui_menu_pie       import *
from .ui_menu_special   import *
from .ui_keymap         import *

importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())



# PANEL TO CONTAINING THE TOOLS #
class VIEW3D_PT_snapset_panel_ui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Test'
    bl_label = "SnapSet"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        draw_snapset_ui(self, context, layout)



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




# UPDATE TOOLS # not needed if we used bool props #
def update_snapset_tools(self, context):

    try:
        return True
    except:
        pass

    if context.preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None    


# ADDON PREFERENCES PANEL #
class Addon_Preferences_Snapset(bpy.types.AddonPreferences):
    bl_idname = __name__
    
    # PANEL # 
    category: StringProperty(
              name="Tab Category",
              description="Choose a name for the category of the panel",
              default="Tools",
              update=update_panel
              )

   
    # INFO LIST #
    prefs_tabs:EnumProperty(
        items=(('info',  "Info",   "Info"),
               ('panel', "Panel",  "Panel"),
               ('menus', "Menus",  "Menus"),
               ('tools', "Tools",  "Tools")),
        default='info')

    #------------------------------

    # PANEL #          

    tab_display_buttons_pl:EnumProperty(
        name = 'Buttons or Menus', 
        description = 'on = only butttons / off = use menus',
        items=(('off', 'Use Menus',   'enable tools in header'), 
               ('on',  'Use Buttons', 'disable tools in header')), 
        default='on', update = update_snapset_tools)

    tab_display_name_pl:EnumProperty(
        name = 'Name & Icon Toggle', 
        description = 'on / off',
        items=(('both_id', 'Show Name & Icon', 'keep names and icons visible in header menus'), 
               ('icon_id', 'Show only Icons',   'disable icons in header menus')), 
        default='both_id', update = update_snapset_tools)


    #------------------------------


    # MENU #
    tab_snapset_menu:EnumProperty(
        name = '3D View Menu',
        description = 'enable or disable menu for 3D View',
        items=(('menu',   'Use Menu', 'enable menu for 3D View'),
               ('pie',    'Use Pie',  'enable pie for 3D View'),
               ('remove', 'Disable',  'disable menus for 3D View')),
        default='menu', update = update_snapset_menu)


    # SPECIAL W SUBMENUS #    
    tab_snapset_special:EnumProperty(
        name = 'Append to Special Menu',
        description = 'menu for special menu',
        items=(('prepend', 'Menu Top',    'add menus to default special menus'),
               ('append',  'Menu Bottom', 'add menus to default special menus'),
               ('remove',  'Menu Remove', 'remove menus from default menus')),
        default='remove', update = update_snapset_special)               

    toggle_special_snapset_separator:bpy.props.BoolProperty(name="Toggle SubSeparator", description="on / off", default=True)   
    toggle_special_snapset_icon:bpy.props.BoolProperty(name="Toggle SubMenu Icon", description="on / off", default=False)   


    #----------------------------


    # HEADER #
    expand_panel_tools:bpy.props.BoolProperty(name="Expand", description="Expand, to display the settings", default=False)    

    tab_snapset_header:EnumProperty(
        name = 'Header Menu',
        description = 'enable or disable menu for Header',
        items=(('add',    'Menu on',  'enable menu for Header'),
               ('remove', 'Menu off', 'disable menu for Header')),
        default='remove', update = update_snapset_header)

    tab_display_buttons:EnumProperty(
        name = 'Buttons or Menus', 
        description = 'on = only butttons / off = use menus',
        items=(('off', 'Use Menus',   'enable tools in header'), 
               ('on',  'Use Buttons', 'disable tools in header')), 
        default='off', update = update_snapset_tools)

    tab_display_name:EnumProperty(
        name = 'Name & Icon Toggle', 
        description = 'on / off',
        items=(('both_id', 'Show Name & Icon', 'keep names and icons visible in header menus'), 
               ('icon_id', 'Show only Icons',   'disable icons in header menus')), 
        default='both_id', update = update_snapset_tools)


    #----------------------------


    # TOOLS #

    tab_button_type:EnumProperty(
        name = 'Button Menu',
        description = 'choose settings for the buttons',
        items=(('button_a', 'Button A', 'button settings'),
               ('button_b', 'Button B', 'button settings'),
               ('button_c', 'Button C', 'button settings'),
               ('button_d', 'Button D', 'button settings'),
               ('button_e', 'Button E', 'button settings'),
               ('button_f', 'Button F', 'button settings'),
               ('button_m', 'Button M', 'modal settings')),
        default='button_a')

    tpc_use_grid:BoolProperty(name= 'Snap Grid', description = 'botton in menu', default=True)   
    tpc_use_place:BoolProperty(name= 'Snap Place', description = 'botton in menu', default=True)   
    tpc_use_retopo:BoolProperty(name= 'Snap Retopo', description = 'botton in menu', default=True)   
    tpc_use_cursor:BoolProperty(name= 'Snap Cursor', description = 'botton in menu', default=True)   
    tpc_use_closest:BoolProperty(name= 'Snap Closest', description = 'botton in menu', default=True)   
    tpc_use_active:BoolProperty(name= 'Snap Active', description = 'botton in menu', default=True)   

    tpc_use_grid_modal:BoolProperty(name= 'Grid Modal', description = 'botton in menu', default=True)   
    tpc_use_place_modal:BoolProperty(name= 'Place Modal', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal:BoolProperty(name= 'Retopo Modal', description = 'botton in menu', default=True)   
    tpc_use_grid_modal_panel:BoolProperty(name= 'Grid Modal', description = 'botton in menu', default=True)   
    tpc_use_place_modal_panel:BoolProperty(name= 'Place Modal', description = 'botton in menu', default=True)   
    tpc_use_retopo_modal_panel:BoolProperty(name= 'Retopo Modal', description = 'botton in menu', default=True) 
    tpc_use_custom_modal_panel:BoolProperty(name= 'Custom Modal', description = 'botton in menu', default=True)   

    tab_snapset_add_tools:BoolProperty(name= 'Append hotkey to the preference keymap', description = 'append to keymap', default=False)   

    tpc_use_snap:BoolProperty(name= 'Toggle permanent Snap', description = 'toggle snap on or off', default=True)    
    tpc_use_emposs:BoolProperty(name= 'Toggle transparent for button backround', description = 'toggle emboss on or off', default=False)    


    #----------------------------

    
    # BUTTON A = GRID #
    name_bta:bpy.props.StringProperty(default="Grid") 
    icon_bta:bpy.props.StringProperty(default="BLENDER") 
    use_internal_icon_bta:BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_bta_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='BOUNDING_BOX_CENTER') 

    prop_bta_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_bta_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='INCREMENT') 

    prop_bta_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 

    prop_bta_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=True)  
    prop_bta_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_bta_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_bta_project:BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_bta_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_bta_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_bta_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_bta_scale : BoolProperty(name= 'Scale', description = '', default=False)  


    #----------------------------
    

    # BUTTON B = PLACE #
    name_btb:bpy.props.StringProperty(default="Place") 
    icon_btb:bpy.props.StringProperty(default="BLENDER") 
    use_internal_icon_btb:BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btb_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btb_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btb_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='FACE') 

    prop_btb_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 

    prop_btb_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btb_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btb_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=True)  
    prop_btb_project:BoolProperty(name= 'Project Individual Elements', description = '', default=True)  
    prop_btb_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btb_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btb_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btb_scale : BoolProperty(name= 'Scale', description = '', default=False)  


    #----------------------------
    

    # BUTTON C = 3D CURSOR #
    name_btc:bpy.props.StringProperty(default="Cursor") 
    icon_btc:bpy.props.StringProperty(default="BLENDER") 
    use_internal_icon_btc:BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btc_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='CURSOR') 

    prop_btc_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btc_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='VERTEX') 

    prop_btc_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 

    prop_btc_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btc_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btc_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=True)  
    prop_btc_project:BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btc_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btc_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btc_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btc_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    prop_btc_cursor_use:BoolProperty(name= 'Cursor to Active', description = '', default=False)  
   
    prop_btc_cursor:bpy.props.EnumProperty(
        name = "3d Cursor to...", 
        items=[("tpc_active" ,"Active"   ,"Active"   ,"" , 1),                                     
               ("tpc_select" ,"Selected" ,"Selected" ,"" , 2)],
        default = "tpc_active")


    #----------------------------
    

    # BUTTON D = ACTIVE #
    name_btd:bpy.props.StringProperty(default="Active") 
    icon_btd:bpy.props.StringProperty(default="BLENDER") 
    use_internal_icon_btd:BoolProperty(name= 'Internal Icon', description = '', default=False)  
 
    prop_btd_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btd_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btd_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='VERTEX') 

    prop_btd_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='ACTIVE') 

    prop_btd_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btd_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=True)  
    prop_btd_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_btd_project:BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btd_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btd_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btd_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btd_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    
    #----------------------------
    

    # BUTTON E = CLOSESET #
    name_bte:bpy.props.StringProperty(default="Closest") 
    icon_bte:bpy.props.StringProperty(default="BLENDER") 
    use_internal_icon_bte:BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_bte_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='MEDIAN_POINT') 

    prop_bte_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_bte_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='VERTEX') 

    prop_bte_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 

    prop_bte_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_bte_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=True)  
    prop_bte_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_bte_project:BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_bte_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_bte_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_bte_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_bte_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    #----------------------------
    

    # BUTTON F = RETOPO #
    name_btf:bpy.props.StringProperty(default="Retopo") 
    icon_btf:bpy.props.StringProperty(default="BLENDER") 
    use_internal_icon_btf:BoolProperty(name= 'Internal Icon', description = '', default=False)  

    prop_btf_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='BOUNDING_BOX_CENTER') 

    prop_btf_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  


    prop_btf_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='FACE') 

    prop_btf_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 


    prop_btf_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btf_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btf_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=False)  
    prop_btf_project:BoolProperty(name= 'Project Individual Elements', description = '', default=False)  
    prop_btf_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btf_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btf_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btf_scale : BoolProperty(name= 'Scale', description = '', default=False)  


    #----------------------------
    

    # BUTTON MODAL = HOTKEY = PLACE #
    name_btM:bpy.props.StringProperty(default="Place") 

    prop_btM_pivot:EnumProperty(
        name = 'Pivot Point', 
        description = 'transform pivot point',
        items=(('BOUNDING_BOX_CENTER',  'Bounding Box Center', 'transform pivot point'), 
               ('CURSOR',               'Cursor',              'transform pivot point'), 
               ('INDIVIDUAL_ORIGINS',   'Individual Orign',    'transform pivot point'), 
               ('MEDIAN_POINT',         'Median Point',        'transform pivot point'), 
               ('ACTIVE_ELEMENT',       'Active Element',      'transform pivot point')), 
        default='ACTIVE_ELEMENT') 

    prop_btM_use_pivot:BoolProperty(name= 'Origin Only', description = '', default=False)  

    prop_btM_elements:EnumProperty(
        name = 'Snap Elements', 
        description = 'snap elements',
        items=(('INCREMENT',  'Increment',  'snap elements'), 
               ('VERTEX',     'Vertex',     'snap elements'), 
               ('EDGE',       'Edge',       'snap elements'), 
               ('FACE',       'Face',       'snap elements'), 
               ('VOLUME',     'Volume',     'snap elements')), 
        default='FACE') 

    prop_btM_target:EnumProperty(
        name = 'Snap Target', 
        description = 'snap target',
        items=(('CLOSEST', 'Closest', 'snap target'), 
               ('CENTER',  'Center',  'snap target'), 
               ('MEDIAN',  'Median',  'snap target'), 
               ('ACTIVE',  'Active',  'snap target')), 
        default='CLOSEST') 

    prop_btM_absolute_grid:BoolProperty(name= 'Absolute Grid Snap', description = '', default=False)  
    prop_btM_snap_self:BoolProperty(name= 'Project onto Self', description = '', default=False)  
    prop_btM_align_rotation:BoolProperty(name= 'Align Rotation to Target', description = '', default=True)  
    prop_btM_project:BoolProperty(name= 'Project Individual Elements', description = '', default=True)  
    prop_btM_peel_object:BoolProperty(name= 'Snap Peel Object', description = '', default=False)  
    
    prop_btM_translate : BoolProperty(name= 'Move', description = '', default=True)  
    prop_btM_rotation : BoolProperty(name= 'Rotation', description = '', default=False)  
    prop_btM_scale : BoolProperty(name= 'Scale', description = '', default=False)  

    hotkey_button_m:bpy.props.StringProperty(name = 'Key', default="F", description = 'change hotkey / only capital letters allowed') 
    hotkey_button_m_ctrl:BoolProperty(name= 'use Ctrl', description = 'enable ctrl for button m', default=False) 
    hotkey_button_m_alt:BoolProperty(name= 'use Alt', description = 'enable ctrl for button m', default=False) 
    hotkey_button_m_shift:BoolProperty(name= 'use Shift', description = 'enable ctrl for button m', default=False) 


    #----------------------------
    
    
    # DRAW PREFENCES #
    def draw(self, context):
        layout = self.layout

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
            row.label(text="> This addon contains snap setting presets for the 3d view.")       
            row.label(text="> They change the pivot and snap functions for respective task at the same time.")                     
                       
            row.separator()             
          
            row.label(text="> Have Fun! ;)")  
        
            box.separator() 



        # TOOLS #
        if self.prefs_tabs == 'tools':
            
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
            row.label(text="> Button F replace Button B in editmode.")  
            row.label(text="> Button M to use with a keyboard shortcut.")  
            
            box.separator() 
            box.separator() 
           
            row = box.row(align=False)
            row.prop(self, "tab_button_type", expand=True)             
            
            box.separator() 

            if self.tab_button_type == 'button_a':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_bta", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_bta", text="Use Internal or Custom Icon")     
            
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


            if self.tab_button_type == 'button_b':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btb", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btb", text="Use Internal or Custom Icon")     
            
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
                        row.prop(self, "pro_btb_project")  
                   
                    if self.prop_btb_elements == "VOLUME":
                        row.prop(self, "prop_btb_peel_object")  
         
                box.separator() 

                row = box.row(align=True)
                row.prop(self, "prop_btb_translate")  
                row.prop(self, "prop_btb_rotation")  
                row.prop(self, "prop_btb_scale")  

                box.separator() 


            if self.tab_button_type == 'button_c':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btc", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btc", text="Use Internal or Custom Icon")     
            
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


            if self.tab_button_type == 'button_d':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btd", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btd", text="Use Internal or Custom Icon")     
            
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


            if self.tab_button_type == 'button_e':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_bte", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_bte", text="Use Internal or Custom Icon")     
            
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
                


            if self.tab_button_type == 'button_f':

                box.separator() 

                row = box.row(align=False)
                row.prop(self, "name_btf", text="Custom Name")   
 
                box.separator()              
                box.separator()              

                row = box.row(align=False)                    
                row.prop(self, "use_internal_icon_btf", text="Use Internal or Custom Icon")     
            
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



            if self.tab_button_type == 'button_m':
             
                box.separator()
             
                row = box.row(align=True)  
                row.label(text="Button M = Modal Hotkey Operator", icon ="COLLAPSEMENU")         
             
                box.separator() 

                row = box.row(align=True)  
                row.prop(self, 'tab_snapset_add_tools', expand=True)

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
         
            row = box.column(align=False)
            row.label(text="Icons", icon="INFO")
            row.label(text="> images in the addon icon folder.")
            row.label(text="> they can be exchanged by other one.")

            row.separator()
         
            row.label(text="> to use internal icons: enable the addon icon viewer for text editor.")
            row.label(text="> it shows all icons that blender use.")
            row.label(text="> attention: the icon names have always to be written as capitalization.")

            box.separator()



        # LOCATION #
        if self.prefs_tabs == 'panel':
            
            box = layout.box().column(align=True)
             
            row = box.row(align=True) 
            row.label(text="Panel Location:")

            box.separator() 
        
            row = box.row(align=True)            
            row.prop(self, "category")

            box.separator() 
            box.separator() 

            row = box.row()           
            row.label(text=" ")   
            row.prop(self, 'tab_display_buttons_pl',  expand=True)
       
            box.separator() 

            row = box.row()                  
            row.label(text=" ")   
            row.prop(self, 'tab_display_name_pl',  expand=True)

            box.separator() 
            box.separator() 

            row = box.row(align=True)    
            row.label(text="Append function to the panel", icon ="COLLAPSEMENU")       
           
            box.separator()            
           
            row = box.row(align=True)   
            row.prop(self, "tpc_use_grid_modal_panel")      
            row.prop(self, "tpc_use_place_modal_panel")    
            row.prop(self, "tpc_use_retopo_modal_panel")   

            box.separator() 

     
            

        # APPEND #
        if self.prefs_tabs == 'menus':

            col = layout.column(align=True)   

            box = col.box().column(align=True)
           
            box.separator()            
           
            row = box.row(align=True)    
            row.label(text="Append Function to 3D View Header", icon ="COLLAPSEMENU")       

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snapset_header', expand=True)

            box.separator() 

            row = box.row()           
            row.prop(self, 'tab_display_buttons',  expand=True)
       
            box.separator() 

            row = box.row()                  
            row.prop(self, 'tab_display_name',  expand=True)

            box.separator() 

            #-----------------------------------------------------
          
            box.separator() 
            box = col.box().column(align=True)         
            box.separator()
         
            row = box.row(align=True)  
            row.label(text="Special Menu [W]", icon ="COLLAPSEMENU")         

            box.separator()            
         
            row = box.column(align=True)          
            row.label(text="A snapset menu will be added to the default special menu.")

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snapset_special', expand=True)

            if self.tab_snapset_special == 'remove':
                pass
            else:

                box.separator() 

                row = box.column(align=True)  
                row.prop(self, 'toggle_special_snapset_separator')
                row.prop(self, 'toggle_special_snapset_icon')

            box.separator()

            #-----------------------------------------------------
         
            box.separator()
            box = col.box().column(align=True)
            box.separator()
            
            row = box.row(align=True)  
            row.label(text="Context Menu: [SHIFT+W] ", icon ="COLLAPSEMENU")        

            box.separator() 

            row = box.row(align=True)  
            row.prop(self, 'tab_snapset_menu', expand=True)

            if self.tab_snapset_menu == 'pie': 
               
                box.separator()   
              
                row = box.column(align=True)                                                  
                row.label(text="> This menu is always a proposal.")
                row.label(text="> Left or right, up or down, there are too many preferences,")
                row.label(text="> to create a pie menu for everyone.")
                row.label(text="> But it would be handy if you work with a bigger screen.")
            
                box.separator() 
                box.separator() 

                row = box.row()                  
                row.prop(self, 'tpc_use_emposs')

                box.separator() 
             
                row = box.column(align=True)    
                row.label(text="> only for the pie menu.")
                row.label(text="> if off the active function (icons) have a transparent backround.")

           
           
            if self.tab_snapset_menu == 'menu': 
                
                box.separator() 
              
                row = box.column(align=False)
                row.label(text="Order of tools in menu:")   

                box.separator() 
     
                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_grid", text='')  
                
                button_snap_grid = icons.get("icon_snap_grid")
                row.label(text="Grid", icon_value=button_snap_grid.icon_id)
                row.label(text="> snap pivot with absolute grid alignment")   
             
                box.separator() 

                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_grid_modal", text='')  
                
                button_snap_grid = icons.get("icon_snap_grid")
                row.label(text="GridM (*)", icon_value=button_snap_grid.icon_id)
                row.label(text="> snap pivot with absolute grid alignment til release")              

                box.separator()            
               
                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_place", text='')   
               
                button_snap_place = icons.get("icon_snap_place")
                row.label(text="Place", icon_value=button_snap_place.icon_id)             
                row.label(text="> snap pivot to surface of other objects")   

                box.separator() 
               
                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_place_modal", text='')   
               
                button_snap_place = icons.get("icon_snap_place")
                row.label(text="PlaceM (*)", icon_value=button_snap_place.icon_id)             
                row.label(text="> snap pivot to surface of other objects til release")   

                box.separator()            
               
                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_cursor", text='') 

                button_snap_cursor = icons.get("icon_snap_cursor")           
                row.label(text="Cursor", icon_value=button_snap_cursor.icon_id) 
                row.label(text="> set 3d cursor to active or selected")   
               
                box.separator()            
               
                row = box.row(align=False)
                row.alignment = 'LEFT' 
                row.prop(self, "tpc_use_closest", text='')  

                button_snap_closest = icons.get("icon_snap_closest")
                row.label(text="Closest", icon_value=button_snap_closest.icon_id)            
                row.label(text="> snap closest point onto target")   
                
                box.separator()            
               
                row = box.row(align=False)
                row.alignment = 'LEFT'  
                row.prop(self, "tpc_use_active", text='')
              
                button_snap_active = icons.get("icon_snap_active")            
                row.label(text="Active", icon_value=button_snap_active.icon_id) 
                row.label(text="> snap active pivot onto target")   
               
                box.separator()           
               
                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_retopo", text='')  
              
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.label(text="Retopo", icon_value=button_snap_retopo.icon_id) 
                row.label(text="> snap selected onto target in editmode")   
              
                box.separator()           
               
                row = box.row(align=False)
                row.alignment = 'LEFT'
                row.prop(self, "tpc_use_retopo_modal", text='')  
              
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.label(text="RetopoM (*)", icon_value=button_snap_retopo.icon_id) 
                row.label(text="> snap selected onto target in editmode til release")  

                box.separator() 
                box = layout.box().column(align=True)
                box.separator() 
          
                row = box.column(align=False)              
                row.label(text="(*) Modal Tools:")   
                row.label(text="> After execute the snap setting toggle to the needed preference.")   
                row.label(text="> When finished the settings switch back to the previous one.")   
                
                box.separator() 
          
                row = box.column(align=False)              
                row.label(text="Checkbox:", icon='CHECKBOX_HLT')   
                row.label(text="> toggle the tools in the menus on or off.")   

 
            box.separator()

            #-----------------------------------------------------
           
            box.separator()
            box = col.box().column(align=True)           
            box.separator()              
           

            # TIP #            
            row = box.row(align=True)             
            row.label(text="! For key change go to > Edit: Preferences > Keymap !", icon ="INFO")

            row = box.column(align=True) 
            row.label(text="1 > change search to key-bindig and insert the hotkey: shift w or f", icon ="BLANK1")
            row.label(text="2 > go to 3D View > Call Menu [SHIFT+W]: VIEW3D_TP_SnapSet_Menu /_Pie!", icon ="BLANK1")
            row.label(text="3 > go to Objectmode > Operator [F]: tpc_ot.snapset_modal!", icon ="BLANK1")
            row.label(text="4 > choose a new key configuration and save preferences !", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)             
            row.label(text="Or edit the keymap script directly:", icon ="BLANK1")

            box.separator()  

            row = box.row(align=True)  
            row.label(text="", icon ="BLANK1")
            row.operator("tpc_ot.keymap_snapset", text = 'Open KeyMap in Text Editor')
            row.operator('wm.url_open', text = 'Type of Events').url = "https://github.com/mkbreuer/Misc-Share-Archiv/blob/master/images/SHORTCUTS_Type%20of%20key%20event.png?raw=true"
            
            box.separator()




addon_keymaps = []


# REGISTER #
classes = (
    VIEW3D_PT_snapset_panel_ui,
    VIEW3D_OT_KeyMap_Snapset,
    VIEW3D_OT_Snapset_Button_A,
    VIEW3D_OT_Snapset_Button_B,
    VIEW3D_OT_Snapset_Button_C,
    VIEW3D_OT_Snapset_Button_D,
    VIEW3D_OT_Snapset_Button_E,
    VIEW3D_OT_Snapset_Button_F,
    VIEW3D_OT_Snapset_Modal,
    VIEW3D_OT_PIVOT_TARGET,
    VIEW3D_OT_ORIENT_AXIS,
    VIEW3D_OT_SNAP_TARGET,
    VIEW3D_OT_SNAP_ELEMENT,
    VIEW3D_OT_SNAP_USE,
    VIEW3D_MT_SnapSet_Menu_Panel,
    VIEW3D_MT_SnapSet_Menu_Pencil,
    VIEW3D_MT_SnapSet_Menu_Special,
    VIEW3D_MT_SnapSet_Header_Menu,
    Addon_Preferences_Snapset,
)

import bpy.utils.previews

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:   

        addon_prefs = context.preferences.addons[__name__].preferences
        if addon_prefs.tab_snapset_add_tools == True:

            #km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('tpc_ot.snapset_modal', 
                                       addon_prefs.hotkey_button_m, 'PRESS', 
                                       ctrl=addon_prefs.hotkey_button_m_ctrl, 
                                       alt=addon_prefs.hotkey_button_m_alt, 
                                       shift=addon_prefs.hotkey_button_m_ctrl)
            kmi.properties.mode = "CUSTOM"                             
            addon_keymaps.append((km,kmi))

    update_snapset_menu(None, bpy.context)
    update_snapset_special(None, bpy.context)
    update_snapset_header(None, bpy.context)
    update_snapset_tools(None, bpy.context)
    update_panel(None, bpy.context)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    # clear the list
    addon_keymaps.clear()
    

if __name__ == "__main__":
    register()


