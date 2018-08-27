# -*- coding: utf-8 -*-   

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
    "name": "1D_Scripts",                     
    "author": "Alexander Nedovizin, Paul Kotelevets aka 1D_Inc (concept design), Nikitron",
    "version": (0, 8, 20),
    "blender": (2, 7, 5),
    "location": "View3D > Toolbar",
    "category": "ToolPlus"
}  

# http://dl.dropboxusercontent.com/u/59609328/Blender-Rus/1D_Scripts.py

import bpy,bmesh, mathutils, math
from mathutils import Vector, Matrix
from mathutils.geometry import intersect_line_plane, intersect_point_line, intersect_line_line
from math import sin, cos, pi, sqrt, degrees, tan, radians
import os, urllib
from bpy.props import (BoolProperty, FloatProperty, StringProperty, EnumProperty, IntProperty, CollectionProperty)
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.types import Operator
import time 



#Align
def check_lukap(bm):
    if hasattr(bm.verts, "ensure_lookup_table"): 
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()
        bm.faces.ensure_lookup_table()

#Align
def find_index_of_selected_vertex(mesh):  
    selected_verts = [i.index for i in mesh.vertices if i.select]  
    verts_selected = len(selected_verts)  
    if verts_selected <1:  
        return None                            
    else:  
        return selected_verts  
    
#Align
def find_connected_verts_simple(me, found_index):  
    edges = me.edges  
    connecting_edges = [i for i in edges if found_index in i.vertices[:] and \
        me.vertices[i.vertices[0]].select and me.vertices[i.vertices[1]].select]  
    if len(connecting_edges) == 0: 
        return []
    else:  
        connected_verts = []  
        for edge in connecting_edges:  
            cvert = set(edge.vertices[:])   
            cvert.remove(found_index)                            
            vert = cvert.pop()
            connected_verts.append(vert)  
        return connected_verts  


def find_connected_verts(me, found_index, not_list):  
    edges = me.edges  
    connecting_edges = [i for i in edges if found_index in i.vertices[:]]  
    if len(connecting_edges) == 0: 
        return []
    else:  
        connected_verts = []  
        for edge in connecting_edges:  
            cvert = set(edge.vertices[:])   
            cvert.remove(found_index)                            
            vert = cvert.pop()
            if not (vert in not_list) and me.vertices[vert].select:
                connected_verts.append(vert)  
        return connected_verts  
    
#Align    
def find_all_connected_verts(me, active_v, not_list=[], step=0):
    vlist = [active_v]
    not_list.append(active_v)
    step+=1
    list_v_1 = find_connected_verts(me, active_v, not_list)              

    for v in list_v_1:
        list_v_2 = find_all_connected_verts(me, v, not_list, step) 
        vlist += list_v_2
    return vlist  


#Align
def find_dupes_verts(context, radius):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    
    ob = context.active_object
    mesh = ob.data
    
    bpy.ops.mesh.select_all(action='DESELECT')
    
    bm = bmesh.new()
    bm.from_mesh(mesh)    

    doubs = bmesh.ops.find_doubles(bm, verts=bm.verts, dist=radius)
    
    bpy.ops.object.mode_set(mode='OBJECT') 
    double_verts = doubs['targetmap']
    if len(double_verts.keys()) > 1:
        for k, v in double_verts.items():
            mesh.vertices[v.index].select=True

    mesh.update()   
    bm.free()

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(use_expand=True, type='VERT')      
    context.tool_settings.mesh_select_mode = (True, False, False)
    return len(double_verts)



#Align
def bm_vert_active_get(bm):
    for elem in reversed(bm.select_history):
        if isinstance(elem, (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)):
            return elem.index, str(elem)[3:4]     
    return None, None



