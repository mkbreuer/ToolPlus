# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

        
def draw_snapflatten_ui(self, context, layout):

    icons = load_icons()
    
    panel_prefs = context.user_preferences.addons[__package__].preferences

    layout.operator_context = 'INVOKE_REGION_WIN'    

    col = layout.column(align=True)
 
    box = col.box().column(align=True) 

    row = box.row(1)
    row.label(text="Select linked face by angle")
  
    box.separator() 
 
    row = box.row(1)    
    row.prop(panel_prefs, 'threshold')
   
    box.separator() 

