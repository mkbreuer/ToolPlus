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

EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE"]


# UI: HOTKEY MENU PIE # 
class VIEW3D_MT_Origin_Menu_Pie(bpy.types.Menu):
    bl_label = "Set Origin"
    bl_idname = "VIEW3D_MT_Origin_Menu_Pie"

    def draw(self, context):
        layout = self.layout
       
        menu_prefs = context.user_preferences.addons[__package__].preferences

        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()      
      

        #Box 1 L
        row = pie.split().column()
        
        button_origin_center_view = icons.get("icon_origin_center_view")
        row.operator("tpc_ot.set_origin_to", text="Origin to Center", icon_value=button_origin_center_view.icon_id).mode = "ORIGIN_CENTER"       

        obj = context.active_object
        if obj:
            if obj.type in {'MESH'}:
 
                if len(bpy.context.selected_objects) == 1:               
                    if context.mode in EDIT:                   
                        button_origin_center_loc = icons.get("icon_origin_center_loc")
                        row.operator("tpc_ot.snaporigin_modal", text="Object to Center", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"
                    else:                
                        button_origin_center_loc = icons.get("icon_origin_center_loc")
                        row.operator("tpc_ot.snaporigin_modal", text="Object to Center", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"

      
        #Box 2 R
        row = pie.split().column()
        
        button_origin_mass = icons.get("icon_origin_mass")           
        row.operator("tpc_ot.set_origin_to", text="Mass (Surface)", icon_value=button_origin_mass.icon_id).mode = "ORIGIN_CENTER_OF_MASS"
        row.operator("tpc_ot.set_origin_to", text="Mass (Volume)", icon_value=button_origin_mass.icon_id).mode = "ORIGIN_CENTER_OF_VOLUME"
     
       
        #Box 3 B
        row = pie.split().column()
        
        button_origin_tomesh = icons.get("icon_origin_tomesh")
        row.operator("tpc_ot.set_origin_to", text="Origin to Object", icon_value=button_origin_tomesh.icon_id).mode = "ORIGIN_GEOMETRY"
      
        button_origin_meshto = icons.get("icon_origin_meshto")
        row.operator("tpc_ot.set_origin_to", text="Object to Origin", icon_value=button_origin_meshto.icon_id).mode = "GEOMETRY_ORIGIN"


        #Box 4 T 
        row = pie.split().column()
        
        button_origin_cursor = icons.get("icon_origin_cursor")
        row.operator("tpc_ot.set_origin_to", text="Origin to Cursor", icon_value=button_origin_cursor.icon_id).mode = "ORIGIN_CURSOR"
            

        #Box 5 LT
        row = pie.split().column()
        
        if context.mode == 'OBJECT':

            selected = bpy.context.selected_objects
            n = len(selected)                         
            if n == 1:

                button_origin_tosnap = icons.get("icon_origin_tosnap")         
                row.operator("tpc_ot.origin_to_snap_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
                    
            if n > 1:
                button_origin_to_active = icons.get("icon_origin_to_active") 
                row.operator("tpc_ot.set_origin_to", text="Origin to Active", icon_value=button_origin_to_active.icon_id).mode = "COPY_ORIGIN, ORIGIN_CURSOR"   

       
        if context.mode == 'EDIT_MESH':

            button_origin_edm = icons.get("icon_origin_edm")   
            row.operator("tpc_ot.snaporigin_modal", text="M-Select-EdM", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"

            button_origin_obj = icons.get("icon_origin_obj")   
            row.operator("tpc_ot.snaporigin_modal", text="M-Select-ObM", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"



        #Box 6 RT 
        row = pie.split().column()
       
        if context.mode == 'EDIT_MESH':
 
            button_origin_ccc = icons.get("icon_origin_ccc")            
            row.operator("tpc_ot.origin_ccc","3P-Circle", icon_value=button_origin_ccc.icon_id)      
      
        if context.mode == 'OBJECT':        
            row.operator("tpc_ot.snap_to_bbox", text="BoundBoxM", icon="SNAP_PEEL_OBJECT")

        obj = context.active_object     
        if obj:                                                   
            if obj.type in {'MESH'}: 
                button_origin_bbox = icons.get("icon_origin_bbox")            
                row.operator("tpc_ot.bbox_origin_set", text="BoundBoxX", icon_value=button_origin_bbox.icon_id)                                 



        #Box 7 LB 
        row = pie.split().column()
      
        if context.mode == 'OBJECT':       
            obj = context.active_object
            if obj:
                if obj.type in {'MESH'}:

                    button_origin_selected= icons.get("icon_origin_selected")   
                    row.operator("tpc_ot.snaporigin_modal", text="Origin to Select", icon_value=button_origin_selected.icon_id).mode = "cursor, obm"  

        if context.mode in EDIT:  

            if context.mode == 'EDIT_MESH':    
                row.operator("tpc_ot.set_origin_to", text="Selected Mesh", icon ="EDIT").mode = "SELECTED_MESH, ORIGIN_CURSOR"  
            else:
                button_origin_obj = icons.get("icon_origin_obj")   
                row.operator("tpc_ot.set_origin_to","Select-ObM", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"  

        button_align_zero = icons.get("icon_align_zero")          
        row.operator("tpc_ot.zero_axis_menu", text="Zero to Axis", icon_value=button_align_zero.icon_id)      
                                          


        #Box 8 RB
        row = pie.split().column()
       
        if context.mode == 'OBJECT':  

            button_origin_distribute = icons.get("icon_origin_distribute")  
            row.operator("tpc_ot.distribute_objects", "Distribute", icon_value=button_origin_distribute.icon_id)

            button_origin_align = icons.get("icon_origin_align")                
            row.operator("tpc_ot.advanced_align_tools", "Advanced", icon_value=button_origin_align.icon_id)    
                        

        if context.mode in EDIT:   

            if context.mode == 'EDIT_MESH':
                row.operator("tpc_ot.set_origin_to", text="Linked Mesh", icon ="LINKED").mode = "LINKED_MESH, ORIGIN_CURSOR" 
            else:
                button_origin_edm = icons.get("icon_origin_edm")   
                row.operator("tpc_ot.set_origin_to","Select-EdM", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"       

            button_origin_mesh = icons.get("icon_origin_mesh")                
            row.operator("tpc_ot.origin_transform", "Advanced", icon_value=button_origin_mesh.icon_id)    

           
        
