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
  

class VIEW3D_TP_OpenCurve(bpy.types.Operator):
    """Open Curve"""
    bl_idname = "curve.open_circle"
    bl_label = "Open Curve"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.cyclic_toggle()     
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
    

class VIEW3D_TP_toPoly(bpy.types.Operator):
    """Curve to Poly Spline"""
    bl_idname = "curve.to_poly"
    bl_label = "Curve to Poly Spline"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.spline_type_set(type='POLY')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_toBezier(bpy.types.Operator):
    """Curve to Bezier Spline"""
    bl_idname = "curve.to_bezier"
    bl_label = "Curve to Bezier Spline"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.spline_type_set(type='BEZIER')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_toNurbs(bpy.types.Operator):
    """Curve to Nurbs Spline"""
    bl_idname = "curve.to_nurbs"
    bl_label = "Curve to Nurbs Spline"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.spline_type_set(type='NURBS')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_toAutomatic(bpy.types.Operator):
    """Handle to Automatic Rounded Type"""
    bl_idname = "curve.handle_to_automatic"
    bl_label = "Handle to Automatic Rounded Type"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.handle_type_set(type='AUTOMATIC')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_toVector(bpy.types.Operator):
    """Handle to Vector Type"""
    bl_idname = "curve.handle_to_vector"
    bl_label = "Handle to Vector Type"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.handle_type_set(type='VECTOR')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_toAligned(bpy.types.Operator):
    """Handle to Aligned Type"""
    bl_idname = "curve.handle_to_aligned"
    bl_label = "Handle to Aligned Type"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.handle_type_set(type='ALIGNED')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_toFree(bpy.types.Operator):
    """Handle to Free Type"""
    bl_idname = "curve.handle_to_free"
    bl_label = "Handle to Free Type"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.handle_type_set(type='FREE_ALIGN')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_SmoothCurve(bpy.types.Operator):
    """Smooth Curve Spline"""
    bl_idname = "curve.smoothspline"
    bl_label = "Smooth Curve Spline"

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.smooth()
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_CurveDirection(bpy.types.Operator):
    """switch curve direction > only BEZIER"""                 
    bl_idname = "curve.switch_direction_obm"        
    bl_label = "Curve Direction"                  
    #bl_options = {'REGISTER', 'UNDO'}  
        
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.switch_direction()
        bpy.ops.object.editmode_toggle()        
        bpy.ops.curvetools2.operatororigintospline0start()        
        return {'FINISHED'}


class VIEW3D_TP_ConvertBezier(bpy.types.Operator):
    """Convert to Curve with Bezièr Spline Typ"""
    bl_idname = "curve.convert_bezier"
    bl_label = "Convert to Curve with Bezièr Spline Typ"

    def execute(self, context):
        bpy.ops.object.convert(target='CURVE')
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.spline_type_set(type='BEZIER')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class VIEW3D_TP_Purge_Curves(bpy.types.Operator):
    '''Purge orphaned curves'''
    bl_idname="tp_purge.unused_curves_data"
    bl_label="Purge Curves"
    
    def execute(self, context):
        
        target_coll = eval("bpy.data.curves")
      
        num_deleted = len([x for x in target_coll if x.users==0])
        num_kept = len([x for x in target_coll if x.users==1])
      
        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        msg = "Curves: %d removed & %d kept" % (num_deleted, num_kept)
        self.report( { 'INFO' }, msg  )
        return {'FINISHED'}


class VIEW3D_TP_Curve_Origin_First(bpy.types.Operator):
    """origin to first point"""
    bl_idname = "tp_ops.origin_first"
    bl_label = "Origin First"
    bl_options = {'REGISTER', 'UNDO'}
            
    def execute(self, context):
        

        activeObj = bpy.context.active_object
        oldMode = activeObj.mode    

        bpy.ops.object.mode_set(mode='OBJECT')

        active_curve = context.active_object
        selected_spline = active_curve.data.splines[0]

        new_origin = active_curve.matrix_world * selected_spline.bezier_points[0].co
    
        loc_origin = bpy.context.scene.cursor_location.copy()

        bpy.context.scene.cursor_location = new_origin
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        
        bpy.context.scene.cursor_location = loc_origin

        bpy.ops.object.mode_set(mode=oldMode)
        
        return {'FINISHED'}




