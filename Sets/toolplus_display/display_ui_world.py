import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
    


class ToolPlus_Sharpen_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Shade / UVs"
    bl_idname = "ToolPlus_Sharpen_Panel_TOOLS"
    bl_label = "Sharpen"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode 
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_AREA'

        draw_flymode_panel_layout(self, context, layout) 



class ToolPlus_Sharpen_Panel_UI(bpy.types.Panel):
    bl_idname = "ToolPlus_Sharpen_Panel_UI"
    bl_label = "Sharpen"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode 

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_AREA'

        draw_flymode_panel_layout(self, context, layout) 



def draw_flymode_panel_layout(self, context, layout):
    icons = load_icons()

    box = layout.box().column(1)    

    row = box.row(1).column_flow(2)
    row.label("Mark Sharp") 
    row.operator("mesh.mark_sharp", text="Edges", icon='SNAP_EDGE').use_verts = True  
    row.operator("mesh.mark_sharp", text="Vertices", icon='SNAP_VERTEX').use_verts = True          
    
    row.label("Clear Sharp")  
    row.operator("mesh.mark_sharp", text="", icon='X').clear = True
    props = row.operator("mesh.mark_sharp", text="", icon='X')
    props.use_verts = True
    props.clear = True

    box.separator()   
        



                                   
