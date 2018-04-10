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


class VIEW3D_TP_Align_Menu_Gstretch(bpy.types.Menu):
    bl_label = "Gstretch"
    bl_idname = "VIEW3D_TP_Align_Menu_Gstretch" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = 1.3
        
        layout.operator("tp_ops.surface_pencil", text="Draw",icon="GREASEPENCIL")    
        layout.operator("mesh.looptools_gstretch", text="Gstretch", icon='IPO_EASE_IN_OUT')    
        layout.operator("remove.gp", text="Remove", icon="PANEL_CLOSE")    

