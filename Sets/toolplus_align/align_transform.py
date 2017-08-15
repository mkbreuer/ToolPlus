import bpy, bmesh
from bpy import *
from mathutils import Vector 


class VIEW_TP_Space_LOBAL(bpy.types.Operator):
    """Transform Orientation Global"""
    bl_idname = "tp_ops.space_global"
    bl_label = "Transform Orientation GLOBAL"
    bl_options = {'REGISTER'}

    def execute(self, context):

        bpy.context.space_data.transform_orientation = 'GLOBAL'
        return {'FINISHED'}
    

class VIEW_TP_Space_LOCAL(bpy.types.Operator):
    """Transform Orientation LOCAL"""
    bl_idname = "tp_ops.space_local"
    bl_label = "Transform Orientation LOCAL"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'LOCAL'
        return {'FINISHED'}


class VIEW_TP_Space_NORMAL(bpy.types.Operator):
    """Transform Orientation NORMAL"""
    bl_idname = "tp_ops.space_normal"
    bl_label = "Transform Orientation NORMAL"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'NORMAL'
        return {'FINISHED'}
    
class VIEW_TP_Space_GIMBAL(bpy.types.Operator):
    """Transform Orientation GIMBAL"""
    bl_idname = "tp_ops.space_gimbal"
    bl_label = "Transform Orientation GIMBAL"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'GIMBAL'
        return {'FINISHED'}


class VIEW_TP_Space_VIEW(bpy.types.Operator):
    """Transform Orientation VIEW"""
    bl_idname = "tp_ops.space_view"
    bl_label = "Transform Orientation VIEW"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'VIEW'
        return {'FINISHED'}




def register():
    
    bpy.utils.register_module(__name__)        

def unregister():
    
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register() 	




        



































