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
"""
bl_info = {
    "name": "Looptools Circle",
    "author": "Bart Crouch",
    "version": (4, 6, 5),
    "blender": (2, 72, 2),
    "description": "Mesh modelling",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Modeling/looptools",
}

# ATTENTION: this is a reduced looptool function for us as an internal operator. 

"""



import bmesh
import bpy
import collections
import mathutils
import math
from bpy_extras import view3d_utils


####### GENERAL FUNCTIONS #################

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

    #if method == 'best_fit':
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

    return(com, normal)



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


# input: list of edge-keys, output: dictionary with vertex-vertex connections
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


# return the edgekey ([v1.index, v2.index]) of a bmesh edge
def edgekey(edge):
    return(tuple(sorted([edge.verts[0].index, edge.verts[1].index])))


# returns the edgekeys of a bmesh face
def face_edgekeys(face):
    return([tuple(sorted([edge.verts[0].index, edge.verts[1].index])) for \
        edge in face.edges])



# sorts all edge-keys into a list of loops
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


# get the derived mesh data, if there is a mirror modifier
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


# gather initial data
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


# move the vertices to their new locations
def move_verts(object, bm, mapping, move, lock, influence):

    for loop in move:
        for index, loc in loop:
            if mapping:
                if mapping[index] == -1:
                    continue
                else:
                    index = mapping[index]

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



####### RESET SETTINGS #################

# clean up and set settings back to original state
def terminate(global_undo):
    # update editmesh cached data
    obj = bpy.context.active_object
    if obj.mode == 'EDIT':
        bmesh.update_edit_mesh(obj.data, tessface=True, destructive=True)

    bpy.context.user_preferences.edit.use_global_undo = global_undo




####### CIRCLE FUNCTIONS #################

# convert 3d coordinates to 2d coordinates on plane
def circle_3d_to_2d(bm_mod, loop, com, normal):
    # project vertices onto the plane
    verts = [bm_mod.verts[v] for v in loop[0]]
    verts_projected = [[v.co - (v.co - com).dot(normal) * normal, v.index]
                       for v in verts]

    # calculate two vectors (p and q) along the plane
    m = mathutils.Vector((normal[0] + 1.0, normal[1], normal[2]))
    p = m - (m.dot(normal) * normal)
    if p.dot(p) < 1e-6:
        m = mathutils.Vector((normal[0], normal[1] + 1.0, normal[2]))
        p = m - (m.dot(normal) * normal)
    q = p.cross(normal)

    # change to 2d coordinates using perpendicular projection
    locs_2d = []
    for loc, vert in verts_projected:
        vloc = loc - com
        x = p.dot(vloc) / p.dot(p)
        y = q.dot(vloc) / q.dot(q)
        locs_2d.append([x, y, vert])

    return(locs_2d, p, q)


# calculate a best-fit circle to the 2d locations on the plane
def circle_calculate_best_fit(locs_2d):
    # initial guess
    x0 = 0.0
    y0 = 0.0
    r = 1.0

    # calculate center and radius (non-linear least squares solution)
    for iter in range(500):
        jmat = []
        k = []
        for v in locs_2d:
            d = (v[0]**2-2.0*x0*v[0]+v[1]**2-2.0*y0*v[1]+x0**2+y0**2)**0.5
            jmat.append([(x0-v[0])/d, (y0-v[1])/d, -1.0])
            k.append(-(((v[0]-x0)**2+(v[1]-y0)**2)**0.5-r))
        jmat2 = mathutils.Matrix(((0.0, 0.0, 0.0),
                                  (0.0, 0.0, 0.0),
                                  (0.0, 0.0, 0.0),
                                  ))
        k2 = mathutils.Vector((0.0, 0.0, 0.0))
        for i in range(len(jmat)):
            k2 += mathutils.Vector(jmat[i])*k[i]
            jmat2[0][0] += jmat[i][0]**2
            jmat2[1][0] += jmat[i][0]*jmat[i][1]
            jmat2[2][0] += jmat[i][0]*jmat[i][2]
            jmat2[1][1] += jmat[i][1]**2
            jmat2[2][1] += jmat[i][1]*jmat[i][2]
            jmat2[2][2] += jmat[i][2]**2
        jmat2[0][1] = jmat2[1][0]
        jmat2[0][2] = jmat2[2][0]
        jmat2[1][2] = jmat2[2][1]
        try:
            jmat2.invert()
        except:
            pass
        dx0, dy0, dr = jmat2 * k2
        x0 += dx0
        y0 += dy0
        r += dr
        # stop iterating if we're close enough to optimal solution
        if abs(dx0)<1e-6 and abs(dy0)<1e-6 and abs(dr)<1e-6:
            break

    # return center of circle and radius
    return(x0, y0, r)





