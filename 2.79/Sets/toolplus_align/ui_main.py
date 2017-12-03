# ##### BEGIN GPL LICENSE BLOCK #####
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


import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
import addon_utils

def draw_axis_tools(context, layout):
    icons = load_icons()

    col = layout.column(align=True)

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

    button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
    row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
             
    sub = row.row(1)
    sub.scale_x = 0.3                   
    sub.operator("tp_ops.mirror1",text="X")
    sub.operator("tp_ops.mirror2",text="Y")
    sub.operator("tp_ops.mirror3",text="Z")            

    box.separator() 

    row = box.row(1)               
    row.label("Mody", icon ="MOD_MIRROR")                 

    sub = row.row(1)
    sub.scale_x = 0.3                               
    sub.operator("tp_ops.mod_mirror_x",text="X")
    sub.operator("tp_ops.mod_mirror_y",text="Y")
    sub.operator("tp_ops.mod_mirror_z",text="Z")      

    box.separator()   

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






def draw_align_panel_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_align   

        icons = load_icons()

        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box()
        
        row = box.row(1)  
        sub = row.row(1)
        sub.scale_x = 7
       
        button_snap_place = icons.get("icon_snap_place")
        sub.menu("VIEW3D_TP_SnapSetMenu", text=" ", icon_value=button_snap_place.icon_id)        
        sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
        sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")    


        col = layout.column(align=True)        

        if context.mode == 'OBJECT':
 
            box = col.box().column(1)  

            row = box.row(1)        
            row.label("Origin to...")  

            row = box.row(1) 
            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("object.transform_apply", text=" ", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_set_cursor", text=" ", icon_value=button_origin_cursor.icon_id)

            button_origin_tomesh = icons.get("icon_origin_tomesh")
            row.operator("tp_ops.origin_tomesh", text=" ", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            row.operator("tp_ops.origin_meshto", text=" ", icon_value=button_origin_meshto.icon_id)

            button_origin_mass = icons.get("icon_origin_mass")           
            row.operator("tp_ops.origin_set_mass", text=" ", icon_value=button_origin_mass.icon_id)                                              

            row = box.row(1)

            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:                

                    if tp_props.display_origin_bbox:                     
                        
                        button_origin_bbox = icons.get("icon_origin_bbox")            
                        row.prop(tp_props, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)                                                
                        row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
                  
                    else:
                       
                        button_origin_bbox = icons.get("icon_origin_bbox")                
                        row.prop(tp_props, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)
                        row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")

                else:
                    row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
                                

            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:

                    if tp_props.display_origin_bbox: 
                     
                         box = col.box().row(1)

                         row = box.column(1) 
                         row.label("+Y") 
                         row.label("Axis") 
                         row.label("Back") 
                         
                         #Top
                         row = box.column(1)
                         
                         button_origin_left_top = icons.get("icon_origin_left_top")                  
                         row.operator("tp_ops.cubeback_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)#"Back- Left -Top")

                         button_origin_left = icons.get("icon_origin_left")
                         row.operator("tp_ops.cubefront_edgemiddle_minus_x", "", icon_value=button_origin_left.icon_id)#"Back- Left")

                         button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                         row.operator("tp_ops.cubeback_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)#"Back- Left -Bottom")
                          
                         #Middle
                         row = box.column(1)

                         button_origin_top = icons.get("icon_origin_top")                     
                         row.operator("tp_ops.cubeback_edgetop_minus_y", "", icon_value=button_origin_top.icon_id)#"Back - Top")                            

                         button_origin_cross = icons.get("icon_origin_cross")
                         row.operator("tp_ops.cubefront_side_plus_y","", icon_value=button_origin_cross.icon_id)#"Back")                 

                         button_origin_bottom = icons.get("icon_origin_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_plus_y","", icon_value=button_origin_bottom.icon_id)#"Back - Bottom") 
                          
                         #Bottom
                         row = box.column(1) 

                         button_origin_right_top = icons.get("icon_origin_right_top")
                         row.operator("tp_ops.cubeback_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)#"Back- Right -Top ")                 

                         button_origin_right = icons.get("icon_origin_right")
                         row.operator("tp_ops.cubefront_edgemiddle_plus_x","", icon_value=button_origin_right.icon_id)#"Back- Right")      

                         button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                         row.operator("tp_ops.cubeback_cornerbottom_plus_xy","", icon_value=button_origin_right_bottom.icon_id)# "Back- Right -Bottom")  

                    
                         box.separator()
                         box.separator()
                         box.separator()
                         
                         row.separator()
                         
                         ############################

                         box = col.box().row(1)

                         row = box.column(1) 
                         row.label("XZ") 
                         row.label("Axis") 
                         row.label("Center") 
                         
                         #Top
                         row = box.column(1)
                         
                         button_origin_left_top = icons.get("icon_origin_left_top")   
                         row.operator("tp_ops.cubefront_edgetop_minus_x","", icon_value=button_origin_left_top.icon_id)#"Middle - Left Top")
                         
                         button_origin_left = icons.get("icon_origin_left")
                         row.operator("tp_ops.cubefront_side_minus_x","", icon_value=button_origin_left.icon_id)#"Left")         
                         
                         button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_minus_x","", icon_value=button_origin_left_bottom.icon_id)#"Middle - Left Bottom")
                          
                         #Middle
                         row = box.column(1) 
                         
                         button_origin_top = icons.get("icon_origin_top")
                         row.operator("tp_ops.cubefront_side_plus_z", "", icon_value=button_origin_top.icon_id)#"Top")  
                         
                         button_origin_diagonal = icons.get("icon_origin_diagonal")
                         row.operator("object.origin_set", text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'                    
                         
                         button_origin_bottom = icons.get("icon_origin_bottom")
                         row.operator("tp_ops.cubefront_side_minus_z","", icon_value=button_origin_bottom.icon_id)#"Bottom")    

                         #Bottom
                         row = box.column(1) 
                         
                         button_origin_right_top = icons.get("icon_origin_right_top")
                         row.operator("tp_ops.cubefront_edgetop_plus_x","", icon_value=button_origin_right_top.icon_id)#"Middle - Right Top")  
                         
                         button_origin_right = icons.get("icon_origin_right")
                         row.operator("tp_ops.cubefront_side_plus_x","", icon_value=button_origin_right.icon_id)#"Right")            
                         
                         button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_plus_x","", icon_value=button_origin_right_bottom.icon_id)#"Middle - Right Bottom")  

                         box.separator()
                         box.separator()
                         box.separator()
                         
                         row.separator()

                         ############################
                         
                         box = col.box().row(1)

                         row = box.column(1) 
                         row.label("-- Y") 
                         row.label("Axis") 
                         row.label("Front") 
                        
                         #Top
                         row = box.column(1) 
                         
                         button_origin_left_top = icons.get("icon_origin_left_top") 
                         row.operator("tp_ops.cubefront_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)#"Front- Left -Top"
                         
                         button_origin_left = icons.get("icon_origin_left")
                         row.operator("tp_ops.cubefront_edgemiddle_minus_y","", icon_value=button_origin_left.icon_id)#"Front- Left"  
                         
                         button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                         row.operator("tp_ops.cubefront_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)#"Front- Left -Bottom"  
                                   
                         #Middle
                         row = box.column(1) 
                         
                         button_origin_top = icons.get("icon_origin_top")
                         row.operator("tp_ops.cubeback_edgetop_plus_y","", icon_value=button_origin_top.icon_id)#"Front - Top"                                      
                         
                         #button_origin_center = icons.get("icon_origin_center")
                         
                         button_origin_cross = icons.get("icon_origin_cross")
                         row.operator("tp_ops.cubefront_side_minus_y","", icon_value=button_origin_cross.icon_id)#"Front"           
                         
                         button_origin_bottom = icons.get("icon_origin_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_minus_y","", icon_value=button_origin_bottom.icon_id)#"Front - Bottom"           

                         #Bottom
                         row = box.column(1) 
                         
                         button_origin_right_top = icons.get("icon_origin_right_top")
                         row.operator("tp_ops.cubefront_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)#"Front- Right -Top"
                         
                         button_origin_right = icons.get("icon_origin_right")
                         row.operator("tp_ops.cubefront_edgemiddle_plus_y","", icon_value=button_origin_right.icon_id)#"Front- Right"    
                         
                         button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                         row.operator("tp_ops.cubefront_cornerbottom_plus_xy", "", icon_value=button_origin_right_bottom.icon_id)#"Front- Right -Bottom") 

                         box.separator()
                         box.separator()
                         box.separator()
                         
                         row.separator()
            
            box.separator()  


            box = col.box().column(1)         
            
            row = box.row(1)
            row.label("Align to...")                  
           
            row = box.row(1)
            props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_TRANS')   
            props.tp_axis='axis_xyz'
            props.tp_transform='LOCATION'

            props = row.operator("tp_ops.align_transform",text="X")
            props.tp_axis='axis_x'
            props.tp_transform='LOCATION'

            props = row.operator("tp_ops.align_transform",text="Y")
            props.tp_axis='axis_y'
            props.tp_transform='LOCATION' 
 
            props = row.operator("tp_ops.align_transform",text="Z")
            props.tp_axis='axis_z'
            props.tp_transform='LOCATION'
       
            sub = row.row(1)
            sub.scale_x = 2.0    
            sub.operator("object.location_clear", text= " ", icon="X")
          
            props = row.operator("object.transform_apply", text=" ",icon="FILE_TICK")
            props.location= True
            props.rotation= False
            props.scale= False
                         
            row = box.row(1)

            props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_ROT') 
            props.tp_axis='axis_xyz'
            props.tp_transform='ROTATION'

            props = row.operator("tp_ops.align_transform",text="X")
            props.tp_axis='axis_x'
            props.tp_transform='ROTATION'

            props = row.operator("tp_ops.align_transform",text="Y")
            props.tp_axis='axis_y'
            props.tp_transform='ROTATION'

            props = row.operator("tp_ops.align_transform",text="Z")
            props.tp_axis='axis_z'
            props.tp_transform='ROTATION'
            
            sub = row.row(1)
            sub.scale_x = 2.0           
            sub.operator("object.rotation_clear", text=" ", icon="X")
            props = row.operator("object.transform_apply", text=" ",icon="FILE_TICK")
            props.location= False
            props.rotation= True
            props.scale= False           

            row = box.row(1)
            props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_SCALE')  
            props.tp_axis='axis_xyz'
            props.tp_transform='SCALE'

            props = row.operator("tp_ops.align_transform",text="X")
            props.tp_axis='axis_x'
            props.tp_transform='SCALE'

            props = row.operator("tp_ops.align_transform",text="Y")
            props.tp_axis='axis_y'
            props.tp_transform='SCALE'

            props = row.operator("tp_ops.align_transform",text="Z")
            props.tp_axis='axis_z'
            props.tp_transform='SCALE'
            
            sub = row.row(1)
            sub.scale_x = 2.0           
            sub.operator("object.scale_clear", text=" ", icon="X")
            
            props = row.operator("object.transform_apply", text=" ",icon="FILE_TICK")
            props.location= False
            props.rotation= False
            props.scale= True  
       
            box.separator()        

            row = box.row(1)  
            
            button_align_advance = icons.get("icon_align_advance")
            row.operator("tp_origin.align_tools", "Advance", icon_value=button_align_advance.icon_id)    
       
            button_origin_align = icons.get("icon_origin_align") 
            row.operator("object.distribute_osc", text="Even", icon_value=button_origin_align.icon_id)           
        
 
            box.separator() 
            
            row = box.row(1)                     
            row.prop(context.space_data, "transform_orientation", text="", icon='MANIPUL')
            row.operator("transform.create_orientation", text="", icon='ZOOMIN')

            if context.space_data.current_orientation:
                box.separator() 
                
                row = box.row(1)
                row.prop(context.space_data.current_orientation, "name", text="")
                row.operator("transform.delete_orientation", text="", icon='X')

            box.separator()       



            box = col.box().column(1)       
                         
            row = box.row(1)             

            row.label("Zero to...")  
            row = box.row()
            row.prop(context.scene, 'tp_switch_axis', expand=True)      

            row = box.row(1)
            row.prop(context.scene, 'tp_switch', expand=True)              
          
            button_align_zero = icons.get("icon_align_zero") 
            row.operator("tp_ops.zero_axis_panel", text="Run", icon_value=button_align_zero.icon_id)  

            box.separator()  


            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:


                    box = col.box().column(1)           

                    row = box.column(1)  

                    button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                    row.operator("object.align_by_faces", text="Face to Face", icon_value=button_snap_face_to_face.icon_id)  

                    button_snap_drop_down = icons.get("icon_snap_drop_down") 
                    row.operator("object.drop_on_active", text="Drop on Active", icon_value=button_snap_drop_down.icon_id) 

                    button_snap_abc = icons.get("icon_snap_abc") 
                    row.operator("tp_ops.np_020_point_align", text='ABC Point Align', icon_value=button_snap_abc.icon_id) 
                   
                    button_snap_offset = icons.get("icon_snap_offset")  
                    row.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   
                    
                    box.separator()     


                    box = col.box().column(1)         

                    row = box.row(1)
                   
                    button_snap_grab = icons.get("icon_snap_grab") 
                    row.operator("tp_ops.np_020_point_move", text='G', icon_value=button_snap_grab.icon_id)
                   
                    button_snap_rotate = icons.get("icon_snap_rotate") 
                    row.operator("tp_ops.np_020_roto_move", text='R', icon_value=button_snap_rotate.icon_id)

                    button_snap_scale = icons.get("icon_snap_scale") 
                    row.operator("tp_ops.np_020_point_scale", text='S', icon_value=button_snap_scale.icon_id)

                    box.separator()                      


                    box = col.box().column(1)           
                  
                    row = box.column(1) 
                    row.label("Interpolate...")              
                  
                    row = box.column(1)    
                    row.operator("mesh.wplsmthdef_snap", text="Save Mesh State", icon ="SHAPEKEY_DATA")

                    box.separator() 

                else:
                    pass

 
            box = col.box().column(1) 
                      
            row = box.row(1)  
            button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
            row.label("Mirror", icon_value=button_align_mirror_obm.icon_id)                 

            sub = row.row(1)
            sub.scale_x = 0.3                               
            sub.operator("tp_ops.mirror1",text="X")
            sub.operator("tp_ops.mirror2",text="Y")
            sub.operator("tp_ops.mirror3",text="Z")      

            box.separator()   

            row = box.row(1)               
            row.label("Mody", icon ="MOD_MIRROR")                 

            sub = row.row(1)
            sub.scale_x = 0.3                               
            sub.operator("tp_ops.mod_mirror_x",text="X")
            sub.operator("tp_ops.mod_mirror_y",text="Y")
            sub.operator("tp_ops.mod_mirror_z",text="Z")      

            box.separator()   


            Display_AutoMirror = context.user_preferences.addons[__package__].preferences.tab_automirror
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

                            obj = context.active_object
                            if obj:
                                mod_list = obj.modifiers
                                if mod_list:
                                    row.operator("tp_ops.mods_view","", icon = 'RESTRICT_VIEW_OFF')                                                                            
                            else:
                                pass


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
                    row.operator("tp_ops.apply_mods_mirror", text="", icon='FILE_TICK') 

                    box.separator()                                                                      
            else:
                pass

      




        if context.mode == 'EDIT_MESH':


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
                     
                         box = col.box().row(1)

                         row = box.column(1) 
                         row.label("+Y") 
                         row.label("Axis") 
                         row.label("Back") 
                         
                         #Top
                         row = box.column(1)
                         
                         button_origin_left_top = icons.get("icon_origin_left_top")                  
                         row.operator("tp_ops.cubeback_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)#"Back- Left -Top")

                         button_origin_left = icons.get("icon_origin_left")
                         row.operator("tp_ops.cubefront_edgemiddle_minus_x", "", icon_value=button_origin_left.icon_id)#"Back- Left")

                         button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                         row.operator("tp_ops.cubeback_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)# "Back- Left -Bottom")
                          
                         #Middle
                         row = box.column(1)

                         button_origin_top = icons.get("icon_origin_top")                     
                         row.operator("tp_ops.cubeback_edgetop_minus_y", "", icon_value=button_origin_top.icon_id)#"Back - Top")                            

                         button_origin_cross = icons.get("icon_origin_cross")
                         row.operator("tp_ops.cubefront_side_plus_y","", icon_value=button_origin_cross.icon_id)# "Back")                 

                         button_origin_bottom = icons.get("icon_origin_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_plus_y","", icon_value=button_origin_bottom.icon_id)#"Back - Bottom") 
                          
                         #Bottom
                         row = box.column(1) 

                         button_origin_right_top = icons.get("icon_origin_right_top")
                         row.operator("tp_ops.cubeback_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)# "Back- Right -Top ")                 

                         button_origin_right = icons.get("icon_origin_right")
                         row.operator("tp_ops.cubefront_edgemiddle_plus_x","", icon_value=button_origin_right.icon_id)#"Back- Right")      

                         button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                         row.operator("tp_ops.cubeback_cornerbottom_plus_xy","", icon_value=button_origin_right_bottom.icon_id)# "Back- Right -Bottom")  

                    
                         box.separator()
                         box.separator()
                         box.separator()
                         
                         row.separator()
                         
                         ############################

                         box = col.box().row(1)

                         row = box.column(1) 
                         row.label("XZ") 
                         row.label("Axis") 
                         row.label("Center") 
                         
                         #Top
                         row = box.column(1)
                         
                         button_origin_left_top = icons.get("icon_origin_left_top")   
                         row.operator("tp_ops.cubefront_edgetop_minus_x","", icon_value=button_origin_left_top.icon_id)#"Middle - Left Top")
                         
                         button_origin_left = icons.get("icon_origin_left")
                         row.operator("tp_ops.cubefront_side_minus_x","", icon_value=button_origin_left.icon_id)# "Left")         
                         
                         button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_minus_x","", icon_value=button_origin_left_bottom.icon_id)#"Middle - Left Bottom")
                          
                         #Middle
                         row = box.column(1) 
                         
                         button_origin_top = icons.get("icon_origin_top")
                         row.operator("tp_ops.cubefront_side_plus_z", "", icon_value=button_origin_top.icon_id)#"Top")  
                         
                         button_origin_diagonal = icons.get("icon_origin_diagonal")
                         row.operator("object.origin_set", text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'                    
                         
                         button_origin_bottom = icons.get("icon_origin_bottom")
                         row.operator("tp_ops.cubefront_side_minus_z","", icon_value=button_origin_bottom.icon_id)# "Bottom")    

                         #Bottom
                         row = box.column(1) 
                         
                         button_origin_right_top = icons.get("icon_origin_right_top")
                         row.operator("tp_ops.cubefront_edgetop_plus_x","", icon_value=button_origin_right_top.icon_id)#"Middle - Right Top")  
                         
                         button_origin_right = icons.get("icon_origin_right")
                         row.operator("tp_ops.cubefront_side_plus_x","", icon_value=button_origin_right.icon_id)# "Right")            
                         
                         button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_plus_x","", icon_value=button_origin_right_bottom.icon_id)#"Middle - Right Bottom")  

                         box.separator()
                         box.separator()
                         box.separator()
                         
                         row.separator()

                         ############################
                         
                         box = col.box().row(1)

                         row = box.column(1) 
                         row.label("-- Y") 
                         row.label("Axis") 
                         row.label("Front") 
                        
                         #Top
                         row = box.column(1) 
                         
                         button_origin_left_top = icons.get("icon_origin_left_top") 
                         row.operator("tp_ops.cubefront_cornertop_minus_xy", "", icon_value=button_origin_left_top.icon_id)# "Front- Left -Top"
                         
                         button_origin_left = icons.get("icon_origin_left")
                         row.operator("tp_ops.cubefront_edgemiddle_minus_y","", icon_value=button_origin_left.icon_id)# "Front- Left"  
                         
                         button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                         row.operator("tp_ops.cubefront_cornerbottom_minus_xy","", icon_value=button_origin_left_bottom.icon_id)# "Front- Left -Bottom"  
                                   
                         #Middle
                         row = box.column(1) 
                         
                         button_origin_top = icons.get("icon_origin_top")
                         row.operator("tp_ops.cubeback_edgetop_plus_y","", icon_value=button_origin_top.icon_id)# "Front - Top"                                      
                                                    
                         button_origin_cross = icons.get("icon_origin_cross")
                         row.operator("tp_ops.cubefront_side_minus_y","", icon_value=button_origin_cross.icon_id)#  "Front"           
                         
                         button_origin_bottom = icons.get("icon_origin_bottom")
                         row.operator("tp_ops.cubefront_edgebottom_minus_y","", icon_value=button_origin_bottom.icon_id)# "Front - Bottom"           

                         #Bottom
                         row = box.column(1) 
                         
                         button_origin_right_top = icons.get("icon_origin_right_top")
                         row.operator("tp_ops.cubefront_cornertop_plus_xy","", icon_value=button_origin_right_top.icon_id)#  "Front- Right -Top"
                         
                         button_origin_right = icons.get("icon_origin_right")
                         row.operator("tp_ops.cubefront_edgemiddle_plus_y","", icon_value=button_origin_right.icon_id)# "Front- Right"    
                         
                         button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                         row.operator("tp_ops.cubefront_cornerbottom_plus_xy", "", icon_value=button_origin_right_bottom.icon_id)# "Front- Right -Bottom") 

                         box.separator()
                         box.separator()
                         box.separator()
                         
                         row.separator()
            
           

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

            #imdjs_tools
            #button_align_radians = icons.get("icon_align_radians")  
            #row.operator("me

            box.separator()
      
         
            Display_Looptools = context.user_preferences.addons[__package__].preferences.tab_looptools
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

                    box.separator()                 



            Display_Relax = context.user_preferences.addons[__package__].preferences.tab_relax 
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

                Display_Looptools = context.user_preferences.addons[__package__].preferences.tab_looptools
                if Display_Looptools == 'on':

                    loop_tools_addon = "mesh_looptools" 
                    state = addon_utils.check(loop_tools_addon)
                    if not state[0]:             
                        pass        
                    else: 
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


            Display_AutoMirror = context.user_preferences.addons[__package__].preferences.tab_automirror
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






        if context.mode == 'EDIT_LATTICE':
            
                       
            col = layout.column(align=True)

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

            button_flip_lattice = icons.get("icon_flip_lattice")              
            row.label("Flip", icon_value=button_flip_lattice.icon_id) 
                     
            sub = row.row(1)
            sub.scale_x = 0.3 
            sub.operator("lattice.flip", text="X").axis = "U"
            sub.operator("lattice.flip", text="Y").axis = "V"
            sub.operator("lattice.flip", text="Z").axis = "W"

            box.separator()

            row = box.row(1)  

            button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
            row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
                     
            sub = row.row(1)
            sub.scale_x = 0.3           
            sub.operator("tp_ops.mirror1",text="X")
            sub.operator("tp_ops.mirror2",text="Y")
            sub.operator("tp_ops.mirror3",text="Z")            
    
            box.separator()



        if context.mode == 'EDIT_CURVE' or context.mode == 'EDIT_SURFACE':

            draw_axis_tools(context, layout)
              

        if context.mode == 'EDIT_METABALL':    
            
            draw_axis_tools(context, layout)  


        if context.mode == 'EDIT_ARMATURE':     
            
            draw_axis_tools(context, layout)             





EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']


class VIEW3D_TP_Align_TOOLS(bpy.types.Panel):
    bl_category = "Align"
    bl_idname = "VIEW3D_TP_Align_TOOLS"
    bl_label = "Align"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT
        
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_align_panel_layout(self, context, layout) 



class VIEW3D_TP_Align_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Align_UI"
    bl_label = "Align"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_align_panel_layout(self, context, layout) 



class VIEW3D_TP_Align_PROPS(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Align_PROPS"
    bl_label = "Align"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_align_panel_layout(self, context, layout) 
        
        
