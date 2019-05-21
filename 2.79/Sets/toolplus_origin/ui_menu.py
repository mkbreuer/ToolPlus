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
        
        panel_prefs = context.user_preferences.addons[__package__].preferences

        layout.scale_y = panel_prefs.scale_y

        if context.mode == 'EDIT_MESH':
            if panel_prefs.display_layout_separator_i == True: 
                layout.separator()   
                 
        if panel_prefs.display_select_edm == True:
            button_origin_edm = icons.get("icon_origin_edm")   
            layout.operator("tpc_ot.set_origin_to","Select-EdM", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"       
            
        if panel_prefs.display_select_obm == True:
            button_origin_obj = icons.get("icon_origin_obj")   
            layout.operator("tpc_ot.set_origin_to","Select-ObM", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"            
            
        if panel_prefs.display_advance_edm == True:
            if context.mode in EDIT:   

                if panel_prefs.display_layout_separator_j == True: 
                    layout.separator()   

                button_origin_mesh = icons.get("icon_origin_mesh")                
                layout.operator("tpc_ot.origin_transform", "Advanced", icon_value=button_origin_mesh.icon_id)   
                


class VIEW3D_MT_Origin_Menu(bpy.types.Menu):
    bl_label = "Set Origin"
    bl_idname = "VIEW3D_MT_Origin_Menu"   

    def draw(self, context):
        layout = self.layout
        
        panel_prefs = context.user_preferences.addons[__package__].preferences
        
        icons = load_icons()          
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = panel_prefs.scale_y

        if panel_prefs.display_origin_to_cursor == True:
            button_origin_cursor = icons.get("icon_origin_cursor")
            layout.operator("tpc_ot.set_origin_to", text="Origin to Cursor", icon_value=button_origin_cursor.icon_id).mode = "ORIGIN_CURSOR"

        if panel_prefs.display_layout_separator_a == True:
            layout.separator()
        
        if panel_prefs.display_origin_to_center == True:
            button_origin_center_view = icons.get("icon_origin_center_view")
            layout.operator("tpc_ot.set_origin_to", text="Origin to Center", icon_value=button_origin_center_view.icon_id).mode = "ORIGIN_CENTER"       

        if panel_prefs.display_object_to_center == True:
            if len(bpy.context.selected_objects) == 1:               
                if context.mode in EDIT:                   
                    button_origin_center_loc = icons.get("icon_origin_center_loc")
                    layout.operator("tpc_ot.snaporigin_modal", text="Object to Center", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"
                else:                
                    button_origin_center_loc = icons.get("icon_origin_center_loc")
                    layout.operator("tpc_ot.snaporigin_modal", text="Object to Center", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"       

        if panel_prefs.display_layout_separator_b == True:
            layout.separator()

        if panel_prefs.display_origin_to_object == True:
            button_origin_tomesh = icons.get("icon_origin_tomesh")
            layout.operator("tpc_ot.set_origin_to", text="Origin to Object", icon_value=button_origin_tomesh.icon_id).mode = "ORIGIN_GEOMETRY"

        if panel_prefs.display_object_to_origin == True:          
            button_origin_meshto = icons.get("icon_origin_meshto")
            layout.operator("tpc_ot.set_origin_to", text="Object to Origin", icon_value=button_origin_meshto.icon_id).mode = "GEOMETRY_ORIGIN"

        if panel_prefs.display_layout_separator_c == True:
            layout.separator()

        button_origin_mass = icons.get("icon_origin_mass") 
        if panel_prefs.display_mass_surface == True:            
            layout.operator("tpc_ot.set_origin_to", text="Mass (Surface)", icon_value=button_origin_mass.icon_id).mode = "ORIGIN_CENTER_OF_MASS"

        if panel_prefs.display_mass_surface == True:  
            layout.operator("tpc_ot.set_origin_to", text="Mass (Volume)", icon_value=button_origin_mass.icon_id).mode = "ORIGIN_CENTER_OF_VOLUME"


        if panel_prefs.display_layout_separator_d == True:       
            layout.separator() 

        if context.mode == 'EDIT_MESH':

            if panel_prefs.display_linked_mesh == True:            
                layout.operator("tpc_ot.set_origin_to", text="Linked Mesh", icon ="LINKED").mode = "LINKED_MESH, ORIGIN_CURSOR"
           
            if panel_prefs.display_selected_mesh == True:             
                layout.operator("tpc_ot.set_origin_to", text="Selected Mesh", icon ="EDIT").mode = "SELECTED_MESH, ORIGIN_CURSOR"   

            if panel_prefs.display_layout_separator_e == True: 
                layout.separator()

            if panel_prefs.display_mselect_edm == True:  
                button_origin_edm = icons.get("icon_origin_edm")   
                layout.operator("tpc_ot.snaporigin_modal", text="M-Select-Edm", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"

            if panel_prefs.display_mselect_obm == True:  
                button_origin_obj = icons.get("icon_origin_obj")   
                layout.operator("tpc_ot.snaporigin_modal", text="M-Select-Obm", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"

            if panel_prefs.display_layout_separator_f == True: 
                layout.separator()
           

        if context.mode == 'OBJECT':

            selected = bpy.context.selected_objects
            n = len(selected)  

            if panel_prefs.display_origin_to_snap == True:                         
                if n == 1:                
                    button_origin_tosnap = icons.get("icon_origin_tosnap")         
                    layout.operator("tpc_ot.origin_to_snap_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
          
            if panel_prefs.display_origin_to_select == True: 
                obj = context.active_object
                if obj:                
                    if obj.type in {'MESH'}:

                        button_origin_selected= icons.get("icon_origin_selected")   
                        layout.operator("tpc_ot.snaporigin_modal", text="Origin to Select", icon_value=button_origin_selected.icon_id).mode = "cursor, obm"  

            if panel_prefs.display_origin_to_active == True:                         
                if n > 1:
                    button_origin_to_active = icons.get("icon_origin_to_active") 
                    layout.operator("tpc_ot.set_origin_to", text="Origin to Active", icon_value=button_origin_to_active.icon_id).mode = "COPY_ORIGIN, ORIGIN_CURSOR"   


            if panel_prefs.display_layout_separator_g == True: 
                layout.separator()         

        if context.mode == 'EDIT_MESH':
           
            if panel_prefs.display_3_point_circle == True:           
                button_origin_ccc = icons.get("icon_origin_ccc")            
                layout.operator("tpc_ot.origin_ccc","3P-Circle", icon_value=button_origin_ccc.icon_id)      

        if context.mode == 'OBJECT':        
                  
            if panel_prefs.display_boundbox_m == True:  
                layout.operator("tpc_ot.snap_to_bbox", text="BoundBoxM", icon="SNAP_PEEL_OBJECT")
   
    
        if panel_prefs.display_boundbox_x == True:  
            obj = context.active_object     
            if obj:                                                               
                if obj.type in {'MESH'}: 
                                   
                    button_origin_bbox = icons.get("icon_origin_bbox")            
                    layout.operator("tpc_ot.bbox_origin_set", text="BoundBoxX", icon_value=button_origin_bbox.icon_id)                                 


        if context.mode == 'OBJECT':  

            if panel_prefs.display_layout_separator_h == True: 
                layout.separator()    

            if panel_prefs.display_distribute == True:   
                button_origin_distribute = icons.get("icon_origin_distribute")  
                layout.operator("tpc_ot.distribute_objects_menu", "Distribute", icon_value=button_origin_distribute.icon_id)

            if panel_prefs.display_advance_obm == True:   
                button_origin_align = icons.get("icon_origin_align")                
                layout.operator("tpc_ot.advanced_align_tools", "Advanced", icon_value=button_origin_align.icon_id)    
                                                      

        if context.mode == 'EDIT_MESH':
            draw_origin_menu_layout(self, context, layout) 

        if context.mode == 'EDIT_CURVE':            
            draw_origin_menu_layout(self, context, layout) 
     
        if context.mode == 'EDIT_SURFACE':            
            draw_origin_menu_layout(self, context, layout) 

        if context.mode == 'EDIT_METABALL':            
            draw_origin_menu_layout(self, context, layout) 
   
        if context.mode == 'EDIT_LATTICE':            
            draw_origin_menu_layout(self, context, layout)             
                 
        if  context.mode == 'PARTICLE':       
            draw_origin_menu_layout(self, context, layout) 

        if context.mode == 'EDIT_ARMATURE':
            draw_origin_menu_layout(self, context, layout)             

        if context.mode == 'POSE':
            draw_origin_menu_layout(self, context, layout) 


        if panel_prefs.display_layout_separator_k == True: 
            layout.separator()   
                       
        if panel_prefs.display_zero_to_axis == True:  
            button_align_zero = icons.get("icon_align_zero")          
            layout.operator("tpc_ot.zero_axis_menu", text="Zero to Axis", icon_value=button_align_zero.icon_id)        
