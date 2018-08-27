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

def draw_pencil_ui(self, context, layout):
        tp = context.window_manager.tp_props_looptools 
        tp_scn = context.scene.tp_bsurfaces 
        tp_props = context.window_manager.tp_props_resurface            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     
        
        col = layout.column(align=True)

        box = col.box().column(1)  

        if not tp_props.display_pencil_edm:               
            row = box.row(1)                   
            row.prop(tp_props, "display_pencil_edm", text="", icon="TRIA_RIGHT", emboss = False)
            row.label(text="GPencil")
           
            row.operator("tp_ops.remove_gp", text="", icon="PANEL_CLOSE")               

            if context.mode == 'EDIT_MESH':

                button_draw_baply = icons.get("icon_baply")   
                row.operator("mesh.tp_looptools_gstretch", text="", icon_value=button_draw_baply.icon_id)
   
            button_draw_pencil = icons.get("icon_draw_pencil")
            row.operator("tp_ops.surface_pencil", text="",icon_value=button_draw_pencil.icon_id)     

       
        else:               
            row = box.row(1)                 
            row.prop(tp_props, "display_pencil_edm", text="", icon="TRIA_DOWN", emboss = False)
            row.label(text="GPencil")
           

            row.operator("tp_ops.remove_gp", text="", icon="PANEL_CLOSE") 

            if context.mode == 'EDIT_MESH': 
                
                button_draw_baply = icons.get("icon_baply")              
                row.operator("mesh.tp_looptools_gstretch", text="", icon_value=button_draw_baply.icon_id)           

            button_draw_pencil = icons.get("icon_draw_pencil")
            row.operator("tp_ops.surface_pencil", text="",icon_value=button_draw_pencil.icon_id)                      

            box.separator()

            row = box.row(1)
            row.operator("gpencil.draw", text="Hand",icon="GREASEPENCIL").mode = 'DRAW'               
            row.operator("gpencil.draw", text="Straight",icon="LINE_DATA").mode = 'DRAW_STRAIGHT'
            
            row = box.row(1)                
            row.operator("gpencil.draw", text="Polyline",icon="MESH_DATA").mode = 'DRAW_POLY'            
            row.operator("gpencil.draw", text="Eraser",icon="PANEL_CLOSE").mode = 'ERASER'

            box.separator()  

            row = box.row(1)
            row.operator("remove.gp", text="Delete GPencil Strokes", icon="PANEL_CLOSE")

            box.separator()           
            box.separator()           


            if context.mode == 'EDIT_MESH': 

                row = box.row(1)  
                if not tp_props.display_gstretch_edm:                                
                    row.prop(tp_props, "display_gstretch_edm", text="", icon="TRIA_DOWN_BAR")
                    row.operator("mesh.tp_looptools_gstretch", text="Looptools Gstretch (Bsurface)")
                else:                            
                    row.prop(tp_props, "display_gstretch_edm", text="", icon="TRIA_UP_BAR")
                    row.operator("mesh.tp_looptools_gstretch", text="Looptools Gstretch (Bsurface)")
      
                    box.separator()
                    
                    row = box.row(1)
                    row.prop(tp, "gstretch_delete_strokes")

                    box.separator()

                    row = box.row(1)
                    row.prop(tp, "gstretch_method")

                    box.separator()
                    
                    row = box.row(1)                    
                    col_conv = box.column(align=True)
                    col_conv.prop(tp, "gstretch_conversion", text="")
                    if tp.gstretch_conversion == 'distance':
                        col_conv.prop(tp, "gstretch_conversion_distance")
                    
                    elif tp.gstretch_conversion == 'limit_vertices':
                        row = col_conv.row(align=True)
                        row.prop(tp, "gstretch_conversion_min", text="Min")
                        row.prop(tp, "gstretch_conversion_max", text="Max")
                    
                    elif tp.gstretch_conversion == 'vertices':
                        col_conv.prop(tp, "gstretch_conversion_vertices")
                    
                    box.separator()

                    col_move = box.column(align=True)
                    row = col_move.row(align=True)
                    if tp.gstretch_lock_x:
                        row.prop(tp, "gstretch_lock_x", text="X", icon='LOCKED')
                    else:
                        row.prop(tp, "gstretch_lock_x", text="X", icon='UNLOCKED')
                    if tp.gstretch_lock_y:
                        row.prop(tp, "gstretch_lock_y", text="Y", icon='LOCKED')
                    else:
                        row.prop(tp, "gstretch_lock_y", text="Y", icon='UNLOCKED')
                    if tp.gstretch_lock_z:
                        row.prop(tp, "gstretch_lock_z", text="Z", icon='LOCKED')
                    else:
                        row.prop(tp, "gstretch_lock_z", text="Z", icon='UNLOCKED')
                    col_move.prop(tp, "gstretch_influence")

                    box.separator()
                    

        
            box.separator()
            box.separator()  
            
            row = box.row(1)                          
            if context.space_data.type == 'VIEW_3D':
                row.prop(context.tool_settings, "grease_pencil_source", expand=True)
                
                row = box.row(1)
                row.prop_enum(context.tool_settings, "gpencil_stroke_placement_view3d", 'SURFACE')
                row.prop_enum(context.tool_settings, "gpencil_stroke_placement_view3d", 'VIEW')
          
            box.separator()                     
                      