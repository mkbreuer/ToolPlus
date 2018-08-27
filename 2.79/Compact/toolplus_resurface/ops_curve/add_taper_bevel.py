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
#
# extended by Marvin.K.Breuer
#

"""
bl_info = {
    "name": "Bevel/Taper Curve",
    "author": "Cmomoney",
    "version": (1, 1),
    "blender": (2, 69, 0),
    "location": "View3D > Object > Bevel/Taper",
    "description": "Adds bevel and/or taper curve to active curve",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Bevel_-Taper_Curve",
    "tracker_url": "https://projects.blender.org/tracker/index.php?func=detail&aid=37377&group_id=153&atid=467",
    "category": "Curve"}
""" 
 
import bpy
from bpy.types import Operator
from bpy.props import *
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector



# TAPER CREATION #
def make_path(self, context, verts):
    
    target = bpy.context.scene.objects.active

    bpy.ops.curve.primitive_nurbs_path_add(view_align=False, enter_editmode=False, location=(0, 0, 0))

    target.data.taper_object = bpy.context.scene.objects.active

    taper = bpy.context.scene.objects.active
    taper.name = target.name + '_Taper'

    bpy.context.scene.objects.active = target
    points = taper.data.splines[0].points

    for i in range(len(verts)):
        points[i].co = verts[i]


def add_taper(self, context):

    scale_ends1 = self.scale_ends1
    scale_ends2 = self.scale_ends2
    scale_mid = self.scale_mid
    verts = [(-2.0, 1.0 * scale_ends1, 0.0, 1.0), (-1.0, 0.75 * scale_mid, 0.0, 1.0), (0.0, 1.5 * scale_mid, 0.0, 1.0), (1.0, 0.75 * scale_mid, 0.0, 1.0), (2.0, 1.0 * scale_ends2, 0.0, 1.0)]
    make_path(self, context, verts)


class add_tapercurve(Operator, AddObjectHelper):
    """Add taper curve to active curve"""
    bl_idname = "curve.tapercurve"
    bl_label = "Add Curve as Taper"
    bl_options = {'REGISTER', 'UNDO'}


    scale_ends1 = FloatProperty(name="End Width Left", description="Adjust left end taper", default=0.0, min=0.0)
    scale_ends2 = FloatProperty(name="End Width Right", description="Adjust right end taper", default=0.0, min=0.0)
    scale_mid = FloatProperty(name="Center Width", description="Adjust taper at center", default=1.0, min=0.0)
    link1 = BoolProperty(name='link ends', default=True)
    link2 = BoolProperty(name='link ends/center', default=False)
    if link2:
        diff = FloatProperty(name='Difference', default=1, description='Difference between ends and center while linked')

    def execute(self, context):
        if self.link1:
            self.scale_ends2 = self.scale_ends1
        if self.link2:
            self.scale_ends2 = self.scale_ends1 = self.scale_mid-self.diff
        add_taper(self, context)
        return {'FINISHED'}
    




# BEVEL CREATION #
def make_curve(self, context, verts, lh, rh):

    scale_x = self.scale_x
    scale_y = self.scale_y
    
    type = self.shape_type
    
    target = bpy.context.scene.objects.active
    
    curve_data = bpy.data.curves.new(name=target.name +'_Bevel', type='CURVE')
    curve_data.dimensions = '3D'
    
    for p in range(len(verts)):
        c = 0
        spline = curve_data.splines.new(type='BEZIER')
        spline.use_cyclic_u = True
        spline.bezier_points.add( len(verts[p])/3-1 )
        spline.bezier_points.foreach_set('co', verts[p])
    
        for bp in spline.bezier_points:

            bp.handle_left_type = 'ALIGNED'
            bp.handle_right_type = 'ALIGNED'
                       
            bp.handle_left.xyz = lh[p][c]
            bp.handle_right.xyz = rh[p][c]
            c += 1
    
    object_data_add(context, curve_data, operator=self)
    
    target.data.bevel_object = bpy.context.scene.objects.active
    
    bpy.context.scene.objects.active = target



def make_curve_vector(self, context, verts, lh, rh):

    scale_x = self.scale_x
    scale_y = self.scale_y
    
    type = self.shape_type
    
    target = bpy.context.scene.objects.active
    
    curve_data = bpy.data.curves.new(name=target.name +'_Bevel', type='CURVE')
    curve_data.dimensions = '3D'
    
    for p in range(len(verts)):
        c = 0
        spline = curve_data.splines.new(type='BEZIER')
        spline.use_cyclic_u = True
        spline.bezier_points.add( len(verts[p])/3-1 )
        spline.bezier_points.foreach_set('co', verts[p])
    
        for bp in spline.bezier_points:

            bp.handle_left_type = 'VECTOR'
            bp.handle_right_type = 'VECTOR'
                      
            bp.handle_left.xyz = lh[p][c]
            bp.handle_right.xyz = rh[p][c]
            c += 1
    
    object_data_add(context, curve_data, operator=self)
    
    target.data.bevel_object = bpy.context.scene.objects.active
    
    bpy.context.scene.objects.active = target
    

def make_curve_free(self, context, verts, lh, rh):

    scale_x = self.scale_x
    scale_y = self.scale_y
    
    type = self.shape_type
    
    target = bpy.context.scene.objects.active
    
    curve_data = bpy.data.curves.new(name=target.name +'_Bevel', type='CURVE')
    curve_data.dimensions = '3D'
    
    for p in range(len(verts)):
        c = 0
        spline = curve_data.splines.new(type='BEZIER')
        spline.use_cyclic_u = True
        spline.bezier_points.add( len(verts[p])/3-1 )
        spline.bezier_points.foreach_set('co', verts[p])
    
        for bp in spline.bezier_points:

            bp.handle_left_type = 'FREE'
            bp.handle_right_type = 'FREE'
                      
            bp.handle_left.xyz = lh[p][c]
            bp.handle_right.xyz = rh[p][c]
            c += 1
    
    object_data_add(context, curve_data, operator=self)
    
    target.data.bevel_object = bpy.context.scene.objects.active
    
    bpy.context.scene.objects.active = target



def add_type5(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, 0.049549 * scale_y, 0.0, 0.031603 * scale_x, 0.047013 * scale_y, 0.0, 0.05 * scale_x, 0.0 * scale_y, 0.0, 0.031603 * scale_x, -0.047013 * scale_y, 0.0, 0.0 * scale_x, -0.049549 * scale_y, 0.0, -0.031603 * scale_x, -0.047013 * scale_y, 0.0, -0.05 * scale_x, -0.0 * scale_y, 0.0, -0.031603 * scale_x, 0.047013 * scale_y, 0.0]]
    lhandles = [[(-0.008804 * scale_x, 0.049549 * scale_y, 0.0), (0.021304 * scale_x, 0.02119 * scale_y, 0.0), (0.05 * scale_x, 0.051228 * scale_y, 0.0), (0.036552 * scale_x, -0.059423 * scale_y, 0.0), (0.008804 * scale_x, -0.049549 * scale_y, 0.0), (-0.021304 * scale_x, -0.02119 * scale_y, 0.0), (-0.05 * scale_x, -0.051228 * scale_y, 0.0), (-0.036552 * scale_x, 0.059423 * scale_y, 0.0)]]
    rhandles = [[(0.008803 * scale_x, 0.049549 * scale_y, 0.0), (0.036552 * scale_x, 0.059423 * scale_y, 0.0), (0.05 * scale_x, -0.051228 * scale_y, 0.0), (0.021304 * scale_x, -0.02119 * scale_y, 0.0), (-0.008803 * scale_x, -0.049549 * scale_y, 0.0), (-0.036552 * scale_x, -0.059423 * scale_y, 0.0), (-0.05 * scale_x, 0.051228 * scale_y, 0.0), (-0.021304 * scale_x, 0.02119 * scale_y, 0.0)]]
    make_curve(self, context, verts, lhandles, rhandles)
    
