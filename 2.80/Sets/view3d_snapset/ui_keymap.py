# LOAD MODUL #    
import bpy
from bpy import *

# ADD 3D VIEW MENU #  
from view3d_snapset.ui_menu         import (VIEW3D_MT_SnapSet_Menu)
from view3d_snapset.ui_menu_pie     import (VIEW3D_MT_SnapSet_Menu_Pie)

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

        addon_prefs = context.preferences.addons[__package__].preferences

        if addon_prefs.tab_snapset_menu == 'menu':

            bpy.utils.register_class(VIEW3D_MT_SnapSet_Menu)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            
                                                    # ADD NEW KEYS HERE #
            kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', shift=True) #, ctrl=True, alt=True)
            
            kmi.properties.name = "VIEW3D_MT_SnapSet_Menu"       


        if addon_prefs.tab_snapset_menu == 'pie':

            bpy.utils.register_class(VIEW3D_MT_SnapSet_Menu_Pie)

            km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
            
                                                        # ADD NEW KEYS HERE #
            kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', shift=True) #, ctrl=True, alt=True)
            
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





# ADD TO SPECIAL [W] #  
from view3d_snapset.ui_menu_special  import (draw_snapset_item_special)

def update_snapset_special(self, context):

    try:     
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.remove(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.remove(draw_snapset_item_special)  

    except:
        pass
    
    addon_prefs = context.preferences.addons[__package__].preferences    
  
    if addon_prefs.tab_snapset_special == 'append':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_object_context_menu.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.append(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.append(draw_snapset_item_special)  

    if addon_prefs.tab_snapset_special == 'prepend':

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_object_context_menu.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_edit_curve_context_menu.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_armature_context_menu.prepend(draw_snapset_item_special)  
        bpy.types.VIEW3D_MT_particle_context_menu.prepend(draw_snapset_item_special)  

    if addon_prefs.tab_snapset_special == 'remove':  
        return None




# ADD TO HEADER #  
from view3d_snapset.ui_header  import (VIEW3D_HT_SnapSet_Header_Menu)

def update_snapset_header(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_HT_SnapSet_Header_Menu)  
        
    except:
        pass
    
    addon_prefs = context.preferences.addons[__package__].preferences   

    if addon_prefs.tab_snapset_header == 'add':

        bpy.utils.register_class(VIEW3D_HT_SnapSet_Header_Menu)

    if addon_prefs.tab_snapset_header == 'remove':
        return None  




