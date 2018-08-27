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


def draw_knifes_ui(self, context, layout):        
        tp_props = context.window_manager.tp_props_resurface  

        icons = load_icons()     

        box = col.box().column(1)       
        
        row = box.row(1) 
        row.alignment = 'CENTER'               
        sub = row.row(1)
        sub.scale_x = 1.9  

        if not tp_props.display_knife: 
            sub.prop(tp_props, "display_knife", text="", icon="COLLAPSEMENU")  

            sub.operator("mesh.knife_project", text="", icon="LINE_DATA") 
            props = sub.operator("mesh.knife_tool", text="", icon="LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False                
            sub.operator("mesh.bisect", text="", icon="SCULPTMODE_HLT")
            sub.operator("mesh.ext_cut_faces", text="", icon = "SNAP_EDGE")     
            sub.operator("tp_ops.fastloop", text="", icon="GRIP") 

        else:                  
            box.separator() 
            sub.prop(tp_props, "display_knife", text="", icon="COLLAPSEMENU")                                
            sub.label("Knifes Tools")                   
 
        if tp_props.display_knife:      
          
            box.separator()  
         
            row = box.row(1)              
            row.operator("mesh.knife_project", icon="LINE_DATA")           
            props = row.operator("mesh.knife_tool", text="Knife Select", icon="LINE_DATA")
            props.use_occlude_geometry = False
            props.only_selected = True
                               
            box.separator() 


