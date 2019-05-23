# LOAD MODUL #    
import bpy
from bpy import *


# ADD 3D VIEW MENU #  
from toolplus_snapflat.ui_menu         import (VIEW3D_MT_SnapFlat_Menu)
from toolplus_snapflat.ui_menu_pie     import (VIEW3D_MT_SnapFlat_Menu_Pie)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_snapflat_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MT_SnapFlat_Menu)
        bpy.utils.unregister_class(VIEW3D_MT_SnapFlat_Menu_Pie)
        
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

        addon_prefs = context.user_preferences.addons[__package__].preferences

        if addon_prefs.tab_snapflat_menu == 'menu':

            bpy.utils.register_class(VIEW3D_MT_SnapFlat_Menu)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu', 'TWO', 'PRESS', shift=True) #, ctrl=True, alt=True)
            kmi.properties.name = "VIEW3D_MT_SnapFlat_Menu"    


        if addon_prefs.tab_snapflat_menu == 'pie':

            bpy.utils.register_class(VIEW3D_MT_SnapFlat_Menu_Pie)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu_pie', 'TWO', 'PRESS', shift=True) #, ctrl=True, alt=True)
            kmi.properties.name = "VIEW3D_MT_SnapFlat_Menu_Pie"   
            

        if addon_prefs.tab_snapflat_menu == 'remove':

            km = kc.keymaps['3D View']
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "VIEW3D_MT_SnapFlat_Menu":
                        km.keymap_items.remove(kmi)
                        break
                 
                    if kmi.properties.name == "VIEW3D_MT_SnapFlat_Menu_Pie":
                        km.keymap_items.remove(kmi)
                        break





# ADD TO SPECIAL [W] #  
from toolplus_snapflat.ui_menu_special  import (draw_snapflat_item_special)

def update_snapflat_special(self, context):

    try:     
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(draw_snapflat_item_special)  

    except:
        pass

    addon_prefs = context.user_preferences.addons[__package__].preferences
    
    if addon_prefs.tab_snapflat_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(draw_snapflat_item_special)  

    if addon_prefs.tab_snapflat_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_snapflat_item_special)  

    if addon_prefs.tab_snapflat_special == 'remove':  
        return None





