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
class VIEW3D_MT_SnapOrigin_Menu_Special(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapOrigin_Menu_Special"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        menu_prefs = context.user_preferences.addons[__package__].preferences

        
        if context.mode == 'OBJECT':

            if len(bpy.context.selected_objects) == 1: 
              
                button_origin_tosnap = icons.get("icon_origin_tosnap")         
                layout.operator("tpc_ot.snap_to_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
                
                button_origin_edm = icons.get("icon_origin_edm")   
                layout.operator("tpc_ot.snaporigin_modal", text="Origin to Mesh", icon_value=button_origin_edm.icon_id).mode = "cursor, obm"     
                
                layout.separator()
              
                button_origin_bbox = icons.get("icon_origin_bbox")                               
                layout.operator("tpc_ot.snap_to_bbox", text="Origin to BBox", icon="SNAP_PEEL_OBJECT")                              

                layout.separator()
                
                button_origin_center_loc = icons.get("icon_origin_center_loc")
                layout.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"
          
            else:
                layout.label(text="Only for 1")
                layout.label(text="selected")
                layout.label(text="object")
                layout.label(text="allowed!")
     
        else:

            button_origin_edm = icons.get("icon_origin_edm")   
            layout.operator("tpc_ot.snaporigin_modal", text="Edm-Select", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"

            button_origin_obj = icons.get("icon_origin_obj")   
            layout.operator("tpc_ot.snaporigin_modal", text="Obm-Select", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"


            layout.separator() 
                 
            button_origin_center_loc = icons.get("icon_origin_center_loc")
            layout.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"

            

def draw_snaporigin_item_special(self, context):
    layout = self.layout

    icons = load_icons()
  
    if context.user_preferences.addons[__package__].preferences.tab_snaporigin_special == 'append':
        layout.separator()      

    button_snap_origin = icons.get("icon_snap_origin")
    layout.menu("VIEW3D_MT_SnapOrigin_Menu_Special", text="SnapOrigin", icon_value=button_snap_origin.icon_id)      
    
    if context.user_preferences.addons[__package__].preferences.tab_snaporigin_special == 'prepend':
        layout.separator()


            






                  










