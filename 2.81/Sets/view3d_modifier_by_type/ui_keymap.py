# LOAD MODUL #    
import bpy
from bpy import *
from .ui_properties import draw_modifier_by_type_ui_properties


# UI: HOTKEY MENU # 
def draw_popover(self, context):
    if (context.active_object):
        if (len(context.active_object.modifiers)):
            layout = self.layout
            layout.operator_context = 'INVOKE_REGION_WIN'

            addon_prefs = context.preferences.addons[__package__].preferences
               
            if addon_prefs.toggle_popover_separator == True:
                if addon_prefs.toggle_popover == 'append': # bottom   
                    layout.separator()      

            if addon_prefs.toggle_popover_icon == True:
                layout.popover(panel="VIEW3D_PT_modifier_by_type_panel_ui", text="Mod By Type", icon='MODIFIER_OFF')      
            else:
                layout.popover(panel="VIEW3D_PT_modifier_by_type_panel_ui", text="Mod By Type")      

            if addon_prefs.toggle_popover_separator == True:
                if addon_prefs.toggle_popover == 'prepend':  # top 
                    layout.separator()      


# UI: HEADER MENU #
def draw_popover_header(self, context):	
    if (context.active_object):
        if (len(context.active_object.modifiers)):
            layout = self.layout
          
            addon_prefs = context.preferences.addons[__package__].preferences
                   
            if addon_prefs.toggle_popover_separator == True:
                if addon_prefs.toggle_popover == 'append': # bottom   
                    layout.separator()  
           
            if addon_prefs.toggle_popover_icon == True:
                layout.popover(panel="VIEW3D_PT_modifier_by_type_panel_ui", text="", icon='MODIFIER_OFF')      
            else:
                layout.popover(panel="VIEW3D_PT_modifier_by_type_panel_ui", text="Mod By Type")      

            if addon_prefs.toggle_popover_separator == True:
                if addon_prefs.toggle_popover == 'prepend':  # top 
                    layout.separator()    


# UI: MENUS # 
def update_menu(self, context):
    try:            
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_popover)
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_popover)
        bpy.types.VIEW3D_MT_edit_curve_context_menu.remove(draw_popover)
        bpy.types.VIEW3D_MT_editor_menus.remove(draw_popover_header)    
        bpy.types.VIEW3D_HT_header.remove(draw_popover_header)    
    except:
        pass
    
    addon_prefs = context.preferences.addons[__package__].preferences    
  
    if addon_prefs.toggle_popover == 'prepend': # top        

        if addon_prefs.toggle_MT_menu == 'menu_special':
            bpy.types.VIEW3D_MT_object_context_menu.prepend(draw_popover)  
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.prepend(draw_popover)
            bpy.types.VIEW3D_MT_edit_curve_context_menu.prepend(draw_popover)

        if addon_prefs.toggle_MT_menu == 'menu_header':
            if addon_prefs.toggle_MT_menu_location == 'header_editor_menus':
                bpy.types.VIEW3D_MT_editor_menus.prepend(draw_popover_header)
            else:
                bpy.types.VIEW3D_HT_header.prepend(draw_popover_header)

    if addon_prefs.toggle_popover == 'append': # bottom
       
        if addon_prefs.toggle_MT_menu == 'menu_special':
            bpy.types.VIEW3D_MT_object_context_menu.append(draw_popover)
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(draw_popover)
            bpy.types.VIEW3D_MT_edit_curve_context_menu.append(draw_popover)

        if addon_prefs.toggle_MT_menu == 'menu_header':
            if addon_prefs.toggle_MT_menu_location == 'header_editor_menus':
                bpy.types.VIEW3D_MT_editor_menus.append(draw_popover_header)
            else:
                bpy.types.VIEW3D_HT_header.append(draw_popover_header)

    if addon_prefs.toggle_popover == 'off':  
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_popover)    
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_popover)    
        bpy.types.VIEW3D_MT_edit_curve_context_menu.remove(draw_popover)    
        bpy.types.VIEW3D_MT_editor_menus.remove(draw_popover_header) 
        bpy.types.VIEW3D_HT_header.remove(draw_popover_header) 
        return None

# Menus #
def func_menu_properties(self, context):
    if (context.active_object):
        if (len(context.active_object.modifiers)):
            layout = self.layout
            draw_modifier_by_type_ui_properties(self, context, layout)

# UI: PROPERTIES # 
def update_properties(self, context):
    try:     
        bpy.types.DATA_PT_modifiers.remove(func_menu_properties)         
    except:
        pass
    
    addon_prefs = context.preferences.addons[__package__].preferences    
  
    if addon_prefs.toggle_layout_properties == True: # top        
        bpy.types.DATA_PT_modifiers.prepend(func_menu_properties) 
 
    else: 
        bpy.types.DATA_PT_modifiers.remove(func_menu_properties)  
        return None
