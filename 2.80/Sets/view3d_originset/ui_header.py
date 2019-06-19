# LOAD UI #   
from view3d_originset.ui_panel import draw_originset_ui

# LOAD MODUL #    
import bpy
from . icons.icons import load_icons  


class VIEW3D_MT_originset_menu_header(bpy.types.Menu):
    bl_label = "OriginSet"
    bl_idname = "VIEW3D_MT_originset_menu_header"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'       
        
        draw_originset_ui(self, context, layout)
  

class VIEW3D_PT_originset_panel_header(bpy.types.Panel):
    bl_label = "OriginSet"
    bl_idname = "VIEW3D_PT_originset_panel_header"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
  
    def draw(self, context):
        layout = self.layout.box().column(align=True)
        layout.operator_context = 'INVOKE_REGION_WIN'       
        
        draw_originset_ui(self, context, layout)



# UI: HEADER MENU # 
class VIEW3D_HT_originset_header_menu(bpy.types.Header):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    @classmethod
    def poll(self, context):
       return 
       
    def draw(self, context):
        layout = self.layout       

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'    

        addon_prefs = context.preferences.addons[__package__].preferences
                
        button_icon_origin_snap_origin = icons.get("icon_origin_snap_origin")                

        if addon_prefs.tab_origin_header_type == True:                        
            if addon_prefs.tab_origin_header_text == True:                        
                layout.menu("VIEW3D_MT_originset_menu_header", text=" OriginSet", icon_value=button_icon_origin_snap_origin.icon_id)      
            else:
                layout.menu("VIEW3D_MT_originset_menu_header", text="", icon_value=button_icon_origin_snap_origin.icon_id)               
        else:
            layout.popover(panel="VIEW3D_PT_originset_panel_header", icon_value=button_icon_origin_snap_origin.icon_id, text="")




                  










