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

    mkb_icons.load("icon_align_zero", os.path.join(icons_dir, "align_zero.png"), 'IMAGE')
    
    mkb_icons.load("icon_cursor", os.path.join(icons_dir, "cursor.png"), 'IMAGE')

    mkb_icons.load("icon_origin_active", os.path.join(icons_dir, "origin_active.png"), 'IMAGE')
    mkb_icons.load("icon_origin_align", os.path.join(icons_dir, "origin_align.png"), 'IMAGE')
    mkb_icons.load("icon_origin_apply", os.path.join(icons_dir, "origin_apply.png"), 'IMAGE')
    mkb_icons.load("icon_origin_bbox", os.path.join(icons_dir, "origin_bbox.png"), 'IMAGE')
    mkb_icons.load("icon_origin_bottom", os.path.join(icons_dir, "origin_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_ccc", os.path.join(icons_dir, "origin_ccc.png"), 'IMAGE')
    mkb_icons.load("icon_origin_center", os.path.join(icons_dir, "origin_center.png"), 'IMAGE')
    mkb_icons.load("icon_origin_center_view", os.path.join(icons_dir, "origin_center_view.png"), 'IMAGE')
    mkb_icons.load("icon_origin_center_loc", os.path.join(icons_dir, "origin_center_loc.png"), 'IMAGE')
    mkb_icons.load("icon_origin_cross", os.path.join(icons_dir, "origin_cross.png"), 'IMAGE')
    mkb_icons.load("icon_origin_cursor", os.path.join(icons_dir, "origin_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_origin_diagonal", os.path.join(icons_dir, "origin_diagonal.png"), 'IMAGE')
    mkb_icons.load("icon_origin_distribute", os.path.join(icons_dir, "origin_distribute.png"), 'IMAGE')
    mkb_icons.load("icon_origin_edm", os.path.join(icons_dir, "origin_edm.png"), 'IMAGE')
    mkb_icons.load("icon_origin_left", os.path.join(icons_dir, "origin_left.png"), 'IMAGE')
    mkb_icons.load("icon_origin_left_bottom", os.path.join(icons_dir, "origin_left_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_left_top", os.path.join(icons_dir, "origin_left_top.png"), 'IMAGE')
    mkb_icons.load("icon_origin_mass", os.path.join(icons_dir, "origin_mass.png"), 'IMAGE')
    mkb_icons.load("icon_origin_meshto", os.path.join(icons_dir, "origin_meshto.png"), 'IMAGE')
    mkb_icons.load("icon_origin_obj", os.path.join(icons_dir, "origin_obj.png"), 'IMAGE')
    mkb_icons.load("icon_origin_right", os.path.join(icons_dir, "origin_right.png"), 'IMAGE')
    mkb_icons.load("icon_origin_right_bottom", os.path.join(icons_dir, "origin_right_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_right_top", os.path.join(icons_dir, "origin_right_top.png"), 'IMAGE')
    mkb_icons.load("icon_origin_selected", os.path.join(icons_dir, "origin_selected.png"), 'IMAGE')
    mkb_icons.load("icon_origin_tomesh", os.path.join(icons_dir, "origin_tomesh.png"), 'IMAGE')
    mkb_icons.load("icon_origin_top", os.path.join(icons_dir, "origin_top.png"), 'IMAGE')
    mkb_icons.load("icon_origin_copy", os.path.join(icons_dir, "origin_copy.png"), 'IMAGE')
    mkb_icons.load("icon_origin_tosnap", os.path.join(icons_dir, "origin_tosnap.png"), 'IMAGE')
    mkb_icons.load("icon_origin_toactive", os.path.join(icons_dir, "origin_toactive.png"), 'IMAGE')
    mkb_icons.load("icon_origin_mesh", os.path.join(icons_dir, "origin_mesh.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_active", os.path.join(icons_dir, "origin_to_active.png"), 'IMAGE')
    
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False