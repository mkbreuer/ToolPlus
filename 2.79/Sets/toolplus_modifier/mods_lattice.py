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


def draw_mods_lattice_layout(self, context, layout):
      
    tp_props = context.window_manager.tp_collapse_menu_modifier         
   

    col = layout.column(align=True)  
            
    box = col.box().column(1)
    
    row = box.row(1)
    if tp_props.display_lattice:            
        row.prop(tp_props, "display_lattice", text="", icon="MOD_LATTICE")
    else:
        row.prop(tp_props, "display_lattice", text="", icon="MOD_LATTICE")
        
    row.label("Easy Lattice")

    box.separator()                       
     
    row = box.row(1)     
    row.prop(context.object.data, "use_outside")
    row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

    box.separator()                       

    row = box.row(1)
    row.prop(context.object.data, "points_u", text="X")
    row.prop(context.object.data, "points_v", text="Y")
    row.prop(context.object.data, "points_w", text="Z")
 
    row = box.row(1)
    row.prop(context.object.data, "interpolation_type_u", text="")
    row.prop(context.object.data, "interpolation_type_v", text="")
    row.prop(context.object.data, "interpolation_type_w", text="")  

    box.separator()                       

    row = box.row(1)
    row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")
  
    box.separator()    

    row = box.row(1)
    row.label('Selection', icon ="RESTRICT_SELECT_OFF")
    row.operator("lattice.select_ungrouped", text="Ungrouped") 
               
    row = box.row(1) 
    row.operator("lattice.select_all", text="All").action = 'TOGGLE'
    row.operator("lattice.select_all", text="Inverse").action = 'INVERT'

    row = box.row(1)
    row.operator("lattice.select_random", text="Random") 
    row.operator("lattice.select_mirror", text="Mirror") 

    box.separator()

    row = box.row()         
    if tp_props.display_vertgrp:                       
        row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")
    else:
        row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")                     
        
    box.separator() 
    
    if not tp_props.display_vertgrp:                                                                              
        
        row = box.row()
        obj = context.object
        if obj:                                
            row.template_list("MESH_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=4)           

        split = row.split(1)
        row = split.column(1)
        row.operator("object.vertex_group_add", icon='ZOOMIN', text="")
        row.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
        row.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
        row.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
        row.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                

        box.separator()  
        
        row = box.row(1)
        row.operator("object.vertex_group_assign", text="Assign", icon="ZOOMIN") 
        row.operator("object.vertex_group_remove_from", text="Remove", icon="ZOOMOUT") 

        row = box.row(1)                    
        row.operator("object.vertex_group_select", text="Select", icon="RESTRICT_SELECT_OFF")
        row.operator("object.vertex_group_deselect", text="Deselect", icon="RESTRICT_SELECT_ON")
        
        row = box.row(1)
        row.prop(context.tool_settings, "vertex_group_weight", text="Weight")
  
        box.separator()   

