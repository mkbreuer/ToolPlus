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


def draw_relax_ui(self, context, layout):
        tp = context.window_manager.tp_props_looptools            
        tp_props = context.window_manager.tp_props_resurface      
        
        icons = load_icons()

        col = layout.column(align=True)
                
        if not tp_props.display_relax: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_relax", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Relaxing")               
          
            button_align_vertices = icons.get("icon_align_vertices") 
            row.operator("mesh.vertices_smooth", text="", icon_value=button_align_vertices.icon_id) 

            button_align_laplacian = icons.get("icon_align_laplacian")
            row.operator("mesh.vertices_smooth_laplacian", text="" , icon_value=button_align_laplacian.icon_id)  

            button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
            row.operator("mesh.shrinkwrap_smooth", text="", icon_value=button_align_shrinkwrap.icon_id)         
            

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_relax", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Relaxing")  

                     
            button_align_vertices = icons.get("icon_align_vertices") 
            row.operator("mesh.vertices_smooth", text="", icon_value=button_align_vertices.icon_id) 

            button_align_laplacian = icons.get("icon_align_laplacian")
            row.operator("mesh.vertices_smooth_laplacian", text="" , icon_value=button_align_laplacian.icon_id)  

            button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
            row.operator("mesh.shrinkwrap_smooth", text="", icon_value=button_align_shrinkwrap.icon_id)  



            box = col.box().column(1)
         
            row = box.column(1)
            
            button_align_vertices = icons.get("icon_align_vertices") 
            row.operator("mesh.vertices_smooth","Smooth Verts", icon_value=button_align_vertices.icon_id) 

            button_align_laplacian = icons.get("icon_align_laplacian")
            row.operator("mesh.vertices_smooth_laplacian","Smooth Laplacian", icon_value=button_align_laplacian.icon_id)  

            button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
            row.operator("mesh.shrinkwrap_smooth","Smooth Shrinkwrap ", icon_value=button_align_shrinkwrap.icon_id)  

           
            box.separator()    
                         
            row = box.row(1)                 
                         
            tp = context.window_manager.tp_props_looptools

            # relax - first line
            split = row.split(percentage=0.15, align=True)
            if tp.display_relax:
                button_align_looptools = icons.get("icon_align_looptools")
                split.prop(tp, "display_relax", text="", icon_value=button_align_looptools.icon_id)
                split.operator("mesh.tp_looptools_relax", text="  LoopTool Relax")

            else:
                button_align_looptools = icons.get("icon_align_looptools")
                split.prop(tp, "display_relax", text="", icon_value=button_align_looptools.icon_id)
                split.operator("mesh.tp_looptools_relax", text="  LoopTool Relax")

            # relax - settings
            if tp.display_relax:
                box = layout.box().column(1)    
                 
                row = box.column(1)  
                row.prop(tp, "relax_interpolation")
                row.prop(tp, "relax_input")
                row.prop(tp, "relax_iterations")
                row.prop(tp, "relax_regular")

            box.separator()         