# LOAD UI #   
from view3d_snapset.ui_menu import (VIEW3D_MT_SnapSet_Menu_Special)


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  

          

def draw_snapset_item_special(self, context):
    layout = self.layout

    icons = load_icons()

    addon_prefs = context.preferences.addons[__package__].preferences
  
    if addon_prefs.tab_snapset_special == 'append':
        if addon_prefs.toggle_special_separator == True:
            layout.separator()      

    if addon_prefs.toggle_special_icon == True:
        button_snap_set = icons.get("icon_snap_set")
        layout.menu("VIEW3D_MT_SnapSet_Menu_Special", text="SnapSet", icon_value=button_snap_set.icon_id)      
    else:
        layout.menu("VIEW3D_MT_SnapSet_Menu_Special", text="SnapSet")      
    
    if addon_prefs.tab_snapset_special == 'prepend':
        if addon_prefs.toggle_special_separator == True:
            layout.separator()      


            






                  