#Align
def to_store_coner(obj_name, bm, mode):
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    old_name_c = config.object_name_store_c
    old_coner1 = config.coner_edge1_store 
    old_coner2 = config.coner_edge2_store 
    
    def check():
        if mode=='EDIT_MESH' and \
          (old_name_c != config.object_name_store_c or \
           old_coner1 != config.coner_edge1_store or \
           old_coner2 != config.coner_edge2_store):
           config.flip_match = False
    
    if active_edge != None and el=='E':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_c = obj_name
        config.coner_edge1_store = active_edge
        verts = bm.edges[active_edge].verts
        v0 = verts[0].index
        v1 = verts[1].index
        edges_idx = [i.index for i in mesh.edges \
            if (v1 in i.vertices[:] or v0 in i.vertices[:])and i.select \
            and i.index!=active_edge] 
        if edges_idx:
            config.coner_edge2_store = edges_idx[0]
            check()
            return True
        
    if active_edge != None and el=='V':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_c = obj_name
        
        v2_l = find_all_connected_verts(mesh, active_edge,[],0)
        control_vs = find_connected_verts_simple(mesh, active_edge)
        if len(v2_l)>2 and len(control_vs)==1:
            v1 = v2_l.pop(1)
            edges_idx = []
            for v2 in v2_l[:2]:
                edges_idx.extend([i.index for i in mesh.edges \
                    if v1 in i.vertices[:] and v2 in i.vertices[:]] )
            
            if len(edges_idx)>1:
                config.coner_edge1_store = edges_idx[0]
                config.coner_edge2_store = edges_idx[1]
                check()
                return True
    
    check()
    config.object_name_store_c = ''
    config.coner_edge1_store = -1
    config.coner_edge2_store = -1
    if mode =='EDIT_MESH':
        config.flip_match = False   
        print_error('Two edges is not detected')
        print('Error: align 05')
    return False


#Align
def to_store_vert(obj_name, bm):
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    old_edge1 = config.active_edge1_store
    old_edge2 = config.active_edge2_store
    old_name_v = config.object_name_store_v
    
    def check():
        if old_name_v != config.object_name_store_v or \
           old_edge1 != config.active_edge1_store or \
           old_edge2 != config.active_edge2_store:
           config.flip_match = False    
    
    if active_edge != None and el=='E':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_v = obj_name
        config.active_edge1_store = active_edge
        verts = bm.edges[active_edge].verts
        v0 = verts[0].index
        v1 = verts[1].index
        edges_idx = [i.index for i in mesh.edges \
            if (v1 in i.vertices[:] or v0 in i.vertices[:])and i.select \
            and i.index!=active_edge] 
        if edges_idx:
            config.active_edge2_store = edges_idx[0]
            check()
            return True
        
    if active_edge != None and el=='V':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_v = obj_name
        
        v2_l = find_all_connected_verts(mesh, active_edge,[],0)
        control_vs = find_connected_verts_simple(mesh, active_edge)
        if len(v2_l)>2 and len(control_vs)==1:
            v1 = v2_l.pop(1)
            edges_idx = []
            for v2 in v2_l[:2]:
                edges_idx.extend([i.index for i in mesh.edges \
                    if v1 in i.vertices[:] and v2 in i.vertices[:]] )
                
            if len(edges_idx)>1:
                config.active_edge1_store = edges_idx[0]
                config.active_edge2_store = edges_idx[1]
                check()
                return True
    
    check()
    config.object_name_store_v = ''
    config.active_edge1_store = -1
    config.active_edge2_store = -1
    config.flip_match = False   
    print_error('Side is undefined')
    print('Error: 3dmatch 10')
    return False
    
    
#Align
def to_store(obj_name, bm):
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    if active_edge != None and el=='E':
        config.object_name_store = obj_name
        config.edge_idx_store = active_edge
        verts = bm.edges[active_edge].verts
        config.vec_store = (verts[1].co - verts[0].co) * \
        bpy.data.objects[obj_name].matrix_world.to_3x3().transposed()
        return True
    
    if active_edge != None and el=='V':
        obj_act = bpy.context.active_object
        mesh = obj_act.data
        v2_l = find_index_of_selected_vertex(mesh)
        if len(v2_l)==2:
            v1 = active_edge
            v2_l.pop(v2_l.index(v1))
            v2 = v2_l[0]
            edges_idx = [i.index for i in mesh.edges \
                if v1 in i.vertices[:] and v2 in i.vertices[:]] 
                
            if edges_idx:
                config.edge_idx_store = edges_idx[0]

            config.object_name_store = obj_name
            config.vec_store = (mesh.vertices[v1].co - mesh.vertices[v2].co) * \
                bpy.data.objects[obj_name].matrix_world.to_3x3().transposed()
            return True
                
    config.object_name_store = ''
    config.edge_idx_store = -1
    config.vec_store = mathutils.Vector((0,0,0))
    print_error('Active edge is not detected')
    print('Error: align 02')
    return False



