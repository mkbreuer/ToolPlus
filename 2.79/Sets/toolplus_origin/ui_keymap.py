# LOAD MODUL #    
import bpy
from bpy import *


# ADD 3D VIEW MENU #  
from toolplus_origin.ui_menu         import (VIEW3D_MT_OriginSet_Menu)
from toolplus_origin.ui_menu_pie     import (VIEW3D_MT_OriginSet_Menu_Pie)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_origin_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MT_OriginSet_Menu)
        bpy.utils.unregister_class(VIEW3D_MT_OriginSet_Menu_Pie)
        
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

        if addon_prefs.tab_origin_menu == 'menu':

            bpy.utils.register_class(VIEW3D_MT_OriginSet_Menu)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu',
            addon_prefs.use_hotkey, 
            addon_prefs.use_event, 
            shift=addon_prefs.use_shift, 
            ctrl=addon_prefs.use_ctrl, 
            alt=addon_prefs.use_alt)
            kmi.properties.name = "VIEW3D_MT_OriginSet_Menu"    


        if addon_prefs.tab_origin_menu == 'pie':

            bpy.utils.register_class(VIEW3D_MT_OriginSet_Menu_Pie)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu_pie',
            addon_prefs.use_hotkey, 
            addon_prefs.use_event, 
            shift=addon_prefs.use_shift, 
            ctrl=addon_prefs.use_ctrl, 
            alt=addon_prefs.use_alt)
            kmi.properties.name = "VIEW3D_MT_OriginSet_Menu_Pie"   
            

        if addon_prefs.tab_origin_menu == 'remove':

            bpy.utils.unregister_class(VIEW3D_MT_OriginSet_Menu)
            bpy.utils.unregister_class(VIEW3D_MT_OriginSet_Menu_Pie)

            km = kc.keymaps['3D View']
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "VIEW3D_MT_OriginSet_Menu":
                        km.keymap_items.remove(kmi)
                        break
                 
                    if kmi.properties.name == "VIEW3D_MT_OriginSet_Menu_Pie":
                        km.keymap_items.remove(kmi)
                        break


# ADD TO HEADER #  
from toolplus_origin.ui_header  import (VIEW3D_HT_OriginSet_Header_Menu)

def update_origin_header(self, context):

    try:     
        bpy.utils.unregister_class(VIEW3D_HT_OriginSet_Header_Menu)  

    except:
        pass

    addon_prefs = context.user_preferences.addons[__package__].preferences  

    if addon_prefs.tab_origin_header == 'prepend':

        bpy.utils.register_class(VIEW3D_HT_Set_Origin_Header_Menu)  

    if addon_prefs.tab_origin_header == 'remove':  
        return None



# ADD TO SPECIAL [W] #  
from toolplus_origin.ui_menu_special  import (draw_origin_item_special)

def update_origin_special(self, context):

    try:     
        bpy.types.VIEW3D_MT_object_specials.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.remove(draw_origin_item_special)  

    except:
        pass

    addon_prefs = context.user_preferences.addons[__package__].preferences
    
    if addon_prefs.tab_origin_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_object_specials.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.append(draw_origin_item_special)  

    if addon_prefs.tab_origin_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_object_specials.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.prepend(draw_origin_item_special)  

    if addon_prefs.tab_origin_special == 'remove':  
        return None




