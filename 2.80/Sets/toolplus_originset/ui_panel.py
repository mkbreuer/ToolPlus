# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    

EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE"]
CLICK_MODE = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE"]
CLICK_OBJECT = {'MESH', 'SURFACE', 'CURVE'}
MESH_MODE = ["OBJECT", "EDIT_MESH"]
MESH_OBJECT = {'MESH'}


def draw_originset_edit_layout(self, context, layout):
          
    icons = load_icons()
    
    addon_prefs = context.preferences.addons[__package__].preferences

    layout.scale_y = addon_prefs.ui_scale_y
     
    if addon_prefs.use_button_icons ==True: 
        button_origin_to_selected = icons.get("icon_origin_to_selected")   
        layout.operator("tpc_ops.set_origin_to_edit", text="Selected Edit", icon_value=button_origin_to_selected.icon_id)             
    else:                     
        layout.operator("tpc_ops.set_origin_to_edit", text="Selected Edit")         



# DRAW UI LAYOUT #
def draw_originset_default_ui(self, context, layout):
    
    addon_prefs = context.preferences.addons[__package__].preferences
    
    icons = load_icons()
     
    layout.operator_context = 'INVOKE_REGION_WIN'

    layout.scale_y = addon_prefs.ui_scale_y

    view_layer = bpy.context.view_layer      
    obj = view_layer.objects.active

    if addon_prefs.display_tpc_origin_to_cursor == True:     
        if addon_prefs.use_button_icons ==True:
            button_origin_to_cursor = icons.get("icon_origin_to_cursor")
            layout.operator("tpc_ops.set_origin_to", text="Origin to Cursor", icon_value=button_origin_to_cursor.icon_id).mode = "ORIGIN_CURSOR"
        else:                
            layout.operator("tpc_ops.set_origin_to", text="Origin to Cursor").mode = "ORIGIN_CURSOR"

    if addon_prefs.display_tpc_origin_to_center == True:
        if addon_prefs.use_button_icons ==True:
            button_origin_to_center_view = icons.get("icon_origin_to_center_view")
            layout.operator("tpc_ops.set_origin_to", text="Origin to Center", icon_value=button_origin_to_center_view.icon_id).mode = "ORIGIN_CENTER"     
        else:  
            layout.operator("tpc_ops.set_origin_to", text="Origin to Center").mode = "ORIGIN_CENTER"       

    if addon_prefs.display_tpc_origin_to_object == True:      
        if addon_prefs.use_button_icons ==True: 
            button_origin_to_object = icons.get("icon_origin_to_object")
            layout.operator("tpc_ops.set_origin_to", text="Origin to Object", icon_value=button_origin_to_object.icon_id).mode = "ORIGIN_GEOMETRY"
        else:                    
            layout.operator("tpc_ops.set_origin_to", text="Origin to Object").mode = "ORIGIN_GEOMETRY"

    if addon_prefs.display_tpc_object_to_origin == True:                 
        if addon_prefs.use_button_icons ==True: 
            button_object_to_origin = icons.get("icon_object_to_origin")
            layout.operator("tpc_ops.set_origin_to", text="Object to Origin", icon_value=button_object_to_origin.icon_id).mode = "GEOMETRY_ORIGIN"               
        else:                 
            layout.operator("tpc_ops.set_origin_to", text="Object to Origin").mode = "GEOMETRY_ORIGIN"

    if addon_prefs.display_tpc_mass_surface == True:                    
        if addon_prefs.use_button_icons ==True: 
            button_origin_to_surface = icons.get("icon_origin_to_surface")             
            layout.operator("tpc_ops.set_origin_to", text="Mass (Surface)", icon_value=button_origin_to_surface.icon_id).mode = "ORIGIN_CENTER_OF_MASS"
        else:                 
            layout.operator("tpc_ops.set_origin_to", text="Mass (Surface)").mode = "ORIGIN_CENTER_OF_MASS"

    if addon_prefs.display_tpc_mass_surface == True:          
        if addon_prefs.use_button_icons ==True:             
            button_origin_to_volume = icons.get("icon_origin_to_volume") 
            layout.operator("tpc_ops.set_origin_to", text="Mass (Volume)", icon_value=button_origin_to_volume.icon_id).mode = "ORIGIN_CENTER_OF_VOLUME"
        else:    
            layout.operator("tpc_ops.set_origin_to", text="Mass (Volume)").mode = "ORIGIN_CENTER_OF_VOLUME"
   



