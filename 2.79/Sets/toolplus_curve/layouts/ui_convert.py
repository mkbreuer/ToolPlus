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


def draw_convert_ui(self, context, layout):

    tp_props = context.window_manager.tp_props_curve     
   
    icons = load_icons()     
    my_button_one = icons.get("icon_image1")
    
    col = layout.column(1)  

    obj = context.active_object
    if obj:
        obj_type = obj.type                
        if obj.type in {'CURVE', 'NURBS', 'SURFACE','TEXT','MBALL'}: 

             box = col.box().column(1)  
             
             box.separator() 
            
             row = box.column(1)                    
             row.scale_y = 1.2                    
             row.operator("object.convert",text="Convert to Mesh", icon = "OUTLINER_DATA_MESH").target="MESH"              
           
             box.separator() 
            
        else:

             box = col.box().column(1)  
            
             box.separator()             
             
             row = box.row(1)
             row.scale_y = 1.2       
 
             if tp_props.display_non_destructiv:   
                row.prop(tp_props, "display_non_destructiv", text="", icon="SCRIPTWIN")                
             else:
                row.prop(tp_props, "display_non_destructiv", text="", icon="SCRIPTWIN")      
             
             row.operator("object.convert", text="    Convert to Curve").target="CURVE"

             box.separator()    
   

             
             if tp_props.display_non_destructiv:                      
                
                 obj = context.active_object
                 if obj:
                     obj_type = obj.type                
                    
                     box.separator()                       
   
                     if obj.type in {'MESH'}: 
                         
                         row = box.row(1)                 
                         row.label("Linked Convert / Non Destructiv")
                         
                         row = box.row(1)
                         row.scale_y = 1.2       
                         row.label("CurveName:")
                         row.prop(context.object, "names");
                       
                         row = box.row(1)
                         row.scale_y = 1.2       
                         row.prop(context.object, "rscale", "CopyScale")
                         row.operator("mesh.convert_update")
                  
                     else:
                         
                         row = box.row(1)
                         row.label("Convert Non Destructiv:")
                        
                         row = box.row(1)
                         row.label("select Mesh Object", icon = "ERROR")

                     box.separator()               




class VIEW3D_TP_Curve_Convert_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Convert_Panel_TOOLS"
    bl_label = "Convert"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'         

        draw_convert_ui(self, context, layout)


class VIEW3D_TP_Curve_Convert_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Convert_Panel_UI"
    bl_label = "Convert"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'         

        draw_convert_ui(self, context, layout)


