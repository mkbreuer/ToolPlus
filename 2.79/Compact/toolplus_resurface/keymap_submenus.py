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

from toolplus_resurface.ui_menus.menu_submenus  import*

# REGISTRY # 
def update_menu_submenus(self, context):

    try:
        bpy.types.VIEW3D_PT_tools_transform.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_PT_tools_transform_mesh.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_PT_tools_transform_curve.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_PT_tools_transform_surface.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_PT_tools_mballedit.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_PT_tools_latticeedit.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_MT_transform_object.remove(Draw_VIEW3D_TP_Transform_Normal)
        bpy.types.VIEW3D_MT_transform.remove(Draw_VIEW3D_TP_Transform_Normal)
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_submenus == 'menu':

        bpy.types.VIEW3D_PT_tools_transform.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_PT_tools_transform_mesh.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_PT_tools_transform_curve.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_PT_tools_transform_surface.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_PT_tools_mballedit.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_PT_tools_latticeedit.append(Draw_VIEW3D_TP_Transform_Normal)    
        bpy.types.VIEW3D_MT_transform_object.prepend(Draw_VIEW3D_TP_Transform_Normal)  
        bpy.types.VIEW3D_MT_transform.prepend(Draw_VIEW3D_TP_Transform_Normal)  

    if context.user_preferences.addons[__package__].preferences.tab_menu_submenus == 'off':
        pass



