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
from . icons.icons import load_icons    
     

class VIEW3D_TP_Transform_Menu(bpy.types.Menu):
    bl_label = "Transform+"
    bl_idname = "VIEW3D_TP_Transform_Menu"  
    bl_space_type = 'VIEW_3D'
    
    def draw(self, context):
        panel_prefs = context.user_preferences.addons[__package__].preferences
       
        icons = load_icons()
        
        layout = self.layout

        layout.scale_y = 1.5

        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'


        if bpy.context.area.type == 'VIEW_3D':
            
            layout.menu("VIEW3D_TP_SnapSet_Menu", text="SnapSet") 
            
            layout.separator()
            
            if panel_prefs.tab_normal_menu == True:  
            
                layout.menu("VIEW3D_TP_Move_Normal_Menu", text="N-Translate")
                layout.menu("VIEW3D_TP_Rotate_Normal_Menu", text="N-Rotate")
                layout.menu("VIEW3D_TP_Resize_Normal_Menu", text="N-Scale")

                layout.separator()


            if context.mode == 'OBJECT':
             
                layout.menu("VIEW3D_TP_Location_Menu", text="Align Location")   
                layout.menu("VIEW3D_TP_Rotation_Menu", text="Align Rotate")  
                layout.menu("VIEW3D_TP_Scale_Menu", text="Align Scale")  

            else:
     
                layout.menu("VIEW3D_TP_Axis_Menu", text="Align To Axis")   

        

        if bpy.context.area.type == 'IMAGE_EDITOR':        
 
            button_align_x = icons.get("icon_align_x") 
            layout.operator("tp_ops.align_uv_image", text="X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'
          
            button_align_y = icons.get("icon_align_y") 
            layout.operator("tp_ops.align_uv_image", text="Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'
            
            button_align_xy = icons.get("icon_align_xy") 
            layout.operator("tp_ops.align_uv_image", text="Xy", icon_value=button_align_xy.icon_id).tp_axis ='axis_xy'

            layout.separator()

            layout.prop(bpy.context.scene, 'tp_pivot2', text="") 


        if bpy.context.area.type == 'GRAPH_EDITOR':
 
            button_align_x = icons.get("icon_align_x") 
            layout.operator("tp_ops.align_graph", text="X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'
            
            button_align_y = icons.get("icon_align_y") 
            layout.operator("tp_ops.align_graph", text="Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'
            
            button_align_xy = icons.get("icon_align_xy") 
            layout.operator("tp_ops.align_graph", text="Xy", icon_value=button_align_xy.icon_id).tp_axis ='axis_xy'

            layout.separator()

            layout.prop(bpy.context.scene, 'tp_pivot3', text="") 

        
        if bpy.context.area.type == 'NODE_EDITOR':

            button_align_x = icons.get("icon_align_x") 
            layout.operator("tp_ops.align_node", text="X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'
          
            button_align_y = icons.get("icon_align_y") 
            layout.operator("tp_ops.align_node", text="Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'

     

         
 

class VIEW3D_TP_Move_Normal_Menu(bpy.types.Menu):
    """Move Normal Constraint"""
    bl_label = "Normal Move"
    bl_idname = "VIEW3D_TP_Move_Normal_Menu"

    def draw(self, context):
        layout = self.layout         

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


class VIEW3D_TP_Rotate_Normal_Menu(bpy.types.Menu):
    """Rotate Normal Constraint"""
    bl_label = "Normal Rotate"
    bl_idname = "VIEW3D_TP_Rotate_Normal_Menu"

    def draw(self, context):
        layout = self.layout         
        
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



class VIEW3D_TP_Resize_Normal_Menu(bpy.types.Menu):
    """Resize Normal Constraint"""
    bl_label = "Normal Scale"
    bl_idname = "VIEW3D_TP_Resize_Normal_Menu"

    def draw(self, context):
        layout = self.layout         
      
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
     
        col.operator("tp_ops.location_clear", text="", icon="PANEL_CLOSE")

        button_apply = icons.get("icon_apply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_apply.icon_id)
        props.location=True
        props.rotation=False
        props.scale=False
 
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

        col.operator("tp_ops.rotation_clear", text="", icon="PANEL_CLOSE")
        
        button_apply = icons.get("icon_apply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_apply.icon_id)
        props.location=False
        props.rotation=True
        props.scale=False

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

        col.operator("tp_ops.scale_clear", text="", icon="PANEL_CLOSE")        

        button_apply = icons.get("icon_apply") 
        props = col.operator("object.transform_apply", text="", icon_value=button_apply.icon_id)
        props.location=False
        props.rotation=False
        props.scale=True


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




 
class VIEW3D_TP_Axis_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Axis_Menu"
    bl_label = "Axis"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()
            
        col = split.column(1)            
      
        col.scale_y = 1.3

        button_align_x = icons.get("icon_align_x") 
        col.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis ='axis_x'

        button_align_y = icons.get("icon_align_y") 
        col.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis ='axis_y'           

        button_align_z = icons.get("icon_align_z") 
        col.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis ='axis_z'


        col = split.column(1)

        col.scale_y = 1.3
      
        button_align_xy = icons.get("icon_align_xy") 
        col.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis ='axis_xy'

        button_align_zx = icons.get("icon_align_zx")
        col.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis ='axis_zx'

        button_align_zy = icons.get("icon_align_zy") 
        col.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis ='axis_zy'    
            

        

