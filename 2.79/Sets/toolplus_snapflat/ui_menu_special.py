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

 
# UI: HOTKEY MENU # 
class VIEW3D_MT_SnapFlat_Menu_Special(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapFlat_Menu_Special"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
        addon_prefs = context.user_preferences.addons[__package__].preferences
        
        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        layout.operator("tpc_ops.snapflat_modal", text="Flatten LpT").mode="flatten_lpt"
        
        layout.separator()

        layout.operator("tpc_ops.snapflat_modal", text="Flatten X-Axis").mode="flatten_x"
        layout.operator("tpc_ops.snapflat_modal", text="Flatten Y-Axis").mode="flatten_y"
        layout.operator("tpc_ops.snapflat_modal", text="Flatten Z-Axis").mode="flatten_z"
   
        layout.separator()
       
        layout.operator("tpc_ops.snapflat_modal", text="Flatten Normal").mode="flatten_n"
   
        layout.separator()

        layout.operator("tpc_ops.snapflat_modal", text="Boundary SharpEdges").mode="snap_for_sharp"
        layout.operator("tpc_ops.snapflat_modal", text="Boundary UV Seams").mode="snap_for_uvs"   

        layout.separator() 
      
        layout.prop(addon_prefs, 'mesh_select_mode', text="")   
        layout.prop(addon_prefs, 'threshold') 



def draw_snapflat_item_special(self, context):
    layout = self.layout

    icons = load_icons()

    addon_prefs = context.user_preferences.addons[__package__].preferences
    
    if addon_prefs.tab_snapflat_special == 'append':
        if addon_prefs.toggle_special_snapflat_separator == True:
            layout.separator()      

    if addon_prefs.toggle_special_snapflat_icon == True:        
        button_snap_flat = icons.get("icon_snap_flat")
        layout.menu("VIEW3D_MT_SnapFlat_Menu_Special", text="SnapFlat", icon_value=button_snap_flat.icon_id)      
    else:
        layout.menu("VIEW3D_MT_SnapFlat_Menu_Special", text="SnapFlat")     
                
    if addon_prefs.tab_snapflat_special == 'prepend':
        if addon_prefs.toggle_special_snapflat_separator == True:
            layout.separator()      



            






                  










