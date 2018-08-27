# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons


# PANEL LAYOUT #
def draw_sculptnoise_panel_layout(self, context, layout):
    tp_props = context.window_manager.tp_sculptnoise_props        

    icons = load_icons()
    #button_tubehole = icons.get("icon_tubehole") 
    #row.operator("tp_ops.tubehole", text="", icon_value=button_tubehole.icon_id) 

    layout.operator_context = 'INVOKE_REGION_WIN'
    
    col = layout.column(1)                                                
    box = col.box().column(1)
  
    row = box.row(1) 
    if tp_props.display_sculpt_noise:
        row.prop(tp_props, "display_sculpt_noise", text="", icon='ASSET_MANAGER')
    else:
        row.prop(tp_props, "display_sculpt_noise", text="", icon='ASSET_MANAGER')

    row.operator("tp_ops.add_displace_noise", text='Add Displace Noise')

    is_displace = False        
    for mode in bpy.context.object.modifiers:
        if mode.type == 'DISPLACE':
            is_displace  = True

    if is_displace  == True:   
        row.prop(bpy.context.active_object.modifiers["Displace"], "show_viewport", text="")             
        row.operator("tp_ops.remove_mods_displace", text="" , icon='X')                                 
        row.operator("tp_ops.apply_mods_displace", text="", icon='FILE_TICK')              
        
        obj = context.active_object
        mo_types = []
        append = mo_types.append

        row = box.row(1)  
        
        for mo in obj.modifiers:           
            if mo.type == 'DISPLACE':
                row.prop(mo, "strength")
                row.prop(mo, "mid_level")
                                
        
        box.separator()             
        
        row = box.row(1)
        row.label(text="Mask", icon="BRUSH_MASK") 
        row.operator("tp_ops.displace_mask_paint", text="", icon="BRUSH_DATA")    
        row.operator("tp_ops.displace_mask_areas", text="", icon="DISCLOSURE_TRI_RIGHT")            
        row.operator("tp_ops.displace_mask_remove", text="", icon="DISCLOSURE_TRI_DOWN")
  
  
    else:                 
        pass

    if tp_props.display_sculpt_noise:

        box.separator()            
        
        is_displace = False        
        for mode in bpy.context.object.modifiers:
            if mode.type == 'DISPLACE':
                is_displace  = True

        if is_displace  == True:    
  
            row = box.row(1) 
            tex = bpy.data.textures["Sculpt_Noise"]

            box.prop(tex, "musgrave_type")    
            box.prop(tex, "noise_basis", "Noise:")                                 
            
            box.separator()               
           
            row = box.row(1)  
            
            row.prop(tex, "noise_scale", text="Size")         
            row.prop(tex, "noise_intensity", text="Intensity") 

            row = box.row(1)   
            row.prop(tex, "dimension_max", text="Dimension")
            row.prop(tex, "octaves")
           
            row = box.row(1)          
            row.prop(tex, "nabla")
            row.prop(tex, "lacunarity")

            
            musgrave_type = tex.musgrave_type
           
            col = box.column()           
            if musgrave_type in {'HETERO_TERRAIN', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL'}:
                col.prop(tex, "offset")
           
            if musgrave_type in {'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL'}:
                col.prop(tex, "gain")

        else:                     
            row = box.row(1)
            row.label(text="no displace active", icon="INFO") 

            box.separator()     
                
            row = box.row(1)           
            props = row.operator("paint.mask_flood_fill", text="Remove Mask", icon ="BRUSH_TEXFILL")
            props.mode = 'VALUE'
            props.value = 0    

    box.separator()







EDIT = ["SCULPT"]
GEOM = ['MESH']

class VIEW3D_TP_SculptNoise_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_SculptNoise_Panel_TOOLS"
    bl_label = "SculptNoise"
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
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_sculptnoise_panel_layout(self, context, layout)         
        


class VIEW3D_TP_SculptNoise_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_SculptNoise_Panel_UI"
    bl_label = "SculptNoise"
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
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_sculptnoise_panel_layout(self, context, layout) 
