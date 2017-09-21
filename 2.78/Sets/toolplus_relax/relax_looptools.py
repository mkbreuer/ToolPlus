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

bl_info = {
    "name": "LoopTools Relax",
    "author": "Bart Crouch",
    "version": (4, 6, 5),
    "blender": (2, 72, 2),
    "location": "View3D > Toolbar and View3D > Specials (W-key)",
    "warning": "",
    "description": "Mesh modelling toolkit. Several tools to aid modelling",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Modeling/LoopTools",
    "category": "T+",
}

#    blender 2.73 needs to call ensure_lookup_table() for bm.verts[], bm.edges[], bm.faces[].
#    the lookup_table will get "dirty" after:
#    bm.new(), bm.from_mesh(), bm.from_edit_mesh()
#    bm.verts.new(), bm.edges.new(), bm.faces.new()
#    bm.verts.remove(), bm.edges.remove(), bm.faces.remove()
#    bm.normal_update(), bm.copy()
#
#    bm.verts.ensure_lookup_table() ### 2.73
#    bm.edges.ensure_lookup_table() ### 2.73
#    bm.faces.ensure_lookup_table() ### 2.73



import bmesh
import bpy
import collections
import mathutils
import math
from bpy_extras import view3d_utils


##########################################
####### General functions ################
##########################################


# used by all tools to improve speed on reruns
looptools_cache = {}



#need: force a full recalculation next time
def cache_delete(tool):
    if tool in looptools_cache:
        del looptools_cache[tool]


#need: check cache for stored information
def cache_read(tool, object, bm, input_method, boundaries):
    # current tool not cached yet
    if tool not in looptools_cache:
        return(False, False, False, False, False)
    # check if selected object didn't change
    if object.name != looptools_cache[tool]["object"]:
        return(False, False, False, False, False)
    # check if input didn't change
    if input_method != looptools_cache[tool]["input_method"]:
        return(False, False, False, False, False)
    if boundaries != looptools_cache[tool]["boundaries"]:
        return(False, False, False, False, False)
    modifiers = [mod.name for mod in object.modifiers if mod.show_viewport \
        and mod.type == 'MIRROR']
    if modifiers != looptools_cache[tool]["modifiers"]:
        return(False, False, False, False, False)
    input = [v.index for v in bm.verts if v.select and not v.hide]
    if input != looptools_cache[tool]["input"]:
        return(False, False, False, False, False)
    # reading values
    single_loops = looptools_cache[tool]["single_loops"]
    loops = looptools_cache[tool]["loops"]
    derived = looptools_cache[tool]["derived"]
    mapping = looptools_cache[tool]["mapping"]

    return(True, single_loops, loops, derived, mapping)


#need: store information in the cache
def cache_write(tool, object, bm, input_method, boundaries, single_loops,
loops, derived, mapping):
    # clear cache of current tool
    if tool in looptools_cache:
        del looptools_cache[tool]
    # prepare values to be saved to cache
    input = [v.index for v in bm.verts if v.select and not v.hide]
    modifiers = [mod.name for mod in object.modifiers if mod.show_viewport \
        and mod.type == 'MIRROR']
    # update cache
    looptools_cache[tool] = {"input": input, "object": object.name,
        "input_method": input_method, "boundaries": boundaries,
        "single_loops": single_loops, "loops": loops,
        "derived": derived, "mapping": mapping, "modifiers": modifiers}


