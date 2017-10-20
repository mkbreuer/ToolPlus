43# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



def draw_curve_edit_panel_layout(self, context, layout):

        icons = load_icons()     
        my_button_one = icons.get("icon_image1")        

        if context.mode == 'EDIT_CURVE':
            
             box = layout.box().column(1) 

             row = box.column(1)
             #row.alignment = 'CENTER'  
             row.label("Set Spline Type", icon="IPO_BEZIER") 
             
             box.separator()
                       
             row = box.row(1)  
             row.operator("curve.spline_type_set", "Poly").type = 'POLY'   
             row.operator("curve.spline_type_set", "Bezier").type = 'BEZIER'   
             row.operator("curve.spline_type_set", "Nurbs").type = 'NURBS'   

             box.separator()   

             box = layout.box().column(1)
     
             row = box.row(1)
             #row.alignment = 'CENTER'  
             row.label("Curve Handle Type", icon='IPO_BEZIER') 

             box.separator() 
                     
             row = box.row(1)   
             row.operator("curve.handle_type_set", text="Auto", icon='BLANK1').type = 'AUTOMATIC'
             row.operator("curve.handle_type_set", text="Vector", icon='BLANK1').type = 'VECTOR'
             
             row = box.row(1)   
             row.operator("curve.handle_type_set", text="Align", icon='BLANK1').type = 'ALIGNED'
             row.operator("curve.handle_type_set", text="Free", icon='BLANK1').type = 'FREE_ALIGN'

             box.separator()  
                  
             box = layout.box().column(1) 

             row = box.column(1)                
             row.operator("curve.surfsk_first_points", text="Set First Points", icon = "FORCE_CURVE")                   
             row.operator("curve.switch_direction", text="Switch Direction", icon = "ARROW_LEFTRIGHT")                   
             row.operator("curve.cyclic_toggle","Open / Close Curve", icon="MOD_CURVE")  

             row = box.row(1)
             row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
             row.prop(context.object.data, "resolution_u", text="Resolution")
             row.operator("tp_ops.wire_all", text="", icon='WIRE') 

             box.separator()  

             box = layout.box().column(1)

             row = box.row(1)
             row.alignment = 'CENTER' 
             row.label("Subdivide")   
             
             row = box.row(1) 
             row.operator("curve.subdivide", text="1").number_cuts=1        
             row.operator("curve.subdivide", text="2").number_cuts=2
             row.operator("curve.subdivide", text="3").number_cuts=3
             row.operator("curve.subdivide", text="4").number_cuts=4
             row.operator("curve.subdivide", text="5").number_cuts=5        
             row.operator("curve.subdivide", text="6").number_cuts=6  

             box.separator() 
            

             box = layout.box().column(1)
             
             row = box.row(1)  
             row.operator("curve.extrude_move", text="Extrude")
             row.operator("curve.make_segment",  text="Weld") 
       
             row = box.row(1) 
             row.operator("transform.tilt", text="Tilt")                                     
             row.operator("curve.radius_set", "Radius")                 
               
             row = box.row(1)                   
             row.operator("transform.vertex_random") 
             row.operator("curve.smooth_x_times", text="Smooth")

             box.separator() 

             row = box.row(1) 
             row.operator("curve.separate",  text="Separate") 
             row.operator("object.curve_outline", text = "Outline")            
            
             row = box.row(1)               
             row.operator("curve.split",  text="Split")   
             row.operator("curve.trim_tool", text="Trim")                
       
             row = box.row(1)
             row.operator("curve.remove_doubles", text="Rem. Doubles")  
             row.operator("tp_ops.curve_copies", text = "Copy")                                      


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

                 if len(vertex) > 0 and n > 2:
                     simple_edit = row.operator("curve.bezier_points_fillet", text='Fillet')
                
                 #if len(vertex) == 2 and abs(selected[0] - selected[1]) == 1:
                     #simple_divide = row.operator("curve.bezier_spline_divide", text='Divide')                 
                 
                 if len(vertex) > 0 and n > 2:
                    row.operator("curve.extend_tool", text="Extend")

                 if len(vertex) == 2:
                     box.separator() 
                     row = box.row(1)   
                     simple_edit = row.operator("tp_ops.quader_curve","Beveled Quarter")   

                 if len(vertex) == 1:
                     box.separator() 
                     row = box.row(1)
                     simple_edit = row.operator("tp_ops.half_curve","Beveled Half-Circle")               
              

             box.separator()                   


        else:
            
             box = layout.box().column(1)   

             row = box.row(1)
             sub = row.row(1)
             sub.scale_x = 7
             sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
             sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
             sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
             sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
             sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")  
             row.operator("purge.unused_curve_data", "", icon = "PANEL_CLOSE") 

             box = layout.box().column(1) 

             row = box.column(1) 
             row.label("Curve Type", icon="MOD_CURVE") 
             
             box.separator()
             
             row = box.row(1)
             row.operator("curve.to_poly","Poly")
             row.operator("curve.to_bezier","Bezièr")
             row.operator("curve.to_nurbs","Nurbs")

             box.separator() 
             
             box = layout.box().column(1) 

             row = box.column(1)
             row.label("Handle Type", icon="IPO_BEZIER") 
             
             box.separator()
             row = box.row(1)                            
             row.operator("curve.handle_to_free","Free")                         
             row.operator("curve.handle_to_automatic","Auto")
             
             row = box.row(1)                                                   
             row.operator("curve.handle_to_vector","Vector") 
             row.operator("curve.handle_to_aligned","Aligned")

             box.separator() 

             box = layout.box().column(1)   
             
             row = box.column(1)
             row.operator("curvetools2.operatororigintospline0start", text="FirstPoint", icon = "FORCE_CURVE")         
             row.operator("curve.open_circle", text = "Open / Close", icon = "MOD_CURVE")                                                                              
             row.operator("curve.smoothspline", "Smooth Curve", icon ="SMOOTHCURVE")                

             box = layout.box().column(1)  
            
             row = box.row(1)
             row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
             row.prop(context.object.data, "resolution_u", text="Resolution")                         

             active_wire = bpy.context.object.show_wire 
             if active_wire == True:
                row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
             else:                       
                 row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 


             box = layout.box().column(1)  
              
             row = box.row(1) 
             row.scale_y = 1.5                  
             row.operator("curvetools2.create_auto_loft", text = "Loft")
             row.operator("curvetools2.operatorsweepcurves", text = "Sweep")  
             row.operator("curvetools2.operatorbirail", text = "Birail")  

             box.separator() 

             row = box.row(1)              
             row.prop(context.window_manager, "auto_loft", toggle=True)             

             row = box.column_flow(2)              
             scene = context.scene
             lofters = [o for o in scene.objects if "autoloft" in o.keys()]
             for o in lofters:
                 row.label(o.name)
             
             box = layout.box().column(1)  
            
             row = box.row(1)
             row.operator("tp_ops.curve_copies", text = "Copy")
             row.operator("object.curve_outline", text = "Outline")
             
             row = box.column(1)
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
                    row.operator("object.sep_outline", text = "Separate Outline")
                
                 if len(vertex) == 2 and abs(selected[0] - selected[1]) == 1:
                     simple_divide = row.operator("curve.bezier_spline_divide", text='Spline Divide')

             box = layout.box().column(1)  

             row = box.row(1)
             row.operator("curvetools2.operatorintersectcurves", text = "Intersect Curves")
             row = box.row(1)
             row.prop(context.scene.curvetools, "LimitDistance", text = "LimitDistance")
                     
             box = layout.box().column(1) 
            
             row = box.row(align=0)
             row.prop(context.scene.curvetools, "IntersectCurvesAlgorithm", text = "Algorithm")

             row = box.row(align=0.1)
             row.prop(context.scene.curvetools, "IntersectCurvesMode", text = "Mode")

             row = box.row(align=0.1)
             row.prop(context.scene.curvetools, "IntersectCurvesAffect", text = "Affect")

             box.separator()               

             box = layout.box().column(1)  
           
             row = box.row(1)    
             #row.operator("3dmish.paste_mirror", text="PMirror", icon="PASTEFLIPDOWN")
             row.operator("tp_origin.align_tools", "Advance Align", icon="ALIGN")  

             row = box.row(1)    
             row.operator("3dmish.copy", icon="COPYDOWN")
             row.operator("3dmish.paste", icon="PASTEDOWN")
           

            
             box.separator() 

        
        box = layout.box().column(1)  
       
        row = box.row(1)        
        row.operator("view3d.ruler", text="Ruler")   
         
        row.operator("ed.undo_history", text="History")
        row.operator("ed.undo", text="", icon="LOOP_BACK")
        row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 

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

         draw_curve_edit_panel_layout(self, context, layout)         


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

         draw_curve_edit_panel_layout(self, context, layout) 





# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


