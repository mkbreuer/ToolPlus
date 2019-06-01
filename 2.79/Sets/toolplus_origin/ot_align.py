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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


def edit_align_function(tp_axis, tp_orient, tp_mirror, propedit, falloff, propsize, tp_pivot):

    if tp_pivot == "ACTIVE_ELEMENT":
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'

    if tp_pivot == "MEDIAN_POINT":
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'

    if tp_pivot == "CURSOR":
        bpy.context.space_data.pivot_point = 'CURSOR'   


    if tp_axis == "axis_x":
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

    if tp_axis == "axis_y":
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

    if tp_axis == "axis_z":
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)
      
    if tp_axis == "axis_xy":
        bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

    if tp_axis == "axis_zy":
        bpy.ops.transform.resize(value=(1, 0, 0), constraint_axis=(False, True, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

    if tp_axis == "axis_zx":
        bpy.ops.transform.resize(value=(0, 1, 0), constraint_axis=(True, False, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

    if tp_axis == "axis_xyz":
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)
        bpy.ops.mesh.merge(type='CENTER')



      
class VIEW3D_OT_Origin_Transform(bpy.types.Operator):
    """align selected mesh to an axis"""
    bl_label = "Align to Axis"
    bl_idname = "tpc_ops.origin_transform"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis = bpy.props.EnumProperty(
        items=[("axis_x"     ,"X"     ,""),
               ("axis_y"     ,"Y"     ,""),
               ("axis_z"     ,"Z"     ,""),
               ("axis_xy"    ,"Xy"    ,""),
               ("axis_zy"    ,"Zy"    ,""),
               ("axis_zx"    ,"Zx"    ,""),
               ("axis_xyz"   ,"XYZ"   ,"")],
               name = " ",
               default = "axis_x")

    tp_pivot = bpy.props.EnumProperty(
        items=[("ACTIVE_ELEMENT"  ,"Active Element"  ,""  ,"ROTACTIVE"    ,0),
               ("MEDIAN_POINT"    ,"Median Point"    ,""  ,"ROTATECENTER" ,1),
               ("CURSOR"          ,"3D Cursor"       ,""  ,"CURSOR"       ,2)],
               name = "Pivot", 
               default = "ACTIVE_ELEMENT")

    tp_orient = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "Orientation",
               default = "GLOBAL")

    propedit = bpy.props.EnumProperty(
        items=[("DISABLED"   ,"Disabled"   ,""  ,"PROP_OFF" ,0),
               ("ENABLED"    ,"Enabled"    ,""  ,"PROP_ON"  ,1),
               ("PROJECTED"  ,"Projected"  ,""  ,"PROP_ON"  ,2),
               ("CONNECTED"  ,"Connected"  ,""  ,"PROP_CON" ,3)],
               name = "Proportional Editing",
               default = "DISABLED", options={'SKIP_SAVE'})

    falloff = bpy.props.EnumProperty(
        items=[("SMOOTH"            ,"Smooth"           ,""   ,"SMOOTHCURVE"  ,0),
               ("SPHERE"            ,"Sphere"           ,""   ,"SPHERECURVE"  ,1),
               ("ROOT"              ,"Root"             ,""   ,"ROOTCURVE"    ,2),
               ("INVERSE_SQUARE"    ,"Inverse Square"   ,""   ,"ROOTCURVE"    ,3),
               ("SHARP"             ,"Sharp"            ,""   ,"SHARPCURVE"   ,4),
               ("LINEAR"            ,"Linear"           ,""   ,"LINCURVE"     ,5),
               ("CONSTANT"          ,"Constant"         ,""   ,"NOCURVE"      ,6),
               ("RANDOM"            ,"Random"           ,""   ,"RNDCURVE"     ,7)],
               name = "Proportional Falloff",
               default = "SMOOTH")

    propsize = FloatProperty(name="Size",  description= "Proportional Editing Size", min=0.001, max=100.0, default=1.0)

    tp_mirror = BoolProperty (name = "X-Mirror", default= False, description= "toggle x-axis mirror over origin")

    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(1)              
            
        row = box.row(1) 
        row.prop(self, 'tp_axis', expand =True)
    
        box.separator() 
     
        row = box.row(1) 
        row.label('Oriention:')      
        row.prop(self, 'tp_orient', text="")      

        box.separator() 

        row = box.row(1) 
        row.label('Pivot Point:')      
        row.prop(self, 'tp_pivot', text="")    

        box.separator() 

        box = col.box().column(1)   

        row = box.row(1) 
        row.label("Proportional Editing")

        box.separator() 

        row = box.row() 
        row.prop(self, 'propedit', text="")
        row.prop(self, 'falloff', text="")
     
        box.separator() 
        
        row = box.row(1) 
        row.prop(self, 'propsize')
        row.prop(self, 'tp_mirror')              

        box.separator()


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        edit_align_function( self.tp_axis, self.tp_orient, self.tp_mirror, self.propedit, self.falloff, self.propsize, self.tp_pivot)                               
        return {'FINISHED'} 


    # without ok button
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)      
    



