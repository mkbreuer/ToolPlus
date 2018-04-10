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


class VIEW3D_TP_Align_Menu_UV(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_uv" 

    def draw(self, context):
        layout = self.layout
      
        icons = load_icons()

        layout.scale_y = 1.5

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_x = icons.get("icon_align_x") 
        layout.operator("tp_ops.align_uv_image", text="X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'
      
        button_align_y = icons.get("icon_align_y") 
        layout.operator("tp_ops.align_uv_image", text="Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'
        
        button_align_xy = icons.get("icon_align_xy") 
        layout.operator("tp_ops.align_uv_image", text="Xy", icon_value=button_align_xy.icon_id).tp_axis ='axis_xy'

        layout.separator()

        layout.prop(bpy.context.scene, 'tp_pivot2', text="") 



class VIEW3D_TP_Align_Menu_Graph(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_graph" 

    def draw(self, context):
        layout = self.layout
        
        icons = load_icons()

        layout.scale_y = 1.5

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_x = icons.get("icon_align_x") 
        layout.operator("tp_ops.align_graph", text="X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'
        
        button_align_y = icons.get("icon_align_y") 
        layout.operator("tp_ops.align_graph", text="Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'
        
        button_align_xy = icons.get("icon_align_xy") 
        layout.operator("tp_ops.align_graph", text="Xy", icon_value=button_align_xy.icon_id).tp_axis ='axis_xy'

        layout.separator()

        layout.prop(bpy.context.scene, 'tp_pivot3', text="") 



class VIEW3D_TP_Align_Menu_Node(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_node" 

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()
      
        layout.scale_y = 1.5
       
        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_x = icons.get("icon_align_x") 
        layout.operator("tp_ops.align_node", text="X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'
      
        button_align_y = icons.get("icon_align_y") 
        layout.operator("tp_ops.align_node", text="Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'



