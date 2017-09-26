import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons



def draw_history_layout(context, layout):          
      
    layout.operator_context = 'INVOKE_REGION_WIN'
   
    icons = load_icons()     

    box = layout.box().column(1)  

    row = box.row(1)        
    #row.operator("screen.redo_last", text="", icon="COLLAPSEMENU") 
    row.operator('wm.path_open',  text = '', icon = 'COLLAPSEMENU').filepath = "C:\\Users\Public\Documents" 

    button_ruler = icons.get("icon_ruler")
    row.operator("view3d.ruler", text="Ruler", icon_value=button_ruler.icon_id)   
     
    row.operator("ed.undo_history", text="Undo", icon="SCRIPTPLUGINS")

    row.operator("ed.undo", text="", icon="LOOP_BACK")  
    row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
   
    box.separator()                
    