#need: calculates natural cubic splines through all given knots
def calculate_cubic_splines(bm_mod, tknots, knots):
    # hack for circular loops
    if knots[0] == knots[-1] and len(knots) > 1:
        circular = True
        k_new1 = []
        for k in range(-1, -5, -1):
            if k - 1 < -len(knots):
                k += len(knots)
            k_new1.append(knots[k-1])
        k_new2 = []
        for k in range(4):
            if k + 1 > len(knots) - 1:
                k -= len(knots)
            k_new2.append(knots[k+1])
        for k in k_new1:
            knots.insert(0, k)
        for k in k_new2:
            knots.append(k)
        t_new1 = []
        total1 = 0
        for t in range(-1, -5, -1):
            if t - 1 < -len(tknots):
                t += len(tknots)
            total1 += tknots[t] - tknots[t-1]
            t_new1.append(tknots[0] - total1)
        t_new2 = []
        total2 = 0
        for t in range(4):
            if t + 1 > len(tknots) - 1:
                t -= len(tknots)
            total2 += tknots[t+1] - tknots[t]
            t_new2.append(tknots[-1] + total2)
        for t in t_new1:
            tknots.insert(0, t)
        for t in t_new2:
            tknots.append(t)
    else:
        circular = False
    # end of hack

    n = len(knots)
    if n < 2:
        return False
    x = tknots[:]
    locs = [bm_mod.verts[k].co[:] for k in knots]
    result = []
    for j in range(3):
        a = []
        for i in locs:
            a.append(i[j])
        h = []
        for i in range(n-1):
            if x[i+1] - x[i] == 0:
                h.append(1e-8)
            else:
                h.append(x[i+1] - x[i])
        q = [False]
        for i in range(1, n-1):
            q.append(3/h[i]*(a[i+1]-a[i]) - 3/h[i-1]*(a[i]-a[i-1]))
        l = [1.0]
        u = [0.0]
        z = [0.0]
        for i in range(1, n-1):
            l.append(2*(x[i+1]-x[i-1]) - h[i-1]*u[i-1])
            if l[i] == 0:
                l[i] = 1e-8
            u.append(h[i] / l[i])
            z.append((q[i] - h[i-1] * z[i-1]) / l[i])
        l.append(1.0)
        z.append(0.0)
        b = [False for i in range(n-1)]
        c = [False for i in range(n)]
        d = [False for i in range(n-1)]
        c[n-1] = 0.0
        for i in range(n-2, -1, -1):
            c[i] = z[i] - u[i]*c[i+1]
            b[i] = (a[i+1]-a[i])/h[i] - h[i]*(c[i+1]+2*c[i])/3
            d[i] = (c[i+1]-c[i]) / (3*h[i])
        for i in range(n-1):
            result.append([a[i], b[i], c[i], d[i], x[i]])
    splines = []
    for i in range(len(knots)-1):
        splines.append([result[i], result[i+n-1], result[i+(n-1)*2]])
    if circular: # cleaning up after hack
        knots = knots[4:-4]
        tknots = tknots[4:-4]

    return(splines)


#need: calculates linear splines through all given knots
def calculate_linear_splines(bm_mod, tknots, knots):
    splines = []
    for i in range(len(knots)-1):
        a = bm_mod.verts[knots[i]].co
        b = bm_mod.verts[knots[i+1]].co
        d = b-a
        t = tknots[i]
        u = tknots[i+1]-t
        splines.append([a, d, t, u]) # [locStart, locDif, tStart, tDif]

    return(splines)


# calculate a best-fit plane to the given vertices
def calculate_plane(bm_mod, loop, method="best_fit", object=False):
    # getting the vertex locations
    locs = [bm_mod.verts[v].co.copy() for v in loop[0]]

    # calculating the center of masss
    com = mathutils.Vector()
    for loc in locs:
        com += loc
    com /= len(locs)
    x, y, z = com

    if method == 'best_fit':
        # creating the covariance matrix
        mat = mathutils.Matrix(((0.0, 0.0, 0.0),
                                (0.0, 0.0, 0.0),
                                (0.0, 0.0, 0.0),
                                ))
        for loc in locs:
            mat[0][0] += (loc[0]-x)**2
            mat[1][0] += (loc[0]-x)*(loc[1]-y)
            mat[2][0] += (loc[0]-x)*(loc[2]-z)
            mat[0][1] += (loc[1]-y)*(loc[0]-x)
            mat[1][1] += (loc[1]-y)**2
            mat[2][1] += (loc[1]-y)*(loc[2]-z)
            mat[0][2] += (loc[2]-z)*(loc[0]-x)
            mat[1][2] += (loc[2]-z)*(loc[1]-y)
            mat[2][2] += (loc[2]-z)**2

        # calculating the normal to the plane
        normal = False
        try:
            mat = matrix_invert(mat)
        except:
            ax = 2
            if math.fabs(sum(mat[0])) < math.fabs(sum(mat[1])):
                if math.fabs(sum(mat[0])) < math.fabs(sum(mat[2])):
                    ax = 0
            elif math.fabs(sum(mat[1])) < math.fabs(sum(mat[2])):
                ax = 1
            if ax == 0:
                normal = mathutils.Vector((1.0, 0.0, 0.0))
            elif ax == 1:
                normal = mathutils.Vector((0.0, 1.0, 0.0))
            else:
                normal = mathutils.Vector((0.0, 0.0, 1.0))
        if not normal:
            # warning! this is different from .normalize()
            itermax = 500
            iter = 0
            vec = mathutils.Vector((1.0, 1.0, 1.0))
            vec2 = (mat * vec)/(mat * vec).length
            while vec != vec2 and iter<itermax:
                iter+=1
                vec = vec2
                vec2 = mat * vec
                if vec2.length != 0:
                    vec2 /= vec2.length
            if vec2.length == 0:
                vec2 = mathutils.Vector((1.0, 1.0, 1.0))
            normal = vec2

    elif method == 'normal':
        # averaging the vertex normals
        v_normals = [bm_mod.verts[v].normal for v in loop[0]]
        normal = mathutils.Vector()
        for v_normal in v_normals:
            normal += v_normal
        normal /= len(v_normals)
        normal.normalize()

    elif method == 'view':
        # calculate view normal
        rotation = bpy.context.space_data.region_3d.view_matrix.to_3x3().\
            inverted()
        normal = rotation * mathutils.Vector((0.0, 0.0, 1.0))
        if object:
            normal = object.matrix_world.inverted().to_euler().to_matrix() * \
                     normal

    return(com, normal)


