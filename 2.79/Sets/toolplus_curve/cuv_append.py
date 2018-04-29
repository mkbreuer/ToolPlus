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

# LOAD UI #  
from toolplus_curve.menus.menu_item  import (draw_item_curve)
#from toolplus_curve.menus.menu_item  import (draw_item_special)
from toolplus_curve.menus.menu_item  import (draw_item_surface)
from toolplus_curve.menus.menu_item  import (draw_item_mesh)
from toolplus_curve.menus.menu_item  import (draw_item_delete)
from toolplus_curve.menus.menu_item  import (draw_item_SVG)
from toolplus_curve.menus.menu_item  import (draw_item_editor_graph)
from toolplus_curve.menus.menu_item  import (draw_item_editor_dopesheet)

# LOAD MODUL #    
import bpy
from bpy import *


# REGISTRY: APPEND MENUS # 

def update_append_menus(self, context):

    try:
        # REMOVE FROM MENUS #
        bpy.types.INFO_MT_curve_add.remove(draw_item_curve)
        bpy.types.INFO_MT_surface_add.remove(draw_item_surface)
        bpy.types.INFO_MT_mesh_add.remove(draw_item_mesh)
#        bpy.types.VIEW3D_MT_edit_curve_specials.remove(draw_item_spezial) 
        bpy.types.VIEW3D_MT_edit_curve_delete.remove(draw_item_delete)
        bpy.types.INFO_MT_file_import.remove(draw_item_SVG)         
        bpy.types.GRAPH_MT_channel.remove(draw_item_editor_graph)
        bpy.types.DOPESHEET_MT_channel.remove(draw_item_editor_dopesheet)
        
    except:
        pass

    # APPEND MENUS #  
    if context.user_preferences.addons[__package__].preferences.tab_menu_append == 'add':
       
        # ADD MENUS #  
        if context.user_preferences.addons[__package__].preferences.tab_append_add == True:
                       
            bpy.types.INFO_MT_curve_add.append(draw_item_curve)                   
            bpy.types.INFO_MT_surface_add.append(draw_item_surface)
            bpy.types.INFO_MT_mesh_add.append(draw_item_mesh)
       
#        # SPECIAL #  
#        if context.user_preferences.addons[__package__].preferences.tab_append_special == True:       
#          
#            bpy.types.VIEW3D_MT_edit_curve_specials.append(draw_item_special)

        # DELETE #            
        if context.user_preferences.addons[__package__].preferences.tab_append_delete == True:              
            
            bpy.types.VIEW3D_MT_edit_curve_delete.append(draw_item_delete)

        # IMPORT #
        if context.user_preferences.addons[__package__].preferences.tab_append_import == True:            
            
            bpy.types.INFO_MT_file_import.append(draw_item_SVG)   

        # EDITORS #
        if context.user_preferences.addons[__package__].preferences.tab_append_editors == True:

            bpy.types.GRAPH_MT_channel.append(draw_item_editor_graph)
            bpy.types.DOPESHEET_MT_channel.append(draw_item_editor_dopesheet)


    # REMOVE MENUS #  
    if context.user_preferences.addons[__package__].preferences.tab_menu_append == 'remove':  
        pass

