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
           

class VIEW3D_TP_Align_Menu_LoopTools(bpy.types.Menu):
    bl_label = "LoopTools"
    bl_idname = "VIEW3D_TP_Align_Menu_LoopTools" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = 1.2

        button_align_space = icons.get("icon_align_space")
        layout.operator("mesh.looptools_space", text="LpT  Space", icon_value=button_align_space.icon_id)
       
        button_align_curve = icons.get("icon_align_curve") 
        layout.operator("mesh.looptools_curve", text="LpT  Curve", icon_value=button_align_curve.icon_id)

        button_align_circle = icons.get("icon_align_circle") 
        layout.operator("mesh.looptools_circle", text="LpT  Circle", icon_value=button_align_circle.icon_id)

        button_align_flatten = icons.get("icon_align_flatten")                
        layout.operator("mesh.looptools_flatten", text="LpT  Circle", icon_value=button_align_flatten.icon_id)
 
        button_align_bridge = icons.get("icon_align_bridge")
        layout.operator("mesh.looptools_bridge", text="LpT  Bridge", icon_value=button_align_bridge.icon_id).loft = False        
