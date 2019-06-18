# LOAD UI #   
from toolplus_originset.ui_panel import draw_originset_ui

# LOAD MODUL #    
import bpy

class VIEW3D_MT_originset_menu(bpy.types.Menu):
    bl_label = "OriginSet"
    bl_idname = "VIEW3D_MT_originset_menu"   

    def draw(self, context):
        layout = self.layout

        draw_originset_ui(self, context, layout)        

         