#Align
def sel_radius_verts(context, radius):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    
    ob = context.active_object
    mesh = ob.data
    
    points = [v.co for v in mesh.vertices if v.select]
    if not points:
        print_error2('No selected vertices', 'sel_radius_verts 01')
        return 0
    
    size = len(mesh.vertices) 
    kd = mathutils.kdtree.KDTree(size) 
    for i, p in enumerate(mesh.vertices):
        kd.insert(p.co, i) 

    kd.balance()

    arr_idx = []
    for point in points:
        for (co, index, dist) in kd.find_range(point, radius):
            arr_idx.append(index)
            
    bpy.ops.object.mode_set(mode='OBJECT')
    for vi in arr_idx:
        mesh.vertices[vi].select=True
        
    bpy.ops.object.mode_set(mode='EDIT')
    arr_idx=set(arr_idx)
    return len(arr_idx)-len(points)


#Align
def select_mesh_rot(me, matrix):
    verts = [v for v in me.verts if v.select==True]
    for v in verts:
        v.co = v.co*matrix


#Align
def store_align(vts='edge', mode='EDIT_MESH'):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    
    obj = bpy.context.active_object
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)  
    result = True
    check_lukap(bm)
    
    if vts=='vert':
        result = to_store_vert(obj.name, bm)
    elif vts=='edge':
        result = to_store(obj.name, bm)
    else:
        # vts=='coner':
        result = to_store_coner(obj.name, bm, mode)
    
    bm.free()   
    return result


#Align
def getNormalPlane(vecs, mat):
    if len(vecs)<3:
        return None
    
    out_ = []
    vec_c = mathutils.Vector((0,0,0))
    for v in vecs:
        vec  = v*mat
        out_.append(vec)
        vec_c+=vec
    
    vec_c = vec_c / len(vecs) 
                                       
    v = out_[1]-out_[0]
    w = out_[2]-out_[0]
    A = v.y*w.z - v.z*w.y
    B = -v.x*w.z + v.z*w.x
    C = v.x*w.y - v.y*w.x
    D = -out_[0].x*A - out_[0].y*B - out_[0].z*C   
    
    norm = mathutils.Vector((A,B,C)).normalized()
    return norm



