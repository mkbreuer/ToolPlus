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


def ConvertToMesh(smooth, sub):
    pipe = bpy.context.object
    if pipe.type == 'CURVE':
        cross = pipe.data.bevel_object
        taper = pipe.data.taper_object
        sce = bpy.context.scene

        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.beautify_fill()
        bpy.ops.mesh.tris_convert_to_quads()

        if smooth:
            bpy.ops.mesh.normals_make_consistent()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.edges_select_sharp()
            bpy.ops.mesh.bevel(offset_type='OFFSET', offset=9999, segments=sub, vertex_only=False, clamp_overlap=True)
            bpy.ops.mesh.remove_doubles(threshold=0.0101)
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.shade_smooth()

        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.modifier_add(type='EDGE_SPLIT')
            bpy.context.object.modifiers["EdgeSplit"].split_angle = 1.22173

        bpy.ops.object.select_all(action='DESELECT')
        try:
            cross.select = True
        except:
            pass
        try:
            taper.select = True
        except:
            pass
        bpy.ops.object.delete()
        sce.objects.active = pipe
        bpy.context.object.select = True
        return {'FINISHED'}
    else:
        return {'CANCELLED'}


class Convert(bpy.types.Operator):
    """Converts pipe to mesh and beautifies the rim polygons"""
    bl_idname = "mesh.convert_pipe_to_mesh"
    bl_label = "Convert pipe to mesh"
    bl_options = {'REGISTER', 'UNDO'}

    smooth = bpy.props.BoolProperty(name="Smooth rim",
                                    description="Smooth the pipe rim",
                                    default=0)

    sub = bpy.props.IntProperty(name="Subdivisions",
                                description="Subdivisions on pipe rim",
                                min=1,
                                max=5,
                                default=2)

    def execute(self, context):
        rv = ConvertToMesh(self.smooth, self.sub)

        return rv
