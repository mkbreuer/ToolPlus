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

    # ICONS UI #   
    mkb_icons.load("icon_wire_on", os.path.join(icons_dir, "wire_on.png"), 'IMAGE')     
    mkb_icons.load("icon_wire_off", os.path.join(icons_dir, "wire_off.png"), 'IMAGE')        
    mkb_icons.load("icon_draw_pencil", os.path.join(icons_dir, "draw_pencil.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_knife", os.path.join(icons_dir, "draw_knife.png"), 'IMAGE')         
    mkb_icons.load("icon_draw_besurface", os.path.join(icons_dir, "draw_besurface.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_meshbrush", os.path.join(icons_dir, "draw_meshbrush.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_poly", os.path.join(icons_dir, "draw_poly.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_mt", os.path.join(icons_dir, "draw_mt.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_face", os.path.join(icons_dir, "draw_face.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_square", os.path.join(icons_dir, "draw_square.png"), 'IMAGE')     
    mkb_icons.load("icon_draw_fast", os.path.join(icons_dir, "draw_fast.png"), 'IMAGE')     
    mkb_icons.load("icon_edit_divide", os.path.join(icons_dir, "edit_divide.png"), 'IMAGE')     

    mkb_icons.load("icon_draw_carver", os.path.join(icons_dir, "draw_carver.png"), 'IMAGE') 
    mkb_icons.load("icon_draw_curve", os.path.join(icons_dir, "draw_curve.png"), 'IMAGE') 
    mkb_icons.load("icon_draw_surface", os.path.join(icons_dir, "draw_surface.png"), 'IMAGE') 
    mkb_icons.load("icon_draw_lathe", os.path.join(icons_dir, "draw_lathe.png"), 'IMAGE') 
    mkb_icons.load("icon_draw_bevel", os.path.join(icons_dir, "draw_bevel.png"), 'IMAGE') 

    # ICONS CURVE # 
    mkb_icons.load("icon_curve_start", os.path.join(icons_dir, "curve_start.png"), 'IMAGE') 
    mkb_icons.load("icon_curve_open", os.path.join(icons_dir, "curve_open.png"), 'IMAGE') 
    mkb_icons.load("icon_curve_extrude", os.path.join(icons_dir, "curve_extrude.png"), 'IMAGE') 
    mkb_icons.load("icon_curve_smooth", os.path.join(icons_dir, "curve_smooth.png"), 'IMAGE') 

 
    # ICONS CHECK # 
    mkb_icons.load("icon_check_ngon", os.path.join(icons_dir, "check_ngon.png"), 'IMAGE')
    mkb_icons.load("icon_check_quads", os.path.join(icons_dir, "check_quads.png"), 'IMAGE')
    mkb_icons.load("icon_check_triangle", os.path.join(icons_dir, "check_triangle.png"), 'IMAGE')


    # ICONS VISUALS # 
    mkb_icons.load("icon_flip", os.path.join(icons_dir, "flip.png"), 'IMAGE')
    mkb_icons.load("icon_matcap", os.path.join(icons_dir, "matcap.png"), 'IMAGE')
    

    mkb_icons.load("icon_remove_doubles", os.path.join(icons_dir, "remove_doubles.png"), 'IMAGE')
    mkb_icons.load("icon_ruler", os.path.join(icons_dir, "ruler.png"), 'IMAGE')
    mkb_icons.load("icon_switch", os.path.join(icons_dir, "switch.png"), 'IMAGE')


    mkb_icons.load("icon_linked", os.path.join(icons_dir, "linked.png"), 'IMAGE')

    mkb_icons.load("icon_center", os.path.join(icons_dir, "axis_centered.png"), 'IMAGE')   
    mkb_icons.load("icon_deltas", os.path.join(icons_dir, "axis_deltas.png"), 'IMAGE')   

    mkb_icons.load("icon_baply", os.path.join(icons_dir, "baply.png"), 'IMAGE')    
    mkb_icons.load("icon_bbox", os.path.join(icons_dir, "bbox.png"), 'IMAGE')    
    mkb_icons.load("icon_bcyl", os.path.join(icons_dir, "bcyl.png"), 'IMAGE')    
    mkb_icons.load("icon_bloc", os.path.join(icons_dir, "bloc.png"), 'IMAGE')    
    mkb_icons.load("icon_bsel", os.path.join(icons_dir, "bsel.png"), 'IMAGE')    
    mkb_icons.load("icon_bsph", os.path.join(icons_dir, "bsph.png"), 'IMAGE')    

    mkb_icons.load("icon_apply_move", os.path.join(icons_dir, "apply_move.png"), 'IMAGE')    
    mkb_icons.load("icon_apply_rota", os.path.join(icons_dir, "apply_rota.png"), 'IMAGE')  
    mkb_icons.load("icon_apply_scale", os.path.join(icons_dir, "apply_scale.png"), 'IMAGE')    

    mkb_icons.load("icon_relocal", os.path.join(icons_dir, "relocal.png"), 'IMAGE')    
    mkb_icons.load("icon_recenter", os.path.join(icons_dir, "recenter.png"), 'IMAGE')    
    mkb_icons.load("icon_reposition", os.path.join(icons_dir, "reposition.png"), 'IMAGE')  

    mkb_icons.load("icon_mirror_x", os.path.join(icons_dir, "mirror_x.png"), 'IMAGE')
    mkb_icons.load("icon_mirror_y", os.path.join(icons_dir, "mirror_y.png"), 'IMAGE')
    mkb_icons.load("icon_mirror_z", os.path.join(icons_dir, "mirror_z.png"), 'IMAGE')

    mkb_icons.load("icon_align_advance", os.path.join(icons_dir, "align_advance.png"), 'IMAGE')    
    mkb_icons.load("icon_align_con_face", os.path.join(icons_dir, "align_con_face.png"), 'IMAGE')    
    mkb_icons.load("icon_align_laplacian", os.path.join(icons_dir, "align_laplacian.png"), 'IMAGE')    
    mkb_icons.load("icon_align_looptools", os.path.join(icons_dir, "align_looptools.png"), 'IMAGE')
    mkb_icons.load("icon_align_planar", os.path.join(icons_dir, "align_planar.png"), 'IMAGE')
    mkb_icons.load("icon_align_radians", os.path.join(icons_dir, "align_radians.png"), 'IMAGE')
    mkb_icons.load("icon_align_rectangular", os.path.join(icons_dir, "align_rectangular.png"), 'IMAGE')
    mkb_icons.load("icon_align_shrinkwrap", os.path.join(icons_dir, "align_shrinkwrap.png"), 'IMAGE')
    mkb_icons.load("icon_align_vertices", os.path.join(icons_dir, "align_vertices.png"), 'IMAGE')

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

    mkb_icons.load("icon_copy_tocursor", os.path.join(icons_dir, "copy_tocursor.png"), 'IMAGE')

    mkb_icons.load("icon_flip_lattice", os.path.join(icons_dir, "flip_lattice.png"), 'IMAGE')
    mkb_icons.load("icon_lattice_create", os.path.join(icons_dir, "lattice_create.png"), 'IMAGE')
    mkb_icons.load("icon_lattice_apply", os.path.join(icons_dir, "lattice_apply.png"), 'IMAGE')


    mkb_icons.load("icon_origin_active", os.path.join(icons_dir, "origin_active.png"), 'IMAGE')
    mkb_icons.load("icon_origin_align", os.path.join(icons_dir, "origin_align.png"), 'IMAGE')
    mkb_icons.load("icon_origin_bbox", os.path.join(icons_dir, "origin_bbox.png"), 'IMAGE')
    mkb_icons.load("icon_origin_bottom", os.path.join(icons_dir, "origin_bottom.png"), 'IMAGE')
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
    mkb_icons.load("icon_origin_ccc", os.path.join(icons_dir, "origin_ccc.png"), 'IMAGE')
    mkb_icons.load("icon_origin_top", os.path.join(icons_dir, "origin_top.png"), 'IMAGE')
    mkb_icons.load("icon_ruler_triangle", os.path.join(icons_dir, "ruler_triangle.png"), 'IMAGE')
    mkb_icons.load("icon_origin_copy", os.path.join(icons_dir, "origin_copy.png"), 'IMAGE')

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
 
 
    mkb_icons.load("icon_axis_x", os.path.join(icons_dir, "axis_x.png"), 'IMAGE')    
    mkb_icons.load("icon_axis_xyz_planes", os.path.join(icons_dir, "axis_xyz_planes.png"), 'IMAGE')
    mkb_icons.load("icon_axis_y", os.path.join(icons_dir, "axis_y.png"), 'IMAGE')
    mkb_icons.load("icon_axis_z", os.path.join(icons_dir, "axis_z.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_carver", os.path.join(icons_dir, "boolean_carver.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_union", os.path.join(icons_dir, "boolean_union.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_intersect", os.path.join(icons_dir, "boolean_intersect.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_difference", os.path.join(icons_dir, "boolean_difference.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_rebool", os.path.join(icons_dir, "boolean_rebool.png"), 'IMAGE')
    
    mkb_icons.load("icon_boolean_union_brush", os.path.join(icons_dir, "boolean_union_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_intersect_brush", os.path.join(icons_dir, "boolean_intersect_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_difference_brush", os.path.join(icons_dir, "boolean_difference_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_rebool_brush", os.path.join(icons_dir, "boolean_rebool_brush.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_draw", os.path.join(icons_dir, "boolean_draw.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_bevel", os.path.join(icons_dir, "boolean_bevel.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_edge", os.path.join(icons_dir, "boolean_edge.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_bridge", os.path.join(icons_dir, "boolean_bridge.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_sym", os.path.join(icons_dir, "boolean_sym.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_pipe", os.path.join(icons_dir, "boolean_pipe.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_custom", os.path.join(icons_dir, "boolean_custom.png"), 'IMAGE')
    
    mkb_icons.load("icon_boolean_separate", os.path.join(icons_dir, "boolean_separate.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_substract", os.path.join(icons_dir, "boolean_substract.png"), 'IMAGE')

    mkb_icons.load("icon_boolean_weld", os.path.join(icons_dir, "boolean_weld.png"), 'IMAGE')
    mkb_icons.load("icon_boolean_isolate", os.path.join(icons_dir, "boolean_isolate.png"), 'IMAGE')   

    mkb_icons.load("icon_boolean_exclude", os.path.join(icons_dir, "boolean_exclude.png"), 'IMAGE') 
    mkb_icons.load("icon_boolean_facemerge", os.path.join(icons_dir, "boolean_facemerge.png"), 'IMAGE')

    mkb_icons.load("icon_skin_human", os.path.join(icons_dir, "skin_human.png"), 'IMAGE')
    mkb_icons.load("icon_skin_animal", os.path.join(icons_dir, "skin_animal.png"), 'IMAGE')
    mkb_icons.load("icon_skin_empty", os.path.join(icons_dir, "skin_empty.png"), 'IMAGE')




   
    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
	global toolplus_icons_loaded
	for icon in toolplus_icon_collections.values():
		bpy.utils.previews.remove(icon)
	toolplus_icon_collections.clear()
	toolplus_icons_loaded = False