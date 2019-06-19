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
    
    mkb_icons.load("icon_object_to_origin", os.path.join(icons_dir, "icon_object_to_origin.png"), 'IMAGE')
    
    mkb_icons.load("icon_origin_align_mesh", os.path.join(icons_dir, "icon_origin_align_mesh.png"), 'IMAGE')
    mkb_icons.load("icon_origin_align_object", os.path.join(icons_dir, "icon_origin_align_object.png"), 'IMAGE')
    
    mkb_icons.load("icon_origin_to_bbox_m", os.path.join(icons_dir, "icon_origin_to_bbox_m.png"), 'IMAGE')      
    mkb_icons.load("icon_origin_to_cc", os.path.join(icons_dir, "icon_origin_to_cc.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_center_view", os.path.join(icons_dir, "icon_origin_to_center_view.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_cursor", os.path.join(icons_dir, "icon_origin_to_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_object", os.path.join(icons_dir, "icon_origin_to_object.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_selected", os.path.join(icons_dir, "icon_origin_to_selected.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_click_point", os.path.join(icons_dir, "icon_origin_to_click_point.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_snap_point", os.path.join(icons_dir, "icon_origin_to_snap_point.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_surface", os.path.join(icons_dir, "icon_origin_to_surface.png"), 'IMAGE')   
    mkb_icons.load("icon_origin_to_volume", os.path.join(icons_dir, "icon_origin_to_volume.png"), 'IMAGE')
    
    mkb_icons.load("icon_distribute_origins", os.path.join(icons_dir, "icon_distribute_origins.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_bbox_multi", os.path.join(icons_dir, "icon_origin_to_bbox_multi.png"), 'IMAGE')
    mkb_icons.load("icon_origin_to_bbox_modal", os.path.join(icons_dir, "icon_origin_to_bbox_modal.png"), 'IMAGE')
    
    mkb_icons.load("icon_origin_bottom", os.path.join(icons_dir, "origin_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_center", os.path.join(icons_dir, "origin_center.png"), 'IMAGE')
    mkb_icons.load("icon_origin_cross", os.path.join(icons_dir, "origin_cross.png"), 'IMAGE') 
    mkb_icons.load("icon_origin_cursor", os.path.join(icons_dir, "origin_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_origin_diagonal", os.path.join(icons_dir, "origin_diagonal.png"), 'IMAGE')
    mkb_icons.load("icon_origin_left", os.path.join(icons_dir, "origin_left.png"), 'IMAGE')
    mkb_icons.load("icon_origin_left_bottom", os.path.join(icons_dir, "origin_left_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_left_top", os.path.join(icons_dir, "origin_left_top.png"), 'IMAGE')
    mkb_icons.load("icon_origin_right", os.path.join(icons_dir, "origin_right.png"), 'IMAGE')
    mkb_icons.load("icon_origin_right_bottom", os.path.join(icons_dir, "origin_right_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_right_top", os.path.join(icons_dir, "origin_right_top.png"), 'IMAGE')
    mkb_icons.load("icon_origin_top", os.path.join(icons_dir, "origin_top.png"), 'IMAGE')

    mkb_icons.load("icon_origin_snap_origin", os.path.join(icons_dir, "icon_origin_snap_origin.png"), 'IMAGE')
    mkb_icons.load("icon_align_to_zero", os.path.join(icons_dir, "icon_align_to_zero.png"), 'IMAGE')

    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = Falseicon_origin_to_volume