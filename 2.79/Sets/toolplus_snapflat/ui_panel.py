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

    row = box.row(1)
    row.label(text="Modal Settings")
  
    box.separator() 
 
    row = box.row(1)    
    row.prop(addon_prefs, 'threshold')

    box.separator() 
 
    row = box.row(1)   
    row.prop(addon_prefs, 'mesh_select_mode', text="Mode")
   
    box.separator() 

