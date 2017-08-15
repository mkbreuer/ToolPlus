__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy, mathutils, math, re
from mathutils.geometry import intersect_line_plane
from mathutils import Vector
from math import radians

from bpy import *
from bpy.props import *
from . icons.icons import load_icons


#Align
def axe_select(self, context):
    axes = ['X','Y','Z']
    return [tuple(3 * [axe]) for axe in axes]

#Align
def project_select(self, context):
    projects = ['XY','XZ','YZ','XYZ']
    return [tuple(3 * [proj]) for proj in projects]


def draw_cursor_origin_tools(context, layout):
    icons = load_icons()
    
    Display_Snap_to = context.user_preferences.addons[__package__].preferences.tab_batch_snap_to
    if Display_Snap_to == 'on':

        box = layout.box().column(1)  
        
        Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
        if Display_Title == 'on':
            
            row = box.row(1)          
            row.label("Cursor to...")  

        row = box.row(1) 
        button_cursor_center = icons.get("icon_cursor_center")
        row.operator("view3d.snap_cursor_to_center", text=" ", icon_value=button_cursor_center.icon_id)

        button_cursor_object = icons.get("icon_cursor_object")
        row.operator("view3d.snap_cursor_to_selected", text=" ", icon_value=button_cursor_object.icon_id)

        button_cursor_active_obm = icons.get("icon_cursor_active_obm")
        row.operator("view3d.snap_cursor_to_active", text=" ", icon_value=button_cursor_active_obm.icon_id)

        button_cursor_grid = icons.get("icon_cursor_grid")
        row.operator("view3d.snap_cursor_to_grid", text=" ", icon_value=button_cursor_grid.icon_id)

        box.separator() 

        Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
        if Display_Title == 'on':
            
            row = box.row(1)           
            row.label("Selected to...")  

        row = box.row(1) 

        button_select_center = icons.get("icon_select_center")
        row.operator("tp_ops.zero_all_axis", text=" ", icon_value=button_select_center.icon_id)

        button_select_cursor = icons.get("icon_select_cursor")           
        row.operator("view3d.snap_selected_to_cursor", text=" ", icon_value=button_select_cursor.icon_id).use_offset=False

        button_select_active_obm = icons.get("icon_select_active_obm")
        row.operator("view3d.snap_selected_to_active", text=" ", icon_value=button_select_active_obm.icon_id)

        button_select_grid = icons.get("icon_select_grid")
        row.operator("view3d.snap_selected_to_grid", text=" ", icon_value=button_select_grid.icon_id)

        button_select_cursor_offset_obm = icons.get("icon_select_cursor_offset_obm")           
        row.operator("view3d.snap_selected_to_cursor", text=" ", icon_value=button_select_cursor_offset_obm.icon_id).use_offset=True

        box.separator() 


    Display_Origin_to = context.user_preferences.addons[__package__].preferences.tab_batch_origin_to
    if Display_Origin_to == 'on':

        box = layout.box().column(1)  

        Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
        if Display_Title == 'on':

            row = box.row(1)           
            row.label("Origin to...")  

        row = box.row(1) 

        button_origin_center_view = icons.get("icon_origin_center_view")
        row.operator("tp_ops.origin_set_center", text=" ", icon_value=button_origin_center_view.icon_id)

        button_origin_cursor = icons.get("icon_origin_cursor")
        row.operator("tp_ops.origin_cursor_edm", text=" ", icon_value=button_origin_cursor.icon_id)            

        button_origin_edm = icons.get("icon_origin_edm")            
        row.operator("tp_ops.origin_edm"," ", icon_value=button_origin_edm.icon_id)       

        button_origin_obj = icons.get("icon_origin_obj")   
        row.operator("tp_ops.origin_obm"," ", icon_value=button_origin_obj.icon_id)             

        box.separator()  


