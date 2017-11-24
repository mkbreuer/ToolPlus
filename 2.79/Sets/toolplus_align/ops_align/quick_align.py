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


#bl_info = {"name": "Quick align", "author": "Nexus Studio"}

import bpy
from bpy import*
from bpy.props import *


def align_XYZ(x, y, z, axisX, axisY, axisZ):
    piv = bpy.context.space_data.pivot_point
    scene = bpy.context.scene
    bpy.context.space_data.pivot_point = scene.regarding

    if bpy.context.mode == 'OBJECT':
        bpy.context.space_data.use_pivot_point_align = True
        bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.space_data.use_pivot_point_align = False
    else:
        bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.context.space_data.pivot_point = piv


def align_graph(x, y, z, axisX, axisY, axisZ):
    bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)




# VIEW 3D #
class VIEW3D_Align_ALL_Axis(bpy.types.Operator):
    """alignment: xyz-axis"""
    bl_idname = "tp_ops.align_all_axis"
    bl_label = "Align x"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    itemsEnum = [
        ("ACTIVE_ELEMENT", "Active element", ""),
        ("MEDIAN_POINT", "Median point", ""),
        ("CURSOR", "3D Cursor", "")]
    regarding = EnumProperty(items=itemsEnum)

    def execute(self, context):
        align_XYZ(0,0,0,True,True,True)
        return {'FINISHED'}


class VIEW3D_Align_X(bpy.types.Operator):
    """alignment: x-axis"""
    bl_idname = "tp_ops.align_x"
    bl_label = "Align x"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    itemsEnum = [
        ("ACTIVE_ELEMENT", "Active element", ""),
        ("MEDIAN_POINT", "Median point", ""),
        ("CURSOR", "3D Cursor", "")]
    regarding = EnumProperty(items=itemsEnum)

    def execute(self, context):
        align_XYZ(0,1,1,True,False,False)
        return {'FINISHED'}


class VIEW3D_Align_Y(bpy.types.Operator):
    """alignment: y-axis"""
    bl_idname = "tp_ops.align_y"
    bl_label = "Align y"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    itemsEnum = [
        ("ACTIVE_ELEMENT", "Active element", ""),
        ("MEDIAN_POINT", "Median point", ""),
        ("CURSOR", "3D Cursor", "")]
    regarding = EnumProperty(items=itemsEnum)

    def execute(self, context):
        align_XYZ(1,0,1,False,True,False)
        return {'FINISHED'}


class VIEW3D_Align_Z(bpy.types.Operator):
    """alignment: z-axis"""
    bl_idname = "tp_ops.align_z"
    bl_label = "Align z"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    itemsEnum = [
        ("ACTIVE_ELEMENT", "Active element", ""),
        ("MEDIAN_POINT", "Median point", ""),
        ("CURSOR", "3D Cursor", "")]
    regarding = EnumProperty(items=itemsEnum)

    def execute(self, context):
        align_XYZ(1,1,0,False,False,True)
        return {'FINISHED'}



# GRAPH #
class GRAPH_Align_X(bpy.types.Operator):
    """alignment: x-axis"""
    bl_idname = "tp_ops.graph_align_x"
    bl_label = "Align x"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        align_graph(0,1,1,True,False,False)
        return {'FINISHED'}


class GRAPH_Align_Y(bpy.types.Operator):
    """alignment: y-axis"""
    bl_idname = "tp_ops.graph_align_y"
    bl_label = "Align y"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        align_graph(1,0,1,False,True,False)
        return {'FINISHED'}



# UV #
class UV_Align_X(bpy.types.Operator):
    """alignment: x-axis"""
    bl_idname = "tp_ops.uv_align_x"
    bl_label = "X Axis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        align_graph(0,1,1,True,False,False)
        return {'FINISHED'}


class UV_Align_Y(bpy.types.Operator):
    """alignment: y-axis"""
    bl_idname = "tp_ops.uv_align_y"
    bl_label = "Y Axis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        align_graph(1,0,1,False,True,False)
        return {'FINISHED'}



# NODE #
class NODE_align_x_slots(bpy.types.Operator):
    """alignment: x-axis"""
    bl_idname = "tp_ops.node_align_x"
    bl_label = "X Axis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        align_graph(0,1,1,True,False,False)
        return {'FINISHED'}


class NODE_align_y_slots(bpy.types.Operator):
    """alignment: y-axis"""
    bl_idname = "tp_ops.node_align_y"
    bl_label = "Y Axis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        align_graph(1,0,1,False,True,False)
        return {'FINISHED'}




# REGISTER #

def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()
















