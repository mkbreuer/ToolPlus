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


def draw_lattice_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        if context.mode == 'EDIT_LATTICE':

            box = layout.box().column(1)   
             
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

                       