# 3D NAVIGATION TOOLBAR v1.2 - 3Dview Addon - Blender 2.5x
#
# THIS SCRIPT IS LICENSED UNDER GPL,
# please read the license block.
#
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
# contributed to by: Demohero, uriel, jbelcik, meta-androcto

bl_info = {
    "name": "3D Navigation",
    "author": "Demohero, uriel",
    "version": (1, 2, 1),
    "blender": (2, 77, 0),
    "location": "View3D > Tool Shelf > Navigation Tab",
    "description": "Navigate the Camera & 3D View from the Toolshelf",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/3D_Navigation",
    "category": "3D View",
}

# import the basic library
import bpy

# main class of this toolbar

## re-ordered (reversed) Orbit Oprators
class OrbitUpView1(bpy.types.Operator):
    bl_idname = 'opr.orbit_up_view1'
    bl_label = 'Orbit Up View'
    bl_description = 'Orbit the view towards you'

    def execute(self, context):
        bpy.ops.view3d.view_orbit(type='ORBITUP')
        return {'FINISHED'}


class OrbitLeftView1(bpy.types.Operator):
    bl_idname = 'opr.orbit_left_view1'
    bl_label = 'Orbit Left View'
    bl_description = 'Orbit the view around to your Right'

    def execute(self, context):
        bpy.ops.view3d.view_orbit(type='ORBITLEFT')
        return {'FINISHED'}


class OrbitRightView1(bpy.types.Operator):
    bl_idname = 'opr.orbit_right_view1'
    bl_label = 'Orbit Right View'
    bl_description = 'Orbit the view around to your Left'

    def execute(self, context):
        bpy.ops.view3d.view_orbit(type='ORBITRIGHT')
        return {'FINISHED'}


class OrbitDownView1(bpy.types.Operator):
    bl_idname = 'opr.orbit_down_view1'
    bl_label = 'Orbit Down View'
    bl_description = 'Orbit the view away from you'

    def execute(self, context):
        bpy.ops.view3d.view_orbit(type='ORBITDOWN')
        return {'FINISHED'}

## re-ordered (reversed) Pan Oprators
class PanUpView1(bpy.types.Operator):
    bl_idname = 'opr.pan_up_view1'
    bl_label = 'Pan Up View'
    bl_description = 'Pan the view Down'

    def execute(self, context):
        bpy.ops.view3d.view_pan(type='PANUP')
        return {'FINISHED'}


class PanLeftView1(bpy.types.Operator):
    bl_idname = 'opr.pan_left_view1'
    bl_label = 'Pan Right View'
    bl_description = 'Pan the view to your Right'

    def execute(self, context):
        bpy.ops.view3d.view_pan(type='PANLEFT')
        return {'FINISHED'}


class PanRightView1(bpy.types.Operator):
    bl_idname = 'opr.pan_right_view1'
    bl_label = 'Pan Left View'
    bl_description = 'Pan the view to your Left'

    def execute(self, context):
        bpy.ops.view3d.view_pan(type='PANRIGHT')
        return {'FINISHED'}


class PanDownView1(bpy.types.Operator):
    bl_idname = 'opr.pan_down_view1'
    bl_label = 'Pan Down View'
    bl_description = 'Pan the view up'

    def execute(self, context):
        bpy.ops.view3d.view_pan(type='PANDOWN')
        return {'FINISHED'}

## Zoom Oprators
class ZoomInView1(bpy.types.Operator):
    bl_idname = 'opr.zoom_in_view1'
    bl_label = 'Zoom In View'
    bl_description = 'Zoom in in the view'

    def execute(self, context):
        bpy.ops.view3d.zoom(delta=1)
        return {'FINISHED'}


class ZoomOutView1(bpy.types.Operator):
    bl_idname = 'opr.zoom_out_view1'
    bl_label = 'Zoom Out View'
    bl_description = 'Zoom out in the view'

    def execute(self, context):
        bpy.ops.view3d.zoom(delta=-1)
        return {'FINISHED'}

## Roll Oprators
class RollLeftView1(bpy.types.Operator):
    bl_idname = 'opr.roll_left_view1'
    bl_label = 'Roll Left View'
    bl_description = 'Roll the view left'

    def execute(self, context):
        bpy.ops.view3d.view_roll(angle=-0.261799)
        return {'FINISHED'}


class RollRightView1(bpy.types.Operator):
    bl_idname = 'opr.roll_right_view1'
    bl_label = 'Roll Right View'
    bl_description = 'Roll the view right'

    def execute(self, context):
        bpy.ops.view3d.view_roll(angle=0.261799)
        return {'FINISHED'}


class LeftViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.left_viewpoint1'
    bl_label = 'Left Viewpoint'
    bl_description = 'View from the Left'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='LEFT')
        return {'FINISHED'}


class RightViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.right_viewpoint1'
    bl_label = 'Right Viewpoint'
    bl_description = 'View from the Right'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='RIGHT')
        return {'FINISHED'}


class FrontViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.front_viewpoint1'
    bl_label = 'Front Viewpoint'
    bl_description = 'View from the Front'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='FRONT')
        return {'FINISHED'}


class BackViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.back_viewpoint1'
    bl_label = 'Back Viewpoint'
    bl_description = 'View from the Back'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='BACK')
        return {'FINISHED'}


class TopViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.top_viewpoint1'
    bl_label = 'Top Viewpoint'
    bl_description = 'View from the Top'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='TOP')
        return {'FINISHED'}


class BottomViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.bottom_viewpoint1'
    bl_label = 'Bottom Viewpoint'
    bl_description = 'View from the Bottom'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='BOTTOM')
        return {'FINISHED'}


class ShowHideObject1(bpy.types.Operator):
    bl_idname = 'opr.show_hide_object1'
    bl_label = 'Show/Hide Object'
    bl_description = 'Show/hide selected objects'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.object == None:
            self.report({'ERROR'}, 'Cannot perform this operation on NoneType objects')
            return {'CANCELLED'}

        if context.object.mode != 'OBJECT':
            self.report({'ERROR'}, 'This operation can be performed only in object mode')
            return {'CANCELLED'}

        for i in bpy.data.objects:
            if i.select:
                if i.hide:
                    i.hide = False
                    i.hide_select = False
                    i.hide_render = False
                else:
                    i.hide = True
                    i.select = False

                    if i.type not in ['CAMERA', 'LAMP']:
                        i.hide_render = True
        return {'FINISHED'}


classes = [
    OrbitUpView1,
    OrbitLeftView1,
    OrbitRightView1,
    OrbitDownView1,
    PanUpView1,
    PanLeftView1,
    PanRightView1,
    PanDownView1,
    ZoomInView1,
    ZoomOutView1,
    RollLeftView1,
    RollRightView1,
    LeftViewpoint1,
    RightViewpoint1,
    FrontViewpoint1,
    BackViewpoint1,
    TopViewpoint1,
    BottomViewpoint1,
    ShowHideObject1
]

# register the class

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
