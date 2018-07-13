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


class VIEW3D_TP_Align_PIE(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_pie.align_pie_menu"

    @classmethod
    def poll(cls, context):
        return (context.scene)

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        icons = load_icons()

        pie = layout.menu_pie()

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        expand = panel_prefs.expand_panel_tools 


#B1
########### 1_Left ------------------------------------------------ 

        box = pie.split().box().column(1)


        if context.mode =="OBJECT":

            row = box.row(1)                      
            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("tp_ops.origin_set_center", text=" ", icon_value=button_origin_center_view.icon_id)

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_set_cursor", text=" ", icon_value=button_origin_cursor.icon_id)

            button_origin_mass = icons.get("icon_origin_mass")           
            row.operator("tp_ops.origin_set_mass", text=" ", icon_value=button_origin_mass.icon_id)   

            row = box.row(1)

            if len(bpy.context.selected_objects) == 1: 
              
                if context.mode == 'OBJECT':
                    button_origin_bbox = icons.get("icon_origin_bbox")                               
                    row.operator("tp_ops.bbox_origin_modal_ops", text=" ", icon_value=button_origin_bbox.icon_id)                                
            else:                            

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:

                        button_origin_bbox = icons.get("icon_origin_bbox")   
                        row.operator("tp_ops.bbox_origin_set"," ", icon_value=button_origin_bbox.icon_id)

                    else:
                        button_origin_bbox = icons.get("icon_origin_bbox")                               
                        row.operator("tp_ops.bbox_origin_modal_ops", text=" ", icon_value=button_origin_bbox.icon_id)                     


            button_origin_tomesh = icons.get("icon_origin_tomesh")
            row.operator("tp_ops.origin_tomesh", text=" ", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            row.operator("tp_ops.origin_meshto", text=" ", icon_value=button_origin_meshto.icon_id)


        else:


            row = box.row(1)
         


            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("tp_ops.origin_set_center", text=" ", icon_value=button_origin_center_view.icon_id)

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_cursor_edm", text=" ", icon_value=button_origin_cursor.icon_id)            
 
            row = box.row(1)

            button_origin_bbox = icons.get("icon_origin_bbox")   
            row.operator("tp_ops.bbox_origin_set"," ", icon_value=button_origin_bbox.icon_id)

            button_origin_obj = icons.get("icon_origin_obj")   
            row.operator("tp_ops.origin_obm"," ", icon_value=button_origin_obj.icon_id)              

            button_origin_edm = icons.get("icon_origin_edm")            
            row.operator("tp_ops.origin_edm"," ", icon_value=button_origin_edm.icon_id)       





#B2
########### 2_Right ------------------------------------------------       
    
        box = pie.split().box().column(1)        
        box.scale_x = 0.85     

        if not context.space_data.current_orientation:
            row = box.row(1)
            row.label("Transform Orientation")

        row = box.row(1)
        row.prop(context.space_data, "transform_orientation", text="", icon='MANIPUL')
        row.operator("transform.create_orientation", text="", icon='ZOOMIN')

        if context.space_data.current_orientation:
            
            row = box.row(1)
            row.prop(context.space_data.current_orientation, "name", text="")
            row.operator("transform.delete_orientation", text="", icon='X')



    
#B3
########### 3_Bottom ------------------------------------------------   

        box = pie.split().box().column(1)
        
        if context.mode =="OBJECT":
            box.scale_x = 0.9
                    
            row = box.row(1) 
            props = row.operator("tp_ops.align_transform",text="Rotate", icon='MAN_ROT') 
            props.tp_axis= 'axis_xyz'         
            props.tp_transform= 'ROTATION'     

            row.operator("object.rotation_clear", text="", icon="PANEL_CLOSE")       
           
            button_align_baply = icons.get("icon_align_baply") 
            props = row.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
            props.location= False
            props.rotation= True
            props.scale= False  

            box.separator()

            row = box.row(1)

            button_align_x = icons.get("icon_align_x") 
            props = row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id)
            props.tp_axis= 'axis_x'       
            props.tp_transform= 'ROTATION'       

            button_align_y = icons.get("icon_align_y")       
            props = row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id)             
            props.tp_axis= 'axis_y' 
            props.tp_transform= 'ROTATION' 

            button_align_z = icons.get("icon_align_z")     
            props = row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id)
            props.tp_axis= 'axis_z'         
            props.tp_transform= 'ROTATION'   
            
            row = box.row(1)

            button_align_xy = icons.get("icon_align_xy") 
            props = row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
            props.tp_axis= 'axis_xy'         
            props.tp_transform= 'ROTATION'    

            button_align_zx = icons.get("icon_align_zx")
            props = row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
            props.tp_axis= 'axis_zx'         
            props.tp_transform= 'ROTATION'    
            
            button_align_zy = icons.get("icon_align_zy") 
            props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
            props.tp_axis= 'axis_zy'         
            props.tp_transform= 'ROTATION'     

      
        


        else:
           
            if bpy.context.mode == "EDIT_MESH":
               
                row = box.row(1)
              
                button_align_straigten = icons.get("icon_align_straigten") 
                row.operator("mesh.vertex_align",text=" ", icon_value=button_align_straigten.icon_id) 

                button_align_distribute = icons.get("icon_align_distribute")  
                row.operator("mesh.vertex_distribute",text=" ", icon_value=button_align_distribute.icon_id)                                        
              
                button_align_unbevel = icons.get("icon_align_unbevel") 
                row.operator("tp_ops.unbevel", text=" ", icon_value=button_align_unbevel.icon_id)

                imdjs_tools_addon = "IMDJS_mesh_tools" 
                state = addon_utils.check(imdjs_tools_addon)
                if not state[0]:   
                  
                    button_align_radians = icons.get("icon_align_radians")  
                    row.operator("mesh.round_selected_points", text="Radians", icon_value=button_align_radians.icon_id)  
        
                row = box.row(1)        
                row.operator("mesh.wplsmthdef_apply", text="Deform", icon ="FRAME_NEXT")                
                
                button_lattice_add = icons.get("icon_lattice_add") 
                row.operator("tp_ops.easy_lattice", "E-Lattice", icon_value=button_lattice_add.icon_id)     

  
                Display_Looptools = context.user_preferences.addons[addon_key].preferences.tab_looptools
                if Display_Looptools == True:
                        
                    loop_tools_addon = "mesh_looptools" 
                    state = addon_utils.check(loop_tools_addon)
                    if not state[0]:                         
                        
                        row = box.row(1) 
                        row.operator("tp_ops.enable_looptools", text="!_Activate Looptools_!")    

                    else: 
                        
                        row = box.row(1)

                        button_align_space = icons.get("icon_align_space")
                        row.operator("mesh.looptools_space", text=" ", icon_value=button_align_space.icon_id)
                       
                        button_align_curve = icons.get("icon_align_curve") 
                        row.operator("mesh.looptools_curve", text=" ", icon_value=button_align_curve.icon_id)

                        button_align_circle = icons.get("icon_align_circle") 
                        row.operator("mesh.looptools_circle", text=" ", icon_value=button_align_circle.icon_id)

                        button_align_flatten = icons.get("icon_align_flatten")                
                        row.operator("mesh.looptools_flatten", text=" ", icon_value=button_align_flatten.icon_id)



                Display_Relax = context.user_preferences.addons[addon_key].preferences.tab_relax 
                if Display_Relax == True:
             
                    row = box.row(1)                                    
             
                    button_align_vertices = icons.get("icon_align_vertices") 
                    row.operator("mesh.vertices_smooth"," ", icon_value=button_align_vertices.icon_id) 

                    button_align_laplacian = icons.get("icon_align_laplacian")
                    row.operator("mesh.vertices_smooth_laplacian"," ", icon_value=button_align_laplacian.icon_id)  

                    button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
                    row.operator("mesh.shrinkwrap_smooth"," ", icon_value=button_align_shrinkwrap.icon_id)         


               
                Display_Looptools = context.user_preferences.addons[addon_key].preferences.tab_looptools
                if Display_Looptools == True:
                        
                    loop_tools_addon = "mesh_looptools" 
                    state = addon_utils.check(loop_tools_addon)
                    if not state[0]:
                        pass                         
                    else: 
                        
                        button_align_looptools = icons.get("icon_align_looptools")              
                        row.operator("mesh.looptools_relax", text=" ", icon_value=button_align_looptools.icon_id)

                        box.separator()                        
                        
                        row = box.row(1)          
                        row.operator("tp_ops.surface_pencil", text=" ",icon="GREASEPENCIL")    
                        sub = row.row(1)
                        sub.scale_x = 1
                        sub.operator("mesh.looptools_gstretch", text="Gstretch", icon='IPO_EASE_IN_OUT')    
                        row.operator("remove.gp", text=" ", icon="PANEL_CLOSE")    

            else:

                if context.mode =="EDIT_CURVE": 
                    box.scale_x = 0.9
                    
                    row = box.row(1) 
                    row.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
                    row.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'          
                    row.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'
                    
                    row = box.row(1)                      
                    row.operator("curve.switch_direction", text="Route")
                    row.operator("curve.cyclic_toggle", text="Cyclic")
                    row.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'  
             
                else:
                    pass
                


            
