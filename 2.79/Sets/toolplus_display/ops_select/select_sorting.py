# ab_mesh_sorting_tools.py Copyright (C) 2012, Jakub Zolcik
#
# Searches through files in file browser by name.
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

"""
bl_info = {
    "name": "Mesh Sorting Tools",
    "author": "Jakub Zolcik",
    "version": (0, 0, 1),
    "blender": (2, 7, 2),
    "location": "View3D -> Tool Shelf",
    "description": "Allows advanced sorting of meshes.",
    "warning": "",
    "wiki_url": "http://studio.allblue.pl/wiki/wikis/blender/mesh-sorting-tools/",
    "tracker_url": "https://github.com/sftd/AllBlue-Blender-Tools",
    "category": "Mesh"
}


Usage:

To Do.
"""


# LOAD MODUL #    
import bpy
import bmesh
import sys

from operator import itemgetter
from random import randint
from random import shuffle

def sort_objects_enum(self, context):
    items = list()
    items.append(tuple(['NONE', '', 'NONE']))
    
    for obj in bpy.context.scene.objects:        
        if obj.type == 'MESH':
            name = obj.name
            items.append(tuple([name, name, name]))
        
    items = tuple(items)
    return items

    
class MSTSortMeshElementsOperator(bpy.types.Operator):
    """MST Sort Mesh Elements"""
    bl_idname = "object.mst_sort_mesh_elements"
    bl_label = "MST Sort Mesh Elements"
    
    @classmethod
    def poll(cls, context):        
        return operator_poll(context)        

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)    
    
    def draw(self, context):        
        draw_options(self.layout, context)
        
    def get_vars(self, context):
        
        self.sort_from = context.window_manager.mst_sort_from
        self.sort_object = context.window_manager.mst_sort_object
        self.sort_verts = True #context.window_manager.mst_sort_verts
        self.sort_faces = context.window_manager.mst_sort_faces
        self.connected_first = context.window_manager.mst_connected_first
        self.from_faces = context.window_manager.mst_from_faces
        self.reverse = context.window_manager.mst_reverse

    def execute(self, context):                        
        
        self.get_vars(context)
        
        bpy.ops.object.mode_set(mode='OBJECT')            
        
        start_cos = []
        
        obj = context.active_object        
        data = obj.data
        bm = bmesh.new()
        bm.from_mesh(data)
        
        if self.sort_from == 'CURSOR':
            self.select_from_cursor(context, bm)
        elif self.sort_from == 'WEIGHTS' or self.sort_from == 'RANDOMIZE':
            self.select_from_weights(context, bm)
        
        
        verts_matches = None
        faces_matches = None                
        
        #if self.sort_from == 'CURSOR' or self.sort_from == 'SELECTED':
        
        if self.from_faces:
            for f in bm.faces:
                if f.select:
                    start_cos.append(f.calc_center_median())

        else:
            for v in bm.verts:
                if v.select:
                    start_cos.append(v.co)                
       
    
        if len(start_cos) <= 0:
            print('No mesh elements selected.')
            bpy.ops.object.mode_set(mode='EDIT')
            return {'CANCELLED'}
        
        
        print("\n\nCalculating distances...")
        
        
        if self.sort_from=='RANDOMIZE':
            use_rand = True
        else:
            use_rand = False
        
        if (self.sort_from == 'OBJECT'):
                
            if (self.sort_object == 'NONE'):
                return
            
            self.from_faces = False
            
            t_bm = bmesh.new()
            t_bm.from_mesh(context.scene.objects[self.sort_object].data)
        
        
        if self.sort_verts:
            
            if self.sort_from == 'WEIGHTS':
                v_dists = self.set_v_weights(obj, bm.verts)
            elif self.sort_from != 'OBJECT':
                v_dists = self.set_v_dists(start_cos, bm.verts, use_rand)
                
            vlen = len(bm.verts)                
            verts_matches = [-1] * vlen
            
        if self.sort_faces:
            flen = len(bm.faces)    
            faces_matches = [-1] * flen
            f_centers = []
            i = 0
            for f in bm.faces:
                f_centers.append(f.calc_center_median())
                if self.sort_from == 'SELECTED' and self.from_faces:
                    if f.select:
                        faces_matches[f.index] = i
                        i += 1
                    
            if (self.sort_from == 'OBJECT'): 
                loop_steps = [-1] * len(data.loops)        
                t_f_centers = []
                for f in t_bm.faces:
                    t_f_centers.append(f.calc_center_median())
            elif self.sort_from == 'WEIGHTS':    
                f_dists = self.set_f_weights(obj, bm.faces, bm.verts)
            else: 
                f_dists = self.set_f_dists(start_cos, bm.faces, f_centers, use_rand)
                
        print("Sorting Started")
        
        if self.connected_first:            
            available_verts = []
            for i in range(len(start_cos)):
                available_verts.append([])
        
        
        if self.sort_from == 'OBJECT':
            next_vi = 0
            t_len = len(bm.faces)
            s_len = len(t_bm.faces)
            t_faces = bm.faces[:]
            #s_faces = s_faces[:]
            i_range = list(range(t_len))
            shuffle(i_range)
            
            j = 0
            
            for i in i_range:
                
                s_i = int(s_len * i / t_len)
                
                t_f = self.get_closest_face_ob(t_faces, f_centers, t_f_centers[s_i])
                t_faces.remove(t_f)
                faces_matches[t_f.index] = i
                
                
                t_verts = t_f.verts[:]
                
                i_s_l = 0
                t_loops = t_f.loops[:]
                s_loops = t_bm.faces[s_i].loops
                
                first = True
                
                for ii in range(len(t_f.loops)):
                    
                    i_l, t_l = self.get_closest_loop_ob(t_loops, s_loops[i_s_l], f_centers[t_f.index], t_f_centers[s_i])
                    t_loops.remove(t_l)
                    
                    if (first):
                        loop_steps[t_f.index] = i_l
                        first = False
                    
                    if (self.sort_verts):
                        if (verts_matches[t_l.vert.index] == -1):
                            verts_matches[t_l.vert.index] = next_vi
                            next_vi += 1
                    else:
                        break
                            
                    if (i_s_l + 1 < len(s_loops)):
                        i_s_l += 1
                    
                j += 1                        
                if j % 100 == 0:
                    print("Matched Faces: ", j)
                    
                    
                    
            if (self.sort_verts):
                for v in t_f.verts:
                    if (verts_matches[v.index] == -1):
                        printf("Should'nt happen for now.")
                        verts_matches[v.index] = next_vi
                        next_vi += 1
                        
                #print("s_f: " + str(s_f.index) + ", i: " + str(i))                                                                                
        elif self.sort_faces and not self.connected_first:
            finish = False
        
            if self.from_faces:
                i = len(start_cos)            
            else:
                i = 0
                
            while not finish:
                
                for sco in range(len(start_cos)):
                    
                    f = self.get_closest_face(sco, f_dists, faces_matches)
                    faces_matches[f.index] = i
                    
                    i += 1
                    
                    if i % 100 == 0:
                        print("Matched Faces: ", i)
                    
                    if i >= flen:
                        finish = True
                        break;
        
        
        if self.sort_verts and self.sort_from != 'OBJECT':
            finish = False
        
            i = 0            
            fi = 0
            while not finish:
                
                for sco_i in range(len(start_cos)):
                    
                    if self.connected_first:
                        v = self.get_connected_vert(sco_i, v_dists, verts_matches, available_verts)
                        if self.sort_faces:
                            for f in v.link_faces:
                                if faces_matches[f.index] == -1:
                                    faces_matches[f.index] = fi
                                    fi += 1
                    else:
                        v = self.get_closest_vert(sco_i, v_dists, verts_matches)         
                    
                    verts_matches[v.index] = i
                    
                    i += 1
                    
                    if i % 100 == 0:
                        print("Matched Verts: ", i)
                    
                    if i >= vlen:
                        finish = True
                        break;
        
        
        print("Replacing Started...")
        
        self.replace_all(verts_matches, faces_matches, data)
        
        if (self.sort_from == 'OBJECT'):
            self.slide_loops(loop_steps, data)
                
        bpy.ops.object.mode_set(mode='EDIT')
                    
        print("Finished")                 
        
        return {'FINISHED'}
    
    def select_from_weights(self, context, bm):
        
        first = True                          
                
        for v in bm.verts:
            if first:
                v.select = True
                first = False
            else:
                v.select = False
    
    def select_from_cursor(self, context, bm):
        
        cur = context.space_data.cursor_location
        bdist = 99999
        bv = None
        for v in bm.verts:
            cdist = self.calc_dist(cur, v.co)
            if cdist < bdist:
                bdist = cdist
                bv = v                    
                
        for v in bm.verts:
            if v == bv:
                v.select = True
            else:
                v.select = False
    
    def get_closest_vert(self, sco_i, v_dists, verts_matches):                
        dist, v = v_dists[sco_i].pop()
        
        while verts_matches[v.index] != -1:
            dist, v = v_dists[sco_i].pop()
        
        return v
    
    def get_closest_face(self, sco_i, f_dists, faces_matches):                
        dist, f = f_dists[sco_i].pop()
        
        while faces_matches[f.index] != -1:
            dist, f = f_dists[sco_i].pop()
        
        return f
    
    def get_closest_face_ob(self, s_faces, f_centers, co):
        dist = 99999
        f = None
        
        #print("s_face len: " + str(len(s_faces)))
        
        for s_f in s_faces:
            
            t_dist = self.calc_dist(f_centers[s_f.index], co)
            if (t_dist < dist):
                dist = t_dist
                f = s_f
        
        return f
    
    def get_closest_loop_ob(self, s_loops, t_l, s_center, t_center):                
        dist = 99999
        l = None
        i_l = -1
        
        #print("s_face len: " + str(len(s_faces)))
        i = 0
        for i in range(len(s_loops)):
            
            s_l = s_loops[i]
            
            t_dist = self.calc_dist(s_l.vert.co - s_center, t_l.vert.co - t_center)
            if (t_dist < dist):
                dist = t_dist
                l = s_l
                i_l = i
        
        return i_l, l
    
    
    def get_connected_vert(self, sco_i, v_dists, verts_matches, available_verts):
        if len(available_verts[sco_i]) > 0:
            while True:
                v = available_verts[sco_i].pop(0)
                
                if verts_matches[v.index] == -1:
                    self.add_available_verts(sco_i, v, available_verts, verts_matches)
                    return v
                if len(available_verts[sco_i]) <= 0:
                    break
                
        v = self.get_closest_vert(sco_i, v_dists, verts_matches)
        self.add_available_verts(sco_i, v, available_verts, verts_matches)
                        
        return v
        
    
    def add_available_verts(self, sco_i, v, available_verts, verts_matches):
        
        for ed in v.link_edges:
            nv = ed.other_vert(v)
            if nv not in available_verts[sco_i]:
                if verts_matches[nv.index] == -1:
                    available_verts[sco_i].append(nv)
    
    
    def set_v_weights(self, obj, verts):
        gr_i = obj.vertex_groups.active_index
        lay_i = verts.layers.deform.active
        dists = []
        calc = 0
        vlen = len(verts)
        v_dists = []
        
        for v in verts:
            dvert = v[lay_i]            
            
            if gr_i in dvert:
                dist = dvert[gr_i]
            else:
                dist = 0
        
            v_dists.append((dist, v))
                
            calc += 1
            if calc % 100 == 0:
                print('Calculated:', calc)                    
            
        print('Sorting')
        v_dists.sort(key=itemgetter(0), reverse=self.reverse)
        dists.append(v_dists)
                
        return dists    
    
    
    def set_f_weights(self, obj, faces, verts):
        gr_i = obj.vertex_groups.active_index
        lay_i = verts.layers.deform.active
        dists = []
        calc = 0
        flen = len(faces)
        f_dists = []
        
        for f in faces:
            
            sum = 0
            sum_i = 0
            
            for v in f.verts:                      
                dvert = v[lay_i]     
                
                if gr_i in dvert:
                    sum += dvert[gr_i]

                sum_i += 1
                
            dist = sum / sum_i
        
            f_dists.append((dist, f))
                
            calc += 1
            if calc % 100 == 0:
                print('Calculated:', calc)                    
            
        print('Sorting')
        f_dists.sort(key=itemgetter(0), reverse=self.reverse)
        dists.append(f_dists)
                
        return dists    
    
        
    def set_v_dists(self, scos, verts, rand=False):
        dists = []               
        calc = 0
        vlen = len(verts)
        
        for co in scos:
            v_dists = []            
            for v in verts:
                if rand:
                    dist = randint(0, vlen)
                else:
                    dist = self.calc_dist(co, v.co)
                    
                v_dists.append((dist, v))
                
                calc += 1
                if calc % 100 == 0:
                    print('Calculated:', calc)
            
            print('Sorting')
            v_dists.sort(key=itemgetter(0), reverse=not self.reverse)
            dists.append(v_dists)
                
                
        return dists
    
    
    def set_f_dists(self, scos, faces, f_centers, rand=False):
        dists = []               
        calc = 0
        flen = len(faces)
        
        for co in scos:
            f_dists = []            
            for i in range(flen):
                fc = f_centers[i]
                if rand:
                    dist = randint(0, flen)
                else:
                    dist = self.calc_dist(co, fc)
                faces.ensure_lookup_table()
                f_dists.append((dist, faces[i]))
                
                calc += 1
                if calc % 100 == 0:
                    print('Calculated:', calc)
            
            print('Sorting')
            f_dists.sort(key=itemgetter(0), reverse=not self.reverse)
            dists.append(f_dists)
                
                
        return dists
    
    
    def calc_dist(self, co1, co2):
        
        return (co1[0] - co2[0]) * (co1[0] - co2[0]) + (co1[1] - co2[1]) * (co1[1] - co2[1]) + (co1[2] - co2[2]) * (co1[2] - co2[2])


    def has_index(self, i, verts):
        
        for v in verts:
            if v[0] == i:
                return v
            
        return (-1, None)
    
    def replace_all(self, verts_matches, faces_matches, data):
        
        if self.sort_verts:
            self.replace_in_vertices(verts_matches, data)
            self.replace_in_shape_keys(verts_matches, data)
            #Wrrrrrraaaaa!
            #self.replace_in_polygons(verts_matches, data)
            self.replace_in_edges(verts_matches, data)
            self.replace_in_loops(verts_matches, data)
        
        if self.sort_faces:
            self.replace_faces(faces_matches, data)
    
    def replace_in_vertices(self, verts_matches, data):
        verts = []
        for v in data.vertices:
            verts.append((v.co[:], v.select))
        
        for d in range(len(data.vertices)):
            #print("v old: " + str(d) + ", new: " + str(verts_matches[d]))
            
            data.vertices[verts_matches[d]].co = verts[d][0]
            data.vertices[verts_matches[d]].select = verts[d][1]
            
    def replace_in_shape_keys(self, verts_matches, data):
        
        if not hasattr(data, 'shape_keys'):
            return
        
        if data.shape_keys is None:
            return
        
        for key in data.shape_keys.key_blocks:                    
            verts = []
            for v in key.data:
                verts.append(v.co[:])
            
            for d in range(len(key.data)):
                key.data[verts_matches[d]].co = verts[d]
    
    def replace_in_edges(self, verts_matches, data):
        for d in range(len(data.edges)):
            for i in range(len(data.edges[d].vertices)):
                vi = data.edges[d].vertices[i]
                data.edges[d].vertices[i] = verts_matches[vi]                            
                                                
    def replace_in_loops(self, verts_matches, data):
        for d in range(len(data.loops)):
            vi = data.loops[d].vertex_index
            data.loops[d].vertex_index = verts_matches[vi]                
            
    
    def slide_loops(self, steps, data):
        #test
        for pi in range(len(data.polygons)):
            
            p = data.polygons[pi]
            
            r_vertex_indexes = [-1] * p.loop_total
            r_edge_indexes = [-1] * p.loop_total
            
            for i in range(p.loop_total):
                r_vertex_indexes[i] = data.loops[p.loop_start + i].vertex_index
                r_edge_indexes[i] = data.loops[p.loop_start + i].edge_index 
            
            f_li = steps[pi]
            t_li = p.loop_start
            
            for i in range(p.loop_total):
                    
                if (f_li >= p.loop_total):
                    f_li -= p.loop_total
                    
                if (t_li >= p.loop_start + p.loop_total):
                    t_li -= p.loop_total
                
                data.loops[t_li].vertex_index = r_vertex_indexes[f_li]
                data.loops[t_li].edge_index = r_edge_indexes[f_li]
                
                f_li += 1                                    
                t_li += 1
          
    def replace_faces(self, polygons_matches, data):        
        
        polys_copy = []
        for p in data.polygons:
            polys_copy.append(self.copy_poly(p))
        
        for d in range(len(data.polygons)):
            
            pi = polygons_matches[d]
            #print("old: " + str(d) + ", new: " + str(pi))         
            data.polygons[pi].material_index = polys_copy[d][0]
            data.polygons[pi].loop_start = polys_copy[d][1]
            data.polygons[pi].loop_total = polys_copy[d][2]
            data.polygons[pi].select = polys_copy[d][3]
            
    def copy_poly(self, p):
        return (p.material_index, p.loop_start, p.loop_total, p.select)    
        

def operator_poll(context):
    if context.edit_object is None:
        return False            
    
    return True
    
