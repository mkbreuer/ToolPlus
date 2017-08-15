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


import bpy
from bpy.types import Operator, Panel


def Add_Pipe(outer_radius, inner_radius, height, res, res2, do_taper, taperval):

    # Adds Curve Path to scene
    bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=False, view_align=False)
    curv = bpy.context.object
    curv.name = "Pipe"
    bpy.ops.transform.translate(value=(height / 2.0, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)

    # Create Cross-section
    bpy.ops.curve.primitive_bezier_circle_add(radius=outer_radius, rotation=(0, 0, 0), view_align=False)
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.context.object.data.resolution_u = res
    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.duplicate_move(CURVE_OT_duplicate={}, TRANSFORM_OT_translate={"value": (0, 0, 0), "constraint_axis": (False, False, False), "constraint_orientation": 'GLOBAL', "mirror": False, "proportional": 'DISABLED', "proportional_edit_falloff": 'SMOOTH', "proportional_size": 1, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "gpencil_strokes": False, "texture_space": False, "remove_on_cancel": False, "release_confirm": False})
    scale = inner_radius / outer_radius
    bpy.ops.transform.resize(value=(scale, scale, scale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()

    cross = bpy.context.object
    cross.name = "Pipe_cross-section"
    bpy.ops.object.shade_smooth()

    # Select curve path
    sce = bpy.context.scene
    sce.objects.active = curv
    cross.select = False
    curv.select = True
    bpy.ops.object.editmode_toggle()
    scale = height / 4
    bpy.ops.transform.resize(value=(scale, scale, scale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()

    if do_taper:
        # Create taper curve
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False, "mode": 'TRANSLATION'}, TRANSFORM_OT_translate={"value": (0, 0, 0), "constraint_axis": (False, False, False), "constraint_orientation": 'GLOBAL', "mirror": False, "proportional": 'DISABLED', "proportional_edit_falloff": 'SMOOTH', "proportional_size": 1, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "gpencil_strokes": False, "texture_space": False, "remove_on_cancel": False, "release_confirm": False})
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.translate(value=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
        bpy.ops.curve.de_select_first()
        bpy.ops.curve.de_select_last()
        bpy.ops.curve.delete(type='VERT')
        bpy.ops.object.editmode_toggle()
        lr = 1
        if (outer_radius > inner_radius):
            lr = outer_radius
        else:
            lr = inner_radius
        bpy.ops.transform.resize(value=(lr, lr, lr), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.de_select_last()
        bpy.ops.transform.translate(value=(0, lr * taperval - lr, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
        bpy.ops.object.editmode_toggle()

        taper = bpy.context.object
        taper.name = "Pipe_taper"

        # Select curve path
        sce = bpy.context.scene
        sce.objects.active = curv
        curv.select = True
        bpy.context.object.data.taper_object = bpy.data.objects[taper.name]

    bpy.context.object.data.bevel_object = bpy.data.objects[cross.name]
    bpy.context.object.data.use_fill_caps = True
    bpy.context.object.data.resolution_u = res2


class AddPipe(bpy.types.Operator):
    """Create an editable Pipe with seperate Path and Cross-section curve objects"""
    bl_idname = "mesh.primitive_pipe_add"
    bl_label = "Add Pipe"
    bl_options = {'REGISTER', 'UNDO'}

    outer_radius = bpy.props.FloatProperty(name="Radius 1",
                                           description="Pipe 1st radius",
                                           min=0.01,
                                           max=9999.0,
                                           default=0.6)
    inner_radius = bpy.props.FloatProperty(name="Radius 2",
                                           description="Pipe 2nd radius",
                                           min=0.01,
                                           max=9999.0,
                                           default=0.5)
    height = bpy.props.FloatProperty(name="Length",
                                     description="Length of the pipe",
                                     min=0.01,
                                     max=9999.0,
                                     default=4.0)
    res = bpy.props.IntProperty(name="Cross-section resolution",
                                description="Controls mesh smoothness for cross-section",
                                min=1,
                                max=20,
                                default=6)
    res2 = bpy.props.IntProperty(name="Path curves resolution",
                                 description="Controls mesh smoothness for curves",
                                 min=1,
                                 max=20,
                                 default=6)
    taper = bpy.props.BoolProperty(name="Taper",
                                   description="Adds taper curve for variable cross-section size over the length of the pipe",
                                   default=0)
    taperval = bpy.props.FloatProperty(name="Taper rate",
                                       description="Sets the initial size of the pipe end relative to its origin",
                                       min=0.01,
                                       max=10.0,
                                       default=1)

    def execute(self, context):
        Add_Pipe(self.outer_radius, self.inner_radius, self.height, self.res, self.res2, self.taper, self.taperval)

        return {'FINISHED'}
