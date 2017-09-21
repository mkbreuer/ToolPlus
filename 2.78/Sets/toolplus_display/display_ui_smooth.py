
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

EDIT = ["EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

class VIEW3D_TP_Smooth_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Shade / UVs"
    bl_idname = "VIEW3D_TP_Smooth_Panel_TOOLS"
    bl_label = "Smooth"
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
        layout.operator_context = 'INVOKE_AREA'

        draw_smooth_panel_layout(self, context, layout) 



class VIEW3D_TP_Smooth_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Smooth_Panel_UI"
    bl_label = "Smooth"
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
        layout.operator_context = 'INVOKE_AREA'

        draw_smooth_panel_layout(self, context, layout) 




def draw_smooth_panel_layout(self, context, layout):
    icons = load_icons()
  
    ob = context.object  
    obj = context.object
    scene = context.scene
    scn = context.scene
    rs = bpy.context.scene 

    if context.mode == 'OBJECT':
        
       box = layout.box().column(1) 
        
       row = box.column(1)
       row.operator("object.shade_flat", text="Shade Flat", icon="MESH_CIRCLE")
       row.operator("object.shade_smooth", text="Shade Smooth", icon="SMOOTH")   
              
       obj = context.active_object     
       if obj:
           obj_type = obj.type
                          
           if obj_type in {'MESH'}:
           
                box.separator() 
               
                row = box.row(1) 
                if context.active_object.data.use_auto_smooth == False:              
                    row.prop(context.active_object.data, "use_auto_smooth", "use auto smooth off",icon="AUTO")
                else:  
                    row.prop(context.active_object.data, "use_auto_smooth", "use auto smooth on",icon="AUTO")
            
                row = box.row(1)
                row.active = context.active_object.data.use_auto_smooth
                row.prop(context.active_object.data, "auto_smooth_angle", text="Angle") 
               
                box.separator() 
                
                row = box.row(1) 
                if context.active_object.data.show_double_sided == False:  
                    row.prop(context.active_object.data, "show_double_sided", "double sided light off",icon="GHOST")        
                else:  
                    row.prop(context.active_object.data, "show_double_sided", "double sided light on",icon="GHOST")  

           else:
               pass

       box.separator()  


    if context.mode == 'EDIT_MESH':


        box = layout.box().column(1)                   

        row = box.column(1)
        row.operator("mesh.faces_shade_flat", icon="MESH_CIRCLE") 
        row.operator("mesh.faces_shade_smooth", icon="SMOOTH") 
        
        box.separator() 
        
        row = box.row(1) 
        if context.active_object.data.use_auto_smooth == False:              
            row.prop(context.active_object.data, "use_auto_smooth", "use auto smooth off",icon="AUTO")
        else:  
            row.prop(context.active_object.data, "use_auto_smooth", "use auto smooth on",icon="AUTO")
    
        row = box.row(1)
        row.active = context.active_object.data.use_auto_smooth
        row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")     

        box.separator() 
        
        row = box.row(1) 
        if context.active_object.data.show_double_sided == False:  
            row.prop(context.active_object.data, "show_double_sided", "double sided light off",icon="GHOST")        
        else:  
            row.prop(context.active_object.data, "show_double_sided", "double sided light on",icon="GHOST")    
       
        box.separator()   
    