#need: calculate splines based on given interpolation method (controller function)
def calculate_splines(interpolation, bm_mod, tknots, knots):
    if interpolation == 'cubic':
        splines = calculate_cubic_splines(bm_mod, tknots, knots[:])
    else: # interpolations == 'linear'
        splines = calculate_linear_splines(bm_mod, tknots, knots[:])

    return(splines)


#need: check loops and only return valid ones
def check_loops(loops, mapping, bm_mod):
    valid_loops = []
    for loop, circular in loops:
        # loop needs to have at least 3 vertices
        if len(loop) < 3:
            continue
        # loop needs at least 1 vertex in the original, non-mirrored mesh
        if mapping:
            all_virtual = True
            for vert in loop:
                if mapping[vert] > -1:
                    all_virtual = False
                    break
            if all_virtual:
                continue
        # vertices can not all be at the same location
        stacked = True
        for i in range(len(loop) - 1):
            if (bm_mod.verts[loop[i]].co - \
            bm_mod.verts[loop[i+1]].co).length > 1e-6:
                stacked = False
                break
        if stacked:
            continue
        # passed all tests, loop is valid
        valid_loops.append([loop, circular])

    return(valid_loops)


# input: bmesh, output: dict with the edge-key as key and face-index as value
def dict_edge_faces(bm):
    edge_faces = dict([[edgekey(edge), []] for edge in bm.edges if \
        not edge.hide])
    for face in bm.faces:
        if face.hide:
            continue
        for key in face_edgekeys(face):
            edge_faces[key].append(face.index)

    return(edge_faces)


# input: bmesh (edge-faces optional), output: dict with face-face connections
def dict_face_faces(bm, edge_faces=False):
    if not edge_faces:
        edge_faces = dict_edge_faces(bm)

    connected_faces = dict([[face.index, []] for face in bm.faces if \
        not face.hide])
    for face in bm.faces:
        if face.hide:
            continue
        for edge_key in face_edgekeys(face):
            for connected_face in edge_faces[edge_key]:
                if connected_face == face.index:
                    continue
                connected_faces[face.index].append(connected_face)

    return(connected_faces)


# input: bmesh, output: dict with the vert index as key and edge-keys as value
def dict_vert_edges(bm):
    vert_edges = dict([[v.index, []] for v in bm.verts if not v.hide])
    for edge in bm.edges:
        if edge.hide:
            continue
        ek = edgekey(edge)
        for vert in ek:
            vert_edges[vert].append(ek)

    return(vert_edges)


# input: bmesh, output: dict with the vert index as key and face index as value
def dict_vert_faces(bm):
    vert_faces = dict([[v.index, []] for v in bm.verts if not v.hide])
    for face in bm.faces:
        if not face.hide:
            for vert in face.verts:
                vert_faces[vert.index].append(face.index)

    return(vert_faces)


#need: input: list of edge-keys, output: dictionary with vertex-vertex connections
def dict_vert_verts(edge_keys):
    # create connection data
    vert_verts = {}
    for ek in edge_keys:
        for i in range(2):
            if ek[i] in vert_verts:
                vert_verts[ek[i]].append(ek[1-i])
            else:
                vert_verts[ek[i]] = [ek[1-i]]

    return(vert_verts)