#B4
########### 4_Top ------------------------------------------------ 

        box = pie.split().box().column()         
        box.scale_x = 1 

        row = box.row(1)
        row.operator("tp_ops.pivot_bounding_box", " ", icon="ROTATE", emboss=False)
        row.operator("tp_ops.pivot_3d_cursor", " ", icon="CURSOR", emboss=False)
        
        button_snap_cursor = icons.get("icon_snap_cursor")           
        row.menu("VIEW3D_TP_SnapSet_Menu", text=" ", icon_value=button_snap_cursor.icon_id)    


        row = box.row(1)
        row.operator("tp_ops.pivot_active", " ", icon="ROTACTIVE", emboss=False)
        row.operator("tp_ops.pivot_individual", " ", icon="ROTATECOLLECTION", emboss=False)
        row.operator("tp_ops.pivot_median", " ", icon="ROTATECENTER", emboss=False)    





#B5                   
########### 5_Top_Left ------------------------------------------------        

        box = pie.split().box().column(1)
        box.scale_x = 0.95
                
        if context.mode =="OBJECT":

            row = box.row(1)
            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:      

                    row = box.row(1)  

                    button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                    row.operator("object.align_by_faces", text=" ", icon_value=button_snap_face_to_face.icon_id)  

                    button_snap_drop_down = icons.get("icon_snap_drop_down") 
                    row.operator("object.drop_on_active", text=" ", icon_value=button_snap_drop_down.icon_id) 

                    button_lattice_apply = icons.get("icon_lattice_apply") 
                    row.operator("tp_ops.lattice_apply", " ", icon_value=button_lattice_apply.icon_id)   
                    
                    row.operator("mesh.wplsmthdef_snap", text=" ", icon ="SHAPEKEY_DATA")

                    row = box.row(1)  

                    button_snap_offset = icons.get("icon_snap_offset")  
                    row.operator("view3d.xoffsets_main", " ", icon_value=button_snap_offset.icon_id)   

                    row.operator("tp_ops.xy_spread", text=" ", icon="AXIS_TOP")  
                                        
                else:
                    button_align_advance = icons.get("icon_align_advance")
                    row.operator("tp_origin.align_tools", " ", icon_value=button_align_advance.icon_id)  

            button_origin_distribute = icons.get("icon_origin_distribute")  
            row.operator("tp_ops.distribute_objects_menu", " ", icon_value=button_origin_distribute.icon_id)      

            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", " ", icon_value=button_align_zero.icon_id)   

        else:
            
            box.scale_x = 1.4   
            
           
            row = box.row(1)            
         
            if context.mode =="EDIT_MESH":

                button_align_planar = icons.get("icon_align_planar") 
                row.operator("mesh.face_make_planar", " ", icon_value=button_align_planar.icon_id)   
                        
                button_snap_offset = icons.get("icon_snap_offset")  
                row.operator("view3d.xoffsets_main", " ", icon_value=button_snap_offset.icon_id)  

                row = box.row(1)     
           
                button_align_con_face = icons.get("icon_align_con_face") 
                row.operator("mesh.rot_con", " ", icon_value=button_align_con_face.icon_id)    
       
            button_align_zero = icons.get("icon_align_zero")                
            row.operator("tp_ops.zero_axis", " ", icon_value=button_align_zero.icon_id)   