#Align
def match3D(flip = False):
    mode_ = bpy.context.mode
    store_align('coner', mode_)
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store_v == '' or \
        config.object_name_store_v not in bpy.context.scene.objects or \
        config.active_edge1_store < 0 or config.active_edge2_store < 0:
            print_error('Stored Vertex is required')
            print('Error: 3dmatch 01')
            return False
    
    if config.object_name_store_c == '':
        if mode_ =='EDIT_MESH':
            print_error('Not specified object')
            print('Error: 3dmatch 02')
            return False
        else:
            config.object_name_store_c = bpy.context.active_object.name
    
    if config.coner_edge1_store == -1 or \
       config.coner_edge2_store == -1:
        if mode_ =='EDIT_MESH':
            #print_error('Not specified object')
            print_error('Stored edges is required')
            print('Error: 3dmatch 03')
            return False
    
    obj_A =  bpy.data.objects[config.object_name_store_v]
    obj_B =  bpy.data.objects[config.object_name_store_c]
    ve1 = obj_A.data.edges[config.active_edge1_store]
    ve2 = obj_A.data.edges[config.active_edge2_store]
    e1 = obj_B.data.edges[config.coner_edge1_store]
    e2 = obj_B.data.edges[config.coner_edge2_store]
    
    # получаем ещё две вершины. Иначе - реджект
    connect_vs = []
    connect_vs.extend(ve1.vertices[:])
    connect_vs.extend(ve2.vertices[:])
    v1 = -1
    for v in connect_vs:
        if connect_vs.count(v)>1:
            v1 = obj_A.data.vertices[v]
            connect_vs.pop(connect_vs.index(v))
            connect_vs.pop(connect_vs.index(v))
            break
    
    if v1 == -1:
        print_error('Active vertex of object_A must have two edges')
        print('Error: 3dmatch 04')
        return False
    
    v2 = obj_A.data.vertices[connect_vs[0]]
    v3 = obj_A.data.vertices[connect_vs[1]]
    
    # вычислить нормаль объекта Б
    #if mode_ =='EDIT_MESH':
    if config.coner_edge1_store != -1:
        lws = list(e1.vertices[:]+e2.vertices[:])
        for l in lws:
            if lws.count(l)>1: 
                lws.pop(lws.index(l))
                w1 = obj_B.data.vertices[lws.pop(lws.index(l))]
        
        w3 = obj_B.data.vertices[lws.pop()]
        w2 = obj_B.data.vertices[lws.pop()]
    else:
        w1,w2,w3 = 0,0,0
    
    mat_w = obj_B.matrix_world.copy()
    k_x = 1
    if mode_ !='EDIT_MESH':
        if config.flip_match: k_x = -1
        else: k_x = 1
        
    if flip!=config.flip_match:
        config.flip_match = flip
        if mode_ =='EDIT_MESH':
            bpy.ops.object.mode_set(mode='EDIT') 
            normal_B = getNormalPlane([w1.co, w2.co, w3.co], mathutils.Matrix())
            normal_z = mathutils.Vector((0,0,1))
            mat_rot_norm = normal_B.rotation_difference(normal_z).to_matrix().to_4x4()
           
            verts = [v for v in obj_B.data.vertices if v.select==True]
            for v in verts:
                v.co = mat_rot_norm * v.co
            
            bpy.ops.transform.resize(value=(1,1,-1), constraint_axis=(False, False, True))
        else:
            k_x *= -1
    
    normal_x = mathutils.Vector((1,0,0)) * k_x
        
    bpy.ops.object.mode_set(mode='EDIT') 
    bpy.ops.object.mode_set(mode='OBJECT')    
    edge_idx = [i.index for i in obj_A.data.edges \
        if v1 in i.vertices[:] and v2 in i.vertices[:]] 
            
    vecA= (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
    
    if mode_ =='EDIT_MESH':
        v1A = obj_A.matrix_world * v1.co 
        w1B = obj_B.matrix_world * w1.co 

        vecB = (w2.co - w1.co)
        mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()
        
        # rotation1
        bpy.ops.object.mode_set(mode='EDIT') 
        bpy.ops.object.mode_set(mode='OBJECT')
        
        normal_A = getNormalPlane([v1.co, v2.co, v3.co], mathutils.Matrix())
        normal_A = normal_A * obj_A.matrix_world.to_3x3().transposed()
        normal_B = getNormalPlane([w1.co, w2.co, w3.co], mathutils.Matrix())
        mat_rot2 = normal_B.rotation_difference(normal_A).to_matrix().to_4x4()
        
        verts = [v for v in obj_B.data.vertices if v.select==True]
        for v in verts:
            v.co = mat_rot2 * v.co 
        
        
        bpy.ops.object.mode_set(mode='EDIT') 
        bpy.ops.object.mode_set(mode='OBJECT')
        
        vecA= (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
        vecB = (w2.co - w1.co)
        mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()
        verts = [v for v in obj_B.data.vertices if v.select==True]
        for v in verts:
            v.co = mat_rot * v.co
        
        
        # invert rotation
        bpy.ops.object.mode_set(mode='EDIT') 
        bpy.ops.object.mode_set(mode='OBJECT')
        
        vec1 = mathutils.Vector((0,0,1))
        vec2 = obj_B.matrix_world * vec1
        mat_rot2 = vec1.rotation_difference(vec2).to_matrix().to_4x4()
        mat_tmp = obj_B.matrix_world.copy()
        
        mat_tmp[0][3]=0
        mat_tmp[1][3]=0
        mat_tmp[2][3]=0
        mat_inv = mat_tmp.inverted()
        
        verts = [v for v in obj_B.data.vertices if v.select==True]
        for v in verts:
            v.co = mat_inv * v.co
        
        # location
        bpy.ops.object.mode_set(mode='EDIT') 
        bpy.ops.object.mode_set(mode='OBJECT')
        
        w1B = obj_B.matrix_world * w1.co
        mat_loc = mathutils.Matrix.Translation(v1A-w1B)
        vec_l = mat_inv * (v1A-w1B)
        
        mat_tp = obj_B.matrix_world
        vec_loc = mathutils.Vector((mat_tp[0][3],mat_tp[1][3],mat_tp[2][3]))
        
        verts = [v for v in obj_B.data.vertices if v.select==True]
        for v in verts:
            v.co = v.co + vec_l 
            
        bpy.ops.object.mode_set(mode='EDIT') 
        
    else:
        if config.coner_edge1_store == -1:
            v1A = obj_A.matrix_world * v1.co
            normal_A = getNormalPlane([v1.co, v2.co, v3.co], mathutils.Matrix())
            normal_A = normal_A * obj_A.matrix_world.to_3x3().transposed()
            normal_z = mathutils.Vector((0,0,1))
            mat_rot1 = normal_z.rotation_difference(normal_A).to_matrix().to_4x4()
            
            vecA = (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
            vecB = mat_rot1 * normal_x
            mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()
            
            obj_B.matrix_world = mat_rot * mat_rot1
            vec_l = v1A-obj_B.location
            obj_B.location = obj_B.location+vec_l
            
        else:
            v1A = obj_A.matrix_world * v1.co
            w1B = obj_B.matrix_world * w1.co 
            vecB = (w2.co - w1.co) * obj_B.matrix_world.to_3x3().transposed()
            
            normal_A = getNormalPlane([v1.co, v2.co, v3.co], mathutils.Matrix())
            normal_A = normal_A * obj_A.matrix_world.to_3x3().transposed()
            normal_B = getNormalPlane([w1.co, w2.co, w3.co], mathutils.Matrix())
            normal_B = normal_B * obj_B.matrix_world.to_3x3().transposed()
            mat_rot1 = normal_B.rotation_difference(normal_A).to_matrix().to_4x4()
            
            vecA = (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
            vecB = mat_rot1 * vecB
            mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()
            
            obj_B.matrix_world = mat_rot * mat_rot1
            w1B = obj_B.matrix_world * w1.co
            vec_l = v1A-w1B
            obj_B.location = obj_B.location+vec_l
    return True


#Align
def mirrorside():
    mode_ = bpy.context.mode
    bpy.ops.object.mode_set(mode='OBJECT')  
    bpy.ops.object.mode_set(mode='EDIT')  
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store_v == '' or \
       config.active_edge1_store < 0 or config.active_edge2_store < 0:
        print_error2('Stored Vertex is required','mirrorside 01')
        return False
    
    obj_A =  bpy.data.objects[config.object_name_store_v]
    ve1 = obj_A.data.edges[config.active_edge1_store]
    ve2 = obj_A.data.edges[config.active_edge2_store]
    
    # получаем ещё две вершины. Иначе - реджект
    connect_vs = []
    connect_vs.extend(ve1.vertices[:])
    connect_vs.extend(ve2.vertices[:])
    v1 = -1
    for v in connect_vs:
        if connect_vs.count(v)>1:
            v1 = obj_A.matrix_world * obj_A.data.vertices[v].co
            connect_vs.pop(connect_vs.index(v))
            connect_vs.pop(connect_vs.index(v))
            break
    
    if v1 == -1:
        print_error2('Active vertex of object_A must have two edges', 'mirrorside 04')
        return False
    
    v2 = obj_A.matrix_world * obj_A.data.vertices[connect_vs[0]].co
    v3 = obj_A.matrix_world * obj_A.data.vertices[connect_vs[1]].co
    
    obj_B = bpy.context.scene.objects.active
    normal_B = getNormalPlane([v1, v2, v3], mathutils.Matrix())
    if mode_ =='EDIT_MESH':
        bpy.ops.object.mode_set(mode='EDIT') 
        ref_vts = [v for v in obj_B.data.vertices if v.select==True]
        verts = []
        v_idx_B = []
        for v in ref_vts:
            verts.append(v.co)
            v_idx_B.append(v.index)
        
        bpy.ops.object.mode_set(mode='OBJECT')  
        bm = bmesh.new()
        bm.from_mesh(obj_B.data) 
        check_lukap(bm)
        
        vts = []
        mat_inv = obj_B.matrix_world.inverted()
        for pt_a_ in verts:
            pt_a = obj_B.matrix_world * pt_a_
            pt_b = normal_B + pt_a
            cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, v1, normal_B)
            
            d_vec = cross_pt-pt_a
            pt_c = cross_pt + d_vec
            v_new = bm.verts.new(mat_inv*pt_c)
            vts.append(v_new)
        
        bm.verts.index_update() 
        check_lukap(bm)
        vts_ = [v.index for v in vts]
        ref_edges = [(e.vertices[0], e.vertices[1]) for e in obj_B.data.edges if e.select==True]
        for e in ref_edges:
            ev0 = v_idx_B.index(e[0])
            ev1 = v_idx_B.index(e[1])
            e = (bm.verts[vts_[ev0]], bm.verts[vts_[ev1]])
            bm.edges.new(e)
        check_lukap(bm)
        
        ref_faces = [(v for v in f.vertices) for f in obj_B.data.polygons if f.select==True]
        for f in ref_faces:
            f_B = []
            for v in f:
                fv = v_idx_B.index(v)
                f_B.append(bm.verts[vts_[fv]])
                
            bm.faces.new(tuple(f_B))
        
        bm.to_mesh(obj_B.data)       
        bm.free() 
        bpy.ops.object.mode_set(mode='EDIT')
        
    elif mode_ =='OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(obj_B.data) 
        check_lukap(bm)
        
        ref_vtert = bm.verts
        mat_inv = obj_B.matrix_world.inverted()
        for pt_a_ in ref_vtert:
            pt_a = obj_B.matrix_world * pt_a_.co
            pt_b = normal_B + pt_a
            cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, v1, normal_B)
            
            d_vec = cross_pt-pt_a
            pt_c = cross_pt + d_vec
            ref_vtert[pt_a_.index].co = mat_inv*pt_c
        
        name = obj_B.name+'copy'
        me = bpy.data.meshes.new(name+'_Mesh')
        obj_C = bpy.data.objects.new(name, me)
        # Привязка объекта к сцене
        bpy.context.scene.objects.link(obj_C)
        
        bm.to_mesh(me)       
        me.update()   
        bm.free() 
    return True


#Align
def main_align_object(axe='X',project='XY'):
    obj_res = bpy.context.active_object
    if obj_res.type=='MESH':
        bpy.ops.object.mode_set(mode='EDIT') 
        bpy.ops.object.mode_set(mode='OBJECT')
    
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: align_object 01')
        return False
    
    obj = bpy.data.objects[config.object_name_store]
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)  
    check_lukap(bm)
    
    # Найдём диагональ Store
    edge_idx = config.edge_idx_store
    verts_edge_store = bm.edges[edge_idx].verts
    vec_diag_store = verts_edge_store[1].co - verts_edge_store[0].co
    
    # Развернем объект
    dict_axe = {'X':(1.0,0.0,0.0), 'Y':(0.0,1.0,0.0), 'Z':(0.0,0.0,1.0)}
    aa_vec = dict_axe[axe]
    
    aa = mathutils.Vector(aa_vec) 
    bb = vec_diag_store.normalized()
    
    planes = set(project)
    if 'X' not in planes:
        aa.x=0
        bb.x=0
    if 'Y' not in planes:
        aa.y=0
        bb.y=0
    if 'Z' not in planes:
        aa.z=0
        bb.z=0        

    vec = aa
    q_rot = vec.rotation_difference(bb).to_matrix().to_4x4()
    obj_res.matrix_world *= q_rot
    for obj in bpy.context.scene.objects:
        if obj.select:
            if obj.name!=obj_res.name:
                orig_tmp = obj_res.location-obj.location
                mat_loc = mathutils.Matrix.Translation(orig_tmp)
                mat_loc2 = mathutils.Matrix.Translation(-orig_tmp)
        
                obj.matrix_world *= mat_loc*q_rot*mat_loc2
    return True
    
  

#Align
def main_align():
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT') 
    
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: align 01')
        return False
    
    obj = bpy.data.objects[config.object_name_store]
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)  
    check_lukap(bm)
    
    # Найдём диагональ Store
    edge_idx = config.edge_idx_store
    verts_edge_store = bm.edges[edge_idx].verts
    vec_diag_store = verts_edge_store[1].co - verts_edge_store[0].co
    
    # Получим выделенное ребро
    obj_res = bpy.context.active_object
    mesh_act = obj_res.data
    bm_act = bmesh.new()
    bm_act.from_mesh(mesh_act)  
    check_lukap(bm_act)
    
    edge_idx_act, el = bm_vert_active_get(bm_act)
    if edge_idx_act == None:
        print_error('Selection with active edge is required')
        print('Error: align 03')
        return False
    
    d_pos = bpy.context.scene.cursor_location - obj_res.location
    if not config.align_dist_z:  
        for v in bm_act.verts:
            if v.select:
                v.co -= d_pos
        
    
    verts_edge_act = bm_act.edges[edge_idx_act].verts
    vec_diag_act = verts_edge_act[1].co - verts_edge_act[0].co
    
    # Сравниваем
    aa = vec_diag_act 
    if config.align_lock_z:
        aa.z = 0
    aa.normalized()
    
    bb = vec_diag_store
    if config.align_lock_z:
        bb.z = 0
    bb.normalized()
    q_rot = bb.rotation_difference(aa).to_matrix().to_4x4()
    
    select_mesh_rot(bm_act, q_rot)
    verts = [v for v in bm_act.verts if v.select==True]
    pos = (verts_edge_store[0].co + obj.location)\
        - (verts_edge_act[0].co + obj_res.location)
        
    if not config.align_dist_z:
        pos = mathutils.Vector((0,0,0)) #bpy.context.scene.cursor_location
    for v in verts:
        pos_z = v.co.z
        v.co = v.co + pos
        if config.align_lock_z:
            v.co.z = pos_z
    
    if not config.align_dist_z:    
        for v in bm_act.verts:
            if v.select:
                v.co += d_pos
            
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bm_act.to_mesh(mesh_act)
    bm_act.free()
    
    bm.free()
    
    bpy.ops.object.mode_set(mode='EDIT') 
    return True
        