#need: return the edgekey ([v1.index, v2.index]) of a bmesh edge
def edgekey(edge):
    return(tuple(sorted([edge.verts[0].index, edge.verts[1].index])))


#need: returns the edgekeys of a bmesh face
def face_edgekeys(face):
    return([tuple(sorted([edge.verts[0].index, edge.verts[1].index])) for \
        edge in face.edges])


#need: calculate input loops
def get_connected_input(object, bm, scene, input):
    # get mesh with modifiers applied
    derived, bm_mod = get_derived_bmesh(object, bm, scene)

    # calculate selected loops
    edge_keys = [edgekey(edge) for edge in bm_mod.edges if \
        edge.select and not edge.hide]
    loops = get_connected_selections(edge_keys)

    # if only selected loops are needed, we're done
    if input == 'selected':
        return(derived, bm_mod, loops)
    # elif input == 'all':
    loops = get_parallel_loops(bm_mod, loops)

    return(derived, bm_mod, loops)


#need: sorts all edge-keys into a list of loops
def get_connected_selections(edge_keys):
    # create connection data
    vert_verts = dict_vert_verts(edge_keys)

    # find loops consisting of connected selected edges
    loops = []
    while len(vert_verts) > 0:
        loop = [iter(vert_verts.keys()).__next__()]
        growing = True
        flipped = False

        # extend loop
        while growing:
            # no more connection data for current vertex
            if loop[-1] not in vert_verts:
                if not flipped:
                    loop.reverse()
                    flipped = True
                else:
                    growing = False
            else:
                extended = False
                for i, next_vert in enumerate(vert_verts[loop[-1]]):
                    if next_vert not in loop:
                        vert_verts[loop[-1]].pop(i)
                        if len(vert_verts[loop[-1]]) == 0:
                            del vert_verts[loop[-1]]
                        # remove connection both ways
                        if next_vert in vert_verts:
                            if len(vert_verts[next_vert]) == 1:
                                del vert_verts[next_vert]
                            else:
                                vert_verts[next_vert].remove(loop[-1])
                        loop.append(next_vert)
                        extended = True
                        break
                if not extended:
                    # found one end of the loop, continue with next
                    if not flipped:
                        loop.reverse()
                        flipped = True
                    # found both ends of the loop, stop growing
                    else:
                        growing = False

        # check if loop is circular
        if loop[0] in vert_verts:
            if loop[-1] in vert_verts[loop[0]]:
                # is circular
                if len(vert_verts[loop[0]]) == 1:
                    del vert_verts[loop[0]]
                else:
                    vert_verts[loop[0]].remove(loop[-1])
                if len(vert_verts[loop[-1]]) == 1:
                    del vert_verts[loop[-1]]
                else:
                    vert_verts[loop[-1]].remove(loop[0])
                loop = [loop, True]
            else:
                # not circular
                loop = [loop, False]
        else:
            # not circular
            loop = [loop, False]

        loops.append(loop)

    return(loops)


#need: get the derived mesh data, if there is a mirror modifier
def get_derived_bmesh(object, bm, scene):
    # check for mirror modifiers
    if 'MIRROR' in [mod.type for mod in object.modifiers if mod.show_viewport]:
        derived = True
        # disable other modifiers
        show_viewport = [mod.name for mod in object.modifiers if \
            mod.show_viewport]
        for mod in object.modifiers:
            if mod.type != 'MIRROR':
                mod.show_viewport = False
        # get derived mesh
        bm_mod = bmesh.new()
        mesh_mod = object.to_mesh(scene, True, 'PREVIEW')
        bm_mod.from_mesh(mesh_mod)
        bpy.context.blend_data.meshes.remove(mesh_mod)
        # re-enable other modifiers
        for mod_name in show_viewport:
            object.modifiers[mod_name].show_viewport = True
    # no mirror modifiers, so no derived mesh necessary
    else:
        derived = False
        bm_mod = bm

    bm_mod.verts.ensure_lookup_table() ### 2.73
    bm_mod.edges.ensure_lookup_table() ### 2.73
    bm_mod.faces.ensure_lookup_table() ### 2.73

    return(derived, bm_mod)


