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




def draw_add_taper_panel_layout(self, context, layout):

        icons = load_icons()
        my_button_one = icons.get("icon_image1")

        if context.mode == "OBJECT":

            box = layout.box().column(1)                         

            row = box.row(1)      
            row.label(text="Taper Bevel")

            row = box.row(1) 
            row.operator("curve.new_beveled_curve", icon_value=my_button_one.icon_id)
            
            row = box.row(1) 
            row.label(text="Edit Bevel:")

            row = box.row(1) 
            row.operator("curve.edit_bevel_curve", text="Edit")
            row.operator("curve.hide_bevel_objects", text="Hide")
            row.operator("curve.add_bevel_to_curve", text="Reset")

            row = box.row(1) 
            row.label(text="Convert to Mesh:")
           
            row = box.row(1)             
            row.operator("curve.convert_beveled_curve_to_meshes", text="Mesh(es)")
            row.operator("curve.convert_beveled_curve_to_separated_meshes", text="Merged")

            row = box.row(1)   
            row.operator("curve.convert_beveled_curve_to_merged_mesh", text="Separated")
            row.operator("curve.convert_beveled_curve_to_union_mesh", text="Union")

            box.separator()


        if context.mode =='EDIT_CURVE':
            
            box = layout.box().column(1)                         

            row = box.row(1)      
            row.label(text="Taper Bevel (Layer 19)")

            row = box.row(1) 
            row.operator("curve.finish_edit_bevel")
            row.operator("tp_ops.wire_all", text="", icon='WIRE')
           
            box.separator()




class VIEW3D_TP_Taper_Curve_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Taper_Curve_Panel_TOOLS"
    bl_label = "Taper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_add_taper_panel_layout(self, context, layout) 



class VIEW3D_TP_Taper_Curve_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Taper_Curve_Panel_UI"
    bl_label = "Taper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_add_taper_panel_layout(self, context, layout) 


# Registry               

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