#Align
def GetStoreVecLength():
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: offset 01')
        return False
    
    vec = mathutils.Vector(config.vec_store)
    return vec.length


#Align
def axe_select(self, context):
    axes = ['X','Y','Z']
    return [tuple(3 * [axe]) for axe in axes]

#Align
def project_select(self, context):
    projects = ['XY','XZ','YZ','XYZ']
    return [tuple(3 * [proj]) for proj in projects]


"""
class LayoutSSPanel(bpy.types.Panel):

    bl_label = "1D_Scripts"
    bl_idname = "Paul_Operator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = '1D'
    #bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}  
    
    bpy.types.Scene.AxesProperty = bpy.props.EnumProperty(items=axe_select)
    bpy.types.Scene.ProjectsProperty = bpy.props.EnumProperty(items=project_select)
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def draw(self, context):
        lt = bpy.context.window_manager.paul_manager
        
        layout = self.layout
        col = layout.column(align=True)
        
        split = col.split()
        if lt.display_align:
            split.prop(lt, "display_align", text="Aligner", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_align", text="Aligner", icon='RIGHTARROW')
            
        if lt.display_align and context.mode == 'EDIT_MESH':
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.align_operator", text = 'Store Edge').type_op = 1
            row = col_top.row(align=True)
            align_op = row.operator("mesh.align_operator", text = 'Align').type_op = 0
            row = col_top.row(align=True)
            row.prop(lt, 'align_dist_z', text = 'Superpose')
            row = col_top.row(align=True)
            row.prop(lt, 'align_lock_z', text = 'lock Z')

        if lt.display_align and context.mode == 'OBJECT':
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.align_operator", text = 'Store Edge').type_op = 1
            row = col_top.row(align=True)
            align_op = row.operator("mesh.align_operator", text = 'Align').type_op = 2
            row = col_top.row(align=True)
            row.prop(context.scene,'AxesProperty', text = 'Axis')
            row = col_top.row(align=True)
            row.prop(context.scene,'ProjectsProperty', text = 'Projection')
"""        