# return a mapping of derived indices to indices
def get_mapping(derived, bm, bm_mod, single_vertices, full_search, loops):
    if not derived:
        return(False)

    if full_search:
        verts = [v for v in bm.verts if not v.hide]
    else:
        verts = [v for v in bm.verts if v.select and not v.hide]

    # non-selected vertices around single vertices also need to be mapped
    if single_vertices:
        mapping = dict([[vert, -1] for vert in single_vertices])
        verts_mod = [bm_mod.verts[vert] for vert in single_vertices]
        for v in verts:
            for v_mod in verts_mod:
                if (v.co - v_mod.co).length < 1e-6:
                    mapping[v_mod.index] = v.index
                    break
        real_singles = [v_real for v_real in mapping.values() if v_real>-1]

        verts_indices = [vert.index for vert in verts]
        for face in [face for face in bm.faces if not face.select \
        and not face.hide]:
            for vert in face.verts:
                if vert.index in real_singles:
                    for v in face.verts:
                        if not v.index in verts_indices:
                            if v not in verts:
                                verts.append(v)
                    break

    # create mapping of derived indices to indices
    mapping = dict([[vert, -1] for loop in loops for vert in loop[0]])
    if single_vertices:
        for single in single_vertices:
            mapping[single] = -1
    verts_mod = [bm_mod.verts[i] for i in mapping.keys()]
    for v in verts:
        for v_mod in verts_mod:
            if (v.co - v_mod.co).length < 1e-6:
                mapping[v_mod.index] = v.index
                verts_mod.remove(v_mod)
                break

    return(mapping)


# calculate the determinant of a matrix
def matrix_determinant(m):
    determinant = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] \
        + m[0][2] * m[1][0] * m[2][1] - m[0][2] * m[1][1] * m[2][0] \
        - m[0][1] * m[1][0] * m[2][2] - m[0][0] * m[1][2] * m[2][1]

    return(determinant)


# custom matrix inversion, to provide higher precision than the built-in one
def matrix_invert(m):
    r = mathutils.Matrix((
        (m[1][1]*m[2][2] - m[1][2]*m[2][1], m[0][2]*m[2][1] - m[0][1]*m[2][2],
        m[0][1]*m[1][2] - m[0][2]*m[1][1]),
        (m[1][2]*m[2][0] - m[1][0]*m[2][2], m[0][0]*m[2][2] - m[0][2]*m[2][0],
        m[0][2]*m[1][0] - m[0][0]*m[1][2]),
        (m[1][0]*m[2][1] - m[1][1]*m[2][0], m[0][1]*m[2][0] - m[0][0]*m[2][1],
        m[0][0]*m[1][1] - m[0][1]*m[1][0])))

    return (r * (1 / matrix_determinant(m)))


#need: returns a list of all loops parallel to the input, input included
def get_parallel_loops(bm_mod, loops):
    # get required dictionaries
    edge_faces = dict_edge_faces(bm_mod)
    connected_faces = dict_face_faces(bm_mod, edge_faces)
    # turn vertex loops into edge loops
    edgeloops = []
    for loop in loops:
        edgeloop = [[sorted([loop[0][i], loop[0][i+1]]) for i in \
            range(len(loop[0])-1)], loop[1]]
        if loop[1]: # circular
            edgeloop[0].append(sorted([loop[0][-1], loop[0][0]]))
        edgeloops.append(edgeloop[:])
    # variables to keep track while iterating
    all_edgeloops = []
    has_branches = False

    for loop in edgeloops:
        # initialise with original loop
        all_edgeloops.append(loop[0])
        newloops = [loop[0]]
        verts_used = []
        for edge in loop[0]:
            if edge[0] not in verts_used:
                verts_used.append(edge[0])
            if edge[1] not in verts_used:
                verts_used.append(edge[1])

        # find parallel loops
        while len(newloops) > 0:
            side_a = []
            side_b = []
            for i in newloops[-1]:
                i = tuple(i)
                forbidden_side = False
                if not i in edge_faces:
                    # weird input with branches
                    has_branches = True
                    break
                for face in edge_faces[i]:
                    if len(side_a) == 0 and forbidden_side != "a":
                        side_a.append(face)
                        if forbidden_side:
                            break
                        forbidden_side = "a"
                        continue
                    elif side_a[-1] in connected_faces[face] and \
                    forbidden_side != "a":
                        side_a.append(face)
                        if forbidden_side:
                            break
                        forbidden_side = "a"
                        continue
                    if len(side_b) == 0 and forbidden_side != "b":
                        side_b.append(face)
                        if forbidden_side:
                            break
                        forbidden_side = "b"
                        continue
                    elif side_b[-1] in connected_faces[face] and \
                    forbidden_side != "b":
                        side_b.append(face)
                        if forbidden_side:
                            break
                        forbidden_side = "b"
                        continue

            if has_branches:
                # weird input with branches
                break

            newloops.pop(-1)
            sides = []
            if side_a:
                sides.append(side_a)
            if side_b:
                sides.append(side_b)

            for side in sides:
                extraloop = []
                for fi in side:
                    for key in face_edgekeys(bm_mod.faces[fi]):
                        if key[0] not in verts_used and key[1] not in \
                        verts_used:
                            extraloop.append(key)
                            break
                if extraloop:
                    for key in extraloop:
                        for new_vert in key:
                            if new_vert not in verts_used:
                                verts_used.append(new_vert)
                    newloops.append(extraloop)
                    all_edgeloops.append(extraloop)

    # input contains branches, only return selected loop
    if has_branches:
        return(loops)

    # change edgeloops into normal loops
    loops = []
    for edgeloop in all_edgeloops:
        loop = []
        # grow loop by comparing vertices between consecutive edge-keys
        for i in range(len(edgeloop)-1):
            for vert in range(2):
                if edgeloop[i][vert] in edgeloop[i+1]:
                    loop.append(edgeloop[i][vert])
                    break
        if loop:
            # add starting vertex
            for vert in range(2):
                if edgeloop[0][vert] != loop[0]:
                    loop = [edgeloop[0][vert]] + loop
                    break
            # add ending vertex
            for vert in range(2):
                if edgeloop[-1][vert] != loop[-1]:
                    loop.append(edgeloop[-1][vert])
                    break
            # check if loop is circular
            if loop[0] == loop[-1]:
                circular = True
                loop = loop[:-1]
            else:
                circular = False
        loops.append([loop, circular])

    return(loops)


