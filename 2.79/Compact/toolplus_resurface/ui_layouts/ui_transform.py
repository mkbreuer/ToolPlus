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


def draw_transform_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        
        
        icons = load_icons()

        col = layout.column(align=True)
                
        if not tp_props.display_copydim: 
          
            box = col.box().column(1)
            
            row = box.row(1)   

            row.prop(tp_props, "display_copydim", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Transform")

            #button_bloc = icons.get("icon_bloc") 
            #row.operator("tp_ops.copy_local_transform",text="", icon_value=button_bloc.icon_id )  

            button_move = icons.get("icon_apply_move") 
            props = row.operator("object.transform_apply", text="", icon_value=button_move.icon_id)
            props.location=True
            props.rotation=False
            props.scale=False

            button_rota = icons.get("icon_apply_rota") 
            props = row.operator("object.transform_apply", text="", icon_value=button_rota.icon_id)             
            props.location=False
            props.rotation=True
            props.scale=False
            
            button_scale = icons.get("icon_apply_scale") 
            props = row.operator("object.transform_apply", text="", icon_value=button_scale.icon_id)
            props.location=False
            props.rotation=False
            props.scale=True            
          

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_copydim", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Transform")  
          
            #button_bloc = icons.get("icon_bloc") 
            #row.operator("tp_ops.copy_local_transform",text="", icon_value=button_bloc.icon_id )  

            button_move = icons.get("icon_apply_move") 
            row.operator("object.transform_apply", text="", icon_value=button_move.icon_id).location=True

            button_rota = icons.get("icon_apply_rota") 
            row.operator("object.transform_apply", text="", icon_value=button_rota.icon_id).rotation=True                

            button_scale = icons.get("icon_apply_scale") 
            row.operator("object.transform_apply", text="", icon_value=button_scale.icon_id).scale=True  

           
            box = col.box().column(1)
         
            row = box.row(1)         
            row.label("Local Align")  

            row = box.row(1)   
            button_bloc = icons.get("icon_bloc") 
            row.operator("tp_ops.copy_local_transform", icon_value=button_bloc.icon_id )  

            box.separator()  
            

            box = col.box().column(1)
         
            row = box.row(1)         
            row.label("Arrest Transform")  

            row = box.row(1)   
            row.operator("tp_ops.lock_all", text="Lock all", icon="LOCKED").lock_mode = "lock"        
            row.operator("tp_ops.lock_all", text="Unlock all", icon="UNLOCKED").lock_mode = "unlock"   

            box.separator()  


            box = col.box().column(1)
         
            row = box.row(1)         
            row.label("Set To Delta")  
         
            row = box.row(1)            
            row.operator("object.transforms_to_deltas", text="All").mode='ALL'
            row.operator("object.transforms_to_deltas", text="Locate").mode='LOC'            
            row.operator("object.transforms_to_deltas", text="Rotate").mode='ROT' 
            row.operator("object.transforms_to_deltas", text="Scale").mode='SCALE' 

            box.separator()  

