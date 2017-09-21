__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *


class VIEW3D_TP_FAKE_OPS(bpy.types.Operator):
    """do nothing"""
    bl_idname = "tp_ops.fake_ops"
    bl_label = "Do Nothing"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print
        return {'FINISHED'}

    
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


