# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  



# DRAW UI LAYOUT #
class draw_snapset_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode           

    def draw(self, context):
        layout = self.layout.column_flow(align=True)  

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'    

        col = layout.column(align=True)
 
        box = col.box().column(align=True) 

        # USE BUTTONS #
        display_buttons_pl = context.user_preferences.addons[__package__].preferences.tab_display_buttons_pl
        if display_buttons_pl == 'on': 
           
           
            # NAMES / ICONS #  
            display_name_pl = context.user_preferences.addons[__package__].preferences.tab_display_name_pl
            if display_name_pl == 'both_id':  

                tx_snapset_active = "Active"
                tx_snapset_closet = "Closet"
                tx_snapset_cursor = "Cursor"
                tx_snapset_grid   = "Grid"
                tx_snapset_place  = "Place"
                tx_snapset_retopo = "Retopo"


            if display_name_pl == 'icon_id':  
       
                tx_snapset_active = " "
                tx_snapset_closet = " "
                tx_snapset_cursor = " "
                tx_snapset_grid   = " "
                tx_snapset_place  = " "
                tx_snapset_retopo = " "
 

            # OPTIONS #  
            if display_name_pl == 'both_id':  
                row = box.column(align=True)
            else:
                row = box.row(align=True)


            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tp_ops.place", text= tx_snapset_place, icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tp_ops.retopo", text= tx_snapset_retopo, icon_value=button_snap_retopo.icon_id)    

            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tp_ops.grid", text= tx_snapset_grid, icon_value=button_snap_grid.icon_id)

            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tp_ops.active_3d", text= tx_snapset_cursor, icon_value=button_snap_cursor.icon_id)                         

            button_snap_active = icons.get("icon_snap_active")
            row.operator("tp_ops.active_snap", text= tx_snapset_active, icon_value=button_snap_active.icon_id) 

            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tp_ops.closest_snap", text= tx_snapset_closet, icon_value=button_snap_closest.icon_id)


        # USE MENUS #
        else:

            # NAMES / ICONS #  
            display_name_pl = context.user_preferences.addons[__package__].preferences.tab_display_name_pl
            if display_name_pl == 'both_id':  
                                                    
                tx_snapset = " SnapSet"
  
            if display_name_pl == 'icon_id':  
      
                tx_snapset = " "

           
            # OPTIONS #  
            row = box.row(align=True)

            button_snap_set = icons.get("icon_snap_set") 
            row.menu("VIEW3D_TP_SnapSet_Menu_Panel", text= tx_snapset, icon_value=button_snap_set.icon_id) 





# LOAD UI: PANEL #
class VIEW3D_TP_SnapSet_Panel_TOOLS(bpy.types.Panel, draw_snapset_layout):
    bl_category = "Tools"
    bl_idname = "VIEW3D_TP_SnapSet_Panel_TOOLS"
    bl_label = "SnapSet"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_SnapSet_Panel_UI(bpy.types.Panel, draw_snapset_layout):
    bl_idname = "VIEW3D_TP_SnapSet_Panel_UI"
    bl_label = "SnapSet"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
