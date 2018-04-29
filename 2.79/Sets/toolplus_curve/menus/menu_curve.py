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


import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons


class VIEW3D_TP_Spline_Info_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_spline_info"
    bl_label = "Info"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.scale_y = 1.2

        layout.operator("curve.bezier_length","Lenght")   
        
        layout.separator()                 
      
        layout.operator("curvetools2.operatorcurveinfo", text = "Curve")                        
        layout.operator("curvetools2.operatorsplinesinfo", text = "Splines")
        layout.operator("curvetools2.operatorsegmentsinfo", text = "Segments")



class VIEW3D_TP_Curve_Bevel_Objects_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_bevel_objects"
    bl_label = "Bvl-Objects"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.scale_y = 1.2
        
        layout.operator("curve.bevelcurve", "Bevel Object")             
        layout.operator("curve.tapercurve", "Taper Object")         

        layout.separator()  

        layout.operator("tp_ops.curves_galore", "Multi Bevel")             



class VIEW3D_TP_Curve_MAterial_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_material"
    bl_label = "Material"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.scale_y = 1.2
                                                                                                                                 
        layout.operator("tp_ops.material_new","MAT-New")                                                                                  
        layout.menu("tp_ops.material_list", text="MAT-List")  



class VIEW3D_TP_Select_Edit_Curve(bpy.types.Menu):
    bl_idname = "tp_menu.curve_edit_select"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout
        
        layout.scale_y = 1.2
       
        if context.mode == "EDIT_CURVE":

            layout.operator("view3d.select_border")
            layout.operator("view3d.select_circle")

            layout.separator()

            layout.operator("curve.select_all").action = 'TOGGLE'
            layout.operator("curve.select_all", text="Inverse").action = 'INVERT'
            layout.operator("curve.select_random")
            layout.operator("curve.select_nth")
            layout.operator("curve.select_linked", text="Select Linked")
            layout.operator("curve.select_similar", text="Select Similar")

            layout.separator()

            layout.operator("curve.de_select_first")
            layout.operator("curve.de_select_last")
            layout.operator("curve.select_next")
            layout.operator("curve.select_previous")

            layout.separator()

            layout.operator("curve.select_more")
            layout.operator("curve.select_less")

        else:

            layout.operator("view3d.select_border")
            layout.operator("view3d.select_circle")

            layout.separator()

            layout.operator("curve.select_all").action = 'TOGGLE'
            layout.operator("curve.select_all", text="Inverse").action = 'INVERT'
            layout.operator("curve.select_random")
            layout.operator("curve.select_nth")
            layout.operator("curve.select_linked", text="Select Linked")
            layout.operator("curve.select_similar", text="Select Similar")

            layout.separator()

            layout.operator("curve.select_row")

            layout.separator()

            layout.operator("curve.select_more")
            layout.operator("curve.select_less")



class VIEW3D_TP_Curve_Subdivide(bpy.types.Menu):
    bl_label = "Subdivide"
    bl_idname = "tp_menu.curve_subdiv"
    
    def draw(self, context):
        layout = self.layout

        split = layout.split()

        col = split.column()
        col.scale_y = 1.2        
              
        col.operator("curve.bezier_subdivide","3xParam")   
       
        col.separator()
       
        col.operator("curve.subdivide", text="1").number_cuts=1        
        col.operator("curve.subdivide", text="2").number_cuts=2
        col.operator("curve.subdivide", text="3").number_cuts=3

        col = split.column()
        col.scale_y = 1.2

        col.label("")            
       
        col.separator()
        
        col.operator("curve.subdivide", text="4").number_cuts=4
        col.operator("curve.subdivide", text="5").number_cuts=5        
        col.operator("curve.subdivide", text="6 ").number_cuts=6 




