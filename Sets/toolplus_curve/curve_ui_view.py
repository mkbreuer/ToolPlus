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




def draw_curve_view_panel_layout(self, context, layout):
    
        icons = load_icons()     
        my_button_one = icons.get("icon_image1")
        
        obj = context.active_object  
        
        box = layout.box().column(1)                                                           
  
        row = box.row(1)
        row.prop(context.space_data, "use_matcap", icon ="MATCAP_01")

        #if context.space_data.use_matcap:
        sub = row.row(1)
        sub.scale_y = 0.2
        sub.scale_x = 1.5
        sub.template_icon_view(context.space_data, "matcap_icon")

        
        row = box.row(1)                
        row.operator("object.toggle_silhouette", text="Silhouette", icon ="MATCAP_08") 
                            
        row.prop(context.space_data.fx_settings, "use_ssao", text="AOccl", icon="GROUP")

        if context.space_data.fx_settings.use_ssao:
            row = box.row(1)
            row.prop(context.space_data.fx_settings.ssao, "color","")
            row.prop(context.space_data.fx_settings.ssao, "factor")
            
            row = box.row(1)
            row.prop(context.space_data.fx_settings.ssao, "distance_max")
            row.prop(context.space_data.fx_settings.ssao, "attenuation")
            row.prop(context.space_data.fx_settings.ssao, "samples")
               

        box.separator()   
        box.separator()   

        row = box.row(1)
        row.prop(context.space_data, "show_only_render", text="Render", icon ="RESTRICT_RENDER_OFF")
        row.prop(context.space_data, "show_floor", text="Grid", icon ="GRID")     
        
        row = box.row(1)
        row.prop(context.space_data, "show_world", "World" ,icon ="WORLD")
        
        sub = row.row(1)
        sub.scale_x = 0.335
        sub.prop(context.space_data, "show_axis_x", text="X", toggle=True)
        sub.prop(context.space_data, "show_axis_y", text="Y", toggle=True)
        sub.prop(context.space_data, "show_axis_z", text="Z", toggle=True)

        if context.space_data.show_world:
            row = box.row(1)
            row.prop(context.scene.world, "horizon_color", "")
            
            row = box.row(1)
            row.prop(context.scene.world, "exposure")
            row.prop(context.scene.world, "color_range")

        box.separator() 


class VIEW3D_TP_Curve_View_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_View_Panel_TOOLS"
    bl_label = "View3D"
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
        return (isModelingMode)

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_curve_view_panel_layout(self, context, layout)


class VIEW3D_TP_Curve_View_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_View_Panel_UI"
    bl_label = "View3D"
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
        return (isModelingMode)

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'         

         draw_curve_view_panel_layout(self, context, layout)



# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