def draw_scale_align_tools(context, layout):
    icons = load_icons()
    
    Display_Align_to_Axis = context.user_preferences.addons[__package__].preferences.tab_batch_align_to_axis
    if Display_Align_to_Axis == 'on':

        box = layout.box().row()
        
        row = box.column(1) 
        row.label("Align") 
        row.label("to") 
        row.label("Axis") 

        row = box.column(1)

        button_align_xy = icons.get("icon_align_xy") 
        row.operator("tp_ops.face_align_xy", "Xy", icon_value=button_align_xy.icon_id)

        button_align_zx = icons.get("icon_align_zx")
        row.operator("tp_ops.face_align_xz", "Zx", icon_value=button_align_zx.icon_id)

        button_align_zy = icons.get("icon_align_zy") 
        row.operator("tp_ops.face_align_yz", "Zy", icon_value=button_align_zy.icon_id)           

        row = box.column(1)

        button_align_x = icons.get("icon_align_x") 
        row.operator("tp_ops.face_align_x", "X", icon_value=button_align_x.icon_id)

        button_align_y = icons.get("icon_align_y") 
        row.operator("tp_ops.face_align_y", "Y", icon_value=button_align_y.icon_id)           

        button_align_z = icons.get("icon_align_z") 
        row.operator("tp_ops.face_align_z", "Z", icon_value=button_align_z.icon_id)

        box.separator()  
        

        Display_Align_Tools = context.user_preferences.addons[__package__].preferences.tab_batch_align_tools
        if Display_Align_Tools == 'on':

            if bpy.context.mode == "EDIT_MESH":

                box = layout.box().column(1)    

                row = box.column(1)                  
                
                button_align_to_normal = icons.get("icon_align_to_normal") 
                row.operator("tp_ops.align_to_normal", "Align to Normal", icon_value=button_align_to_normal.icon_id)    

                button_align_planar = icons.get("icon_align_planar") 
                row.operator("mesh.face_make_planar", "Make Planar Faces", icon_value=button_align_planar.icon_id)    

                box.separator() 
                          
                box = layout.box().column(1)   
                             
                row = box.column(1)                                                         

                button_align_straigten = icons.get("icon_align_straigten") 
                row.operator("mesh.vertex_align",text="Straighten", icon_value=button_align_straigten.icon_id) 

                button_align_distribute = icons.get("icon_align_distribute")  
                row.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_align_distribute.icon_id)                                        
                
                #imdjs_tools
                #button_align_radians = icons.get("icon_align_radians")  
                #row.operator("mesh.round_selected_points", text="Radians", icon_value=button_align_radians.icon_id)  

                box.separator() 




