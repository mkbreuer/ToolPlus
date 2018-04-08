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
def VIEW3D_TP_SnapSet_Manual():
    url_manual_prefix = "https://github.com/mkbreuer/Snap-Set"
    url_manual_mapping = (
        ("bpy.ops.tp_ops.active_snap"      , "/wiki"),
        ("bpy.ops.tp_ops.closest_snap"     , "/wiki"),
        ("bpy.ops.tp_ops.active_3d"        , "/wiki"),
        ("bpy.ops.tp_ops.grid"             , "/wiki"),
        ("bpy.ops.tp_ops.place"            , "/wiki"),
        ("bpy.ops.tp_ops.retopo"           , "/wiki"),
        )
    return url_manual_prefix, url_manual_mapping


