# LOAD UI #   
from toolplus_originset.ui_panel import draw_originset_ui

# LOAD MODUL #    
import bpy
from . icons.icons import load_icons  


class VIEW3D_MT_originset_menu_header(bpy.types.Menu):
    bl_label = "Set Origin"
    bl_idname = "VIEW3D_MT_originset_menu_header"

    def draw(self, context):
        layout = self.layout
       
        draw_originset_ui(self, context, layout)
  


# UI: HEADER MENU # 
class VIEW3D_HT_originset_header_menu(bpy.types.Header):
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
       return 
       
    def draw(self, context):
        layout = self.layout       

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'    

        addon_prefs = context.preferences.addons[__package__].preferences
        
        row = layout.row(align=True)

        button_icon_origin_snap_origin = icons.get("icon_origin_snap_origin")                
        if addon_prefs.tab_origin_header_text == True:            
            row.menu("VIEW3D_MT_originset_menu_header", text="Set Origin", icon_value=button_icon_origin_snap_origin.icon_id)      
        else:
            row.menu("VIEW3D_MT_originset_menu_header", text="", icon_value=button_icon_origin_snap_origin.icon_id)               






                  










