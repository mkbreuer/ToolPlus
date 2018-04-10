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

    #--------------------------------------------------
  

    # ALIGN #
    mkb_icons.load("icon_apply", os.path.join(icons_dir, "apply.png"), 'IMAGE')    
    mkb_icons.load("icon_align_baply", os.path.join(icons_dir, "baply.png"), 'IMAGE')    

    mkb_icons.load("icon_align_advance", os.path.join(icons_dir, "align_advance.png"), 'IMAGE')    
    mkb_icons.load("icon_align_con_face", os.path.join(icons_dir, "align_con_face.png"), 'IMAGE')    
    mkb_icons.load("icon_align_laplacian", os.path.join(icons_dir, "align_laplacian.png"), 'IMAGE')    
    mkb_icons.load("icon_align_looptools", os.path.join(icons_dir, "align_looptools.png"), 'IMAGE')
    mkb_icons.load("icon_align_planar", os.path.join(icons_dir, "align_planar.png"), 'IMAGE')
    mkb_icons.load("icon_align_radians", os.path.join(icons_dir, "align_radians.png"), 'IMAGE')
    mkb_icons.load("icon_align_rectangular", os.path.join(icons_dir, "align_rectangular.png"), 'IMAGE')
    mkb_icons.load("icon_align_shrinkwrap", os.path.join(icons_dir, "align_shrinkwrap.png"), 'IMAGE')
    mkb_icons.load("icon_align_vertices", os.path.join(icons_dir, "align_vertices.png"), 'IMAGE')
    mkb_icons.load("icon_align_unbevel", os.path.join(icons_dir, "align_unbevel.png"), 'IMAGE')

    mkb_icons.load("icon_align_to_normal", os.path.join(icons_dir, "align_to_normal.png"), 'IMAGE')    

    mkb_icons.load("icon_align_mirror_edge", os.path.join(icons_dir, "align_mirror_edge.png"), 'IMAGE')    
    mkb_icons.load("icon_align_mirror_edm", os.path.join(icons_dir, "align_mirror_edm.png"), 'IMAGE')    
    mkb_icons.load("icon_align_mirror_obm", os.path.join(icons_dir, "align_mirror_obm.png"), 'IMAGE')    

    mkb_icons.load("icon_navi_orbit_down", os.path.join(icons_dir, "navi_orbit_down.png"), 'IMAGE') 
    mkb_icons.load("icon_navi_orbit_left", os.path.join(icons_dir, "navi_orbit_left.png"), 'IMAGE') 
    mkb_icons.load("icon_navi_orbit_right", os.path.join(icons_dir, "navi_orbit_right.png"), 'IMAGE') 
    mkb_icons.load("icon_navi_orbit_up", os.path.join(icons_dir, "navi_orbit_up.png"), 'IMAGE') 
    mkb_icons.load("icon_navi_roll_left", os.path.join(icons_dir, "navi_roll_left.png"), 'IMAGE') 
    mkb_icons.load("icon_navi_roll_right", os.path.join(icons_dir, "navi_roll_right.png"), 'IMAGE') 
       
    mkb_icons.load("icon_align_circle", os.path.join(icons_dir, "align_circle.png"), 'IMAGE')    
    mkb_icons.load("icon_align_curve", os.path.join(icons_dir, "align_curve.png"), 'IMAGE')    
    mkb_icons.load("icon_align_distribute", os.path.join(icons_dir, "align_distribute.png"), 'IMAGE')    
    mkb_icons.load("icon_align_flatten", os.path.join(icons_dir, "align_flatten.png"), 'IMAGE')       
    mkb_icons.load("icon_align_space", os.path.join(icons_dir, "align_space.png"), 'IMAGE')    
    mkb_icons.load("icon_align_straigten", os.path.join(icons_dir, "align_straigten.png"), 'IMAGE')    

    mkb_icons.load("icon_align_x", os.path.join(icons_dir, "align_x.png"), 'IMAGE')    
    mkb_icons.load("icon_align_y", os.path.join(icons_dir, "align_y.png"), 'IMAGE')    
    mkb_icons.load("icon_align_z", os.path.join(icons_dir, "align_z.png"), 'IMAGE')    
    mkb_icons.load("icon_align_xy", os.path.join(icons_dir, "align_xy.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zx", os.path.join(icons_dir, "align_zx.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zy", os.path.join(icons_dir, "align_zy.png"), 'IMAGE')    

    mkb_icons.load("icon_align_zero", os.path.join(icons_dir, "align_zero.png"), 'IMAGE')    
    
    mkb_icons.load("icon_flip_lattice", os.path.join(icons_dir, "flip_lattice.png"), 'IMAGE')
    
    mkb_icons.load("icon_look_at_cursor", os.path.join(icons_dir, "look_at_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_look_at_obj", os.path.join(icons_dir, "look_at_obj.png"), 'IMAGE')

    mkb_icons.load("icon_lattice_add", os.path.join(icons_dir, "lattice_add.png"), 'IMAGE')
    mkb_icons.load("icon_lattice_apply", os.path.join(icons_dir, "lattice_apply.png"), 'IMAGE')


    # CURSOR #
    mkb_icons.load("icon_cursor", os.path.join(icons_dir, "cursor.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_3point_center", os.path.join(icons_dir, "cursor_3point_center.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_active_edm", os.path.join(icons_dir, "cursor_active_edm.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_active_obm", os.path.join(icons_dir, "cursor_active_obm.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_center", os.path.join(icons_dir, "cursor_center.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_center_offset_edm", os.path.join(icons_dir, "cursor_center_offset_edm.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_center_offset_obm", os.path.join(icons_dir, "cursor_center_offset_obm.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_grid", os.path.join(icons_dir, "cursor_grid.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_mesh", os.path.join(icons_dir, "cursor_mesh.png"), 'IMAGE')
    mkb_icons.load("icon_cursor_object", os.path.join(icons_dir, "cursor_object.png"), 'IMAGE')



    # ORIGIN #
    mkb_icons.load("icon_origin_active", os.path.join(icons_dir, "origin_active.png"), 'IMAGE')
    mkb_icons.load("icon_origin_align", os.path.join(icons_dir, "origin_align.png"), 'IMAGE')
    mkb_icons.load("icon_origin_apply", os.path.join(icons_dir, "origin_apply.png"), 'IMAGE')
    mkb_icons.load("icon_origin_bbox", os.path.join(icons_dir, "origin_bbox.png"), 'IMAGE')
    mkb_icons.load("icon_origin_bottom", os.path.join(icons_dir, "origin_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_origin_ccc", os.path.join(icons_dir, "origin_ccc.png"), 'IMAGE')
    mkb_icons.load("icon_origin_center", os.path.join(icons_dir, "origin_center.png"), 'IMAGE')
    mkb_icons.load("icon_origin_center_view", os.path.join(icons_dir, "origin_center_view.png"), 'IMAGE')
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


    # RULER #
    mkb_icons.load("icon_ruler_triangle", os.path.join(icons_dir, "ruler_triangle.png"), 'IMAGE')
   

    # SELECT #
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


    # SNAP #
    mkb_icons.load("icon_snap_abc", os.path.join(icons_dir, "snap_abc.png"), 'IMAGE')
    mkb_icons.load("icon_snap_active", os.path.join(icons_dir, "snap_active.png"), 'IMAGE')
    mkb_icons.load("icon_snap_cursor", os.path.join(icons_dir, "snap_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_snap_drop_down", os.path.join(icons_dir, "snap_drop_down.png"), 'IMAGE')
    mkb_icons.load("icon_snap_face_to_face", os.path.join(icons_dir, "snap_face_to_face.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid", os.path.join(icons_dir, "snap_grid.png"), 'IMAGE')
    mkb_icons.load("icon_snap_move", os.path.join(icons_dir, "snap_move.png"), 'IMAGE')
    mkb_icons.load("icon_snap_retopo", os.path.join(icons_dir, "snap_retopo.png"), 'IMAGE')
    mkb_icons.load("icon_snap_offset", os.path.join(icons_dir, "snap_offset.png"), 'IMAGE')
    mkb_icons.load("icon_snap_place", os.path.join(icons_dir, "snap_place.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grab", os.path.join(icons_dir, "snap_grab.png"), 'IMAGE')
    mkb_icons.load("icon_snap_rotate", os.path.join(icons_dir, "snap_rotate.png"), 'IMAGE')
    mkb_icons.load("icon_snap_scale", os.path.join(icons_dir, "snap_scale.png"), 'IMAGE')
    mkb_icons.load("icon_snap_ruler", os.path.join(icons_dir, "snap_ruler.png"), 'IMAGE')
    mkb_icons.load("icon_snap_set", os.path.join(icons_dir, "snap_set.png"), 'IMAGE')
    


    #--------------------------------------------

    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False