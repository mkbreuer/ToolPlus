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

# <pep8-80 compliant>

import bgl
import blf
import bpy
import gpu
from gpu_extras.batch import batch_for_shader
from math import pi, sqrt
from mathutils import Matrix, Vector
from random import random

class View3DGraphic():
    def __init__(self):
        self.is_enabled = True
        
    def draw_text(self, x, y, text, size, color = (0, 0, 0, 1)):
        if not self.is_enabled:
            return

        # Draw the specified text.
        font_id = 0
        blf.color(font_id, *color)
        blf.position(font_id, x, y, 0)
        blf.size(font_id, size, 72)
        blf.draw(font_id, text)
        
        self.restore_opengl()

    def draw_brush(self, brush, outline_color = (0, 0, 0, 1),
                   outline_thickness = 1, interior_color = (0, 0, 0, 0.2)):
        if not self.is_enabled:
            return

        # Treat the brush as a sphere centered at the origin with a pole in the
        # direction of it's normal.  Given this scenario, find a point on the
        # sphere's equator.
        brush_radius = brush.radius
        brush_normal = brush.normal
        if brush.normal.xy != Vector((0, 0)):
            point_on_equator = brush_radius * (
                Vector((brush_normal.y, -brush_normal.x, 0)).normalized()
            )
        else:
            point_on_equator = brush_radius * (
                Vector((brush_normal.z, -brush_normal.y, 0)).normalized()
            )

        # Generate a list of radially symmetrical vertices around the pole.
        segments = 48
        rotation_matrix = Matrix.Rotation(2 * pi / segments, 3, brush_normal)
        vertices = [point_on_equator]
        for side in range(segments - 1):
            vertices.append(rotation_matrix @ vertices[-1])

        # Translate the vertices from the world origin to the brush's center.
        brush_center = brush.center
        brush_center_x = brush_center.x
        brush_center_y = brush_center.y
        brush_center_z = brush_center.z
        for vertex in vertices:
            vertex.x += brush_center_x
            vertex.y += brush_center_y
            vertex.z += brush_center_z

        shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
        shader.bind()
        bgl.glDepthRange(0, 0.1)

        # Draw the brush's outline.
        if outline_color[3] > 0:
            bgl.glLineWidth(outline_thickness)
            shader.uniform_float("color", outline_color)
            batch = batch_for_shader(shader, 'LINES', {"pos": vertices})
            batch.draw(shader)

        # Draw the brush's interior.
        if interior_color[3] > 0:
            shader.uniform_float("color", interior_color)
            batch = batch_for_shader(shader, 'LINES', {"pos": vertices})
            batch.draw(shader)

        self.restore_opengl()

    def draw_brush_influence(self, brush, coordinate_map):
        if not self.is_enabled:
            return
        
        shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
        shader.bind()
        
        bgl.glPointSize(bpy.context.preferences.themes['Default'].view_3d.vertex_size * 2)

        # Draw each vertex using its corresponding color map value.
        brush_indices = brush.indices
        brush_color_map = brush.color_map

        for index in brush_indices:
            vert = [coordinate_map[index]]
            r, g, b = brush_color_map[index]
            shader.uniform_float("color", (r, g, b, 1.0))
            batch = batch_for_shader(shader, 'POINTS', {"pos": vert}) 
            batch.draw(shader)
        
        self.restore_opengl()

    def draw_region_circle(self, region_x, region_y, radius,
                           outline_color = (0, 0, 0, 1),
                           outline_thickness = 1,
                           interior_color = (0, 0, 0, 0.2)):
        if not self.is_enabled:
            return

        # Generate a list of radially symmetrical vertices around the origin.
        segments = int(5 * sqrt(radius) + 3)
        rotation_matrix = Matrix.Rotation(2 * pi / segments, 2)
        vertices = [Vector((radius, 0))]
        for side in range(segments - 1):
            vertices.append(rotation_matrix @ vertices[-1])

        # Translate the vertices from the origin to the circle's center.
        for vertex in vertices:
            vertex.x += region_x
            vertex.y += region_y

        shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
        shader.bind()
        # Draw the circle's outline.
        if outline_color[3] > 0:
            bgl.glLineWidth(outline_thickness)
            shader.uniform_float("color", outline_color)
            batch = batch_for_shader(shader, 'LINE_LOOP', {"pos": vertices})
            batch.draw(shader)

        # Draw the circle's interior.
        if interior_color[3] > 0:
            shader.uniform_float("color", interior_color)
            batch = batch_for_shader(shader, 'LINE_LOOP', {"pos": vertices})
            batch.draw(shader)

        self.restore_opengl()

    def draw_octree(self, octree, nodes = {'ROOT'},
                    space = 'WORLD', mesh_object = None):
        if not self.is_enabled:
            return

        # The octree data can only be drawn in object or world coordinate
        # systems.
        if space not in {'OBJECT', 'WORLD'}:
            raise Exception((
                    "Invalid space argument '{0}' not found in " +
                    "('OBJECT', 'WORLD')"
                ).format(space)
            )

        # Object space coordinates require a specified mesh object to determine
        # the transformation matrix from object space to world space.
        if space == 'OBJECT' and mesh_object == None:
            raise Exception(
                "Object space coordinates need to be accompanied by a mesh " +
                "object argument"
            )

        # Draw the root node, if specified.
        if 'ROOT' in nodes:
            self.draw_octree_node(octree.root, space, mesh_object)

        # Draw interior nodes, if specified.
        if 'INTERIOR' in nodes:
            self.draw_octree_interior(octree.root, space, mesh_object)

        # Draw leaf nodes, if specified.
        if 'LEAF' in nodes:
            self.draw_octree_leaves(octree.root, space, mesh_object)

    def draw_octree_leaves(self, node, space, mesh_object):
        if not self.is_enabled:
            return

        # Recursively draw all leaf nodes that branch from the specified node.
        child_map = node.child_map
        if child_map:
            for key in child_map:
                self.draw_octree_leaves(child_map[key], space, mesh_object)
        else:
            self.draw_octree_node(node, space, mesh_object)

    def draw_octree_interior(self, node, space, mesh_object):
        if not self.is_enabled:
            return

        # Recursively draw all interior nodes that branch from the specified
        # node.
        child_map = node.child_map
        if child_map:
            for key in child_map:
                self.draw_octree_node(node, space, mesh_object)
                self.draw_octree_interior(child_map[key], space, mesh_object)

    def draw_octree_node(self, node, space, mesh_object):
        if not self.is_enabled:
            return

        # Determine the eight corners of the octree node.
        center = node.center
        half_size = node.half_size
        offset_map = node.offset_map
        corners = [
            center + half_size * offset_map[key]
            for key in (
                '+++', '+-+', '--+', '-++', '++-', '+--', '---', '-+-'
            )
        ]

        # Transform each object space coordinates into world space.
        if space == 'OBJECT':
            matrix_world = mesh_object.matrix_world
            for co in corners:
                co.xyz = matrix_world @ co

        shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
        shader.uniform_float("color", (0, 1, 0.67, 1.0))

        # Draw opposite squares of the cube.
        shader.bind()
        vertices = []
        for x, y, z in corners[:4]:
            vertices.append(Vector(x, y, z))
        batch = batch_for_shader(shader, 'LINE_LOOP', {"pos": vertices})
        batch.draw(shader)
            
        shader.bind()
        vertices = []
        for x, y, z in corners[4:]:
            vertices.append(Vector(x, y, z))
        batch = batch_for_shader(shader, 'LINE_LOOP', {"pos": vertices})
        batch.draw(shader)

        # Draw lines between opposite squares to form a cube.
        shader.bind()
        vertices = []
        for i in [0, 4, 1, 5, 2, 6, 3, 7]:
            x, y, z = corners[i]
            vertices.append(Vector(x, y, z))
        batch = batch_for_shader(shader, 'LINES', {"pos": vertices})
        batch.draw(shader)

        self.restore_opengl()

    def restore_opengl(self):
        # Restore OpenGL to its default state.
        bgl.glDepthRange(0, 1)
        bgl.glLineWidth(1)
        bgl.glPolygonOffset(0, 0)
