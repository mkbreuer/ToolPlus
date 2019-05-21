# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

        
def draw_snaporigin_ui(self, context, layout):

    icons = load_icons()
    
    panel_prefs = context.user_preferences.addons[__package__].preferences

    layout.operator_context = 'INVOKE_REGION_WIN'    

    col = layout.column(align=True)
 
    box = col.box().column(align=True) 

    row = box.column(1)
    if context.mode == 'OBJECT':

        if len(bpy.context.selected_objects) == 1: 
          
            button_origin_tosnap = icons.get("icon_origin_tosnap")         
            row.operator("tpc_ot.snap_to_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
            
            button_origin_edm = icons.get("icon_origin_edm")   
            row.operator("tpc_ot.snaporigin_modal", text="Origin to Mesh", icon_value=button_origin_edm.icon_id).mode = "cursor, obm"     
          
            row.separator()
          
            button_origin_bbox = icons.get("icon_origin_bbox")                               
            row.operator("tpc_ot.snap_to_bbox", text="Origin to BBox", icon="SNAP_PEEL_OBJECT")                              

            row.separator()
            
            button_origin_center_loc = icons.get("icon_origin_center_loc")
            row.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"
      
        else:
            row.label(text="Only for 1")
            row.label(text="selected")
            row.label(text="object")
            row.label(text="allowed!")
 
    else:

        button_origin_edm = icons.get("icon_origin_edm")   
        row.operator("tpc_ot.snaporigin_modal", text="Edm-Select", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"

        button_origin_obj = icons.get("icon_origin_obj")   
        row.operator("tpc_ot.snaporigin_modal", text="Obm-Select", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"

        row.separator() 
             
        button_origin_center_loc = icons.get("icon_origin_center_loc")
        larowyout.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"
          
   