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


def draw_custom_ui(self, context, layout):
    
        # needed for icon load
        icons = load_icons()     
        
        # display functions in a box 
        box = layout.box().column(align=True) 
         
       
        row = box.row(align=True) # align functions in a raw 
     
        my_button_1 = icons.get("icon_custom_1")
        row.label(text="", icon_value = my_button_1.icon_id) # display only custom icon    
    
        row.label("< Custom Icon") # display text      
        row.operator("tp_ops.help_curve_custom",text="", icon = "INFO") # display only default icon        
        
        row = box.column(align=True) # align functions in a column 
        
        row.label("open layout script") # display only text
        row.label("to add new functions") # display only text

        box.separator() # add emtpy space in between        
        
        col = box.column(align=True) # align functions in a column         
        

        col.operator("tp_ops.keymap_curve_custom", text="Script to Text Editor", icon= "SCRIPT") # functions with custom icon



        # col.separator() # add emtpy space in between   
        
        # each new icon need a 'get' assignation  
             
        # my_button_2 = icons.get("icon_custom_2")
        # col.operator("view3d.view_all", text="", icon_value = my_button_2.icon_id).center=True

        # my_button_3 = icons.get("icon_custom_3")
        # col.operator("view3d.view_all", text="", icon_value = my_button_3.icon_id).center=True

        # col.separator() # add emtpy space in between   

        # my_button_4 = icons.get("icon_custom_4")
        # col.operator("view3d.view_all", text="", icon_value = my_button_4.icon_id).center=True

        box.separator() # add emtpy space in between   


class VIEW3D_TP_Custom_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Custom_Panel_TOOLS"
    bl_label = "Custom"
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

         draw_custom_ui(self, context, layout)


class VIEW3D_TP_Custom_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Custom_Panel_UI"
    bl_label = "Custom"
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

         draw_custom_ui(self, context, layout)



