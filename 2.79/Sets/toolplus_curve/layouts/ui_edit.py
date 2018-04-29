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

def draw_edit_ui(self, context, layout):

    icons = load_icons()     
    my_button_one = icons.get("icon_image1")        
        
    col = layout.column(align=True) 
 
    if context.mode == 'EDIT_CURVE': 


         box = col.box().column(1)
        
         box.separator()  
       
         row = box.row(1)
         row.scale_y = 1.2    
         active_wire = bpy.context.object.show_wire 
         if active_wire == True:
            row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
         else:                       
             row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 
         row.prop(context.object.data, "bevel_depth", text="Resolution")
         row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  

         box.separator()          
         box.separator()

         row = box.row(1)
         row.scale_y = 1.2                                         
         row.operator("curve.surfsk_first_points", text="Set First") 
         row.operator("tp_ops.origin_first", text="Origin First")                   
                           

         row = box.row(1)
         row.scale_y = 1.2     
         row.operator("curve.cyclic_toggle","Cyclic")  
         row.operator("curve.switch_direction", text="Direction")                   
 
         box.separator()   
         box.separator() 

         row = box.row(1)
         row.scale_y = 1.2    
         row.label("Subdivide")      
         row.operator("curve.bezier_subdivide","3x Params")                  
         
         row = box.row(1) 
         row.scale_y = 1.2    
         row.operator("curve.subdivide", text="1").number_cuts=1        
         row.operator("curve.subdivide", text="2").number_cuts=2
         row.operator("curve.subdivide", text="3").number_cuts=3
         row.operator("curve.subdivide", text="4").number_cuts=4
         row.operator("curve.subdivide", text="5").number_cuts=5        
         row.operator("curve.subdivide", text="6").number_cuts=6  

         box.separator()  
         box.separator()             
          

         row = box.row(1)
         row.scale_y = 1.2    
         row.operator("curve.extrude_move", text="Extrude")                                             
         row.operator("curve.remove_doubles", text="Rem. Doubles") 
  
         row = box.row(1)
         row.scale_y = 1.2         
         row.operator("curve.make_segment",  text="Weld") 
         row.operator("curve.bezier_merge_ends","MergeEnd")  

         box.separator() 

         row = box.row(1)
         row.scale_y = 1.2                   
         row.operator("curve.trim_tool", text="Trim")  
         row.operator("curve.bezier_intersection","Intersect")                   

         row = box.row(1)
         row.scale_y = 1.2     
         row.operator("curve.separate",  text="Separate") 
         row.operator("curve.split",  text="Split")     

         box.separator() 

         row = box.row(1)
         row.scale_y = 1.2      
         row.operator("curve.smooth", text="Smooth") 
         row.operator("curve.bezier_circle","Circle")  
        
         row = box.row(1)
         row.scale_y = 1.2       
         row.operator("curve.bezier_offset","Offset") 
         row.operator("object.curve_outline", text = "Outline") 

         box.separator() 

         row = box.row(1)
         row.scale_y = 1.2     
         row.operator("curve.radius_set", "Radius")  
         row.operator("transform.tilt", text="Tilt")  
    
         row = box.row(1)
         row.scale_y = 1.2                                        
         row.operator("transform.vertex_random", text="Random") 
         row.operator("curve.tilt_clear", "Clear Tilt")                 

         box.separator() 
        
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



             if len(vertex) > 0 and n > 2:
                
                row = box.row(1)
                row.scale_y = 1.2                    
                simple_edit = row.operator("curve.bezier_points_fillet", text='Curve Fillet')       
                row.operator("curve.extend_tool", text="Curve Extend")
                
                box.separator()   
 
             
             if len(vertex) == 1 and n > 0:
              
                data = context.active_object.data
                points = data.splines.active.bezier_points

                selected_points = [idx for idx, p in enumerate(points) if p.select_control_point]
                
                if len(selected_points) > 0:
                    idx = selected_points[0]
                    point = points[idx]

                    box.separator() 

                    row = box.row(1)
                    row.scale_y = 1.2                                 
                    row.prop(point, "weight_softbody", text='weight')
                    row.operator("curve.smooth_weight", text="", icon="LAYER_USED")                            
                    
                    row = box.row(1)
                    row.scale_y = 1.2     
                    row.prop(point, "radius", text='radius')
                    row.operator("curve.smooth_radius", text="", icon="LAYER_USED")                             
                    
                    
                    row = box.row(1)
                    row.scale_y = 1.2     
                    row.prop(point, "tilt", text='tilt')
                    row.operator("curve.smooth_tilt", text="", icon="LAYER_USED") 
                 
                    box.separator()       


             if len(vertex) == 2:
                 if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':    

                     box.separator() 
                    
                     row = box.row(1)
                     row.scale_y = 1.2       
                     simple_edit = row.operator("tp_ops.quader_curve","Beveled Quarter", icon="BLANK1")   

                     box.separator()   


             if len(vertex) == 1:
                 if context.object.data.splines.active.type == 'BEZIER' and context.object.data.dimensions == '3D':    

                     box.separator() 
                   
                     row = box.row(1)
                     row.scale_y = 1.2    
                     simple_edit = row.operator("tp_ops.half_curve","Beveled Half-Circle", icon="BLANK1")               

                     box.separator()                   


             if len(vertex) > 0:

                box.separator()  

                box = col.box().column(1)   
             
                box.separator()                      
           
                row = box.column(1)
                row.scale_y = 1.2    
                                
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
                        row.scale_y = 1.2                                                          
                        row.prop(context.object.data.splines.active, "tilt_interpolation", text="Tilt")
                        row.prop(context.object.data.splines.active, "radius_interpolation", text="Radius")
                    
                    box.separator()          
                    
                    row = box.column(1) 
                    row.scale_y = 1.2                                        
                    row.prop(context.object.data.splines.active, "use_smooth")

                box.separator() 

             else:
                pass


    else:
        
     
         box = col.box().column(1)  
        
         box.separator()  

         row = box.row(1) 
         row.scale_y = 1.3     
         row.operator("dynamic.normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')  

         row.prop(context.object.data, "bevel_depth", text="Resolution")

         active_wire = bpy.context.object.show_wire 
         if active_wire == True:
            row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
         else:                       
             row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 

         box.separator()  
         
         box = col.box().column(1)  
          
         box.separator()  

         row = box.row(1) 
         row.scale_y = 1.5                  
         row.operator("curvetools2.create_auto_loft", text = "Loft", icon = 'IPO_QUAD')
         row.operator("curvetools2.operatorsweepcurves", text = "Sweep", icon = 'IPO_QUAD')  
         row.operator("curvetools2.operatorbirail", text = "Birail", icon = 'IPO_CUBIC')  

         box.separator() 

         row = box.row(1) 
         row.scale_y = 1.2             
         row.prop(context.window_manager, "auto_loft", toggle=True)             

         row = box.column_flow(2) 
         row.scale_y = 1.2                         
         scene = context.scene
         lofters = [o for o in scene.objects if "autoloft" in o.keys()]
         for o in lofters:
             row.label(o.name)
        
         box.separator()           

         box = col.box().column(1)  

         box.separator()           

         row = box.row(1) 
         row.scale_y = 1.2  
         row.operator("curve.open_circle", text = "Cyclic")   
         row.operator("curvetools2.operatororigintospline0start", text="First")                                                                                    

         row = box.row(1) 
         row.scale_y = 1.2  
         row.operator("tp_ops.curve_copies", text = "Copy")
         row.operator("curve.smoothspline", text ="Smooth")     
       
         box.separator()   
        
         row = box.row(1) 
         row.scale_y = 1.2  
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
                row.operator("object.sep_outline", text = "Sep-Outline")
            
             if len(vertex) == 2 and abs(selected[0] - selected[1]) == 1:
                 simple_divide = row.operator("curve.bezier_spline_divide", text='Spline Divide')
        
         box.separator()  

         box = col.box().column(1)  
         
         box.separator()  
         
         row = box.column(1) 
         row.scale_y = 1.2  
         row.operator("curvetools2.operatorintersectcurves", text = "Intersect Curves")
         row.prop(context.scene.curvetools, "LimitDistance", text = "LimitDistance")
        
         box.separator()                   
        
         box = col.box().column(1) 
                
         box.separator()  
                      
         row = box.row(align=0)
         row.scale_y = 1.2            
         row.prop(context.scene.curvetools, "IntersectCurvesAlgorithm", text = "Algorithm")

         row = box.row(align=0.1)
         row.scale_y = 1.2            
         row.prop(context.scene.curvetools, "IntersectCurvesMode", text = "Mode")

         row = box.row(align=0.1)
         row.scale_y = 1.2            
         row.prop(context.scene.curvetools, "IntersectCurvesAffect", text = "Affect")

         box.separator()                   
        
         box = col.box().column(1) 
                
         box.separator()  

         row = box.row(1) 
         row.scale_y = 1.2   
         row.operator("3dmish.copy", text ="Copy Loc", icon="COPYDOWN")
         row.operator("3dmish.paste", text ="Paste Loc", icon="PASTEDOWN")
               
     
         box.separator()  



class VIEW3D_TP_Curve_Edit_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Edit_Panel_TOOLS"
    bl_label = "Editing"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_edit_ui(self, context, layout)         


class VIEW3D_TP_Curve_Edit_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Edit_Panel_UI"
    bl_label = "Editing"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_edit_ui(self, context, layout) 

