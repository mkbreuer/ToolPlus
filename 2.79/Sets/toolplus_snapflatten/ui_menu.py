# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  

import addon_utils

class VIEW3D_MT_SnapFlatten_Menu(bpy.types.Menu):
    bl_label = "Flatten Modal"
    bl_idname = "VIEW3D_MT_SnapFlatten_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        loop_tools_addon = "mesh_looptools" 
        state = addon_utils.check(loop_tools_addon)
        if not state[0]: 
            pass                        

        else:

            layout.operator("tpc_ot.snapflatten_modal", text="Flatten LpT").mode="flatten_lpt"
        
            layout.separator()

        layout.operator("tpc_ot.snapflatten_modal", text="Flatten X-Axis").mode="flatten_x"
        layout.operator("tpc_ot.snapflatten_modal", text="Flatten Y-Axis").mode="flatten_y"
        layout.operator("tpc_ot.snapflatten_modal", text="Flatten Z-Axis").mode="flatten_z"
   
        layout.separator()
       
        layout.operator("tpc_ot.snapflatten_modal", text="Flatten Normal").mode="flatten_n"



