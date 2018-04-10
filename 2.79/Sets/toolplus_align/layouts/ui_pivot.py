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

from toolplus_align.menus.menu_snapset      import  (VIEW3D_TP_SnapSet_Menu_Panel)

def draw_pivot_layout(self, context, layout):

    icons = load_icons()

    layout.operator_context = 'INVOKE_REGION_WIN'

    box = layout.box()
    
    row = box.row(1)  
    sub = row.row(1)
    sub.scale_x = 7

    sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
    sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
    sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
    sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
    sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")    

    button_snap_set = icons.get("icon_snap_set")
    sub.menu("VIEW3D_TP_SnapSet_Menu_Panel", text=" ", icon_value=button_snap_set.icon_id)  
