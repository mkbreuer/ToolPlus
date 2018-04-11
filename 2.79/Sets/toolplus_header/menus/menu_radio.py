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


def draw_non_button_header_menu(self, context):
    layout = self.layout
    
    layout.operator_context = 'INVOKE_REGION_WIN'
    
    view = context.space_data
    scene = context.scene        
    gs = scene.game_settings
    mode_string = context.mode
    edit_object = context.edit_object
    obj = context.active_object
    
    toolsettings = context.tool_settings

    row = layout.row(align=True)
    
    if not scene.render.use_shading_nodes:
        row.prop(gs, "material_mode", text="")

    if view.viewport_shade == 'SOLID':
        row.prop(view, "show_textured_solid", text="Texture")
        row.prop(view, "show_only_render", text="Render")
        row.prop(view, "show_floor", text="Grid")
        row.prop(view, "use_matcap")
      
        if view.use_matcap:
            row.template_icon_view(view, "matcap_icon")

    elif view.viewport_shade == 'TEXTURED':
        if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
            row.prop(view, "show_textured_shadeless")        

    
    row.prop(view, "show_backface_culling", text="Backface")
    if obj and obj.mode == 'EDIT' and view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
        row.prop(view, "show_occlude_wire", text="Hidden")


    row = layout.row(align=True)
    row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")

    if view.region_quadviews:
        region = view.region_quadviews[2]
        col = layout.column()
        col.prop(region, "lock_rotation")
        row = layout.row(align=True)
        row.enabled = region.lock_rotation
        row.prop(region, "show_sync_view")
        row = layout.row(align=True)
        row.enabled = region.lock_rotation and region.show_sync_view
        row.prop(region, "use_box_clip")

