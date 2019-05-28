# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

        
def draw_snapflat_ui(self, context, layout):

    icons = load_icons()    
    addon_prefs = context.user_preferences.addons[__package__].preferences

    layout.operator_context = 'INVOKE_REGION_WIN'    

    col = layout.column(align=True)
 
    box = col.box().column(align=True) 

    if addon_prefs.show_snapflat_buttons == True:
        row = box.column(align=True)
        
        row.operator("tpc_ops.snapflat_modal", text="Flatten LpT").mode="flatten_lpt"
        
        row.separator()

        row.operator("tpc_ops.snapflat_modal", text="Flatten X-Axis").mode="flatten_x"
        row.operator("tpc_ops.snapflat_modal", text="Flatten Y-Axis").mode="flatten_y"
        row.operator("tpc_ops.snapflat_modal", text="Flatten Z-Axis").mode="flatten_z"
   
        row.separator()
       
        row.operator("tpc_ops.snapflat_modal", text="Flatten Normal").mode="flatten_n"
   
        row.separator()

        row.operator("tpc_ops.snapflat_modal", text="Boundary Sharp Edges").mode="snap_for_sharp"
        row.operator("tpc_ops.snapflat_modal", text="Boundary UV Seams").mode="snap_for_uvs"   
      
        box.separator() 
        box = col.box().column(align=True) 
        box.separator() 


    row = box.row(align=True)
    row.label(text="Modal Settings")
  
    box.separator() 
 
    row = box.row(align=True)    
    row.prop(addon_prefs, 'threshold')

    box.separator() 
 
    row = box.row(align=True)   
    row.prop(addon_prefs, 'mesh_select_mode', text="Mode")
   
    box.separator() 

