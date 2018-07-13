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



def draw_object_layout(self, context, layout):
    tp_props = context.window_manager.tp_collapse_align   
    tp_props_zero = context.window_manager.tp_props_zero   

    addon_key = __package__.split(".")[0]    
    panel_prefs = context.user_preferences.addons[addon_key].preferences

    icons = load_icons()

    col = layout.column(align=True)        

    # ORIGIN #
    Display_Origin = context.user_preferences.addons[addon_key].preferences.tab_origin
    if Display_Origin == True: 

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

        selected = bpy.context.selected_objects
        n = len(selected)                         
        if n == 1:

            button_origin_tosnap = icons.get("icon_origin_tosnap")         
            row.operator("tp_ops.origin_modal", text="", icon_value=button_origin_tosnap.icon_id)

        button_origin_mass = icons.get("icon_origin_mass")           
        row.operator("tp_ops.origin_set_mass", text=" ", icon_value=button_origin_mass.icon_id)                                              

        box.separator()

        row = box.row(1)

        obj = context.active_object
        if obj:
            obj_type = obj.type
            
            if obj.type in {'MESH'}:                

                if tp_props.display_origin_bbox:                     
                    
                    button_origin_bbox = icons.get("icon_origin_bbox")            
                    row.prop(tp_props, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)                                                
                    row.operator("tp_ops.bbox_origin_modal_ops", text="   BBoxOrigin")
              
                else:
                   
                    button_origin_bbox = icons.get("icon_origin_bbox")                
                    row.prop(tp_props, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)
                    row.operator("tp_ops.bbox_origin_modal_ops", text="   BBoxOrigin")

            else:
                row.operator("tp_ops.bbox_origin_modal_ops", text="   BBoxOrigin")
                            

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

        box.separator()  
       

    # ALIGN TO #
    Display_Align = context.user_preferences.addons[addon_key].preferences.tab_align_to 
    if Display_Align == True: 

        box = col.box().column(1)         
        
        row = box.row(1)
        row.label("Align to...")                  


        row = box.row(1)
        button_align_advance = icons.get("icon_align_advance")
        row.operator("tp_origin.align_tools", " ", icon_value=button_align_advance.icon_id, emboss=False)   
       
        button_align_x = icons.get("icon_align_x") 
        row.label(text=" ", icon_value=button_align_x.icon_id)  
      
        button_align_y = icons.get("icon_align_y") 
        row.label(text=" ", icon_value=button_align_y.icon_id)  
       
        button_align_z = icons.get("icon_align_z") 
        row.label(text=" ", icon_value=button_align_z.icon_id)  

        row.label(text=" ", icon='BLANK1')  
        row.label(text=" ", icon='BLANK1')  
       
       
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
        sub.operator("object.location_clear", text= " ", icon="PANEL_CLOSE")

        button_apply = icons.get("icon_apply")    
        props = row.operator("object.transform_apply", text=" ", icon_value=button_apply.icon_id)
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
        sub.operator("object.rotation_clear", text=" ", icon="PANEL_CLOSE")

        button_apply = icons.get("icon_apply")  
        props = row.operator("object.transform_apply", text=" ", icon_value=button_apply.icon_id)
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
        sub.operator("object.scale_clear", text=" ", icon="PANEL_CLOSE")

        button_apply = icons.get("icon_apply")      
        props = row.operator("object.transform_apply", text=" ", icon_value=button_apply.icon_id)
        props.location= False
        props.rotation= False
        props.scale= True  
       
        box.separator()        

        row = box.row(1)  

        row.operator("tp_ops.xy_spread", text="DXF-Spread", icon="AXIS_TOP")  
       
        button_origin_distribute = icons.get("icon_origin_distribute")  
        row.operator("tp_ops.distribute_objects", "Distribute", icon_value=button_origin_distribute.icon_id)       
     
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

    # ZERO TO #
    Display_Zero = context.user_preferences.addons[addon_key].preferences.tab_zero_to 
    if Display_Zero == True: 

        box = col.box().column(1)       
                     
        row = box.row(1)             

        row.label("Zero to...")  
        row = box.row()
        row.prop(tp_props_zero, 'tp_switch', expand=True)      
       
        box.separator()  

        row = box.row(1)
        row.prop(tp_props_zero, 'align_x')              
        row.prop(tp_props_zero, 'align_y')              
        row.prop(tp_props_zero, 'align_z')              
      
        button_align_zero = icons.get("icon_align_zero") 
        row.operator("tp_ops.zero_axis", text="Run", icon_value=button_align_zero.icon_id)  

        box.separator()  


    obj = context.active_object
    if obj:
        obj_type = obj.type
        
        if obj.type in {'MESH'}:


            # TOOLS #
            Display_Aligner = context.user_preferences.addons[addon_key].preferences.tab_aligner
            if Display_Aligner == True: 

                box = col.box().column(1)           

                row = box.column(1)  

                button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                row.operator("object.align_by_faces", text="Face to Face", icon_value=button_snap_face_to_face.icon_id)  

                button_snap_drop_down = icons.get("icon_snap_drop_down") 
                row.operator("object.drop_on_active", text="Drop on Active", icon_value=button_snap_drop_down.icon_id) 
               
                button_snap_offset = icons.get("icon_snap_offset")  
                row.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   

                button_lattice_apply = icons.get("icon_lattice_apply") 
                row.operator("tp_ops.lattice_apply", "Apply Easy Lattice", icon_value=button_lattice_apply.icon_id)   
                        
                box.separator()     

          
            # NP STATION #
            Display_Station = context.user_preferences.addons[addon_key].preferences.tab_station
            if Display_Station == True: 

                box = col.box().column(1)         

                row = box.row(1)

                button_snap_grab = icons.get("icon_snap_grab") 
                row.operator("tp_ops.np_020_point_move", text='G', icon_value=button_snap_grab.icon_id)
               
                button_snap_rotate = icons.get("icon_snap_rotate") 
                row.operator("tp_ops.np_020_roto_move", text='R', icon_value=button_snap_rotate.icon_id)

                button_snap_scale = icons.get("icon_snap_scale") 
                row.operator("tp_ops.np_020_point_scale", text='S', icon_value=button_snap_scale.icon_id)
     
                button_snap_abc = icons.get("icon_snap_abc") 
                row.operator("tp_ops.np_020_point_align", text='A', icon_value=button_snap_abc.icon_id)  
               
                box.separator()                      

            # INTERPOLATE #
            Display_Interpolate = context.user_preferences.addons[addon_key].preferences.tab_interpolate
            if Display_Interpolate == True: 
            
                box = col.box().column(1)           
              
                row = box.column(1) 
                row.label("Interpolate...")              
              
                row = box.column(1)    
                row.operator("mesh.wplsmthdef_snap", text="Save Mesh State", icon ="SHAPEKEY_DATA")

                box.separator() 


        else:
            pass

 
    # MIRROR # 
    Display_Mirror = context.user_preferences.addons[addon_key].preferences.tab_mirror
    if Display_Mirror == True: 
        
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



    # AUTO MIRROR # 
    Display_AutoMirror = context.user_preferences.addons[addon_key].preferences.tab_automirror
    if Display_AutoMirror == True:
        
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

  



