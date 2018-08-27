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

import addon_utils


def draw_spacing_ui(self, context, layout):
        tp = context.window_manager.tp_props_looptools            
        tp_props = context.window_manager.tp_props_resurface        
       
        icons = load_icons()

        col = layout.column(align=True)
                
        if not tp_props.display_spacing: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_spacing", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Spacing")

            button_align_space = icons.get("icon_align_space") 
            row.operator("mesh.tp_looptools_space", text="", icon_value=button_align_space.icon_id)                                      
            
            button_align_distribute = icons.get("icon_align_distribute")  
            row.operator("mesh.vertex_distribute",text="", icon_value=button_align_distribute.icon_id)   

            button_align_straigten = icons.get("icon_align_straigten") 
            row.operator("mesh.vertex_align",text="", icon_value=button_align_straigten.icon_id) 


        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_spacing", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Spacing")  

            button_align_space = icons.get("icon_align_space") 
            row.operator("mesh.tp_looptools_space", text="", icon_value=button_align_space.icon_id)                                      
            
            button_align_distribute = icons.get("icon_align_distribute")  
            row.operator("mesh.vertex_distribute",text="", icon_value=button_align_distribute.icon_id)  

            button_align_straigten = icons.get("icon_align_straigten") 
            row.operator("mesh.vertex_align",text="", icon_value=button_align_straigten.icon_id)  



            box = col.box().column(1)
         
            row = box.column(1)
            row.operator("mesh.hd_viewport_vertex_align")
          
            box.separator() 
      
            row = box.column(1)          
            button_align_straigten = icons.get("icon_align_straigten") 
            row.operator("mesh.vertex_align",text="Straighten", icon_value=button_align_straigten.icon_id) 

            button_align_distribute = icons.get("icon_align_distribute")  
            row.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_align_distribute.icon_id)    

            imdjs_tools_addon = "IMDJS_mesh_tools" 
            state = addon_utils.check(imdjs_tools_addon)
            if not state[0]:
                pass
            else:  
                button_align_radians = icons.get("icon_align_radians")  
                row.operator("mesh.round_selected_points", text="Radians")

            box.separator() 
            
            row = box.row(1)  
            # space - first line
            split = row.split(percentage=0.15, align=True)

            button_align_space = icons.get("icon_align_space") 
            if tp.display_space:
                split.prop(tp, "display_space", text="", icon_value=button_align_space.icon_id)
            else:
                split.prop(tp, "display_space", text="", icon_value=button_align_space.icon_id)
            
            split.operator("mesh.tp_looptools_space", text="LoopTools Space", icon='BLANK1')

            # space - settings
            if tp.display_space:
                box = col.box().column(1)             
                
                row = box.column(1) 
                row.prop(tp, "space_interpolation")
                row.prop(tp, "space_input")

                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if tp.space_lock_x:
                    row.prop(tp, "space_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(tp, "space_lock_x", text = "X", icon='UNLOCKED')
                if tp.space_lock_y:
                    row.prop(tp, "space_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(tp, "space_lock_y", text = "Y", icon='UNLOCKED')
                if tp.space_lock_z:
                    row.prop(tp, "space_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(tp, "space_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(tp, "space_influence")

                box.separator() 
                box = layout.box().column(1)   


            row = box.row(1)  
            # curve - first line
            split = row.split(percentage=0.15, align=True)

            button_align_curve = icons.get("icon_align_curve") 
            if tp.display_curve:
                split.prop(tp, "display_curve", text="", icon_value=button_align_curve.icon_id)
            else:
                split.prop(tp, "display_curve", text="", icon_value=button_align_curve.icon_id)

            split.operator("mesh.tp_looptools_curve", text="LoopTools Curve", icon='BLANK1')

            # curve - settings
            if tp.display_curve:
                box = col.box().column(1)              
                
                row = box.column(1) 
                row.prop(tp, "curve_interpolation")
                row.prop(tp, "curve_restriction")
                row.prop(tp, "curve_boundaries")
                row.prop(tp, "curve_regular")
                
                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if tp.curve_lock_x:
                    row.prop(tp, "curve_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(tp, "curve_lock_x", text = "X", icon='UNLOCKED')
                if tp.curve_lock_y:
                    row.prop(tp, "curve_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(tp, "curve_lock_y", text = "Y", icon='UNLOCKED')
                if tp.curve_lock_z:
                    row.prop(tp, "curve_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(tp, "curve_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(tp, "curve_influence")

                box.separator() 
                box = layout.box().column(1)    


            row = box.row(1)  
            # circle - first line
            split = row.split(percentage=0.15, align=True)

            button_align_circle = icons.get("icon_align_circle") 
            if tp.display_circle:
                split.prop(tp, "display_circle", text="", icon_value=button_align_circle.icon_id)
            else:
                split.prop(tp, "display_circle", text="", icon_value=button_align_circle.icon_id)

            split.operator("mesh.tp_looptools_circle", text="LoopTools Circle", icon='BLANK1')

            # circle - settings
            if tp.display_circle:
                box = col.box().column(1)              
                
                row = box.column(1) 
                row.prop(tp, "circle_fit")
                
                row.separator()

                row.prop(tp, "circle_flatten")
                
                row = box.row(align=True)
                row.prop(tp, "circle_custom_radius")
                
                row_right = row.row(align=True)
                row_right.active = tp.circle_custom_radius
                row_right.prop(tp, "circle_radius", text="")                
                box.prop(tp, "circle_regular")
                
                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if tp.circle_lock_x:
                    row.prop(tp, "circle_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(tp, "circle_lock_x", text = "X", icon='UNLOCKED')
                if tp.circle_lock_y:
                    row.prop(tp, "circle_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(tp, "circle_lock_y", text = "Y", icon='UNLOCKED')
                if tp.circle_lock_z:
                    row.prop(tp, "circle_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(tp, "circle_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(tp, "circle_influence")

                box.separator() 
                box = layout.box().column(1)    
                

            row = box.row(1) 
            # flatten - first line
            split = row.split(percentage=0.15, align=True)

            button_align_flatten = icons.get("icon_align_flatten") 
            if tp.display_flatten:
                split.prop(tp, "display_flatten", text="", icon_value=button_align_flatten.icon_id)
            else:
                split.prop(tp, "display_flatten", text="", icon_value=button_align_flatten.icon_id)

            split.operator("mesh.tp_looptools_flatten", text="LoopTool Flatten", icon ="BLANK1")

            # flatten - settings
            if tp.display_flatten:
                box = col.box().column(1)    
                 
                row = box.column(1)  
                row.prop(tp, "flatten_plane")

                box.separator()

                col_move = box.column(align=True)
                row = col_move.row(align=True)
                if tp.flatten_lock_x:
                    row.prop(tp, "flatten_lock_x", text = "X", icon='LOCKED')
                else:
                    row.prop(tp, "flatten_lock_x", text = "X", icon='UNLOCKED')
                if tp.flatten_lock_y:
                    row.prop(tp, "flatten_lock_y", text = "Y", icon='LOCKED')
                else:
                    row.prop(tp, "flatten_lock_y", text = "Y", icon='UNLOCKED')
                if tp.flatten_lock_z:
                    row.prop(tp, "flatten_lock_z", text = "Z", icon='LOCKED')
                else:
                    row.prop(tp, "flatten_lock_z", text = "Z", icon='UNLOCKED')
                col_move.prop(tp, "flatten_influence")

                box.separator() 

            box.separator() 
            
            row = box.row(1) 
            button_align_planar = icons.get("icon_align_planar") 
            row.operator("mesh.face_make_planar", "Make Planar Faces", icon_value=button_align_planar.icon_id)   

            box.separator()                 


                             