#B6
########### 6_Top_Right ------------------------------------------------  

        box = pie.split().box().column(1)
        box.scale_x = 0.95

        if context.mode =="OBJECT":

            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:

                    row = box.row(1)  
                   
                    button_snap_grab = icons.get("icon_snap_grab") 
                    row.operator("tp_ops.np_020_point_move", text='G', icon_value=button_snap_grab.icon_id)
                   
                    button_snap_rotate = icons.get("icon_snap_rotate") 
                    row.operator("tp_ops.np_020_roto_move", text='R', icon_value=button_snap_rotate.icon_id)

                    button_snap_scale = icons.get("icon_snap_scale") 
                    row.operator("tp_ops.np_020_point_scale", text='S', icon_value=button_snap_scale.icon_id)

                    button_snap_abc = icons.get("icon_snap_abc") 
                    row.operator("tp_ops.np_020_point_align", text='A', icon_value=button_snap_abc.icon_id)                                         


   


        if context.mode =="EDIT_MESH":  
            
            row = box.row(1)      
           
            button_align_mirror_edge = icons.get("icon_align_mirror_edge")          
            row.operator("tp_ops.mirror_over_edge", "Mirror over Edge", icon_value=button_align_mirror_edge.icon_id)    

        row = box.row(1)                               
        row.operator("tp_ops.mirror1",text="X", icon='ARROW_LEFTRIGHT')
        row.operator("tp_ops.mirror2",text="Y", icon='ARROW_LEFTRIGHT')
        row.operator("tp_ops.mirror3",text="Z", icon='ARROW_LEFTRIGHT')     

        button_align_advance = icons.get("icon_align_advance")
        row.operator("tp_origin.align_tools", " ", icon_value=button_align_advance.icon_id)   


    
