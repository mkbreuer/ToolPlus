__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


def draw_align_relax_tools_panel_layout(self, context, layout):
        tp = context.window_manager.tp_align_looptools
        
        icons = load_icons()

        box = layout.box().column(1)    

        row = box.column(1)                      
 
        button_align_vertices = icons.get("icon_align_vertices") 
        row.operator("mesh.vertices_smooth","Vertices", icon_value=button_align_vertices.icon_id) 

        button_align_laplacian = icons.get("icon_align_laplacian")
        row.operator("mesh.vertices_smooth_laplacian","Laplacian", icon_value=button_align_laplacian.icon_id)  

        button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
        row.operator("mesh.shrinkwrap_smooth","Shrinkwrap", icon_value=button_align_shrinkwrap.icon_id)         

        box.separator()   

        row = box.row(1)              

        button_align_planar = icons.get("icon_align_planar")  
        row.operator("mesh.face_make_planar", "Planar Faces", icon_value=button_align_planar.icon_id) 

        box.separator()    
                     
        row = box.row(1)                 
                     
        # relax - first line
        split = row.split(percentage=0.15, align=True)
        if tp.display_relax:
            button_align_looptools = icons.get("icon_align_looptools")
            split.prop(tp, "display_relax", text="", icon_value=button_align_looptools.icon_id)
            split.operator("mesh.looptools_relax", text="  LoopTool Relax")

        else:
            button_align_looptools = icons.get("icon_align_looptools")
            split.prop(tp, "display_relax", text="", icon_value=button_align_looptools.icon_id)
            split.operator("mesh.looptools_relax", text="  LoopTool Relax")

        # relax - settings
        if tp.display_relax:
            box = layout.box().column(1)    
             
            row = box.column(1)  
            row.prop(tp, "relax_interpolation")
            row.prop(tp, "relax_input")
            row.prop(tp, "relax_iterations")
            row.prop(tp, "relax_regular")

        ###
        box.separator()    


        Display_History = context.user_preferences.addons[__package__].preferences.tab_history_relax 
        if Display_History == 'on':
            
            box = layout.box().column(1)  

            row = box.row(1)    
                
            button_ruler_triangle = icons.get("icon_ruler_triangle") 
            row.operator("view3d.ruler", text="Ruler", icon_value=button_ruler_triangle.icon_id)   
             
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
           
            box.separator()  




class VIEW3D_TP_Align_Relax_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Align"
    bl_idname = "VIEW3D_TP_Align_Relax_Panel_TOOLS"
    bl_label = "Relax"
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
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        #layout.operator_context = 'INVOKE_AREA'

        draw_align_relax_tools_panel_layout(self, context, layout) 



class VIEW3D_TP_Align_Relax_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Align_Relax_Panel_UI"
    bl_label = "Relax"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        #layout.operator_context = 'INVOKE_AREA'

        draw_align_relax_tools_panel_layout(self, context, layout) 


