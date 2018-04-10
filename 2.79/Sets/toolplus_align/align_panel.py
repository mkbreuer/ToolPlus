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




# LOAD UI #
from toolplus_align.layouts.ui_pivot    import *
from toolplus_align.layouts.ui_object   import *
from toolplus_align.layouts.ui_edit     import *
from toolplus_align.layouts.ui_lattice  import *
from toolplus_align.layouts.ui_axis     import *
from toolplus_align.layouts.ui_history  import *



EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']

# DRAW UI LAYOUT #
class draw_align_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT


    def draw(self, context):
        layout = self.layout.column(1)
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = 1

        draw_pivot_layout(self, context, layout)
        
        if context.mode == 'OBJECT':

            draw_object_layout(self, context, layout)

        if context.mode == 'EDIT_MESH':

            draw_edit_layout(self, context, layout)

        if context.mode == 'EDIT_LATTICE':
            
            draw_lattice_layout(self, context, layout)                   

        if context.mode == 'EDIT_CURVE' or context.mode == 'EDIT_SURFACE':

            draw_axis_tools(context, layout)          

        if context.mode == 'EDIT_METABALL':    
            
            draw_axis_tools(context, layout)  


        if context.mode == 'EDIT_ARMATURE':     
            
            draw_axis_tools(context, layout)             

        draw_history_tools(context, layout)             




class VIEW3D_TP_Align_TOOLS(bpy.types.Panel, draw_align_panel_layout):
    bl_category = "Align"
    bl_idname = "VIEW3D_TP_Align_TOOLS"
    bl_label = "Align"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Align_UI(bpy.types.Panel, draw_align_panel_layout):
    bl_idname = "VIEW3D_TP_Align_UI"
    bl_label = "Align"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Align_PROPS(bpy.types.Panel, draw_align_panel_layout):
    bl_idname = "VIEW3D_TP_Align_PROPS"
    bl_label = "Align"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