#B7
########### 7_Bottom_Left ------------------------------------------------  
  
        box = pie.split().box().column(1)              
        box.scale_x = 0.9        
        
        if context.mode == "OBJECT":
          
            row = box.row(1)
            props = row.operator("tp_ops.align_transform",text="Scale", icon='MAN_SCALE')    
            props.tp_axis= 'axis_xyz'         
            props.tp_transform= 'SCALE'    

            row.operator("object.scale_clear", text="", icon="PANEL_CLOSE")        
            button_align_baply = icons.get("icon_align_baply") 
            props = row.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
            props.location= False
            props.rotation= False
            props.scale= True  

            box.separator()
                       
            row = box.row(1)

            button_align_x = icons.get("icon_align_x") 
            props = row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id)
            props.tp_axis= 'axis_x'       
            props.tp_transform= 'SCALE'       

            button_align_y = icons.get("icon_align_y")       
            props = row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id)             
            props.tp_axis= 'axis_y' 
            props.tp_transform= 'SCALE' 

            button_align_z = icons.get("icon_align_z")     
            props = row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id)
            props.tp_axis= 'axis_z'         
            props.tp_transform= 'SCALE'  

            row = box.row(1)

            button_align_xy = icons.get("icon_align_xy") 
            props = row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
            props.tp_axis= 'axis_xy'         
            props.tp_transform= 'SCALE'    

            button_align_zx = icons.get("icon_align_zx")
            props = row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
            props.tp_axis= 'axis_zx'         
            props.tp_transform= 'SCALE'    
                     
            button_align_zy = icons.get("icon_align_zy") 
            props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
            props.tp_axis= 'axis_zy'         
            props.tp_transform= 'SCALE'     

        

        if context.mode =="EDIT_MESH": 
            
            row = box.row(1) 
           
            row.operator("mesh.align_operator", text = 'Store Edge').type_op = 1
            align_op = row.operator("mesh.align_operator", text = 'Align Edges').type_op = 0

            row = box.row(1) 
            row.prop(bpy.context.window_manager.paul_manager, 'align_dist_z', text = 'dist Z')
            row.prop(bpy.context.window_manager.paul_manager, 'align_lock_z', text = 'lock Z')

        
        if context.mode =="EDIT_CURVE": 
            box.scale_x = 0.725      
                  
            row = box.row(1) 
            row.operator("curve.spline_type_set", text="CvType")
            row.operator("curve.normals_make_consistent", text="Recalc")
            row.operator("curve.smooth", text="Smooth")

            row = box.row(1)  
            row.operator("transform.transform", text="Shrink").mode = 'CURVE_SHRINKFATTEN'   
            row.operator("curve.radius_set", text="Radius")
            row.operator("transform.tilt", text="Tilt")      
 