# calculate the new locations of the vertices that need to be moved
def circle_calculate_verts(flatten, bm_mod, locs_2d, com, p, q, normal):
    # changing 2d coordinates back to 3d coordinates
    locs_3d = []
    for loc in locs_2d:
        locs_3d.append([loc[2], loc[0]*p + loc[1]*q + com])

    if flatten: # flat circle
        return(locs_3d)

    else: # project the locations on the existing mesh
        vert_edges = dict_vert_edges(bm_mod)
        vert_faces = dict_vert_faces(bm_mod)
        faces = [f for f in bm_mod.faces if not f.hide]
        rays = [normal, -normal]
        new_locs = []
        for loc in locs_3d:
            projection = False
            if bm_mod.verts[loc[0]].co == loc[1]: # vertex hasn't moved
                projection = loc[1]
            else:
                dif = normal.angle(loc[1]-bm_mod.verts[loc[0]].co)
                if -1e-6 < dif < 1e-6 or math.pi-1e-6 < dif < math.pi+1e-6:
                    # original location is already along projection normal
                    projection = bm_mod.verts[loc[0]].co
                else:
                    # quick search through adjacent faces
                    for face in vert_faces[loc[0]]:
                        verts = [v.co for v in bm_mod.faces[face].verts]
                        if len(verts) == 3: # triangle
                            v1, v2, v3 = verts
                            v4 = False
                        else: # assume quad
                            v1, v2, v3, v4 = verts[:4]
                        for ray in rays:
                            intersect = mathutils.geometry.\
                            intersect_ray_tri(v1, v2, v3, ray, loc[1])
                            if intersect:
                                projection = intersect
                                break
                            elif v4:
                                intersect = mathutils.geometry.\
                                intersect_ray_tri(v1, v3, v4, ray, loc[1])
                                if intersect:
                                    projection = intersect
                                    break
                        if projection:
                            break
            if not projection:
                # check if projection is on adjacent edges
                for edgekey in vert_edges[loc[0]]:
                    line1 = bm_mod.verts[edgekey[0]].co
                    line2 = bm_mod.verts[edgekey[1]].co
                    intersect, dist = mathutils.geometry.intersect_point_line(\
                        loc[1], line1, line2)
                    if 1e-6 < dist < 1 - 1e-6:
                        projection = intersect
                        break
            if not projection:
                # full search through the entire mesh
                hits = []
                for face in faces:
                    verts = [v.co for v in face.verts]
                    if len(verts) == 3: # triangle
                        v1, v2, v3 = verts
                        v4 = False
                    else: # assume quad
                        v1, v2, v3, v4 = verts[:4]
                    for ray in rays:
                        intersect = mathutils.geometry.intersect_ray_tri(\
                            v1, v2, v3, ray, loc[1])
                        if intersect:
                            hits.append([(loc[1] - intersect).length,
                                intersect])
                            break
                        elif v4:
                            intersect = mathutils.geometry.intersect_ray_tri(\
                                v1, v3, v4, ray, loc[1])
                            if intersect:
                                hits.append([(loc[1] - intersect).length,
                                    intersect])
                                break
                if len(hits) >= 1:
                    # if more than 1 hit with mesh, closest hit is new loc
                    hits.sort()
                    projection = hits[0][1]
            if not projection:
                # nothing to project on, remain at flat location
                projection = loc[1]
            new_locs.append([loc[0], projection])

        # return new positions of projected circle
        return(new_locs)


