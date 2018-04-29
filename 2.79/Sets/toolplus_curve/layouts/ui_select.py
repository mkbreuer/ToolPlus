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


def draw_select_ui(self, context, layout):
 
    icons = load_icons()

    col = layout.column(1)  

    box = col.box().column(1)     
        
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


EDIT = ["EDIT_CURVE", "EDIT_SURFACE"]
GEOM = ['CURVE']

class VIEW3D_TP_Curve_Select_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Select_Panel_TOOLS"
    bl_label = "Select"
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
        layout = self.layout

        draw_select_ui(self, context, layout)
        
                
                 
class VIEW3D_TP_Curve_Select_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Select_Panel_UI"
    bl_label = "Select"
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
        layout = self.layout    
       
        draw_select_ui(self, context, layout)
