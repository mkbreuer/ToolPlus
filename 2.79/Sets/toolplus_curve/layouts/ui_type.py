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



# DRAW UI LAYOUT #

def draw_type_ui(self, context, layout):

    icons = load_icons()     
    my_button_one = icons.get("icon_image1")        
        
    col = layout.column(align=True) 
 
    if context.mode == 'EDIT_CURVE': 

         box = col.box().column(1) 

         box.separator()  
         
         row = box.row(1)
         row.alignment = 'CENTER'  
         row.label("Splines") 
         
         box.separator()
                   
         row = box.row(1)
         row.scale_y = 1.2   
         row.operator("curve.spline_type_set", "Poly").type = 'POLY'   
         row.operator("curve.spline_type_set", "Bezier").type = 'BEZIER'   
         row.operator("curve.spline_type_set", "Nurbs").type = 'NURBS'   

         box.separator()   
         box.separator()   

         row = box.row(1)
         row.scale_y = 1.2                 
         row.prop(context.active_object.data, "show_normal_face", text="Normals:")                          
         row.operator("curve.switch_direction", text="", icon="ARROW_LEFTRIGHT")  
       
         sub = row.row(1)
         sub.scale_x = 0.75
         sub.prop(context.scene.tool_settings, "normal_size", text=" ")

         box.separator()                   

         box = col.box().column(1)
 
         box.separator()  

         row = box.row(1)
         row.alignment = 'CENTER'  
         row.scale_y = 1.2   
         row.prop(context.active_object.data, "show_handles", text="Handles")

         box.separator() 
                 
         row = box.row(1)
         row.scale_y = 1.2   
         row.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
         row.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'
         
         row = box.row(1)
         row.scale_y = 1.2    
         row.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'
         row.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'

         box.separator()   


    else:
        
         box = col.box().column(1) 

         box.separator()  

         row = box.row(1) 
         row.alignment = 'CENTER' 
         row.label("Splines") 
         
         box.separator()
         
         row = box.row(1) 
         row.scale_y = 1.2    
         row.operator("curve.to_poly", text="Poly")
         row.operator("curve.to_bezier", text="Bezièr")
         row.operator("curve.to_nurbs", text="Nurbs")

         box.separator() 
         
         box = col.box().column(1) 

         box.separator()  

         row = box.row(1)
         row.alignment = 'CENTER' 
         row.label("Handles") 
         
         box.separator()
         
         row = box.row(1) 
         row.scale_y = 1.2                             
         row.operator("curve.handle_to_free", text="Free")                         
         row.operator("curve.handle_to_automatic", text="Auto")
         
         row = box.row(1) 
         row.scale_y = 1.2                                                   
         row.operator("curve.handle_to_vector", text="Vector") 
         row.operator("curve.handle_to_aligned", text="Aligned")

         box.separator() 




class VIEW3D_TP_Curve_Type_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Type_Panel_TOOLS"
    bl_label = "Type"
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
        layout = self.layout.column(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
    
        draw_type_ui(self, context, layout)    


class VIEW3D_TP_Curve_Type_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Type_Panel_UI"
    bl_label = "Type"
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
        layout = self.layout.column(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_type_ui(self, context, layout)           