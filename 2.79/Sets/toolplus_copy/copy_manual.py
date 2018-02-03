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
def VIEW3D_TP_Copy_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.tp_ops.mft_radialclone"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.copy_to_cursor_panel"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.copy_to_meshtarget_pl"     , "/TP-Copy"),

        ("bpy.ops.tp_ops.origin_plus_z"             , "/TP-Copy"),
        ("bpy.ops.object.origin_set"                , "/TP-Copy"),
        ("bpy.ops.tp_ops.origin_minus_z"            , "/TP-Copy"),

        ("bpy.ops.tp_ops.x_array"                   , "/TP-Copy"),
        ("bpy.ops.tp_ops.y_array"                   , "/TP-Copy"),
        ("bpy.ops.tp_ops.z_array"                   , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_array"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_array_mods"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_curve"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_empty_curve_mods"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_curve_array"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_curve_array_mods"      , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_circle_array"          , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_circle_array_mods"     , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_fpath_curve"           , "/TP-Copy"),
        ("bpy.ops.tp_ops.add_fpath_con"             , "/TP-Copy"),
        )       
    return url_manual_prefix, url_manual_mapping


