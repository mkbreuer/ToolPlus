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
    "name": "Curve Trim",
    "description": "Trims segment from selected point for Bezier Splines",
    "author": "jimflim",
    "version": (0, 1),
    "blender": (2, 75, 0),
    "category": "Add Curve",
    "location": "View3D > Tools > Curves",
    "warning": "",
    "wiki_url": "https://github.com/jimflim/blender-scripts"
}
"""

import bpy
from mathutils import Vector
from mathutils.geometry import intersect_line_line_2d, intersect_line_line, interpolate_bezier


PRECISION = 1.0e-5


def active_spline_id(shape_ob):
    '''
    returns integer of active spline
    '''
    return [i for i,s in enumerate(shape_ob.data.splines) if s == shape_ob.data.splines.active][0]


def sel_point_id(spline_ob):
    '''
    > spline_ob:     bezier spline object
    < returns integer of selected points
    '''
    return [i for i,bp in enumerate(spline_ob.bezier_points) if bp.select_control_point]


def interpolate_all_segments(spline_ob):
    '''
    > spline_ob:     bezier spline object
    < returns interpolated splinepoints
    '''
    point_range = len(spline_ob.bezier_points)
    pl = []

    for i in range (0, point_range-1+spline_ob.use_cyclic_u):
        if len(pl) > 0:
            pl.pop()
        seg = (interpolate_bezier(spline_ob.bezier_points[i%point_range].co,
                                  spline_ob.bezier_points[i%point_range].handle_right,
                                  spline_ob.bezier_points[(i+1)%point_range].handle_left,
                                  spline_ob.bezier_points[(i+1)%point_range].co,
                                  spline_ob.resolution_u+1))
        pl += seg
    return pl


def interpolate_spline(spline_ob):
    '''
    > spline_ob:     bezier spline object
    < returns segments as lists of vectors
    '''
    point_range = len(spline_ob.bezier_points)
    segments = []

    for i in range (0, point_range-1+spline_ob.use_cyclic_u):
        segments.append(interpolate_bezier(spline_ob.bezier_points[i%point_range].co,
                                           spline_ob.bezier_points[i%point_range].handle_right,
                                           spline_ob.bezier_points[(i+1)%point_range].handle_left,
                                           spline_ob.bezier_points[(i+1)%point_range].co,
                                           spline_ob.resolution_u+1))
    return segments


def linear_spline_list(shape_ob):
    '''
    > shape_ob:     bezier shape object
    < returns list of linear interpolated splinepoints
    '''
    return [interpolate_spline(spl) for spl in shape_ob.data.splines]


def spline_X_shape(shape_ob, spl_index):
    '''
    > shape_ob:     bezier shape object
    > spl_index:    spline number
    < returns list of intersections, occuring segment
    '''

    shape_list = linear_spline_list(shape_ob)
    sl = interpolate_all_segments(shape_ob.data.splines[spl_index])
    cross = []

    # check for self-intersections first
    sl_length = 0
    for i in range(len(sl)-1):
        for j in range(i+2, len(sl)-1):
            x = intersect_line_line_2d(sl[i], sl[i+1], sl[j], sl[j+1])
            if x != None:
                cross.append([x ,i // shape_ob.data.splines[spl_index].resolution_u, sl_length + (x.to_3d()-sl[i]).length])
        sl_length += (sl[i+1] - sl[i]).length

    # then empty active spline from shapelist
    shape_list[spl_index] = []

    # check complete shape for intersection with active spline
    sl_length = 0
    for i in range(len(sl)-1):
        for j,spl in enumerate(shape_list):
            for k,pt in enumerate(spl):
                for l in range(len(pt)-1):
                    x = intersect_line_line_2d(sl[i], sl[i+1], pt[l], pt[l+1])
                    if x != None and not ((sl[i] - pt[l]).length < PRECISION or
                                         (sl[i] - pt[l+1]).length < PRECISION or
                                         (sl[i+1] - pt[l]).length < PRECISION or
                                         (sl[i+1] - pt[l+1]).length < PRECISION):
                        cross.append([x, i // shape_ob.data.splines[spl_index].resolution_u, sl_length + (x.to_3d()-sl[i]).length])
        sl_length += (sl[i+1] - sl[i]).length

    cross = sorted([c for c in cross], key = lambda i:i[2])
    return [c[0:2] for c in cross]


def is_between(x, a, b):
    '''
    > x, a, b = point
    < True if x lies between a and b
    '''
    cross = (x[1] - a[1]) * (b[0] - a[0]) - (x[0] - a[0]) * (b[1] - a[1])
    if abs(cross) > PRECISION: return False
    dot = (x[0] - a[0]) * (b[0] - a[0]) + (x[1] - a[1])*(b[1] - a[1])
    if dot < 0 : return False
    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dot > squaredlengthba: return False

    return True


def ratio_to_segment(x, p1, p2, p3, p4, res):
    '''
    > x:            intersection point
    > p1,p2,p3,p4:  cubic bezier control points
    < ratio of x to length of the segment
    '''
    seg = interpolate_bezier(p1, p2, p3, p4, res+1)
    seg_length = length = ratio = 0

    for i in range (len(seg)-1):
        seg_length += (seg[i+1] - seg[i]).length

    for i in range (len(seg)-1):
        if is_between(x, seg[i], seg[i+1]):
            length += (x - seg[i].to_2d()).length
            return length/seg_length
        else:
            length += (seg[i+1] - seg[i]).length


def split_segment(t,p1,p2,p3,p4):
    '''
    > t:            ratio
    > p1,p2,p3,p4:  cubic bezier control points
    < two lists of 4 control points using de Casteljau's algorithm
    '''
    q1 = p1 + (p2-p1)*t
    q2 = p2 + (p3-p2)*t
    q3 = p3 + (p4-p3)*t

    r1 = q1 + (q2-q1)*t
    r2 = q2 + (q3-q2)*t
    r3 = r1 + (r2-r1)*t

    return ([p1,q1,r1,r3], [r3,r2,q3,p4])


def chop(x, p1, p2, p3, p4, res):
    '''
    > x:            intersection point
    > p1,p2,p3,p4:  cubic bezier control points
    > res:          spline resolution
    < both chopped segment's cubic bezier control points
    '''

    ratio = ratio_to_segment(x, p1, p2, p3, p4, res)

    if ratio != None:
        return split_segment(ratio, p1, p2, p3, p4)
    else:
        return None


def main(context):

    shape_ob = context.active_object
    spline_ob = shape_ob.data.splines.active
    spline_id = active_spline_id(shape_ob)

    # gather all intersections of the active spline
    spl_int = spline_X_shape(shape_ob, spline_id)
    point_id = sel_point_id(shape_ob.data.splines[spline_id])

    if len(point_id) > 1: return
    else: point_id = point_id[0]

    low = [x for x in spl_int if x[1] <  point_id]
    high = spl_int[len(low):]

    # case of cyclic spline
    if spline_ob.use_cyclic_u:

        if len(low) + len(high) <= 1:
            print ("cyclic spline needs at least 2 intersections")
            return

        elif len(low) + len(high) > 1:
            print ("breaking up cyclic spline")
            if len(low) == 0:
                low = high
                npoints = high[-1][1] - high[0][1] + 2
            elif len(high) == 0:
                high = low
                npoints = low[-1][1] - low[0][1] + 2
            else:
                npoints = len(spline_ob.bezier_points) - high[0][1] + low[-1][1] + 2

            spline_ob_data = [[[bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right] for bp in spline_ob.bezier_points], spline_ob.resolution_u, spline_ob.use_cyclic_u]

            shape_ob.data.splines.new('BEZIER')
            new_spl = shape_ob.data.splines[-1]
            new_spl.bezier_points.add(npoints-1)

            print (len(spline_ob_data[0]), len(new_spl.bezier_points), npoints)

            for i, bp in enumerate(new_spl.bezier_points):
                print((i+high[0][1])%npoints)
                bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right = spline_ob_data[0][(i+high[0][1])%(len(spline_ob_data[0]))]
            new_spl.resolution_u = spline_ob_data[1]

            s1, s2 = chop(low[-1][0],
                  spline_ob.bezier_points[low[-1][1]].co,
                  spline_ob.bezier_points[low[-1][1]].handle_right,
                  spline_ob.bezier_points[(low[-1][1]+1)%(len(spline_ob_data[0]))].handle_left,
                  spline_ob.bezier_points[(low[-1][1]+1)%(len(spline_ob_data[0]))].co,
                  spline_ob.resolution_u)

            new_spl.bezier_points[-1].handle_left_type = 'FREE'
            new_spl.bezier_points[-1].handle_right_type = 'FREE'
            new_spl.bezier_points[-2].handle_left_type = 'FREE'
            new_spl.bezier_points[-2].handle_right_type = 'FREE'
            new_spl.bezier_points[-1].co = low[-1][0].to_3d() # though mathematically correct: s1[3]
            new_spl.bezier_points[-2].handle_right = s1[1]
            new_spl.bezier_points[-1].handle_left = s1[2]
            new_spl.bezier_points[-1].handle_right = s2[1]

            s3, s4 = chop(high[0][0],
                  spline_ob.bezier_points[high[0][1]].co,
                  spline_ob.bezier_points[high[0][1]].handle_right,
                  spline_ob.bezier_points[(high[0][1]+1)%(len(spline_ob_data[0]))].handle_left,
                  spline_ob.bezier_points[(high[0][1]+1)%(len(spline_ob_data[0]))].co,
                  spline_ob.resolution_u)

            new_spl.bezier_points[0].handle_left_type = 'FREE'
            new_spl.bezier_points[0].handle_right_type = 'FREE'
            new_spl.bezier_points[1].handle_left_type = 'FREE'
            new_spl.bezier_points[1].handle_right_type = 'FREE'
            new_spl.bezier_points[0].co = high[0][0].to_3d() # though mathematically correct: s2[0]
            new_spl.bezier_points[0].handle_left = s3[2]
            new_spl.bezier_points[0].handle_right = s4[1]
            new_spl.bezier_points[1].handle_left = s4[2]

            shape_ob.data.splines.remove(spline_ob)

    # case of open spline
    elif not spline_ob.use_cyclic_u:

        # case of spline end selected
        if len(low) > 0 and len(high) == 0:
            print ("moving last point to ", low[-1])

            spline_ob_data = [[[bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right] for bp in spline_ob.bezier_points], spline_ob.resolution_u, spline_ob.use_cyclic_u]

            shape_ob.data.splines.new('BEZIER')
            new_spl = shape_ob.data.splines[-1]
            new_spl.bezier_points.add(low[-1][1] + 1)

            for i, bp in enumerate(new_spl.bezier_points):
                bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right = spline_ob_data[0][i]
            new_spl.resolution_u, new_spl.use_cyclic_u = spline_ob_data[1], spline_ob_data[2]

            s1, s2 = chop(low[-1][0],
                          spline_ob.bezier_points[low[-1][1]].co,
                          spline_ob.bezier_points[low[-1][1]].handle_right,
                          spline_ob.bezier_points[low[-1][1]+1].handle_left,
                          spline_ob.bezier_points[low[-1][1]+1].co,
                          spline_ob.resolution_u)

            new_spl.bezier_points[-1].handle_left_type = 'FREE'
            new_spl.bezier_points[-1].handle_right_type = 'FREE'
            new_spl.bezier_points[-2].handle_left_type = 'FREE'
            new_spl.bezier_points[-2].handle_right_type = 'FREE'
            new_spl.bezier_points[-1].co = low[-1][0].to_3d() # though mathematically correct: s1[3]
            new_spl.bezier_points[-2].handle_right = s1[1]
            new_spl.bezier_points[-1].handle_left = s1[2]
            new_spl.bezier_points[-1].handle_right = s2[1]

            shape_ob.data.splines.remove(spline_ob)

        # case of spline start selected
        elif len(low) == 0 and len(high) > 0:
            print ("moving first point to ", high[0][0])

            spline_ob_data = [[[bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right] for bp in spline_ob.bezier_points], spline_ob.resolution_u, spline_ob.use_cyclic_u]

            shape_ob.data.splines.new('BEZIER')
            new_spl = shape_ob.data.splines[-1]
            new_spl.bezier_points.add(len(spline_ob_data[0])-high[0][1]-1)

            print(len(spline_ob_data[0]), high[0][1])

            for i, bp in enumerate(new_spl.bezier_points):
                bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right = spline_ob_data[0][i+high[0][1]]
            new_spl.resolution_u, new_spl.use_cyclic_u = spline_ob_data[1], spline_ob_data[2]

            s1, s2 = chop(high[0][0],
                          spline_ob.bezier_points[high[0][1]].co,
                          spline_ob.bezier_points[high[0][1]].handle_right,
                          spline_ob.bezier_points[high[0][1]+1].handle_left,
                          spline_ob.bezier_points[high[0][1]+1].co,
                          spline_ob.resolution_u)

            new_spl.bezier_points[0].handle_left_type = 'FREE'
            new_spl.bezier_points[0].handle_right_type = 'FREE'
            new_spl.bezier_points[1].handle_left_type = 'FREE'
            new_spl.bezier_points[1].handle_right_type = 'FREE'
            new_spl.bezier_points[0].co = high[0][0].to_3d() # though mathematically correct: s2[0]
            new_spl.bezier_points[0].handle_left = s1[2]
            new_spl.bezier_points[0].handle_right = s2[1]
            new_spl.bezier_points[1].handle_left = s2[2]

            shape_ob.data.splines.remove(spline_ob)

        # case of middle of the spline selected
        elif len(low) > 0 and len(high) > 0:
            print ("split spline and move starting and ending point")

            spline_ob_data = [[[bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right] for bp in spline_ob.bezier_points], spline_ob.resolution_u, spline_ob.use_cyclic_u]

            shape_ob.data.splines.new('BEZIER')
            new_spl = shape_ob.data.splines[-1]
            new_spl.bezier_points.add(low[-1][1] + 1)

            for i, bp in enumerate(new_spl.bezier_points):
                bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right = spline_ob_data[0][i]
            new_spl.resolution_u, new_spl.use_cyclic_u = spline_ob_data[1], spline_ob_data[2]

            s1, s2 = chop(low[-1][0],
                          spline_ob.bezier_points[low[-1][1]].co,
                          spline_ob.bezier_points[low[-1][1]].handle_right,
                          spline_ob.bezier_points[low[-1][1]+1].handle_left,
                          spline_ob.bezier_points[low[-1][1]+1].co,
                          spline_ob.resolution_u)

            new_spl.bezier_points[-1].handle_left_type = 'FREE'
            new_spl.bezier_points[-1].handle_right_type = 'FREE'
            new_spl.bezier_points[-2].handle_left_type = 'FREE'
            new_spl.bezier_points[-2].handle_right_type = 'FREE'
            new_spl.bezier_points[-1].co = low[-1][0].to_3d() # though mathematically correct: s1[3]
            new_spl.bezier_points[-2].handle_right = s1[1]
            new_spl.bezier_points[-1].handle_left = s1[2]
            new_spl.bezier_points[-1].handle_right = s2[1]

            shape_ob.data.splines.new('BEZIER')
            new_spl = shape_ob.data.splines[-1]
            new_spl.bezier_points.add(len(spline_ob_data[0])-high[0][1]-1)

            for i, bp in enumerate(new_spl.bezier_points):
                bp.co, bp.handle_left_type, bp.handle_right_type, bp.handle_left, bp.handle_right = spline_ob_data[0][i+high[0][1]]
            new_spl.resolution_u, new_spl.use_cyclic_u = spline_ob_data[1], spline_ob_data[2]

            s1, s2 = chop(high[0][0],
                          spline_ob.bezier_points[high[0][1]].co,
                          spline_ob.bezier_points[high[0][1]].handle_right,
                          spline_ob.bezier_points[high[0][1]+1].handle_left,
                          spline_ob.bezier_points[high[0][1]+1].co,
                          spline_ob.resolution_u)

            new_spl.bezier_points[0].handle_left_type = 'FREE'
            new_spl.bezier_points[0].handle_right_type = 'FREE'
            new_spl.bezier_points[1].handle_left_type = 'FREE'
            new_spl.bezier_points[1].handle_right_type = 'FREE'
            new_spl.bezier_points[0].co = high[0][0].to_3d() # though mathematically correct: s2[0]
            new_spl.bezier_points[0].handle_left = s1[2]
            new_spl.bezier_points[0].handle_right = s2[1]
            new_spl.bezier_points[1].handle_left = s2[2]

            shape_ob.data.splines.remove(spline_ob)


class TrimTool(bpy.types.Operator):
    """Curve Trim Tool"""
    bl_idname = "curve.trim_tool"
    bl_label = "Trim"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ((ob is not None) and
               (ob.type == 'CURVE'))

    def execute(self, context):
        main(context)
        return {'FINISHED'}



def register():
    bpy.utils.register_class(TrimTool)

def unregister():
    bpy.utils.unregister_class(TrimTool)
 
if __name__ == "__main__":
    register()
   

