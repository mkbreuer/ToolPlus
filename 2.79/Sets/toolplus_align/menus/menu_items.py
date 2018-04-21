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
from .. icons.icons import load_icons    

import addon_utils

# LOAD MENU # 
from toolplus_align.menus.menu_normals        import (VIEW3D_TP_Translate_Normal_Menu)
from toolplus_align.menus.menu_normals        import (VIEW3D_TP_Rotate_Normal_Menu)
from toolplus_align.menus.menu_normals        import (VIEW3D_TP_Resize_Normal_Menu)


# UI: SUB MENU # 
def draw_item_transform_normal(self,context):
    layout = self.layout

    icons = load_icons()

    col = layout.column(align=True)

    col.scale_y = 1.3

    col.operator("transform.tosphere", text="To Sphere")
    col.operator("transform.shear", text="Shear")
    col.operator("transform.bend", text="Bend")

    col.separator() 

    col.menu("VIEW3D_TP_Translate_Normal_Menu", text="N-Translate")
    col.menu("VIEW3D_TP_Rotate_Normal_Menu", text="N-Rotate")
    col.menu("VIEW3D_TP_Resize_Normal_Menu", text="N-Scale")

    col.separator()     


from toolplus_align.menus.menu_machine        import (VIEW3D_TP_Machine_Align_Menu)

# UI: SUB MENU # 
def draw_item_machine(self,context):
    layout = self.layout

    meshmaschine_addon = "MESHmachine" 
    state = addon_utils.check(meshmaschine_addon)
    if not state[0]:   
        pass  
    else:   
        layout.menu("VIEW3D_TP_Machine_Align_Menu", text="MESHmachine")

        layout.separator()     
