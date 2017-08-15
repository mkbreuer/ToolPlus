__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy, os
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


def draw_origin_menu_layout(self, context, layout):
          
        icons = load_icons()

        button_origin_center_view = icons.get("icon_origin_center_view")
        layout.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

        button_origin_cursor = icons.get("icon_origin_cursor")
        layout.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

        layout.separator()

        button_origin_edm = icons.get("icon_origin_edm")            
        layout.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

        button_origin_obj = icons.get("icon_origin_obj")   
        layout.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)            
      
        layout.separator()
       
        button_align_zero = icons.get("icon_align_zero")                
        layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)           



class VIEW3D_TP_Origin_Menu(bpy.types.Menu):
    bl_label = "Origin :) "
    bl_idname = "tp_menu.origin_base"   

    def draw(self, context):
        layout = self.layout

        icons = load_icons()          
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
      
  
        ob = context
        if ob.mode == 'OBJECT':

            button_origin_center_view = icons.get("icon_origin_center_view")
            layout.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            layout.operator("tp_ops.origin_set_cursor", text="3D Cursor", icon_value=button_origin_cursor.icon_id)

            layout.separator()
            
            button_origin_tomesh = icons.get("icon_origin_tomesh")
            layout.operator("tp_ops.origin_tomesh", text="Origin to Mesh", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            layout.operator("tp_ops.origin_meshto", text="Mesh to Origin", icon_value=button_origin_meshto.icon_id)

            layout.separator()

            button_origin_mass = icons.get("icon_origin_mass")           
            layout.operator("tp_ops.origin_set_mass", text="Center of Mass", icon_value=button_origin_mass.icon_id)

            layout.separator()
            
            button_origin_bbox = icons.get("icon_origin_bbox")
            layout.operator("object.bbox_origin_modal_ops", text="BBox Origin", icon_value=button_origin_bbox.icon_id)

            layout.separator()

            button_align_zero = icons.get("icon_align_zero")                
            layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)  

            button_origin_distribute = icons.get("icon_origin_distribute")  
            layout.operator("object.distribute_osc", "Distribute", icon_value=button_origin_distribute.icon_id)
           
            button_origin_align = icons.get("icon_origin_align")
            layout.operator("tp_origin.align_tools", "AlignTools", icon_value=button_origin_align.icon_id)           
            

        if ob.mode == 'EDIT_MESH':


            draw_origin_menu_layout(self, context, layout) 
            
            
        if ob.mode == 'EDIT_CURVE':
            
            draw_origin_menu_layout(self, context, layout) 


       
        if ob.mode == 'EDIT_SURFACE':
            
            draw_origin_menu_layout(self, context, layout) 



        if ob.mode == 'EDIT_METABALL':
            
            draw_origin_menu_layout(self, context, layout) 

   
        if ob.mode == 'EDIT_LATTICE':
            
            draw_origin_menu_layout(self, context, layout) 
            
                 
        if  context.mode == 'PARTICLE':
       
            draw_origin_menu_layout(self, context, layout) 


        if ob.mode == 'EDIT_ARMATURE':

            draw_origin_menu_layout(self, context, layout) 
            

        if context.mode == 'POSE':

            draw_origin_menu_layout(self, context, layout) 








