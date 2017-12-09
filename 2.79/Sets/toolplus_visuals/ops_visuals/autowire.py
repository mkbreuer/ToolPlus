# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****


# space_view_3d_display_tools.py Copyright (C) 2014, Jordi Vall-llovera
# Multiple display tools for fast navigate/interact with the viewport
# wire tools by Lapineige


# LOAD MODUL #
import bpy
from bpy.types import Operator
from bpy.props import (BoolProperty, EnumProperty)



class VIEW3D_TP_WT_SelectionHandlerToggle(Operator):
    bl_idname = "tp_ops.wt_selection_handler_toggle"
    bl_label = "Wire Selection (auto)"
    bl_description = "Display the wire of the selection, auto update when selecting another object"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        obj = bpy.context.object
        
        display_props = context.scene.display_props
        if display_props.WT_handler_enable:
            try:
                bpy.app.handlers.scene_update_post.remove(wire_on_selection_handler)
            except:
                self.report({'INFO'}, "Wire Selection: auto mode exit seems to have failed. If True, reload the file")

            display_props.WT_handler_enable = False
            if hasattr(obj, "show_wire"):
                obj.show_wire, obj.show_all_edges = False, False
        else:
            bpy.app.handlers.scene_update_post.append(wire_on_selection_handler)
            display_props.WT_handler_enable = True
           
            if hasattr(obj, "show_wire"):
                obj.show_wire, obj.show_all_edges = True, True

        return {'FINISHED'}


# HANDLER #
def wire_on_selection_handler(scene):
    obj = bpy.context.object

    if not scene.display_props.WT_handler_previous_object:
        if hasattr(obj, "show_wire"):
            obj.show_wire, obj.show_all_edges = True, True
            scene.display_props.WT_handler_previous_object = obj.name
    else:
        if scene.display_props.WT_handler_previous_object != obj.name:
            previous_obj = bpy.data.objects[scene.display_props.WT_handler_previous_object]
            if hasattr(previous_obj, "show_wire"):
                previous_obj.show_wire, previous_obj.show_all_edges = False, False

            scene.display_props.WT_handler_previous_object = obj.name

            if hasattr(obj, "show_wire"):
                obj.show_wire, obj.show_all_edges = True, True


# REGISTER #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