def add_type4(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0 * scale_x, 0.017183 * scale_y, 0.0, 0.05 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, -0.017183 * scale_y, 0.0, -0.05 * scale_x, -0.0 * scale_y, 0.0]]
    lhandles = [[(-0.017607 * scale_x, 0.017183 * scale_y, 0.0), (0.05 * scale_x, 0.102456 * scale_y, 0.0), (0.017607 * scale_x, -0.017183 * scale_y, 0.0), (-0.05 * scale_x, -0.102456 * scale_y, 0.0)]]
    rhandles = [[(0.017607 * scale_x, 0.017183 * scale_y, 0.0), (0.05 * scale_x, -0.102456 * scale_y, 0.0), (-0.017607 * scale_x, -0.017183 * scale_y, 0.0), (-0.05 * scale_x, 0.102456 * scale_y, 0.0)]]
    make_curve(self, context, verts, lhandles, rhandles)
    
def add_type3(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.017183 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, 0.05 * scale_y, 0.0, 0.017183 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, -0.05 * scale_y, 0.0]]
    lhandles = [[(-0.017183 * scale_x, -0.017607 * scale_y, 0.0), (-0.102456 * scale_x, 0.05 * scale_y, 0.0), (0.017183 * scale_x, 0.017607 * scale_y, 0.0), (0.102456 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.017183 * scale_x, 0.017607 * scale_y, 0.0), (0.102456 * scale_x, 0.05 * scale_y, 0.0), (0.017183 * scale_x, -0.017607 * scale_y, 0.0), (-0.102456 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve(self, context, verts, lhandles, rhandles)
    
def add_type2(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.05 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, 0.05 * scale_y, 0.0, 0.05 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, -0.05 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.047606 * scale_y, 0.0), (-0.047606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.047607 * scale_y, 0.0), (0.047606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.047607 * scale_y, 0.0), (0.047607 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, -0.047607 * scale_y, 0.0), (-0.047607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve(self, context, verts, lhandles, rhandles)
    



# SHAPE: MISC #

def add_type_cross(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)



def add_type_scales(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)



def add_type_leaf(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)



def add_type_flower(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.01 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)



# SHAPE: VECTOR #

def add_type_segment(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, -0.1 * scale_y, 0.0,   -0.0866025 * scale_x, 0.05 * scale_y, 0.0,   0.00 * scale_x, 0.1 * scale_y, 0.0,    0.0866025 * scale_x, 0.05 * scale_y, 0.0]]
    lhandles = [[( 0.028868 * scale_x, -0.05 * scale_y, 0.0), (-0.057735 * scale_x, 0.0      * scale_y, 0.0), (-0.039041 * scale_x, 0.1 * scale_y, 0.0), (0.086603 * scale_x, 0.066667 * scale_y, 0.0)]]
    rhandles = [[(-0.028868 * scale_x, -0.05 * scale_y, 0.0), (-0.086603 * scale_x, 0.066667 * scale_y, 0.0), ( 0.039041 * scale_x, 0.1 * scale_y, 0.0), (0.057735 * scale_x, 0.0      * scale_y, 0.0)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_octagon(self, context):   
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, -0.1 * scale_y, 0.0,   -0.0707107 * scale_x, -0.0707107  * scale_y, 0.0,   -0.1 * scale_x, 0.0 * scale_y, 0.0,   -0.0707107 * scale_x,   0.0707107  * scale_y, 0.0,
              0.0 * scale_x,  0.1 * scale_y, 0.0,    0.0707107 * scale_x,  0.0707107  * scale_y, 0.0,    0.1 * scale_x, 0.0 * scale_y, 0.0,    0.0707107  * scale_x, -0.0707107  * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_hexagon(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, -0.1 * scale_y, 0.0,   -0.0866025 * scale_x, -0.05 * scale_y, 0.0,   -0.0866025 * scale_x, 0.05 * scale_y, 0.0,   0.0 * scale_x, 0.1 * scale_y, 0.0,
              0.0866025 * scale_x, 0.05 * scale_y, 0.0,   0.0866025 * scale_x, -0.05 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_pentagon(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0587785 * scale_x, -0.0809017 * scale_y, 0.0,   -0.0951057 * scale_x, 0.0309017 * scale_y, 0.0,   0.0 * scale_x, 0.1 * scale_y, 0.0,  0.0951057 * scale_x, 0.0309017  * scale_y, 0.0,
               0.0587785 * scale_x, -0.0809017 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_rhombus(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, -0.1 * scale_y, 0.0,  -0.1 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, 0.1 * scale_y, 0.0, 0.1 * scale_x, 0.0 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_triangle(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y                         
    verts = [[-0.0866 * scale_x, -0.05 * scale_y, 0.0,    0.0 * scale_x, 0.1 * scale_y, 0.0,   0.0866 * scale_x, -0.05 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_trapez(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0707107 * scale_x, -0.0707107 * scale_y, 0.0,   -0.0353553 * scale_x, 0.0707107 * scale_y, 0.0,   0.0353553 * scale_x, 0.0707107 * scale_y, 0.0,    0.0707107 * scale_x, -0.0707107 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)    


def add_type_rectangle(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0707107 * scale_x, -0.0424264 * scale_y, 0.0,   -0.0707107 * scale_x, 0.0424264 * scale_y, 0.0,   0.0707107 * scale_x, 0.0424264 * scale_y, 0.0,    0.0707107 * scale_x, -0.0424264 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_square(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0707107 * scale_x, -0.0707107 * scale_y, 0.0,   -0.0707107 * scale_x, 0.0707107 * scale_y, 0.0,   0.0707107 * scale_x, 0.0707107 * scale_y, 0.0,    0.0707107 * scale_x, -0.0707107 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_quadercircle(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, 0.0 * scale_y, 0.0,   0.0 * scale_x, 0.1 * scale_y, 0.0,   0.1 * scale_x, 0.0 * scale_y, 0.0]] 
    lhandles = [[( 0.044787 * scale_x,  0.0      * scale_y, 0.0),  ( 0.0      * scale_x, 0.044787 * scale_y, 0.0),   (0.10 * scale_x, 0.055213 * scale_y, 0.0)]]
    rhandles = [[( 0.0      * scale_x,  0.044787 * scale_y, 0.0),  ( 0.055213 * scale_x, 0.10     * scale_y, 0.0),   (0.05 * scale_x, 0.0      * scale_y, 0.0)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_halfcircle(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.1 * scale_x, 0.0 * scale_y, 0.0,   0.0 * scale_x, 0.1 * scale_y, 0.0,   0.1 * scale_x, 0.0 * scale_y, 0.0]] 
    lhandles = [[(-0.055213 * scale_x,  0.0      * scale_y, 0.0),  (-0.055213 * scale_x, 0.10 * scale_y, 0.0),   (0.10 * scale_x, 0.055213 * scale_y, 0.0)]]
    rhandles = [[(-0.1      * scale_x,  0.055213 * scale_y, 0.0),  ( 0.055213 * scale_x, 0.10 * scale_y, 0.0),   (0.05 * scale_x, 0.0      * scale_y, 0.0)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_circle(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.05 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, 0.05 * scale_y, 0.0, 0.05 * scale_x, 0.0 * scale_y, 0.0, 0.0 * scale_x, -0.05 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0),  ( 0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0),  (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve(self, context, verts, lhandles, rhandles)




# SHAPE: CHAMFER #

def add_type_3chamfer(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.061603 * scale_x, -0.05     * scale_y, 0.0,  -0.074103 * scale_x, -0.028349 * scale_y, 0.0,   -0.0125 * scale_x, 0.078349 * scale_y, 0.0,    0.0125 * scale_x, 0.078349 * scale_y, 0.0,
               0.074103 * scale_x, -0.028349 * scale_y, 0.0,   0.061603 * scale_x, -0.05     * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_4chamfer(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.017678 * scale_x, -0.082322 * scale_y, 0.0,   -0.082322 * scale_x, -0.017678 * scale_y, 0.0,  -0.082322 * scale_x,  0.017678 * scale_y, 0.0,   -0.017678 * scale_x,  0.082322 * scale_y, 0.0,
               0.017678 * scale_x,  0.082322 * scale_y, 0.0,    0.082322 * scale_x,  0.017678 * scale_y, 0.0,   0.082322 * scale_x, -0.017678 * scale_y, 0.0,    0.017678 * scale_x, -0.082322 * scale_y, 0.0,]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_5chamfer(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.033779 * scale_x, -0.080902 * scale_y, 0.0,   -0.066504 * scale_x, -0.057125 * scale_y, 0.0,   -0.08738 * scale_x,  0.0071253 * scale_y, 0.0,   -0.07488 * scale_x,  0.045596  * scale_y, 0.0,
              -0.020225 * scale_x,  0.085305 * scale_y, 0.0,    0.020225 * scale_x,  0.085305 * scale_y, 0.0,    0.07488 * scale_x,  0.045596  * scale_y, 0.0,    0.08738 * scale_x,  0.0071253 * scale_y, 0.0,
               0.066504 * scale_x, -0.057125 * scale_y, 0.0,    0.033779 * scale_x, -0.080902 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_6chamfer(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.021651 * scale_x, -0.0875 * scale_y, 0.0,   -0.064952 * scale_x, -0.0625 * scale_y, 0.0,   -0.086603 * scale_x, -0.025  * scale_y, 0.0,   -0.086603 * scale_x,  0.025  * scale_y, 0.0,
              -0.064952 * scale_x,  0.0625 * scale_y, 0.0,   -0.021651 * scale_x,  0.0875 * scale_y, 0.0,    0.021651 * scale_x,  0.0875 * scale_y, 0.0,    0.064952 * scale_x,  0.0625 * scale_y, 0.0,        
               0.086603 * scale_x,  0.025  * scale_y, 0.0,    0.086603 * scale_x, -0.025  * scale_y, 0.0,    0.064952 * scale_x, -0.0625 * scale_y, 0.0,    0.021651 * scale_x, -0.0875 * scale_y, 0.0,]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_8chamfer(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.023097 * scale_x, -0.090433 * scale_y, 0.0,   -0.047614 * scale_x, -0.080278 * scale_y, 0.0,   -0.080278 * scale_x, -0.047614 * scale_y, 0.0,   -0.090433 * scale_x, -0.023097 * scale_y, 0.0,
              -0.090433 * scale_x,  0.023097 * scale_y, 0.0,   -0.080278 * scale_x,  0.047614 * scale_y, 0.0,   -0.047614 * scale_x,  0.080278 * scale_y, 0.0,   -0.023097 * scale_x,  0.090433 * scale_y, 0.0,        
               0.023097 * scale_x,  0.090433 * scale_y, 0.0,    0.047614 * scale_x,  0.080278 * scale_y, 0.0,    0.080278 * scale_x,  0.047614 * scale_y, 0.0,    0.090433 * scale_x,  0.023097 * scale_y, 0.0,        
               0.090433 * scale_x, -0.023097 * scale_y, 0.0,    0.080278 * scale_x, -0.047614 * scale_y, 0.0,    0.047614 * scale_x, -0.080278 * scale_y, 0.0,    0.023097 * scale_x, -0.090433 * scale_y, 0.0]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)




# SHAPE: STAR #

def add_type_3star(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0      * scale_x, -0.025  * scale_y, 0.0,  -0.086603 * scale_x, -0.05 * scale_y, 0.0,   -0.024651 * scale_x, 0.0125 * scale_y, 0.0,   0.0 * scale_x, 0.1 * scale_y, 0.0,
              0.021651 * scale_x,  0.0125 * scale_y, 0.0,   0.086603 * scale_x, -0.05 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_4star(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0 * scale_x, -0.1 * scale_y, 0.0,   -0.025 * scale_x, -0.025 * scale_y, 0.0,  -0.1 * scale_x, 0.0 * scale_y, 0.0,   -0.025 * scale_x,  0.025 * scale_y, 0.0,
              0.0 * scale_x,  0.1 * scale_y, 0.0,    0.025 * scale_x,  0.025 * scale_y, 0.0,   0.1 * scale_x, 0.0 * scale_y, 0.0,    0.025 * scale_x, -0.025 * scale_y, 0.0]] 
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_5star(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0      * scale_x, -0.044314 * scale_y, 0.0,   -0.058779 * scale_x, -0.080902 * scale_y, 0.0,   -0.038471 * scale_x, -0.016363 * scale_y, 0.0,    -0.095106 * scale_x,  0.030902 * scale_y, 0.0,
              -0.023776 * scale_x,  0.028863 * scale_y, 0.0,    0.0      * scale_x,  0.1      * scale_y, 0.0,    0.023776 * scale_x,  0.028863 * scale_y, 0.0,     0.095106 * scale_x,  0.030902 * scale_y, 0.0,          
               0.038471 * scale_x, -0.016363 * scale_y, 0.0,    0.058779 * scale_x, -0.080902 * scale_y, 0.0]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_6star(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[ 0.0      * scale_x, -0.1  * scale_y, 0.0,   -0.021651 * scale_x, -0.0375 * scale_y, 0.0,   -0.086603 * scale_x, -0.05 * scale_y, 0.0,   -0.043301 * scale_x,  0.0    * scale_y, 0.0,
              -0.086603 * scale_x,  0.05 * scale_y, 0.0,   -0.021651 * scale_x,  0.0375 * scale_y, 0.0,    0.00     * scale_x,  0.1  * scale_y, 0.0,    0.021651 * scale_x,  0.0375 * scale_y, 0.0,
               0.086603 * scale_x,  0.05 * scale_y, 0.0,    0.043301 * scale_x,  0.0    * scale_y, 0.0,    0.086603 * scale_x, -0.05 * scale_y, 0.0,    0.021651 * scale_x, -0.0375 * scale_y, 0.0,]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)


def add_type_8star(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[ 0.0 * scale_x, -0.1 * scale_y, 0.0,   -0.017678 * scale_x, -0.042678 * scale_y, 0.0,   -0.070711 * scale_x, -0.070711 * scale_y, 0.0,   -0.042678 * scale_x, -0.017678 * scale_y, 0.0,       
              -0.1 * scale_x,  0.0 * scale_y, 0.0,   -0.042678 * scale_x,  0.017678 * scale_y, 0.0,   -0.070711 * scale_x,  0.070711 * scale_y, 0.0,   -0.017678 * scale_x,  0.042678 * scale_y, 0.0,
               0.0 * scale_x,  0.1 * scale_y, 0.0,    0.017678 * scale_x,  0.042678 * scale_y, 0.0,    0.070711 * scale_x,  0.070711 * scale_y, 0.0,    0.042678 * scale_x,  0.017678 * scale_y, 0.0,
               0.1 * scale_x,  0.0 * scale_y, 0.0,    0.042678 * scale_x, -0.017678 * scale_y, 0.0,    0.070711 * scale_x, -0.070711 * scale_y, 0.0,    0.017678 * scale_x, -0.042678 * scale_y, 0.0,]]
    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05  * scale_y, 0.0), (0.05 * scale_x,  0.027606 * scale_y, 0.0), ( 0.027606 * scale_x, -0.05 * scale_y, 0.0)]]
    rhandles = [[(-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x,  0.027607 * scale_y, 0.0), ( 0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]
    make_curve_vector(self, context, verts, lhandles, rhandles)




# SHAPE: GROOVE #

def add_type_3groove(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)


def add_type_4groove(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)


def add_type_5groove(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)


def add_type_6groove(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)


def add_type_8groove(self, context):
    
    scale_x = self.scale_x
    scale_y = self.scale_y
              #                                      #                                        #                                        #
    verts = [[-0.25 * scale_x, 0.0 * scale_y, 0.0,   -0.073 * scale_x, 0.073 * scale_y, 0.0,   0.00 * scale_x, 0.25 * scale_y, 0.0,    0.073 * scale_x, 0.073 * scale_y, 0.0,
               0.25 * scale_x, 0.0 * scale_y, 0.0,   0.073 * scale_x, -0.073 * scale_y, 0.0,   0.00 * scale_x, -0.25 * scale_y, 0.0,   -0.073 * scale_x, -0.073 * scale_y, 0.0,]]

    lhandles = [[(-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, -0.027606 * scale_y, 0.0), (-0.027606 * scale_x, 0.05 * scale_y, 0.0), (0.05 * scale_x, 0.027606 * scale_y, 0.0), (0.027606 * scale_x, -0.05 * scale_y, 0.0)]]

    rhandles = [[(-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0),
                 (-0.05 * scale_x, 0.027607 * scale_y, 0.0), (0.027607 * scale_x, 0.005 * scale_y, 0.0), (0.05 * scale_x, -0.027607 * scale_y, 0.0), (-0.027607 * scale_x, -0.05 * scale_y, 0.0)]]

    make_curve(self, context, verts, lhandles, rhandles)





# SHAPE: CONVEX #

def add_type_3convex(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y              #                                      #                                        #                                        #
    verts = [[-0.086603 * scale_x, -0.050000 * scale_y, 0.0000,  -0.021651 * scale_x,  0.006250 * scale_y, 0.0000,  0.0000 * scale_x, 0.100000 * scale_y, 0.0000,  0.021651 * scale_x, 0.006250 * scale_y, 0.0000,
               0.086603 * scale_x, -0.050000 * scale_y, 0.0000,   0.0000   * scale_x, -0.031250 * scale_y, 0.0000]]
    lhandles = [[(-0.057735 * scale_x, -0.043750 * scale_y, 0.0000), (-0.038956 * scale_x, -0.022487 * scale_y, 0.0000), (-0.007217 * scale_x, 0.068750 * scale_y, 0.0000), (0.002272 * scale_x, 0.038430 * scale_y, 0.0000),
                 ( 0.064952 * scale_x, -0.031250 * scale_y, 0.0000), ( 0.034594 * scale_x, -0.031250 * scale_y, 0.0000)]]
    rhandles = [[(-0.064952 * scale_x, -0.031250 * scale_y, 0.0000), (-0.002272 * scale_x,  0.038430 * scale_y, 0.0000), (0.007217 * scale_x, 0.068750 * scale_y, 0.0000), (0.038956 * scale_x, -0.022487 * scale_y, 0.0000), 
                 ( 0.057735 * scale_x, -0.043750 * scale_y, 0.0000), (-0.034594 * scale_x, -0.031250 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_4convex(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[0.0000 * scale_x,  0.10000 * scale_y, 0.0000,   0.025000 * scale_x,  0.025000 * scale_y, 0.0000,    0.10000 * scale_x,  0.0000 * scale_y, 0.0000,    0.025000 * scale_x, -0.025000 * scale_y, 0.0000,
              0.0000 * scale_x, -0.10000 * scale_y, 0.0000,  -0.025000 * scale_x, -0.025000 * scale_y, 0.0000,   -0.10000 * scale_x, -0.0000 * scale_y, 0.0000,   -0.025000 * scale_x,  0.025000 * scale_y, 0.0000]]          
    lhandles = [[(-0.008333 * scale_x,  0.075000 * scale_y, 0.0000),  ( 0.003175 * scale_x,  0.046825 * scale_y, 0.0000),  ( 0.075000 * scale_x,  0.008333 * scale_y, 0.0000),  ( 0.046825 * scale_x, -0.003175 * scale_y, 0.0000),
                 ( 0.008333 * scale_x, -0.075000 * scale_y, 0.0000),  (-0.003175 * scale_x, -0.046825 * scale_y, 0.0000),  (-0.075000 * scale_x, -0.008333 * scale_y, 0.0000),  (-0.046825 * scale_x,  0.003175 * scale_y, 0.0000)]]
    rhandles = [[( 0.008333 * scale_x,  0.075000 * scale_y, 0.0000),  ( 0.046825 * scale_x,  0.003175 * scale_y, 0.0000),  ( 0.075000 * scale_x, -0.008333 * scale_y, 0.0000),  ( 0.003175 * scale_x, -0.046825 * scale_y, 0.0000),
                 (-0.008333 * scale_x, -0.075000 * scale_y, 0.0000),  (-0.046825 * scale_x, -0.003175 * scale_y, 0.0000),  (-0.075000 * scale_x,  0.008333 * scale_y, 0.0000),  (-0.003175 * scale_x,  0.046825 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_5convex(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y 
    verts = [[-0.0588 * scale_x, -0.0809 * scale_y, 0.0000,  -0.0385 * scale_x, -0.0164 * scale_y, 0.0000,  -0.0951 * scale_x, 0.0309 * scale_y, 0.0000,  -0.0238 * scale_x,  0.0289 * scale_y, 0.0000,
               0.0000 * scale_x,  0.1000 * scale_y, 0.0000,   0.0238 * scale_x,  0.0289 * scale_y, 0.0000,   0.0951 * scale_x, 0.0309 * scale_y, 0.0000,   0.0385 * scale_x, -0.0164 * scale_y, 0.0000,
               0.0588 * scale_x, -0.0809 * scale_y, 0.0000,   0.0000 * scale_x, -0.0443 * scale_y, 0.0000]]
    lhandles = [[(-0.0392 * scale_x, -0.0687 * scale_y, 0.0000),  (-0.0310 * scale_x, -0.0417 * scale_y, 0.0000),  (-0.0762 * scale_x, 0.0151 * scale_y, 0.0000),  (-0.0466 * scale_x, 0.0129 * scale_y, 0.0000),
                 (-0.0079 * scale_x,  0.0763 * scale_y, 0.0000),  (-0.0002 * scale_x,  0.0456 * scale_y, 0.0000),  ( 0.0713 * scale_x, 0.0302 * scale_y, 0.0000),  ( 0.0466 * scale_x, 0.0113 * scale_y, 0.0000),
                 ( 0.0520 * scale_x, -0.0594 * scale_y, 0.0000),  ( 0.0270 * scale_x, -0.0443 * scale_y, 0.0000)]]
    rhandles = [[(-0.0520 * scale_x, -0.0594 * scale_y, 0.0000),  (-0.0466 * scale_x,  0.0113 * scale_y, 0.0000),  (-0.0713 * scale_x, 0.0302 * scale_y, 0.0000),  (0.0002 * scale_x,  0.0456 * scale_y, 0.0000),
                 ( 0.0079 * scale_x,  0.0763 * scale_y, 0.0000),  ( 0.0466 * scale_x,  0.0129 * scale_y, 0.0000),  ( 0.0762 * scale_x, 0.0151 * scale_y, 0.0000),  (0.0310 * scale_x, -0.0417 * scale_y, 0.0000),
                 ( 0.0392 * scale_x, -0.0687 * scale_y, 0.0000),  (-0.0270 * scale_x, -0.0443 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_6convex(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0217 * scale_x, -0.0375 * scale_y, 0.0000,  -0.0866 * scale_x, -0.0500 * scale_y, 0.0000,  -0.0433 * scale_x, -0.0000 * scale_y, 0.0000,  -0.0866 * scale_x,  0.0500 * scale_y, 0.0000,
              -0.0217 * scale_x,  0.0375 * scale_y, 0.0000,   0.0000 * scale_x,  0.1000 * scale_y, 0.0000,   0.0217 * scale_x,  0.0375 * scale_y, 0.0000,   0.0866 * scale_x,  0.0500 * scale_y, 0.0000,
               0.0433 * scale_x,  0.0000 * scale_y, 0.0000,   0.0866 * scale_x, -0.0500 * scale_y, 0.0000,   0.0217 * scale_x, -0.0375 * scale_y, 0.0000,   0.0000 * scale_x, -0.1000 * scale_y, 0.0000]]

    lhandles = [[( 0.0007 * scale_x, -0.0504 * scale_y, 0.0000),  (-0.0650 * scale_x, -0.0458 * scale_y, 0.0000),  (-0.0433 * scale_x, -0.0258 * scale_y, 0.0000),  (-0.0722 * scale_x,  0.0333 * scale_y, 0.0000),
                 (-0.0440 * scale_x,  0.0246 * scale_y, 0.0000),  (-0.0072 * scale_x,  0.0792 * scale_y, 0.0000),  (-0.0007 * scale_x,  0.0504 * scale_y, 0.0000),  ( 0.0650 * scale_x,  0.0458 * scale_y, 0.0000),
                 ( 0.0433 * scale_x,  0.0258 * scale_y, 0.0000),  ( 0.0722 * scale_x, -0.0333 * scale_y, 0.0000),  ( 0.0440 * scale_x, -0.0246 * scale_y, 0.0000),  ( 0.0072 * scale_x, -0.0792 * scale_y, 0.0000)]]
    rhandles = [[(-0.0440 * scale_x, -0.0246 * scale_y, 0.0000),  (-0.0722 * scale_x, -0.0333 * scale_y, 0.0000),  (-0.0433 * scale_x,  0.0258 * scale_y, 0.0000),  (-0.0650 * scale_x,  0.0458 * scale_y, 0.0000),
                 ( 0.0007 * scale_x,  0.0504 * scale_y, 0.0000),  ( 0.0072 * scale_x,  0.0792 * scale_y, 0.0000),  ( 0.0440 * scale_x,  0.0246 * scale_y, 0.0000),  ( 0.0722 * scale_x,  0.0333 * scale_y, 0.0000),
                 ( 0.0433 * scale_x, -0.0258 * scale_y, 0.0000),  ( 0.0650 * scale_x, -0.0458 * scale_y, 0.0000),  (-0.0007 * scale_x, -0.0504 * scale_y, 0.0000),  (-0.0072 * scale_x, -0.0792 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_8convex(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0177 * scale_x, -0.0427 * scale_y, 0.0000,  -0.0707 * scale_x, -0.0707 * scale_y, 0.0000,  -0.0427 * scale_x, -0.0177 * scale_y, 0.0000,  -0.1000 * scale_x, -0.0000 * scale_y, 0.0000,
              -0.0427 * scale_x,  0.0177 * scale_y, 0.0000,  -0.0707 * scale_x,  0.0707 * scale_y, 0.0000,  -0.0177 * scale_x,  0.0427 * scale_y, 0.0000,   0.0000 * scale_x,  0.1000 * scale_y, 0.0000,
               0.0177 * scale_x,  0.0427 * scale_y, 0.0000,   0.0707 * scale_x,  0.0707 * scale_y, 0.0000,   0.0427 * scale_x,  0.0177 * scale_y, 0.0000,   0.1000 * scale_x,  0.0000 * scale_y, 0.0000,
               0.0427 * scale_x, -0.0177 * scale_y, 0.0000,   0.0707 * scale_x, -0.0707 * scale_y, 0.0000,   0.0177 * scale_x, -0.0427 * scale_y, 0.0000,   0.0000 * scale_x, -0.1000 * scale_y, 0.0000]]
    lhandles = [[( 0.0040 * scale_x, -0.0516 * scale_y, 0.0000),  (-0.0530 * scale_x, -0.0614 * scale_y, 0.0000),  (-0.0337 * scale_x, -0.0393 * scale_y, 0.0000),  (-0.0809 * scale_x, -0.0059 * scale_y, 0.0000),
                 (-0.0516 * scale_x, -0.0040 * scale_y, 0.0000),  (-0.0614 * scale_x,  0.0530 * scale_y, 0.0000),  (-0.0393 * scale_x,  0.0337 * scale_y, 0.0000),  (-0.0059 * scale_x,  0.0809 * scale_y, 0.0000),
                 (-0.0040 * scale_x,  0.0516 * scale_y, 0.0000),  ( 0.0530 * scale_x,  0.0614 * scale_y, 0.0000),  ( 0.0337 * scale_x,  0.0393 * scale_y, 0.0000),  ( 0.0809 * scale_x,  0.0059 * scale_y, 0.0000),
                 ( 0.0516 * scale_x,  0.0040 * scale_y, 0.0000),  ( 0.0614 * scale_x, -0.0530 * scale_y, 0.0000),  ( 0.0393 * scale_x, -0.0337 * scale_y, 0.0000),  ( 0.0059 * scale_x, -0.0809 * scale_y, 0.0000)]]
    rhandles = [[(-0.0393 * scale_x, -0.0337 * scale_y, 0.0000),  (-0.0614 * scale_x, -0.0530 * scale_y, 0.0000),  (-0.0516 * scale_x,  0.0040 * scale_y, 0.0000),  (-0.0809 * scale_x,  0.0059 * scale_y, 0.0000),
                 (-0.0337 * scale_x,  0.0393 * scale_y, 0.0000),  (-0.0530 * scale_x,  0.0614 * scale_y, 0.0000),  ( 0.0040 * scale_x,  0.0516 * scale_y, 0.0000),  ( 0.0059 * scale_x,  0.0809 * scale_y, 0.0000),
                 ( 0.0393 * scale_x,  0.0337 * scale_y, 0.0000),  ( 0.0614 * scale_x,  0.0530 * scale_y, 0.0000),  ( 0.0516 * scale_x, -0.0040 * scale_y, 0.0000),  ( 0.0809 * scale_x, -0.0059 * scale_y, 0.0000),
                 ( 0.0337 * scale_x, -0.0393 * scale_y, 0.0000),  ( 0.0530 * scale_x, -0.0614 * scale_y, 0.0000),  (-0.0040 * scale_x, -0.0516 * scale_y, 0.0000),  (-0.0059 * scale_x, -0.0809 * scale_y, 0.0000)]] 
    make_curve_free(self, context, verts, lhandles, rhandles)





# SHAPE: CONCAVE #

def add_type_3concave(self, context):    
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0866 * scale_x, -0.0500 * scale_y, 0.0000,  -0.0650 * scale_x,  0.0438 * scale_y, 0.0000,   0.0000 * scale_x,  0.1000 * scale_y, 0.0000,   0.0650 * scale_x,  0.0438 * scale_y, 0.0000,
               0.0866 * scale_x, -0.0500 * scale_y, 0.0000,   0.0000 * scale_x, -0.0688 * scale_y, 0.0000]]               
    lhandles = [[(-0.0577 * scale_x, -0.0563 * scale_y, 0.0000),  (-0.0843 * scale_x,  0.0116 * scale_y, 0.0000),  (-0.0217 * scale_x,  0.0813 * scale_y, 0.0000),  ( 0.0476 * scale_x,  0.0725 * scale_y, 0.0000),
                 ( 0.0794 * scale_x, -0.0187 * scale_y, 0.0000),  ( 0.0346 * scale_x, -0.0688 * scale_y, 0.0000)]]
    rhandles = [[(-0.0794 * scale_x, -0.0188 * scale_y, 0.0000),  (-0.0476 * scale_x,  0.0725 * scale_y, 0.0000),  ( 0.0217 * scale_x,  0.0813 * scale_y, 0.0000),  ( 0.0843 * scale_x,  0.0116 * scale_y, 0.0000),
                 ( 0.0577 * scale_x, -0.0563 * scale_y, 0.0000),  (-0.0346 * scale_x, -0.0688 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_4concave(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0750 * scale_x, -0.0750 * scale_y, 0.0000,   -0.1000 * scale_x, -0.0000 * scale_y, 0.0000,   -0.0750 * scale_x,  0.0750 * scale_y, 0.0000,    0.0000 * scale_x,  0.1000 * scale_y, 0.0000,
               0.0750 * scale_x,  0.0750 * scale_y, 0.0000,    0.1000 * scale_x,  0.0000 * scale_y, 0.0000,    0.0750 * scale_x, -0.0750 * scale_y, 0.0000,    0.0000 * scale_x, -0.1000 * scale_y, 0.0000]] 
    lhandles = [[(-0.0532 * scale_x, -0.0968 * scale_y, 0.0000),  (-0.0917 * scale_x, -0.0250 * scale_y, 0.0000),  (-0.0968 * scale_x,  0.0532 * scale_y, 0.0000),  (-0.0250 * scale_x,  0.0917 * scale_y, 0.0000),
                 ( 0.0532 * scale_x,  0.0968 * scale_y, 0.0000),  ( 0.0917 * scale_x,  0.0250 * scale_y, 0.0000),  ( 0.0968 * scale_x, -0.0532 * scale_y, 0.0000),  ( 0.0250 * scale_x, -0.0917 * scale_y, 0.0000)]] 
    rhandles = [[(-0.0968 * scale_x, -0.0532 * scale_y, 0.0000),  (-0.0917 * scale_x,  0.0250 * scale_y, 0.0000),  (-0.0532 * scale_x,  0.0968 * scale_y, 0.0000),  ( 0.0250 * scale_x,  0.0917 * scale_y, 0.0000),
                 ( 0.0968 * scale_x,  0.0532 * scale_y, 0.0000),  ( 0.0917 * scale_x, -0.0250 * scale_y, 0.0000),  ( 0.0532 * scale_x, -0.0968 * scale_y, 0.0000),  (-0.0250 * scale_x, -0.0917 * scale_y, 0.0000)]] 
    make_curve_free(self, context, verts, lhandles, rhandles)



def add_type_5concave(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0588 * scale_x, -0.0809 * scale_y, 0.0000,  -0.1154 * scale_x, -0.0336 * scale_y, 0.0000,  -0.0951 * scale_x,  0.0309 * scale_y, 0.0000,  -0.0713 * scale_x,  0.1020 * scale_y, 0.0000,
               0.0000 * scale_x,  0.1000 * scale_y, 0.0000,   0.0713 * scale_x,  0.1020 * scale_y, 0.0000,   0.0951 * scale_x,  0.0309 * scale_y, 0.0000,   0.1154 * scale_x, -0.0336 * scale_y, 0.0000,
               0.0588 * scale_x, -0.0809 * scale_y, 0.0000,   0.0000 * scale_x, -0.1175 * scale_y, 0.0000]]               
    lhandles = [[(-0.0392 * scale_x, -0.0931 * scale_y, 0.0000),  (-0.1073 * scale_x, -0.0613 * scale_y, 0.0000),  (-0.1019 * scale_x,  0.0094 * scale_y, 0.0000),  (-0.0953 * scale_x,  0.0853 * scale_y, 0.0000),
                 (-0.0238 * scale_x,  0.1007 * scale_y, 0.0000),  ( 0.0485 * scale_x,  0.1180 * scale_y, 0.0000),  ( 0.0872 * scale_x,  0.0546 * scale_y, 0.0000),  ( 0.1228 * scale_x, -0.0083 * scale_y, 0.0000),
                 ( 0.0777 * scale_x, -0.0651 * scale_y, 0.0000),  ( 0.0270 * scale_x, -0.1175 * scale_y, 0.0000)]]
    rhandles = [[(-0.0777 * scale_x, -0.0651 * scale_y, 0.0000),  (-0.1228 * scale_x, -0.0083 * scale_y, 0.0000),  (-0.0872 * scale_x,  0.0546 * scale_y, 0.0000),  (-0.0485 * scale_x,  0.1180 * scale_y, 0.0000),
                 ( 0.0238 * scale_x,  0.1007 * scale_y, 0.0000),  ( 0.0953 * scale_x,  0.0853 * scale_y, 0.0000),  ( 0.1019 * scale_x,  0.0094 * scale_y, 0.0000),  ( 0.1073 * scale_x, -0.0613 * scale_y, 0.0000),
                 ( 0.0392 * scale_x, -0.0931 * scale_y, 0.0000),  (-0.0270 * scale_x, -0.1175 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_6concave(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0650 * scale_x, -0.1125 * scale_y, 0.0000,  -0.0866 * scale_x, -0.0500 * scale_y, 0.0000,  -0.1299 * scale_x, -0.0000 * scale_y, 0.0000,  -0.0866 * scale_x,  0.0500 * scale_y, 0.0000,
              -0.0650 * scale_x,  0.1125 * scale_y, 0.0000,   0.0000 * scale_x,  0.1000 * scale_y, 0.0000,   0.0650 * scale_x,  0.1125 * scale_y, 0.0000,   0.0866 * scale_x,  0.0500 * scale_y, 0.0000,
               0.1299 * scale_x,  0.0000 * scale_y, 0.0000,   0.0866 * scale_x, -0.0500 * scale_y, 0.0000,   0.0650 * scale_x, -0.1125 * scale_y, 0.0000,   0.0000 * scale_x, -0.1000 * scale_y, 0.0000]]
    lhandles = [[(-0.0426 * scale_x, -0.1254 * scale_y, 0.0000),  (-0.0794 * scale_x, -0.0708 * scale_y, 0.0000),  (-0.1299 * scale_x, -0.0258 * scale_y, 0.0000),  (-0.1010 * scale_x,  0.0333 * scale_y, 0.0000),
                 (-0.0873 * scale_x,  0.0996 * scale_y, 0.0000),  (-0.0217 * scale_x,  0.1042 * scale_y, 0.0000),  ( 0.0426 * scale_x,  0.1254 * scale_y, 0.0000),  ( 0.0794 * scale_x,  0.0708 * scale_y, 0.0000),
                 ( 0.1299 * scale_x,  0.0258 * scale_y, 0.0000),  ( 0.1010 * scale_x, -0.0333 * scale_y, 0.0000),  ( 0.0873 * scale_x, -0.0996 * scale_y, 0.0000),  ( 0.0217 * scale_x, -0.1042 * scale_y, 0.0000)]]
    rhandles = [[(-0.0873 * scale_x, -0.0996 * scale_y, 0.0000),  (-0.1010 * scale_x, -0.0333 * scale_y, 0.0000),  (-0.1299 * scale_x,  0.0258 * scale_y, 0.0000),  (-0.0794 * scale_x,  0.0708 * scale_y, 0.0000),
                 (-0.0426 * scale_x,  0.1254 * scale_y, 0.0000),  ( 0.0217 * scale_x,  0.1042 * scale_y, 0.0000),  ( 0.0873 * scale_x,  0.0996 * scale_y, 0.0000),  ( 0.1010 * scale_x,  0.0333 * scale_y, 0.0000),
                 ( 0.1299 * scale_x, -0.0258 * scale_y, 0.0000),  ( 0.0794 * scale_x, -0.0708 * scale_y, 0.0000),  ( 0.0426 * scale_x, -0.1254 * scale_y, 0.0000),  (-0.0217 * scale_x, -0.1042 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)


def add_type_8concave(self, context):
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [[-0.0530 * scale_x, -0.1280 * scale_y, 0.0000,  -0.0707 * scale_x, -0.0707 * scale_y, 0.0000,  -0.1280 * scale_x, -0.0530 * scale_y, 0.0000,  -0.1000 * scale_x, -0.0000 * scale_y, 0.0000,
              -0.1280 * scale_x,  0.0530 * scale_y, 0.0000,  -0.0707 * scale_x,  0.0707 * scale_y, 0.0000,  -0.0530 * scale_x,  0.1280 * scale_y, 0.0000,   0.0000 * scale_x,  0.1000 * scale_y, 0.0000,
               0.0530 * scale_x,  0.1280 * scale_y, 0.0000,   0.0707 * scale_x,  0.0707 * scale_y, 0.0000,   0.1280 * scale_x,  0.0530 * scale_y, 0.0000,   0.1000 * scale_x,  0.0000 * scale_y, 0.0000,
               0.1280 * scale_x, -0.0530 * scale_y, 0.0000,   0.0707 * scale_x, -0.0707 * scale_y, 0.0000,   0.0530 * scale_x, -0.1280 * scale_y, 0.0000,   0.0000 * scale_x, -0.1000 * scale_y, 0.0000]]
    lhandles = [[(-0.0314 * scale_x, -0.1370 * scale_y, 0.0000),  (-0.0648 * scale_x, -0.0898 * scale_y, 0.0000),  (-0.1191 * scale_x, -0.0747 * scale_y, 0.0000),  (-0.1093 * scale_x, -0.0177 * scale_y, 0.0000),
                 (-0.1370 * scale_x,  0.0314 * scale_y, 0.0000),  (-0.0898 * scale_x,  0.0648 * scale_y, 0.0000),  (-0.0747 * scale_x,  0.1191 * scale_y, 0.0000),  (-0.0177 * scale_x,  0.1093 * scale_y, 0.0000),
                 ( 0.0314 * scale_x,  0.1370 * scale_y, 0.0000),  ( 0.0648 * scale_x,  0.0898 * scale_y, 0.0000),  ( 0.1191 * scale_x,  0.0747 * scale_y, 0.0000),  ( 0.1093 * scale_x,  0.0177 * scale_y, 0.0000),
                 ( 0.1370 * scale_x, -0.0314 * scale_y, 0.0000),  ( 0.0898 * scale_x, -0.0648 * scale_y, 0.0000),  ( 0.0747 * scale_x, -0.1191 * scale_y, 0.0000),  ( 0.0177 * scale_x, -0.1093 * scale_y, 0.0000)]]
    rhandles = [[(-0.0747 * scale_x, -0.1191 * scale_y, 0.0000),  (-0.0898 * scale_x, -0.0648 * scale_y, 0.0000),  (-0.1370 * scale_x, -0.0314 * scale_y, 0.0000),  (-0.1093 * scale_x,  0.0177 * scale_y, 0.0000),
                 (-0.1191 * scale_x,  0.0747 * scale_y, 0.0000),  (-0.0648 * scale_x,  0.0898 * scale_y, 0.0000),  (-0.0314 * scale_x,  0.1370 * scale_y, 0.0000),  ( 0.0177 * scale_x,  0.1093 * scale_y, 0.0000),
                 ( 0.0747 * scale_x,  0.1191 * scale_y, 0.0000),  ( 0.0898 * scale_x,  0.0648 * scale_y, 0.0000),  ( 0.1370 * scale_x,  0.0314 * scale_y, 0.0000),  ( 0.1093 * scale_x, -0.0177 * scale_y, 0.0000),
                 ( 0.1191 * scale_x, -0.0747 * scale_y, 0.0000),  ( 0.0648 * scale_x, -0.0898 * scale_y, 0.0000),  ( 0.0314 * scale_x, -0.1370 * scale_y, 0.0000),  (-0.0177 * scale_x, -0.1093 * scale_y, 0.0000)]]
    make_curve_free(self, context, verts, lhandles, rhandles)





# LOAD MODUL #    
#from .. icons.icons import load_icons    


class add_bevelcurve(Operator, AddObjectHelper):
    """Add bevel curve to active curve"""
    bl_idname = "curve.bevelcurve"
    bl_label = "Add Curve as Bevel"
    bl_options = {'REGISTER', 'UNDO'}


#    icons = load_icons()
#    types_bool =  [("tp_01"    ,"Direct"  ,"direct boolean"  ,icons["icon_boolean_rebool"].icon_id          ,0),
#                   ("tp_02"    ,"Brush"   ,"brush boolean"   ,icons["icon_boolean_rebool_brush"].icon_id    ,1), 
#                   ("tp_03"    ,"Multi"   ,"multi boolean"   ,"MOD_ARRAY" ,2)]                   
#    bpy.types.Scene.tp_bool = bpy.props.EnumProperty(name = " ", default = "tp_01", items = types_bool)
    

    shape_type = EnumProperty(name = "Shape Type",
            items=(('3CONVEX',      "3-Convex",     ""),                   
                   ('4CONVEX',      "4-Convex",     ""),                   
                   ('5CONVEX',      "5-Convex",     ""),                   
                   ('6CONVEX',      "6-Convex",     ""),                   
                   ('8CONVEX',      "8-Convex",     ""),                   

                   ('3CONCAVE',     "3-Concave",    ""),                   
                   ('4CONCAVE',     "4-Concave",    ""),                   
                   ('5CONCAVE',     "5-Concave",    ""),                   
                   ('6CONCAVE',     "6-Concave",    ""),                   
                   ('8CONCAVE',     "8-Concave",    ""),       

                   ('3STAR',        "3-Star",       ""),                   
                   ('4STAR',        "4-Star",       ""),                   
                   ('5STAR',        "5-Star",       ""),                   
                   ('6STAR',        "6-Star",       ""),                   
                   ('8STAR',        "8-Star",       ""),       

                   ('3GROOVE',      "3-Groove",     ""),
                   ('4GROOVE',      "4-Groove",     ""),
                   ('5GROOVE',      "5-Groove",     ""),
                   ('6GROOVE',      "6-Groove",     ""),
                   ('8GROOVE',      "8-Groove",     ""),

                   ('3CHAMFER',      "3-Chamfer",    ""),
                   ('4CHAMFER',      "4-Chamfer",    ""),
                   ('5CHAMFER',      "5-Chamfer",    ""),
                   ('6CHAMFER',      "6-Chamfer",    ""),
                   ('8CHAMFER',      "8-Chamfer",    ""),
                   
                   ('CROSS',        "Cross",        ""), 
                   ('SCALES',       "Scales",       ""), 
                   ('LEAF',         "Leaf",         ""), 
                   ('FLOWER',       "Flower",       ""),     

                   ('SEGMENT',      "Segment",      ""),
                   ('OCTAGON',      "Octagon",      ""),  
                   ('HEXAGON',      "Hexagon",      ""),  
                   ('PENTAGON',     "Pentagon",     ""),  
                   ('RHOMBUS',      "Rhombus",      ""), 
                   ('TRIANGLE',     "Triangle",     ""), 
                   ('TRAPEZ',       "Trapez",       ""), 
                   ('RECTANGLE',    "Rectangle",    ""), 
                   ('SQUARE',       "Square",       ""),
                   
                   ('QUADERCIRCLE', "1/4-Circle",   ""),                   
                   ('HALFCIRCLE',   "1/2-Circle",   ""),                   
                   ('CIRCLE',       "1/1-Circle",   "")),                   

                   default='CIRCLE',
                   description="Use predefined shape of bevel")


    scale_x = FloatProperty(name="scale x", description="scale on x axis", default=5.0)
    scale_y = FloatProperty(name="scale y", description="scale on y axis", default=5.0)
    link = BoolProperty(name='link xy', default=True)

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_center()

        if self.link:
            self.scale_y = self.scale_x
        
        
        if self.shape_type == 'CIRCLE':
            add_type_circle(self, context)

        if self.shape_type == 'HALFCIRCLE':
            add_type_halfcircle(self, context)

        if self.shape_type == 'QUADERCIRCLE':
            add_type_quadercircle(self, context)


        if self.shape_type == 'SQUARE':
            add_type_square(self, context)   

        if self.shape_type == 'RECTANGLE':
            add_type_rectangle(self, context)   
                     
        if self.shape_type == 'TRAPEZ':
            add_type_trapez(self, context)

        if self.shape_type == 'TRIANGLE':
            add_type_triangle(self, context)
            
        if self.shape_type == 'RHOMBUS':
            add_type_rhombus(self, context)
 
        if self.shape_type == 'PENTAGON':
            add_type_pentagon(self, context)

        if self.shape_type == 'HEXAGON':
            add_type_hexagon(self, context)

        if self.shape_type == 'OCTAGON':
            add_type_octagon(self, context)

        if self.shape_type == 'SEGMENT':
            add_type_segment(self, context)


        if self.shape_type == 'FLOWER':
            add_type_flower(self, context)

        if self.shape_type == 'LEAF':
            add_type_leaf(self, context)

        if self.shape_type == 'SCALES':
            add_type_scales(self, context)

        if self.shape_type == 'CROSS':
            add_type_cross(self, context)



        if self.shape_type == '3CHAMFER':
            add_type_3chamfer(self, context)

        if self.shape_type == '4CHAMFER':
            add_type_4chamfer(self, context)

        if self.shape_type == '5CHAMFER':
            add_type_5chamfer(self, context)

        if self.shape_type == '6CHAMFER':
            add_type_6chamfer(self, context)

        if self.shape_type == '8CHAMFER':
            add_type_8chamfer(self, context)
            
            

        if self.shape_type == '3GROOVE':
            add_type_3groove(self, context)

        if self.shape_type == '4GROOVE':
            add_type_4groove(self, context)
      
        if self.shape_type == '5GROOVE':
            add_type_5groove(self, context)
      
        if self.shape_type == '6GROOVE':
            add_type_6groove(self, context)

        if self.shape_type == '8GROOVE':
            add_type_8groove(self, context)


        if self.shape_type == '3STAR':
            add_type_3star(self, context)
            
        if self.shape_type == '4STAR':
            add_type_4star(self, context)
      
        if self.shape_type == '5STAR':
            add_type_5star(self, context)
      
        if self.shape_type == '6STAR':
            add_type_6star(self, context)

        if self.shape_type == '8STAR':
            add_type_8star(self, context)


        if self.shape_type == '3CONVEX':
            add_type_3convex(self, context)
            
        if self.shape_type == '4CONVEX':
            add_type_4convex(self, context)

        if self.shape_type == '5CONVEX':
            add_type_5convex(self, context)

        if self.shape_type == '6CONVEX':
            add_type_6convex(self, context)

        if self.shape_type == '8CONVEX':
            add_type_8convex(self, context)


        if self.shape_type == '3CONCAVE':
            add_type_3concave(self, context)
            
        if self.shape_type == '4CONCAVE':
            add_type_4concave(self, context)

        if self.shape_type == '5CONCAVE':
            add_type_5concave(self, context)

        if self.shape_type == '6CONCAVE':
            add_type_6concave(self, context)

        if self.shape_type == '8CONCAVE':
            add_type_8concave(self, context)


        return {'FINISHED'}



def register():
    bpy.utils.register_class(add_tapercurve)
    bpy.utils.register_class(add_bevelcurve)

def unregister():
    bpy.utils.unregister_class(add_tapercurve)
    bpy.utils.unregister_class(add_bevelcurve)

if __name__ == "__main__":
    register()