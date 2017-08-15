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
  
    mkb_icons.load("icon_space_align_to_normal", os.path.join(icons_dir, "space_align_to_normal.png"), 'IMAGE')    

    mkb_icons.load("icon_space_circle", os.path.join(icons_dir, "space_circle.png"), 'IMAGE')    
    mkb_icons.load("icon_space_curve", os.path.join(icons_dir, "space_curve.png"), 'IMAGE')    
    mkb_icons.load("icon_space_distribute", os.path.join(icons_dir, "space_distribute.png"), 'IMAGE')    
    mkb_icons.load("icon_space_flatten", os.path.join(icons_dir, "space_flatten.png"), 'IMAGE')       
    mkb_icons.load("icon_space_space", os.path.join(icons_dir, "space_space.png"), 'IMAGE')    
    mkb_icons.load("icon_space_straigten", os.path.join(icons_dir, "space_straigten.png"), 'IMAGE')    

    mkb_icons.load("icon_space_x", os.path.join(icons_dir, "space_x.png"), 'IMAGE')    
    mkb_icons.load("icon_space_y", os.path.join(icons_dir, "space_y.png"), 'IMAGE')    
    mkb_icons.load("icon_space_z", os.path.join(icons_dir, "space_z.png"), 'IMAGE')    
    mkb_icons.load("icon_space_xy", os.path.join(icons_dir, "space_xy.png"), 'IMAGE')    
    mkb_icons.load("icon_space_zx", os.path.join(icons_dir, "space_zx.png"), 'IMAGE')    
    mkb_icons.load("icon_space_zy", os.path.join(icons_dir, "space_zy.png"), 'IMAGE')    


    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False