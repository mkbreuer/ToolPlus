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


class VIEW3D_TP_Pivot_Box(bpy.types.Operator):
   """use Bounding Box Center"""
   bl_label = "Bounding Box Center"
   bl_idname = "tp_ops.pivot_bounding_box"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
       return {"FINISHED"} 

 
class VIEW3D_TP_Pivot_Cursor(bpy.types.Operator):
   """use 3D Cursor"""
   bl_label = "3D Cursor"
   bl_idname = "tp_ops.pivot_3d_cursor"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CURSOR'
       return {"FINISHED"} 


class VIEW3D_TP_Pivot_Median(bpy.types.Operator):
    """use Median Point"""
    bl_label = "Median Point"
    bl_idname = "tp_ops.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}


class VIEW3D_TP_Pivot_Active(bpy.types.Operator):
   """use Active Element"""
   bl_label = "Active Element"
   bl_idname = "tp_ops.pivot_active"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
       return {"FINISHED"} 


class VIEW3D_TP_Pivot_Individual(bpy.types.Operator):
    """use Individual Origins"""
    bl_label = "Individual Origins"
    bl_idname = "tp_ops.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}   



# REGISTER #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()



