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


def draw_bevel_ui(self, context, layout):
    
    tp_props = context.window_manager.tp_props_curve 
   
    icons = load_icons()       
    my_button_one = icons.get("icon_image1")
   
    col = layout.column(1)    
    
    if context.mode == 'EDIT_CURVE':

         box = col.box().column(1)
         
         box.separator()  
         
         row = box.row(1)
         row.alignment = 'CENTER' 
         row.label("Bevel Properties") 
         
         box.separator()           
         
         row = box.row(1)        
         row.scale_y = 1    
         row.prop(context.object.data, "fill_mode", text="")                        
         
         button_curve_extrude = icons.get("icon_curve_extrude")     
         row.operator("tp_ops.curve_extrude", text="2d", icon_value=button_curve_extrude.icon_id)    
          
         active_bevel = bpy.context.object.data.bevel_depth            
         if active_bevel == 0.0:              
            row.operator("tp_ops.enable_bevel", text="on", icon='MOD_WARP')
         else:   
            row.operator("tp_ops.enable_bevel", text="off", icon='MOD_WARP')  
         
         box.separator()      
         box.separator()      
         
         row = box.row(1)
         row.scale_y = 1.3     
         active_wire = bpy.context.object.show_wire 
         if active_wire == True:
            row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
         else:                       
             row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 
         row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
         row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  

         
         row = box.row(1)
         row.scale_y = 1.3     
         row.prop(context.object.data, "resolution_u", text="Rings")          
         row.prop(context.object.data, "bevel_resolution", text="Loops")

         row = box.row(1)
         row.scale_y = 1.3     
         row.prop(context.object.data, "offset")
         row.prop(context.object.data, "extrude","Height") 
              
         act_spline = context.object.data.splines.active 
         if act_spline:

             show = bpy.context.object.data.dimensions
             if show == '3D': 
             
                 data = context.active_object.data
                 points = data.splines.active.bezier_points
                 selected_points = [idx for idx, p in enumerate(points) if p.select_control_point]

                 if len(selected_points) == 1:
                     idx = selected_points[0]
                     point = points[idx]

                     row = box.row(1) 
                     row.scale_y = 1.3  
                     row.prop(context.object.data, "twist_smooth", text="Twist")      
                     row.prop(point, "tilt", text='Tilt')

                     row = box.row(1)  
                     #row.active = (context.object.data.dimensions == '2D' or (context.object.data.bevel_object is None and context.object.data.dimensions == '3D'))
                     row.prop(context.object.data,"twist_mode", text="")
                     act_spline = context.object.data.splines.active 
                     row.prop(act_spline, "tilt_interpolation", text="")  

                 
                 else:
                     row = box.row(1) 
                     row.prop(context.object.data,"twist_mode", text="")  
                     row.prop(context.object.data, "twist_smooth", text="Twist")      


             data = context.active_object.data
             points = data.splines.active.bezier_points
             selected_points = [idx for idx, p in enumerate(points) if p.select_control_point]
             if len(selected_points) == 1:
                 idx = selected_points[0]
                 point = points[idx]
                 
                 box.separator()
                 
                 row = box.column(1) 
                 row.scale_y = 1.3              
                 row.label("1-Point")
                 row.prop(point, "weight_softbody", text='Weight')
                 row.prop(point, "radius", text='Radius')


        
         box.separator()  

         row = box.row(1) 
         row.label("Resolution")   

         if not tp_props.display_bevel_reso:                                 
            row.prop(tp_props, "display_bevel_reso", text="", icon='SCRIPTWIN')                 
         else:                 
            row.prop(tp_props, "display_bevel_reso", text="", icon='SCRIPTWIN')        
            
            box.separator() 

            row = box.column_flow(2)
            row.label("Rings")  
            row.label("1 = 4",) 
            row.label("2 = 8") 
            row.label("4 = 16") 
            row.label("8 = 32")
            row.label("(+4) Circle")          

            row.label("Loops")  
            row.label("0 = 4",) 
            row.label("2 = 8") 
            row.label("4 = 12") 
            row.label("8 = 16")           
            row.label("(+2) Along")   
                        
         
         box.separator()  


         box = col.box().column(1)

         box.separator()  
         
         row = box.row(1)  
         row.scale_y = 1.2     
         row.label(text="Taper:")
         row.prop(context.object.data, "taper_object", text="")
         
         row = box.row(1) 
         row.scale_y = 1.2     
         row.label(text="Bevel:")
         row.prop(context.object.data, "bevel_object", text="")

         box.separator() 
         
         

         box = col.box().column(1)

         box.separator()

         row = box.row(1)              
         row.alignment = 'CENTER'         
         
         act_spline = context.object.data.splines.active 
         if act_spline:                    
             if context.object.data.splines.active.use_cyclic_u == True:
                button_curve_open = icons.get("icon_curve_open") 
                ico_value=button_curve_open
             else:
                button_curve_close = icons.get("icon_curve_close") 
                ico_value=button_curve_close
             row.prop(context.object.data.splines.active, "use_cyclic_u", text="", icon_value=ico_value.icon_id)                       
         
         row.label("Bevel Factor")    
        
         box.separator()
       
         row = box.row(1)              
         row.prop(context.object.data, "bevel_factor_start", text="Curve Start") 

         sub = row.row(1)
         sub.scale_x = 0.35
         sub.alignment = 'RIGHT'  
         sub.prop(context.object.data, "bevel_factor_mapping_start", text="")

         row = box.row(1) 
         row.prop(context.object.data, "bevel_factor_end", text="Curve End")  

         sub = row.row(1)
         sub.scale_x = 0.35
         sub.alignment = 'RIGHT'  
         sub.prop(context.object.data, "bevel_factor_mapping_end", text="")
                  
         box.separator() 

         row = box.row(1)                      
         row.prop(context.object.data, "use_map_taper")
         row.prop(context.object.data, "use_fill_caps")

         box.separator()  


         box = col.box().column(1)

         box.separator()  

         row = box.row(1) 
         row.alignment = 'CENTER'
         row.label(text="Fill / Path / Deform")

         box.separator()  

         row = box.column(1)                          
         row.scale_y = 1.2     
         row.prop(context.object.data, "use_fill_deform")  
         row.prop(context.object.data, "use_deform_bounds")

         row = box.row(1)
         row.scale_y = 1.2     
         row.prop(context.object.data, "use_radius")
         row.prop(context.object.data, "use_stretch")

         box.separator()   

    else:  
                  
         box = col.box().column(1)   
        
         box.separator()  
         
         row = box.row(1)
         row.alignment = 'CENTER' 
         row.label("Bevel Properties") 
         
         box.separator()         
         row = box.row(1)        
         row.scale_y = 1   
         row.prop(context.object.data, "fill_mode", text="")           

         active_bevel = bpy.context.object.data.bevel_depth            
         if active_bevel == 0.0:              
            row.operator("tp_ops.enable_bevel", text="Bevel on", icon='MOD_WARP')
         else:   
            row.operator("tp_ops.enable_bevel", text="Bevel off", icon='MOD_WARP')                 
                  

         box.separator() 
         box.separator()  
                  
         row = box.row(1) 
         row.scale_y = 1.3     
         row.operator("dynamic.normalize", text="", icon='KEYTYPE_BREAKDOWN_VEC')   

         row.prop(context.object.data, "bevel_depth", text="Bevel Radius")

         active_wire = bpy.context.object.show_wire          
         if active_wire == True:
            row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
         else:                       
             row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 
                     
         row = box.row(1)
         row.scale_y = 1.3     
         row.prop(context.object.data, "resolution_u", text="Rings")          
         row.prop(context.object.data, "bevel_resolution", text="Loops")

         row = box.row(1)
         row.scale_y = 1.3     
         row.prop(context.object.data, "offset")
         row.prop(context.object.data, "extrude","Height")
        
         show = bpy.context.object.data.dimensions
         if show == '3D': 

             row = box.row(1) 
             row.scale_y = 1    
             #row.active = (context.object.data.dimensions == '2D' or (context.object.data.bevel_object is None and context.object.data.dimensions == '3D'))
             row.prop(context.object.data,"twist_mode", text="")
             row.prop(context.object.data, "twist_smooth", text="Twist")
          
         box.separator()  

         row = box.row(1) 
         row.label("Resolution")   

         if not tp_props.display_bevel_reso:                                 
            row.prop(tp_props, "display_bevel_reso", text="", icon='SCRIPTWIN')                 
         else:                 
            row.prop(tp_props, "display_bevel_reso", text="", icon='SCRIPTWIN')        
            
            box.separator() 

            row = box.column_flow(2)
            row.label("Rings")  
            row.label("1 = 4",) 
            row.label("2 = 8") 
            row.label("4 = 16") 
            row.label("8 = 32")
            row.label("(+4) Circle")          

            row.label("Loops")  
            row.label("0 = 4",) 
            row.label("2 = 8") 
            row.label("4 = 12") 
            row.label("8 = 16")           
            row.label("(+2) Along") 


         box.separator() 


         box = col.box().column(1)

         box.separator()

         row = box.row(1)              
         row.alignment = 'CENTER'
         row.label("Bevel & Taper")    
        
         box.separator()
          
         row = box.row(1)
         row.scale_y = 1             
         #row.operator("curve.tapercurve", "", icon = "CURVE_BEZCURVE") 
         row.operator("curve.tapercurve", "C-Taper", icon = "CURVE_BEZCURVE") 
         row.prop(context.object.data, "taper_object", text = "")

         row = box.row(1)
         row.scale_y = 1    
         #row.operator("curve.bevelcurve", "", icon = "CURVE_BEZCIRCLE") 
         row.operator("tp_ops.curves_galore", "C-Bevel", icon = "CURVE_BEZCIRCLE") 
         row.prop(context.object.data, "bevel_object", text = "")
 
         box.separator() 
         
         box = col.box().column(1)

         box.separator()

         row = box.row(1)              
         row.alignment = 'CENTER'

         act_spline = context.object.data.splines.active 
         if act_spline:      
             if context.object.data.splines.active.use_cyclic_u == True:
                button_curve_open = icons.get("icon_curve_open") 
                ico_value=button_curve_open
             else:
                button_curve_close = icons.get("icon_curve_close") 
                ico_value=button_curve_close
             row.prop(context.object.data.splines.active, "use_cyclic_u", text="", icon_value=ico_value.icon_id)     
      
         row.label("Bevel Factor")    
        
         box.separator()
       
         row = box.row(1)              
         row.prop(context.object.data, "bevel_factor_start", text="Curve Start") 

         sub = row.row(1)
         sub.scale_x = 0.35
         sub.alignment = 'RIGHT'  
         sub.prop(context.object.data, "bevel_factor_mapping_start", text="")

         row = box.row(1) 
         row.prop(context.object.data, "bevel_factor_end", text="Curve End")  

         sub = row.row(1)
         sub.scale_x = 0.35
         sub.alignment = 'RIGHT'  
         sub.prop(context.object.data, "bevel_factor_mapping_end", text="")
                  
         box.separator() 

         row = box.row(1)                      
         row.prop(context.object.data, "use_map_taper")
         row.prop(context.object.data, "use_fill_caps")

         box.separator() 


         box = col.box().column(1)  

         box.separator()

         row = box.row(1) 
         row.alignment = 'CENTER'
         row.label(text="Fill / Path / Deform")

         row = box.column(1)                          
         row.scale_y = 1.2     
         row.prop(context.object.data, "use_fill_deform")  
         row.prop(context.object.data, "use_deform_bounds")

         row = box.row(1)
         row.scale_y = 1.2     
         row.prop(context.object.data, "use_radius")
         row.prop(context.object.data, "use_stretch")
         


         ###
         box.separator()                                    
 




class VIEW3D_TP_Curve_Bevel_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Bevel_Panel_TOOLS"
    bl_label = "Bevel"
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

         draw_bevel_ui(self, context, layout)



class VIEW3D_TP_Curve_Bevel_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Bevel_Panel_UI"
    bl_label = "Bevel"
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
         
         draw_bevel_ui(self, context, layout)


