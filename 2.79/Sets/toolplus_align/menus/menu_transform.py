# ##### BEGIN GPL LICENSE BLOCK #####
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


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons


class VIEW3D_TP_Location_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Location_Menu"
    bl_label = "Location"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()
        
        col = split.column()

        col.scale_y = 1.3    

        props = col.operator("tp_ops.align_transform", text="", icon='MAN_TRANS')        
        props.tp_axis= 'axis_xyz'         
        props.tp_transform= 'LOCATION'   
     
        col.operator("object.location_clear", text="", icon="PANEL_CLOSE")

        button_align_baply = icons.get("icon_align_baply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
        props.location=True
        props.rotation=False
        props.scale=False
 
        col = split.column()

        col.scale_y = 1.3    
  
        button_align_xy = icons.get("icon_align_xy") 
        props = col.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
        props.tp_axis= 'axis_xy'         
        props.tp_transform= 'LOCATION'    

        button_align_zx = icons.get("icon_align_zx")
        props = col.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
        props.tp_axis= 'axis_zx'         
        props.tp_transform= 'LOCATION'    
        
        button_align_zy = icons.get("icon_align_zy") 
        props = col.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
        props.tp_axis= 'axis_zy'         
        props.tp_transform= 'LOCATION'     

        col = split.column()

        col.scale_y = 1.3    

        button_align_x = icons.get("icon_align_x") 
        props = col.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id)
        props.tp_axis= 'axis_x'       
        props.tp_transform= 'LOCATION'       

        button_align_y = icons.get("icon_align_y")       
        props = col.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id)             
        props.tp_axis= 'axis_y' 
        props.tp_transform= 'LOCATION' 

        button_align_z = icons.get("icon_align_z")     
        props = col.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id)
        props.tp_axis= 'axis_z'         
        props.tp_transform= 'LOCATION'         
        




class VIEW3D_TP_Rotation_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Rotation_Menu"
    bl_label = "Rotation"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()
        
        col = split.column()

        col.scale_y = 1.3    

        props = col.operator("tp_ops.align_transform",text="", icon='MAN_ROT') 
        props.tp_axis= 'axis_xyz'         
        props.tp_transform= 'ROTATION'     

        col.operator("object.rotation_clear", text="", icon="PANEL_CLOSE")
        
        button_align_baply = icons.get("icon_align_baply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
        props.location=False
        props.rotation=True
        props.scale=False

        col = split.column()
  
        col.scale_y = 1.3    

        button_align_xy = icons.get("icon_align_xy") 
        props = col.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
        props.tp_axis= 'axis_xy'         
        props.tp_transform= 'ROTATION'    

        button_align_zx = icons.get("icon_align_zx")
        props = col.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
        props.tp_axis= 'axis_zx'         
        props.tp_transform= 'ROTATION'    
        
        button_align_zy = icons.get("icon_align_zy") 
        props = col.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
        props.tp_axis= 'axis_zy'         
        props.tp_transform= 'ROTATION'     

        col = split.column()

        col.scale_y = 1.3    

        button_align_x = icons.get("icon_align_x") 
        props = col.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id)
        props.tp_axis= 'axis_x'       
        props.tp_transform= 'ROTATION'       

        button_align_y = icons.get("icon_align_y")       
        props = col.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id)             
        props.tp_axis= 'axis_y' 
        props.tp_transform= 'ROTATION' 

        button_align_z = icons.get("icon_align_z")     
        props = col.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id)
        props.tp_axis= 'axis_z'         
        props.tp_transform= 'ROTATION'         
        


      
class VIEW3D_TP_Scale_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Scale_Menu"
    bl_label = "Scale"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split(1)

        col = split.column(1)
    
        col.scale_y = 1.3            
   
        props = col.operator("tp_ops.align_transform",text="", icon='MAN_SCALE')    
        props.tp_axis= 'axis_xyz'         
        props.tp_transform= 'SCALE'    

        col.operator("object.scale_clear", text="", icon="PANEL_CLOSE")        

        button_align_baply = icons.get("icon_align_baply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_align_baply.icon_id)
        props.location=False
        props.rotation=False
        props.scale=True


        col = split.column()
  
        col.scale_y = 1.3    

        button_align_xy = icons.get("icon_align_xy") 
        props = col.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
        props.tp_axis= 'axis_xy'         
        props.tp_transform= 'SCALE'    

        button_align_zx = icons.get("icon_align_zx")
        props = col.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
        props.tp_axis= 'axis_zx'         
        props.tp_transform= 'SCALE'    
        
        button_align_zy = icons.get("icon_align_zy") 
        props = col.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
        props.tp_axis= 'axis_zy'         
        props.tp_transform= 'SCALE'     

        col = split.column()
      
        col.scale_y = 1.3    
     
        button_align_x = icons.get("icon_align_x") 
        props = col.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id)
        props.tp_axis= 'axis_x'       
        props.tp_transform= 'SCALE'       

        button_align_y = icons.get("icon_align_y")       
        props = col.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id)             
        props.tp_axis= 'axis_y' 
        props.tp_transform= 'SCALE' 

        button_align_z = icons.get("icon_align_z")     
        props = col.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id)
        props.tp_axis= 'axis_z'         
        props.tp_transform= 'SCALE'  

