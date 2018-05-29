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

    # ICONS VISUALS # 
    mkb_icons.load("icon_flip", os.path.join(icons_dir, "flip.png"), 'IMAGE')
    mkb_icons.load("icon_matcap", os.path.join(icons_dir, "matcap.png"), 'IMAGE')
    mkb_icons.load("icon_remove_doubles", os.path.join(icons_dir, "remove_doubles.png"), 'IMAGE')
    mkb_icons.load("icon_ruler", os.path.join(icons_dir, "ruler.png"), 'IMAGE')
    mkb_icons.load("icon_switch", os.path.join(icons_dir, "switch.png"), 'IMAGE')


    # ICONS BOUNDINGS # 
    mkb_icons.load("icon_linked", os.path.join(icons_dir, "linked.png"), 'IMAGE')

    mkb_icons.load("icon_baply", os.path.join(icons_dir, "baply.png"), 'IMAGE')    
    mkb_icons.load("icon_bbox", os.path.join(icons_dir, "bbox.png"), 'IMAGE')    
    mkb_icons.load("icon_bcyl", os.path.join(icons_dir, "bcyl.png"), 'IMAGE')    
    mkb_icons.load("icon_bloc", os.path.join(icons_dir, "bloc.png"), 'IMAGE')    
    mkb_icons.load("icon_bsel", os.path.join(icons_dir, "bsel.png"), 'IMAGE')    
    mkb_icons.load("icon_bsph", os.path.join(icons_dir, "bsph.png"), 'IMAGE')    


    # ICONS TRANSFORM # 
    mkb_icons.load("icon_apply_move", os.path.join(icons_dir, "apply_move.png"), 'IMAGE')    
    mkb_icons.load("icon_apply_rota", os.path.join(icons_dir, "apply_rota.png"), 'IMAGE')  
    mkb_icons.load("icon_apply_scale", os.path.join(icons_dir, "apply_scale.png"), 'IMAGE')    


    # ICONS RECOPLANAR # 
    mkb_icons.load("icon_relocal", os.path.join(icons_dir, "relocal.png"), 'IMAGE')    
    mkb_icons.load("icon_recenter", os.path.join(icons_dir, "recenter.png"), 'IMAGE')    
    mkb_icons.load("icon_reposition", os.path.join(icons_dir, "reposition.png"), 'IMAGE')   
    mkb_icons.load("icon_center", os.path.join(icons_dir, "axis_centered.png"), 'IMAGE')   
    mkb_icons.load("icon_deltas", os.path.join(icons_dir, "axis_deltas.png"), 'IMAGE')    
    
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False