# check loops and only return valid ones
def circle_check_loops(single_loops, loops, mapping, bm_mod):
    valid_single_loops = {}
    valid_loops = []
    for i, [loop, circular] in enumerate(loops):
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
        # loop has to be non-collinear
        collinear = True
        loc0 = mathutils.Vector(bm_mod.verts[loop[0]].co[:])
        loc1 = mathutils.Vector(bm_mod.verts[loop[1]].co[:])
        for v in loop[2:]:
            locn = mathutils.Vector(bm_mod.verts[v].co[:])
            if loc0 == loc1 or loc1 == locn:
                loc0 = loc1
                loc1 = locn
                continue
            d1 = loc1-loc0
            d2 = locn-loc1
            if -1e-6 < d1.angle(d2, 0) < 1e-6:
                loc0 = loc1
                loc1 = locn
                continue
            collinear = False
            break
        if collinear:
            continue
        # passed all tests, loop is valid
        valid_loops.append([loop, circular])
        valid_single_loops[len(valid_loops)-1] = single_loops[i]

    return(valid_single_loops, valid_loops)


# calculate the location of single input vertices that need to be flattened
def circle_flatten_singles(bm_mod, com, p, q, normal, single_loop):
    new_locs = []
    for vert in single_loop:
        loc = mathutils.Vector(bm_mod.verts[vert].co[:])
        new_locs.append([vert,  loc - (loc-com).dot(normal)*normal])

    return(new_locs)


# calculate input loops
def circle_get_input(object, bm, scene):
    # get mesh with modifiers applied
    derived, bm_mod = get_derived_bmesh(object, bm, scene)

    # create list of edge-keys based on selection state
    faces = False
    for face in bm.faces:
        if face.select and not face.hide:
            faces = True
            break
    if faces:
        # get selected, non-hidden , non-internal edge-keys
        eks_selected = [key for keys in [face_edgekeys(face) for face in \
            bm_mod.faces if face.select and not face.hide] for key in keys]
        edge_count = {}
        for ek in eks_selected:
            if ek in edge_count:
                edge_count[ek] += 1
            else:
                edge_count[ek] = 1
        edge_keys = [edgekey(edge) for edge in bm_mod.edges if edge.select \
            and not edge.hide and edge_count.get(edgekey(edge), 1)==1]
    else:
        # no faces, so no internal edges either
        edge_keys = [edgekey(edge) for edge in bm_mod.edges if edge.select \
            and not edge.hide]

    # add edge-keys around single vertices
    verts_connected = dict([[vert, 1] for edge in [edge for edge in \
        bm_mod.edges if edge.select and not edge.hide] for vert in \
        edgekey(edge)])
    single_vertices = [vert.index for vert in bm_mod.verts if \
        vert.select and not vert.hide and not \
        verts_connected.get(vert.index, False)]

    if single_vertices and len(bm.faces)>0:
        vert_to_single = dict([[v.index, []] for v in bm_mod.verts \
            if not v.hide])
        for face in [face for face in bm_mod.faces if not face.select \
        and not face.hide]:
            for vert in face.verts:
                vert = vert.index
                if vert in single_vertices:
                    for ek in face_edgekeys(face):
                        if not vert in ek:
                            edge_keys.append(ek)
                            if vert not in vert_to_single[ek[0]]:
                                vert_to_single[ek[0]].append(vert)
                            if vert not in vert_to_single[ek[1]]:
                                vert_to_single[ek[1]].append(vert)
                    break

    # sort edge-keys into loops
    loops = get_connected_selections(edge_keys)

    # find out to which loops the single vertices belong
    single_loops = dict([[i, []] for i in range(len(loops))])
    if single_vertices and len(bm.faces)>0:
        for i, [loop, circular] in enumerate(loops):
            for vert in loop:
                if vert_to_single[vert]:
                    for single in vert_to_single[vert]:
                        if single not in single_loops[i]:
                            single_loops[i].append(single)

    return(derived, bm_mod, single_vertices, single_loops, loops)


# recalculate positions based on the influence of the circle shape
def circle_influence_locs(locs_2d, new_locs_2d, influence):
    for i in range(len(locs_2d)):
        oldx, oldy, j = locs_2d[i]
        newx, newy, k = new_locs_2d[i]
        altx = newx*(influence/100)+ oldx*((100-influence)/100)
        alty = newy*(influence/100)+ oldy*((100-influence)/100)
        locs_2d[i] = [altx, alty, j]

    return(locs_2d)


