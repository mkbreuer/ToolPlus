# LOAD UI #   
from view3d_originset.ui_panel import draw_originset_ui

# LOAD MODUL #    
import bpy
from . icons.icons import load_icons  


# UI: HOTKEY MENU # 
class VIEW3D_MT_originset_menu_special(bpy.types.Menu):
    bl_label = "OriginSet"
    bl_idname = "VIEW3D_MT_originset_menu_special"

    def draw(self, context):
        layout = self.layout
        
        draw_originset_ui(self, context, layout)        

 

def draw_origin_item_special(self, context):
    layout = self.layout

    icons = load_icons()
    
    addon_prefs = context.preferences.addons[__package__].preferences
          
    if addon_prefs.tab_origin_special == 'append':
        if addon_prefs.toggle_special_origin_separator == True:
            layout.separator()      

    if addon_prefs.toggle_special_origin_icon == True:
        button_icon_origin_snap_origin = icons.get("icon_origin_snap_origin")
        layout.menu("VIEW3D_MT_originset_menu_special", text="OriginSet", icon_value=button_icon_origin_snap_origin.icon_id)      
    else:
        layout.menu("VIEW3D_MT_originset_menu_special", text="OriginSet")      

    if addon_prefs.tab_origin_special == 'prepend':
        if addon_prefs.toggle_special_origin_separator == True:
            layout.separator()      




                  










