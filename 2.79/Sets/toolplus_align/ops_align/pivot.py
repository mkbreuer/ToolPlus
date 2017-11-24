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
from .. icons.icons import load_icons


class VIEW3D_TP_SnapSetMenu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_TP_SnapSetMenu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
        
        layout.label("SnapSet")

        layout.separator()

        if context.mode == 'OBJECT':
            button_snap_place = icons.get("icon_snap_place")
            layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

        else:
            button_snap_retopo = icons.get("icon_snap_retopo")
            layout.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    

        layout.separator()

        button_snap_grid = icons.get("icon_snap_grid")
        layout.operator("tp_ops.grid", text="GridSnap", icon_value=button_snap_grid.icon_id)
                    
        button_snap_cursor = icons.get("icon_snap_cursor")           
        layout.operator("tp_ops.active_3d", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 
 
        layout.separator()  

 
        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_active.icon_id)

        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 




class VIEW3D_TP_Pivot_Box(bpy.types.Operator):
   """Set pivot point to Bounding Box"""
   bl_label = "Set pivot point to Bounding Box"
   bl_idname = "tp_ops.pivot_bounding_box"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
       return {"FINISHED"} 

 
class VIEW3D_TP_Pivot_Cursor(bpy.types.Operator):
   """Set pivot point to 3D Cursor"""
   bl_label = "Set pivot point to 3D Cursor"
   bl_idname = "tp_ops.pivot_3d_cursor"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CURSOR'
       return {"FINISHED"} 


class VIEW3D_TP_Pivot_Median(bpy.types.Operator):
    """Set pivot point to Median Point"""
    bl_label = "Set pivot point to Median Point"
    bl_idname = "tp_ops.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}


class VIEW3D_TP_Pivot_Active(bpy.types.Operator):
   """Set pivot point to Active"""
   bl_label = "Set pivot point to Active"
   bl_idname = "tp_ops.pivot_active"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
       return {"FINISHED"} 


class VIEW3D_TP_Pivot_Individual(bpy.types.Operator):
    """Set pivot point to Individual"""
    bl_label = "Set pivot point to Individual Point"
    bl_idname = "tp_ops.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}   




def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__) 


if __name__ == "__main__":
    register()


