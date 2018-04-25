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

    mkb_icons.load("icon_mirror_x", os.path.join(icons_dir, "mirror_x.png"), 'IMAGE')
    mkb_icons.load("icon_mirror_y", os.path.join(icons_dir, "mirror_y.png"), 'IMAGE')
    mkb_icons.load("icon_mirror_z", os.path.join(icons_dir, "mirror_z.png"), 'IMAGE')

    mkb_icons.load("icon_ruler", os.path.join(icons_dir, "ruler.png"), 'IMAGE')

    mkb_icons.load("icon_apply", os.path.join(icons_dir, "apply.png"), 'IMAGE') 
    mkb_icons.load("icon_apply_move", os.path.join(icons_dir, "apply_move.png"), 'IMAGE')    
    mkb_icons.load("icon_apply_rota", os.path.join(icons_dir, "apply_rota.png"), 'IMAGE')  
    mkb_icons.load("icon_apply_scale", os.path.join(icons_dir, "apply_scale.png"), 'IMAGE')    

    mkb_icons.load("icon_mods_append", os.path.join(icons_dir, "mods_append.png"), 'IMAGE')    
    mkb_icons.load("icon_mods_copy", os.path.join(icons_dir, "mods_copy.png"), 'IMAGE')    
   
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False