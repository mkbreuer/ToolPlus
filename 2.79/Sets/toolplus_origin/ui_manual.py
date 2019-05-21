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
def VIEW3D_MT_Origin_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.tpc.OT_set_origin_to"                 , "/TP-Origin"),
        ("bpy.ops.tpc.OT_snaporigin_modal"              , "/TP-Origin"),
        ("bpy.ops.tpc.OT_origin_to_snap_helper"         , "/TP-Origin"),
        ("bpy.ops.tpc.OT_origin_ccc"                    , "/TP-Origin"),
        ("bpy.ops.tpc.OT_snap_to_bbox"                  , "/TP-Origin"),
        ("bpy.ops.tpc.OT_origin_to_bounding_box"        , "/TP-Origin"),
        ("bpy.ops.tp_ops.zero_axis"                     , "/TP-Origin"),
        ("bpy.ops.tpc.OT_distribute_objects"            , "/TP-Origin"),
        ("bpy.ops.tpc.OT_advanced_align_tools"          , "/TP-Origin"),
        ("bpy.ops.tpc.OT_origin_transform"              , "/TP-Origin"),
        ("bpy.data.window_managers.bbox_origin_window.display_origin_box"      , "/TP-Origin"),
        ("bpy.data.window_managers.bbox_origin_window.display_origin_editbox"  , "/TP-Origin"),
        )
    return url_manual_prefix, url_manual_mapping


