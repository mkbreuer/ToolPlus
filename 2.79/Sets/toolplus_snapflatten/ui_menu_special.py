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
 
# UI: HOTKEY MENU # 
class VIEW3D_MT_SnapFlatten_Menu_Special(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapFlatten_Menu_Special"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        loop_tools_addon = "mesh_looptools" 
        state = addon_utils.check(loop_tools_addon)
        if not state[0]:                                     
            pass
        else:
            layout.operator("tpc_ot.snapflatten_modal", text="Flatten LpT").mode="flatten_lpt"
            
            layout.separator()

        layout.operator("tpc_ot.snapflatten_modal", text="Flatten X-Axis").mode="flatten_x"
        layout.operator("tpc_ot.snapflatten_modal", text="Flatten Y-Axis").mode="flatten_y"
        layout.operator("tpc_ot.snapflatten_modal", text="Flatten Z-Axis").mode="flatten_z"
   
        layout.separator()
       
        layout.operator("tpc_ot.snapflatten_modal", text="Flatten Normal").mode="flatten_n"




def draw_snapflatten_item_special(self, context):
    layout = self.layout

    icons = load_icons()
  
    if context.user_preferences.addons[__package__].preferences.tab_snapflatten_special == 'append':
        layout.separator()      

    button_snap_flatten = icons.get("icon_snap_flatten")
    layout.menu("VIEW3D_MT_SnapFlatten_Menu_Special", text="SnapFlatten", icon_value=button_snap_flatten.icon_id)      
    
    if context.user_preferences.addons[__package__].preferences.tab_snapflatten_special == 'prepend':
        layout.separator()


            






                  










