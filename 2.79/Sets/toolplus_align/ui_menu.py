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



class VIEW3D_TP_Snap_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Snap_Menu"
    bl_label = "SnapTools"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'


        if context.mode == 'EDIT_MESH': 
       
            button_align_to_normal = icons.get("icon_align_to_normal") 
            layout.operator("tp_ops.align_to_normal", "Normal Align", icon_value=button_align_to_normal.icon_id)    

            layout.separator() 

            button_align_con_face = icons.get("icon_align_con_face") 
            layout.operator("mesh.rot_con", "Square Rotate", icon_value=button_align_con_face.icon_id)   
            
            button_snap_offset = icons.get("icon_snap_offset")  
            layout.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   

        else:

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

            layout.separator() 


            button_origin_align = icons.get("icon_origin_align") 
            layout.operator("object.distribute_osc", text="Distribute", icon_value=button_origin_align.icon_id)                     

            button_align_advance = icons.get("icon_align_advance")
            layout.operator("tp_origin.align_tools", "Advance Align", icon_value=button_align_advance.icon_id)    




class VIEW3D_TP_Location_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Location_Menu"
    bl_label = "Location"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()

        col = split.column()

        col.operator("object.align_location_all", text="", icon='MAN_TRANS')        
        col.operator("object.location_clear", text="", icon="PANEL_CLOSE")


        button_align_baply = icons.get("icon_align_baply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
        props.location= True
        props.rotation= False
        props.scale= False

 
        col = split.column()
  
        button_align_xy = icons.get("icon_align_xy") 
        col.operator("tp_ops.align_transform_xy", "Xy", icon_value=button_align_xy.icon_id)

        button_align_zx = icons.get("icon_align_zx")
        col.operator("tp_ops.align_transform_zy", "Zx", icon_value=button_align_zx.icon_id)

        button_align_zy = icons.get("icon_align_zy") 
        col.operator("tp_ops.align_transform_zy", "Zy", icon_value=button_align_zy.icon_id)
 

        col = split.column()

        button_align_x = icons.get("icon_align_x") 
        col.operator("tp_ops.align_transform_x", "X", icon_value=button_align_x.icon_id)
       
        button_align_y = icons.get("icon_align_y") 
        col.operator("tp_ops.align_transform_y", "Y", icon_value=button_align_y.icon_id)       

        button_align_z = icons.get("icon_align_z") 
        col.operator("tp_ops.align_transform_z", "Z", icon_value=button_align_z.icon_id)
        
        




class VIEW3D_TP_Rotation_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Rotation_Menu"
    bl_label = "Rotation"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split(1)


        col = split.column(1)  

        col.operator("object.align_rotation_all",text="", icon='MAN_ROT') 
        col.operator("object.rotation_clear", text="", icon="PANEL_CLOSE")
        
        button_align_baply = icons.get("icon_align_baply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
        props.location= False
        props.rotation= True
        props.scale= False    


        col = split.column(1)   

        button_align_x = icons.get("icon_align_x") 
        col.operator("object.align_rotation_x",text="X", icon_value=button_align_x.icon_id)

        button_align_y = icons.get("icon_align_y") 
        col.operator("object.align_rotation_y",text="Y", icon_value=button_align_y.icon_id)

        button_align_z = icons.get("icon_align_z") 
        col.operator("object.align_rotation_z",text="Z", icon_value=button_align_z.icon_id)




      
class VIEW3D_TP_Scale_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Scale_Menu"
    bl_label = "Scale"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split(1)


        col = split.column(1)
        
        col.operator("object.align_objects_scale_all",text="", icon='MAN_SCALE')    
        col.operator("object.scale_clear", text="", icon="PANEL_CLOSE")        

        button_align_baply = icons.get("icon_align_baply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
        props.location= False
        props.rotation= False
        props.scale= True  


        col = split.column(1)

        button_align_x = icons.get("icon_align_x") 
        col.operator("object.align_objects_scale_x",text="X", icon_value=button_align_x.icon_id)

        button_align_y = icons.get("icon_align_y") 
        col.operator("object.align_objects_scale_y",text="Y", icon_value=button_align_y.icon_id)  
  
        button_align_z = icons.get("icon_align_z") 
        col.operator("object.align_objects_scale_z",text="Z", icon_value=button_align_z.icon_id)  
  




class VIEW3D_TP_Axis_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Axis_Menu"
    bl_label = "Axis"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()
            
        col = split.column(1)
        button_align_xy = icons.get("icon_align_xy") 
        col.operator("tp_ops.face_align_xy", "Xy", icon_value=button_align_xy.icon_id)

        button_align_zx = icons.get("icon_align_zx")
        col.operator("tp_ops.face_align_xz", "Zx", icon_value=button_align_zx.icon_id)

        button_align_zy = icons.get("icon_align_zy") 
        col.operator("tp_ops.face_align_yz", "Zy", icon_value=button_align_zy.icon_id)    
    
        col = split.column(1)            
        button_align_x = icons.get("icon_align_x") 
        col.operator("tp_ops.face_align_x", "X", icon_value=button_align_x.icon_id)

        button_align_y = icons.get("icon_align_y") 
        col.operator("tp_ops.face_align_y", "Y", icon_value=button_align_y.icon_id)           

        button_align_z = icons.get("icon_align_z") 
        col.operator("tp_ops.face_align_z", "Z", icon_value=button_align_z.icon_id)




class VIEW3D_TP_Mirror_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Mirror_Menu"
    bl_label = "Mirror"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()

        col = split.column(1)  
        props = col.operator("transform.mirror", text="X Global")
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'GLOBAL'
 
        props = col.operator("transform.mirror", text="Y Global")
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'GLOBAL'
  
        props = col.operator("transform.mirror", text="Z Global")
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'GLOBAL'


        if context.edit_object:
            
            col = split.column(1)  
            props = col.operator("transform.mirror", text="X Local")
            props.constraint_axis = (True, False, False)
            props.constraint_orientation = 'LOCAL'
         
            props = col.operator("transform.mirror", text="Y Local")
            props.constraint_axis = (False, True, False)
            props.constraint_orientation = 'LOCAL'
            
        
            props = col.operator("transform.mirror", text="Z Local")
            props.constraint_axis = (False, False, True)
            props.constraint_orientation = 'LOCAL'




class VIEW3D_TP_Pivot_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Pivot_Menu"
    bl_label = "Pivot"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("tp_ops.pivot_bounding_box", "BoundBox", icon="ROTATE")
        layout.operator("tp_ops.pivot_3d_cursor", "3D Cursor", icon="CURSOR")
        layout.operator("tp_ops.pivot_active", "Active", icon="ROTACTIVE")
        layout.operator("tp_ops.pivot_individual", "Individual", icon="ROTATECOLLECTION")
        layout.operator("tp_ops.pivot_median", "Median", icon="ROTATECENTER")    



class VIEW3D_TP_Station_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Station_Menu"
    bl_label = "NP STATION"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()

        col = split.column()
      
        button_snap_grab = icons.get("icon_snap_grab") 
        col.operator("tp_ops.np_020_point_move", text='Point Move', icon_value=button_snap_grab.icon_id)
       
        button_snap_rotate = icons.get("icon_snap_rotate") 
        col.operator("tp_ops.np_020_roto_move", text='Point Roto', icon_value=button_snap_rotate.icon_id)

        button_snap_scale = icons.get("icon_snap_scale") 
        col.operator("tp_ops.np_020_point_scale", text='Point Scale', icon_value=button_snap_scale.icon_id)


        obj = context.active_object
        if obj:
            obj_type = obj.type
            
            if obj.type in {'MESH'}:
                col.separator()
                
                button_snap_abc = icons.get("icon_snap_abc") 
                col.operator("tp_ops.np_020_point_align", text='Point ABC', icon_value=button_snap_abc.icon_id)

            else:
                pass
        else:
            pass

        col.separator()

        button_ruler_triangle = icons.get("icon_ruler_triangle") 
        col.operator("tp_ops.np_020_point_distance", text=" Point Distance", icon_value=button_ruler_triangle.icon_id)  





def draw_origin_menu_layout(self, context, layout):
          
        icons = load_icons()

        button_origin_center_view = icons.get("icon_origin_center_view")
        layout.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

        button_origin_cursor = icons.get("icon_origin_cursor")
        layout.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

        layout.separator()

        button_origin_edm = icons.get("icon_origin_edm")            
        layout.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

        button_origin_obj = icons.get("icon_origin_obj")   
        layout.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)            
             
        if context.mode == 'EDIT_MESH':
            
            layout.separator()

            button_origin_bbox = icons.get("icon_origin_bbox")   
            layout.operator("tp_ops.bbox_origin_set","BBox Origin", icon_value=button_origin_bbox.icon_id)




class VIEW3D_TP_Origin_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Origin_Menu"
    bl_label = "Origin"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        if context.mode == 'OBJECT':

            button_origin_center_view = icons.get("icon_origin_center_view")
            layout.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            layout.operator("tp_ops.origin_set_cursor", text="3D Cursor", icon_value=button_origin_cursor.icon_id)


            layout.separator()
                       

            button_origin_tomesh = icons.get("icon_origin_tomesh")
            layout.operator("tp_ops.origin_tomesh", text="Origin to Mesh", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            layout.operator("tp_ops.origin_meshto", text="Mesh to Origin", icon_value=button_origin_meshto.icon_id)


            layout.separator()


            button_origin_mass = icons.get("icon_origin_mass")           
            layout.operator("tp_ops.origin_set_mass", text="Center of Surface", icon_value=button_origin_mass.icon_id)

            button_origin_mass = icons.get("icon_origin_mass")           
            layout.operator("tp_ops.origin_set_volume", text="Center of Volume", icon_value=button_origin_mass.icon_id)


            layout.separator()


            if len(bpy.context.selected_objects) == 1: 
              
                if context.mode == 'OBJECT':
                    button_origin_bbox = icons.get("icon_origin_bbox")                               
                    layout.operator("object.bbox_origin_modal_ops", text="BBox Origin", icon_value=button_origin_bbox.icon_id)                                
            else:                            

                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:

                        button_origin_bbox = icons.get("icon_origin_bbox")   
                        layout.operator("tp_ops.bbox_origin_set","BBox Origin", icon_value=button_origin_bbox.icon_id)


        if context.mode == 'EDIT_MESH':
            draw_origin_menu_layout(self, context, layout)            
            
        if context.mode == 'EDIT_CURVE':            
            draw_origin_menu_layout(self, context, layout) 
       
        if context.mode == 'EDIT_SURFACE':
            draw_origin_menu_layout(self, context, layout) 

        if context.mode == 'EDIT_METABALL':            
            draw_origin_menu_layout(self, context, layout) 
   
        if context.mode == 'EDIT_LATTICE':            
            draw_origin_menu_layout(self, context, layout) 
                             
        if context.mode == 'PARTICLE':       
            draw_origin_menu_layout(self, context, layout) 

        if context.mode == 'EDIT_ARMATURE':
            draw_origin_menu_layout(self, context, layout) 
            
        if context.mode == 'POSE':
            draw_origin_menu_layout(self, context, layout) 



class VIEW3D_TP_SnapSet_Menu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_TP_SnapSet_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
        
        if context.mode == 'OBJECT':
            button_snap_place = icons.get("icon_snap_place")
            layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

        else:
            button_snap_retopo = icons.get("icon_snap_retopo")
            layout.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    

        layout.separator()

        button_snap_grid = icons.get("icon_snap_grid")
        layout.operator("tp_ops.grid", text="GridSnap", icon_value=button_snap_grid.icon_id)
                    
        button_snap_cursor = icons.get("icon_snap_cursor")           
        layout.operator("tp_ops.active_3d", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 
 
        layout.separator()  
 
        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_active.icon_id)

        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 






class VIEW3D_TP_Align_Menu_Graph(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_graph" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_x = icons.get("icon_align_x") 
        layout.operator("tp_ops.graph_align_x", text="X", icon_value=button_align_x.icon_id)
      
        button_align_y = icons.get("icon_align_y") 
        layout.operator("tp_ops.graph_align_y", text="Y", icon_value=button_align_y.icon_id)



class VIEW3D_TP_Align_Menu_UV(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_uv" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_x = icons.get("icon_align_x") 
        layout.operator("tp_ops.uv_align_x", text="X", icon_value=button_align_x.icon_id)
      
        button_align_y = icons.get("icon_align_y") 
        layout.operator("tp_ops.uv_align_y", text="Y", icon_value=button_align_y.icon_id)



class VIEW3D_TP_Align_Menu_Node(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_node" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_x = icons.get("icon_align_x") 
        layout.operator("tp_ops.node_align_x", text="X", icon_value=button_align_x.icon_id)
      
        button_align_y = icons.get("icon_align_y") 
        layout.operator("tp_ops.node_align_y", text="Y", icon_value=button_align_y.icon_id)




class VIEW3D_TP_Align_Menu_Sub(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main_sub" 

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.prop(scene, "regarding", expand=True)

#       layout.menu(align_submenu.bl_idname, text="Align by")





class VIEW3D_TP_Align_Menu_Space(bpy.types.Menu):
    bl_label = "Space"
    bl_idname = "VIEW3D_TP_Align_Menu_Space" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_straigten = icons.get("icon_align_straigten") 
        layout.operator("mesh.vertex_align",text="Straigten", icon_value=button_align_straigten.icon_id) 

        button_align_distribute = icons.get("icon_align_distribute")  
        layout.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_align_distribute.icon_id)                                        
   
        #imdjs_tools
        #button_align_radians = icons.get("icon_align_radians")  
        #row.operator("mesh.round_selected_points", text="Radians", icon_value=button_align_radians.icon_id)  


                

class VIEW3D_TP_Align_Menu_LoopTools(bpy.types.Menu):
    bl_label = "LoopTools"
    bl_idname = "VIEW3D_TP_Align_Menu_LoopTools" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'


        button_align_space = icons.get("icon_align_space")
        layout.operator("mesh.looptools_space", text="LpT  Space", icon_value=button_align_space.icon_id)
       
        button_align_curve = icons.get("icon_align_curve") 
        layout.operator("mesh.looptools_curve", text="LpT  Curve", icon_value=button_align_curve.icon_id)

        button_align_circle = icons.get("icon_align_circle") 
        layout.operator("mesh.looptools_circle", text="LpT  Circle", icon_value=button_align_circle.icon_id)

        button_align_flatten = icons.get("icon_align_flatten")                
        layout.operator("mesh.looptools_flatten", text="LpT  Circle", icon_value=button_align_flatten.icon_id)
 



class VIEW3D_TP_Align_Menu_Relax(bpy.types.Menu):
    bl_label = "Smooth Relax"
    bl_idname = "VIEW3D_TP_Align_Menu_Relax" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_vertices = icons.get("icon_align_vertices") 
        layout.operator("mesh.vertices_smooth","Smooth Verts", icon_value=button_align_vertices.icon_id) 

        button_align_laplacian = icons.get("icon_align_laplacian")
        layout.operator("mesh.vertices_smooth_laplacian","Smooth Laplacian", icon_value=button_align_laplacian.icon_id)  

        button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
        layout.operator("mesh.shrinkwrap_smooth","Smooth Shrinkwrap", icon_value=button_align_shrinkwrap.icon_id)         
        
               
        Display_Looptools = context.user_preferences.addons[__package__].preferences.tab_looptools
        if Display_Looptools == 'on':
                
            loop_tools_addon = "mesh_looptools" 
            state = addon_utils.check(loop_tools_addon)
            if not state[0]:
                pass                         
            else: 
                button_align_looptools = icons.get("icon_align_looptools")              
                layout.operator("mesh.looptools_relax", text="LT Smooth Relax", icon_value=button_align_looptools.icon_id)





class VIEW3D_TP_Align_Menu_Gstretch(bpy.types.Menu):
    bl_label = "Gstretch"
    bl_idname = "VIEW3D_TP_Align_Menu_Gstretch" 

    def draw(self, context):
        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("tp_ops.surface_pencil", text="Draw",icon="GREASEPENCIL")    
        layout.operator("mesh.looptools_gstretch", text="Gstretch", icon='IPO_EASE_IN_OUT')    
        layout.operator("remove.gp", text="Remove", icon="PANEL_CLOSE")    






class VIEW3D_TP_Align_Menu(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main"   
       
    def draw(self, context):
        layout = self.layout

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'        

        layout.menu("VIEW3D_TP_Pivot_Menu", text="Pivot", icon="CURSOR")  

        button_snap_cursor = icons.get("icon_snap_cursor")           
        layout.menu("VIEW3D_TP_SnapSet_Menu", text="SnapSet", icon_value=button_snap_cursor.icon_id)  

        layout.separator()   
          
        layout.menu("VIEW3D_TP_Origin_Menu", text="Origin", icon="LAYER_ACTIVE")   

  
        layout.separator()

        if context.mode == 'OBJECT':
         
            layout.menu("VIEW3D_TP_Location_Menu", text="Move", icon ="MAN_TRANS")   
            layout.menu("VIEW3D_TP_Rotation_Menu", text="Rotate", icon ="MAN_ROT")  
            layout.menu("VIEW3D_TP_Scale_Menu", text="Scale", icon ="MAN_SCALE")  

        else:
 
#            button_select_link = icons.get("icon_select_link") 
#            layout.operator("mesh.faces_select_linked_flat", text="Linked Flat", icon_value=button_select_link.icon_id) 

#            layout.separator() 
 
            layout.menu("VIEW3D_TP_Axis_Menu", text="To Axis", icon ="MANIPUL")   

       
        layout.separator()

        button_origin_align = icons.get("icon_origin_align") 
        layout.menu("VIEW3D_TP_Snap_Menu", text="Tools", icon_value=button_origin_align.icon_id)      


        if context.mode == 'OBJECT':

            button_snap_grab = icons.get("icon_snap_grab") 
            layout.menu("VIEW3D_TP_Station_Menu", text="NPoint", icon_value=button_snap_grab.icon_id)  

           
            obj = context.active_object     
            if obj:
               obj_type = obj.type
                              
               if obj_type in {'MESH'}:           
           
                    layout.separator()
                      
                    layout.operator("mesh.wplsmthdef_snap", text="Save M-State", icon ="SHAPEKEY_DATA")



        if context.mode == 'EDIT_MESH':
       
            layout.separator()

            layout.operator("mesh.wplsmthdef_apply", text="Apply S-Deform", icon ="FRAME_NEXT")

            layout.separator()

           
            button_align_straigten = icons.get("icon_align_straigten") 
            layout.menu("VIEW3D_TP_Align_Menu_Space", text="Space", icon_value=button_align_straigten.icon_id)   

           
            Display_Looptools = context.user_preferences.addons[__package__].preferences.tab_looptools
            if Display_Looptools == 'on':
            
                loop_tools_addon = "mesh_looptools" 
                state = addon_utils.check(loop_tools_addon)
                if not state[0]:                                         
                    layout.operator("tp_ops.enable_looptools", text="!_Activate Looptools_!", icon='BLANK1')                 
                else:             
                    layout.menu("VIEW3D_TP_Align_Menu_Gstretch", text="GStretch", icon="GREASEPENCIL")   
              
                    layout.separator()

                    button_align_circle = icons.get("icon_align_circle")           
                    layout.menu("VIEW3D_TP_Align_Menu_LoopTools", text="LoopTools", icon_value=button_align_circle.icon_id)   



            Display_Relax = context.user_preferences.addons[__package__].preferences.tab_relax 
            if Display_Relax == 'on':

                button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
                layout.menu("VIEW3D_TP_Align_Menu_Relax", text="Smooth Relax", icon_value=button_align_shrinkwrap.icon_id)   



        layout.separator()

        button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
        layout.menu("VIEW3D_TP_Mirror_Menu", text="Mirror", icon_value=button_align_mirror_obm.icon_id)   

        layout.separator()
       
        button_align_zero = icons.get("icon_align_zero")                
        layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)      
