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
from toolplus_align.menus.menu_items        import (draw_item_transform_normal)


def update_submenu_normal(self, context):
    try:
        bpy.types.VIEW3D_PT_tools_transform.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_PT_tools_transform_mesh.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_PT_tools_transform_curve.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_PT_tools_transform_surface.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_PT_tools_mballedit.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_PT_tools_latticeedit.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_MT_transform_object.remove(draw_item_transform_normal)
        bpy.types.VIEW3D_MT_transform.remove(draw_item_transform_normal)
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_normal == 'menu':

        bpy.types.VIEW3D_PT_tools_transform.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_PT_tools_transform_mesh.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_PT_tools_transform_curve.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_PT_tools_transform_surface.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_PT_tools_mballedit.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_PT_tools_latticeedit.append(draw_item_transform_normal)    
        bpy.types.VIEW3D_MT_transform_object.prepend(draw_item_transform_normal)  
        bpy.types.VIEW3D_MT_transform.prepend(draw_item_transform_normal)  

    if context.user_preferences.addons[__package__].preferences.tab_menu_normal == 'off':
        pass




from toolplus_align.menus.menu_items        import (draw_item_machine)


def update_submenu_machine(self, context):
    try:
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(draw_item_machine)
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_submenu_machine == 'menu':

        bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(draw_item_machine)    

    if context.user_preferences.addons[__package__].preferences.tab_submenu_machine == 'off':
        pass




