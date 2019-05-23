# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  

class VIEW3D_MT_SnapFlat_Menu(bpy.types.Menu):
    bl_label = "SnapFlat"
    bl_idname = "VIEW3D_MT_SnapFlat_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        layout.operator("tpc_ot.snapflat_modal", text="Flatten LpT").mode="flatten_lpt"
        
        layout.separator()

        layout.operator("tpc_ot.snapflat_modal", text="Flatten X-Axis").mode="flatten_x"
        layout.operator("tpc_ot.snapflat_modal", text="Flatten Y-Axis").mode="flatten_y"
        layout.operator("tpc_ot.snapflat_modal", text="Flatten Z-Axis").mode="flatten_z"
   
        layout.separator()
       
        layout.operator("tpc_ot.snapflat_modal", text="Flatten Normal").mode="flatten_n"
   
        layout.separator()

        layout.operator("tpc_ot.snapflat_modal", text="Boundary Sharp Edges").mode="snap_for_sharp"
        layout.operator("tpc_ot.snapflat_modal", text="Boundary UV Seams").mode="snap_for_uvs"        