# DRAW UI LAYOUT #
def draw_originset_ui(self, context, layout):
    
    addon_prefs = context.preferences.addons[__package__].preferences
    
    icons = load_icons()
     
    layout.operator_context = 'INVOKE_REGION_WIN'

    layout.scale_y = addon_prefs.ui_scale_y

    view_layer = bpy.context.view_layer      
    obj = view_layer.objects.active

    if context.mode == 'OBJECT':      
        if addon_prefs.display_tpc_hide_defaults_in_object == False:  
            draw_originset_default_ui(self, context, layout)


    if addon_prefs.display_tpc_hide_defaults_in_edit == False:     
        if context.mode in EDIT:
            draw_originset_default_ui(self, context, layout)


    if addon_prefs.display_tpc_origin_to_click_point == True: 
        if context.mode in CLICK_MODE:  
            if obj: 
                if obj.type in CLICK_OBJECT:
                    if addon_prefs.use_button_icons ==True:   
                        button_origin_to_click_point = icons.get("icon_origin_to_click_point")   
                        layout.operator("tpc_ops.snap_origin_to_click_point", text="Click Point", icon_value=button_origin_to_click_point.icon_id) 
                    else:                             
                        layout.operator("tpc_ops.snap_origin_to_click_point", text="Click Point") 
                       
    if context.mode == 'OBJECT':  
                  
        if addon_prefs.display_tpc_origin_to_snap_point == True:                                     
            if addon_prefs.use_button_icons ==True:   
                button_origin_to_snap_point = icons.get("icon_origin_to_snap_point")         
                layout.operator("tpc_ops.origin_to_snap_point", text="Snap Point", icon_value=button_origin_to_snap_point.icon_id)
            else:                           
                layout.operator("tpc_ops.origin_to_snap_point", text="Snap Point")
      
    if context.mode == 'EDIT_MESH':
       
        if addon_prefs.display_tpc_3_vert_circle == True:                      
            if addon_prefs.use_button_icons ==True:  
                button_origin_to_cc = icons.get("icon_origin_to_cc")                     
                layout.operator("tpc_ops.origin_to_ccc", text="3Vert Circle", icon_value=button_origin_to_cc.icon_id)          
            else:                     
                layout.operator("tpc_ops.origin_to_ccc", text="3Vert Circle")      

        if addon_prefs.display_tpc_set_origin_to_edit_mesh == True:                         
            if addon_prefs.use_button_icons ==True:  
                button_origin_to_selected = icons.get("icon_origin_to_selected")  
                layout.operator("tpc_ops.set_origin_to_edit_mesh", text="Selected Edit", icon_value=button_origin_to_selected.icon_id)  
            else:                    
                layout.operator("tpc_ops.set_origin_to_edit_mesh", text="Selected Edit")  
 


    if addon_prefs.display_tpc_set_origin_to_edit == True:
     
        if context.mode == 'EDIT_CURVE':            
            draw_originset_edit_layout(self, context, layout) 
     
        if context.mode == 'EDIT_SURFACE':            
            draw_originset_edit_layout(self, context, layout) 

        if context.mode == 'EDIT_METABALL':            
            draw_originset_edit_layout(self, context, layout) 
       
        if context.mode == 'EDIT_LATTICE':            
            draw_originset_edit_layout(self, context, layout)             
                 
        if  context.mode == 'PARTICLE':       
            draw_originset_edit_layout(self, context, layout) 

        if context.mode == 'EDIT_ARMATURE':
            draw_originset_edit_layout(self, context, layout)             

        if context.mode == 'POSE':
            draw_originset_edit_layout(self, context, layout)  

 

    if context.mode in EDIT:
        if addon_prefs.display_tpc_align_to_axis == True:   
            if addon_prefs.use_button_icons ==True: 
                button_origin_align_mesh = icons.get("icon_origin_align_mesh")                
                layout.operator("tpc_ops.align_to_axis", text="Advanced Align", icon_value=button_origin_align_mesh.icon_id)    
            else:                      
                layout.operator("tpc_ops.align_to_axis", text="Advanced Align")   
                            
    else:            

        if addon_prefs.display_tpc_snap_to_bbox_multi == True: 
            if context.mode in MESH_MODE:  
                if obj: 
                    if obj.type in MESH_OBJECT: 
                        if addon_prefs.use_button_icons ==True:  
                            button_origin_to_bbox_multi = icons.get("icon_origin_to_bbox_multi")   
                            layout.operator("tpc_ops.snap_to_bbox_multi", text="BBox Multi", icon_value=button_origin_to_bbox_multi.icon_id)
                        else:                    
                            layout.operator("tpc_ops.snap_to_bbox_multi", text="BBox Multi")

        if addon_prefs.display_tpc_snap_to_bbox_modal == True:  
            if addon_prefs.use_button_icons ==True:  
                button_origin_to_bbox_modal = icons.get("icon_origin_to_bbox_modal")   
                layout.operator("tpc_ops.snap_to_bbox", text="BBox Modal", icon_value=button_origin_to_bbox_modal.icon_id)
            else:                    
                layout.operator("tpc_ops.snap_to_bbox", text="BBox Modal")

        
        if addon_prefs.display_tpc_distribute_origins == True:   
            if addon_prefs.use_button_icons ==True:     
                button_icon_distribute_origins = icons.get("icon_distribute_origins")                
                layout.operator("tpc_ops.distribute_origins", text="Distribute XYZ", icon_value=button_icon_distribute_origins.icon_id)       
            else:                      
                layout.operator("tpc_ops.distribute_origins", text="Distribute XYZ")    


        if addon_prefs.display_tpc_advanced_align_tools == True:   
            if addon_prefs.use_button_icons ==True:     
                button_origin_align_object = icons.get("icon_origin_align_object")                
                layout.operator("tpc_ops.advanced_align_tools", text="Advanced Align", icon_value=button_origin_align_object.icon_id)       
            else:                      
                layout.operator("tpc_ops.advanced_align_tools", text="Advanced Align")    


    if addon_prefs.display_tpc_zero_to_axis == True:  
        if addon_prefs.use_button_icons ==True:   
            button_align_to_zero = icons.get("icon_align_to_zero")          
            layout.operator("tpc_ops.zero_to_axis", text="Zero to XYZ Axis", icon_value=button_align_to_zero.icon_id)               
        else: 
            layout.operator("tpc_ops.zero_to_axis", text="Zero to XYZ Axis")   


