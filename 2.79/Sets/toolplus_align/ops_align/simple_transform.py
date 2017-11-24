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


import bpy
from bpy import *
from bpy.props import *


class VIEW3D_Align_Transform_X(bpy.types.Operator):
    """Align Transform X Axis"""
    bl_idname = "tp_ops.align_transform_x"
    bl_label = "Align Transform X Axis"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("tp_loc"        ,"Location"     ,"Location"),
               ("tp_rot"        ,"Rotation"     ,"Rotation"),
               ("tp_scal"       ,"Scale"        ,"Scale")],
               name = "TP-Axis",
               default = "tp_loc",    
               description = "switch transformation type")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True) 

    def execute(self, context):
        
        if self.tp_axis == "tp_loc":

            bpy.ops.object.align_location_x()               

        elif self.tp_axis == "tp_rot":

            bpy.ops.object.align_rotation_x()

        elif self.tp_axis == "tp_scal":

            bpy.ops.object.align_objects_scale_x()       

        return {'FINISHED'}




class VIEW3D_Align_Transform_Y(bpy.types.Operator):
    """Align Transform Y Axis"""
    bl_idname = "tp_ops.align_transform_y"
    bl_label = "Align Transform Y Axis"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("tp_loc"        ,"Location"     ,"Location"),
               ("tp_rot"        ,"Rotation"     ,"Rotation"),
               ("tp_scal"       ,"Scale"        ,"Scale")],
               name = "TP-Axis",
               default = "tp_loc",    
               description = "switch transformation type")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True) 

    def execute(self, context):
        
        if self.tp_axis == "tp_loc":

            bpy.ops.object.align_location_y()               

        elif self.tp_axis == "tp_rot":

            bpy.ops.object.align_rotation_y()

        elif self.tp_axis == "tp_scal":

            bpy.ops.object.align_objects_scale_y()       

        return {'FINISHED'}



class VIEW3D_Align_Transform_Z(bpy.types.Operator):
    """Align Transform Z Axis"""
    bl_idname = "tp_ops.align_transform_z"
    bl_label = "Align Transform Z Axis"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("tp_loc"        ,"Location"     ,"Location"),
               ("tp_rot"        ,"Rotation"     ,"Rotation"),
               ("tp_scal"       ,"Scale"        ,"Scale")],
               name = "TP-Axis",
               default = "tp_loc",    
               description = "switch transformation type")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True) 

    def execute(self, context):
        
        if self.tp_axis == "tp_loc":

            bpy.ops.object.align_location_z()               

        elif self.tp_axis == "tp_rot":

            bpy.ops.object.align_rotation_z()

        elif self.tp_axis == "tp_scal":

            bpy.ops.object.align_objects_scale_z()       

        return {'FINISHED'}










class VIEW3D_Align_Transform_Xy(bpy.types.Operator):
    """Align Transform Xy Axis"""
    bl_idname = "tp_ops.align_transform_xy"
    bl_label = "Align Transform Xy Axis"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("tp_loc"        ,"Location"     ,"Location"),
               ("tp_rot"        ,"Rotation"     ,"Rotation"),
               ("tp_scal"       ,"Scale"        ,"Scale")],
               name = "TP-Axis",
               default = "tp_loc",    
               description = "switch transformation type")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True) 

    def execute(self, context):
        
        if self.tp_axis == "tp_loc":

            bpy.ops.object.align_location_x()               
            bpy.ops.object.align_location_y()               

        elif self.tp_axis == "tp_rot":

            bpy.ops.object.align_rotation_x()
            bpy.ops.object.align_rotation_y()

        elif self.tp_axis == "tp_scal":

            bpy.ops.object.align_objects_scale_x()       
            bpy.ops.object.align_objects_scale_y()       

        return {'FINISHED'}



class VIEW3D_Align_Transform_Zx(bpy.types.Operator):
    """Align Transform Zx Axis"""
    bl_idname = "tp_ops.align_transform_zx"
    bl_label = "Align Transform Zx Axis"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("tp_loc"        ,"Location"     ,"Location"),
               ("tp_rot"        ,"Rotation"     ,"Rotation"),
               ("tp_scal"       ,"Scale"        ,"Scale")],
               name = "TP-Axis",
               default = "tp_loc",    
               description = "switch transformation type")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True) 

    def execute(self, context):
        
        if self.tp_axis == "tp_loc":

            bpy.ops.object.align_location_z()               
            bpy.ops.object.align_location_x()               

        elif self.tp_axis == "tp_rot":

            bpy.ops.object.align_rotation_z()
            bpy.ops.object.align_rotation_x()

        elif self.tp_axis == "tp_scal":

            bpy.ops.object.align_objects_scale_z()       
            bpy.ops.object.align_objects_scale_x()       

        return {'FINISHED'}



class VIEW3D_Align_Transform_Zy(bpy.types.Operator):
    """Align Transform Zy Axis"""
    bl_idname = "tp_ops.align_transform_zy"
    bl_label = "Align Transform Zy Axis"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("tp_loc"        ,"Location"     ,"Location"),
               ("tp_rot"        ,"Rotation"     ,"Rotation"),
               ("tp_scal"       ,"Scale"        ,"Scale")],
               name = "TP-Axis",
               default = "tp_loc",    
               description = "switch transformation type")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True) 

    def execute(self, context):
        
        if self.tp_axis == "tp_loc":

            bpy.ops.object.align_location_z()               
            bpy.ops.object.align_location_y()               

        elif self.tp_axis == "tp_rot":

            bpy.ops.object.align_rotation_z()
            bpy.ops.object.align_rotation_y()

        elif self.tp_axis == "tp_scal":

            bpy.ops.object.align_objects_scale_z()       
            bpy.ops.object.align_objects_scale_y()       

        return {'FINISHED'}




