#Align
class DistVerticesOperator(bpy.types.Operator):
    """Volumetric vertices selection"""
    bl_idname = "mesh.dist_verts"
    bl_label = "Dist Vertices"
    bl_options = {'REGISTER', 'UNDO'} 
    
    type_op = bpy.props.IntProperty(name = 'type_op', default = 0, options = {'HIDDEN'})
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type=='MESH'
    
    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.type_op==0:
            result = find_dupes_verts(context, config.dist_verts)
            if result==0:
                self.report({'INFO'}, "nothing found") 
            else:
                self.report({'INFO'}, "found "+str(result)+" vertices") 
        elif self.type_op==1:
            result = sel_radius_verts(context, config.dist_verts)
            if result==0:
                self.report({'INFO'}, "nothing added") 
            else:
                self.report({'INFO'}, "added "+str(result)+" vertices") 
        else:
            result=False
        
        if result:
            return {'FINISHED'}  
        else:
            return {'CANCELLED'}



#Align
class AlignOperator(bpy.types.Operator):
    bl_idname = "mesh.align_operator"
    bl_label = "Align operator"
    bl_options = {'REGISTER', 'UNDO'} 
    
    type_op = bpy.props.IntProperty(name = 'type_op', default = 0, options = {'HIDDEN'})

    dist = bpy.props.FloatProperty(name='dist', precision=4)

    dist_x = bpy.props.FloatProperty(name='X', precision=4)
    dist_y = bpy.props.FloatProperty(name='Y', precision=4)
    dist_z = bpy.props.FloatProperty(name='Z', precision=4)
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type=='MESH'

    def execute(self, context):
        resfunc = False
        config = bpy.context.window_manager.paul_manager
        if self.type_op==1:
            resfunc = store_align()
            if not resfunc:
                return{'CANCELLED'}
            
            config.step_len = GetStoreVecLength()
            self.dist_x = Vector(config.vec_store).x
            self.dist_y = Vector(config.vec_store).y
            self.dist_z = Vector(config.vec_store).z
            self.report({'INFO'}, \
                'dist: '+str(round(config.step_len,4)))
        elif self.type_op==0:
            resfunc = main_align()
        elif self.type_op==2:
            scene = bpy.context.scene
            #for obj_a in bpy.context.selected_objects:
            #        bpy.context.scene.objects.active = obj_a
            resfunc = main_align_object(scene.AxesProperty, scene.ProjectsProperty)
        elif self.type_op==3:
            # Store Vert
            resfunc = store_align('vert')
        elif self.type_op==4:
            # Store Coner
            resfunc = store_align('coner') 
        elif self.type_op==5:
            # 3D Match
            resfunc = match3D(False)
        elif self.type_op==6:
            # 3d Match Flip
            resfunc = match3D(True)
        elif self.type_op==7:
            resfunc = mirrorside()
        
        if not resfunc:
            return{'CANCELLED'}
        
        self.dist = config.step_len
        return {'FINISHED'}




