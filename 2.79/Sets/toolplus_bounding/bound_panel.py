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
from .icons.icons import load_icons

# LOAD UI #  
from toolplus_bounding.bound_history    import draw_history_layout
from toolplus_bounding.bound_main       import draw_panel_layout



def draw_bounding_panel_layout(context, layout):

    layout.operator_context = 'INVOKE_REGION_WIN'
                                                  
    draw_panel_layout(context, layout)   

    panel_prefs = context.user_preferences.addons[__package__].preferences
    if panel_prefs.tab_display_history == True:
        
        draw_history_layout(context, layout)     



EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']

class VIEW3D_TP_BBOX_MESHES_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_BBOX_MESHES_TOOLS"
    bl_label = "Bounding"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}
    
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
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_bounding_panel_layout(context, layout) 



class VIEW3D_TP_BBOX_MESHES_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_BBOX_MESHES_UI"
    bl_label = "Bounding"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

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
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_bounding_panel_layout(context, layout) 



