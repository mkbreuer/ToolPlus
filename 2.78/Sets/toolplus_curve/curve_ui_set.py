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



def draw_curve_set_panel_layout(self, context, layout):
        
         icons = load_icons() 
         my_button_one = icons.get("icon_image1")

         box = layout.box().column(1)   
         
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

             if context.object.data.splines.active.type == 'BEZIER':

                 row.label(text="Interpolation:")
                 row.active = (context.object.data.dimensions == '3D')
                 row.prop(context.object.data.splines.active, "tilt_interpolation", text="Tilt")
                 row.prop(context.object.data.splines.active, "radius_interpolation", text="Radius")
             
             row.prop(context.object.data.splines.active, "use_smooth")

         box.separator() 

         box = layout.box().column(1)   
         
         row = box.row(1)        
         row.prop(context.object.data, "use_path", text="Path Animation")

         row = box.column()
         row.prop(context.object.data, "path_duration", text="Frames")
         row.prop(context.object.data, "eval_time")

         # these are for paths only
         row = box.row()
         row.prop(context.object.data, "use_path_follow")

         ###
         box.separator() 

        


class VIEW3D_TP_Curve_Set_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_context = "objectmode"
    bl_idname = "VIEW3D_TP_Curve_Set_Panel_TOOLS"
    bl_label = "Setting"
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
         
         draw_curve_set_panel_layout(self, context, layout)



class VIEW3D_TP_Curve_Set_Panel_UI(bpy.types.Panel):
    bl_context = "objectmode"
    bl_idname = "VIEW3D_TP_Curve_Set_Panel_UI"
    bl_label = "Setting"
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
         
         draw_curve_set_panel_layout(self, context, layout)



# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


