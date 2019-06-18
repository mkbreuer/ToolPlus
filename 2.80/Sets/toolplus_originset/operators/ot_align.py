# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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


def edit_align_function(tp_axis, tp_orient, tp_mirror, tp_use, falloff, propsize, tp_pivot, tp_connected, tp_projected, tp_merge, tp_merge_uv):


    if tp_pivot == "ACTIVE_ELEMENT":
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
   
    if tp_pivot == "INDIVIDUAL_ORIGINS":
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

    if tp_pivot == "MEDIAN_POINT":
        bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'

    if tp_pivot == "CURSOR":
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'  

    if tp_pivot == "BOUNDING_BOX_CENTER":
        bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'


    if tp_axis == "axis_x":
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)

    if tp_axis == "axis_y":
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)

    if tp_axis == "axis_z":
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)
      
    if tp_axis == "axis_xy":
        bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)

    if tp_axis == "axis_zy":
        bpy.ops.transform.resize(value=(1, 0, 0), constraint_axis=(False, True, True), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)

    if tp_axis == "axis_zx":
        bpy.ops.transform.resize(value=(0, 1, 0), constraint_axis=(True, False, True), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)

    if tp_axis == "axis_xyz":
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)
        
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)
        
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), 
        orient_type=tp_orient, mirror=tp_mirror, use_proportional_edit=tp_use, proportional_edit_falloff=falloff, 
        proportional_size=propsize, use_proportional_connected=tp_connected, use_proportional_projected=tp_projected)

        bpy.ops.mesh.merge(type=tp_merge, uvs=tp_merge_uv)


      
class VIEW3D_OT_align_to_axis(bpy.types.Operator):
    """align selected mesh to an axis"""
    bl_label = "Align to Axis"
    bl_idname = "tpc_ops.align_to_axis"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis : bpy.props.EnumProperty(
        items=[("axis_x"     ,"X"     ,""),
               ("axis_y"     ,"Y"     ,""),
               ("axis_z"     ,"Z"     ,""),
               ("axis_xy"    ,"Xy"    ,""),
               ("axis_zy"    ,"Zy"    ,""),
               ("axis_zx"    ,"Zx"    ,""),
               ("axis_xyz"   ,"XYZ"   ,"")],
               name = " ",
               default = "axis_x")

    tp_pivot : bpy.props.EnumProperty(
        items=[("ACTIVE_ELEMENT"        ,"Active Element"       ,""  ,"PIVOT_ACTIVE"     ,0),
               ("MEDIAN_POINT"          ,"Median Point"         ,""  ,"PIVOT_MEDIAN"     ,1),
               ("INDIVIDUAL_ORIGINS"    ,"Individuals Origins"  ,""  ,"PIVOT_INDIVIDUAL" ,2),
               ("CURSOR"                ,"3D Cursor"            ,""  ,"PIVOT_CURSOR"     ,3),
               ("BOUNDING_BOX_CENTER"   ,"Bounding Box Cener"   ,""  ,"PIVOT_BOUNDBOX"   ,4)],
               name = "Pivot", 
               default = "ACTIVE_ELEMENT")

    tp_orient : bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,""  ,"ORIENTATION_LOCAL"  ,0),
               ("LOCAL"     ,"Local"    ,""  ,"ORIENTATION_LOCAL"  ,1),
               ("NORMAL"    ,"Normal"   ,""  ,"ORIENTATION_NORMAL" ,2),
               ("GIMBAL"    ,"Gimbal"   ,""  ,"ORIENTATION_GIMBAL" ,3),
               ("VIEW"      ,"View"     ,""  ,"ORIENTATION_VIEW"   ,4),
               ("CURSOR"    ,"Cursor"   ,""  ,"ORIENTATION_CURSOR" ,5)],
               name = "Orientation",
               default = "GLOBAL")

    falloff : bpy.props.EnumProperty(
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

    propsize : FloatProperty(name="Size",  description= "Proportional Editing Size", min=0.001, max=100.0, default=1.0)

    tp_use : BoolProperty (name = "Proportional Editing", default= False, description= "toggle on/off")
    tp_mirror : BoolProperty (name = "X-Mirror", default= False, description= "toggle x-axis mirror over origin")
    tp_connected : BoolProperty (name = "Connect", default= False, description= "toggle on/off")
    tp_projected : BoolProperty (name = "Projected 2D", default= False, description= "toggle on/off")

    tp_merge : bpy.props.EnumProperty(
        items=[("CENTER"   ,"Center"   ,""),
               ("COLLAPSE" ,"Collapse" ,""),
               ("CURSOR"   ,"Cursor"   ,"")],
               name = "Merge",
               default = "CENTER")

    tp_merge_uv : BoolProperty (name = "UV", default= False, description= "toggle on/off")


    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(align=True)              
            
        row = box.row(align=True) 
        row.prop(self, 'tp_axis', expand =True)
    
        box.separator() 
     
        row = box.row(align=True) 
        row.label(text='Oriention:')      
        row.prop(self, 'tp_orient', text="")      

        box.separator() 

        row = box.row(align=True) 
        row.label(text='Pivot Point:')      
        row.prop(self, 'tp_pivot', text="")    

        box.separator() 

        box = col.box().column(align=True)   

        row = box.row(align=True) 
        row.prop(self, 'tp_use', text="")
        row.label(text="Proportional Editing")
        row.prop(self, 'falloff', text="")
     
        box.separator() 
        
        row = box.row(align=True) 
        row.prop(self, 'propsize')
        row.prop(self, 'tp_mirror')              
       
        box.separator() 
        
        row = box.row(align=True) 
        row.prop(self, 'tp_connected')
        row.prop(self, 'tp_projected')  

        box.separator() 
        
        if self.tp_axis == 'axis_xyz':   

            box = col.box().column(align=True)   
           
            row = box.row(align=False)     
            row.label(text="Merge:")
            row.prop(self, 'tp_merge', text="")      
            row.prop(self, 'tp_merge_uv')      

            box.separator() 


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        edit_align_function( self.tp_axis, self.tp_orient, self.tp_mirror, self.tp_use, self.falloff, self.propsize, self.tp_pivot, self.tp_connected, self.tp_projected, self.tp_merge, self.tp_merge_uv)                               
        return {'FINISHED'} 


    # without ok button
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)      
    



# REGISTER #
def register():
    bpy.utils.register_class(VIEW3D_OT_align_to_axis)  
 
def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_align_to_axis)   
     
if __name__ == "__main__":
    register() 