class View3D_TP_Align_Menu(bpy.types.Operator):
    """T+ Align Batch :)"""
    bl_label = "T+ Align"
    bl_idname = "tp_batch.align_menu"               
    bl_options = {'REGISTER', 'UNDO'}          
    
    bpy.types.Scene.AxesProperty = bpy.props.EnumProperty(items=axe_select)
    bpy.types.Scene.ProjectsProperty = bpy.props.EnumProperty(items=project_select)

    def draw(self, context):
        tpw = context.window_manager.tp_collapse_menu_align
        lt = context.window_manager.bbox_origin_window    
        tp = context.window_manager.tp_align_looptools

        icons = load_icons()
        
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box().column(1) 
        
        row = box.row(1)  
        sub = row.row(1)
        sub.scale_x = 7

        sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
        sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")                   

        Display_Snap_Set = context.user_preferences.addons[__package__].preferences.tab_batch_snap_set
        if Display_Snap_Set == 'on':

            box = layout.box().column(1)  
            
            Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
            if Display_Title == 'on':
                
                row = box.row(1)        
                row.label("SnapSet")  

            row = box.row(1) 

            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tp_ops.grid", text=" ", icon_value=button_snap_grid.icon_id)
            
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tp_ops.place", text=" ", icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tp_ops.retopo", text=" ", icon_value=button_snap_retopo.icon_id)                

            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tp_ops.active_3d", text=" ", icon_value=button_snap_cursor.icon_id) 
 
            button_snap_active = icons.get("icon_snap_active")
            row.operator("tp_ops.active_vert", text=" ", icon_value=button_snap_active.icon_id)

            box.separator() 


        if context.mode == 'OBJECT':


            Display_Snap_to = context.user_preferences.addons[__package__].preferences.tab_batch_snap_to
            if Display_Snap_to == 'on':

                box = layout.box().column(1)  

                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':
                                    
                    row = box.row(1)        
                    row.label("Cursor to...")  

                row = box.row(1) 
                button_cursor_center = icons.get("icon_cursor_center")
                row.operator("view3d.snap_cursor_to_center", text=" ", icon_value=button_cursor_center.icon_id)

                button_cursor_object = icons.get("icon_cursor_object")
                row.operator("view3d.snap_cursor_to_selected", text=" ", icon_value=button_cursor_object.icon_id)

                button_cursor_active_obm = icons.get("icon_cursor_active_obm")
                row.operator("view3d.snap_cursor_to_active", text=" ", icon_value=button_cursor_active_obm.icon_id)

                button_cursor_grid = icons.get("icon_cursor_grid")
                row.operator("view3d.snap_cursor_to_grid", text=" ", icon_value=button_cursor_grid.icon_id)

                #Custom
                #button_cursor_center_offset_obm = icons.get("icon_cursor_center_offset_obm")           
                #row.operator("tp_ops.active_3d", text=" ", icon_value=button_cursor_center_offset_obm.icon_id)

                box.separator() 

                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':

                    row = box.row(1)    
                    row.label("Selected to...")  

                row = box.row(1) 
                button_select_center = icons.get("icon_select_center")
                row.operator("tp_ops.zero_all_axis", text=" ", icon_value=button_select_center.icon_id)

                button_select_cursor = icons.get("icon_select_cursor")           
                row.operator("view3d.snap_selected_to_cursor", text=" ", icon_value=button_select_cursor.icon_id).use_offset=False

                button_select_active_obm = icons.get("icon_select_active_obm")
                row.operator("view3d.snap_selected_to_active", text=" ", icon_value=button_select_active_obm.icon_id)

                button_select_grid = icons.get("icon_select_grid")
                row.operator("view3d.snap_selected_to_grid", text=" ", icon_value=button_select_grid.icon_id)

                button_select_cursor_offset_obm = icons.get("icon_select_cursor_offset_obm")           
                row.operator("view3d.snap_selected_to_cursor", text=" ", icon_value=button_select_cursor_offset_obm.icon_id).use_offset=True

                box.separator() 


            Display_Origin_to = context.user_preferences.addons[__package__].preferences.tab_batch_origin_to
            if Display_Origin_to == 'on':
 
                box = layout.box().column(1)  

                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':
                    
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

                box.separator()                                                     

                row = box.row(1)

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:                

                        if lt.display_origin_bbox:                     
                            
                            button_origin_bbox = icons.get("icon_origin_bbox")            
                            row.prop(lt, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)                     
                           
                            row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
                      
                        else:
                           
                            button_origin_bbox = icons.get("icon_origin_bbox")                
                            row.prop(lt, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)
                            row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")

                    else:
                        row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
                                    
                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:

                        if lt.display_origin_bbox: 
                         
                             box = layout.box().row(1)

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

                             box = layout.box().row(1)

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
                             
                             box = layout.box().row(1)

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



            Display_Align_to_Axis = context.user_preferences.addons[__package__].preferences.tab_batch_align_to_axis
            if Display_Align_to_Axis == 'on':

                box = layout.box().column(1)  

                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':   
                                 
                    row = box.row(1)        
                    row.label("Align to...")  
                            
                row = box.row(1)
                row.operator("object.align_location_all",text=" ", icon='MAN_TRANS')  
                row.operator("object.align_location_x",text="X")
                row.operator("object.align_location_y",text="Y")
                row.operator("object.align_location_z",text="Z")
            
                sub = row.row(1)
                sub.scale_x = 2.0    
                sub.operator("object.location_clear", text="", icon="X")
              
                props = row.operator("object.transform_apply", text="",icon="FILE_TICK")
                props.location= True
                props.rotation= False
                props.scale= False
                             
                row = box.row(1)
                row.operator("object.align_rotation_all",text=" ", icon='MAN_ROT') 
                row.operator("object.align_rotation_x",text="X")
                row.operator("object.align_rotation_y",text="Y")
                row.operator("object.align_rotation_z",text="Z")
                
                sub = row.row(1)
                sub.scale_x = 2.0           
                sub.operator("object.rotation_clear", text="", icon="X")
                props = row.operator("object.transform_apply", text="",icon="FILE_TICK")
                props.location= False
                props.rotation= True
                props.scale= False           

                row = box.row(1)
                row.operator("object.align_objects_scale_all",text=" ", icon='MAN_SCALE')  
                row.operator("object.align_objects_scale_x",text="X")
                row.operator("object.align_objects_scale_y",text="Y")
                row.operator("object.align_objects_scale_z",text="Z")
                
                sub = row.row(1)
                sub.scale_x = 2.0           
                sub.operator("object.scale_clear", text="", icon="X")
                
                props = row.operator("object.transform_apply", text="",icon="FILE_TICK")
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



            Display_Zero_to = context.user_preferences.addons[__package__].preferences.tab_batch_zero_to
            if Display_Zero_to == 'on':

                box = layout.box().column(1)           

                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':   
                                 
                    row = box.row(1)             
                    row.label("Zero to...")  

                row = box.row()
                row.prop(context.scene, 'tp_switch_axis', expand=True)      

                row = box.row(1)
                row.prop(context.scene, 'tp_switch', expand=True)

                button_align_zero = icons.get("icon_align_zero")  
                row.operator("tp_ops.zero_axis_panel", text=" ", icon_value=button_align_zero.icon_id)  

                box.separator()  



            Display_Snap_Tools = context.user_preferences.addons[__package__].preferences.tab_batch_snap_tools
            if Display_Snap_Tools == 'on':
                
                        
                box = layout.box().column(1)           

                row = box.column(1)     

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:
                   

                        button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                        row.operator("object.align_by_faces", text="Face to Face", icon_value=button_snap_face_to_face.icon_id)  

                        button_snap_drop_down = icons.get("icon_snap_drop_down") 
                        row.operator("object.drop_on_active", text="Drop on Active", icon_value=button_snap_drop_down.icon_id) 

                        button_snap_offset = icons.get("icon_snap_offset")  
                        row.operator("view3d.xoffsets_main", "Offset & Rotate", icon_value=button_snap_offset.icon_id)   

                        box.separator()  

                        if context.mode == 'OBJECT':
                            
                            button_snap_abc = icons.get("icon_snap_abc") 
                            row.operator("tp_ops.np_020_point_align", text='ABC Point Align', icon_value=button_snap_abc.icon_id)

                    else:
                        pass
                else:                    
                    pass
                
                if context.mode == 'OBJECT':
                    
                    box.separator()  
                    
                    row = box.row(1)  

                    button_snap_grab = icons.get("icon_snap_grab") 
                    row.operator("tp_ops.np_020_point_move", text='G', icon_value=button_snap_grab.icon_id)
                   
                    button_snap_rotate = icons.get("icon_snap_rotate") 
                    row.operator("tp_ops.np_020_roto_move", text='R', icon_value=button_snap_rotate.icon_id)

                    button_snap_scale = icons.get("icon_snap_scale") 
                    row.operator("tp_ops.np_020_point_scale", text='S', icon_value=button_snap_scale.icon_id)

 
                    box.separator()  
                    


            Display_Mirror_Obm = context.user_preferences.addons[__package__].preferences.tab_batch_mirror_obm
            if Display_Mirror_Obm == 'on':

                box = layout.box().column(1) 
                          
                row = box.row(1)  

                button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
                row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
                         
                sub = row.row(1)
                sub.scale_x = 0.3                               
                sub.operator("tp_ops.mirror1",text="X")
                sub.operator("tp_ops.mirror2",text="Y")
                sub.operator("tp_ops.mirror3",text="Z")      

                box.separator()  



            Display_AutoMirror = context.user_preferences.addons[__package__].preferences.tab_batch_automirror
            if Display_AutoMirror == 'on':
  

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:


                        box = layout.box().column(1) 
                      
                        row = box.row(1)
                        row.operator("tp_ops.mod_mirror_x", "", icon ="MOD_MIRROR")

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
                        row.prop(context.scene, "AutoMirror_orientation", text="")                                     
                                 
                        row.prop(context.scene, "AutoMirror_axis", text="")            
                        
                        box.separator()                  
                     
                        row = box.row(1)

                        if tpw.display_mirror_auto:            
                            row.prop(tpw, "display_mirror_auto", text="Set", icon="PREFERENCES")
                        else:
                            row.prop(tpw, "display_mirror_auto", text="Set", icon="PREFERENCES") 
         
                        row.prop(context.scene, "AutoMirror_threshold", text="Threshold")      

                        box.separator() 

                        if tpw.display_mirror_auto:    
                                              
                            box = layout.box().column(1) 
                            row = box.row(1)
                            row.prop(context.scene, "AutoMirror_toggle_edit", text="Editmode")
                            row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
                            
                            row = box.row(1)
                            row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                            row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")            

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
                                    row.prop(mo, "use_mirror_merge", text="Merge")
                                    row.prop(mo, "use_clip", text="Clipping")

                                    box.separator() 
                        else:
                            pass


                        obj = context.active_object
                        if obj:
                            mod_list = obj.modifiers
                            if mod_list:
                               
                                box.separator()                            

                                row = box.row(1)    
                                
                                row.operator("tp_ops.remove_mod", text="", icon='X') 
                                row.operator("tp_ops.remove_mods_mirror", text="Remove") 
                                row.operator("tp_ops.apply_mod", text="", icon='FILE_TICK') 
                                row.operator("tp_ops.apply_mods_mirror", text="Apply") 

                                box.separator()                                                                      
                        else:
                            pass

                    else:
                        pass
                else:
                    pass
                




            Display_YLook_Tools = context.user_preferences.addons[__package__].preferences.tab_batch_ylook_tools
            if Display_YLook_Tools == 'on':

                box = layout.box().column(1) 
                          
                row = box.row(1)         
                row.label("Y-Look @") 
                
                sub = row.row(1)
                sub.scale_x = 0.3             
                
                button_look_at_obj = icons.get("icon_look_at_obj") 
                row.operator("lookat.it", text="", icon_value=button_look_at_obj.icon_id)

                button_look_at_cursor = icons.get("icon_look_at_cursor") 
                row.operator("lookat.cursor", text="", icon_value=button_look_at_cursor.icon_id)   

                box.separator()  



        if context.mode == 'EDIT_MESH':

            Display_Snap_to = context.user_preferences.addons[__package__].preferences.tab_batch_snap_to
            if Display_Snap_to == 'on':

                box = layout.box().column(1)  
               
                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on': 
                                   
                    row = box.row(1)         
                    row.label("Cursor to...")  

                row = box.row(1) 
                button_cursor_center = icons.get("icon_cursor_center")
                row.operator("view3d.snap_cursor_to_center", text=" ", icon_value=button_cursor_center.icon_id)

                button_cursor_object = icons.get("icon_cursor_object")
                row.operator("view3d.snap_cursor_to_selected", text=" ", icon_value=button_cursor_object.icon_id)

                button_cursor_active_obm = icons.get("icon_cursor_active_obm")
                row.operator("view3d.snap_cursor_to_active", text=" ", icon_value=button_cursor_active_obm.icon_id)

                button_cursor_grid = icons.get("icon_cursor_grid")
                row.operator("view3d.snap_cursor_to_grid", text=" ", icon_value=button_cursor_grid.icon_id)

                button_cursor_3point_center = icons.get("icon_cursor_3point_center")           
                row.operator("mesh.circlecentercursor", text=" ", icon_value=button_cursor_3point_center.icon_id)

                box.separator() 

                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':

                    row = box.row(1)                       
                    row.label("Selected to...")  

                row = box.row(1) 

                button_select_center = icons.get("icon_select_center")
                row.operator("tp_ops.zero_all_axis", text=" ", icon_value=button_select_center.icon_id)

                button_select_cursor = icons.get("icon_select_cursor")           
                row.operator("view3d.snap_selected_to_cursor", text=" ", icon_value=button_select_cursor.icon_id).use_offset=False

                button_select_active_obm = icons.get("icon_select_active_obm")
                row.operator("view3d.snap_selected_to_active", text=" ", icon_value=button_select_active_obm.icon_id)

                button_select_grid = icons.get("icon_select_grid")
                row.operator("view3d.snap_selected_to_grid", text=" ", icon_value=button_select_grid.icon_id)

                button_select_cursor_offset_obm = icons.get("icon_select_cursor_offset_obm")           
                row.operator("view3d.snap_selected_to_cursor", text=" ", icon_value=button_select_cursor_offset_obm.icon_id).use_offset=True

                box.separator() 



            Display_Origin_to = context.user_preferences.addons[__package__].preferences.tab_batch_origin_to
            if Display_Origin_to == 'on':

                box = layout.box().column(1)  
                
                Display_Title = context.user_preferences.addons[__package__].preferences.tab_batch_title
                if Display_Title == 'on':
                    
                    row = box.row(1)         
                    row.label("Origin to...")  

                row = box.row(1) 

                button_origin_center_view = icons.get("icon_origin_center_view")
                row.operator("tp_ops.origin_set_center", text=" ", icon_value=button_origin_center_view.icon_id)

                button_origin_cursor = icons.get("icon_origin_cursor")
                row.operator("tp_ops.origin_cursor_edm", text=" ", icon_value=button_origin_cursor.icon_id)            

                button_origin_edm = icons.get("icon_origin_edm")            
                row.operator("tp_ops.origin_edm"," ", icon_value=button_origin_edm.icon_id)       

                button_origin_obj = icons.get("icon_origin_obj")   
                row.operator("tp_ops.origin_obm"," ", icon_value=button_origin_obj.icon_id)             

                if lt.display_origin_bbox:                     
                    
                    button_origin_bbox = icons.get("icon_origin_bbox")            
                    row.prop(lt, "display_origin_bbox", text=" ", icon_value=button_origin_bbox.icon_id)                     
                else:               
                    button_origin_bbox = icons.get("icon_origin_bbox")                
                    row.prop(lt, "display_origin_bbox", text=" ", icon_value=button_origin_bbox.icon_id)

                box.separator()                                                     

                row = box.row(1)

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:

                        if lt.display_origin_bbox: 
                         
                             box = layout.box().row(1)

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

                             box = layout.box().row(1)

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
                             
                             box = layout.box().row(1)

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

                    
            draw_scale_align_tools(context, layout) 

            
            Display_Looptools_Edm = context.user_preferences.addons[__package__].preferences.tab_batch_looptools_edm
            if Display_Looptools_Edm == 'on':

                box = layout.box().column(1)              
                
                row = box.row(1)  
                # space - first line
                split = row.split(percentage=0.15, align=True)

                button_align_space = icons.get("icon_align_space") 
                if tp.display_space:
                    split.prop(tp, "display_space", text="", icon_value=button_align_space.icon_id)
                else:
                    split.prop(tp, "display_space", text="", icon_value=button_align_space.icon_id)
                
                split.operator("mesh.looptools_space", text="LoopTools Space", icon='BLANK1')

                # space - settings
                if tp.display_space:
                    box = layout.box().column(1)              
                    
                    row = box.column(1) 
                    row.prop(tp, "space_interpolation")
                    row.prop(tp, "space_input")

                    box.separator()

                    col_move = box.column(align=True)
                    row = col_move.row(align=True)
                    if tp.space_lock_x:
                        row.prop(tp, "space_lock_x", text = "X", icon='LOCKED')
                    else:
                        row.prop(tp, "space_lock_x", text = "X", icon='UNLOCKED')
                    if tp.space_lock_y:
                        row.prop(tp, "space_lock_y", text = "Y", icon='LOCKED')
                    else:
                        row.prop(tp, "space_lock_y", text = "Y", icon='UNLOCKED')
                    if tp.space_lock_z:
                        row.prop(tp, "space_lock_z", text = "Z", icon='LOCKED')
                    else:
                        row.prop(tp, "space_lock_z", text = "Z", icon='UNLOCKED')
                    col_move.prop(tp, "space_influence")

                    box.separator() 
                    box = layout.box().column(1)   


                row = box.row(1)  
                # curve - first line
                split = row.split(percentage=0.15, align=True)

                button_align_curve = icons.get("icon_align_curve") 
                if tp.display_curve:
                    split.prop(tp, "display_curve", text="", icon_value=button_align_curve.icon_id)
                else:
                    split.prop(tp, "display_curve", text="", icon_value=button_align_curve.icon_id)

                split.operator("mesh.looptools_curve", text="LoopTools Curve", icon='BLANK1')

                # curve - settings
                if tp.display_curve:
                    box = layout.box().column(1)              
                    
                    row = box.column(1) 
                    row.prop(tp, "curve_interpolation")
                    row.prop(tp, "curve_restriction")
                    row.prop(tp, "curve_boundaries")
                    row.prop(tp, "curve_regular")
                    
                    box.separator()

                    col_move = box.column(align=True)
                    row = col_move.row(align=True)
                    if tp.curve_lock_x:
                        row.prop(tp, "curve_lock_x", text = "X", icon='LOCKED')
                    else:
                        row.prop(tp, "curve_lock_x", text = "X", icon='UNLOCKED')
                    if tp.curve_lock_y:
                        row.prop(tp, "curve_lock_y", text = "Y", icon='LOCKED')
                    else:
                        row.prop(tp, "curve_lock_y", text = "Y", icon='UNLOCKED')
                    if tp.curve_lock_z:
                        row.prop(tp, "curve_lock_z", text = "Z", icon='LOCKED')
                    else:
                        row.prop(tp, "curve_lock_z", text = "Z", icon='UNLOCKED')
                    col_move.prop(tp, "curve_influence")

                    box.separator() 
                    box = layout.box().column(1)    


                row = box.row(1)  
                # circle - first line
                split = row.split(percentage=0.15, align=True)

                button_align_circle = icons.get("icon_align_circle") 
                if tp.display_circle:
                    split.prop(tp, "display_circle", text="", icon_value=button_align_circle.icon_id)
                else:
                    split.prop(tp, "display_circle", text="", icon_value=button_align_circle.icon_id)

                split.operator("mesh.looptools_circle", text="LoopTools Circle", icon='BLANK1')

                # circle - settings
                if tp.display_circle:
                    box = layout.box().column(1)              
                    
                    row = box.column(1) 
                    row.prop(tp, "circle_fit")
                    
                    row.separator()

                    row.prop(tp, "circle_flatten")
                    
                    row = box.row(align=True)
                    row.prop(tp, "circle_custom_radius")
                    
                    row_right = row.row(align=True)
                    row_right.active = tp.circle_custom_radius
                    row_right.prop(tp, "circle_radius", text="")                
                    box.prop(tp, "circle_regular")
                    
                    box.separator()

                    col_move = box.column(align=True)
                    row = col_move.row(align=True)
                    if tp.circle_lock_x:
                        row.prop(tp, "circle_lock_x", text = "X", icon='LOCKED')
                    else:
                        row.prop(tp, "circle_lock_x", text = "X", icon='UNLOCKED')
                    if tp.circle_lock_y:
                        row.prop(tp, "circle_lock_y", text = "Y", icon='LOCKED')
                    else:
                        row.prop(tp, "circle_lock_y", text = "Y", icon='UNLOCKED')
                    if tp.circle_lock_z:
                        row.prop(tp, "circle_lock_z", text = "Z", icon='LOCKED')
                    else:
                        row.prop(tp, "circle_lock_z", text = "Z", icon='UNLOCKED')
                    col_move.prop(tp, "circle_influence")

                    box.separator() 
                    box = layout.box().column(1)    
                    

                row = box.row(1) 
                # flatten - first line
                split = row.split(percentage=0.15, align=True)

                button_align_flatten = icons.get("icon_align_flatten") 
                if tp.display_flatten:
                    split.prop(tp, "display_flatten", text="", icon_value=button_align_flatten.icon_id)
                else:
                    split.prop(tp, "display_flatten", text="", icon_value=button_align_flatten.icon_id)

                split.operator("mesh.looptools_flatten", text="LoopTool Flatten", icon ="BLANK1")

                # flatten - settings
                if tp.display_flatten:
                    box = layout.box().column(1)    
                     
                    row = box.column(1)  
                    row.prop(tp, "flatten_plane")

                    box.separator()

                    col_move = box.column(align=True)
                    row = col_move.row(align=True)
                    if tp.flatten_lock_x:
                        row.prop(tp, "flatten_lock_x", text = "X", icon='LOCKED')
                    else:
                        row.prop(tp, "flatten_lock_x", text = "X", icon='UNLOCKED')
                    if tp.flatten_lock_y:
                        row.prop(tp, "flatten_lock_y", text = "Y", icon='LOCKED')
                    else:
                        row.prop(tp, "flatten_lock_y", text = "Y", icon='UNLOCKED')
                    if tp.flatten_lock_z:
                        row.prop(tp, "flatten_lock_z", text = "Z", icon='LOCKED')
                    else:
                        row.prop(tp, "flatten_lock_z", text = "Z", icon='UNLOCKED')
                    col_move.prop(tp, "flatten_influence")

                    box.separator() 

                box.separator()                 



            Display_Relax = context.user_preferences.addons[__package__].preferences.tab_batch_relax 
            if Display_Relax == 'on':

                box = layout.box().column(1)    

                row = box.column(1)                      
         
                button_align_vertices = icons.get("icon_align_vertices") 
                row.operator("mesh.vertices_smooth","Smooth Verts", icon_value=button_align_vertices.icon_id) 

                button_align_laplacian = icons.get("icon_align_laplacian")
                row.operator("mesh.vertices_smooth_laplacian","Smooth Laplacian", icon_value=button_align_laplacian.icon_id)  

                button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
                row.operator("mesh.shrinkwrap_smooth","Smooth Shrinkwrap ", icon_value=button_align_shrinkwrap.icon_id)         
                             
                box.separator()    

                row = box.row(1)                 
                             
                # relax - first line
                split = row.split(percentage=0.15, align=True)
                if tp.display_relax:
                    button_align_looptools = icons.get("icon_align_looptools")
                    split.prop(tp, "display_relax", text="", icon_value=button_align_looptools.icon_id)
                    split.operator("mesh.looptools_relax", text="  LoopTool Relax")

                else:
                    button_align_looptools = icons.get("icon_align_looptools")
                    split.prop(tp, "display_relax", text="", icon_value=button_align_looptools.icon_id)
                    split.operator("mesh.looptools_relax", text="  LoopTool Relax")

                # relax - settings
                if tp.display_relax:
                    box = layout.box().column(1)    
                     
                    row = box.column(1)  
                    row.prop(tp, "relax_interpolation")
                    row.prop(tp, "relax_input")
                    row.prop(tp, "relax_iterations")
                    row.prop(tp, "relax_regular")

                box.separator()    



            Display_Snap_to = context.user_preferences.addons[__package__].preferences.tab_batch_snap_to
            if Display_Snap_to == 'on':

                box = layout.box().column(1)              
                
                row = box.column(1) 

                button_snap_offset = icons.get("icon_snap_offset")  
                row.operator("view3d.xoffsets_main", "Offset & Rotate", icon_value=button_snap_offset.icon_id)   
                
                button_align_con_face = icons.get("icon_align_con_face") 
                row.operator("mesh.rot_con", "Rotate Face co-planar", icon_value=button_align_con_face.icon_id)   

                box.separator() 


            Display_Mirror_Edm = context.user_preferences.addons[__package__].preferences.tab_batch_mirror_edm
            if Display_Mirror_Edm == 'on':

                box = layout.box().column(1)   
                             
                row = box.row(1)             
                button_align_mirror_edm = icons.get("icon_align_mirror_edm")              
                row.label("Mirror", icon_value=button_align_mirror_edm.icon_id) 

                sub = row.row(1)
                sub.scale_x = 0.3    
                sub.operator("tp_ops.mirror1",text="X")
                sub.operator("tp_ops.mirror2",text="Y")
                sub.operator("tp_ops.mirror3",text="Z")      

                box.separator() 

                row = box.column(1)
                button_align_mirror_edge = icons.get("icon_align_mirror_edge")          
                row.operator("tp_ops.mirror_over_edge", "Mirror over Edge", icon_value=button_align_mirror_edge.icon_id)    

                box.separator() 



            Display_Edge_Align = context.user_preferences.addons[__package__].preferences.tab_batch_edge_align
            if Display_Edge_Align == 'on':

                
                box = layout.box().column(1)
                
                row = box.row(1) 
                row.operator("mesh.align_operator", text = 'Store Edge').type_op = 1
                align_op = row.operator("mesh.align_operator", text = 'Align Edges').type_op = 0

                box.separator()      
     
                row = box.row(1) 
                if tpw.display_align_help:
                    row.prop(tpw, "display_align_help", text="", icon='INFO')
                else:
                    row.prop(tpw, "display_align_help", text="", icon='INFO')

                row.prop(bpy.context.window_manager.paul_manager, 'align_dist_z', text = 'Superpose')
                row.prop(bpy.context.window_manager.paul_manager, 'align_lock_z', text = 'lock Z')

                if tpw.display_align_help:

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



            Display_AutoMirror = context.user_preferences.addons[__package__].preferences.tab_batch_automirror_edm
            if Display_AutoMirror == 'on':

                
                box = layout.box().column(1) 
              
                row = box.row(1)
                row.operator("tp_ops.mod_mirror_x", "", icon ="MOD_MIRROR")

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
                row.prop(context.scene, "AutoMirror_orientation", text="")                                     
                         
                row.prop(context.scene, "AutoMirror_axis", text="")            
                
                box.separator()                  
             
                row = box.row(1)

                if tpw.display_mirror_auto:            
                    row.prop(tpw, "display_mirror_auto", text="Set", icon="PREFERENCES")
                else:
                    row.prop(tpw, "display_mirror_auto", text="Set", icon="PREFERENCES") 
 
                row.prop(context.scene, "AutoMirror_threshold", text="Threshold")      

                box.separator() 

                if tpw.display_mirror_auto:    
                                      
                    box = layout.box().column(1) 
                    row = box.row(1)
                    row.prop(context.scene, "AutoMirror_toggle_edit", text="Editmode")
                    row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
                    
                    row = box.row(1)
                    row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                    row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")            

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
                            row.prop(mo, "use_mirror_merge", text="Merge")
                            row.prop(mo, "use_clip", text="Clipping")

                            box.separator() 
                else:
                    pass


                obj = context.active_object
                if obj:
                    mod_list = obj.modifiers
                    if mod_list:
                       
                        box.separator()                            

                        row = box.row(1)    
                        
                        row.operator("tp_ops.remove_mod", text="", icon='X') 
                        row.operator("tp_ops.remove_mods_mirror", text="Remove") 
                        row.operator("tp_ops.apply_mod", text="", icon='FILE_TICK') 
                        row.operator("tp_ops.apply_mods_mirror_edm", text="Apply") 

                        box.separator()                                                                      
                else:
                    pass


  

        if context.mode == 'EDIT_LATTICE':

            draw_cursor_origin_tools(context, layout)
            
            draw_scale_align_tools(context, layout) 


            box = layout.box().column(1)   

            row = box.row(1)  

            button_flip_lattice = icons.get("icon_flip_lattice")              
            row.label("Flip", icon_value=button_flip_lattice.icon_id) 
                     
            sub = row.row(1)
            sub.scale_x = 0.3 
            sub.operator("lattice.flip", text="X").axis = "U"
            sub.operator("lattice.flip", text="Y").axis = "V"
            sub.operator("lattice.flip", text="Z").axis = "W"

            box.separator()
          
            Display_Mirror_Lat = context.user_preferences.addons[__package__].preferences.tab_batch_mirror_lat
            if Display_Mirror_Lat == 'on':

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

            draw_cursor_origin_tools(context, layout)
            
            draw_scale_align_tools(context, layout)
                        

            Display_Mirror_Curve = context.user_preferences.addons[__package__].preferences.tab_batch_mirror_curve
            if Display_Mirror_Curve == 'on':

                box = layout.box().column(1)               
                
                row = box.row(1)   

                button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
                row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
                         
                sub = row.row(1)
                sub.scale_x = 0.3                   
                sub.operator("tp_ops.mirror1",text="X")
                sub.operator("tp_ops.mirror2",text="Y")
                sub.operator("tp_ops.mirror3",text="Z")            
       
                box.separator()


        if context.mode == 'EDIT_METABALL':    

            draw_cursor_origin_tools(context, layout)
            
            draw_scale_align_tools(context, layout)  


        if context.mode == 'EDIT_ARMATURE':    

            draw_cursor_origin_tools(context, layout)
            
            draw_scale_align_tools(context, layout)             



        Display_Shade = context.user_preferences.addons[__package__].preferences.tab_batch_shade
        if Display_Shade == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tpw.display_display:            
                row.prop(tpw, "display_display", text="", icon="WORLD")
            else:
                row.prop(tpw, "display_display", text="", icon="WORLD")
                
            row.label("Display")

            if tpw.display_display: 
            
                box.separator()
                
                row = box.row(1)                                                          
                row.operator("tp_ops.wire_all", text="Wire all", icon='WIRE')
                
                obj = context.active_object
                if obj:
                    active_wire = obj.show_wire 
                    if active_wire == True:
                        row.operator("tp_ops.wire_off", "Wire Select", icon = 'MESH_PLANE')              
                    else:                       
                        row.operator("tp_ops.wire_on", "Wire Select", icon = 'MESH_GRID')
                else:
                    row.label("", icon="BLANK1")            
               
                row = box.row(1)
                
                obj = context.active_object
                if obj:               
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text="Solid Shade", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="Wire Shade", icon='GHOST_ENABLED')        
                else:
                    row.label("", icon="BLANK1")  
 
                ob = context.object
                if ob: 
                    row.prop(ob, "draw_type", text="")
                    
                    row = box.row(1)
                    row.prop(ob, "show_bounds", text="ShowBounds", icon='STICKY_UVS_LOC') 
                    row.prop(ob, "draw_bounds_type", text="")    
               
                else:
                    row.label("", icon="BLANK1") 

                
                if context.mode == 'EDIT_MESH':          
                    
                    box.separator() 
                    
                    row = box.row(1)  
                    row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                    row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 
                    
                    row = box.row(1)  
                    row.operator("mesh.normals_make_consistent", text="Consistent Normals", icon="SNAP_NORMAL")  
                
                else:            
                    
                    box.separator() 
                    
                    if context.mode == 'OBJECT': 
                        
                        row = box.row(1)  
                        row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                        row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
                   
                    row = box.row(1)  
                    row.operator("tp_ops.rec_normals", text="Consistent Normals", icon="SNAP_NORMAL")  

                box.separator() 



        Display_History = context.user_preferences.addons[__package__].preferences.tab_batch_history_align
        if Display_History == 'on':

            box = layout.box().column(1)  
           
            row = box.row(1)
            row.scale_y = 0.85        

            button_ruler_triangle = icons.get("icon_ruler_triangle") 
            row.operator("tp_ops.np_020_point_distance", text="", icon_value=button_ruler_triangle.icon_id) 
              
            row.operator("view3d.ruler", text="Ruler")   
             
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
           
            box.separator()   
    
        

    def execute(self, context):
   
        return {'FINISHED'}

    def check(self, context):
        return True

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)





def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__) 


if __name__ == "__main__":
    register()

   