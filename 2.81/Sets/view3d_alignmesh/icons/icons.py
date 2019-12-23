import os
import bpy
import bpy.utils.previews

mkb_icon_collections = {}
mkb_icons_loaded = False

def load_icons():
    global mkb_icon_collections
    global mkb_icons_loaded

    if mkb_icons_loaded: return mkb_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))
    
    mkb_icons.load("icon_align_x", os.path.join(icons_dir, "align_x.png"), 'IMAGE')    
    mkb_icons.load("icon_align_y", os.path.join(icons_dir, "align_y.png"), 'IMAGE')    
    mkb_icons.load("icon_align_z", os.path.join(icons_dir, "align_z.png"), 'IMAGE')    
    mkb_icons.load("icon_align_xy", os.path.join(icons_dir, "align_xy.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zx", os.path.join(icons_dir, "align_zx.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zy", os.path.join(icons_dir, "align_zy.png"), 'IMAGE')   

    mkb_icons.load("icon_align_n", os.path.join(icons_dir, "align_n.png"), 'IMAGE')   

    mkb_icons.load("icon_align_distribute", os.path.join(icons_dir, "align_distribute.png"), 'IMAGE')   
    mkb_icons.load("icon_align_straigten", os.path.join(icons_dir, "align_straigten.png"), 'IMAGE')   
    mkb_icons.load("icon_align_both", os.path.join(icons_dir, "align_both.png"), 'IMAGE')   

    mkb_icons.load("icon_align_laplacian", os.path.join(icons_dir, "align_laplacian.png"), 'IMAGE')   
    mkb_icons.load("icon_align_looptools", os.path.join(icons_dir, "align_looptools.png"), 'IMAGE')   
    mkb_icons.load("icon_align_vertices", os.path.join(icons_dir, "align_vertices.png"), 'IMAGE')   

    mkb_icons.load("icon_align_space", os.path.join(icons_dir, "align_space.png"), 'IMAGE')   
    mkb_icons.load("icon_align_circle", os.path.join(icons_dir, "align_circle.png"), 'IMAGE')   
    mkb_icons.load("icon_align_curve", os.path.join(icons_dir, "align_curve.png"), 'IMAGE')   
    mkb_icons.load("icon_align_flatten", os.path.join(icons_dir, "align_flatten.png"), 'IMAGE')   
    mkb_icons.load("icon_align_smooth", os.path.join(icons_dir, "align_smooth.png"), 'IMAGE')   

    
    mkb_icon_collections["main"] = mkb_icons
    mkb_icons_loaded = True

    return mkb_icon_collections["main"]

def clear_icons():
	global mkb_icons_loaded
	for icon in mkb_icon_collections.values():
		bpy.utils.previews.remove(icon)
	mkb_icon_collections.clear()
	mkb_icons_loaded = False