#need: gather initial data
def initialise():
    global_undo = bpy.context.user_preferences.edit.use_global_undo
    bpy.context.user_preferences.edit.use_global_undo = False
    object = bpy.context.active_object
    if 'MIRROR' in [mod.type for mod in object.modifiers if mod.show_viewport]:
        # ensure that selection is synced for the derived mesh
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(object.data)

    bm.verts.ensure_lookup_table() ### 2.73
    bm.edges.ensure_lookup_table() ### 2.73
    bm.faces.ensure_lookup_table() ### 2.73

    return(global_undo, object, bm)


#need: move the vertices to their new locations
def move_verts(object, bm, mapping, move, lock, influence):
    if lock:
        lock_x, lock_y, lock_z = lock
        orientation = bpy.context.space_data.transform_orientation
        custom = bpy.context.space_data.current_orientation
        if custom:
            mat = custom.matrix.to_4x4().inverted() * object.matrix_world.copy()
        elif orientation == 'LOCAL':
            mat = mathutils.Matrix.Identity(4)
        elif orientation == 'VIEW':
            mat = bpy.context.region_data.view_matrix.copy() * \
                object.matrix_world.copy()
        else: # orientation == 'GLOBAL'
            mat = object.matrix_world.copy()
        mat_inv = mat.inverted()

    for loop in move:
        for index, loc in loop:
            if mapping:
                if mapping[index] == -1:
                    continue
                else:
                    index = mapping[index]
            if lock:
                delta = (loc - bm.verts[index].co) * mat_inv
                if lock_x:
                    delta[0] = 0
                if lock_y:
                    delta[1] = 0
                if lock_z:
                    delta[2] = 0
                delta = delta * mat
                loc = bm.verts[index].co + delta
            if influence < 0:
                new_loc = loc
            else:
                new_loc = loc*(influence/100) + \
                    bm.verts[index].co*((100-influence)/100)
            bm.verts[index].co = new_loc
    bm.normal_update()
    object.data.update()

    bm.verts.ensure_lookup_table() ### 2.73
    bm.edges.ensure_lookup_table() ### 2.73
    bm.faces.ensure_lookup_table() ### 2.73


#need: load custom tool settings
def settings_load(self):
    
    tp = bpy.context.window_manager.tp_relax_looptools
    
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, tool + "_" + key))


#need: store custom tool settings
def settings_write(self):
    
    tp = bpy.context.window_manager.tp_relax_looptools
    
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, tool + "_" + key, getattr(self, key))


#need: clean up and set settings back to original state
def terminate(global_undo):

    # update editmesh cached data
    obj = bpy.context.active_object
    if obj.mode == 'EDIT':
        bmesh.update_edit_mesh(obj.data, tessface=True, destructive=True)

    bpy.context.user_preferences.edit.use_global_undo = global_undo



