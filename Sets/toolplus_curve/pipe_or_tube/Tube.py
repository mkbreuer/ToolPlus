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


import bpy
from bpy.types import Operator, Panel


def Add_Tube(outer_radius, inner_radius, height, res, makemesh):

    # Inserts Circle primitive
    bpy.ops.curve.primitive_bezier_circle_add(radius=outer_radius)

    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.duplicate_move(CURVE_OT_duplicate={}, TRANSFORM_OT_translate={"value": (0, 0, 0), "constraint_axis": (False, False, False), "constraint_orientation": 'GLOBAL', "mirror": False, "proportional": 'DISABLED', "proportional_edit_falloff": 'SMOOTH', "proportional_size": 1, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "gpencil_strokes": False, "texture_space": False, "remove_on_cancel": False, "release_confirm": False})
    scale = inner_radius / outer_radius
    bpy.ops.transform.resize(value=(scale, scale, scale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()
    bpy.context.object.name = "Tube"

    # Extrude
    bpy.context.object.data.dimensions = '2D'
    bpy.context.object.data.extrude = height
    bpy.context.object.data.resolution_u = res

    if makemesh == 1:
        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.beautify_fill()
        bpy.ops.mesh.tris_convert_to_quads()
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.edges_select_sharp()
        bpy.ops.mesh.mark_sharp()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='EDGE_SPLIT')
        bpy.context.object.modifiers["EdgeSplit"].split_angle = 1.22173
        bpy.context.object.modifiers["EdgeSplit"].use_edge_angle = False


class AddTube(bpy.types.Operator):
    """Create a simple straight Tube, either as mesh or extruded curve"""
    bl_idname = "mesh.primitive_tube_add"
    bl_label = "Add Tube"
    bl_options = {'REGISTER', 'UNDO'}

    outer_radius = bpy.props.FloatProperty(name="Radius 1",
                                           description="Tube 1st radius",
                                           min=0.01,
                                           max=9999.0,
                                           default=1.0)
    inner_radius = bpy.props.FloatProperty(name="Radius 2",
                                           description="Tube 2nd radius",
                                           min=0.01,
                                           max=9999.0,
                                           default=0.5)
    height = bpy.props.FloatProperty(name="Height",
                                     description="Height of the tube",
                                     min=0.01,
                                     max=9999.0,
                                     default=2.0)
    res = bpy.props.IntProperty(name="Mesh resolution",
                                description="Controls mesh smoothness",
                                min=1,
                                max=20,
                                default=6)
    makemesh = bpy.props.BoolProperty(name="Create as Mesh",
                                      description="If disabled, the tube will be an extruded curve",
                                      default=1)

    def execute(self, context):
        Add_Tube(self.outer_radius, self.inner_radius, self.height, self.res, self.makemesh)

        return {'FINISHED'}
