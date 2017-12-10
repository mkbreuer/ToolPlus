# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    


class draw_layout_sharpen:

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode 

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        icons = load_icons()

        box = layout.box().column(1)    

        row = box.row(1).column_flow(2)
        row.label("Mark Sharp") 
        row.operator("mesh.mark_sharp", text="Edges", icon='SNAP_EDGE').use_verts = True  
        row.operator("mesh.mark_sharp", text="Vertices", icon='SNAP_VERTEX').use_verts = True          
        
        row.label("Clear Sharp")  
        row.operator("mesh.mark_sharp", text="", icon='X').clear = True
        props = row.operator("mesh.mark_sharp", text="", icon='X')
        props.use_verts = True
        props.clear = True

        box.separator()   
            


class VIEW3D_TP_Sharpen_Panel_TOOLS(bpy.types.Panel, draw_layout_sharpen):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Sharpen_Panel_TOOLS"
    bl_label = "Sharpen"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Sharpen_Panel_UI(bpy.types.Panel, draw_layout_sharpen):
    bl_idname = "VIEW3D_TP_Sharpen_Panel_UI"
    bl_label = "Sharpen"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}
                                       