class VIEW3D_TP_Optimize_Curve(bpy.types.Operator):
    """recalculate normals, purge unused orphaned Curve"""
    bl_idname = "tp_ops.optimize_curve"
    bl_label = "Optimize Curve"
    bl_options = {'REGISTER', 'UNDO'}  

    smooth = bpy.props.BoolProperty(name="Smooth",  description="Smooth Curve", default=False)                   
    direction = bpy.props.BoolProperty(name=" Direction",  description="Switch Direction", default=False) 
    rec = bpy.props.BoolProperty(name="Recal. Normals ",  description="Recalculate Normals", default=False) 
    purge = bpy.props.BoolProperty(name="Purge Orphan",  description="Purge unused orphaned Mesh", default=False) 

    def draw(self, context):
        layout = self.layout.column(1)
        
        box = layout.box().column(1)
        
        row = box.column(1)
        row.scale_y = 1.2
        row.prop(self, 'smooth', text="Smooth", icon ="SPHERECURVE")  
        row.prop(self, 'direction', text="Direction", icon ="FILE_REFRESH")         
        row.prop(self, 'rec', text="Recal. Normals", icon ="SNAP_NORMAL")   
        row.prop(self, 'purge', text="Purge Orphan", icon ="CURVE_DATA")  
        
        box.separator()

    def execute(self, context):
        #print(self)
        #self.report({'INFO'}, "Optimize")                                 

        if context.mode == 'OBJECT':

            bpy.ops.object.editmode_toggle()
     
            bpy.ops.curve.select_all(action='SELECT')

            for i in range(self.direction):   
                bpy.ops.curve.switch_direction()            

            for i in range(self.rec):   
                bpy.ops.curve.normals_make_consistent()

            for i in range(self.smooth):   
                bpy.ops.curve.smooth()

            bpy.ops.object.editmode_toggle()


        if context.object.mode == 'EDIT_CURVE':

            for i in range(self.direction):   
                bpy.ops.curve.switch_direction()            

            for i in range(self.rec):   
                bpy.ops.curve.normals_make_consistent()

            for i in range(self.smooth):   
                bpy.ops.curve.smooth()

        for i in range(self.purge):   
            bpy.ops.purge.unused_curve_data()    

        return {'FINISHED'}

    def invoke(self, context, event):
        self.smooth
        self.direction
        self.rec
        self.purge
        return context.window_manager.invoke_props_dialog(self, width = 125) 












# MODAL EXAMPLE
#class VIEW3D_TP_Curve_Tilt(bpy.types.Operator):
#    bl_idname = 'tp_ops.tilt_slider'
#    bl_label = 'Tilt'
#    bl_options = {'REGISTER', 'UNDO'}

#    bpy.types.Scene.tilt = bpy.props.FloatProperty(name='Tilt', default=0.00, min=0.00, max=360, subtype='ANGLE')
#    
#    def modal(self, context, event):
#        
#        scene = bpy.context.scene   
#                
#        if event.type == 'MOUSEMOVE':
#                
#                delta = scene.tilt - event.mouse_x
#                

#                        
#                #bpy.ops.transform.tilt(value=self.offset)
#                bpy.ops.transform.tilt(value=scene.tilt)

#        
#        elif event.type == 'LEFTMOUSE':
#                return {'FINISHED'}

#        elif event.type in {'RIGHTMOUSE', 'ESC'}:
#            bpy.ops.ed.undo()
#            return {'CANCELLED'}

#        return {'RUNNING_MODAL'}

#    def invoke(self, context, event):
#               
#        if context.object:
#            scene = bpy.context.scene        
#            scene.tilt = event.mouse_x
#            context.window_manager.modal_handler_add(self)
#            return {'RUNNING_MODAL'}
#                

#        else:
#            self.report({'WARNING'}, "No active object, could not finish")
#            return {'CANCELLED'}




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()