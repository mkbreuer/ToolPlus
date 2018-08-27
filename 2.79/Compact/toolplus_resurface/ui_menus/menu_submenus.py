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


import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



def Draw_VIEW3D_TP_Transform_Normal(self,context):
    layout = self.layout
    col = layout.column(align=True)

    col.operator("transform.tosphere", text="To Sphere")
    col.operator("transform.shear", text="Shear")
    col.operator("transform.bend", text="Bend")

    col.separator() 

    col.menu("tp_ops.translate_normal_menu", text="N-Translate")
    col.menu("tp_ops.rotate_normal_menu", text="N-Rotate")
    col.menu("tp_ops.resize_normal_menu", text="N-Scale")

    col.separator()     
