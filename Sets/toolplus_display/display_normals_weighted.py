bl_info = {
    "name": "Weighted Normals Calculation",
    "description": "Simple operator to calculate weighted normals on the mesh.",
    "author": "Simon Lusenc (50keda)",
    "version": (1, 1),
    "blender": (2, 74, 0),
    "location": "3D View > Quick Search",
    "category": "Object",
    "support": "COMMUNITY"
}

import bpy, bmesh, array
from mathutils import Vector


class WeightNormalsCalculator(bpy.types.Operator):
    """Calculate weighted normals for active object."""
    bl_idname = "tp_ops.calculate_weighted_normals"
    bl_label = "Weight Normals"

    cache = {}
    """Cache for calculated weighted normals. It stores normals by key: 'vert_index:edge_index'."""

    @staticmethod
    def calc_weighted_normal(bm, vert_index, edge_index):
        """Calculates weighted normal for given combination of vertex and edge index.
        WARNING: There is no safety chec if thoose two belongs together.

        :param bm: bmesh object
        :type bm: bmesh
        :param vert_index: index of the vertex to calculate normal for
        :type vert_index: int
        :param edge_index: index of the edge to use for calculation (vertex has to belong to this edge)
        :returns: Vector
        """
        normal_hash = str(vert_index) + ":" + str(edge_index)

        if normal_hash in WeightNormalsCalculator.cache:
            return WeightNormalsCalculator.cache[normal_hash]

        edge = bm.edges[edge_index]
        vert = bm.verts[vert_index]

        selected_faces = []

        # edge.seam = True
        # edge.select_set(True)

        for f in edge.link_faces:

            if not f.select:

                f.select = True
                selected_faces.append(f)

        # select linked faces of already selected edges
        # until every smooth face around current loop is selected
        more_selected = 1
        while more_selected > 0:

            more_selected = 0
            for edge1 in vert.link_edges:

                if edge1.smooth and edge1.select:

                    for f in edge1.link_faces:

                        if not f.select:

                            f.select = True
                            selected_faces.append(f)

                            more_selected += 1

        # calc areas
        max_area = 0
        areas = {}
        for i, f in enumerate(selected_faces):
            area = f.calc_area()
            areas[i] = area

            if area > max_area:
                max_area = area

        # calc normal
        normal = Vector()
        for i, f in enumerate(selected_faces):
            perc = areas[i] / max_area
            f.normal_update()
            normal += perc * f.normal

            # also unselect all the faces
            f.select = False

        WeightNormalsCalculator.cache[normal_hash] = normal.normalized()

        return normal.normalized()

    @classmethod
    def poll(cls, context):
        return context.object and context.object.mode == "OBJECT" and context.object.type == "MESH"

    def execute(self, context):

        WeightNormalsCalculator.cache = {}

        mesh = context.object.data

        bm = bmesh.new()
        bm.from_mesh(mesh)
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()

        # unselect everything first
        for v in bm.faces:
            v.select = False

        for v in bm.edges:
            v.select = False

        for v in bm.verts:
            v.select = False

        nor_list = [(0,)] * len(mesh.loops)
        for f in bm.faces:

            # map both edge indices into vertex (loop has info only about one edge)
            verts_edge_map = {}
            for e in f.edges:
                for v in e.verts:

                    v_i = v.index

                    if v_i not in verts_edge_map:
                        verts_edge_map[v_i] = {e.index: 1}
                    else:
                        verts_edge_map[v_i][e.index] = 1

            for curr_loop in f.loops:

                edge_keys = verts_edge_map[curr_loop.vert.index].keys()

                # if current loop vertex has at leas one sharp edge around calculate weighted normal
                for e_i in edge_keys:

                    if not mesh.edges[e_i].use_edge_sharp:

                        curr_n = WeightNormalsCalculator.calc_weighted_normal(bm, curr_loop.vert.index, e_i)
                        nor_list[curr_loop.index] = curr_n

                        break

                else:

                    nor_list[curr_loop.index] = mesh.loops[curr_loop.index].normal

        bm.free()

        mesh.use_auto_smooth = True
        bpy.ops.mesh.customdata_custom_splitnormals_clear()

        bpy.ops.mesh.customdata_custom_splitnormals_add()
        mesh.normals_split_custom_set(nor_list)
        mesh.free_normals_split()

        return {'FINISHED'}


def register():
    bpy.utils.register_class(WeightNormalsCalculator)


def unregister():
    bpy.utils.unregister_class(WeightNormalsCalculator)


if __name__ == '__main__':
    register()
