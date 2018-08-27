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
import bpy, os
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE"]


def draw_origin_menu_layout(self, context, layout):
          
        icons = load_icons()

        button_origin_center_view = icons.get("icon_origin_center_view")
        layout.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

        button_origin_cursor = icons.get("icon_origin_cursor")
        layout.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

        layout.separator()

        button_origin_edm = icons.get("icon_origin_edm")            
        layout.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

        button_origin_obj = icons.get("icon_origin_obj")   
        layout.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)            

        if context.mode == 'EDIT_MESH':
             
            layout.separator()

            button_origin_ccc = icons.get("icon_origin_ccc")            
            layout.operator("tp_ops.origin_ccc","3P-Center", icon_value=button_origin_ccc.icon_id)       
      
            layout.separator() 
             
            button_origin_bbox = icons.get("icon_origin_bbox")       
            layout.operator("tp_ops.bbox_origin_set","BBox Origin", icon_value=button_origin_bbox.icon_id)



class VIEW3D_TP_Origin_Menu(bpy.types.Menu):
    bl_label = "Origin"
    bl_idname = "tp_menu.origin_base"   

    def draw(self, context):
        layout = self.layout

        icons = load_icons()          
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
      
  
        ob = context
        if ob.mode == 'OBJECT':

            button_origin_center_view = icons.get("icon_origin_center_view")
            layout.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            layout.operator("tp_ops.origin_set_cursor", text="3D Cursor", icon_value=button_origin_cursor.icon_id)

            layout.separator()
            
            button_origin_tomesh = icons.get("icon_origin_tomesh")
            layout.operator("tp_ops.origin_tomesh", text="Origin to Geom", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            layout.operator("tp_ops.origin_meshto", text="Geom to Origin", icon_value=button_origin_meshto.icon_id)

            if len(bpy.context.selected_objects) == 1: 
                
                button_origin_tosnap = icons.get("icon_origin_tosnap")         
                layout.operator("tp_ops.origin_modal", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
      

            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_tools
            if display_advanced == 'on':
                pass
            else:  
                if len(bpy.context.selected_objects) == 2: 
                    
                    button_origin_toactive = icons.get("icon_origin_toactive")         
                    layout.operator("tp_ops.origin_to_active", text="Align to Active", icon_value=button_origin_toactive.icon_id)

            layout.separator()

            button_origin_mass = icons.get("icon_origin_mass")           
            layout.operator("tp_ops.origin_set_mass", text="Center of Mass", icon_value=button_origin_mass.icon_id)

            layout.separator()

            if len(bpy.context.selected_objects) == 1: 

                button_origin_bbox = icons.get("icon_origin_bbox")                               
                layout.operator("object.bbox_origin_modal_ops", text="1-BBox Modal", icon_value=button_origin_bbox.icon_id)                                
                       
            if len(bpy.context.selected_objects) > 1: 
                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:

                        button_origin_bbox = icons.get("icon_origin_bbox")   
                        layout.operator("tp_ops.bbox_origin_set","X-BBox Bound", icon_value=button_origin_bbox.icon_id)
      

            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_tools
            if display_advanced == 'on':  

                layout.separator()

                button_origin_distribute = icons.get("icon_origin_distribute")  
                layout.operator("object.distribute_osc", "Distribute", icon_value=button_origin_distribute.icon_id)

                button_origin_align = icons.get("icon_origin_align")                
                layout.operator("tp_origin.align_tools", "Advanced", icon_value=button_origin_align.icon_id)    

 

        if ob.mode == 'EDIT_MESH':

            draw_origin_menu_layout(self, context, layout) 
                        

        if ob.mode == 'EDIT_CURVE':
            
            draw_origin_menu_layout(self, context, layout) 
     
        if ob.mode == 'EDIT_SURFACE':
            
            draw_origin_menu_layout(self, context, layout) 

        if ob.mode == 'EDIT_METABALL':
            
            draw_origin_menu_layout(self, context, layout) 
   
        if ob.mode == 'EDIT_LATTICE':
            
            draw_origin_menu_layout(self, context, layout)             
                 
        if  context.mode == 'PARTICLE':
       
            draw_origin_menu_layout(self, context, layout) 

        if ob.mode == 'EDIT_ARMATURE':

            draw_origin_menu_layout(self, context, layout)             

        if context.mode == 'POSE':

            draw_origin_menu_layout(self, context, layout) 


        if ob.mode in EDIT:   
               
            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_tools
            if display_advanced == 'on':  

                layout.separator()

                button_origin_mesh = icons.get("icon_origin_mesh")                
                layout.operator("tp_ops.origin_transform", "Advanced", icon_value=button_origin_mesh.icon_id)   
             

        layout.separator()
       
        button_align_zero = icons.get("icon_align_zero")                
        layout.operator("tp_ops.zero_axis_menu", "Zero to Axis", icon_value=button_align_zero.icon_id)      

