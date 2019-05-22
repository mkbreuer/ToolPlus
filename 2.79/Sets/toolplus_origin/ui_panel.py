# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    


EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE"]

# DRAW UI LAYOUT #
def draw_origin_ui(self, context, layout):
    
    layout = self.layout.column_flow(align=True)  
    layout.operator_context = 'INVOKE_REGION_WIN'
    
    panel_prefs = context.user_preferences.addons[__package__].preferences

    icons = load_icons()

    col = layout.column(align=True)   

    box = col.box().column(align=True)                         
    
    row = box.column(align=True)
    
    button_origin_cursor = icons.get("icon_origin_cursor")
    row.operator("tpc_ot.set_origin_to", text="Origin to Cursor", icon_value=button_origin_cursor.icon_id).mode = "ORIGIN_CURSOR"
        
    row.separator()

    button_origin_center_view = icons.get("icon_origin_center_view")
    row.operator("tpc_ot.set_origin_to", text="Origin to Center", icon_value=button_origin_center_view.icon_id).mode = "ORIGIN_CENTER"       

    obj = context.active_object
    if obj:
        if obj.type in {'MESH'}:

            row = box.row(align=True)  
            if len(bpy.context.selected_objects) == 1:               
                if context.mode in EDIT:                   
                    button_origin_center_loc = icons.get("icon_origin_center_loc")
                    row.operator("tpc_ot.snaporigin_modal", text="Object to Center", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear, edm"
                else:                
                    button_origin_center_loc = icons.get("icon_origin_center_loc")
                    row.operator("tpc_ot.snaporigin_modal", text="Object to Center", icon_value=button_origin_center_loc.icon_id).mode = "cursor, obm, clear"

    box.separator()

    row = box.column(align=True)
    
    button_origin_tomesh = icons.get("icon_origin_tomesh")
    row.operator("tpc_ot.set_origin_to", text="Origin to Object", icon_value=button_origin_tomesh.icon_id).mode = "ORIGIN_GEOMETRY"
  
    button_origin_meshto = icons.get("icon_origin_meshto")
    row.operator("tpc_ot.set_origin_to", text="Object to Origin", icon_value=button_origin_meshto.icon_id).mode = "GEOMETRY_ORIGIN"

    row.separator()
   
    button_origin_mass = icons.get("icon_origin_mass")           
    row.operator("tpc_ot.set_origin_to", text="Mass (Surface)", icon_value=button_origin_mass.icon_id).mode = "ORIGIN_CENTER_OF_MASS"
    row.operator("tpc_ot.set_origin_to", text="Mass (Volume)", icon_value=button_origin_mass.icon_id).mode = "ORIGIN_CENTER_OF_VOLUME"
 
    box.separator() 

    if context.mode == 'EDIT_MESH':

        row = box.column(align=True)
                    
        row.operator("tpc_ot.set_origin_to", text="Linked Mesh", icon ="LINKED").mode = "LINKED_MESH, ORIGIN_CURSOR"
        row.operator("tpc_ot.set_origin_to", text="Selected Mesh", icon ="EDIT").mode = "SELECTED_MESH, ORIGIN_CURSOR"   

    
        row.separator()        
      
        button_origin_edm = icons.get("icon_origin_edm")   
        row.operator("tpc_ot.snaporigin_modal", text="M-Select-EdM", icon_value=button_origin_edm.icon_id).mode = "cursor, obm, edm"

        button_origin_obj = icons.get("icon_origin_obj")   
        row.operator("tpc_ot.snaporigin_modal", text="M-Select-ObM", icon_value=button_origin_obj.icon_id).mode = "cursor, obm"


   

    if context.mode == 'OBJECT':
        
        box.separator() 

        row = box.column(align=True)

        selected = bpy.context.selected_objects
        n = len(selected)                         
        if n == 1:

            button_origin_tosnap = icons.get("icon_origin_tosnap")         
            row.operator("tpc_ot.origin_to_snap_helper", text="Origin to Snap", icon_value=button_origin_tosnap.icon_id)

        obj = context.active_object
        if obj:
            if obj.type in {'MESH'}:

                button_origin_selected= icons.get("icon_origin_selected")   
                row.operator("tpc_ot.snaporigin_modal", text="Origin to Select", icon_value=button_origin_selected.icon_id).mode = "cursor, obm"  
                
        if n > 1:
            button_origin_to_active = icons.get("icon_origin_to_active") 
            row.operator("tpc_ot.set_origin_to", text="Origin to Active", icon_value=button_origin_to_active.icon_id).mode = "COPY_ORIGIN, ORIGIN_CURSOR"   
  


    box.separator()

                        
    if context.mode == 'EDIT_MESH':
    
        row = box.column(align=True)
 
        button_origin_ccc = icons.get("icon_origin_ccc")            
        row.operator("tpc_ot.origin_ccc","3P-Circle", icon_value=button_origin_ccc.icon_id)      


    row = box.row(align=True)

    obj = context.active_object     
    if obj:                                                   
        if obj.type in {'MESH'}: 

            if context.mode == 'OBJECT':        
                row.operator("tpc_ot.snap_to_bbox", text="BoundBoxM", icon="SNAP_PEEL_OBJECT")

            row = box.row(align=True)
            if panel_prefs.display_origin_bbox:                             
                button_origin_bbox = icons.get("icon_origin_bbox")            
                row.prop(panel_prefs, "display_origin_bbox", text="BoundBoxX", icon_value=button_origin_bbox.icon_id)                                 
          
            else:               
                button_origin_bbox = icons.get("icon_origin_bbox")                
                row.prop(panel_prefs, "display_origin_bbox", text="BoundBoxX", icon_value=button_origin_bbox.icon_id)

                            
            if panel_prefs.display_origin_bbox: 
             
                box.separator()                   
                 
                box.scale_x = 0.1
                
                row = box.row(align=True)                                     
                row.alignment ='CENTER'         
                row.label(" +Y Axis")
                row.separator() 
                row.label("   xY Axis")
                row.separator()   
                row.label("--Y Axis")

                #####                  
                row = box.row(align=True)                                     
                row.alignment ='CENTER'
                 
                button_origin_left_top = icons.get("icon_origin_left_top")   
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left_top.icon_id).mode='cubeback_cornertop_minus_xy'
               
                button_origin_top = icons.get("icon_origin_top")  
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_top.icon_id).mode='cubeback_edgetop_minus_y'
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right_top.icon_id).mode='cubeback_cornertop_plus_xy'

                row.separator()
                
                button_origin_left_top = icons.get("icon_origin_left_top")   
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left_top.icon_id).mode='cubefront_edgetop_minus_x'
                
                button_origin_top = icons.get("icon_origin_top")  
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_top.icon_id).mode='cubefront_side_plus_z'
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right_top.icon_id).mode='cubefront_edgetop_plus_x'

                row.separator()
                
                button_origin_left_top = icons.get("icon_origin_left_top")   
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left_top.icon_id).mode='cubefront_cornertop_minus_xy'
                
                button_origin_top = icons.get("icon_origin_top")  
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_top.icon_id).mode='cubeback_edgetop_plus_y'
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right_top.icon_id).mode='cubefront_cornertop_plus_xy'
                
                #####

                row = box.row(align=True)                          
                row.alignment ='CENTER' 
                
                button_origin_left = icons.get("icon_origin_left")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left.icon_id).mode='cubefront_edgemiddle_minus_x'
               
                button_origin_cross = icons.get("icon_origin_cross")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_cross.icon_id).mode='cubefront_side_plus_y'
                
                button_origin_right = icons.get("icon_origin_right")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right.icon_id).mode='cubefront_edgemiddle_plus_x'

                row.separator()

                button_origin_left = icons.get("icon_origin_left")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left.icon_id).mode='cubefront_side_minus_x'
               
                if context.mode == 'OBJECT':
                    button_origin_diagonal = icons.get("icon_origin_diagonal")
                    row.operator('object.origin_set', text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'
                else:
                    button_origin_diagonal = icons.get("icon_origin_diagonal")
                    row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_diagonal.icon_id).mode='origin_set_editcenter'
                
                button_origin_right = icons.get("icon_origin_right")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right.icon_id).mode='cubefront_side_plus_x'

                row.separator()
                
                button_origin_left = icons.get("icon_origin_left")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left.icon_id).mode='cubefront_edgemiddle_minus_y'
                
                button_origin_cross = icons.get("icon_origin_cross")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_cross.icon_id).mode='cubefront_side_minus_y'
                
                button_origin_right = icons.get("icon_origin_right")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right.icon_id).mode='cubefront_edgemiddle_plus_y'

                #####

                row = box.row(align=True)
                row.alignment ='CENTER' 
                
                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left_bottom.icon_id).mode='cubeback_cornerbottom_minus_xy'
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_bottom.icon_id).mode='cubefront_edgebottom_plus_y'
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right_bottom.icon_id).mode='cubeback_cornerbottom_plus_xy'

                row.separator()
                
                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left_bottom.icon_id).mode='cubefront_edgebottom_minus_x'
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_bottom.icon_id).mode='cubefront_side_minus_z'
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right_bottom.icon_id).mode='cubefront_edgebottom_plus_x'    

                row.separator()

                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_left_bottom.icon_id).mode='cubefront_cornerbottom_minus_xy'
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_bottom.icon_id).mode='cubefront_edgebottom_minus_y'
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                row.operator('tpc_ot.origin_to_bounding_box', text="", icon_value=button_origin_right_bottom.icon_id).mode='cubefront_cornerbottom_plus_xy'

                box.separator()
                box.separator()

                row = box.row(align=True)
                row.prop(context.object, "show_bounds", text="Show Bounds") 
                row.prop(context.object, "draw_bounds_type", text="") 

                box.separator()
                box = col.box().column(align=True) 


        else:
            if context.mode == 'OBJECT':        
                row.operator("tpc_ot.snap_to_bbox", text="BoundBoxM", icon="SNAP_PEEL_OBJECT")

      


    if context.mode == 'OBJECT':  

        box.separator()          
       
        row = box.column(align=True)

        button_origin_distribute = icons.get("icon_origin_distribute")  
        row.operator("tpc_ot.distribute_objects_menu", "Distribute", icon_value=button_origin_distribute.icon_id)

        button_origin_align = icons.get("icon_origin_align")                
        row.operator("tpc_ot.advanced_align_tools", "Advanced", icon_value=button_origin_align.icon_id)    


    if context.mode in EDIT:   

        if context.mode == 'EDIT_MESH':
            pass
        else:
            box.separator()  

            row = box.column(align=True)          

            button_origin_edm = icons.get("icon_origin_edm")   
            row.operator("tpc_ot.origin_to_edit_selected","Select-EdM", icon_value=button_origin_edm.icon_id).mode="SET_EDIT"       
            
            button_origin_obj = icons.get("icon_origin_obj")   
            row.operator("tpc_ot.origin_to_edit_selected","Select-ObM", icon_value=button_origin_obj.icon_id).mode="SET_OBJECT"           

            
        box.separator()  
        
        row = box.column(align=True)          

        button_origin_mesh = icons.get("icon_origin_mesh")                
        row.operator("tpc_ot.origin_transform", "Advanced", icon_value=button_origin_mesh.icon_id)    


    box.separator()  
    
    row = box.row(align=True)         

    if panel_prefs.display_origin_zero_edm:                     
        button_align_zero = icons.get("icon_align_zero")          
        row.prop(panel_prefs, "display_origin_zero_edm", text="Zero to Axis", icon_value=button_align_zero.icon_id)                             

    else:
        button_align_zero = icons.get("icon_align_zero")              
        row.prop(panel_prefs, "display_origin_zero_edm", text="Zero to Axis", icon_value=button_align_zero.icon_id)               
                           
    if panel_prefs.display_origin_zero_edm: 

        box.separator()   

        row = box.row(align=True)
        row.prop(panel_prefs, 'tp_switch', expand=True)       
    
        box.separator() 

        row = box.row()
        row.prop(panel_prefs, 'align_x')
        row.prop(panel_prefs, 'align_y')
        row.prop(panel_prefs, 'align_z')
        
        sub = row.row(align=True)
        sub.scale_x = 0.95         
        button_origin_apply = icons.get("icon_origin_apply")  
        sub.operator("tpc_ot.zero_axis", "RUN")#, icon_value=button_origin_apply.icon_id)  
        
    box.separator() 
