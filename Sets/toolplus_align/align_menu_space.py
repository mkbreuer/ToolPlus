__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


class VIEW3D_TP_Space_Menu(bpy.types.Menu):
    bl_label = "T+ Align"
    bl_idname = "tp_menu.align_main"   

    #@classmethod
    #def poll(cls, context):
        #return (bpy.context.mode == 'EDIT')        

    def draw(self, context):
        layout = self.layout

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'        
        
        if context.mode == 'OBJECT':

            button_align_x = icons.get("icon_align_x") 
            layout.operator("tp_ops.align_transform_x", "X", icon_value=button_align_x.icon_id)

            button_align_y = icons.get("icon_align_y") 
            layout.operator("tp_ops.align_transform_y", "Y", icon_value=button_align_y.icon_id)           

            button_align_z = icons.get("icon_align_z") 
            layout.operator("tp_ops.align_transform_z", "Z", icon_value=button_align_z.icon_id)

            layout.separator()

            button_align_xy = icons.get("icon_align_xy") 
            layout.operator("tp_ops.align_transform_xy", "Xy", icon_value=button_align_xy.icon_id)

            button_align_zx = icons.get("icon_align_zx")
            layout.operator("tp_ops.align_transform_zy", "Zx", icon_value=button_align_zx.icon_id)

            button_align_zy = icons.get("icon_align_zy") 
            layout.operator("tp_ops.align_transform_zy", "Zy", icon_value=button_align_zy.icon_id)         

            layout.separator()

            layout.operator("object.align_location_all", text="all Location", icon='MAN_TRANS')
            layout.operator("object.align_rotation_all",text="all Rotation", icon='MAN_ROT') 
            layout.operator("object.align_objects_scale_all",text="all Scale", icon='MAN_SCALE')  


            display_menu_advance = context.user_preferences.addons[__package__].preferences.tab_menu_advance
            if display_menu_advance == 'on':

                layout.separator()

                button_origin_align = icons.get("icon_origin_align") 
                layout.operator("object.distribute_osc", text="Distribute", icon_value=button_origin_align.icon_id)   

                button_align_advance = icons.get("icon_align_advance")
                layout.operator("tp_origin.align_tools", "Advance", icon_value=button_align_advance.icon_id)    

                button_align_zero = icons.get("icon_align_zero")                
                layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)  


            display_menu_snap = context.user_preferences.addons[__package__].preferences.tab_menu_snap
            if display_menu_snap == 'on':

                layout.separator()

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:
                   

                        button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                        layout.operator("object.align_by_faces", text="Face to Face", icon_value=button_snap_face_to_face.icon_id)  

                        button_snap_drop_down = icons.get("icon_snap_drop_down") 
                        layout.operator("object.drop_on_active", text="Drop on Active", icon_value=button_snap_drop_down.icon_id) 

                        button_snap_offset = icons.get("icon_snap_offset")  
                        layout.operator("view3d.xoffsets_main", "Offset & Rotate", icon_value=button_snap_offset.icon_id)   

                    else:
                        pass
                else:
                    pass


            display_menu_np = context.user_preferences.addons[__package__].preferences.tab_menu_np
            if display_menu_np == 'on':

                if context.mode == 'OBJECT':

                    obj = context.active_object
                    if obj:
                        obj_type = obj.type
                        
                        if obj.type in {'MESH'}:
                            
                            button_snap_abc = icons.get("icon_snap_abc") 
                            layout.operator("tp_ops.np_020_point_align", text='ABC Point Align', icon_value=button_snap_abc.icon_id)

                        else:
                            pass
                    else:
                        pass

                    layout.separator()
                  
                    button_snap_grab = icons.get("icon_snap_grab") 
                    layout.operator("tp_ops.np_020_point_move", text='Point Move (G)', icon_value=button_snap_grab.icon_id)
                   
                    button_snap_rotate = icons.get("icon_snap_rotate") 
                    layout.operator("tp_ops.np_020_roto_move", text='Roto Move (R)', icon_value=button_snap_rotate.icon_id)

                    button_snap_scale = icons.get("icon_snap_scale") 
                    layout.operator("tp_ops.np_020_point_scale", text='Point Scale (S)', icon_value=button_snap_scale.icon_id)


        else:     
            
            display_menu_flat = context.user_preferences.addons[__package__].preferences.tab_menu_flat
            if display_menu_flat == 'on':

                if context.mode == 'EDIT_MESH':              
                    
                    button_select_link = icons.get("icon_select_link") 
                    layout.operator("mesh.faces_select_linked_flat", text="Linked Flat", icon_value=button_select_link.icon_id) 

                    layout.separator()
            
            button_align_x = icons.get("icon_align_x") 
            layout.operator("tp_ops.face_align_x", "X", icon_value=button_align_x.icon_id)

            button_align_y = icons.get("icon_align_y") 
            layout.operator("tp_ops.face_align_y", "Y", icon_value=button_align_y.icon_id)           

            button_align_z = icons.get("icon_align_z") 
            layout.operator("tp_ops.face_align_z", "Z", icon_value=button_align_z.icon_id)

            layout.separator()

            button_align_xy = icons.get("icon_align_xy") 
            layout.operator("tp_ops.face_align_xy", "Xy", icon_value=button_align_xy.icon_id)

            button_align_zx = icons.get("icon_align_zx")
            layout.operator("tp_ops.face_align_xz", "Zx", icon_value=button_align_zx.icon_id)

            button_align_zy = icons.get("icon_align_zy") 
            layout.operator("tp_ops.face_align_yz", "Zy", icon_value=button_align_zy.icon_id)           
            
            
            display_menu_advance = context.user_preferences.addons[__package__].preferences.tab_menu_advance
            if display_menu_advance == 'on':

                layout.separator()    

                button_align_zero = icons.get("icon_align_zero")                
                layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)  

             
            if context.mode == 'EDIT_MESH': 

                display_menu_align_face = context.user_preferences.addons[__package__].preferences.tab_menu_align_face
                if display_menu_align_face == 'on':

                    layout.separator()          
                                              
                    button_align_to_normal = icons.get("icon_align_to_normal") 
                    layout.operator("tp_ops.align_to_normal", "Align to Normal", icon_value=button_align_to_normal.icon_id)    

                    button_align_planar = icons.get("icon_align_planar") 
                    layout.operator("mesh.face_make_planar", "Make Planar Faces", icon_value=button_align_planar.icon_id)     


                display_menu_align_loop = context.user_preferences.addons[__package__].preferences.tab_menu_align_loop
                if display_menu_align_loop == 'on':

                    layout.separator() 

                    button_align_straigten = icons.get("icon_align_straigten") 
                    layout.operator("mesh.vertex_align",text="Straighten", icon_value=button_align_straigten.icon_id) 

                    button_align_distribute = icons.get("icon_align_distribute")  
                    layout.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_align_distribute.icon_id)                                        

                    #imdjs_tools
                    #button_align_radians = icons.get("icon_align_radians")  
                    #layout.operator("mesh.round_selected_points", text="Radians", icon_value=button_align_radians.icon_id)  


                display_menu_lpt = context.user_preferences.addons[__package__].preferences.tab_menu_lpt
                if display_menu_lpt == 'on':

                    layout.separator() 

                    button_align_space = icons.get("icon_align_space")         
                    layout.operator("mesh.looptools_space", text="LoopTools Space", icon_value=button_align_space.icon_id)

                    button_align_curve = icons.get("icon_align_curve")
                    layout.operator("mesh.looptools_curve", text="LoopTools Curve", icon_value=button_align_curve.icon_id)

                    button_align_circle = icons.get("icon_align_circle") 
                    layout.operator("mesh.looptools_circle", text="LoopTools Circle", icon_value=button_align_circle.icon_id)

                    button_align_flatten = icons.get("icon_align_flatten") 
                    layout.operator("mesh.looptools_flatten", text="LoopTool Flatten", icon_value=button_align_flatten.icon_id)


                display_menu_offset = context.user_preferences.addons[__package__].preferences.tab_menu_offset
                if display_menu_offset == 'on':

                    layout.separator() 

                    button_align_con_face = icons.get("icon_align_con_face") 
                    layout.operator("mesh.rot_con", "Rotate Face co-planar", icon_value=button_align_con_face.icon_id)   
                    
                    button_snap_offset = icons.get("icon_snap_offset")  
                    layout.operator("view3d.xoffsets_main", "Offset & Rotate", icon_value=button_snap_offset.icon_id)   



        display_menu_ruler = context.user_preferences.addons[__package__].preferences.tab_menu_ruler
        if display_menu_ruler == 'on': 
            
            layout.separator()   
     
            button_ruler_triangle = icons.get("icon_ruler_triangle") 
            layout.operator("tp_ops.np_020_point_distance", text=" Point Distance", icon_value=button_ruler_triangle.icon_id)  