class VIEW3D_TP_Spline_Type_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_spline_type"
    bl_label = "Splines"

    def draw(self, context):
        layout = self.layout.column()
        layout.operator_context = 'INVOKE_REGION_WIN'
 
        split = layout.split()       
       
        if context.mode == 'EDIT_CURVE':
           
            col = split.column()
            col.scale_y = 1.2     
            col.operator("curve.spline_type_set", "Poly").type = 'POLY'     
            col.operator("curve.spline_type_set", "Nurbs").type = 'NURBS'             
            
            col = split.column()
            col.scale_y = 1.2                      
            col.operator("curve.spline_type_set", "Bezier").type = 'BEZIER'         

        else:
            
            col = split.column()
            col.scale_y = 1.2                           
            col.operator("curve.to_poly","Poly")
            col.operator("curve.to_nurbs","Nurbs")

            col = split.column()
            col.scale_y = 1.2  
            col.operator("curve.to_bezier","Bezièr")




class VIEW3D_TP_Curve_Options_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_options"
    bl_label = "Options"

    def draw(self, context):
        layout = self.layout.column()
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        obj = context.object                
        act_spline = context.object.data.splines.active        
  
        split = layout.split()

        col = split.column()
        col.scale_y = 1.2

        col.operator("dynamic.normalize", text="Overlay (ESC)", icon='KEYTYPE_BREAKDOWN_VEC') 
        
        col.separator() 

        col.prop(obj, "show_name", text="Name")
        col.prop(obj, "show_axis", text="Axis")               
        col.prop(obj, "show_wire", text="Wire")
        col.prop(obj, "show_all_edges", text="Edges")


        if context.mode == "EDIT_CURVE":
            col.separator() 
                
            col.prop(context.active_object.data, "show_handles", text="Handles")
            col.prop(context.active_object.data, "show_normal_face", text="Normals:")        
  
  
        col = split.column()
        col.scale_y = 1.2
        
        col.label(" ")
       
        col.separator() 
        
        col.prop(obj, "show_x_ray", text="X-Ray")
        col.prop(obj, "show_bounds", text="Bounds")
        col.prop(act_spline, "use_smooth")
        col.prop(act_spline, "use_cyclic_u", text="Cyclic")
        
        if context.mode == "EDIT_CURVE":
            col.separator() 

            col.operator("curve.switch_direction", text="Direction", icon="ANIM")                                                         
            col.prop(context.scene.tool_settings, "normal_size", text="") 




class VIEW3D_TP_Handle_Type_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_handle_type"
    bl_label = "Handles"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()

        if context.mode == 'EDIT_CURVE':

            col = split.column(1)
            col.scale_y = 1.2               
            col.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
            col.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'
            
            col = split.column(1)
            col.scale_y = 1.2                           
            col.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'  
            col.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'

        else:
            col = split.column(1)
            col.scale_y = 1.2              
            col.operator("curve.handle_to_automatic","Auto")                                                  
            col.operator("curve.handle_to_free","Free") 

            col = split.column(1)
            col.scale_y = 1.2  
            col.operator("curve.handle_to_vector","Vector") 
            col.operator("curve.handle_to_aligned","Align")




class VIEW3D_TP_Curve_Transform_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_transform"
    bl_label = "Transform"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.scale_y = 1.2
        
        split = layout.split()

        if context.mode == 'EDIT_CURVE':

            col = split.column()
            col.scale_y = 1.2
   
            col.operator("transform.tilt")  
            col.operator("transform.tosphere", text="To Sphere")
            col.operator("transform.shear", text="Shear")
            col.operator("transform.bend", text="Bend")
            col.operator("transform.push_pull", text="Push/Pull")    
         
                    
            col.separator()  

            col.operator("curve.smooth_weight") 
            col.operator("curve.smooth_radius")            
           
           
            col = split.column()           
            col.scale_y = 1.2            
            
            col.operator("curve.tilt_clear")    
            col.operator("curve.radius_set", "Radius")         
            col.operator("transform.vertex_random", text="Randomize")   
            col.operator("curve.spline_weight_set", "Weight")   
            col.operator("transform.vertex_warp", text="Warp")  
           
            col.separator()  

            col.operator("curve.smooth_tilt") 
            #col.label("") 


        if context.mode == 'OBJECT':


            layout.operator_menu_enum("object.origin_set", "type", text="Set Origin")
            layout.operator("object.align")          
           
            layout.separator()             
           
            layout.operator("transform.tosphere", text="To Sphere")
            layout.operator("transform.shear", text="Shear")
            layout.operator("transform.bend", text="Bend")
            layout.operator("transform.push_pull", text="Push/Pull")                    
           
            layout.separator()               
            
            layout.operator_context = 'EXEC_REGION_WIN'
            layout.operator("transform.transform", text="Orientation").mode = 'ALIGN'
            layout.operator("object.randomize_transform")
          
            layout.separator()               
           
            layout.operator("transform.translate", text="Move Texture Space").texture_space = True               
            layout.operator("transform.resize", text="Scale Texture Space").texture_space = True           

            




