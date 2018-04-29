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
    "name": "Curve Extend",
    "description": "Extend selected endpoint(s) for Bezier Splines",
    "author": "jimflim",
    "version": (0, 1),
    "blender": (2, 75, 0),
    "category": "Add Curve",
    "location": "View3D > Tools > Curves",
    "warning": "",
    "wiki_url": "https://github.com/jimflim/blender-scripts"
    }
"""

# LOAD MODUL #
import bpy
from mathutils import Vector
from mathutils.geometry import intersect_line_line_2d, intersect_line_line, interpolate_bezier


PRECISION = 1.0e-5


def get_selected_bezier_splines(shape_ob):
    '''
    returns selected splines
    '''
    s = []
    for i,spl in enumerate(shape_ob.data.splines):
        sel = False
        for bp in spl.bezier_points :
            if bp.select_control_point or bp.select_left_handle or bp.select_right_handle:
                sel = True
        if sel:
            s.append(spl)
    if len(s) == 0:
        s = None
    return s


def selected_endpoints(spline_ob):
    '''
    > spline_ob:     bezier spline object
    < returns selected endpoints with handle
    '''
    if spline_ob.use_cyclic_u:
        return None
    if spline_ob.bezier_points[0].select_control_point and spline_ob.bezier_points[-1].select_control_point:
        return (spline_ob.bezier_points[0].co, spline_ob.bezier_points[0].handle_right,
                spline_ob.bezier_points[-1].co, spline_ob.bezier_points[-1].handle_left)
    elif spline_ob.bezier_points[0].select_control_point:
        return spline_ob.bezier_points[0].co, spline_ob.bezier_points[0].handle_right
    elif spline_ob.bezier_points[-1].select_control_point:
        return spline_ob.bezier_points[-1].co, spline_ob.bezier_points[-1].handle_left
    else:
        return None


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


def linear_spline_list(shape_ob):
    '''
    > shape_ob:     bezier shape object
    < returns list of linear interpolated splinepoints
    '''
    return [interpolate_all_segments(spl) for spl in shape_ob.data.splines]


def get_shape_bounds(shape_ob):
    '''
    > shape_ob:     bezier shape object
    < returns min X, max X, min Y, max Y
    '''
    return (shape_ob.bound_box[0][0], shape_ob.bound_box[4][0],
            shape_ob.bound_box[0][1], shape_ob.bound_box[3][1])


def get_max_extent_2d(p1, p2, bounds):
    '''
    p1, p2:     line segment as pair of 2D vectors
    bounds:     2D bounding box (xmin, xmax, ymin, ymax)
    returns furthest projection of p2->p1 inside bounds
    '''
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    if abs(x1-x2) > abs(y1-y2):
        if x1 < x2:
            #return intersect_line_line_2d(p1, p1_handle, Vector((bounds[0], 0)), Vector((bounds[0], 1)))
            return (Vector((bounds[0], (y2-y1)/(x2-x1)*(bounds[0]-x1)+y1)))
        else:
            return (Vector((bounds[1], (y2-y1)/(x2-x1)*(bounds[1]-x1)+y1)))
    else:
        if y1 < y2:
            return (Vector(((x2-x1)/(y2-y1)*(bounds[2]-y1)+x1, bounds[2])))
        else:
            return (Vector(((x2-x1)/(y2-y1)*(bounds[3]-y1)+x1, bounds[3])))


def get_intersections(p1, p2, shape_ob):
    '''
    > p1, p2:       line segment as pair of 2D vectors
    > shape_ob:     bezier shape object
    < list of intersection points
    '''

    il = []

    for spl in linear_spline_list(shape_ob):
        for i in range(0, len(spl)-1):
            point = intersect_line_line_2d(p2, p1, spl[i], spl[i+1])
            if point != None and (point-p1.to_2d()).length > PRECISION:
                il.append(point)
    return il


def dist_2d(p1, p2):
    '''
    > p1, p2:       2D vectors
    < distance between vectors
    '''
    return (p2.to_2d()-p1.to_2d()).length


def nearest_point(p, p_list):
    '''
    > p:        2D vector
    > p_list:   list of 2D vectors
    < nearest point to p from list
    '''
    if len(p_list)==0:
        return None
    elif len(p_list)==1:
        return p_list[0]
    else:
        return min([points for points in p_list], key = lambda p2:dist_2d(p,p2))


def main(context):
    shape_ob = context.active_object

    sel_spl = [spl for spl in get_selected_bezier_splines(shape_ob) if not spl.use_cyclic_u]

    if sel_spl == None or len(sel_spl) == 0 or len(sel_spl) > 2:
        print ("wrong selection")
        return
    # case of one endpoint selected
    if len(sel_spl) == 1:
        sel_pts = selected_endpoints(sel_spl[0])
        if len(sel_pts) == 2:
            p1, p1_handle = sel_pts
            p1_extend = get_max_extent_2d(p1, p1_handle, get_shape_bounds(shape_ob))
            p2 = nearest_point(p1, get_intersections(p1, p1_extend, shape_ob))
        # case of two endpoints selected on the same spline
        elif len(sel_pts) == 4:
            p2 = intersect_line_line(sel_pts[1], sel_pts[0], sel_pts[3], sel_pts[2])[0]
        else:
            print ("wrong selection")
            return
    # case of two endpoints selected on seperate splines
    if len(sel_spl) == 2:
        sel_pts = selected_endpoints(sel_spl[0]) + selected_endpoints(sel_spl[1])
        p2 = intersect_line_line(sel_pts[1], sel_pts[0], sel_pts[3], sel_pts[2])[0]

    # add point to spline(s)
    if p2 == None:
        print ("no extension found")
    else:
        print ("extended point found on: ", p2)
        if len(sel_spl) == 1:
            if len(sel_pts) == 2:
                bpy.ops.curve.handle_type_set(type='ALIGNED')
                bpy.ops.curve.vertex_add(location=(p2.to_3d()+bpy.context.object.location))
                bpy.ops.curve.handle_type_set(type='AUTOMATIC')
            elif len(sel_pts) == 4:
                bpy.ops.curve.handle_type_set(type='ALIGNED')
                bpy.ops.curve.vertex_add()
                sel_spl[0].bezier_points[0].co = p2.to_3d()
                sel_spl[0].bezier_points[-1].co = p2.to_3d()
                bpy.ops.curve.handle_type_set(type='AUTOMATIC')
        elif len(sel_spl) == 2:
            bpy.ops.curve.handle_type_set(type='ALIGNED')
            bpy.ops.curve.vertex_add()
            if sel_spl[0].bezier_points[0].select_control_point:
                sel_spl[0].bezier_points[0].co = p2.to_3d()
            else:
                sel_spl[0].bezier_points[-1].co = p2.to_3d()
            if sel_spl[1].bezier_points[0].select_control_point:
                sel_spl[1].bezier_points[0].co = p2.to_3d()
            else:
                sel_spl[1].bezier_points[-1].co = p2.to_3d()
            bpy.ops.curve.handle_type_set(type='AUTOMATIC')



class ExtendTool(bpy.types.Operator):
    """Curve Extend Tool"""
    bl_idname = "curve.extend_tool"
    bl_label = "Extend"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ((ob is not None) and
               (ob.type == 'CURVE'))

    def execute(self, context):
        main(context)
        return {'FINISHED'}


# REGISTRY #        
def register():
    bpy.utils.register_class(ExtendTool)

def unregister():
    bpy.utils.unregister_class(ExtendTool)

if __name__ == "__main__":
    register()
   
