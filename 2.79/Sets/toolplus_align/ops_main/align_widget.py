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


# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import *
from bpy.types import WindowManager



class VIEW3D_TP_Display_All_Manipulator(bpy.types.Operator):
    """Show all Manipulator"""
    bl_idname = "tp_ops.manipulator_all"
    bl_label = "Show all Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):   
        bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE', 'SCALE'}       
        return {'FINISHED'}


class VIEW3D_TP_Display_Move_Manipulator(bpy.types.Operator):
    """Show Move Manipulator"""
    bl_idname = "tp_ops.manipulator_move"
    bl_label = "Show Move Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.transform_manipulators = {'TRANSLATE'}       
        return {'FINISHED'}


class VIEW3D_TP_Display_Rotate_Manipulator(bpy.types.Operator):
    """Show Rotate Manipulator"""
    bl_idname = "tp_ops.manipulator_rota"
    bl_label = "Show Rotate Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.transform_manipulators = {'ROTATE'}       
        return {'FINISHED'}


class VIEW3D_TP_Display_Scale_Manipulator(bpy.types.Operator):
    """Show Scale Manipulator"""
    bl_idname = "tp_ops.manipulator_scale"
    bl_label = "Show Scale Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.transform_manipulators = {'SCALE'}       
        return {'FINISHED'}



# REGISTER #
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 


