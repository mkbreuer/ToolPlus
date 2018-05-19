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

    mkb_icons.load("icon_fun", os.path.join(icons_dir, "fun.png"), 'IMAGE')  
    mkb_icons.load("icon_image1", os.path.join(icons_dir, "icon_image1.png"), 'IMAGE')    

  
    # ICONS CUSTOM #     
    mkb_icons.load("icon_custom_1", os.path.join(icons_dir, "my_custom_1.png"), 'IMAGE')    
    #mkb_icons.load("icon_custom_2", os.path.join(icons_dir, "my_custom_2.png"), 'IMAGE')    
    #mkb_icons.load("icon_custom_3", os.path.join(icons_dir, "my_custom_3.png"), 'IMAGE')    
    #mkb_icons.load("icon_custom_4", os.path.join(icons_dir, "my_custom_4.png"), 'IMAGE')    


    # ICONS UI #   
    mkb_icons.load("icon_apply_move", os.path.join(icons_dir, "apply_move.png"), 'IMAGE')  
    mkb_icons.load("icon_apply_rota", os.path.join(icons_dir, "apply_rota.png"), 'IMAGE')  
    mkb_icons.load("icon_apply_scale", os.path.join(icons_dir, "apply_scale.png"), 'IMAGE')  
    mkb_icons.load("icon_baply", os.path.join(icons_dir, "baply.png"), 'IMAGE')  

    mkb_icons.load("icon_curve_extrude", os.path.join(icons_dir, "curve_extrude.png"), 'IMAGE')  
    mkb_icons.load("icon_curve_open", os.path.join(icons_dir, "curve_open.png"), 'IMAGE')  
    mkb_icons.load("icon_curve_close", os.path.join(icons_dir, "curve_close.png"), 'IMAGE')  
    mkb_icons.load("icon_curve_smooth", os.path.join(icons_dir, "curve_smooth.png"), 'IMAGE')  
    mkb_icons.load("icon_curve_start", os.path.join(icons_dir, "curve_start.png"), 'IMAGE')  
    mkb_icons.load("icon_curve_simplify", os.path.join(icons_dir, "curve_simplify.png"), 'IMAGE')

    mkb_icons.load("icon_draw_bevel", os.path.join(icons_dir, "draw_bevel.png"), 'IMAGE')  
    mkb_icons.load("icon_draw_brush", os.path.join(icons_dir, "draw_brush.png"), 'IMAGE')  
    mkb_icons.load("icon_draw_curve", os.path.join(icons_dir, "draw_curve.png"), 'IMAGE')  
    mkb_icons.load("icon_draw_lathe", os.path.join(icons_dir, "draw_lathe.png"), 'IMAGE')  
    mkb_icons.load("icon_draw_pencil", os.path.join(icons_dir, "draw_pencil.png"), 'IMAGE')  
    mkb_icons.load("icon_draw_surface", os.path.join(icons_dir, "draw_surface.png"), 'IMAGE')  

    mkb_icons.load("icon_ruler", os.path.join(icons_dir, "ruler.png"), 'IMAGE')

    mkb_icons.load("icon_snap_active", os.path.join(icons_dir, "snap_active.png"), 'IMAGE')
    mkb_icons.load("icon_snap_cursor", os.path.join(icons_dir, "snap_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid", os.path.join(icons_dir, "snap_grid.png"), 'IMAGE')
    mkb_icons.load("icon_snap_place", os.path.join(icons_dir, "snap_place.png"), 'IMAGE')
    mkb_icons.load("icon_snap_retopo", os.path.join(icons_dir, "snap_retopo.png"), 'IMAGE')

   
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False