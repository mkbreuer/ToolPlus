# LOAD MODUL #    
import bpy
from bpy import *


# ADD 3D VIEW MENU #  
from view3d_originset.ui_menu         import (VIEW3D_MT_originset_menu)
from view3d_originset.ui_menu_pie     import (VIEW3D_MT_originset_menu_pie)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_origin_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MT_originset_menu)
        bpy.utils.unregister_class(VIEW3D_MT_originset_menu_pie)
        
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

        addon_prefs = context.preferences.addons[__package__].preferences

        if addon_prefs.tab_origin_menu == 'menu':

            bpy.utils.register_class(VIEW3D_MT_originset_menu)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu',
            addon_prefs.use_hotkey, 
            addon_prefs.use_event, 
            shift=addon_prefs.use_shift, 
            ctrl=addon_prefs.use_ctrl, 
            alt=addon_prefs.use_alt)
            kmi.properties.name = "VIEW3D_MT_originset_menu"    


        if addon_prefs.tab_origin_menu == 'pie':

            bpy.utils.register_class(VIEW3D_MT_originset_menu_pie)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu_pie',
            addon_prefs.use_hotkey, 
            addon_prefs.use_event, 
            shift=addon_prefs.use_shift, 
            ctrl=addon_prefs.use_ctrl, 
            alt=addon_prefs.use_alt)
            kmi.properties.name = "VIEW3D_MT_originset_menu_pie"   
            

        if addon_prefs.tab_origin_menu == 'remove':

            bpy.utils.unregister_class(VIEW3D_MT_originset_menu)
            bpy.utils.unregister_class(VIEW3D_MT_originset_menu_pie)

            km = kc.keymaps['3D View']
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "VIEW3D_MT_originset_menu":
                        km.keymap_items.remove(kmi)
                        break
                 
                    if kmi.properties.name == "VIEW3D_MT_originset_menu_pie":
                        km.keymap_items.remove(kmi)
                        break



# ADD TO SPECIAL [W] #  
from view3d_originset.ui_menu_special  import (draw_origin_item_special)

def update_origin_special(self, context):

    try:     
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.remove(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.remove(draw_origin_item_special)  

    except:
        pass

    addon_prefs = context.preferences.addons[__package__].preferences
    
    if addon_prefs.tab_origin_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_object_context_menu.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.append(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.append(draw_origin_item_special)  

    if addon_prefs.tab_origin_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_object_context_menu.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.prepend(draw_origin_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.prepend(draw_origin_item_special)  

    if addon_prefs.tab_origin_special == 'remove':  
        return None



# ADD TO HEADER #  
from view3d_originset.ui_header  import (VIEW3D_HT_originset_header_menu)

def update_origin_header(self, context):
     
    try:     
        bpy.utils.unregister_class(VIEW3D_HT_originset_header_menu)  

    except:
        pass

    addon_prefs = context.preferences.addons[__package__].preferences  

    #if addon_prefs.tab_origin_header == 'append':
        #bpy.utils.register_class(VIEW3D_HT_originset_header_menu)  

    if addon_prefs.tab_origin_header == 'prepend':
        bpy.utils.register_class(VIEW3D_HT_originset_header_menu)  

    if addon_prefs.tab_origin_header == 'remove':  
        return None



