import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



def draw_history_layout(context, layout):          
      
    layout.operator_context = 'INVOKE_REGION_WIN'
   
    icons = load_icons()     

    col = layout.column(1) 
    box = col.box().column(1)

    row = box.row(1)        
    row.operator("view3d.ruler", text="Ruler")   
     
    row.operator("ed.undo_history", text="History")
    row.operator("ed.undo", text="", icon="LOOP_BACK")
    row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
   
    box.separator()               
    