# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons

import addon_utils


def draw_edit_layout(self, context, layout):
    tp_props = context.window_manager.tp_collapse_align   

    addon_key = __package__.split(".")[0]    
    panel_prefs = context.user_preferences.addons[addon_key].preferences
    expand = panel_prefs.expand_panel_tools

    icons = load_icons()

    layout.operator_context = 'INVOKE_REGION_WIN'

    col = layout.column(align=True)         

    box = col.box().column(1)  
    
    row = box.row(1)         
    row.label("Origin to..")  

    row = box.row(1) 

    if tp_props.display_origin_bbox:                     
        
        button_origin_bbox = icons.get("icon_origin_bbox")            
        row.prop(tp_props, "display_origin_bbox", text=" ", icon_value=button_origin_bbox.icon_id)                     
    else:               
        button_origin_bbox = icons.get("icon_origin_bbox")                
        row.prop(tp_props, "display_origin_bbox", text=" ", icon_value=button_origin_bbox.icon_id)


    button_origin_center_view = icons.get("icon_origin_center_view")
    row.operator("tp_ops.origin_set_center", text=" ", icon_value=button_origin_center_view.icon_id)

    button_origin_cursor = icons.get("icon_origin_cursor")
    row.operator("tp_ops.origin_cursor_edm", text=" ", icon_value=button_origin_cursor.icon_id)            

    button_origin_edm = icons.get("icon_origin_edm")            
    row.operator("tp_ops.origin_edm"," ", icon_value=button_origin_edm.icon_id)       

    button_origin_obj = icons.get("icon_origin_obj")   
    row.operator("tp_ops.origin_obm"," ", icon_value=button_origin_obj.icon_id)             


    box.separator()                                                     

    row = box.row(1)

    obj = context.active_object
    if obj:
        obj_type = obj.type
        
        if obj.type in {'MESH'}:

            if tp_props.display_origin_bbox: 
             
                box = col.box().column(1)     
                box.scale_x = 0.1
                
                row = box.row(1)                                     
                row.alignment ='CENTER'         
                row.label(" +Y Axis")
                row.separator() 
                row.label("   xY Axis")
                row.separator()   
                row.label("--Y Axis")

                #####                  
                row = box.row(1)                                     
                row.alignment ='CENTER'
                 
                button_origin_left_top = icons.get("icon_origin_left_top")   
                row.operator('tp_ops.cubeback_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
               
                button_origin_top = icons.get("icon_origin_top")  
                row.operator('tp_ops.cubeback_edgetop_minus_y', text="", icon_value=button_origin_top.icon_id)
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                row.operator('tp_ops.cubeback_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)

                row.separator()
                
                button_origin_left_top = icons.get("icon_origin_left_top")   
                row.operator('tp_ops.cubefront_edgetop_minus_x', text="", icon_value=button_origin_left_top.icon_id)
                
                button_origin_top = icons.get("icon_origin_top")  
                row.operator('tp_ops.cubefront_side_plus_z', text="", icon_value=button_origin_top.icon_id)
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                row.operator('tp_ops.cubefront_edgetop_plus_x', text="", icon_value=button_origin_right_top.icon_id)

                row.separator()
                
                button_origin_left_top = icons.get("icon_origin_left_top")   
                row.operator('tp_ops.cubefront_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
                
                button_origin_top = icons.get("icon_origin_top")  
                row.operator('tp_ops.cubeback_edgetop_plus_y', text="", icon_value=button_origin_top.icon_id)
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                row.operator('tp_ops.cubefront_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)
                
                #####

                row = box.row(1)                          
                row.alignment ='CENTER' 
                
                button_origin_left = icons.get("icon_origin_left")
                row.operator('tp_ops.cubefront_edgemiddle_minus_x', text="", icon_value=button_origin_left.icon_id)
               
                button_origin_cross = icons.get("icon_origin_cross")
                row.operator('tp_ops.cubefront_side_plus_y', text="", icon_value=button_origin_cross.icon_id)
                
                button_origin_right = icons.get("icon_origin_right")
                row.operator('tp_ops.cubefront_edgemiddle_plus_x', text="", icon_value=button_origin_right.icon_id)

                row.separator()

                button_origin_left = icons.get("icon_origin_left")
                row.operator('tp_ops.cubefront_side_minus_x', text="", icon_value=button_origin_left.icon_id)
               
                if context.mode == 'OBJECT':
                    button_origin_diagonal = icons.get("icon_origin_diagonal")
                    row.operator('object.origin_set', text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'
                else:
                    button_origin_diagonal = icons.get("icon_origin_diagonal")
                    row.operator('tp_ops.origin_set_editcenter', text="", icon_value=button_origin_diagonal.icon_id)
                
                button_origin_right = icons.get("icon_origin_right")
                row.operator('tp_ops.cubefront_side_plus_x', text="", icon_value=button_origin_right.icon_id)

                row.separator()
                
                button_origin_left = icons.get("icon_origin_left")
                row.operator('tp_ops.cubefront_edgemiddle_minus_y', text="", icon_value=button_origin_left.icon_id)
                
                button_origin_cross = icons.get("icon_origin_cross")
                row.operator('tp_ops.cubefront_side_minus_y', text="", icon_value=button_origin_cross.icon_id)
                
                button_origin_right = icons.get("icon_origin_right")
                row.operator('tp_ops.cubefront_edgemiddle_plus_y', text="", icon_value=button_origin_right.icon_id)

                #####

                row = box.row(1)
                row.alignment ='CENTER' 
                
                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                row.operator('tp_ops.cubeback_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                row.operator('tp_ops.cubefront_edgebottom_plus_y', text="", icon_value=button_origin_bottom.icon_id)
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                row.operator('tp_ops.cubeback_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                row.separator()
                
                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                row.operator('tp_ops.cubefront_edgebottom_minus_x', text="", icon_value=button_origin_left_bottom.icon_id)
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                row.operator('tp_ops.cubefront_side_minus_z', text="", icon_value=button_origin_bottom.icon_id)
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                row.operator('tp_ops.cubefront_edgebottom_plus_x', text="", icon_value=button_origin_right_bottom.icon_id)    

                row.separator()

                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                row.operator('tp_ops.cubefront_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                row.operator('tp_ops.cubefront_edgebottom_minus_y', text="", icon_value=button_origin_bottom.icon_id)
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                row.operator('tp_ops.cubefront_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                box.separator()

   

    box = col.box().row()   
    
    row = box.column(1) 
    row.label("Align") 
    row.label("to..") 
    row.label("Axis") 

    row = box.column(1)

    button_align_xy = icons.get("icon_align_xy") 
    row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'

    button_align_zx = icons.get("icon_align_zx")
    row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'

    button_align_zy = icons.get("icon_align_zy") 
    row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'           

    row = box.column(1)

    button_align_x = icons.get("icon_align_x") 
    row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'

    button_align_y = icons.get("icon_align_y") 
    row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

    button_align_z = icons.get("icon_align_z") 
    row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'

    row.separator() 
    

    box = col.box().column(1)
    
    row = box.row(1) 
    row.operator("mesh.align_operator", text = 'Store Edge').type_op = 1
    align_op = row.operator("mesh.align_operator", text = 'Align Edges').type_op = 0

    box.separator()      
 
    row = box.row(1) 
    if tp_props.display_align_help:
        row.prop(tp_props, "display_align_help", text="", icon='INFO')
    else:
        row.prop(tp_props, "display_align_help", text="", icon='INFO')

    row.prop(bpy.context.window_manager.paul_manager, 'align_dist_z', text = 'Superpose')
    row.prop(bpy.context.window_manager.paul_manager, 'align_lock_z', text = 'lock Z')

    if tp_props.display_align_help:

        box.separator() 
                      
        row = box.column(1)         
        row.label("This Tool need stored edge in the target:")         
        row.label("1. go into the editmode of the target") 
        row.label("2. select one edge as active") 
        row.label("3. and press Store Edge") 
       
        row.separator()            
        
        row.label("Now go into editmode of the object you want to align") 
        row.label("1. select all mesh that needs to be align") 
        row.label("2. select on edge as active") 
        row.label("3. and press Align Edges")
        
        row.separator()            
        
        row.label("Superpose: edge jump to edge")                  
        row.label("lock Z: preserve the z axis")                  

    box.separator()     



    box = col.box().column(1)              
    
    row = box.column(1) 

    button_align_planar = icons.get("icon_align_planar") 
    row.operator("mesh.face_make_planar", "Planar Faces", icon_value=button_align_planar.icon_id)   
    
    button_align_con_face = icons.get("icon_align_con_face") 
    row.operator("mesh.rot_con", "Square Rotation", icon_value=button_align_con_face.icon_id)   

    button_snap_offset = icons.get("icon_snap_offset")  
    row.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   

    button_lattice_add = icons.get("icon_lattice_add") 
    row.operator("tp_ops.easy_lattice", "Create Easy Lattice", icon_value=button_lattice_add.icon_id)   

    box.separator()


    box = col.box().column(1)              

    row = box.column(1) 
    row.label("Interpolate...")              
  
    row = box.column(1)    
    row.operator("mesh.wplsmthdef_apply", text="Apply Smooth Deform", icon ="FRAME_NEXT")

    box.separator()


    box = col.box().column(1)              
    
    row = box.column(1)                                                         

    button_align_straigten = icons.get("icon_align_straigten") 
    row.operator("mesh.vertex_align",text="Straighten", icon_value=button_align_straigten.icon_id) 

    button_align_distribute = icons.get("icon_align_distribute")  
    row.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_align_distribute.icon_id)                                        
   
    button_align_unbevel = icons.get("icon_align_unbevel") 
    row.operator("tp_ops.unbevel", text="Unbevel", icon_value=button_align_unbevel.icon_id)

    imdjs_tools_addon = "IMDJS_mesh_tools" 
    state = addon_utils.check(imdjs_tools_addon)
    if not state[0]:   
      
        button_align_radians = icons.get("icon_align_radians")  
        row.operator("mesh.round_selected_points", text="Radians", icon_value=button_align_radians.icon_id)  


    box.separator()
  
 
    Display_Looptools = context.user_preferences.addons[addon_key].preferences.tab_looptools
    if Display_Looptools == 'on':
            
        loop_tools_addon = "mesh_looptools" 
        state = addon_utils.check(loop_tools_addon)
        if not state[0]:                         
            
            row = box.column(1) 
            row.operator("tp_ops.enable_looptools", text="!_Activate Looptools_!", icon='BLANK1')    
            
            box.separator()

        else: 
 
  
            row = box.row(1)          
            row.operator("tp_ops.surface_pencil", text="",icon="GREASEPENCIL")    
            row.operator("mesh.looptools_gstretch", text="Gstretch", icon='IPO_EASE_IN_OUT')    
            row.operator("remove.gp", text="", icon="PANEL_CLOSE")    


            box.separator()                        
           
            lt = context.window_manager.looptools

            box = col.box().column(1)              
            
            row = box.row(1)  
            # space - first line
            split = row.split(percentage=0.15, align=True)

            button_align_space = icons.get("icon_align_space") 
            if lt.display_space:
                split.prop(lt, "display_space", text="", icon_value=button_align_space.icon_id)
            else:
                split.prop(lt, "display_space", text="", icon_value=button_align_space.icon_id)
            
            split.operator("mesh.looptools_space", text="LoopTools Space", icon='BLANK1')
            
            # space - settings
            if lt.display_space:
                box = col.box().column(1)              
                
                row = box.column(1) 
                row.prop(lt, "space_interpolation")
                row.prop(lt, "space_input")

                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if lt.space_lock_x:
                    row.prop(lt, "space_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(lt, "space_lock_x", text = "X", icon='UNLOCKED')
                if lt.space_lock_y:
                    row.prop(lt, "space_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(lt, "space_lock_y", text = "Y", icon='UNLOCKED')
                if lt.space_lock_z:
                    row.prop(lt, "space_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(lt, "space_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(lt, "space_influence")

                box.separator() 
                box = col.box().column(1)   


            row = box.row(1)  
            # curve - first line
            split = row.split(percentage=0.15, align=True)

            button_align_curve = icons.get("icon_align_curve") 
            if lt.display_curve:
                split.prop(lt, "display_curve", text="", icon_value=button_align_curve.icon_id)
            else:
                split.prop(lt, "display_curve", text="", icon_value=button_align_curve.icon_id)

            split.operator("mesh.looptools_curve", text="LoopTools Curve", icon='BLANK1')

            # curve - settings
            if lt.display_curve:
                box = col.box().column(1)              
                
                row = box.column(1) 
                row.prop(lt, "curve_interpolation")
                row.prop(lt, "curve_restriction")
                row.prop(lt, "curve_boundaries")
                row.prop(lt, "curve_regular")
                
                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if lt.curve_lock_x:
                    row.prop(lt, "curve_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(lt, "curve_lock_x", text = "X", icon='UNLOCKED')
                if lt.curve_lock_y:
                    row.prop(lt, "curve_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(lt, "curve_lock_y", text = "Y", icon='UNLOCKED')
                if lt.curve_lock_z:
                    row.prop(lt, "curve_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(lt, "curve_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(lt, "curve_influence")

                box.separator() 
                box = col.box().column(1)    


            row = box.row(1)  
            # circle - first line
            split = row.split(percentage=0.15, align=True)

            button_align_circle = icons.get("icon_align_circle") 
            if lt.display_circle:
                split.prop(lt, "display_circle", text="", icon_value=button_align_circle.icon_id)
            else:
                split.prop(lt, "display_circle", text="", icon_value=button_align_circle.icon_id)

            split.operator("mesh.looptools_circle", text="LoopTools Circle", icon='BLANK1')

            # circle - settings
            if lt.display_circle:
                box = col.box().column(1)              
                
                row = box.column(1) 
                row.prop(lt, "circle_fit")
                
                row.separator()

                row.prop(lt, "circle_flatten")
                
                row = box.row(align=True)
                row.prop(lt, "circle_custom_radius")
                
                row_right = row.row(align=True)
                row_right.active = lt.circle_custom_radius
                row_right.prop(lt, "circle_radius", text="")                
                box.prop(lt, "circle_regular")
                
                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if lt.circle_lock_x:
                    row.prop(lt, "circle_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(lt, "circle_lock_x", text = "X", icon='UNLOCKED')
                if lt.circle_lock_y:
                    row.prop(lt, "circle_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(lt, "circle_lock_y", text = "Y", icon='UNLOCKED')
                if lt.circle_lock_z:
                    row.prop(lt, "circle_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(lt, "circle_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(lt, "circle_influence")

                box.separator() 
                box = col.box().column(1)    
                

            row = box.row(1) 
            # flatten - first line
            split = row.split(percentage=0.15, align=True)

            button_align_flatten = icons.get("icon_align_flatten") 
            if lt.display_flatten:
                split.prop(lt, "display_flatten", text="", icon_value=button_align_flatten.icon_id)
            else:
                split.prop(lt, "display_flatten", text="", icon_value=button_align_flatten.icon_id)

            split.operator("mesh.looptools_flatten", text="LoopTool Flatten", icon ="BLANK1")

            # flatten - settings
            if lt.display_flatten:
                box = col.box().column(1)    
                 
                row = box.column(1)  
                row.prop(lt, "flatten_plane")

                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if lt.flatten_lock_x:
                    row.prop(lt, "flatten_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(lt, "flatten_lock_x", text = "X", icon='UNLOCKED')
                if lt.flatten_lock_y:
                    row.prop(lt, "flatten_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(lt, "flatten_lock_y", text = "Y", icon='UNLOCKED')
                if lt.flatten_lock_z:
                    row.prop(lt, "flatten_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(lt, "flatten_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(lt, "flatten_influence")

                box.separator() 


            row = box.row(1)                                                  
            # relax - first line
            split = row.split(percentage=0.15, align=True)
            if lt.display_relax:
                button_align_looptools = icons.get("icon_align_looptools")
                split.prop(lt, "display_relax", text="", icon_value=button_align_looptools.icon_id)
                split.operator("mesh.looptools_relax", text="  LoopTool Relax", icon='BLANK1')

            else:
                button_align_looptools = icons.get("icon_align_looptools")
                split.prop(lt, "display_relax", text="", icon_value=button_align_looptools.icon_id)
                split.operator("mesh.looptools_relax", text="  LoopTool Relax", icon='BLANK1')

            # relax - settings
            if lt.display_relax:
                box = col.box().column(1)    
                 
                row = box.column(1)  
                row.prop(lt, "relax_interpolation")
                row.prop(lt, "relax_input")
                row.prop(lt, "relax_iterations")
                row.prop(lt, "relax_regular")

                box.separator()    



            box.separator()                 



    Display_Relax = context.user_preferences.addons[addon_key].preferences.tab_relax 
    if Display_Relax == 'on':

        box = col.box().column(1)    

        row = box.column(1)                      
 
        button_align_vertices = icons.get("icon_align_vertices") 
        row.operator("mesh.vertices_smooth","Smooth Verts", icon_value=button_align_vertices.icon_id) 

        button_align_laplacian = icons.get("icon_align_laplacian")
        row.operator("mesh.vertices_smooth_laplacian","Smooth Laplacian", icon_value=button_align_laplacian.icon_id)  

        button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
        row.operator("mesh.shrinkwrap_smooth","Smooth Shrinkwrap ", icon_value=button_align_shrinkwrap.icon_id)         
                     
        box.separator()    





    box = col.box().column(1)   
                 
    row = box.row(1)             
    button_align_mirror_edm = icons.get("icon_align_mirror_edm")              
    row.label("Mirror", icon_value=button_align_mirror_edm.icon_id) 

    sub = row.row(1)
    sub.scale_x = 0.3    
    sub.operator("tp_ops.mirror1",text="X")
    sub.operator("tp_ops.mirror2",text="Y")
    sub.operator("tp_ops.mirror3",text="Z")      

    box.separator() 

    row = box.row(1)               
    button_align_mirror_edge = icons.get("icon_align_mirror_edge")   
    row.label("Turn", icon_value=button_align_mirror_edge.icon_id)    
   
    sub = row.row(1)
    sub.scale_x = 0.9          
    sub.operator("tp_ops.mirror_over_edge", "Over Edge")

    box.separator() 

    row = box.row(1)               
    row.label("Mody", icon ="MOD_MIRROR")                 

    sub = row.row(1)
    sub.scale_x = 0.3                               
    sub.operator("tp_ops.mod_mirror_x",text="X")
    sub.operator("tp_ops.mod_mirror_y",text="Y")
    sub.operator("tp_ops.mod_mirror_z",text="Z")      

    box.separator()   


    Display_AutoMirror = context.user_preferences.addons[addon_key].preferences.tab_automirror
    if Display_AutoMirror == 'on':
        
        auto_mirror_addon = "mesh_auto_mirror" 
        state = addon_utils.check(auto_mirror_addon)
        if not state[0]:                         
            
            box = col.box().column(1) 
            
            row = box.column(1) 
            row.operator("tp_ops.enable_automirror", text="!_Activate AutoMirror_!", icon='BLANK1')    
            
            box.separator()

        else:  
            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:


                    box = col.box().column(1) 
                  
                    row = box.row(1)
                    row.label("AutoMirror")

                    row.operator("object.automirror", text="", icon="MOD_WIREFRAME")   
                    
                    box.separator() 
                    
                    row = box.row(1)                           
                    row.prop(context.scene.auto_mirror, "orientation", text="")                                                                          
                    row.prop(context.scene.auto_mirror, "axis", text="")            
                                                            
                    row = box.row(1)

                    if tp_props.display_mirror_auto:            
                        row.prop(tp_props, "display_mirror_auto", text="Settings", icon="TRIA_DOWN")
                    else:
                        row.prop(tp_props, "display_mirror_auto", text="Settings", icon="TRIA_RIGHT") 
     
                    row.prop(context.scene.auto_mirror, "threshold", text="Threshold")      

                    box.separator() 

                    if tp_props.display_mirror_auto:    
                                          
                        box = col.box().column(1) 
                        
                        row = box.row(1)
                        row.prop(context.scene.auto_mirror, "toggle_edit", text="Editmode")
                        row.prop(context.scene.auto_mirror, "cut", text="Cut+Mirror")
                        
                        row = box.row(1)
                        row.prop(context.scene.auto_mirror, "use_clip", text="Use Clip")
                        row.prop(context.scene.auto_mirror, "show_on_cage", text="Editable")            

                        box.separator() 

                else:
                    pass
            else:
                pass
            



    obj = context.active_object
    if obj:
 
        mo_types = []            
        append = mo_types.append

        for mo in obj.modifiers:
                                          
            if mo.type == 'MIRROR':
                append(mo.type)

                #box.label(mo.name)

                row = box.row(1)
                row.prop(mo, "use_x")
                row.prop(mo, "use_y")
                row.prop(mo, "use_z")
                
                row = box.row(1)
                row.prop(mo, "use_clip", text="Clip")
                row.prop(mo, "use_mirror_merge", text="Merge")               
                if mo.use_mirror_merge is True:
                    row.prop(mo, "merge_threshold", text="Limit")

                box.separator() 
    else:
        pass


    obj = context.active_object
    if obj:
        mod_list = obj.modifiers
        if mod_list:
           
            box.separator()                            

            row = box.row()    
            row.alignment = 'CENTER'                      
            row.operator("tp_ops.mods_view", text="", icon='RESTRICT_VIEW_OFF') 
            row.operator("tp_ops.remove_mods_mirror", text="", icon='PANEL_CLOSE') 
            row.operator("tp_ops.apply_mods_mirror_edm", text="", icon='FILE_TICK') 

            box.separator()                                                                      
    else:
        pass





