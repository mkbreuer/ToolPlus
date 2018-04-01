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


class VIEW3D_TP_Header_Ruler_Menu(bpy.types.Menu):
    bl_label = "Ruler"
    bl_idname = "VIEW3D_TP_Header_Ruler_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5      


        if context.mode == 'OBJECT':

            button_snap_ruler = icons.get("icon_snap_ruler") 
            layout.operator("tp_ops.np_020_point_distance", text='Point Distance', icon_value = button_snap_ruler.icon_id)
  
            button_ruler_triangle = icons.get("icon_ruler_triangle") 
            layout.operator("view3d.ruler", text='Interactive Ruler', icon_value = button_ruler_triangle.icon_id)         

        else:
   
            button_ruler_triangle = icons.get("icon_ruler_triangle") 
            layout.operator("view3d.ruler", text='Interactive Ruler', icon_value = button_ruler_triangle.icon_id)    
            
            layout.separator()
          
            mesh = context.active_object.data

            button_edge_lenght = icons.get("icon_edge_length") 
            layout.prop(mesh, "show_extra_edge_length", text="Edge Length", icon_value = button_edge_lenght.icon_id)

            button_edge_angle = icons.get("icon_edge_angle") 
            layout.prop(mesh, "show_extra_edge_angle", text="Edge Angle", icon_value = button_edge_angle.icon_id)

            layout.separator()   

            button_face_area = icons.get("icon_face_area") 
            layout.prop(mesh, "show_extra_face_area", text="Face Area", icon_value = button_face_area.icon_id)
          
            button_face_angle = icons.get("icon_face_angle") 
            layout.prop(mesh, "show_extra_face_angle", text="Face Angle", icon_value = button_face_angle.icon_id)
        