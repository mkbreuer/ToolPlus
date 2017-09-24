import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


 # LOAD UIs #
from .ui_visual import draw_visual_layout


def draw_main_panel_layout(self, context, layout):

    icons = load_icons()     

    draw_visual_layout(self, context, layout)     


    display_history = context.user_preferences.addons[__package__].preferences.tab_history 
    if display_history == 'on':
        
        box = layout.box().column(1)  

        row = box.row(1)        
        #row.operator("screen.redo_last", text="", icon="COLLAPSEMENU") 
        row.operator('wm.path_open',  text = '', icon = 'COLLAPSEMENU').filepath = "C:\\Users\Public\Documents" 

        button_ruler = icons.get("icon_ruler")
        row.operator("view3d.ruler", text="Ruler", icon_value=button_ruler.icon_id)   
         
        row.operator("ed.undo_history", text="Log", icon="SCRIPTPLUGINS")

        row.operator("ed.undo", text="", icon="LOOP_BACK")  
        row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
       
        box.separator()   
            



class VIEW3D_TP_Visuals_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Visuals_Panel_TOOLS"
    bl_label = "Visuals"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_context = "objectmode"    
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        draw_main_panel_layout(self, context, layout)        
        


class VIEW3D_TP_Visuals_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Visuals_Panel_UI"
    bl_label = "Visuals"
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
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_main_panel_layout(self, context, layout) 


