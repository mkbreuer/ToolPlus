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
from .. icons.icons import load_icons


class VIEW3D_TP_N_Transform_Menu(bpy.types.Menu):
    """Normal Transform Menu for active Pivot Point"""
    bl_label = "Normal Transform Menu"
    bl_idname = "tp_ops.normal_transform_menu"

    def draw(self, context):
        layout = self.layout    
      
        layout.scale_y = 1.3
       
        layout.menu("translate.normal_menu", text="N-Translate")
        layout.menu("rotate.normal_menu", text="N-Rotate")
        layout.menu("resize.normal_menu", text="N-Scale")



class VIEW3D_TP_Translate_Normal_Menu(bpy.types.Menu):
    """Translate Normal Constraint for active Pivot Point"""
    bl_label = "Translate Normal Constraint"
    bl_idname = "tp_ops.translate_normal_menu"

    def draw(self, context):
        layout = self.layout         

        #layout.label("___Move___")
       
        layout.scale_y = 1.3
        
        props = layout.operator("transform.transform", text = "X-Axis")
        props.mode = 'TRANSLATION'
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.transform", text = "Y-Axis")
        props.mode = 'TRANSLATION'
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.transform", text = "Z-Axis")
        props.mode = 'TRANSLATION'
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 



class VIEW3D_TP_Resize_Normal_Menu(bpy.types.Menu):
    """Resize Normal Constraint for active Pivot Point"""
    bl_label = "Resize Normal Constraint"
    bl_idname = "tp_ops.resize_normal_menu"

    def draw(self, context):
        layout = self.layout         
        
        #layout.label("___Scale___") 

        layout.scale_y = 1.3
        
        props = layout.operator("transform.resize", text = "X-Axis")
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.resize", text = "Y-Axis")
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 
        
        props = layout.operator("transform.resize", text = "Z-Axis")
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE'                  

        props = layout.operator("transform.resize", text = "XY-Axis")
        props.constraint_axis = (True, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE'



class VIEW3D_TP_Rotate_Normal_Menu(bpy.types.Menu):
    """Rotate Normal Constraint for active Pivot Point"""
    bl_label = "Rotate Normal Constraint"
    bl_idname = "tp_ops.rotate_normal_menu"

    def draw(self, context):
        layout = self.layout         
        
        #layout.label("___Rotate___") 
        
        layout.scale_y = 1.3

        props = layout.operator("transform.rotate", text = "X-Axis")
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.rotate", text = "Y-Axis")
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 
        
        props = layout.operator("transform.rotate", text = "Z-Axis")
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE'                  



# REGISTER #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.ubregister_module(__name__)

if __name__ == "__main__":
    register()


