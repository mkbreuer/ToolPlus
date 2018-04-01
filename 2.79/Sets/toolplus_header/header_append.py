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


# LOAD UI #  
from toolplus_header.header_menu  import (VIEW3D_TP_Header_Menus)

def update_menu_header(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_Header_Menus)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_header == 'add':

        bpy.utils.register_class(VIEW3D_TP_Header_Menus)

    if context.user_preferences.addons[__package__].preferences.tab_menu_header == 'remove':
        pass        
 



# LOAD UI #  
from toolplus_header.header_item  import (draw_header_item_view)

def update_submenu_header_view(self, context):

    try:
        # REMOVE FROM MENUS #
        bpy.types.VIEW3D_MT_view.remove(draw_header_item_view)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_append_view == 'add':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_view.append(draw_header_item_view)  

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_view.prepend(draw_header_item_view)  

    if context.user_preferences.addons[__package__].preferences.tab_menu_append_view == 'remove':  
        pass


from toolplus_header.header_item  import (draw_header_item_select)

def update_submenu_header_select(self, context):

    try:
        # REMOVE FROM MENUS #
        bpy.types.VIEW3D_MT_select_object.remove(draw_header_item_select)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_append_select == 'add':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_select_object.append(draw_header_item_select)  

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_select_object.prepend(draw_header_item_select)  

    if context.user_preferences.addons[__package__].preferences.tab_menu_append_select == 'remove':  
        pass



from toolplus_header.header_item  import (draw_header_item_add)

def update_submenu_header_add(self, context):

    try:
        # REMOVE FROM MENUS #
        bpy.types.INFO_MT_add.remove(draw_header_item_add)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_append_add == 'add':
       
        # ADD TO MENUS: TOP #
        bpy.types.INFO_MT_add.append(draw_header_item_add)  

        # ADD TO MENUS: BOTTOM #
        bpy.types.INFO_MT_add.prepend(draw_header_item_add)  

    if context.user_preferences.addons[__package__].preferences.tab_menu_append_add == 'remove':  
        pass



from toolplus_header.header_item  import (draw_header_item_object)

def update_submenu_header_objects(self, context):

    try:
        # REMOVE FROM MENUS #
        bpy.types.VIEW3D_MT_object.remove(draw_header_item_object)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_append_objects == 'add':
       
        # ADD TO MENUS: TOP #
        bpy.types.VIEW3D_MT_object.append(draw_header_item_object)  

        # ADD TO MENUS: BOTTOM #
        bpy.types.VIEW3D_MT_object.prepend(draw_header_item_object)  

    if context.user_preferences.addons[__package__].preferences.tab_menu_append_objects == 'remove':  
        pass




