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
 
    mkb_icons.load("icon_align_x", os.path.join(icons_dir, "align_x.png"), 'IMAGE')    
    mkb_icons.load("icon_align_y", os.path.join(icons_dir, "align_y.png"), 'IMAGE')    
    mkb_icons.load("icon_align_z", os.path.join(icons_dir, "align_z.png"), 'IMAGE')    
    
    mkb_icons.load("icon_align_xy", os.path.join(icons_dir, "align_xy.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zx", os.path.join(icons_dir, "align_zx.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zy", os.path.join(icons_dir, "align_zy.png"), 'IMAGE')    

    mkb_icons.load("icon_align_to_normal", os.path.join(icons_dir, "align_to_normal.png"), 'IMAGE')   

    mkb_icons.load("icon_apply", os.path.join(icons_dir, "apply.png"), 'IMAGE')   
    mkb_icons.load("icon_apply_move", os.path.join(icons_dir, "apply_move.png"), 'IMAGE')   
    mkb_icons.load("icon_apply_rota", os.path.join(icons_dir, "apply_rota.png"), 'IMAGE')   
    mkb_icons.load("icon_apply_scale", os.path.join(icons_dir, "apply_scale.png"), 'IMAGE')   

    mkb_icons.load("icon_mirror_over_edge", os.path.join(icons_dir, "mirror_over_edge.png"), 'IMAGE')    


    mkb_icons.load("icon_snap_active", os.path.join(icons_dir, "snap_active.png"), 'IMAGE')
    mkb_icons.load("icon_snap_cursor", os.path.join(icons_dir, "snap_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grab", os.path.join(icons_dir, "snap_grab.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid", os.path.join(icons_dir, "snap_grid.png"), 'IMAGE')
    mkb_icons.load("icon_snap_place", os.path.join(icons_dir, "snap_place.png"), 'IMAGE')
    mkb_icons.load("icon_snap_retopo", os.path.join(icons_dir, "snap_retopo.png"), 'IMAGE')
    mkb_icons.load("icon_snap_rotate", os.path.join(icons_dir, "snap_rotate.png"), 'IMAGE')
    mkb_icons.load("icon_snap_scale", os.path.join(icons_dir, "snap_scale.png"), 'IMAGE')



    mkb_icons.load("icon_ruler", os.path.join(icons_dir, "ruler.png"), 'IMAGE')

    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False