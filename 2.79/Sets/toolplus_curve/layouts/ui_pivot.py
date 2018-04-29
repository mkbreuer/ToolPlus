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
from .. icons.icons import load_icons

from toolplus_curve.menus.menu_delete  import (VIEW3D_TP_Delete_Menu_Curve)
from toolplus_curve.menus.menu_snapset import (VIEW3D_TP_SnapSet_Menu_Panel)


def draw_pivot_ui(self, context, layout):                   
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)                
        box = col.box().column(1)
        
        row = box.row(1)   
        
        box.separator()
                
        row = box.row(1) 
        row.scale_x = 1.55
        row.scale_y = 1.4
        button_snap_place = icons.get("icon_snap_place")
        row.menu("VIEW3D_TP_SnapSet_Menu_Panel", text="", icon_value=button_snap_place.icon_id) 
        row.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
        row.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
        row.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
        row.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
        row.operator("tp_ops.pivot_median", "" , icon="ROTATECENTER")    
        row.menu("tp_menu.curve_delete", "", icon="PANEL_CLOSE")     
  
        box.separator()

