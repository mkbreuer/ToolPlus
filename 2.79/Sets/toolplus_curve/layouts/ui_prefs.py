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


def draw_prefs_ui(self, context, layout):

    icons = load_icons()

    col = layout.column(1)  

    box = col.box().column(1)     
        
    box.separator()         
     
    row = box.column(1)
    row.scale_y = 1.2     
    row.prop(context.active_object, "name", text="Name")        
    row.prop(context.active_object.data, "name", text="Data")        

    box.separator() 

    obj = context.active_object
    if obj:
        obj_type = obj.type                
        if obj.type in {'CURVE', 'NURBS', 'SURFACE'}: 

            box = col.box().column(1) 
          
            box.separator()                     
          
            row = box.row(1)
            row.scale_y = 1.2     
            sub = row.row(1)
            sub.scale_x = 0.25           
            sub.prop(context.object.data, "dimensions", expand=True)    
            
            box.separator()  

    if context.mode == 'EDIT_CURVE':
                         
        row = box.row(1)
        row.scale_y = 1.2     
        row.operator("curvetools2.operatorcurveinfo", text = "Curve")                        
        row.operator("curvetools2.operatorsplinesinfo", text = "Splines")
        row.operator("curvetools2.operatorsegmentsinfo", text = "Segments")
         
        box.separator()  

    row = box.row(1) 
    row.scale_y = 1.2     
    row.operator("curvetools2.operatorselectioninfo", text = "Selected:")
    row.prop(context.scene.curvetools, "NrSelectedObjects", text = "")   


    if context.mode == 'EDIT_CURVE':

        row = box.row(1) 
        row.scale_y = 1.2     
        row.operator("curvetools2.operatorcurvelength", text = "Calc Length")
        row.prop(context.scene.curvetools, "CurveLength", text = "")    

    ###
    box.separator() 



class VIEW3D_TP_Curve_Prefs_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Info_Panel_TOOLS"
    bl_label = "Preferences"
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
         
        draw_prefs_ui(self, context, layout)


         
class VIEW3D_TP_Curve_Prefs_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Prefs_Info_Panel_UI"
    bl_label = "Preferences"
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
         
        draw_prefs_ui(self, context, layout)                              

