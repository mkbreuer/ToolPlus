# ##### BEGIN GPL LICENSE BLOCK #####
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

import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons


# Object is a Canvas
def isCanvas(_obj):
    try:
        if _obj["BoolToolRoot"]:
            return True
    except:
        return False


# Object is a Brush Tool Bool
def isBrush(_obj):
    try:
        if _obj["BoolToolBrush"]:
            return True
    except:
        return False



EDIT = ["OBJECT", "EDIT_MESH"]
GEOM = ['MESH']

class VIEW3D_TP_BoolTool_Brush_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_BoolTool_Brush_TOOLS"
    bl_label = "Boolean BT"
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

        draw_bt_brush_panel_layout(self, context, layout) 
               

class VIEW3D_TP_BoolTool_Brush_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_BoolTool_Brush_UI"
    bl_label = "Boolean BT"
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

        draw_bt_brush_panel_layout(self, context, layout) 



def draw_bt_brush_panel_layout(self, context, layout):
     
    layout.operator_context = 'INVOKE_REGION_WIN'    

    icons = load_icons()    

    box = layout.box().column(1)


    if bpy.context.object.mode == "EDIT":
        
        row = box.column(1) 

        button_boolean_edge = icons.get("icon_boolean_edge")
        row.operator("object.boolean_bevel_custom_edge", text="Custom Edge", icon_value=button_boolean_edge.icon_id)
        
        button_boolean_bridge = icons.get("icon_boolean_bridge")
        row.operator("object.boolean_bevel_bridge", text="Bridge Edge", icon_value=button_boolean_bridge.icon_id)
        

    else:

        row = box.column(1) 
        
        button_boolean_union_brush = icons.get("icon_boolean_union_brush")
        row.operator("tp_ops.tboolean_union", text="BT-Union", icon_value=button_boolean_union_brush.icon_id)            
        
        button_boolean_intersect_brush = icons.get("icon_boolean_intersect_brush")
        row.operator("tp_ops.tboolean_inters", text="BT-Intersect", icon_value=button_boolean_intersect_brush.icon_id)
        
        button_boolean_difference_brush = icons.get("icon_boolean_difference_brush")
        row.operator("tp_ops.tboolean_diff", text="BT-Difference", icon_value=button_boolean_difference_brush.icon_id)
        
        row.separator()

        button_boolean_rebool_brush = icons.get("icon_boolean_rebool_brush")
        row.operator("tp_ops.tboolean_slice", text="BT-SliceRebool", icon_value=button_boolean_rebool_brush.icon_id)

        layout.operator_context = 'INVOKE_REGION_WIN'
        button_boolean_draw = icons.get("icon_boolean_draw")
        row.operator("tp_ops.draw_polybrush", text="BT-DrawPoly", icon_value=button_boolean_draw.icon_id)


        if (isCanvas(context.active_object)) or (isBrush(context.active_object)):

            row.separator()

            if 0 < len(bpy.context.selected_objects) < 2 and bpy.context.object.mode == "OBJECT":
                button_boolean_bevel = icons.get("icon_boolean_bevel")
                row.operator("object.boolean_bevel", text="Run BoolBevel", icon_value=button_boolean_bevel.icon_id)

                if bpy.data.objects.find('BOOLEAN_BEVEL_CURVE') != -1 and bpy.data.objects.find('BOOLEAN_BEVEL_GUIDE') != -1:
                    row.operator("object.boolean_custom_bevel", text="Custom BoolBevel", icon='MOD_BEVEL')
                
                row.operator("tp_ops.cleanup_boolbevel", text="Finish BoolBevel", icon='PANEL_CLOSE')

        row.separator()

