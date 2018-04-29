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



def draw_taper_ui(self, context, layout):
    
    tp_props = context.window_manager.tp_props_curve 
   
    icons = load_icons()       
    my_button_one = icons.get("icon_image1")
   
    col = layout.column(1)

    if context.mode == "OBJECT":

        box = layout.box().column(1)                         

        box.separator()  
        
        row = box.row(1)      
        row.scale_y = 1.2   
        row.operator("curve.new_beveled_curve", icon="BLANK1")

        box.separator()  
        box.separator()  
        
        row = box.row(1) 
        row.scale_y = 1.2    
        row.operator("curve.edit_bevel_curve", text="Edit")
        row.operator("curve.hide_bevel_objects", text="Hide")
        row.operator("curve.add_bevel_to_curve", text="Reset")
        
        box.separator()  
        box.separator()  
        
        row = box.row(1)
        row.alignment = "CENTER"          
        row.label(text="Convert to Mesh:")             
      
        box.separator()  
      
        row = box.row(1) 
        row.scale_y = 1.2    
        row.operator("curve.convert_beveled_curve_to_meshes", text="Mesh(es)")
        row.operator("curve.convert_beveled_curve_to_separated_meshes", text="Merged")  

        row = box.row(1) 
        row.scale_y = 1.2    
        row.operator("curve.convert_beveled_curve_to_merged_mesh", text="Separated")
        row.operator("curve.convert_beveled_curve_to_union_mesh", text="Union")

        box.separator()

    if context.mode =='EDIT_CURVE':
        
        box = layout.box().column(1)                         
        
        box.separator()

        row = box.row(1) 
        row.scale_y = 1.2  
        row.operator("curve.finish_edit_bevel")
        active_wire = bpy.context.object.show_wire 
        if active_wire == True:
            row.operator("tp_ops.wire_all", "", icon = 'MESH_PLANE')              
        else:                       
             row.operator("tp_ops.wire_all", "", icon = 'MESH_GRID') 
       
        box.separator()




# LOAD UI: PANEL #

EDIT = ["OBJECT", "EDIT_CURVE"]
GEOM = ['CURVE', 'SURFACE']


class VIEW3D_TP_Curve_Taper_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Taper_Panel_TOOLS"
    bl_label = "Taper"
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
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT


    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_taper_ui(self, context, layout)



class VIEW3D_TP_Curve_Taper_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Taper_Panel_UI"
    bl_label = "Taper"
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
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
         layout = self.layout.column_flow(1)  
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_taper_ui(self, context, layout)

