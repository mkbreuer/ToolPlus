__author__ = "mkbreuer"
__status__ = "toolplus"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import*
from bpy.props import  *
from . icons.icons import load_icons

class View3D_TP_Axis_Planes_Menu(bpy.types.Menu):
    """add Cutter-Planes to selected mesh"""
    bl_label = "Axis Planes"
    bl_idname = "tp_menu.intersetion_planes"

    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        button_axis_x = icons.get("icon_axis_x")
        layout.operator("tp_ops.plane_x",text="Plane", icon_value=button_axis_x.icon_id)      
      
        button_axis_y = icons.get("icon_axis_y")
        layout.operator("tp_ops.plane_y",text="Plane", icon_value=button_axis_y.icon_id)       

        button_axis_z = icons.get("icon_axis_z")
        layout.operator("tp_ops.plane_z",text="Plane", icon_value=button_axis_z.icon_id) 



class View3D_TP_Boolean_2d_Union_Edm_Menu(bpy.types.Operator):
    """ 2d Union Edm [SHIFT+Numpad /]"""
    bl_idname = "tp_ops.boolean_2d_union_edm_menu"
    bl_label = "2d Union"

    def execute(self, context):
                
        bpy.ops.bpt.boolean_2d_union()
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Union_Edm_Menu(bpy.types.Operator):
    """Union [SHIFT+Numpad +]"""
    bl_idname = "tp_ops.bool_union_edm_menu"
    bl_label = "Union"

    def execute(self, context):
                
        bpy.ops.tp_ops.bool_union()  
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Difference_Edm_Menu(bpy.types.Operator):
    """Difference [SHIFT+Numpad -]"""
    bl_idname = "tp_ops.bool_difference_edm_menu"
    bl_label = "Difference"

    def execute(self, context):
        
        bpy.ops.tp_ops.bool_difference()     
        
        return {'FINISHED'}  


class View3D_TP_Boolean_Intersect_Edm_Menu(bpy.types.Operator):
    """Intersect [SHIFT+Numpad *]"""
    bl_idname = "tp_ops.bool_intersect_edm_menu"
    bl_label = "Intersect"

    def execute(self, context):
      
        bpy.ops.tp_ops.bool_intersect()   
        
        return {'FINISHED'} 




class View3D_TP_Boolean_Union(bpy.types.Operator):
    """Union [SHIFT+ +]"""
    bl_idname = "tp_ops.bool_union"
    bl_label = "Union"

    def execute(self, context):
        
        bpy.ops.mesh.intersect_boolean(operation='UNION')     
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Difference(bpy.types.Operator):
    """Difference [SHIFT+ -]"""
    bl_idname = "tp_ops.bool_difference"
    bl_label = "Difference"

    def execute(self, context):
        
        bpy.ops.mesh.intersect_boolean(operation='DIFFERENCE')      
        
        return {'FINISHED'}  


class View3D_TP_Boolean_Intersect(bpy.types.Operator):
    """Intersect [SHIFT+ *]"""
    bl_idname = "tp_ops.bool_intersect"
    bl_label = "Intersect"

    def execute(self, context):
       
        bpy.ops.mesh.intersect_boolean(operation='INTERSECT')      
        
        return {'FINISHED'} 


class View3D_TP_Plane_X(bpy.types.Operator):
    """Vertical Cutter-Plane along Normal X Axis"""
    bl_idname = "tp_ops.plane_x"
    bl_label = "X Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
       
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.view3d.snap_cursor_to_selected()        
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL')

        return {'FINISHED'}   


class View3D_TP_Plane_Y(bpy.types.Operator):
    """Vertical Cutter-Plane along Normal Y Axis """
    bl_idname = "tp_ops.plane_y"
    bl_label = "Y Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
       
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.view3d.snap_cursor_to_selected()    
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL')

        return {'FINISHED'}  
    

class View3D_TP_Plane_Z(bpy.types.Operator):
    """Horizontal Cutter-Plane along Normal Z Axis"""
    bl_idname = "tp_ops.plane_z"
    bl_label = "Z Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
      
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.view3d.snap_cursor_to_selected()    
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL')

        return {'FINISHED'}  
    
   

class View3D_TP_Boolean_Union_Obm_Menu(bpy.types.Operator):
    """Union [CTRL+Numpad+]"""
    bl_idname = "tp_ops.bool_union_obm_menu"
    bl_label = "Union"

    def execute(self, context):
        
        bpy.ops.btool.direct_union()   
       
        return {'FINISHED'}  


class View3D_TP_Boolean_Intersect_Obm_Menu(bpy.types.Operator):
    """Intersect [CTRL+Numpad*]"""
    bl_idname = "tp_ops.bool_intersect_obm_menu"
    bl_label = "Intersect"

    def execute(self, context):
       
        bpy.ops.btool.direct_intersect()     
        
        return {'FINISHED'} 


class View3D_TP_Boolean_Difference_Obm_Menu(bpy.types.Operator):
    """Difference [CTRL+Numpad-]"""
    bl_idname = "tp_ops.bool_difference_obm_menu"
    bl_label = "Difference"

    def execute(self, context):
        
        bpy.ops.btool.direct_difference()     
        
        return {'FINISHED'}  


class View3D_TP_Boolean_Rebool_Obm_Menu(bpy.types.Operator):
    """Rebool [CTRL+Numpad/]"""
    bl_idname = "tp_ops.bool_rebool_obm_menu"
    bl_label = "Rebool"

    def execute(self, context):
        
        bpy.ops.btool.direct_slice()     
        
        return {'FINISHED'} 


class View3D_TP_Origin_Obm(bpy.types.Operator):
    """set origin to selected / objectmode"""                 
    bl_idname = "tp_ops.origin_obm"          
    bl_label = "origin to selected"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        return {'FINISHED'}


class View3D_TP_Origin_Edm(bpy.types.Operator):
    """set origin to selected / editmode"""                 
    bl_idname = "tp_ops.origin_edm"          
    bl_label = "origin to selected"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class View3D_TP_Select_Linked(bpy.types.Operator):
    """select linked [CTRL+L]"""                 
    bl_idname = "tp_ops.select_linked_edm"          
    bl_label = "selecte linked"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.mesh.select_linked(delimit=set())

        return {'FINISHED'}



def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()






