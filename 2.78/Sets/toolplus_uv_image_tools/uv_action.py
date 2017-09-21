__author__ = "mkbreuer"
__status__ = "toolplus"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import* 

        
class VIEW3D_TP_UV_Rotated_A(bpy.types.Operator):
    """uv rotate 90°"""
    bl_label = "UV Rotate 90°"
    bl_idname = "uv.rotatednine"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.ops.transform.rotate(value=1.5708, axis=(-0, -0, -1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.61051)

        return {"FINISHED"}


class VIEW3D_TP_UV_Rotated_B(bpy.types.Operator):
    """uv rotate -90°"""
    bl_label = "UV Rotate -90°"
    bl_idname = "uv.rotatednineminus"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.ops.transform.rotate(value=-1.5708, axis=(-0, -0, -1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.61051)

        return {"FINISHED"}


class VIEW3D_TP_UV_Rotated_C(bpy.types.Operator):
    """uv rotate 180°"""
    bl_label = "UV Rotate 180°"
    bl_idname = "uv.rotateoneeighty"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.ops.transform.rotate(value=-3.14159, axis=(-0, -0, -1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}
    
    
class VIEW3D_TP_Snap_Vertex(bpy.types.Operator):
    """snap vertex"""
    bl_label = "Snap Vertex"
    bl_idname = "tp_ops.snap_vertex"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.context.scene.tool_settings.snap_uv_element = 'VERTEX'

        return {"FINISHED"}


class VIEW3D_TP_Snap_Increment(bpy.types.Operator):
    """snap increment"""
    bl_label = "Snap Increment"
    bl_idname = "tp_ops.snap_increment"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.context.scene.tool_settings.snap_uv_element = 'INCREMENT'

        return {"FINISHED"}    


class VIEW3D_TP_Mode_Vertex(bpy.types.Operator):
    """vertex mode"""
    bl_label = "Vertex Mode"
    bl_idname = "tp_ops.mode_vertex"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.context.scene.tool_settings.uv_select_mode = 'VERTEX'

        return {"FINISHED"}    


class VIEW3D_TP_Mode_Edge(bpy.types.Operator):
    """edge mode"""
    bl_label = "Edge Mode"
    bl_idname = "tp_ops.mode_edge"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.context.scene.tool_settings.uv_select_mode = 'EDGE'

        return {"FINISHED"}  


class VIEW3D_TP_Mode_Face(bpy.types.Operator):
    """face mode"""
    bl_label = "Face Mode"
    bl_idname = "tp_ops.mode_face"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.context.scene.tool_settings.uv_select_mode = 'FACE'

        return {"FINISHED"}  


class VIEW3D_TP_Mode_Island(bpy.types.Operator):
    """island mode"""
    bl_label = "Island Mode"
    bl_idname = "tp_ops.mode_island"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.context.scene.tool_settings.uv_select_mode = 'ISLAND'

        return {"FINISHED"}  



def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__) 


if __name__ == "__main__":
    register()

    
