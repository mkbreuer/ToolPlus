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

# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons


EDIT = ["EDIT_MESH","EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']


# DRAW UI LAYOUT #
class draw_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        tp_props = context.window_manager.tp_recoplanar    
        
        icons = load_icons()     
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        col = layout.column(1)                                                
         
        panel_prefs = context.user_preferences.addons[__package__].preferences

        if panel_prefs.tab_recoplanar_layout == True: 

            box = col.box().column(1)

            row = box.row(1)                       
            if tp_props.display_alter: 
                row.prop(tp_props, "display_alter", text="", icon="COLLAPSEMENU")  
                box.separator()
            else:                  
                row.prop(tp_props, "display_alter", text="", icon="COLLAPSEMENU")  

      
            row.operator("tp_ops.set_new_local", text = "ReLocal") 
            row.operator("tp_ops.recenter")             
            row.operator("tp_ops.reposition")             

            button_bloc = icons.get("icon_bloc") 
            row.operator("tp_ops.copy_local_transform",text="", icon_value=button_bloc.icon_id ) 

            if tp_props.display_alter: 

                row = box.row(1)                                        
                row.operator("tp_ops.delete_dummy", text=" ", icon="PANEL_CLOSE")       

                row.operator("tp_ops.lock_all", text=" ", icon="LOCKED").lock_mode = "lock"        
                row.operator("tp_ops.lock_all", text=" ", icon="UNLOCKED").lock_mode = "unlock"   

                button_deltas = icons.get("icon_deltas") 
                row.operator("object.transforms_to_deltas", text=" ", icon_value=button_deltas.icon_id).mode='ALL'          

                button_center = icons.get("icon_center") 
                row.operator("tp_ops.relocate", text=" ", icon_value=button_center.icon_id)

                button_move = icons.get("icon_apply_move") 
                row.operator("object.transform_apply", text=" ", icon_value=button_move.icon_id).location=True

                button_rota = icons.get("icon_apply_rota") 
                row.operator("object.transform_apply", text=" ", icon_value=button_rota.icon_id).rotation=True                

                button_scale = icons.get("icon_apply_scale") 
                row.operator("object.transform_apply", text=" ", icon_value=button_scale.icon_id).scale=True  

            box.separator()   

        else:                                            
        
            box = col.box().column(1)

            box.separator()   
            
            row = box.row(1) 
            button_relocal = icons.get("icon_relocal") 
            row.operator("tp_ops.set_new_local", icon_value=button_relocal.icon_id) 

            button_recenter = icons.get("icon_recenter") 
            row.operator("tp_ops.recenter", icon_value=button_recenter.icon_id)   
        
            row = box.row(1) 
         
            button_center = icons.get("icon_center") 
            row.operator("tp_ops.relocate", text="ReLocate", icon_value=button_center.icon_id)    

            button_reposition = icons.get("icon_reposition") 
            row.operator("tp_ops.reposition", icon_value=button_reposition.icon_id)
        
            row = box.row(1)                                        
            row.operator("tp_ops.delete_dummy", text="Delete", icon="PANEL_CLOSE")      

            button_deltas = icons.get("icon_deltas") 
            row.operator("object.transforms_to_deltas", text="DeltaAll", icon_value=button_deltas.icon_id).mode='ALL'          

            box.separator()   

                                                   
            box = col.box().column(1)
            
            box.separator()   
            
            row = box.row(1)                                        
            button_bloc = icons.get("icon_bloc") 
            row.operator("tp_ops.copy_local_transform",text=" ", icon_value=button_bloc.icon_id )  

            row.operator("tp_ops.lock_all", text=" ", icon="LOCKED").lock_mode = "lock"        
            row.operator("tp_ops.lock_all", text=" ", icon="UNLOCKED").lock_mode = "unlock"         

            button_move = icons.get("icon_apply_move") 
            row.operator("object.transform_apply", text=" ", icon_value=button_move.icon_id).location=True

            button_rota = icons.get("icon_apply_rota") 
            row.operator("object.transform_apply", text=" ", icon_value=button_rota.icon_id).rotation=True                

            button_scale = icons.get("icon_apply_scale") 
            row.operator("object.transform_apply", text=" ", icon_value=button_scale.icon_id).scale=True  


            box.separator()

    
    
    
class VIEW3D_TP_ReCoPlanar_UI(bpy.types.Panel, draw_panel_layout):
    bl_idname = "VIEW3D_TP_ReCoPlanar_UI"
    bl_label = "ReCoPlanar"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
         

class VIEW3D_TP_ReCoPlanar_TOOLS(bpy.types.Panel, draw_panel_layout):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_ReCoPlanar_TOOLS"
    bl_label = "ReCoPlanar"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}