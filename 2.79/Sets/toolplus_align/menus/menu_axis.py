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


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons


class VIEW3D_TP_Axis_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Axis_Menu"
    bl_label = "Axis"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()
            
        col = split.column(1)

        col.scale_y = 1.3
      
        button_align_xy = icons.get("icon_align_xy") 
        col.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis ='axis_xy'

        button_align_zx = icons.get("icon_align_zx")
        col.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis ='axis_zx'

        button_align_zy = icons.get("icon_align_zy") 
        col.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis ='axis_zy'    
            

        col = split.column(1)            
      
        col.scale_y = 1.3

        button_align_x = icons.get("icon_align_x") 
        col.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'

        button_align_y = icons.get("icon_align_y") 
        col.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'           

        button_align_z = icons.get("icon_align_z") 
        col.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis ='axis_z'

