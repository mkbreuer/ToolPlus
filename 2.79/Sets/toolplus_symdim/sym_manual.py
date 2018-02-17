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
def VIEW3D_TP_SymDim_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/ToolPlus/wiki"
    url_manual_mapping = (
        ("bpy.ops.tp_ops.copy_dimension_axis"         , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_x_symcut"       , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_y_symcut"       , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_z_symcut"       , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_x_symcut"       , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_y_symcut"       , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_z_symcut"       , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_xy_symcut"      , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_xz_symcut"      , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_yz_symcut"      , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_xy_symcut"      , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_xz_symcut"      , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_yz_symcut"      , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_positiv_xyz_symcut"     , "/TP-SymDim"),
        ("bpy.ops.tp_ops.mods_negativ_xyz_symcut"     , "/TP-SymDim"),
        ("bpy.ops.tp_ops.normal_symcut"               , "/TP-SymDim"),
        )
    return url_manual_prefix, url_manual_mapping
