# LOAD MODUL #    
import bpy
from bpy import *


# ADD 3D VIEW MENU #  
from toolplus_snapflatten.ui_menu         import (VIEW3D_MT_SnapFlatten_Menu)
from toolplus_snapflatten.ui_menu_pie     import (VIEW3D_MT_SnapFlatten_Menu_Pie)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_snapflatten_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MT_SnapFlatten_Menu)
        bpy.utils.unregister_class(VIEW3D_MT_SnapFlatten_Menu_Pie)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:   

        if context.user_preferences.addons[__package__].preferences.tab_snapflatten_menu == 'menu':

            bpy.utils.register_class(VIEW3D_MT_SnapFlatten_Menu)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu', 'TWO', 'PRESS', shift=True) #, ctrl=True, alt=True)
            kmi.properties.name = "VIEW3D_MT_SnapFlatten_Menu"    


        if context.user_preferences.addons[__package__].preferences.tab_snapflatten_menu == 'pie':

            bpy.utils.register_class(VIEW3D_MT_SnapFlatten_Menu_Pie)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu_pie', 'TWO', 'PRESS', shift=True) #, ctrl=True, alt=True)
            kmi.properties.name = "VIEW3D_MT_SnapFlatten_Menu_Pie"   
            

        if context.user_preferences.addons[__package__].preferences.tab_snapflatten_menu == 'remove':

            km = kc.keymaps['3D View']
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "VIEW3D_MT_SnapFlatten_Menu":
                        km.keymap_items.remove(kmi)
                        break
                 
                    if kmi.properties.name == "VIEW3D_MT_SnapFlatten_Menu_Pie":
                        km.keymap_items.remove(kmi)
                        break





# ADD TO SPECIAL [W] #  
from toolplus_snapflatten.ui_menu_special  import (draw_snapflatten_item_special)

def update_snapflatten_special(self, context):

    try:     
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(draw_snapflatten_item_special)  

    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_snapflatten_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(draw_snapflatten_item_special)  

    if context.user_preferences.addons[__package__].preferences.tab_snapflatten_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_snapflatten_item_special)  

    if context.user_preferences.addons[__package__].preferences.tab_snapflatten_special == 'remove':  
        return None





