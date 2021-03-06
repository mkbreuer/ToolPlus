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


class VIEW3D_TP_SnapSet_Menu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_TP_SnapSet_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
        
        layout.scale_y = 1.3

        if context.mode == 'OBJECT':
            button_snap_place = icons.get("icon_snap_place")
            layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

        else:
            button_snap_retopo = icons.get("icon_snap_retopo")
            layout.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    


        button_snap_grid = icons.get("icon_snap_grid")
        layout.operator("tp_ops.grid", text="Grid", icon_value=button_snap_grid.icon_id)
                    
        button_snap_cursor = icons.get("icon_snap_cursor")           
        layout.operator("tp_ops.active_3d", text="Cursor3D", icon_value=button_snap_cursor.icon_id)  
 
        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_active.icon_id)

        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 



class VIEW3D_TP_SnapSet_Menu_Panel(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_TP_SnapSet_Menu_Panel"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
        
        layout.label("SnapSet")

        icons = load_icons()   
        
        layout.scale_y = 1.3

        if context.mode == 'OBJECT':
            button_snap_place = icons.get("icon_snap_place")
            layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

        else:
            button_snap_retopo = icons.get("icon_snap_retopo")
            layout.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    


        button_snap_grid = icons.get("icon_snap_grid")
        layout.operator("tp_ops.grid", text="Grid", icon_value=button_snap_grid.icon_id)
                    
        button_snap_cursor = icons.get("icon_snap_cursor")           
        layout.operator("tp_ops.active_3d", text="Cursor3D", icon_value=button_snap_cursor.icon_id)  
 
        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_active.icon_id)

        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 
