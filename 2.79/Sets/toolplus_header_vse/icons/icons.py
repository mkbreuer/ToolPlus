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
  
    # LIST OF ICONS     
    mkb_icons.load("cut_soft", os.path.join(icons_dir, "cut_soft.png"), 'IMAGE')
    mkb_icons.load("cut_hard", os.path.join(icons_dir, "cut_hard.png"), 'IMAGE')
    mkb_icons.load("gap_insert", os.path.join(icons_dir, "gap_insert.png"), 'IMAGE')
    mkb_icons.load("gap_remove", os.path.join(icons_dir, "gap_remove.png"), 'IMAGE')
    mkb_icons.load("meta_make", os.path.join(icons_dir, "meta_make.png"), 'IMAGE')
    mkb_icons.load("meta_separate", os.path.join(icons_dir, "meta_separate.png"), 'IMAGE')
    mkb_icons.load("snap", os.path.join(icons_dir, "snap.png"), 'IMAGE')
    mkb_icons.load("mute_unselected", os.path.join(icons_dir, "mute_unselected.png"), 'IMAGE')
    mkb_icons.load("deinterlace", os.path.join(icons_dir, "deinterlace.png"), 'IMAGE')
    mkb_icons.load("swap_right", os.path.join(icons_dir, "swap_right.png"), 'IMAGE')
    mkb_icons.load("swap_left", os.path.join(icons_dir, "swap_left.png"), 'IMAGE')
    mkb_icons.load("clear_offset", os.path.join(icons_dir, "clear_offset.png"), 'IMAGE')
    mkb_icons.load("time_extend", os.path.join(icons_dir, "time_extend.png"), 'IMAGE')
    mkb_icons.load("view_selected", os.path.join(icons_dir, "view_selected.png"), 'IMAGE')
    mkb_icons.load("view_all", os.path.join(icons_dir, "view_all.png"), 'IMAGE')
    mkb_icons.load("range_set", os.path.join(icons_dir, "range_set.png"), 'IMAGE')
    mkb_icons.load("range_clear", os.path.join(icons_dir, "range_clear.png"), 'IMAGE')
    mkb_icons.load("select_all_left", os.path.join(icons_dir, "select_all_left.png"), 'IMAGE')
    mkb_icons.load("select_left", os.path.join(icons_dir, "select_left.png"), 'IMAGE')
    mkb_icons.load("select_all_right", os.path.join(icons_dir, "select_all_right.png"), 'IMAGE')
    mkb_icons.load("select_right", os.path.join(icons_dir, "select_right.png"), 'IMAGE')
    mkb_icons.load("select_handle_left", os.path.join(icons_dir, "select_handle_left.png"), 'IMAGE')
    mkb_icons.load("select_handle_both", os.path.join(icons_dir, "select_handle_both.png"), 'IMAGE')
    mkb_icons.load("select_handle_right", os.path.join(icons_dir, "select_handle_right.png"), 'IMAGE')
    mkb_icons.load("add_strips", os.path.join(icons_dir, "add_strips.png"), 'IMAGE')
    mkb_icons.load("add_effects", os.path.join(icons_dir, "add_effects.png"), 'IMAGE')
    mkb_icons.load("marker_delete", os.path.join(icons_dir, "marker_delete.png"), 'IMAGE')
    mkb_icons.load("marker_dupli", os.path.join(icons_dir, "marker_dupli.png"), 'IMAGE')
    mkb_icons.load("marker_dupli_scene", os.path.join(icons_dir, "marker_dupli_scene.png"), 'IMAGE')
    mkb_icons.load("marker_add", os.path.join(icons_dir, "marker_add.png"), 'IMAGE')
    mkb_icons.load("marker_move", os.path.join(icons_dir, "marker_move.png"), 'IMAGE')
    mkb_icons.load("marker_jump_left", os.path.join(icons_dir, "marker_jump_left.png"), 'IMAGE')
    mkb_icons.load("marker_jump_right", os.path.join(icons_dir, "marker_jump_right.png"), 'IMAGE')
    mkb_icons.load("marker_lock", os.path.join(icons_dir, "marker_lock.png"), 'IMAGE')
    mkb_icons.load("marker_rename", os.path.join(icons_dir, "marker_rename.png"), 'IMAGE')


    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False