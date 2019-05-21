# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *


class VIEW3D_OT_All_Gizmo(bpy.types.Operator):
    """Show all Manipulator"""
    bl_idname = "tpc_ot.manipulator_all"
    bl_label = "Show all Manipulator"
    bl_options = {'REGISTER', 'UNDO'}
    
    Global = bpy.props.BoolProperty(name="Global",  description="Transformation Orientation", default=True)    
    Local = bpy.props.BoolProperty(name="Local",  description="Transformation Orientation", default=False)    
    Normal = bpy.props.BoolProperty(name="Normal",  description="Transformation Orientation", default=False)    
    Gimbal = bpy.props.BoolProperty(name="Gimbal",  description="Transformation Orientation", default=False)    
    View = bpy.props.BoolProperty(name="View",  description="Transformation Orientation", default=False)    

    def draw(self, context):
        layout = self.layout.column(1)
        box = layout.box().column(1)

        row = box.column(1)         
        row.prop(self, 'Global')
        row.prop(self, 'Local')
        row.prop(self, 'Normal')
        row.prop(self, 'Gimbal')
        row.prop(self, 'View')

        box.separator()

    def execute(self, context):
   
        bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE', 'SCALE'}       

        for i in range(self.Global):
            bpy.context.space_data.transform_orientation = 'GLOBAL'

        for i in range(self.Local):
            bpy.context.space_data.transform_orientation = 'LOCAL'

        for i in range(self.Normal):
            bpy.context.space_data.transform_orientation = 'NORMAL'

        for i in range(self.Gimbal):
            bpy.context.space_data.transform_orientation = 'GIMBAL'

        for i in range(self.View):
            bpy.context.space_data.transform_orientation = 'VIEW'

        return {'FINISHED'}


class VIEW3D_OT_Move_Gizmo(bpy.types.Operator):
    """Show Move Manipulator"""
    bl_idname = "tpc_ot.manipulator_move"
    bl_label = "Show Move Manipulator"
    bl_options = {'REGISTER', 'UNDO'}
    
    Global = bpy.props.BoolProperty(name="Global",  description="Transformation Orientation", default=True)    
    Local = bpy.props.BoolProperty(name="Local",  description="Transformation Orientation", default=False)    
    Normal = bpy.props.BoolProperty(name="Normal",  description="Transformation Orientation", default=False)    
    Gimbal = bpy.props.BoolProperty(name="Gimbal",  description="Transformation Orientation", default=False)    
    View = bpy.props.BoolProperty(name="View",  description="Transformation Orientation", default=False)    

    def draw(self, context):
        layout = self.layout.column(1)
        box = layout.box().column(1)

        row = box.column(1)         
        row.prop(self, 'Global')
        row.prop(self, 'Local')
        row.prop(self, 'Normal')
        row.prop(self, 'Gimbal')
        row.prop(self, 'View')

        box.separator()

    def execute(self, context):

        bpy.context.space_data.transform_manipulators = {'TRANSLATE'}       

        for i in range(self.Global):
            bpy.context.space_data.transform_orientation = 'GLOBAL'

        for i in range(self.Local):
            bpy.context.space_data.transform_orientation = 'LOCAL'

        for i in range(self.Normal):
            bpy.context.space_data.transform_orientation = 'NORMAL'

        for i in range(self.Gimbal):
            bpy.context.space_data.transform_orientation = 'GIMBAL'

        for i in range(self.View):
            bpy.context.space_data.transform_orientation = 'VIEW'

        return {'FINISHED'}



class VIEW3D_OT_Rotate_Gizmo(bpy.types.Operator):
    """Show Rotate Manipulator"""
    bl_idname = "tpc_ot.manipulator_rotation"
    bl_label = "Show Rotate Manipulator"
    bl_options = {'REGISTER', 'UNDO'}
    
    Global = bpy.props.BoolProperty(name="Global",  description="Transformation Orientation", default=True)    
    Local = bpy.props.BoolProperty(name="Local",  description="Transformation Orientation", default=False)    
    Normal = bpy.props.BoolProperty(name="Normal",  description="Transformation Orientation", default=False)    
    Gimbal = bpy.props.BoolProperty(name="Gimbal",  description="Transformation Orientation", default=False)    
    View = bpy.props.BoolProperty(name="View",  description="Transformation Orientation", default=False)    

    def draw(self, context):
        layout = self.layout.column(1)
        box = layout.box().column(1)

        row = box.column(1)         
        row.prop(self, 'Global')
        row.prop(self, 'Local')
        row.prop(self, 'Normal')
        row.prop(self, 'Gimbal')
        row.prop(self, 'View')
        
        box.separator()
        
    def execute(self, context):

        bpy.context.space_data.transform_manipulators = {'ROTATE'}       

        for i in range(self.Global):
            bpy.context.space_data.transform_orientation = 'GLOBAL'

        for i in range(self.Local):
            bpy.context.space_data.transform_orientation = 'LOCAL'

        for i in range(self.Normal):
            bpy.context.space_data.transform_orientation = 'NORMAL'

        for i in range(self.Gimbal):
            bpy.context.space_data.transform_orientation = 'GIMBAL'

        for i in range(self.View):
            bpy.context.space_data.transform_orientation = 'VIEW'
        return {'FINISHED'}



class VIEW3D_OT_Scale_Gizmo(bpy.types.Operator):
    """Show Scale Manipulator"""
    bl_idname = "tpc_ot.manipulator_scale"
    bl_label = "Show Scale Manipulator"
    bl_options = {'REGISTER', 'UNDO'}
    
    Global = bpy.props.BoolProperty(name="Global",  description="Transformation Orientation", default=True)    
    Local = bpy.props.BoolProperty(name="Local",  description="Transformation Orientation", default=False)    
    Normal = bpy.props.BoolProperty(name="Normal",  description="Transformation Orientation", default=False)    
    Gimbal = bpy.props.BoolProperty(name="Gimbal",  description="Transformation Orientation", default=False)    
    View = bpy.props.BoolProperty(name="View",  description="Transformation Orientation", default=False)    

    def draw(self, context):
        layout = self.layout.column(1)
        box = layout.box().column(1)

        row = box.column(1)         
        row.prop(self, 'Global')
        row.prop(self, 'Local')
        row.prop(self, 'Normal')
        row.prop(self, 'Gimbal')
        row.prop(self, 'View')

        box.separator()

    def execute(self, context):

        bpy.context.space_data.transform_manipulators = {'SCALE'}       

        for i in range(self.Global):
            bpy.context.space_data.transform_orientation = 'GLOBAL'

        for i in range(self.Local):
            bpy.context.space_data.transform_orientation = 'LOCAL'

        for i in range(self.Normal):
            bpy.context.space_data.transform_orientation = 'NORMAL'

        for i in range(self.Gimbal):
            bpy.context.space_data.transform_orientation = 'GIMBAL'

        for i in range(self.View):
            bpy.context.space_data.transform_orientation = 'VIEW'

        return {'FINISHED'}