##########################################
####### Relax functions ##################
##########################################

#Relax: create lists with knots and points, all correctly sorted
def relax_calculate_knots(loops):
    all_knots = []
    all_points = []
    for loop, circular in loops:
        knots = [[], []]
        points = [[], []]
        if circular:
            if len(loop)%2 == 1: # odd
                extend = [False, True, 0, 1, 0, 1]
            else: # even
                extend = [True, False, 0, 1, 1, 2]
        else:
            if len(loop)%2 == 1: # odd
                extend = [False, False, 0, 1, 1, 2]
            else: # even
                extend = [False, False, 0, 1, 1, 2]
        for j in range(2):
            if extend[j]:
                loop = [loop[-1]] + loop + [loop[0]]
            for i in range(extend[2+2*j], len(loop), 2):
                knots[j].append(loop[i])
            for i in range(extend[3+2*j], len(loop), 2):
                if loop[i] == loop[-1] and not circular:
                    continue
                if len(points[j]) == 0:
                    points[j].append(loop[i])
                elif loop[i] != points[j][0]:
                    points[j].append(loop[i])
            if circular:
                if knots[j][0] != knots[j][-1]:
                    knots[j].append(knots[j][0])
        if len(points[1]) == 0:
            knots.pop(1)
            points.pop(1)
        for k in knots:
            all_knots.append(k)
        for p in points:
            all_points.append(p)

    return(all_knots, all_points)


#Relax: calculate relative positions compared to first knot
def relax_calculate_t(bm_mod, knots, points, regular):
    all_tknots = []
    all_tpoints = []
    for i in range(len(knots)):
        amount = len(knots[i]) + len(points[i])
        mix  = []
        for j in range(amount):
            if j%2 == 0:
                mix.append([True, knots[i][round(j/2)]])
            elif j == amount-1:
                mix.append([True, knots[i][-1]])
            else:
                mix.append([False, points[i][int(j/2)]])
        len_total = 0
        loc_prev = False
        tknots = []
        tpoints = []
        for m in mix:
            loc = mathutils.Vector(bm_mod.verts[m[1]].co[:])
            if not loc_prev:
                loc_prev = loc
            len_total += (loc - loc_prev).length
            if m[0]:
                tknots.append(len_total)
            else:
                tpoints.append(len_total)
            loc_prev = loc
        if regular:
            tpoints = []
            for p in range(len(points[i])):
                tpoints.append((tknots[p] + tknots[p+1]) / 2)
        all_tknots.append(tknots)
        all_tpoints.append(tpoints)

    return(all_tknots, all_tpoints)


#Relax: change the location of the points to their place on the spline
def relax_calculate_verts(bm_mod, interpolation, tknots, knots, tpoints,
points, splines):
    change = []
    move = []
    for i in range(len(knots)):
        for p in points[i]:
            m = tpoints[i][points[i].index(p)]
            if m in tknots[i]:
                n = tknots[i].index(m)
            else:
                t = tknots[i][:]
                t.append(m)
                t.sort()
                n = t.index(m)-1
            if n > len(splines[i]) - 1:
                n = len(splines[i]) - 1
            elif n < 0:
                n = 0

            if interpolation == 'cubic':
                ax, bx, cx, dx, tx = splines[i][n][0]
                x = ax + bx*(m-tx) + cx*(m-tx)**2 + dx*(m-tx)**3
                ay, by, cy, dy, ty = splines[i][n][1]
                y = ay + by*(m-ty) + cy*(m-ty)**2 + dy*(m-ty)**3
                az, bz, cz, dz, tz = splines[i][n][2]
                z = az + bz*(m-tz) + cz*(m-tz)**2 + dz*(m-tz)**3
                change.append([p, mathutils.Vector([x,y,z])])
            else: # interpolation == 'linear'
                a, d, t, u = splines[i][n]
                if u == 0:
                    u = 1e-8
                change.append([p, ((m-t)/u)*d + a])
    for c in change:
        move.append([c[0], (bm_mod.verts[c[0]].co + c[1]) / 2])

    return(move)




