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


class VIEW3D_TP_Edit_Boolean_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Edit_Boolean_Panel_TOOLS"
    bl_label = "Boolean"
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

        draw_boolean_panel_layout(self, context, layout) 
     
          

class VIEW3D_TP_Edit_Boolean_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Edit_Boolean_Panel_UI"
    bl_label = "Boolean"
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

        draw_boolean_panel_layout(self, context, layout) 



def draw_boolean_panel_layout(self, context, layout):
    
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()

        if context.mode == "OBJECT":

            box = layout.box().column(1)                                                   

            row = box.column(1) 
            
            button_boolean_union = icons.get("icon_boolean_union")
            row.operator("btool.direct_union", text="Union", icon_value=button_boolean_union.icon_id)

            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.operator("btool.direct_intersect", text="Intersect", icon_value=button_boolean_intersect.icon_id)

            button_boolean_difference = icons.get("icon_boolean_difference")
            row.operator("btool.direct_difference", text="Difference", icon_value=button_boolean_difference.icon_id)
                        
            row.separator()  

            button_boolean_substract = icons.get("icon_boolean_substract")
            row.operator("btool.direct_subtract", icon_value=button_boolean_substract.icon_id)              

            button_boolean_rebool = icons.get("icon_boolean_rebool")
            row.operator("btool.direct_slice", "Slice Rebool", icon_value=button_boolean_rebool.icon_id)        

            Display_Optimize = context.user_preferences.addons[__package__].preferences.tab_optimize
            if Display_Optimize == 'on':  

                box.separator()         

                box = layout.box().column(1)   

                row = box.column(1) 
                
                button_origin_obm = icons.get("icon_origin_obm")
                row.operator("object.origin_set", "Set Origin", icon_value=button_origin_obm.icon_id).type='ORIGIN_GEOMETRY'
            
            box.separator()         

            box = layout.box().column(1)               

            row = box.column(1)   

            button_boolean_carver = icons.get("icon_boolean_carver")
            row.operator("object.carver", text="3d Carver", icon_value=button_boolean_carver.icon_id)

            box.separator()         
  


        if context.mode == "EDIT_MESH":


            box = layout.box().column(1)                     

            row = box.column(1)                        

            button_boolean_union = icons.get("icon_boolean_union")
            row.operator("tp_ops.bool_union", text="Union", icon_value=button_boolean_union.icon_id) 

            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.operator("tp_ops.bool_intersect",text="Intersect", icon_value=button_boolean_intersect.icon_id) 

            button_boolean_difference = icons.get("icon_boolean_difference")
            row.operator("tp_ops.bool_difference",text="Difference", icon_value=button_boolean_difference.icon_id)  

            box.separator()  

            box = layout.box().column(1)                     

            row = box.column(1)  

            button_boolean_weld = icons.get("icon_boolean_weld")
            row.operator("mesh.intersect", "Weld", icon_value=button_boolean_weld.icon_id).use_separate = False

            button_boolean_isolate = icons.get("icon_boolean_isolate")
            row.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).use_separate = True   
            
            box.separator()          
            
            row = box.row(1)           
            row.label("Planes")         

            button_axis_x = icons.get("icon_axis_x")
            row.operator("tp_ops.plane_x",text="", icon_value=button_axis_x.icon_id)      
          
            button_axis_y = icons.get("icon_axis_y")
            row.operator("tp_ops.plane_y",text="", icon_value=button_axis_y.icon_id)       

            button_axis_z = icons.get("icon_axis_z")
            row.operator("tp_ops.plane_z",text="", icon_value=button_axis_z.icon_id) 

            box.separator() 

            box = layout.box().column(1)                     

            row = box.row(1) 
            
            button_boolean_facemerge = icons.get("icon_boolean_facemerge")
            row.operator("bpt.boolean_2d_union", text= "2d Union", icon_value=button_boolean_facemerge.icon_id)        
            
            box.separator() 


            display_optimize = context.user_preferences.addons[__package__].preferences.tab_optimize
            if display_optimize == 'on':   

                box = layout.box().column(1)                          

                row = box.column(1)  
                
                button_select_link = icons.get("icon_select_link")
                row.operator("mesh.select_linked",text="Select Linked", icon_value=button_select_link.icon_id)

                button_remove_double = icons.get("icon_remove_double")
                row.operator("mesh.remove_doubles",text="Remove Doubles", icon_value=button_remove_double.icon_id)             

                row.operator("mesh.normals_make_consistent", text="Recalc. Normals", icon="SNAP_NORMAL")

                row.separator() 

                button_origin_edm = icons.get("icon_origin_edm")
                row.operator("tp_ops.origin_edm",text="Set Origin", icon_value=button_origin_edm.icon_id)
               
                box.separator()




