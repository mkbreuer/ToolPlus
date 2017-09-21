__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *

        #scene = bpy.context.scene 
        #selected = bpy.context.selected_objects 

        #for obj in selected: 


class View3D_TP_Origin_EditCenter(bpy.types.Operator):
    '''Set Origin to Center / Editmode'''
    bl_idname = "tp_ops.origin_set_editcenter"
    bl_label = "Set Origin to Center / Editmode"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.mesh.select_all(action='SELECT') 
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')               
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='DESELECT') 
        
        return{'FINISHED'}  
    

class View3D_TP_OriginObm(bpy.types.Operator):
    """set origin to selected / switch to objectmode"""                 
    bl_idname = "tp_ops.origin_obm"          
    bl_label = "origin to selected / in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
    

class View3D_TP_OriginEdm(bpy.types.Operator):
    """set origin to selected / stay in editmode"""                 
    bl_idname = "tp_ops.origin_edm"          
    bl_label = "origin to selected in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class View3D_TP_Origin_Edm_Cursor(bpy.types.Operator):
    """set origin to cursor / stay in editmode"""                 
    bl_idname = "tp_ops.origin_cursor_edm"          
    bl_label = "origin to cursor in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class View3D_TP_Origin_Obm_Cursor(bpy.types.Operator):
    """set origin to cursor / switch to objectmode"""                 
    bl_idname = "tp_ops.origin_cursor_obm"          
    bl_label = "origin to cursor in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}   



class View3D_TP_Origin_Center(bpy.types.Operator):
    '''Set Origin to Center'''
    bl_idname = "tp_ops.origin_set_center"
    bl_label = "Origin to Center"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        if context.mode == 'OBJECT':

            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)                 

        else:   
            bpy.ops.object.editmode_toggle()
            
            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
            
            bpy.ops.object.editmode_toggle()

        return{'FINISHED'}


class View3D_TP_Origin_Cursor(bpy.types.Operator):
    '''Set Origin to Cursor'''
    bl_idname = "tp_ops.origin_set_cursor"
    bl_label = "Origin to Cursor"
    bl_options = {"REGISTER", 'UNDO'}   

    set_cursor = bpy.props.BoolProperty(name="Set 3D Cursor",  description="set pivot to 3d cursor", default = False)   
    
    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        
        for i in range(self.set_cursor):
        
            bpy.context.space_data.pivot_point = 'CURSOR'

        return{'FINISHED'}

 
class View3D_TP_Origin_Mass(bpy.types.Operator):
    '''Set Origin to Center of Mass'''
    bl_idname = "tp_ops.origin_set_mass"
    bl_label = "Origin to Center of Mass"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        
        return{'FINISHED'}


class View3D_TP_Origin_toMesh(bpy.types.Operator):
    '''Set Origin to Mesh'''
    bl_idname = "tp_ops.origin_tomesh"
    bl_label = "Origin to Mesh"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        return{'FINISHED'}    
    
    
class View3D_TP_Origin_Meshto(bpy.types.Operator):
    '''Set Mesh to Origin'''
    bl_idname = "tp_ops.origin_meshto"
    bl_label = "Mesh to Origin"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        
        return{'FINISHED'}  




def register():

    bpy.utils.register_module(__name__)
 
    
def unregister():

    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()




















