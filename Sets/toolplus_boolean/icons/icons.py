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
    
    mkb_icons.load("icon_boolean_carver", os.path.join(icons_dir, "boolean_carver.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_difference", os.path.join(icons_dir, "boolean_difference.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_exclude", os.path.join(icons_dir, "boolean_exclude.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_facemerge", os.path.join(icons_dir, "boolean_facemerge.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_intersect", os.path.join(icons_dir, "boolean_intersect.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_isolate", os.path.join(icons_dir, "boolean_isolate.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_rebool", os.path.join(icons_dir, "boolean_rebool.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_separate", os.path.join(icons_dir, "boolean_separate.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_substract", os.path.join(icons_dir, "boolean_substract.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_union", os.path.join(icons_dir, "boolean_union.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_weld", os.path.join(icons_dir, "boolean_weld.png"), 'IMAGE')

    mkb_icons.load("icon_origin_edm", os.path.join(icons_dir, "origin_edm.png"), 'IMAGE')
    mkb_icons.load("icon_origin_obm", os.path.join(icons_dir, "origin_obm.png"), 'IMAGE')

    mkb_icons.load("icon_remove_double", os.path.join(icons_dir, "remove_double.png"), 'IMAGE')

    mkb_icons.load("icon_select_link", os.path.join(icons_dir, "select_link.png"), 'IMAGE')

    
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False