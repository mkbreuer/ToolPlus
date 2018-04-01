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


class VIEW3D_TP_Header_CursorTo_Menu(bpy.types.Menu):
    bl_label = "Cursor to..."
    bl_idname = "VIEW3D_TP_Header_CursorTo_Menu"
    
    def draw(self, context):
        layout = self.layout

        icons = load_icons()
       
        layout.operator_context = 'INVOKE_REGION_WIN'
         
        layout.scale_y = 1.5

        if context.mode == 'OBJECT':
           
            button_snap_set = icons.get("icon_snap_set")            
            layout.operator("tp_ops.header_set_cursor", text="SnapPoint", icon_value = button_snap_set.icon_id)

        button_cursor_object = icons.get("icon_cursor_object")
        layout.operator("view3d.snap_cursor_to_selected", text="Selected", icon_value=button_cursor_object.icon_id)

        button_cursor_center = icons.get("icon_cursor_center")
        layout.operator("view3d.snap_cursor_to_center", text="Center", icon_value=button_cursor_center.icon_id)

        button_cursor_grid = icons.get("icon_cursor_grid")
        layout.operator("view3d.snap_cursor_to_grid", text="Grid", icon_value=button_cursor_grid.icon_id)

        button_cursor_active_obm = icons.get("icon_cursor_active_obm")
        layout.operator("view3d.snap_cursor_to_active", text="Active", icon_value=button_cursor_active_obm.icon_id)

        obj = context
        if obj and obj.mode == "EDIT_MESH":         
            
            button_cursor_3point_center = icons.get("icon_cursor_3point_center")           
            layout.operator("mesh.circlecentercursor", text="Circle", icon_value=button_cursor_3point_center.icon_id)   


class VIEW3D_TP_Header_SelectTo_Menu(bpy.types.Menu):
    bl_label = "Select to..."
    bl_idname = "VIEW3D_TP_Header_SelectTo_Menu"
    
    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.scale_y = 1.5

        button_select_grid = icons.get("icon_select_grid")
        layout.operator("view3d.snap_selected_to_grid", text="Grid", icon_value=button_select_grid.icon_id)
        
        button_select_center = icons.get("icon_select_center")
        layout.operator("view3d.snap_cursor_to_center", text="Center", icon_value=button_select_center.icon_id)

        button_select_cursor = icons.get("icon_select_cursor")           
        layout.operator("view3d.snap_selected_to_cursor", text="Cursor", icon_value=button_select_cursor.icon_id).use_offset=False

        button_select_cursor_offset_obm = icons.get("icon_select_cursor_offset_obm")           
        layout.operator("view3d.snap_selected_to_cursor", text="C-Offset", icon_value=button_select_cursor_offset_obm.icon_id).use_offset=True

        button_select_active_obm = icons.get("icon_select_active_obm")
        layout.operator("view3d.snap_selected_to_active", text="Active", icon_value=button_select_active_obm.icon_id)



