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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


class VIEW3D_TP_PIVOT_TARGET(bpy.types.Operator):
    """Set Pivot"""
    bl_idname = "tp_ops.set_pivot"
    bl_label = "Set Pivot"
    bl_options = {'REGISTER', 'UNDO'}

    tp_pivot = bpy.props.EnumProperty(
                 items=[("BOUNDING_BOX_CENTER"  ," "    ,""   ,"ROTATE"            , 1),
                        ("CURSOR"               ," "    ,""   ,"CURSOR"            , 2),
                        ("INDIVIDUAL_ORIGINS"   ," "    ,""   ,"ROTATECOLLECTION"  , 3),
                        ("MEDIAN_POINT"         ," "    ,""   ,"ROTATECENTER"      , 4),
                        ("ACTIVE_ELEMENT"       ," "    ,""   ,"ROTACTIVE"         , 5)],
                        name = "Pivot", 
                        default = "BOUNDING_BOX_CENTER")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_pivot',text=" ", expand =True)                                            
     
        box.separator()


    def execute(self, context):

        if self.tp_pivot == "BOUNDING_BOX_CENTER":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'             

        elif self.tp_pivot == "CURSOR":
            bpy.context.space_data.pivot_point = 'CURSOR' 

        elif self.tp_pivot == "INDIVIDUAL_ORIGINS":
            bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'           

        elif self.tp_pivot == "MEDIAN_POINT":
            bpy.context.space_data.pivot_point = 'MEDIAN_POINT'                        

        elif self.tp_pivot == "ACTIVE_ELEMENT":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'

        return {'FINISHED'}
    
    
               
class VIEW3D_TP_ORIENT_AXIS(bpy.types.Operator):
    """Transform Axis Orientation"""
    bl_idname = "tp_ops.orient_axis"
    bl_label = "Transform Axis Orientation"
    bl_options = {'REGISTER', 'UNDO'}

    tp_axis = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "Orientation",
               default = "GLOBAL",    
               description = "change manipulator axis")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_axis',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):
        
        if self.tp_axis == "GLOBAL":
            bpy.context.space_data.transform_orientation = 'GLOBAL'               
       
        elif self.tp_axis == "LOCAL":
            bpy.context.space_data.transform_orientation = 'LOCAL' 
       
        elif self.tp_axis == "NORMAL":
            bpy.context.space_data.transform_orientation = 'NORMAL'            
       
        elif self.tp_axis == "GIMBAL":
             bpy.context.space_data.transform_orientation = 'GIMBAL'            
       
        elif self.tp_axis == "VIEW":
            bpy.context.space_data.transform_orientation = 'VIEW'      
        
        return {'FINISHED'}




class VIEW3D_TP_SNAP_TARGET(bpy.types.Operator):
    """Snap Target"""
    bl_idname = "tp_ops.snap_target"
    bl_label = "Snap Target"
    bl_options = {'REGISTER', 'UNDO'}

    tp_snapt = bpy.props.EnumProperty(
                 items=[("CLOSEST"   ,"Closest"   ,"Closest"  ,"" , 1),
                        ("CENTER"    ,"Center"   ,"Center"   ,"" , 2),
                        ("MEDIAN"    ,"Median"   ,"Median"   ,"" , 3),
                        ("ACTIVE"    ,"Active"   ,"Active"   ,"" , 4)],
                        name = "Snap Target", 
                        default = "CLOSEST")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_snapt',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):
  
        if self.tp_snapt == "CLOSEST":
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'         
     
        elif self.tp_snapt == "CENTER":
            bpy.context.scene.tool_settings.snap_target = 'CENTER'
     
        elif self.tp_snapt == "MEDIAN":
            bpy.context.scene.tool_settings.snap_target = 'MEDIAN'        
     
        elif self.tp_snapt == "ACTIVE":
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'

        return {'FINISHED'}




class VIEW3D_TP_SNAP_ELEMENT(bpy.types.Operator):
    """Snap Element"""
    bl_idname = "tp_ops.snap_element"
    bl_label = "Snap Element"
    bl_options = {'REGISTER', 'UNDO'}

    tp_snape = bpy.props.EnumProperty(
                 items=[("INCREMENT" ,"Increment"   ,""   ,"SNAP_INCREMENT" , 1),
                        ("VERTEX"    ,"Vertex"      ,""   ,"SNAP_VERTEX"    , 2),
                        ("EDGE"      ,"Edge"        ,""   ,"SNAP_EDGE"      , 3),
                        ("FACE"      ,"Face"        ,""   ,"SNAP_FACE"      , 4),
                        ("VOLUME"    ,"Volume"      ,""   ,"SNAP_VOLUME"    , 5)],
                        name = "Snap Element", 
                        default = "INCREMENT")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_snape',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):

        if self.tp_snape == "INCREMENT":
            bpy.ops.snape.increment()          

        elif self.tp_snape == "VERTEX":
            bpy.ops.snape.vertex()     

        elif self.tp_snape == "EDGE":
            bpy.ops.snape.edge()           

        elif self.tp_snape == "FACE":
            bpy.ops.snape.face()                          

        elif self.tp_snape == "VOLUME":
            bpy.ops.snape.volume()     

        return {'FINISHED'}




# REGISTER #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()



