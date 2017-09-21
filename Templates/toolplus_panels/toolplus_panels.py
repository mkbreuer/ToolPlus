__status__ = "toolplus"
__author__ = "MKB"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


def draw_panel_layout(self, context, layout):
    
    icons = load_icons()
    
    tp = context.window_manager.tp_collapse_template


    box = layout.box().column(1) 
    
    row = box.row(1)  
    sub = row.row(1)
    sub.scale_x = 7

    sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
    sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
    sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
    sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
    sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")  

    box = layout.box().column(1)  

    # Custom A
    display_custom_a = context.user_preferences.addons[__package__].preferences.tab_panel_custom_a
    if display_custom_a == 'on':  

        row = box.row(1)
        button_custom_a = icons.get("icon_custom_a")
        row.label(text="Custom A", icon_value=button_custom_a.icon_id)  


    # Custom B
    display_custom_b = context.user_preferences.addons[__package__].preferences.tab_panel_custom_b
    if display_custom_b == 'on':  

        row = box.row(1)
        button_custom_b = icons.get("icon_custom_b")
        row.label(text="Custom B", icon_value=button_custom_b.icon_id)  

    box.separator()
    
    row = box.row(1)
    
    obj = context.active_object
    if obj:
        obj_type = obj.type
        
        if obj.type in {'MESH'}:                

            if tp.display_collapse:                     
                                         
                row.prop(tp, "display_collapse", text="Collapse", icon ="TRIA_DOWN")                     
               
                #Split Operator
                #row.label(text="Collapse", icon ="INFO")
          
            else:
                            
                row.prop(tp, "display_collapse", text="Collapse", icon ="TRIA_RIGHT")
                
                #Split Operator
                #row.label(text="Collapse", icon ="INFO")

            if tp.display_collapse: 
                
                box = layout.box().column(1) 

                row = box.row(1)     

                row.label(text="Custom Settings", icon ="PLUGIN") 
                
                box.separator()
                
                box = layout.box().column(1)  



    display_history = context.user_preferences.addons[__package__].preferences.tab_panel_history
    if display_history == 'on':

        row = box.row(1)          
        row.operator("ed.undo", text="Undo", icon="LOOP_BACK")
        row.operator("ed.redo", text="Redo", icon="LOOP_FORWARDS") 
       
        box.separator()   
        
        



# Tools Shelf [T]
class VIEW3D_TP_Template_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Template_Panel_TOOLS"
    bl_label = "T+ Panel"
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
        return isModelingMode
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_panel_layout(self, context, layout) 


# Property Shelf [N]
class VIEW3D_TP_Template_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Template_Panel_UI"
    bl_label = "T+ Panel"
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
        return isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_panel_layout(self, context, layout) 


# Properties Editor TAB: Object 
class VIEW3D_TP_Template_Panel_PROPS(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Template_Panel_PROPS"
    bl_label = "T+ Panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object" #TAB
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_panel_layout(self, context, layout) 