#B8
########### 8_Bottom_Right_Objectmode ------------------------------------------------ 

        box = pie.split().box().column(1)
        box.scale_x = 0.9
       
        if context.mode =="OBJECT":
           
            row = box.row(1)
            props = row.operator("tp_ops.align_transform", text="Move", icon='MAN_TRANS')        
            props.tp_axis= 'axis_xyz'         
            props.tp_transform= 'LOCATION'   
 
            row.operator("object.location_clear", text="", icon="PANEL_CLOSE")
            button_align_baply = icons.get("icon_align_baply") 

            props = row.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
            props.location= True
            props.rotation= False
            props.scale= False

            box.separator()
            
            row = box.row(1)
            
            button_align_x = icons.get("icon_align_x") 
            props = row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id)
            props.tp_axis= 'axis_x'       
            props.tp_transform= 'LOCATION'       

            button_align_y = icons.get("icon_align_y")       
            props = row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id)             
            props.tp_axis= 'axis_y' 
            props.tp_transform= 'LOCATION' 

            button_align_z = icons.get("icon_align_z")     
            props = row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id)
            props.tp_axis= 'axis_z'         
            props.tp_transform= 'LOCATION'   
     
            row = box.row(1)

            button_align_xy = icons.get("icon_align_xy") 
            props = row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
            props.tp_axis= 'axis_xy'         
            props.tp_transform= 'LOCATION'    

            button_align_zx = icons.get("icon_align_zx")
            props = row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
            props.tp_axis= 'axis_zx'         
            props.tp_transform= 'LOCATION'    
            
            button_align_zy = icons.get("icon_align_zy") 
            props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
            props.tp_axis= 'axis_zy'         
            props.tp_transform= 'LOCATION'     


        else:

            row = box.row(1)

            button_align_x = icons.get("icon_align_x") 
            row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'

            button_align_y = icons.get("icon_align_y")
            row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'

            button_align_z = icons.get("icon_align_z")
            row.operator("tp_ops.align_transform",text="Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'   

            row = box.row(1)
            
            button_align_xy = icons.get("icon_align_xy") 
            row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'

            button_align_zy = icons.get("icon_align_zy") 
            row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'

            button_align_zx = icons.get("icon_align_zx")
            row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
                
if __name__ == "__main__":
    register()



