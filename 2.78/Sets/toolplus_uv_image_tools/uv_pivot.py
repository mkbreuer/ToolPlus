__author__ = "mkbreuer"
__status__ = "toolplus"
__version__ = "1.0"
__date__ = "2017"

import bpy
from bpy import*


class VIEW3D_TP_Pivot_Box(bpy.types.Operator):
   """Set pivot point to Bounding Box"""
   bl_label = "Set pivot point to Bounding Box"
   bl_idname = "tp_ops.pivot_bounding_box"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CENTER'
       return {"FINISHED"} 

 
class VIEW3D_TP_Pivot_Cursor(bpy.types.Operator):
   """Set pivot point to 3D Cursor"""
   bl_label = "Set pivot point to 3D Cursor"
   bl_idname = "tp_ops.pivot_3d_cursor"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CURSOR'
       return {"FINISHED"} 


class VIEW3D_TP_Pivot_Median(bpy.types.Operator):
    """Set pivot point to Median Point"""
    bl_label = "Set pivot point to Median Point"
    bl_idname = "tp_ops.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}


class VIEW3D_TP_Pivot_Active(bpy.types.Operator):
   """Set pivot point to Active"""
   bl_label = "Set pivot point to Active"
   bl_idname = "tp_ops.pivot_active"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
       return {"FINISHED"} 


class VIEW3D_TP_Pivot_Individual(bpy.types.Operator):
    """Set pivot point to Individual"""
    bl_label = "Set pivot point to Individual Point"
    bl_idname = "tp_ops.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}   




def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__) 


if __name__ == "__main__":
    register()

