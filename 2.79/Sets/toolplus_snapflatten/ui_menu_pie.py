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

import addon_utils

# UI: HOTKEY MENU PIE # 
class VIEW3D_MT_SnapFlatten_Menu_Pie(bpy.types.Menu):
    bl_label = "SnapFlatten"
    bl_idname = "VIEW3D_MT_SnapFlatten_Menu_Pie"

    def draw(self, context):
        layout = self.layout
       
        menu_prefs = context.user_preferences.addons[__package__].preferences

        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()      

        #Box 1 L
        row = pie.split().column()
        row.label(text="")
        
        #Box 2 R
        row = pie.split().column()
        row.label(text="")     
       
        #Box 3 B
        row = pie.split().column()
        row.operator("tpc_ot.snapflatten_modal", text="Flatten Y-Axis").mode="flatten_y"

        #Box 4 T 
        row = pie.split().column()
        row.label(text="")
       
        #Box 5 LT
        row = pie.split().column()
        loop_tools_addon = "mesh_looptools" 
        state = addon_utils.check(loop_tools_addon)
        if not state[0]: 
            row.label(text="")                       
        else:
            row.operator("tpc_ot.snapflatten_modal", text="Flatten LpT").mode="flatten_lpt"
       
        #Box 6 RT 
        row = pie.split().column()
        row.operator("tpc_ot.snapflatten_modal", text="Flatten Normal").mode="flatten_n"  

        #Box 7 LB 
        row = pie.split().column()
        row.operator("tpc_ot.snapflatten_modal", text="Flatten X-Axis").mode="flatten_x"
      
        #Box 8 RB
        row = pie.split().column()
        row.operator("tpc_ot.snapflatten_modal", text="Flatten Z-Axis").mode="flatten_z"      


