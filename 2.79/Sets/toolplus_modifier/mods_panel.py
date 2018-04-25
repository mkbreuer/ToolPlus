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

# LOAD UI: PANEL #
from .mods_title import draw_mods_title_layout
from .mods_pivot import draw_mods_pivot_layout
from .mods_object_edit import draw_mods_object_edit_layout
from .mods_icons import draw_mods_icons_layout
from .mods_lattice import draw_mods_lattice_layout
from .mods_sculpt import draw_mods_sculpt_layout
from .mods_history import draw_mods_history_layout

EDIT = ["OBJECT", "SCULPT", "EDIT_MESH", "EDIT_LATTICE", "EDIT_CURVE", "EDIT_SURFACE"]#, "EDIT_METABALL", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'LATTICE']#, 'FONT', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']

class draw_modifier_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)

#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:
#                return isModelingMode and context.mode in EDIT

        return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column(align=True)    

        icons = load_icons()
       
        layout.scale_y = 1        
       
        display_icon_type = context.user_preferences.addons[__package__].preferences.tab_location_icons        
        if display_icon_type == 'icons':
            
            draw_mods_icons_layout(self, context, layout)
            
        else:

            display_title = context.user_preferences.addons[__package__].preferences.tab_title
            if display_title == True:

                draw_mods_title_layout(self, context, layout)



            if context.mode == 'SCULPT':
                draw_mods_sculpt_layout(self, context, layout)
           
           
            elif context.mode == 'EDIT_LATTICE':                
                
                Display_Pivot = context.user_preferences.addons[__package__].preferences.tab_pivot
                if Display_Pivot == True:
          
                    draw_mods_pivot_layout(self, context, layout)
                                    
                draw_mods_lattice_layout(self, context, layout)

            else:
               
                Display_Pivot = context.user_preferences.addons[__package__].preferences.tab_pivot
                if Display_Pivot == True:
          
                    draw_mods_pivot_layout(self, context, layout)               
               
                draw_mods_object_edit_layout(self, context, layout)


        Display_History = context.user_preferences.addons[__package__].preferences.tab_history 
        if Display_History == True:
            
            draw_mods_history_layout(self, context, layout)





class VIEW3D_TP_Modifier_Panel_TOOLS(bpy.types.Panel, draw_modifier_panel_layout):
    bl_category = "Origin"
    bl_idname = "VIEW3D_TP_Modifier_Panel_TOOLS"
    bl_label = "Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Modifier_Panel_UI(bpy.types.Panel, draw_modifier_panel_layout):
    bl_idname = "VIEW3D_TP_Modifier_Panel_UI"
    bl_label = "Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
