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


def draw_recoplanar_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        
        icons = load_icons()

        col = layout.column(align=True)
                
        if not tp_props.display_recoplanar: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_recoplanar", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Coplanar")

            button_relocal = icons.get("icon_relocal") 
            row.operator("tp_ops.set_new_local",text="", icon_value=button_relocal.icon_id) 

            button_recenter = icons.get("icon_recenter") 
            row.operator("tp_ops.recenter",text="", icon_value=button_recenter.icon_id)   

            button_reposition = icons.get("icon_reposition") 
            row.operator("tp_ops.reposition",text="", icon_value=button_reposition.icon_id)

        else:

            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_recoplanar", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Coplanar")     

            button_relocal = icons.get("icon_relocal") 
            row.operator("tp_ops.set_new_local",text="", icon_value=button_relocal.icon_id) 

            button_recenter = icons.get("icon_recenter") 
            row.operator("tp_ops.recenter",text="", icon_value=button_recenter.icon_id)   

            button_reposition = icons.get("icon_reposition") 
            row.operator("tp_ops.reposition",text="", icon_value=button_reposition.icon_id)
            
            box = col.box().column(1)

            row = box.row(1) 
            button_relocal = icons.get("icon_relocal") 
            row.operator("tp_ops.set_new_local", icon_value=button_relocal.icon_id) 

            button_recenter = icons.get("icon_recenter") 
            row.operator("tp_ops.recenter", icon_value=button_recenter.icon_id)   
        
            row = box.row(1) 
         
            button_center = icons.get("icon_center") 
            row.operator("tp_ops.relocate", text="Relocate", icon_value=button_center.icon_id)    

            button_reposition = icons.get("icon_reposition") 
            row.operator("tp_ops.reposition", icon_value=button_reposition.icon_id)
        
            row = box.row(1)                                        
            row.operator("tp_ops.delete_dummy", text="Delete", icon="PANEL_CLOSE")      

            button_deltas = icons.get("icon_deltas") 
            row.operator("object.transforms_to_deltas", text="DeltaAll", icon_value=button_deltas.icon_id).mode='ALL'          

            box.separator()   

