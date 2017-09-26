import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons

from toolplus_bounding.history_ui import draw_history_layout
from toolplus_bounding.main_ui import draw_panel_layout
from toolplus_bounding.visual_ui import draw_visual_layout


EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']




class VIEW3D_TP_BBOX_MESHES_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_BBOX_MESHES_TOOLS"
    bl_label = "Bounding"
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
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_bounding_panel_layout(context, layout) 



class VIEW3D_TP_BBOX_MESHES_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_BBOX_MESHES_UI"
    bl_label = "Bounding"
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
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_bounding_panel_layout(context, layout) 






def draw_bounding_panel_layout(context, layout):

    layout.operator_context = 'INVOKE_REGION_WIN'
                                              
    
    draw_panel_layout(context, layout)   


    display_visual = context.user_preferences.addons[__package__].preferences.tab_display_visual
    if display_visual == 'on':

        draw_visual_layout(context, layout)     


    display_history = context.user_preferences.addons[__package__].preferences.tab_display_history 
    if display_history == 'on':
        
        draw_history_layout(context, layout)     

