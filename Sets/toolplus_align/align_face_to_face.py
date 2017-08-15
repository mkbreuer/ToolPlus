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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****

#bl_info = {
 #   "name": "Align by faces",
  #  "author": "Tom Rethaller",
   # "version": (0,2,2),
    #"blender": (2, 65, 0),
    #"description": "Align two objects by their active faces",
    #"category": ""}

import bpy
import math
from mathutils import Vector
from functools import reduce


def get_ortho(a,b,c):
    if c != 0.0 and -a != b:
        return [-b-c, a,a]
    else:
        return [c,c,-a-b]

def clamp(v,min,max):
    if v < min:
        return min
    if v > max:
        return max
    return v

def align_faces(from_obj, to_obj):
    fpolys = from_obj.data.polygons
    tpolys = to_obj.data.polygons
    fpoly = fpolys[fpolys.active]
    tpoly = tpolys[tpolys.active]
    
    to_obj.rotation_mode = 'QUATERNION'
    tnorm = to_obj.rotation_quaternion * tpoly.normal
    
    fnorm = fpoly.normal
    axis = fnorm.cross(tnorm)
    dot = fnorm.normalized().dot(tnorm.normalized())
    dot = clamp(dot, -1.0, 1.0)
    
    # Parallel faces need a new rotation vactor
    if axis.length < 1.0e-8:
        axis = Vector(get_ortho(fnorm.x, fnorm.y, fnorm.z))
        
    from_obj.rotation_mode = 'AXIS_ANGLE'
    from_obj.rotation_axis_angle = [math.acos(dot) + math.pi, axis[0],axis[1],axis[2]]
    bpy.context.scene.update()  
    
    # Move from_obj so that faces match
    fvertices = [from_obj.data.vertices[i].co for i in fpoly.vertices]
    tvertices = [to_obj.data.vertices[i].co for i in tpoly.vertices]
    
    fbary = from_obj.matrix_world * (reduce(Vector.__add__, fvertices) / len(fvertices))
    tbary = to_obj.matrix_world * (reduce(Vector.__add__, tvertices) / len(tvertices))
    
    from_obj.location = tbary - (fbary - from_obj.location)


class OBJECT_OT_AlignByFaces(bpy.types.Operator):
    """Align two objects by their highlighted active faces """
    bl_label = "Align by faces"
    bl_description= "Align two objects by their active faces"
    bl_idname = "object.align_by_faces"

    @classmethod
    def poll(cls, context):
        if not len(context.selected_objects) is 2:
            return False
        for obj in context.selected_objects:
            if obj.type != 'MESH':
                return False
        return True

    def execute(self, context):
        objs_to_move = [o for o in context.selected_objects if o != context.active_object]
        for o in objs_to_move:
        	align_faces(o, context.active_object)
        return {'FINISHED'}





