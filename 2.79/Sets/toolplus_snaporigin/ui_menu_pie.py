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
class VIEW3D_MT_SnapOrigin_Menu_Pie(bpy.types.Menu):
    bl_label = "SnapOrigin"
    bl_idname = "VIEW3D_MT_SnapOrigin_Menu_Pie"

    def draw(self, context):
        layout = self.layout
       
        menu_prefs = context.user_preferences.addons[__package__].preferences

        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()      
      
        if context.mode == 'OBJECT':

            if len(bpy.context.selected_objects) == 1: 

                #Box 1 L
                row = pie.split().column()
                button_origin_bbox = icons.get("icon_origin_bbox")                               
                row.operator("tpc_ot.snap_to_bbox", text="Origin to BBox", icon="SNAP_PEEL_OBJECT")     
                
                #Box 2 R
                row = pie.split().column()
                button_origin_center_loc = icons.get("icon_origin_center_loc")
                row.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"
               
                #Box 3 B
                row = pie.split().column()
                button_origin_edm = icons.get("icon_origin_edm")   
                row.operator("tpc_ot.snaporigin_modal", text="Origin to Mesh", icon_value=button_origin_edm.icon_id).mode = "cursor, obm"    
            
                #Box 4 T 
                row = pie.split().column()
                button_origin_tosnap = icons.get("icon_origin_tosnap")         
                row.operator("tpc_ot.snap_to_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
            
            else:

                #Box 1 L
                row = pie.split().column()
                row.label(text="Only for 1")
                
                #Box 2 R
                row = pie.split().column()
                row.label(text="object")

                #Box 3 B
                row = pie.split().column()
                row.label(text="allowed!")
            
                #Box 4 T 
                row = pie.split().column()
                row.label(text="selected")

           
            #Box 5 LT
            row = pie.split().column()
            row.label(text="")
           
            #Box 6 RT 
            row = pie.split().column()
            row.label(text="")

            #Box 7 LB 
            row = pie.split().column()
            row.label(text="")
          
            #Box 8 RB
            row = pie.split().column()
            row.label(text="")   

       
        else:

            #Box 1 L
            row = pie.split().column()
            button_origin_edm = icons.get("icon_origin_edm")   
            row.operator("tpc_ot.snaporigin_modal", text="Edm-Select", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"
            
            #Box 2 R
            row = pie.split().column()
            button_origin_center_loc = icons.get("icon_origin_center_loc")
            row.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"
           
            #Box 3 B
            row = pie.split().column()
            button_origin_obj = icons.get("icon_origin_obj")   
            row.operator("tpc_ot.snaporigin_modal", text="Obm-Select", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"
        
            #Box 4 T 
            row = pie.split().column()
            row.label(text="")
           
            #Box 5 LT
            row = pie.split().column()
            row.label(text="")
           
            #Box 6 RT 
            row = pie.split().column()
            row.label(text="")

            #Box 7 LB 
            row = pie.split().column()
            row.label(text="")
          
            #Box 8 RB
            row = pie.split().column()
            row.label(text="")  

