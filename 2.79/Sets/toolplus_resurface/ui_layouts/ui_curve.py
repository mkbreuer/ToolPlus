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

from toolplus_resurface.ui_menus.menu_curve import (VIEW3D_TP_Spline_Type_Menu, VIEW3D_TP_Handle_Type_Menu)
from toolplus_resurface.ui_menus.menu_origin import (VIEW3D_TP_Origin_Panel_Menu)


def draw_curve_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        
       
        icons = load_icons()
    
        obj = context.object
        scene = context.scene


        col = layout.column(align=True)                
        if not tp_props.display_curve_info: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_curve_info", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Curve Info")

            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'CURVE', 'NURBS', 'SURFACE'}: 
                                                                  
                    sub = row.row(1)
                    sub.scale_x = 0.15
                    sub.alignment = 'RIGHT'            
                    sub.prop(context.object.data, "dimensions", expand=True)   


        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_curve_info", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Curve Info")    

            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'CURVE', 'NURBS', 'SURFACE'}: 
                                                                  
                    sub = row.row(1)
                    sub.scale_x = 0.15
                    sub.alignment = 'RIGHT'            
                    sub.prop(context.object.data, "dimensions", expand=True)   


           
            box.separator()   
            box.separator()  

            row = box.row(1)
            row.label("VertColor")
            row.prop(context.scene, "curve_vertcolor", text="")
            row.operator("dynamic.normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')   

            
            box.separator()  
            box.separator()  


            if context.mode == 'EDIT_CURVE':
                                 
                row = box.row(1)
                row.operator("curvetools2.operatorcurveinfo", text = "Curve")                        
                row.operator("curvetools2.operatorsplinesinfo", text = "Splines")
                row.operator("curvetools2.operatorsegmentsinfo", text = "Segments")
                 
                box.separator()  

            row = box.row(1) 
            row.operator("curvetools2.operatorselectioninfo", text = "Selection Info:")
            row.prop(scene.curvetools, "NrSelectedObjects", text = "")   

            if context.mode == 'EDIT_CURVE':

                row = box.row(1) 
                row.operator("curvetools2.operatorcurvelength", text = "Calc Length")
                row.prop(scene.curvetools, "CurveLength", text = "")    

            box.separator()             
            

                        
                    

            box = col.box().column(1)   
           
            box.separator()              
           
            row = box.row(1)        
            row.prop(context.object.data, "use_path", text="Path Animation")

            row = box.column()
            row.prop(context.object.data, "path_duration", text="Frames")
            row.prop(context.object.data, "eval_time")

            # these are for paths only
            row = box.row()
            row.prop(context.object.data, "use_path_follow")

            box.separator() 

        


        if context.mode == 'EDIT_CURVE':


            col = layout.column(align=True)                
            if not tp_props.display_curve_select: 
              
                box = col.box().column(1)
                
                row = box.row(1)   
                row.prop(tp_props, "display_curve_select", text="", icon="TRIA_RIGHT", emboss = False)                
                row.label("Curve Select")

                row.operator("curve.select_less",text="",  icon = "DISCLOSURE_TRI_DOWN")
                row.operator("curve.select_all",text="",  icon = "PLUS").action = 'TOGGLE'  
                row.operator("curve.select_more",text="",  icon = "DISCLOSURE_TRI_RIGHT")   

            else:
               
                box = col.box().column(1)
                
                row = box.row(1)  
                row.prop(tp_props, "display_curve_select", text="", icon="TRIA_DOWN", emboss = False)            
                row.label("Curve Select")    


                box.separator()   
                box.separator()  

                row = box.row(1)                 
                sub = row.row()
                sub.scale_x = 0.3
                sub.operator("curve.select_more",text="+")
                sub.operator("curve.select_all",text="All").action = 'TOGGLE'  
                sub.operator("curve.select_less",text="-")   

                box.separator()

                row = box.row(1) 
                row.operator("curve.select_all", text="Inverse").action = 'INVERT'
                row.menu("VIEW3D_MT_edit_curve_showhide") 

                row = box.row(1) 
                row.operator("curve.select_random", text="Random") 
                row.operator("curve.select_similar", text="Similar") 

                row = box.row(1)
                row.operator("curve.select_linked", text="Linked")             
                row.operator("curve.select_nth", text="Checker")
                
                box.separator()
                 
                row = box.row(1) 
                row.operator("curve.de_select_first", text="First")
                row.operator("curve.de_select_last", text="Last")
                
                row = box.row(1)             
                row.operator("curve.select_next", text="Next")
                row.operator("curve.select_previous", text="Previous")

                box.separator() 




        col = layout.column(align=True)                
        if not tp_props.display_curve_type: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_curve_type", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Curve Type")


            button_origin_bbox = icons.get("icon_origin_bbox")             
            row.menu("tp_menu.curve_spline_type", text="", icon="IPO_EASE_IN_OUT", icon_value=button_origin_bbox.icon_id)

            button_origin_bbox = icons.get("icon_origin_bbox")             
            row.menu("tp_menu.curve_handle_type", text="", icon="IPO_BEZIER", icon_value=button_origin_bbox.icon_id)
    

        else:
           
             box = col.box().column(1)
            
             row = box.row(1)  
             row.prop(tp_props, "display_curve_type", text="", icon="TRIA_DOWN", emboss = False)            
             row.label("Curve Type")              

             box.separator()   
             box.separator() 
             

             if context.mode == 'EDIT_CURVE':


                 row = box.column(1)
                 row.label("Spline", icon="IPO_CIRC") 
                 
                 box.separator()
                           
                 row = box.row(1)  
                 row.operator("curve.spline_type_set", "Poly").type = 'POLY'   
                 row.operator("curve.spline_type_set", "Bezier").type = 'BEZIER'   
                 row.operator("curve.spline_type_set", "Nurbs").type = 'NURBS'   

                 box.separator()   
                 box.separator()   
         
                 row = box.row(1) 
                 row.label("Handle", icon='IPO_BEZIER') 

                 box.separator() 
                         
                 row = box.row(1)   
                 row.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
                 row.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'
                 
                 row = box.row(1)   
                 row.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'
                 row.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'

                 box.separator()  

             else:

                
                row = box.row(1)
                row.label("Spline", icon="IPO_CIRC")                        
               
                row = box.row(1)
                row.operator("curve.to_poly","Poly")
                row.operator("curve.to_bezier","Bezièr")
                row.operator("curve.to_nurbs","Nurbs")

                box.separator() 
                box.separator() 

                row = box.row(1)
                row.label("Handle", icon="IPO_BEZIER") 
                row.label("")                         
                         
      
                row = box.row(1)                                                    
                row.operator("curve.handle_to_automatic","Auto")                                                  
                row.operator("curve.handle_to_free","Free") 
         
                row = box.row(1)  
                row.operator("curve.handle_to_vector","Vector") 
                row.operator("curve.handle_to_aligned","Aligned")

                box.separator() 
                box.separator() 







        col = layout.column(align=True)                
        if not tp_props.display_curve_edit: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_curve_edit", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Curve Edit")
                                                                                        
            if context.mode == 'EDIT_CURVE':
                
                button_curve_smooth = icons.get("icon_curve_smooth") 
                row.menu("menu.curve_cad", "", icon_value=button_curve_smooth.icon_id)   
                #row.operator("curve.smooth", "", icon_value=button_curve_smooth.icon_id)   
                
                button_curve_open = icons.get("icon_curve_open") 
                row.operator("curve.cyclic_toggle","", icon_value=button_curve_open.icon_id)            
               
                
                button_curve_start = icons.get("icon_curve_start") 
                row.operator("curve.surfsk_first_points", text="", icon_value=button_curve_start.icon_id)             
            else:                

                button_curve_smooth = icons.get("icon_curve_smooth") 
                row.operator("curve.smoothspline", "", icon_value=button_curve_smooth.icon_id)   
                
                button_curve_open = icons.get("icon_curve_open") 
                row.operator("curve.open_circle", text = "", icon_value=button_curve_open.icon_id)  
                
                button_curve_start = icons.get("icon_curve_start") 
                row.operator("curvetools2.operatororigintospline0start", text="", icon_value=button_curve_start.icon_id)   

    
        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_curve_edit", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Curve Edit")              
            

            if context.mode == 'EDIT_CURVE':

                 box.separator()  
                 box.separator()  
                 
                 row = box.row(1)
                 row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
                 row.prop(context.object.data, "resolution_u", text="Resolution")
                 row.operator("tp_ops.wire_all", text="", icon='WIRE') 

                 box.separator()  
                 box.separator()  

                 row = box.row(1) 
                 row.operator("curve.bezier_length","Lenght")                                
                 row.operator("curve.surfsk_first_points", text="Set First")                   

                 row = box.row(1) 
                 row.operator("curve.cyclic_toggle","Cyclic")  
                 row.operator("curve.switch_direction", text="Direction")                   
 
                 box.separator()   
                 box.separator() 

                 row = box.row(1)
                 row.label("Subdivide")      
                 row.operator("curve.bezier_subdivide","3xBezièr")                  
                 
                 row = box.row(1) 
                 row.operator("curve.subdivide", text="1").number_cuts=1        
                 row.operator("curve.subdivide", text="2").number_cuts=2
                 row.operator("curve.subdivide", text="3").number_cuts=3
                 row.operator("curve.subdivide", text="4").number_cuts=4
                 row.operator("curve.subdivide", text="5").number_cuts=5        
                 row.operator("curve.subdivide", text="6").number_cuts=6  

                 box.separator()  
                 box.separator()             
                  

                 row = box.row(1)
                 row.operator("curve.extrude_move", text="Extrude")                                             
                 row.operator("curve.remove_doubles", text="RemDoubles") 
  
                 row = box.row(1)     
                 row.operator("curve.make_segment",  text="Weld") 
                 row.operator("curve.bezier_merge_ends","MergeEnd")  

                 box.separator() 

                 row = box.row(1)               
                 row.operator("curve.trim_tool", text="Trim")  
                 row.operator("curve.bezier_intersection","Intersect")                   
    
                 row = box.row(1) 
                 row.operator("curve.separate",  text="Separate") 
                 row.operator("curve.split",  text="Split")     

                 box.separator() 

                 row = box.row(1)  
                 row.operator("curve.smooth", text="Smooth") 
                 row.operator("curve.bezier_circle","Circle")  
                
                 row = box.row(1)   
                 row.operator("curve.bezier_offset","Offset") 
                 row.operator("object.curve_outline", text = "Outline") 

                 box.separator() 

                 row = box.row(1) 
                 row.operator("curve.radius_set", "Radius")  
                 row.operator("transform.tilt", text="Tilt")  
            
                 row = box.row(1)                                    
                 row.operator("transform.vertex_random", text="Random") 
                 row.operator("curve.tilt_clear", "Clear Tilt")                 


                 box.separator() 

                 row = box.row(1) 
                
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



                     if len(vertex) == 1 and n > 0:
                      
                        data = context.active_object.data
                        points = data.splines.active.bezier_points

                        selected_points = [idx for idx, p in enumerate(points) if p.select_control_point]
                        
                        if len(selected_points) > 0:
                            idx = selected_points[0]
                            point = points[idx]

                            box.separator() 

                            row = box.row(1)                             
                            row.prop(point, "weight_softbody", text='weight')
                            row.operator("curve.smooth_weight", text="", icon="LAYER_USED")                            
                            
                            row = box.row(1) 
                            row.prop(point, "radius", text='radius')
                            row.operator("curve.smooth_radius", text="", icon="LAYER_USED")                             
                            
                            
                            row = box.row(1) 
                            row.prop(point, "tilt", text='tilt')
                            row.operator("curve.smooth_tilt", text="", icon="LAYER_USED") 
                         
                            box.separator()       


                     if len(vertex) > 0 and n > 2:
                         simple_edit = row.operator("curve.bezier_points_fillet", text='Curve Fillet')       
                         
                         box.separator()                        
                     
                     
                     if len(vertex) > 0 and n > 2:
                        row.operator("curve.extend_tool", text="Curve Extend")
                        
                        box.separator()   


                     if len(vertex) == 2:
                         if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':    

                             box.separator() 
                            
                             row = box.row(1)   
                             simple_edit = row.operator("tp_ops.quader_curve","Beveled Quarter", icon="BLANK1")   

                             box.separator()   


                     if len(vertex) == 1:
                         if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':    

                             box.separator() 
                           
                             row = box.row(1)
                             simple_edit = row.operator("tp_ops.half_curve","Beveled Half-Circle", icon="BLANK1")               

                             box.separator()                   


                     if len(vertex) > 0:

                        box.separator()  

                        box = col.box().column(1)   
                     
                        box.separator()                      
                   
                        row = box.column(1)
                                        
                        if context.object.data.splines.active.type == 'POLY':
                            row.prop(context.object.data.splines.active, "use_cyclic_u", text="U Cyclic")                        
                            row.prop(context.object.data.splines.active, "use_smooth")
                        else:
                            if context.object.data.splines.active.type == 'NURBS':
                                row.prop(context.object.data.splines.active, "use_cyclic_u", text="U Cyclic")

                            if context.object.data.splines.active.type == 'NURBS':
                                row.prop(context.object.data.splines.active, "use_bezier_u", text="U Bezier")
                                row.prop(context.object.data.splines.active, "use_endpoint_u", text="U Endpoint")
                                row.prop(context.object.data.splines.active, "order_u", text="U Order")
                 
                            if context.object.data.splines.active.type == 'SURFACE':
                                row.prop(context.object.data.splines.active, "use_cyclic_v", text="V Cyclic")
                                row.prop(context.object.data.splines.active, "use_bezier_v", text="V Bezier")
                                row.prop(context.object.data.splines.active, "use_endpoint_v", text="V Endpoint")
                                row.prop(context.object.data.splines.active, "order_v", text="V Order")

                            if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':

                                row.alignment = 'CENTER'
                                row.label(text="Interpolation:")
                                
                                box.separator()  
                                
                                row = box.column(1)                                                      
                                row.prop(context.object.data.splines.active, "tilt_interpolation", text="Tilt")
                                row.prop(context.object.data.splines.active, "radius_interpolation", text="Radius")
                            
                            box.separator()          
                            
                            row = box.column(1)                                     
                            row.prop(context.object.data.splines.active, "use_smooth")

                        box.separator() 

                     else:
                        pass





            else:


                box.separator()
                box.separator()
                                 
                row = box.row(1)                
                row.operator("curve.open_circle", text = "Cyclic")  
                row.operator("curvetools2.operatororigintospline0start", text="SetFirst")         
                                                                             
                row = box.row(1)
                row.operator("curve.surfsk_reorder_splines", text="GP Reorder")                                                
                row.operator("curve.smoothspline", "Smooth")                
               
                box.separator() 
                box.separator() 


                box = col.box().column(1)   
  
                box.separator()   
                
                row = box.row(1)
                row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
                row.prop(context.object.data, "resolution_u", text="Resolution")                         

                active_wire = bpy.context.object.show_wire 
                if active_wire == True:
                    row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
                else:                       
                    row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 

                box.separator()   
                box.separator()   

                row = box.row(1) 
                row.scale_y = 1.5                  
                row.operator("curvetools2.create_auto_loft", text = "Loft", icon = 'IPO_QUAD')
                row.operator("curvetools2.operatorsweepcurves", text = "Sweep", icon = 'IPO_QUAD')  
                row.operator("curvetools2.operatorbirail", text = "Birail", icon = 'IPO_CUBIC')  

                box.separator() 

                row = box.row(1)              
                row.prop(context.window_manager, "auto_loft", text="AutoLoft", toggle=True, icon ="HOOK")             

                row = box.column_flow(2)              
                
                lofters = [o for o in scene.objects if "autoloft" in o.keys()]
                for o in lofters:
                    row.label(o.name)
                 
                box.separator()   
                box.separator()   

                row = box.row(1)
                row.operator("object.curve_outline", text = "Outline")
                               
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
                        row.operator("object.sep_outline", text = "Separate it")
                    
                    if len(vertex) == 2 and abs(selected[0] - selected[1]) == 1:
                        simple_divide = row.operator("curve.bezier_spline_divide", text='Spline Divide')

               
                box.separator()   
                box.separator()   

                row = box.row(1)
                row.operator("curvetools2.operatorintersectcurves", text = "Intersect Curves")
                row = box.row(1)
                row.prop(scene.curvetools, "LimitDistance", text = "LimitDistance")
               
                box.separator()                           
              
                box = col.box().column(1) 
                
                row = box.row(align=0)
                row.prop(scene.curvetools, "IntersectCurvesAlgorithm", text = "Algorithm")

                row = box.row(align=0.1)
                row.prop(scene.curvetools, "IntersectCurvesMode", text = "Mode")

                row = box.row(align=0.1)
                row.prop(scene.curvetools, "IntersectCurvesAffect", text = "Affect")

                box.separator()               



        col = layout.column(align=True)                
        if not tp_props.display_curve_bevel: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_curve_bevel", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Curve Bevel")
                 
            button_curve_extrude = icons.get("icon_curve_extrude")     
            row.operator("tp_ops.curve_extrude", text="", icon_value=button_curve_extrude.icon_id)                                
            row.operator("tp_ops.enable_bevel", text="", icon='MOD_WARP')                                 
            row.operator("dynamic.normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')
       
        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_curve_bevel", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Curve Bevel")  


            box.separator()  
            box.separator()  


            row = box.row(1)      
            row.prop(context.object.data, "fill_mode", text="")           
            
            show = bpy.context.object.data.dimensions
            if show == '3D':
                 
                active_bevel = bpy.context.object.data.bevel_depth            
                if active_bevel == 0.0:              
                 row.operator("tp_ops.enable_bevel", text="Bevel on", icon='MOD_WARP')
                else:   
                 row.operator("tp_ops.enable_bevel", text="Bevel off", icon='MOD_WARP')                 
                          
            row = box.row(1)                          
            row.prop(context.object.data, "use_fill_deform")

            box.separator()  
            box.separator()  
            
            row = box.row(1) 
            active_wire = bpy.context.object.show_wire                                                        
            if active_wire == True:
                row.operator("tp_ops.wire_off", "", icon = 'SOLID')              
            else:                       
                row.operator("tp_ops.wire_on", "", icon = 'WIRE') 
            row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
            row.operator("dynamic.normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')   
            
            row = box.row(1)
            row.prop(context.object.data, "resolution_u", text="Rings")          
            row.prop(context.object.data, "bevel_resolution", text="Loops")

            row = box.row(1)
            row.prop(context.object.data, "offset")
            row.prop(context.object.data, "extrude","Height")

            box.separator()
            box.separator()

            row = box.row(1) 
            if tp_props.display_bevel_reso:                                 
                row.prop(tp_props, "display_bevel_reso", text="Loop Resolution", icon='TRIA_DOWN_BAR')                 
            else:                 
                row.prop(tp_props, "display_bevel_reso", text="Loop Resolution", icon='TRIA_UP_BAR')        
                                   
            if tp_props.display_bevel_reso:       
                                   
                row = box.column_flow(2)
                row.label("Value Rings", icon = "PROP_CON")  
                row.label("1 = 4",) 
                row.label("2 = 8") 
                row.label("4 = 16") 
                row.label("8 = 32")
                row.label("(+4) Full Circle")          

                row.label("Value Loops", icon = "COLLAPSEMENU")  
                row.label("0 = 4",) 
                row.label("2 = 8") 
                row.label("4 = 12") 
                row.label("8 = 16")           
                row.label("(+2) Along Curve")                                 

            box.separator()  
            box.separator()  

            box = col.box().column(1)  
           
            box.separator()  
           
            row = box.row(1) 
            row.alignment = 'CENTER'
            row.label(text="Path / Deform / Twist:")

            box.separator() 

            row = box.row(1)
            row.prop(context.object.data, "use_radius")
            row.prop(context.object.data, "use_stretch")
            
            row = box.row(1)
            row.prop(context.object.data, "use_deform_bounds")   
            
            row = box.row(1)                        
            row.prop(context.object.data,"twist_mode", text="")
            row.prop(context.object.data, "twist_smooth", text="Smooth")    

            box.separator()    



        col = layout.column(align=True)                
        if not tp_props.display_curve_taper: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_curve_taper", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Curve Guide")
                 
            button_curve_extrude = icons.get("icon_curve_extrude")     
            #row.operator("tp_ops.curve_extrude", text="", icon_value=button_curve_extrude.icon_id)                                
           
            #button_curve_guide = icons.get("icon_curve_guide")              
            row.operator("tp_ops.curve_guide_bevel", text="", icon ="CONSTRAINT_DATA")                          

            #button_curve_guide_taper = icons.get("icon_curve_guide_taper")   
            row.operator("curve.tapercurve", "", icon = "CURVE_BEZCURVE") 

            #button_curve_guide_bevel = icons.get("icon_curve_guide_bevel")   
            row.operator("curve.bevelcurve", "", icon = "CURVE_BEZCIRCLE") 
       
        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_curve_taper", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Curve Guide")  

            if context.mode == "OBJECT":

                box.separator()
                box.separator()
                
                row = box.row(1)
                
                #button_curve_guide = icons.get("icon_curve_guide")                    
                row.operator("tp_ops.curve_guide_bevel", text="Add Bevel Guide", icon ="CONSTRAINT_DATA")                          

                box.separator()

                row = box.row(1)  
                row.label("Taper Draw:") 
             
                button_draw_bevel = icons.get("icon_draw_bevel")
                row.operator("tp_ops.curve_draw", text="", icon_value=button_draw_bevel.icon_id)    
                
                box.separator()

                row = box.row(1)                  
                tool_settings = context.tool_settings
                cps = tool_settings.curve_paint_settings
                row.prop(cps, "radius_taper_start", text="Start")
                row.prop(cps, "radius_taper_end", text="End")

                row = box.row(1) 
                row.prop(cps, "depth_mode", text="")
                row.prop(cps, "depth_mode", text="")

                box.separator() 
               
                active_bevel = (bpy.context.object.data.bevel_depth > 0 or bpy.context.object.data.bevel_object is not None)
                if active_bevel == True:
                    
                    row = box.row(1) 
                    row.label(text="Edit Bevel:")

                    row = box.row(1)  
                    row.operator("curve.edit_bevel_curve", text="Edit")
                    row.operator("curve.hide_bevel_objects", text="(Un)Hide")
                    row.operator("curve.add_bevel_to_curve", text="Reset")

                    box.separator()
               
                else: 
                    pass


            if context.mode =='EDIT_CURVE':                      

                box.separator() 
                box.separator() 
                                
                row = box.row(1)  
                row.label("Taper Draw Reset:") 

                button_draw_bevel = icons.get("icon_draw_bevel")
                row.operator("tp_ops.curve_draw", text="", icon_value=button_draw_bevel.icon_id)                    
                
                box.separator()

                row = box.row(1)                  
                tool_settings = context.tool_settings
                cps = tool_settings.curve_paint_settings
                row.prop(cps, "radius_taper_start", text="Start")
                row.prop(cps, "radius_taper_end", text="End")

                box.separator()
            
                active_level = context.active_object       

                # check if layer 19
                #if active_level.layers[19] == True: 

                row = box.row(1)      
                row.label(text="Taper Bevel (Layer 19)")

                row = box.row(1)             
                row.operator("curve.edit_bevel_curve", text="Edit")                                 
                no_taper = bpy.context.object.data.bevel_object             
                if no_taper is None:
                    row.operator("curve.finish_edit_bevel", text="Finish")
                row.prop(context.scene, "tp_finish_taper", text="", icon ="EDIT")  
               
                box.separator()

                #else:
                    #pass
                
                box.separator() 

                row = box.row(1)  
                row.label(text="Taper:")
                row.prop(context.object.data, "taper_object", text="")
                 
                row = box.row(1) 
                row.label(text="Bevel:")
                row.prop(context.object.data, "bevel_object", text="")
             
                box.separator()  
                box.separator() 

                row1 = box.row(1)              
                row1.active = (context.object.data.bevel_depth > 0 or context.object.data.bevel_object is not None)

                row1.prop(context.object.data, "bevel_factor_start", text="Curve Start") 

                sub = row1.row(1)
                sub.scale_x = 0.35
                sub.alignment = 'RIGHT'  
                sub.prop(context.object.data, "bevel_factor_mapping_start", text="")

                row1 = box.row(1) 
                row1.prop(context.object.data, "bevel_factor_end", text="Curve End")  

                sub = row1.row(1)
                sub.scale_x = 0.35
                sub.alignment = 'RIGHT'  
                sub.prop(context.object.data, "bevel_factor_mapping_end", text="")
                          
                box.separator() 

                row = box.row(1)                      
                sub = row.row()
                sub.active = context.object.data.taper_object is not None
                sub.prop(context.object.data, "use_map_taper")

                sub = row.row()
                sub.active = context.object.data.bevel_object is not None
                sub.prop(context.object.data, "use_fill_caps")

                box.separator() 


            else:

                box.separator()
                  
                row = box.row(1)
                #button_curve_guide_taper = icons.get("icon_curve_guide_taper") 
                row.operator("curve.tapercurve", "C-Taper", icon = "CURVE_BEZCURVE") 
                row.prop(context.object.data, "taper_object", text = "")

                row = box.row(1)
                #button_curve_guide_bevel = icons.get("icon_curve_guide_bevel") 
                row.operator("tp_ops.curveaceous_galore", "C-Bevel", icon = "CURVE_BEZCIRCLE") 
                #row.operator("tp_ops.add_bevel_guide", "C-Bevel", icon = "CURVE_BEZCIRCLE") 
                row.prop(context.object.data, "bevel_object", text = "")
      
                box.separator() 
                box.separator() 

                row1 = box.row(1)              
                row1.active = (context.object.data.bevel_depth > 0 or context.object.data.bevel_object is not None)

                row1.prop(context.object.data, "bevel_factor_start", text="Curve Start") 

                sub = row1.row(1)
                sub.scale_x = 0.35
                sub.alignment = 'RIGHT'  
                sub.prop(context.object.data, "bevel_factor_mapping_start", text="")

                row1 = box.row(1) 
                row1.prop(context.object.data, "bevel_factor_end", text="Curve End")  

                sub = row1.row(1)
                sub.scale_x = 0.35
                sub.alignment = 'RIGHT'  
                sub.prop(context.object.data, "bevel_factor_mapping_end", text="")
                          
                box.separator() 

                row = box.row(1)                      
                sub = row.row()
                sub.active = context.object.data.taper_object is not None
                sub.prop(context.object.data, "use_map_taper")

                sub = row.row()
                sub.active = context.object.data.bevel_object is not None
                sub.prop(context.object.data, "use_fill_caps")

                box.separator() 







        col = layout.column(align=True)                
        if not tp_props.display_curve_utility: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_curve_utility", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Curve Utility")
           
            #button_curve_del_0 = icons.get("icon_curve_del_0") 
            #row.operator("curvetools2.operatorsplinesremovezerosegment",text="", icon_value=button_curve_del_0.icon_id)   
            row.operator("curvetools2.operatorsplinesremovezerosegment", text = "", icon ="IPO_CUBIC")

            #button_curve_del_short = icons.get("icon_curve_del_short") 
            #row.operator("curvetools2.operatorsplinesremoveshort",text="", icon_value=button_curve_del_short.icon_id)  
            row.operator("curvetools2.operatorsplinesremoveshort", text = "", icon ="IPO_QUAD")

            #button_curve_join_spline = icons.get("icon_curve_join_spline") 
            #row.operator("curvetools2.operatorsplinesjoinneighbouring",text="Join neighbouring Splines", icon_value=button_curve_join_splines.icon_id) 
            row.operator("curvetools2.operatorsplinesjoinneighbouring", text = "", icon ="AUTOMERGE_ON")

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_curve_utility", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Curve Utility")  


            if context.mode == 'EDIT_CURVE':
             
                 box.separator()    
                 box.separator()  

                 row = box.row(1)
                 row.alignment = "CENTER" 
                 row.label("Optimize Tools for BezièrCurve", icon="LAMP")

                 box.separator()   
                 box.separator()   

                 row = box.row(1) 

                 #button_curve_join_spline = icons.get("icon_curve_join_spline") 
                 #row.operator("curvetools2.operatorsplinesjoinneighbouring",text="Join neighbouring Splines", icon_value=button_curve_join_splines.icon_id)  
                 row.operator("curvetools2.operatorsplinesjoinneighbouring", text = "Join neighbouring Splines", icon ="AUTOMERGE_ON")

                 row = box.row(1)
                 row.prop(scene.curvetools, "SplineJoinDistance", text = "Threshold join")
                                 
                 box.separator()    
                 box.separator()    

                 row = box.row(1) 
                 row.prop(scene.curvetools, "SplineJoinStartEnd", text = "Only at start & end")

                 row = box.row(align=0.5) 
                 row.prop(scene.curvetools, "SplineJoinMode", text = "Join")
               
                 box.separator()                   
                 box.separator()                   
 
                 row = box.column(1)         

                 #button_curve_del_0 = icons.get("icon_curve_del_0") 
                 #row.operator("curvetools2.operatorsplinesremovezerosegment",text="Del 0-Segments", icon_value=button_curve_del_0.icon_id)  
                 row.operator("curvetools2.operatorsplinesremovezerosegment", text = "Del 0-Segments", icon ="DISCLOSURE_TRI_DOWN")

                 #button_curve_del_short = icons.get("icon_curve_del_short") 
                 #row.operator("curvetools2.operatorsplinesremoveshort",text="Del Short Splines", icon_value=button_curve_del_short.icon_id)  
                 row.operator("curvetools2.operatorsplinesremoveshort", text = "Del Short Splines", icon ="DISCLOSURE_TRI_DOWN")

                 box.separator()   


                 row = box.row(1)
                 row.prop(scene.curvetools, "SplineRemoveLength", text = "Threshold remove")

                 box.separator()                             
             

            else:
                
                 box.separator()   
                 box.separator()   

                 row = box.row(1)
                 row.alignment = "CENTER" 
                 row.label("Optimize Tools for BezièrCurve", icon="LAMP")

                 box.separator()   
                 box.separator()   

                 row = box.row(1) 

                 #button_curve_join_spline = icons.get("icon_curve_join_spline") 
                 #row.operator("curvetools2.operatorsplinesjoinneighbouring",text="Join neighbouring Splines", icon_value=button_curve_join_splines.icon_id)  
                 row.operator("curvetools2.operatorsplinesjoinneighbouring", text = "Join neighbouring Splines", icon ="AUTOMERGE_ON")

                 row = box.row(1)
                 row.prop(scene.curvetools, "SplineJoinDistance", text = "Threshold Join")

                 row = box.row(1) 
                 row.prop(scene.curvetools, "SplineJoinStartEnd", text = "Only at start & end")

                 box.separator()   
                 box.separator()   

                 row = box.row(align=0.5) 
                 row.prop(scene.curvetools, "SplineJoinMode", text = "Join")

                 box.separator()   
                 box.separator()   

                 row = box.row(1)         

                 #button_curve_del_0 = icons.get("icon_curve_del_0") 
                 #row.operator("curvetools2.operatorsplinesremovezerosegment",text="Del 0-Segments", icon_value=button_curve_del_0.icon_id)  
                 row.operator("curvetools2.operatorsplinesremovezerosegment", text = "Del 0-Segments", icon ="DISCLOSURE_TRI_DOWN")

                 #button_curve_del_short = icons.get("icon_curve_del_short") 
                 #row.operator("curvetools2.operatorsplinesremoveshort",text="Del Short Splines", icon_value=button_curve_del_short.icon_id)  
                 row.operator("curvetools2.operatorsplinesremoveshort", text = "Del Short Splines", icon ="DISCLOSURE_TRI_DOWN")

                 box.separator()   

                 row = box.row(1)
                 row.prop(scene.curvetools, "SplineRemoveLength", text = "Threshold Remove")

                 box.separator()  

 