# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  

import addon_utils

class VIEW3D_MT_SnapOrigin_Menu(bpy.types.Menu):
    bl_label = "Origin Modal"
    bl_idname = "VIEW3D_MT_SnapOrigin_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

#        loop_tools_addon = "mesh_looptools" 
#        state = addon_utils.check(loop_tools_addon)
#        if not state[0]: 
#            pass                        

#        else:

#            layout.operator("tpc_ot.snapflatten_modal", text="Flatten LpT").mode="flatten_lpt"        
#            layout.separator()



        if context.mode == 'OBJECT':

            if len(bpy.context.selected_objects) == 1: 
              
                button_origin_tosnap = icons.get("icon_origin_tosnap")         
                layout.operator("tpc_ot.snap_to_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)
                
                button_origin_edm = icons.get("icon_origin_edm")   
                layout.operator("tpc_ot.snaporigin_modal", text="Origin to Mesh", icon_value=button_origin_edm.icon_id).mode = "cursor, obm"                   

                layout.separator()
              
                button_origin_bbox = icons.get("icon_origin_bbox")                               
                layout.operator("tpc_ot.snap_to_bbox", text="Origin to BBox", icon="SNAP_PEEL_OBJECT")                              

                layout.separator()
                
                button_origin_center_loc = icons.get("icon_origin_center_loc")
                layout.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"
          
            else:
                layout.label(text="Only for 1")
                layout.label(text="selected")
                layout.label(text="object")
                layout.label(text="allowed!")
     
        else:

            button_origin_edm = icons.get("icon_origin_edm")   
            layout.operator("tpc_ot.snaporigin_modal", text="Edm-Select", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"

            button_origin_obj = icons.get("icon_origin_obj")   
            layout.operator("tpc_ot.snaporigin_modal", text="Obm-Select", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"


            layout.separator() 
                 
            button_origin_center_loc = icons.get("icon_origin_center_loc")
            layout.operator("tpc_ot.snaporigin_modal", text="Clear Location", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"
              
