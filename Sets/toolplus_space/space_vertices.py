__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy, bmesh, os
from bpy import*
from bpy.props import *
from bpy.types import WindowManager
from bpy.props import (StringProperty, EnumProperty)



#####  Align Mesh Vertices  ####
def align_function(axis_x, axis_y, axis_z, axis_n, manipul):

    if axis_x == True:
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    if axis_y == True:
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    if axis_z == True:
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
      
    if axis_n == True:
        bpy.ops.view3d.pivot_active()
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
    if manipul == True:
        bpy.context.space_data.transform_orientation = 'NORMAL'
    else:
        bpy.context.space_data.transform_orientation = 'GLOBAL'


class View3D_TP_Align_Vertices(bpy.types.Operator):
    """Align Vertices"""
    bl_label = "Align Mesh"
    bl_idname = "tp_ops.align_vertices"
    bl_options = {'REGISTER', 'UNDO'}
    
    axis_x = BoolProperty (name = "X-Axis", default= False, description= "")
    axis_y = BoolProperty (name = "Y-Axis", default= False, description= "")
    axis_z = BoolProperty (name = "Z-Axis", default= False, description= "")
    axis_n = BoolProperty (name = "N-Axis", default= False, description= "")
    manipul = BoolProperty (name = "N-Widget", default= False, description= "Switch Orientation Widget / Global <> Normal")

    def draw(self, context):
        layout = self.layout
       
        box = layout.box().column(1)
        
        row = box.column(1)
        row.prop(self, 'axis_x', icon = "TRIA_RIGHT")
        row.prop(self, 'axis_y', icon = "TRIA_DOWN")
        row.prop(self, 'axis_z', icon = "SPACE3")
   
        row.separator()

        row.prop(self, 'axis_n', icon = "BLANK1")        
        row.prop(self, 'manipul', icon = "BLANK1") 
        
        row.separator()
        
        row.operator('wm.operator_defaults', text="Reset(F6)", icon ="BLANK1")                  

        box.separator()

    def execute(self, context):
        align_function(self.axis_x, self.axis_y, self.axis_z, self.axis_n, self.manipul)                               
        return {'FINISHED'} 
    
    def invoke(self, context, event):
        align_function(self.axis_x, self.axis_y, self.axis_z, self.axis_n, self.manipul)          
        #return context.window_manager.invoke_props_popup(self, event)  
        return context.window_manager.invoke_props_dialog(self, width = 100)  


class View3D_TP_Align_X(bpy.types.Operator):
    """Align selected to X-Axis / depend on pivot point"""
    bl_label = "align x"
    bl_idname = "tp_ops.face_align_x"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 

class View3D_TP_Align_Y(bpy.types.Operator):
    """Align selected to Y-Axis / depend on pivot point"""
    bl_label = "align y"
    bl_idname = "tp_ops.face_align_y"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}

class View3D_TP_Align_Z(bpy.types.Operator):
    """Align selected to Z-Axis / depend on pivot point"""
    bl_label = "align z"
    bl_idname = "tp_ops.face_align_z"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}    


class View3D_TP_Align_XY(bpy.types.Operator):
    """Align selected to XY-Axis / depend on pivot point"""
    bl_label = "align xy"
    bl_idname = "tp_ops.face_align_xy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 

class View3D_TP_Align_XZ(bpy.types.Operator):
    """Align selected to XZ-Axis / depend on pivot point"""
    bl_label = "align xz"
    bl_idname = "tp_ops.face_align_xz"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 1, 0), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}

class View3D_TP_Align_YZ(bpy.types.Operator):
    """Align selected to yz-Axis / depend on pivot point"""
    bl_label = "align yz"
    bl_idname = "tp_ops.face_align_yz"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 0, 0), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 


class View3D_TP_Align_to_Normal(bpy.types.Operator):
    """Align selected to active selected in normal-z-direction / depend on pivot point"""
    bl_idname = "tp_ops.align_to_normal"
    bl_label = "Normal Align"
    bl_options = {'REGISTER', 'UNDO'}

    w_normal = bpy.props.BoolProperty(name="Normal Widget",  description="Switch Orientation Widget / Normal <> Global", default=False) 
    w_global = bpy.props.BoolProperty(name="Global Widget",  description="Switch Orientation Widget / Global <> Normal", default=True) 

    def draw(self, layout):
        layout = self.layout
        
        box = layout.box().column(1)
        
        row  = box.row(1)       
        row.label("Orientation Widget")
        
        row  = box.row(1)
        if self.w_normal == False:
            row.prop(self, 'w_normal', text="Normal <> Global")
        else:            
            row.prop(self, 'w_global', text="Global <> Normal")
        
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    
        for i in range(self.w_normal):            
            bpy.context.space_data.transform_orientation = 'NORMAL'
        
        for i in range(self.w_global):  
            bpy.context.space_data.transform_orientation = 'GLOBAL'

        return {'FINISHED'}


def register():
    
    bpy.utils.register_module(__name__)

def unregister():
    
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

