import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
    

EDIT = ["EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['SURFACE','META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

class VIEW3D_TP_Normals_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Shade / UVs"
    bl_idname = "VIEW3D_TP_Normals_Panel_TOOLS"
    bl_label = "Normals"
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
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT


    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_normals_panel_layout(self, context, layout) 



class VIEW3D_TP_Normals_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Normals_Panel_UI"
    bl_label = "Normals"
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
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_AREA'

        draw_normals_panel_layout(self, context, layout) 




def draw_normals_panel_layout(self, context, layout):
    icons = load_icons()
    
    box = layout.box().column(1) 

    if context.mode == 'OBJECT':

        row = box.column(1)
        row.operator("tp_ops.rec_normals", "Recalculate Normals", icon="SNAP_NORMAL")
       
        row.separator() 
       
        row.operator("tp_ops.editnormals_transfer",text="Transfer Normals", icon="SNAP_NORMAL")  
        row.operator("tp_ops.calculate_weighted_normals", "Weighted Normals", icon="SNAP_NORMAL")   

        box.separator()  

    
    if context.mode == 'EDIT_MESH':

        row = box.row(1)
        row.alignment = "CENTER"
        row.label("Display Normals", icon="RESTRICT_VIEW_OFF")
        
        box.separator()            
        
        row = box.row(1)
        row.prop(context.active_object.data, "show_normal_vertex", text="Vertex", icon='VERTEXSEL')
        row.prop(context.active_object.data, "show_normal_loop", text="Loop", icon='LOOPSEL')
        row.prop(context.active_object.data, "show_normal_face", text="Face", icon='FACESEL')
        
        row = box.row(1)             
        row.active = context.active_object.data.show_normal_vertex or context.active_object.data.show_normal_face
        row.prop(context.scene.tool_settings, "normal_size", text="Size")        

        box.separator()  


        box = layout.box().column(1) 

        row = box.column(1)
        row.operator("mesh.normals_make_consistent",text="Recalculate Normals", icon='SNAP_NORMAL')

        row = box.row(1)        
        row.operator("mesh.normals_make_consistent", text="Outside", icon = "FRAME_PREV").inside = False  
        row.operator("mesh.normals_make_consistent", text="Inside", icon = "FRAME_NEXT").inside = True                   
        row.operator("mesh.flip_normals", text="Flip", icon = "FILE_REFRESH")    

        box.separator() 
         
        row = box.column(1)
        row.operator("mesh.select_similar",text="Select Similar Normals", icon='RESTRICT_SELECT_OFF').type='NORMAL'

        box.separator() 


    if context.mode == 'EDIT_CURVE':
        
        row = box.column(1)
        row.operator("curve.normals_make_consistent",text="Recalculate Normals", icon='SNAP_NORMAL')        

        box.separator() 

        row = box.row(1)   
        row.prop(context.object.data, "show_handles", text="Handles", icon='IPO_BEZIER')
        row.prop(context.object.data, "show_normal_face", text="Normals", icon='SNAP_NORMAL')
       
        if context.object.data.show_normal_face == True:  

            row = box.column(1)
            row.prop(context.scene.tool_settings, "normal_size", text="Size")                                   

        box.separator() 