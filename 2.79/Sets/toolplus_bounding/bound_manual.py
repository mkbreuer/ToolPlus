# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


 # RIGHT CLICK BUTTON TO ONLINE MANUAL
def VIEW3D_TP_Bound_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.tp_ops.bbox_cube"                       , "/TP-Bounding"),
        ("bpy.ops.tp_ops.bbox_cylinder"                   , "/TP-Bounding"),
        ("bpy.ops.tp_ops.bbox_sphere"                     , "/TP-Bounding"),
        ("bpy.ops.tp_ops.bbox_select_box"                 , "/TP-Bounding"),
        ("bpy.ops.tp_ops.set_new_local"                   , "/TP-Bounding"),
        ("bpy.ops.tp_ops.recenter"                        , "/TP-Bounding"),
        ("bpy.ops.tp_ops.reposition"                      , "/TP-Bounding"),
        ("bpy.ops.tp_ops.copy_local_transform"            , "/TP-Bounding"),
        ("bpy.ops.object.transforms_to_deltas"            , "/TP-Bounding"),
        ("bpy.ops.tp_ops.relocate()"                      , "/TP-Bounding"),
        ("bpy.ops.tp_ops.delete_dummy"                    , "/TP-Bounding"),
        )
    return url_manual_prefix, url_manual_mapping


