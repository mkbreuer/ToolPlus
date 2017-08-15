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

    mkb_icons.load("icon_select_active_edm", os.path.join(icons_dir, "select_active_edm.png"), 'IMAGE')
    mkb_icons.load("icon_select_active_obm", os.path.join(icons_dir, "select_active_obm.png"), 'IMAGE')
    mkb_icons.load("icon_select_center", os.path.join(icons_dir, "select_center.png"), 'IMAGE')
    mkb_icons.load("icon_select_cursor", os.path.join(icons_dir, "select_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_select_cursor_offset_edm", os.path.join(icons_dir, "select_cursor_offset_edm.png"), 'IMAGE')
    mkb_icons.load("icon_select_cursor_offset_obm", os.path.join(icons_dir, "select_cursor_offset_obm.png"), 'IMAGE')
    mkb_icons.load("icon_select_grid", os.path.join(icons_dir, "select_grid.png"), 'IMAGE')
    mkb_icons.load("icon_select_mesh", os.path.join(icons_dir, "select_mesh.png"), 'IMAGE')
    mkb_icons.load("icon_select_object", os.path.join(icons_dir, "select_object.png"), 'IMAGE')
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