class VIEW3D_TP_Curve_Editing_Menu(bpy.types.Menu):
    bl_idname = "tp_menu.curve_editing"
    bl_label = "Editing"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        vertex = []
        selected = []
 
        split = layout.split()
        
        if context.mode == 'EDIT_CURVE':

            col = split.column()
            col.scale_y = 1.2
            
            col.operator("curve.surfsk_first_points", text="SetFirst")             
               
            col.separator()  

            col.operator("curve.extrude_move", text="Extrude")                                 
            col.operator("transform.vertex_random") 
            col.operator("object.curve_outline", text = "Outline")       
            col.operator("curve.trim_tool", text="Trim")   
            col.operator("curve.spline_weight_set", text="Weight")           
           
            n = 0
            obj = context.active_object
            if obj != None:
                 if obj.type == 'CURVE':
                     for i in obj.data.splines:
                         for j in i.bezier_points:
                             n += 1
                             if j.select_control_point:
                                 selected.append(n)
                                 vertex.append(obj.matrix_world * j.co)

                 if len(vertex) > 0 and n > 2:
                     simple_edit = col.operator("curve.bezier_points_fillet", text='Fillet')  
  
                 if len(vertex) == 2:
                     col.separator()   

                 if len(vertex) == 1:
                     col.separator()   
  


            col = split.column()
            col.scale_y = 1.2
           
            col.operator("tp_ops.origin_first", text= "Origin First") 
                         
            col.separator() 
            col.operator("curve.make_segment",  text="Weld")                                
            col.operator("curve.smooth_x_times", text="Smooth")  
            col.operator("curve.separate",  text="Separate")             
            col.operator("curve.split",  text="Split")    
            col.operator("tp_ops.curve_copies", text = "Copy")                                      

            n = 0
            obj = context.active_object
            if obj != None:
                 if obj.type == 'CURVE':
                     for i in obj.data.splines:
                         for j in i.bezier_points:
                             n += 1
                             if j.select_control_point:
                                 selected.append(n)
                                 vertex.append(obj.matrix_world * j.co)

                 if len(vertex) > 0 and n > 2:
                     col.operator("curve.extend_tool", text="Extend")

               
                 if len(vertex) == 2:
                     col.separator() 
                     simple_edit = layout.operator("tp_ops.quader_curve","Beveled Quarter")   

                 if len(vertex) == 1:
                     col.separator() 
                     simple_edit = layout.operator("tp_ops.half_curve","Beveled Half-Circle")               

        else:
    
            col = split.column()
            col.scale_y = 1.2
            
            col.operator("tp_ops.optimize_curve", text = "Optimize")            
            col.operator("tp_ops.curve_copies", text = "Copy")            
            col.operator("object.curve_outline", text = "Outline")
               
            
            
            col = split.column()
            col.scale_y = 1.2            
           
            col.operator("curvetools2.operatororigintospline0start", text="SetFirst")                                                                                    
            col.operator("curve.smoothspline", text ="Smooth")  
       
            vertex = []
            selected = []
            n = 0
            obj = context.active_object
            if obj != None:
                 if obj.type == 'CURVE':
                     for i in obj.data.splines:
                         for j in i.bezier_points:
                             n += 1
                             if j.select_control_point:
                                 selected.append(n)
                                 vertex.append(obj.matrix_world * j.co)

                 if len(vertex) > 0:
                    col.operator("object.sep_outline", text = "Sep-Outline")
                
                 if len(vertex) == 2 and abs(selected[0] - selected[1]) == 1:
                     simple_divide = col.operator("curve.bezier_spline_divide", text='Spline Divide')