# project 2d locations on circle, respecting distance relations between verts
def circle_project_non_regular(locs_2d, x0, y0, r):
    for i in range(len(locs_2d)):
        x, y, j = locs_2d[i]
        loc = mathutils.Vector([x-x0, y-y0])
        loc.length = r
        locs_2d[i] = [loc[0], loc[1], j]

    return(locs_2d)


# project 2d locations on circle, with equal distance between all vertices
def circle_project_regular(locs_2d, x0, y0, r):
    # find offset angle and circling direction
    x, y, i = locs_2d[0]
    loc = mathutils.Vector([x-x0, y-y0])
    loc.length = r
    offset_angle = loc.angle(mathutils.Vector([1.0, 0.0]), 0.0)
    loca = mathutils.Vector([x-x0, y-y0, 0.0])
    if loc[1] < -1e-6:
        offset_angle *= -1
    x, y, j = locs_2d[1]
    locb = mathutils.Vector([x-x0, y-y0, 0.0])
    if loca.cross(locb)[2] >= 0:
        ccw = 1
    else:
        ccw = -1
    # distribute vertices along the circle
    for i in range(len(locs_2d)):
        t = offset_angle + ccw * (i / len(locs_2d) * 2 * math.pi)
        x = math.cos(t) * r
        y = math.sin(t) * r
        locs_2d[i] = [x, y, locs_2d[i][2]]

    return(locs_2d)


# shift loop, so the first vertex is closest to the center
def circle_shift_loop(bm_mod, loop, com):
    verts, circular = loop
    distances = [[(bm_mod.verts[vert].co - com).length, i] \
        for i, vert in enumerate(verts)]
    distances.sort()
    shift = distances[0][1]
    loop = [verts[shift:] + verts[:shift], circular]

    return(loop)




# circle operator
class VIEW3D_TP_LPT_Circle_Internal(bpy.types.Operator):
    bl_idname = "tp_mesh.lt_circle"
    bl_label = "Circle"
    bl_description = "Move selected vertices into a circle shape"
    bl_options = {'REGISTER', 'INTERNAL'}


    # PROPS OPERATOR (F6)

    flatten = bpy.props.BoolProperty(name = "Flatten",
        description = "Flatten the circle, instead of projecting it on the mesh",
        default = True)

    influence = bpy.props.FloatProperty(name = "Influence",
        description = "Force of the tool",
        default = 100.0,
        min = 0.0,
        max = 100.0,
        precision = 1,
        subtype = 'PERCENTAGE')


    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return(ob and ob.type == 'MESH' and context.mode == 'EDIT_MESH')
    
    
    def execute(self, context):
        # initialise
        global_undo, object, bm = initialise()

        derived, bm_mod, single_vertices, single_loops, loops = circle_get_input(object, bm, context.scene)
        mapping = get_mapping(derived, bm, bm_mod, single_vertices, False, loops)
        single_loops, loops = circle_check_loops(single_loops, loops, mapping, bm_mod)

        move = []
        for i, loop in enumerate(loops):
           
            # best fitting flat plane
            com, normal = calculate_plane(bm_mod, loop)
           
            # if circular, shift loop so we get a good starting vertex
            if loop[1]:
                loop = circle_shift_loop(bm_mod, loop, com)
          
            # flatten vertices on plane
            locs_2d, p, q = circle_3d_to_2d(bm_mod, loop, com, normal)
           
            # calculate circle best
            x0, y0, r = circle_calculate_best_fit(locs_2d)
            
            # calculate positions on circle
            new_locs_2d = circle_project_regular(locs_2d[:], x0, y0, r)

            # take influence into account
            locs_2d = circle_influence_locs(locs_2d, new_locs_2d, self.influence)
          
            # calculate 3d positions of the created 2d input
            move.append(circle_calculate_verts(self.flatten, bm_mod, locs_2d, com, p, q, normal))
        
            # flatten single input vertices on plane defined by loop           
            #if self.flatten and single_loops:
            move.append(circle_flatten_singles(bm_mod, com, p, q, normal, single_loops[i]))

        # move vertices to new locations
        lock = False
        move_verts(object, bm, mapping, move, lock, -1)

        # cleaning up
        if derived:
            bm_mod.free()
        terminate(global_undo)

        return{'FINISHED'}





def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 