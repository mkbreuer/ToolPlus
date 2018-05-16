# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


# REGISTRY: MENU # 

addon_keymaps_menu = []

def update_menu_courier(self, context):
    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_courier == 'menu':

        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
                                                        
        kmi = km.keymap_items.new('tp_ops.tp_courier_batch', 'BACK_SLASH', 'PRESS') #add here your new key event
        #kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True, shift=True) #example


    if context.user_preferences.addons[__package__].preferences.tab_menu_courier == 'off':
        pass 



# REGISTRY: SPECIALMENU # 
def menu_func(self, context):
    layout = self.layout       
    layout.operator_context = 'INVOKE_REGION_WIN'
   
    icons = load_icons()     
    
    layout.separator()
   
    button_run = icons.get("icon_run")         
    layout.operator('tp_ops.tp_courier_batch', text="T+Courier", icon_value=button_run.icon_id)   



def update_to_special(self, context):

    try:       
        bpy.types.VIEW3D_MT_armature_specials.remove(menu_func) 
        bpy.types.VIEW3D_MT_edit_curve_specials.remove(menu_func) 
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_func)        
        bpy.types.VIEW3D_MT_object_specials.remove(menu_func)           
        bpy.types.VIEW3D_MT_particle_specials.remove(menu_func) 
        bpy.types.VIEW3D_MT_pose_specials.remove(menu_func) 
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_special_courier == 'add':

        bpy.types.VIEW3D_MT_armature_specials.append(menu_func) 
        bpy.types.VIEW3D_MT_edit_curve_specials.append(menu_func) 
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(menu_func)        
        bpy.types.VIEW3D_MT_object_specials.append(menu_func)           
        bpy.types.VIEW3D_MT_particle_specials.append(menu_func) 
        bpy.types.VIEW3D_MT_pose_specials.append(menu_func) 

    if context.user_preferences.addons[__package__].preferences.tab_special_courier == 'remove':
        pass 



# REGISTRY: HEADER # 
class VIEW3D_TP_Courier_Header_Menu(bpy.types.Header):
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
       return 
       
    def draw(self, context):
        layout = self.layout       

        icons = load_icons() 

        button_run = icons.get("icon_run")                          
        layout.operator('tp_ops.tp_courier_batch', text="", icon_value=button_run.icon_id)           


def update_to_header(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Courier_Header_Menu)          
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_header_courier == 'add':

        bpy.utils.register_class(VIEW3D_TP_Courier_Header_Menu)

    if context.user_preferences.addons[__package__].preferences.tab_header_courier == 'remove':
        pass 



# REGISTRY: PANEL # 
from toolplus_courier.courier_panel   import (VIEW3D_TP_Courier_Panel_TOOLS)
from toolplus_courier.courier_panel   import (VIEW3D_TP_Courier_Panel_UI)
from toolplus_courier.courier_panel   import (VIEW3D_TP_Courier_Panel_PROPS)

panels_courier = (VIEW3D_TP_Courier_Panel_TOOLS, VIEW3D_TP_Courier_Panel_UI, VIEW3D_TP_Courier_Panel_PROPS)

def update_panel_courier(self, context):
    try:
        for panel in panels_courier:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels_courier:
            
            if context.user_preferences.addons[__package__].preferences.tab_location_courier == 'tools':                
                                       
                VIEW3D_TP_Courier_Panel_TOOLS.bl_category = context.user_preferences.addons[__package__].preferences.tools_category_courier                
                bpy.utils.register_class(VIEW3D_TP_Courier_Panel_TOOLS)

            if context.user_preferences.addons[__package__].preferences.tab_location_courier == 'ui':
                
                bpy.utils.register_class(VIEW3D_TP_Courier_Panel_UI)        

            if context.user_preferences.addons[__package__].preferences.tab_location_courier == 'props':

                bpy.utils.register_class(VIEW3D_TP_Courier_Panel_PROPS)      

            if context.user_preferences.addons[__package__].preferences.tab_location_courier == 'off':
                pass 

    except:
        pass




