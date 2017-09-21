bl_info = {
    "name": "TP Bevel Curves",
    "author": "MKB",
    "version": (0, 1),
    "blender": (2, 78, 0),
    "location": "View3D > Add Menu > Curve",
    "description": "Add extra curve object types with bevel",
    "warning": "",
    "wiki_url": "",
    "category": "T+"}


import bpy
from bpy import*
from bpy.props import *


class View3D_TP_Beveled_Curve(bpy.types.Operator):
    """Add beveled Curve"""
    bl_idname = "tp_ops.beveled_curve"
    bl_label = "Add beveled Curve"
    bl_options = {'REGISTER', 'UNDO'}

    bpy.types.Scene.curve_type = bpy.props.EnumProperty(
        items=[("tp_bezier"     ,"Bezier Curve"     ,"Bezier Curve"),
               ("tp_circle"     ,"Circle Curve"     ,"Circle Curve"),
               ("tp_nurbs"      ,"Nurbs Curve"      ,"Nurbs Curve"),
               ("tp_ncircle"    ,"Nurbs Circle"     ,"Nurbs Circle")],
               name = "Type",
               default = "tp_bezier",    
               description = "add geometry")

    def execute(self, context):
        
        if context.scene.curve_type == "tp_bezier":   
            bpy.ops.curve.primitive_bezier_curve_add()

        if context.scene.curve_type == "tp_circle":   
            bpy.ops.curve.primitive_bezier_circle_add()        
       
        if context.scene.curve_type == "tp_nurbs":   
            bpy.ops.curve.primitive_nurbs_curve_add()

        if context.scene.curve_type == "tp_ncircle":   
            bpy.ops.curve.primitive_nurbs_circle_add()     

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)        

        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 8
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2         
             
        return {'FINISHED'}
    
    

class View3D_TP_Wire_Curve(bpy.types.Operator):
    """Add wired Curve"""
    bl_idname = "tp_ops.wired_curve"
    bl_label = "Add wired Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        active_wire = bpy.context.object.show_wire 

        if active_wire == True:
            bpy.context.object.show_wire = False             
        else:                       
            bpy.context.object.show_wire = True

        return {'FINISHED'}



class View3D_TP_Bevel(bpy.types.Operator):
    """Bevel Setup"""
    bl_idname = "tp_ops.bevel_set"
    bl_label = "Bevel Setup"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        return {'FINISHED'}    
    
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=350)


    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'     
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box().column(1)         
        
        if context.mode == 'OBJECT': 
            row = box.row(1)
            row.label("", icon='MOD_CURVE') 
            row.prop(context.scene, "curve_type", text="") 
            row.operator("tp_ops.beveled_curve", text="Add Curve")                          
                           
            box.separator()
        
        row = box.row(1)                                                                                                                                                                                                            
        
        active_wire = bpy.context.object.show_wire 
        row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')                                                          
        row.prop(context.object.data, "bevel_depth", text="Bevel Radius")
        
        if active_wire == True:
            row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
        else:                       
            row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID') 
                    
        row = box.row(1)
        row.prop(context.object.data, "resolution_u", text="Rings")          
        row.prop(context.object.data, "bevel_resolution", text="Loops")

        row = box.row(1)
        row.prop(context.object.data, "offset")
        row.prop(context.object.data, "extrude","Height")
                
        if context.object.data.splines.active.type == 'NURBS':

            box.separator()
            
            row = box.row(1)
            row.prop(context.object.data.splines.active, "order_u", text="U Order")

        box.separator() 

        row = box.row(1)
        row.prop(context.object.data, "fill_mode", text="")   
        active_bevel = bpy.context.object.data.bevel_depth            
        if active_bevel == 0.0:              
            row.operator("tp_ops.enable_bevel", text="Bevel on", icon='MOD_WARP')
        else:   
            row.operator("tp_ops.enable_bevel", text="Bevel off", icon='MOD_WARP')      
            
        box.separator() 




    def check(self, context):
        return True






class Purge_Curve(bpy.types.Operator):
    '''Purge orphaned curve'''
    bl_idname="purge.unused_curve_data"
    bl_label="Purge Mesh"
    
    def execute(self, context):

        target_coll = eval("bpy.data.curves")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}



class View3D_TP_Enable_Bevel(bpy.types.Operator):
    """Add enable Bevel"""
    bl_idname = "tp_ops.enable_bevel"
    bl_label = "Add enable Bevel"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
         
        active_bevel = bpy.context.object.data.bevel_depth
      
        if active_bevel == 0.0:              
            bpy.context.object.data.fill_mode = 'FULL'
            bpy.context.object.data.bevel_depth = 0.2   

            #bpy.context.object.data.bevel_resolution = 8           
            #bpy.context.object.data.resolution_u = 10    

        else:                   
            bpy.context.object.data.fill_mode = 'HALF'
            #bpy.context.object.data.bevel_resolution = 0
            #bpy.context.object.data.resolution_u = 0
            bpy.context.object.data.bevel_depth = 0.0
            bpy.context.object.data.extrude = 0
            bpy.context.object.data.offset = 0

        return {'FINISHED'}



class View3D_TP_Quader_Curve(bpy.types.Operator):
    """select 2 Vertices and execute"""
    bl_idname = "tp_ops.quader_curve"
    bl_label = "A full Bevel Quader Curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='TOGGLE')
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.curve.cyclic_toggle()   

        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_depth = 1.5
        bpy.context.object.data.bevel_resolution = 6
        bpy.context.object.show_wire = True

        return {'FINISHED'} 
    


class View3D_TP_Half_Circle_Curve(bpy.types.Operator):
    """select 1 Start-Point-Vertex and execute"""
    bl_idname = "tp_ops.half_curve"
    bl_label = "A full Bevel Quader CircleCurve"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        bpy.ops.curve.surfsk_first_points()
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.cyclic_toggle()
        
        bpy.context.object.data.fill_mode = 'FULL'            
        bpy.context.object.data.bevel_depth = 1.5
        bpy.context.object.data.bevel_resolution = 6
        bpy.context.object.show_wire = True

        return {'FINISHED'}




###from curvetools2
class View3D_TP_Curve_Origin_Start(bpy.types.Operator):
    """Origin to Start Point"""
    bl_idname = "tp_ops.origin_start_point"
    bl_label = "Origin to Start Point"
            
    def execute(self, context):
        blCurve = context.active_object
        blSpline = blCurve.data.splines[0]
        newOrigin = blCurve.matrix_world * blSpline.bezier_points[0].co
    
        origOrigin = bpy.context.scene.cursor_location.copy()

        bpy.context.scene.cursor_location = newOrigin
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor_location = origOrigin

        return {'FINISHED'}

    

#add a menu to ui
def draw_beveled_curve(self, context):
    layout = self.layout
    
    col = layout.column()
    layout.separator() 

    if context.mode == 'OBJECT':      
        layout.operator("tp_ops.bevel_set","Beveled Setup", icon = "MOD_CURVE")
            
    show = bpy.context.object.data.dimensions
    if show == '3D':
         
        active_bevel = bpy.context.object.data.bevel_depth            
        if active_bevel == 0.0:              
            layout.operator("tp_ops.enable_bevel", text="CurveBevel on", icon='MOD_WARP')
        else:   
            layout.operator("tp_ops.enable_bevel", text="CurveBevel off", icon='MOD_WARP')  




def register():   
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
 

 
if __name__ == "__main__":
    register()




















