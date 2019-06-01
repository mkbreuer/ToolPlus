# LOAD MODUL #    
import bpy
from bpy import *


# ADD 3D VIEW MENU #  
from toolplus_snapset.ui_menu         import (VIEW3D_MT_SnapSet_Menu)
from toolplus_snapset.ui_menu_pie     import (VIEW3D_MT_SnapSet_Menu_Pie)

# KEY REGISTRY # 
addon_keymaps_menu = []

def update_snapset_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MT_SnapSet_Menu)
        bpy.utils.unregister_class(VIEW3D_MT_SnapSet_Menu_Pie)
        
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

        if addon_prefs.tab_snapset_menu == 'menu':

            bpy.utils.register_class(VIEW3D_MT_SnapSet_Menu)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu', 
            addon_prefs.use_hotkey, 
            addon_prefs.use_event, 
            shift=addon_prefs.use_shift, 
            ctrl=addon_prefs.use_ctrl, 
            alt=addon_prefs.use_alt)
            kmi.properties.name = "VIEW3D_MT_SnapSet_Menu"    


        if addon_prefs.tab_snapset_menu == 'pie':

            bpy.utils.register_class(VIEW3D_MT_SnapSet_Menu_Pie)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('wm.call_menu_pie', 
            addon_prefs.use_hotkey, 
            addon_prefs.use_event, 
            shift=addon_prefs.use_shift, 
            ctrl=addon_prefs.use_ctrl, 
            alt=addon_prefs.use_alt)
            kmi.properties.name = "VIEW3D_MT_SnapSet_Menu_Pie"   
            

        if addon_prefs.tab_snapset_menu == 'remove':

            km = kc.keymaps['3D View']
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "VIEW3D_MT_SnapSet_Menu":
                        km.keymap_items.remove(kmi)
                        break
                 
                    if kmi.properties.name == "VIEW3D_MT_SnapSet_Menu_Pie":
                        km.keymap_items.remove(kmi)
                        break




addon_keymaps = []

def update_snapset_tools(self, context):
 
    wm = bpy.context.window_manager   
    kc = wm.keyconfigs.addon
    if kc:   

        addon_prefs = context.user_preferences.addons[__package__].preferences
        
        if addon_prefs.tab_snapset_add_tools == True:

            #km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            kmi = km.keymap_items.new('tpc_ot.snapset_modal', 
            addon_prefs.use_hotkey_button, 
            addon_prefs.use_event_button, 
            shift=addon_prefs.use_shift_button, 
            ctrl=addon_prefs.use_ctrl_button, 
            alt=addon_prefs.use_alt_button)
            kmi.properties.mode = "place"               
            addon_keymaps.append((km,kmi))

        else:

            for km, kmi in addon_keymaps:
                km.keymap_items.remove(kmi)
            # clear the list
            addon_keymaps.clear()



# ADD TO SPECIAL [W] #  
from toolplus_snapset.ui_menu_special  import (draw_snapset_item_special)

def update_snapset_special(self, context):

    try:     
        bpy.types.VIEW3D_MT_object_specials.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.remove(draw_snapset_item_special)  

    except:
        pass
    
    addon_prefs = context.user_preferences.addons[__package__].preferences    
  
    if addon_prefs.tab_snapset_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_object_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.append(draw_snapset_item_special)  

    if addon_prefs.tab_snapset_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_object_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_specials.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_specials.prepend(draw_snapset_item_special)  

    if addon_prefs.tab_snapset_special == 'remove':  
        return None




# ADD TO HEADER #  
from toolplus_snapset.ui_header  import (VIEW3D_HT_SnapSet_Header_Menu)

def update_snapset_header(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_HT_SnapSet_Header_Menu)  
        
    except:
        pass
    
    addon_prefs = context.user_preferences.addons[__package__].preferences   

    if addon_prefs.tab_snapset_header == 'add':

        bpy.utils.register_class(VIEW3D_HT_SnapSet_Header_Menu)

    if addon_prefs.tab_snapset_header == 'remove':
        return None  