class paul_managerProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.paul_manager
    """

    #Align
    display_align = bpy.props.BoolProperty(name = 'display_align')
    edge_idx_store = bpy.props.IntProperty(name="edge_idx_store")   

    object_name_store = bpy.props.StringProperty(name="object_name_store") 
    object_name_store_v = bpy.props.StringProperty(name="object_name_store_v") 
    object_name_store_c = bpy.props.StringProperty(name="object_name_store_c") 

    #Align
    align_dist_z = bpy.props.BoolProperty(name = 'align_dist_z')
    align_lock_z = bpy.props.BoolProperty(name = 'align_lock_z')
    step_len = bpy.props.FloatProperty(name="step_len")

    vec_store = bpy.props.FloatVectorProperty(name="vec_store")

    coner_edge1_store = bpy.props.IntProperty(name="coner_edge1_store")
    coner_edge2_store = bpy.props.IntProperty(name="coner_edge2_store")

    active_edge1_store = bpy.props.IntProperty(name="active_edge1_store", default = -1)
    active_edge2_store = bpy.props.IntProperty(name="active_edge2_store", default = -1)


    flip_match = bpy.props.BoolProperty(name="flip_match")
    dist_verts = bpy.props.FloatProperty(name="Dist", default=0.02, precision=2, min=0)
 

    axis_forward_setting = EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )

    axis_up_setting = EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )
    


class MessageOperator(bpy.types.Operator):
    from bpy.props import StringProperty
    
    bl_idname = "error.message"
    bl_label = "Message"
    type = StringProperty()
    message = StringProperty()
 
    def execute(self, context):
        self.report({'INFO'}, self.message)
        print(self.message)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_popup(self, width=400, height=200)
 
    def draw(self, context):
        self.layout.label(self.message, icon='BLENDER')

def print_error(message):
    bpy.ops.error.message('INVOKE_DEFAULT', 
        type = "Message",
        message = message)   
        
def print_error2(message,code_error='None'):
    print('Error:'+code_error)
    bpy.ops.error.message('INVOKE_DEFAULT', 
        type = "Message",
        message = message)   



def register():

    bpy.utils.register_module(__name__)  

    bpy.types.WindowManager.paul_manager = bpy.props.PointerProperty(type = paul_managerProps) 

    bpy.context.window_manager.paul_manager.display_align = False
    bpy.context.window_manager.paul_manager.align_dist_z = True
    bpy.context.window_manager.paul_manager.align_lock_z = False
    bpy.context.window_manager.paul_manager.step_len = 1.0
    bpy.context.window_manager.paul_manager.edge_idx_store = -1

    bpy.context.window_manager.paul_manager.object_name_store = ''
    bpy.context.window_manager.paul_manager.object_name_store_c = ''
    bpy.context.window_manager.paul_manager.object_name_store_v = ''
    bpy.context.window_manager.paul_manager.active_edge1_store = -1
    bpy.context.window_manager.paul_manager.active_edge2_store = -1

    bpy.context.window_manager.paul_manager.coner_edge1_store = -1
    bpy.context.window_manager.paul_manager.coner_edge2_store = -1




    
def unregister():

    del bpy.types.WindowManager.paul_manager

    bpy.utils.unregister_module(__name__)   

if __name__ == "__main__":
    register()