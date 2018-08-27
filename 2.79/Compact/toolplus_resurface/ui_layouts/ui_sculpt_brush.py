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


# MASK DEFAULT TOOLS #
def draw_sculpt_brush_ui(self, context, layout):     
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)
 
        box = col.box().column(1) 

        box.separator() 
      
        row = box.row(1) 
        sub = row.row(1)
        sub.alignment = 'CENTER'    
        sub.scale_x = 2  
        sub.scale_y = 1.7 

        sub.operator("paint.brush_select", text='', icon='BRUSH_BLOB').sculpt_tool= 'BLOB'    
        sub.operator("paint.brush_select", text='', icon='BRUSH_CLAY').sculpt_tool='CLAY'        
        sub.operator("paint.brush_select", text='', icon='BRUSH_CLAY_STRIPS').sculpt_tool= 'CLAY_STRIPS'   
        sub.operator("paint.brush_select", text='', icon='BRUSH_CREASE').sculpt_tool='CREASE'
        sub.operator("paint.brush_select", text='', icon='BRUSH_SCULPT_DRAW').sculpt_tool='DRAW'
        sub.operator("paint.brush_select", text='', icon='BRUSH_LAYER').sculpt_tool= 'LAYER'
        sub.operator("paint.brush_select", text='', icon='BRUSH_INFLATE').sculpt_tool='INFLATE'

        box.separator() 

        row = box.row(1) 
        sub = row.row(1)
        sub.alignment = 'CENTER'    
        sub.scale_x = 2  
        sub.scale_y = 1.7 
        sub.operator("paint.brush_select", text='', icon='BRUSH_MASK').sculpt_tool='MASK'
        sub.operator("paint.brush_select", text='', icon='BRUSH_PINCH').sculpt_tool= 'PINCH'
        sub.operator("paint.brush_select", text='', icon='BRUSH_FILL').sculpt_tool='FILL'
        sub.operator("paint.brush_select", text='', icon='BRUSH_FLATTEN').sculpt_tool='FLATTEN'
        sub.operator("paint.brush_select", text='', icon='BRUSH_SMOOTH').sculpt_tool= 'SMOOTH'
        sub.operator("paint.brush_select", text='', icon='BRUSH_SCRAPE').sculpt_tool= 'SCRAPE'

        box.separator() 
        row = box.row(1) 
        sub = row.row(1)
        sub.alignment = 'CENTER'    
        sub.scale_x = 2  
        sub.scale_y = 1.7 
        
        sub.operator("paint.brush_select", text='', icon='BRUSH_GRAB').sculpt_tool='GRAB'
        sub.operator("paint.brush_select", text='', icon='BRUSH_ROTATE').sculpt_tool= 'ROTATE'
        sub.operator("paint.brush_select", text='', icon='BRUSH_THUMB').sculpt_tool= 'THUMB'
        sub.operator("paint.brush_select", text='', icon='BRUSH_SNAKE_HOOK').sculpt_tool= 'SNAKE_HOOK'
        sub.operator("paint.brush_select", text='', icon='BRUSH_NUDGE').sculpt_tool= 'NUDGE'

        box.separator()              
        box.separator()    
        
        row = box.row(1)
        row.label(text="Mirror")
        row.prop(context.tool_settings.sculpt, "use_symmetry_x", text="X", toggle=True)
        row.prop(context.tool_settings.sculpt, "use_symmetry_y", text="Y", toggle=True)
        row.prop(context.tool_settings.sculpt, "use_symmetry_z", text="Z", toggle=True)

        box.separator() 
        box.separator() 

        row = box.row(1)            
        button_draw_surface = icons.get("icon_draw_surface")  
        row.operator("tp_ops.add_dyntopo_details", text="DynMesh", icon ="VPAINT_HLT")        
        row.prop(context.scene, "expand_mask", text="")  

        box.separator() 