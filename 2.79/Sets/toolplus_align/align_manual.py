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
def VIEW3D_TP_Align_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.object.transform_apply"               , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_set_center"             , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_set_cursor"             , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_tomesh"                 , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_meshto"                 , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_set_mass"               , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_edm"                    , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_obm"                    , "/TP-Origin"),
        ("bpy.ops.tp_ops.origin_ccc"                    , "/TP-Origin"),
        ("bpy.ops.object.bbox_origin_modal_ops"         , "/TP-Origin"),
        ("bpy.ops.tp_ops.zero_axis"                     , "/TP-Origin"),
        ("bpy.ops.object.distribute_osc"                , "/TP-Origin"),
        ("bpy.ops.tp_origin.align_tools"                , "/TP-Origin"),
        ("bpy.data.window_managers.bbox_origin_window.display_origin_box"      , "/TP-Origin"),
        ("bpy.data.window_managers.bbox_origin_window.display_origin_editbox"  , "/TP-Origin"),
        )
    return url_manual_prefix, url_manual_mapping


def VIEW3D_TP_LoopTools_Manual():
    url_manual_prefix = "https://sites.google.com/site/bartiuscrouch/looptools/"
    url_manual_mapping = (
        ("bpy.ops.mesh.looptools_bridge"     , "/bridge"),
        ("bpy.ops.mesh.looptools_circle"     , "/circle"),
        ("bpy.ops.mesh.looptools_curve"      , "/curve"),
        ("bpy.ops.mesh.looptools_flatten"    , "/flatten"),
        ("bpy.ops.mesh.looptools_gstretch"   , "/gstretch"),
        ("bpy.ops.mesh.looptools_loft"       , "/loft"),
        ("bpy.ops.mesh.looptools_relax"      , "/relax"),
        ("bpy.ops.mesh.looptools_space"      , "/space"),
        )
    return url_manual_prefix, url_manual_mapping



def VIEW3D_TP_Machine_Manual():
    url_manual_prefix = "https://machin3.io/MESHmachine/docs/"
    url_manual_mapping = (
        ("bpy.ops.machin3.fuse"                , "/fuse"),
        ("bpy.ops.machin3.change_width"        , "/change_width"),
        ("bpy.ops.machin3.flatten"             , "/flatten"),
        ("bpy.ops.machin3.unfuck"              , "/unfuck"),
        ("bpy.ops.machin3.unfuse"              , "/unfuse"),
        ("bpy.ops.machin3.refuse"              , "/refuse"),
        ("bpy.ops.machin3.unbevel"             , "/unbevel"),
        ("bpy.ops.machin3.unchamfer"           , "/unchamfer"),
        ("bpy.ops.machin3.turn_corner"         , "/turn_corner"),
        ("bpy.ops.machin3.quad_corner"         , "/quad_corner"),
        )
    return url_manual_prefix, url_manual_mapping