# Relax Operator
class Relax(bpy.types.Operator):
    bl_idname = "edit_mesh.looptools_relax"
    bl_label = "Relax"
    bl_description = "Relax the loop, so it is smoother"
    bl_options = {'REGISTER', 'UNDO'}

    input = bpy.props.EnumProperty(name = "Input",
        items = (("all", "Parallel (all)", "Also use non-selected "\
                "parallel loops as input"),
            ("selected", "Selection","Only use selected vertices as input")),
        description = "Loops that are relaxed",
        default = 'selected')

    interpolation = bpy.props.EnumProperty(name = "Interpolation",
        items = (("cubic", "Cubic", "Natural cubic spline, smooth results"),
            ("linear", "Linear", "Simple and fast linear algorithm")),
        description = "Algorithm used for interpolation",
        default = 'cubic')

    iterations = bpy.props.EnumProperty(name = "Iterations",
        items = (("1", "1", "One"),
            ("3", "3", "Three"),
            ("5", "5", "Five"),
            ("10", "10", "Ten"),
            ("25", "25", "Twenty-five")),
        description = "Number of times the loop is relaxed",
        default = "1")

    regular = bpy.props.BoolProperty(name = "Regular",
        description = "Distribute vertices at constant distances along the" \
            "loop",
        default = True)

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return(ob and ob.type == 'MESH' and context.mode == 'EDIT_MESH')

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.prop(self, "interpolation")
        col.prop(self, "input")
        col.prop(self, "iterations")
        col.prop(self, "regular")

    def invoke(self, context, event):
        # load custom settings
        settings_load(self)
        return self.execute(context)

    def execute(self, context):
        # initialise
        global_undo, object, bm = initialise()
        settings_write(self)
        # check cache to see if we can save time
        cached, single_loops, loops, derived, mapping = cache_read("Relax",
            object, bm, self.input, False)
        if cached:
            derived, bm_mod = get_derived_bmesh(object, bm, context.scene)
        else:
            # find loops
            derived, bm_mod, loops = get_connected_input(object, bm,
                context.scene, self.input)
            mapping = get_mapping(derived, bm, bm_mod, False, False, loops)
            loops = check_loops(loops, mapping, bm_mod)
        knots, points = relax_calculate_knots(loops)

        # saving cache for faster execution next time
        if not cached:
            cache_write("Relax", object, bm, self.input, False, False, loops,
                derived, mapping)

        for iteration in range(int(self.iterations)):
            # calculate splines and new positions
            tknots, tpoints = relax_calculate_t(bm_mod, knots, points,
                self.regular)
            splines = []
            for i in range(len(knots)):
                splines.append(calculate_splines(self.interpolation, bm_mod,
                    tknots[i], knots[i]))
            move = [relax_calculate_verts(bm_mod, self.interpolation,
                tknots, knots, tpoints, points, splines)]
            move_verts(object, bm, mapping, move, False, -1)

        # cleaning up
        if derived:
            bm_mod.free()
        terminate(global_undo)

        return{'FINISHED'}




# property group containing all properties for the gui in the panel
class Relax_LoopToolsProps(bpy.types.PropertyGroup):


    # open/close general display properties
    display_tp_relax = bpy.props.BoolProperty(name = "Relax settings",
        description = "Display settings of the Relax tool",
        default = False)

    # relax properties
    relax_input = bpy.props.EnumProperty(name = "Input",
        items = (("all", "Parallel (all)", "Also use non-selected "\
                "parallel loops as input"),
            ("selected", "Selection","Only use selected vertices as input")),
        description = "Loops that are relaxed",
        default = 'selected')

    relax_interpolation = bpy.props.EnumProperty(name = "Interpolation",
        items = (("cubic", "Cubic", "Natural cubic spline, smooth results"),
            ("linear", "Linear", "Simple and fast linear algorithm")),
        description = "Algorithm used for interpolation",
        default = 'cubic')

    relax_iterations = bpy.props.EnumProperty(name = "Iterations",
        items = (("1", "1", "One"),
            ("3", "3", "Three"),
            ("5", "5", "Five"),
            ("10", "10", "Ten"),
            ("25", "25", "Twenty-five")),
        description = "Number of times the loop is relaxed",
        default = "1")

    relax_regular = bpy.props.BoolProperty(name = "Regular",
        description = "Distribute vertices at constant distances along the" \
            "loop",
        default = True)


# define classes for registration
classes = [Relax_LoopToolsProps, Relax]


# registering and menu integration
def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.WindowManager.tp_relax_looptools = bpy.props.PointerProperty(type = Relax_LoopToolsProps)


# unregistering and removing menus
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


    try:
        del bpy.types.WindowManager.tp_relax_looptools
    except:
        pass


if __name__ == "__main__":
    register()
