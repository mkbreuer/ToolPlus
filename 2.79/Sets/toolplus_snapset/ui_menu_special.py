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
class VIEW3D_MT_SnapSet_Menu_Special(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Special"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        addon_prefs = context.user_preferences.addons[__package__].preferences

        if addon_prefs.tpc_use_grid == True:
            if addon_prefs.use_internal_icon_bta == True:  
                layout.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon=addon_prefs.icon_bta)
            else:
                button_snap_grid = icons.get("icon_snap_grid")
                layout.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon_value=button_snap_grid.icon_id)
 
        if addon_prefs.tpc_use_grid_modal == True:
            button_snap_grid = icons.get("icon_snap_grid")
            layout.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "grid"

                    
        if context.mode == 'OBJECT':

            if addon_prefs.tpc_use_place == True:
                if addon_prefs.use_internal_icon_btb == True:   
                    layout.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon=addon_prefs.icon_btb)
                else:
                    button_snap_place = icons.get("icon_snap_place")
                    layout.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon_value=button_snap_place.icon_id)
            
            if addon_prefs.tpc_use_place_modal == True:
                button_snap_place = icons.get("icon_snap_place")
                layout.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "place"

        else:
            if addon_prefs.tpc_use_retopo == True:
                if addon_prefs.use_internal_icon_btf == True:   
                    layout.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon=addon_prefs.icon_btf)    
                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    layout.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon_value=button_snap_retopo.icon_id)    
           
            if addon_prefs.tpc_use_retopo_modal == True:              
                button_snap_retopo = icons.get("icon_snap_retopo")
                layout.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "retopo"   
          

        if addon_prefs.use_internal_icon_btc == True:     
            layout.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon=addon_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            layout.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon_value=button_snap_cursor.icon_id) 


        if addon_prefs.use_internal_icon_bte == True:
            layout.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon=addon_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            layout.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon_value=button_snap_closest.icon_id)
            

        if addon_prefs.tpc_use_active == True: 
            if addon_prefs.use_internal_icon_btd == True:
                layout.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon=addon_prefs.icon_btd) 
            else:
                button_snap_active = icons.get("icon_snap_active")            
                layout.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon_value=button_snap_active.icon_id) 

            

def draw_snapset_item_special(self, context):
    layout = self.layout

    icons = load_icons()

    addon_prefs = context.user_preferences.addons[__package__].preferences
  
    if addon_prefs.tab_snapset_special == 'append':
        if addon_prefs.toggle_special_snapset_separator == True:
            layout.separator()      

    if addon_prefs.toggle_special_snapset_icon == True:
        button_snap_set = icons.get("icon_snap_set")
        layout.menu("VIEW3D_MT_SnapSet_Menu_Special", text="SnapSet", icon_value=button_snap_set.icon_id)      
    else:
        layout.menu("VIEW3D_MT_SnapSet_Menu_Special", text="SnapSet")      
    
    if addon_prefs.tab_snapset_special == 'prepend':
        if addon_prefs.toggle_special_snapset_separator == True:
            layout.separator()      


            






                  










