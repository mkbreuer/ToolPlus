__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


class VIEW3D_TP_Space_Menu(bpy.types.Menu):
    bl_label = "Space :) "
    bl_idname = "tp_menu.space_base"   
        
    def draw(self, context):
        layout = self.layout

        icons = load_icons()
      
        #layout.operator("mesh.faces_select_linked_flat", text="L-Flat") 

        #layout.separator()

        button_space_x = icons.get("icon_space_x") 
        layout.operator("tp_ops.face_align_x", "X", icon_value=button_space_x.icon_id)

        button_space_y = icons.get("icon_space_y") 
        layout.operator("tp_ops.face_align_y", "Y", icon_value=button_space_y.icon_id)           

        button_space_z = icons.get("icon_space_z") 
        layout.operator("tp_ops.face_align_z", "Z", icon_value=button_space_z.icon_id)

        layout.separator()

        button_space_xy = icons.get("icon_space_xy") 
        layout.operator("tp_ops.face_align_xy", "Xy", icon_value=button_space_xy.icon_id)

        button_space_zx = icons.get("icon_space_zx")
        layout.operator("tp_ops.face_align_xz", "Zx", icon_value=button_space_zx.icon_id)

        button_space_zy = icons.get("icon_space_zy") 
        layout.operator("tp_ops.face_align_yz", "Zy", icon_value=button_space_zy.icon_id)           

        layout.separator()          
                      
        button_space_align_to_normal = icons.get("icon_space_align_to_normal") 
        layout.operator("tp_ops.align_to_normal", "Align2Normal", icon_value=button_space_align_to_normal.icon_id)    

        layout.separator() 

        button_space_straigten = icons.get("icon_space_straigten") 
        layout.operator("mesh.vertex_align",text="Straighten", icon_value=button_space_straigten.icon_id) 

        button_space_distribute = icons.get("icon_space_distribute")  
        layout.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_space_distribute.icon_id)                                        

        layout.separator() 

        button_space_space = icons.get("icon_space_space")         
        layout.operator("mesh.looptools_space", text="LoopTools Space", icon_value=button_space_space.icon_id)

        button_space_curve = icons.get("icon_space_curve")
        layout.operator("mesh.looptools_curve", text="LoopTools Curve", icon_value=button_space_curve.icon_id)

        button_space_circle = icons.get("icon_space_circle") 
        layout.operator("mesh.looptools_circle", text="LoopTools Circle", icon_value=button_space_circle.icon_id)

        button_space_flatten = icons.get("icon_space_flatten") 
        layout.operator("mesh.looptools_flatten", text="LoopTool Flatten", icon_value=button_space_flatten.icon_id)










