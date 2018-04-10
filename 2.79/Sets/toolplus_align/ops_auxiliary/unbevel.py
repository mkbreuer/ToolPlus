# ### BEGIN GPL LICENSE BLOCK ###
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# #### END GPL LICENSE BLOCK ####

# This addon is included as a part of "Tea's Ultimate Toolkit" for blender.
# All rights reserved by author.

bl_info = {
    "name"          : "UnBevel",
    "author"        : "TeaCrab",
    "blender"       : (2, 7, 8),
    "description"   : "Unbevel in mesh mode, using Ringed-path selection pattern.",
    "location"      : "3D View, Mesh specials menu [W]",
    "category"      : "T+ Auxiliary",
    }

import bpy, bmesh
from mathutils import geometry
from math import pi

def angle_2vec3(X, Y):
    return X.angle(Y) % pi

def getIntersection(x, y):
    BMEdge = bmesh.types.BMEdge
    x1, x2 = (x.verts[0].co, x.verts[1].co) if isinstance(x, BMEdge) else (x[0], x[1])
    y1, y2 = (y.verts[0].co, y.verts[1].co) if isinstance(y, BMEdge) else (y[0], y[1])
    if angle_2vec3(x1-x2, y1-y2) < 0.002:
        return None
    else:
        vec = geometry.intersect_line_line(x1, x2, y1, y2)
        return (vec[0] + vec[1]) / 2

def is_edge_end_of_selection(edge, selected):
    for v in edge.verts:
        temp = [e for e in v.link_edges if e in selected]
        if len(temp) == 1:
            return True
    return False

def get_current_edge_loop(edge, selected):
    loop = [edge]
    v_checked = []
    v_next = None
    for v in edge.verts:
        possible = [e for e in v.link_edges if e in selected and e not in loop]
        n = len(possible)
        if n == 0:
            v_checked.append(v)
            v_next = edge.other_vert(v)
            break
        elif n == 1:
            v_checked.append(edge.other_vert(v))
            v_next = v
            break
        else:
            print("____X:")
            return None
    
    while v_next not in v_checked:
        possible = [e for e in v_next.link_edges if e in selected and e not in loop]
        n = len(possible)
        if n == 1:
            loop.append(possible[0])
            v_checked.append(v_next)
            v_next = possible[0].other_vert(v_next)
        elif n > 1:
            print("____Y:")
            return None
        else:
            return loop
    return loop

def get_edge_rings(selected_edges):
    edge_rings = [[],]
    context_edges = [e for e in selected_edges if is_edge_end_of_selection(e, selected_edges)]
    if len(context_edges) == 0:
        return None

    for edge in context_edges:
        if edge in [e for ring in edge_rings for e in ring]:
            continue
        else:
            loop = get_current_edge_loop(edge, selected_edges)
            if loop != None:
                if edge_rings[-1] == []:
                    edge_rings[-1] = loop
                else:
                    edge_rings.append(loop)
            else:
                print("____ZZ:")
                return None
    return edge_rings


#class VIEW3D_TP_UnBevel(bpy.types.Panel):
#    bl_category = "Retopo"
#    bl_context = 'mesh_edit'
#    bl_idname = "VIEW3D_TP_UnBevel"
#    bl_label = "UnBevel"
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'TOOLS'
#    #bl_region_type = 'UI'
#    bl_options = {'DEFAULT_CLOSED'}

#    @classmethod
#    def poll(cls, context):
#        isModelingMode = not (
#        context.sculpt_object or 
#        context.vertex_paint_object
#        or context.weight_paint_object
#        or context.image_paint_object)
#        return (isModelingMode)
#    
#    def draw(self, context):
#        layout = self.layout.column_flow(1)  
#        layout.operator_context = 'INVOKE_REGION_WIN'
#        #layout.operator_context = 'INVOKE_AREA'

#        box = layout.box().column(1)  
#       
#        row = box.column(1)
#        row.operator("mesh.tca_unbevel")


class TCA_UnBevel(bpy.types.Operator):
    bl_idname = 'tp_ops.unbevel'
    bl_label = 'Unbevel > Ringed Path'
    bl_description = ''
    bl_options = {'REGISTER', 'UNDO'}

    keep_support = bpy.props.BoolProperty(
        name = "Keep Supporting Edges",
        description = "Keep the supporting edges that were used to be the boundaries of the bevel.",
        default = False)

    @classmethod
    def poll(self, context):
        return context.mode == 'EDIT_MESH'
 
    def execute(self, context):
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        edges = [e for e in bm.edges if e.select]
        verts = [v for v in bm.verts if v.select]
        edge_rings = get_edge_rings(edges)

        intersection_error = 0
        if edge_rings != None:
            for ring in edge_rings:
                edge_pair = [e for e in ring if is_edge_end_of_selection(e, edges)]
                if self.keep_support:
                    edge_pair_verts = [v for e in edge_pair for v in e.verts]
                    other_verts = [v for e in ring for v in e.verts if v not in edge_pair_verts]
                else:
                    other_edges = [e for e in ring if e not in edge_pair]
                    other_verts = [v for e in other_edges for v in e.verts]
                intersection = getIntersection(edge_pair[0], edge_pair[1])
                if intersection == None:
                    intersection_error += 1
                else:
                    for v in other_verts:
                        v.co = intersection
            bmesh.ops.remove_doubles(bm, verts = verts, dist = 0)
            bmesh.update_edit_mesh(me, True)
            if intersection_error > 0:
                msg = "Unbevel can't be done on a path with parallel ends. {} bevels can't be undone.".format(intersection_error)
                self.report({'ERROR'}, msg)
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Unrecognizable selection pattern.")
            return {'CANCELLED'}
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "keep_support", toggle = True)




def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
