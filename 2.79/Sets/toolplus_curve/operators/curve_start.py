# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2
#  of the License.
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
    "name": "SFC Bsurfaces",
    "author": "Eclectiel",
    "version": (1, 5),
    "blender": (2, 63, 0),
    "location": "View3D > EditMode > ToolShelf",
    "description": "Modeling and retopology tool.",
    "wiki_url": "http://wiki.blender.org/index.php/Dev:Ref/Release_Notes/2.64/Bsurfaces_1.5",
    "category": "",
}
"""

# LOAD MODUL #
import bpy
import bmesh
import math
import mathutils
import operator

from math import *


class CURVE_SURFSK_first_points(bpy.types.Operator):
    bl_idname = "curve.surfsk_first_points"
    bl_label = "Bsurfaces set first points"
    bl_description = "Set the selected points as the first point of each spline"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        splines_to_invert = []

        #### Check non-cyclic splines to invert.
        for i in range(len(self.main_curve.data.splines)):
            b_points = self.main_curve.data.splines[i].bezier_points

            if not i in self.cyclic_splines: # Only for non-cyclic splines
                if b_points[len(b_points) - 1].select_control_point:
                    splines_to_invert.append(i)


        #### Reorder points of cyclic splines, and set all handles to "Automatic".

        # Check first selected point.
        cyclic_splines_new_first_pt = {}
        for i in self.cyclic_splines:
            sp = self.main_curve.data.splines[i]

            for t in range(len(sp.bezier_points)):
                bp = sp.bezier_points[t]
                if bp.select_control_point or bp.select_right_handle or bp.select_left_handle:
                    cyclic_splines_new_first_pt[i] = t
                    break # To take only one if there are more.

        # Reorder.
        for spline_idx in cyclic_splines_new_first_pt:
            sp = self.main_curve.data.splines[spline_idx]

            spline_old_coords = []
            for bp_old in sp.bezier_points:
                coords = (bp_old.co[0], bp_old.co[1], bp_old.co[2])

                left_handle_type = str(bp_old.handle_left_type)
                left_handle_length = float(bp_old.handle_left.length)
                left_handle_xyz = (float(bp_old.handle_left.x), float(bp_old.handle_left.y), float(bp_old.handle_left.z))

                right_handle_type = str(bp_old.handle_right_type)
                right_handle_length = float(bp_old.handle_right.length)
                right_handle_xyz = (float(bp_old.handle_right.x), float(bp_old.handle_right.y), float(bp_old.handle_right.z))

                spline_old_coords.append([coords, left_handle_type, right_handle_type, left_handle_length, right_handle_length, left_handle_xyz, right_handle_xyz])


            for t in range(len(sp.bezier_points)):
                bp = sp.bezier_points

                if t + cyclic_splines_new_first_pt[spline_idx] + 1 <= len(bp) - 1:
                    new_index = t + cyclic_splines_new_first_pt[spline_idx] + 1
                else:
                    new_index = t + cyclic_splines_new_first_pt[spline_idx] + 1 - len(bp)

                bp[t].co = mathutils.Vector(spline_old_coords[new_index][0])

                bp[t].handle_left.length = spline_old_coords[new_index][3]
                bp[t].handle_right.length = spline_old_coords[new_index][4]

                bp[t].handle_left_type = "FREE"
                bp[t].handle_right_type = "FREE"

                bp[t].handle_left.x = spline_old_coords[new_index][5][0]
                bp[t].handle_left.y = spline_old_coords[new_index][5][1]
                bp[t].handle_left.z = spline_old_coords[new_index][5][2]

                bp[t].handle_right.x = spline_old_coords[new_index][6][0]
                bp[t].handle_right.y = spline_old_coords[new_index][6][1]
                bp[t].handle_right.z = spline_old_coords[new_index][6][2]

                bp[t].handle_left_type = spline_old_coords[new_index][1]
                bp[t].handle_right_type = spline_old_coords[new_index][2]



        #### Invert the non-cyclic splines designated above.
        for i in range(len(splines_to_invert)):
            bpy.ops.curve.select_all('INVOKE_REGION_WIN', action='DESELECT')

            bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')
            self.main_curve.data.splines[splines_to_invert[i]].bezier_points[0].select_control_point = True
            bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')

            bpy.ops.curve.switch_direction()

        bpy.ops.curve.select_all('INVOKE_REGION_WIN', action='DESELECT')


        #### Keep selected the first vert of each spline.
        bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')
        for i in range(len(self.main_curve.data.splines)):
            if not self.main_curve.data.splines[i].use_cyclic_u:
                bp = self.main_curve.data.splines[i].bezier_points[0]
            else:
                bp = self.main_curve.data.splines[i].bezier_points[len(self.main_curve.data.splines[i].bezier_points) - 1]

            bp.select_control_point = True
            bp.select_right_handle = True
            bp.select_left_handle = True
        bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')




        return {'FINISHED'}



    def invoke (self, context, event):
        self.main_curve = bpy.context.object

        # Check if all curves are Bezier, and detect which ones are cyclic.
        self.cyclic_splines = []
        for i in range(len(self.main_curve.data.splines)):
            if self.main_curve.data.splines[i].type != "BEZIER":
                self.report({'WARNING'}, 'All splines must be Bezier type.')

                return {'CANCELLED'}
            else:
                if self.main_curve.data.splines[i].use_cyclic_u:
                    self.cyclic_splines.append(i)



        self.execute(context)
        self.report({'INFO'}, "First points have been set.")

        return {'FINISHED'}


# REGISTRY #       
def register():
    bpy.utils.register_class(CURVE_SURFSK_first_points)

def unregister():
    bpy.utils.unregister_class(CURVE_SURFSK_first_points)

if __name__ == "__main__":
    register()



