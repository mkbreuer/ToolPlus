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


import os
import bpy
import bpy.utils.previews

toolplus_icon_collections = {}
toolplus_icons_loaded = False

def load_icons():
    global toolplus_icon_collections
    global toolplus_icons_loaded

    if toolplus_icons_loaded: return toolplus_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))

    mkb_icons.load("icon_axis_x", os.path.join(icons_dir, "axis_x.png"), 'IMAGE')    
    mkb_icons.load("icon_axis_xyz_planes", os.path.join(icons_dir, "axis_xyz_planes.png"), 'IMAGE')
    mkb_icons.load("icon_axis_y", os.path.join(icons_dir, "axis_y.png"), 'IMAGE')
    mkb_icons.load("icon_axis_z", os.path.join(icons_dir, "axis_z.png"), 'IMAGE')
    mkb_icons.load("icon_axis_n", os.path.join(icons_dir, "axis_n.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_carver", os.path.join(icons_dir, "boolean_carver.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_union", os.path.join(icons_dir, "boolean_union.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_intersect", os.path.join(icons_dir, "boolean_intersect.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_difference", os.path.join(icons_dir, "boolean_difference.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_rebool", os.path.join(icons_dir, "boolean_rebool.png"), 'IMAGE')
    
    mkb_icons.load("icon_boolean_union_brush", os.path.join(icons_dir, "boolean_union_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_intersect_brush", os.path.join(icons_dir, "boolean_intersect_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_difference_brush", os.path.join(icons_dir, "boolean_difference_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_rebool_brush", os.path.join(icons_dir, "boolean_rebool_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_draw", os.path.join(icons_dir, "boolean_draw.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_bevel", os.path.join(icons_dir, "boolean_bevel.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_edge", os.path.join(icons_dir, "boolean_edge.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_bridge", os.path.join(icons_dir, "boolean_bridge.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_sym", os.path.join(icons_dir, "boolean_sym.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_pipe", os.path.join(icons_dir, "boolean_pipe.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_custom", os.path.join(icons_dir, "boolean_custom.png"), 'IMAGE')
    
    mkb_icons.load("icon_boolean_separate", os.path.join(icons_dir, "boolean_separate.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_substract", os.path.join(icons_dir, "boolean_substract.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_weld", os.path.join(icons_dir, "boolean_weld.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_isolate", os.path.join(icons_dir, "boolean_isolate.png"), 'IMAGE')   

    mkb_icons.load("icon_boolean_exclude", os.path.join(icons_dir, "boolean_exclude.png"), 'IMAGE') 
    mkb_icons.load("icon_boolean_facemerge", os.path.join(icons_dir, "boolean_facemerge.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_apply", os.path.join(icons_dir, "boolean_apply.png"), 'IMAGE')

    mkb_icons.load("icon_origin_edm", os.path.join(icons_dir, "origin_edm.png"), 'IMAGE')
    mkb_icons.load("icon_origin_obm", os.path.join(icons_dir, "origin_obm.png"), 'IMAGE')

    mkb_icons.load("icon_remove_double", os.path.join(icons_dir, "remove_double.png"), 'IMAGE')

    mkb_icons.load("icon_select_link", os.path.join(icons_dir, "select_link.png"), 'IMAGE')

    mkb_icons.load("icon_wire_on", os.path.join(icons_dir, "wire_on.png"), 'IMAGE')
    mkb_icons.load("icon_wire_off", os.path.join(icons_dir, "wire_off.png"), 'IMAGE')
    
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]


def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False