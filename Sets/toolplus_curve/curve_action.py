# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****

__author__ = "mkbreuer"
__status__ = "toolplus"
__version__ = "1.0"
__date__ = "2016"

import bpy
from bpy import*
  

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


class VIEW3D_TP_pivotBox(bpy.types.Operator):
   """Set pivot point to Bounding Box"""
   bl_label = "Set pivot point to Bounding Box"
   bl_idname = "view3d.pivot_bounding_box"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
       return {"FINISHED"} 

 
class VIEW3D_TP_pivotCursor(bpy.types.Operator):
   """Set pivot point to 3D Cursor"""
   bl_label = "Set pivot point to 3D Cursor"
   bl_idname = "view3d.pivot_3d_cursor"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CURSOR'
       return {"FINISHED"} 


class VIEW3D_TP_pivotMedian(bpy.types.Operator):
    """Set pivot point to Median Point"""
    bl_label = "Set pivot point to Median Point"
    bl_idname = "view3d.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}


class VIEW3D_TP_pivotActive(bpy.types.Operator):
   """Set pivot point to Active"""
   bl_label = "Set pivot point to Active"
   bl_idname = "view3d.pivot_active"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
       return {"FINISHED"} 


class VIEW3D_TP_pivotIndividual(bpy.types.Operator):
    """Set pivot point to Individual"""
    bl_label = "Set pivot point to Individual Point"
    bl_idname = "view3d.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}   


class VIEW3D_TP_ThroughSelected(bpy.types.Operator):
    """cycle through selected objects"""
    bl_idname = "to_ops.cycle_through"
    bl_label = "Cycle Through"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        selection = bpy.context.selected_objects

        if not bpy.context.active_object.select:
            if len(selection):
                bpy.context.scene.objects.active = selection[0]
        else:
            for i, o in enumerate(selection):
                if o == bpy.context.active_object:
                    bpy.context.scene.objects.active = selection[(i+1) % len(selection)]
                    break
        
        return {'FINISHED'}
        

class VIEW3D_TP_Freeze_Selected(bpy.types.Operator):
    """freeze selection"""
    bl_idname = "to_ops.freeze"
    bl_label = "Freeze"
    bl_options = {'REGISTER', 'UNDO'}    

    def execute(self, context):
        
        for obj in bpy.context.selected_objects:
    
            bpy.context.scene.objects.active = obj
    
            bpy.context.object.hide_select = True                

        return{'FINISHED'}


class VIEW3D_TP_UnFreeze_Selected(bpy.types.Operator):
    """unfreeze selection"""    
    bl_idname = "to_ops.unfreeze"
    bl_label = "UnFreeze"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        for obj in bpy.context.selected_objects:
    
             bpy.context.object.hide_select = False
             bpy.context.scene.objects.active = obj        

        return{'FINISHED'} 





def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()




