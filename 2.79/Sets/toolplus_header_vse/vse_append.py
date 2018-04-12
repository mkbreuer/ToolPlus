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
from toolplus_header_vse.vse_menu  import (VIEW3D_TP_VSE_HEADER_Menu)

def update_menu_vse(self, context):

    try:
        bpy.utils.unregister_class(VIEW3D_TP_VSE_HEADER_Menu)  
        
    except:
        pass
    
    if context.user_preferences.addons[__package__].preferences.tab_menu_vse == 'add':

        bpy.utils.register_class(VIEW3D_TP_VSE_HEADER_Menu)

    if context.user_preferences.addons[__package__].preferences.tab_menu_vse == 'remove':
        pass        
 


