# LOAD UI #   
from view3d_snapset.ui_menu import draw_snapset_menu_ui

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  
from .ui_utils import get_addon_prefs

def draw_snapset_item_editor(self, context):
    layout = self.layout    
   
    addon_prefs = get_addon_prefs()    

    row = layout.row(align=addon_prefs.row_align)     
    
    if addon_prefs.toggle_editor_layout_scale_x == True:
        row.scale_x = addon_prefs.ui_scale_x_editor
   
    if addon_prefs.toggle_editor_layout_scale_y == True:
        row.scale_y = addon_prefs.ui_scale_y_editor
  
    icons = load_icons()
    icon_snap_set = icons.get("icon_snap_set")

    icon_snap_grid = icons.get("icon_snap_grid")            
    icon_snap_place = icons.get("icon_snap_place")
    icon_snap_retopo = icons.get("icon_snap_retopo")
    icon_snap_cursor = icons.get("icon_snap_cursor")           
    icon_snap_closest = icons.get("icon_snap_closest")
    icon_snap_active = icons.get("icon_snap_active")  
    icon_snap_center = icons.get("icon_snap_center")
    icon_snap_perpendic = icons.get("icon_snap_perpendic")   

    # layout spacer
    if addon_prefs.toggle_editor_separator_prepend == True:
        row.separator(factor=addon_prefs.factor_separator_prepend)      


    # USE BUTTONS #
    if addon_prefs.toggle_editor_layout == 'buttons':
                  
        # NAMES / ICONS #  
        if addon_prefs.toggle_editor_menu_name == 'icon':  

            if addon_prefs.toggle_editor_layout_scale_x == False:
            
                tx_snapset_grid      = ""
                tx_snapset_place     = ""
                tx_snapset_cursor    = ""
                tx_snapset_closet    = ""
                tx_snapset_active    = ""
                tx_snapset_retopo    = ""
                tx_snapset_center    = ""
                tx_snapset_perpendic = ""              

                tx_snapset_gridm      = ""
                tx_snapset_placem     = ""
                tx_snapset_retopom    = ""
                tx_snapset_centerm    = ""
                tx_snapset_perpendicm = ""

            else:
            
                # for x scale
                tx_snapset_grid      = " "
                tx_snapset_place     = " "
                tx_snapset_cursor    = " "            
                tx_snapset_closet    = " "
                tx_snapset_active    = " "
                tx_snapset_retopo    = " "                  
                tx_snapset_center    = " "
                tx_snapset_perpendic = " "   
     
                tx_snapset_gridm      = " "
                tx_snapset_placem     = " "
                tx_snapset_retopom    = " "  
                tx_snapset_centerm    = " "
                tx_snapset_perpendicm = " "
     

        if addon_prefs.toggle_editor_menu_name in ['namend', 'both']:  
            
            tx_snapset_grid      = addon_prefs.name_bta
            tx_snapset_place     = addon_prefs.name_btb
            tx_snapset_cursor    = addon_prefs.name_btc
            tx_snapset_closet    = addon_prefs.name_btd
            tx_snapset_active    = addon_prefs.name_bte
            tx_snapset_retopo    = addon_prefs.name_btf
            tx_snapset_center    = addon_prefs.name_btg
            tx_snapset_perpendic = addon_prefs.name_bth

            tx_snapset_gridm      = "Grid*"
            tx_snapset_placem     = "Place*"
            tx_snapset_retopom    = "Retopo*"
            tx_snapset_centerm    = "MidPoint*"
            tx_snapset_perpendicm = "Perpendic*"

                      
        if addon_prefs.tpc_use_grid_editor == True:           
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid)
            else:
                if addon_prefs.use_internal_icon_bta == True:  
                    row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid , icon=addon_prefs.icon_bta)
                else:                
                    row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon_value=icon_snap_grid.icon_id)
     
     
        # mode switch       
        if context.mode == 'OBJECT':
            if addon_prefs.tpc_use_place_editor == True:
                if addon_prefs.toggle_editor_menu_name == 'namend': 
                    row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place)
                else:
                    if addon_prefs.use_internal_icon_btb == True:   
                        row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon=addon_prefs.icon_btb)
                    else:
                        row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon_value=icon_snap_place.icon_id)
        else:
            if addon_prefs.tpc_use_retopo_editor == True:
                if addon_prefs.toggle_editor_menu_name == 'namend': 
                    row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo)
                else:
                    if addon_prefs.use_internal_icon_btf == True:   
                        row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon=addon_prefs.icon_btf)    
                    else:
                        row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon_value=icon_snap_retopo.icon_id)               


       
        if addon_prefs.tpc_use_cursor_editor == True:
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor)
            else:
                if addon_prefs.use_internal_icon_btc == True:     
                    row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon=addon_prefs.icon_btc) 
                else:       
                    row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon_value=icon_snap_cursor.icon_id) 

        if addon_prefs.tpc_use_closest_editor == True:
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet)
            else:
                if addon_prefs.use_internal_icon_bte == True:
                    row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon=addon_prefs.icon_bte)
                else:           
                    row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon_value=icon_snap_closest.icon_id)
                

        if addon_prefs.tpc_use_active_editor == True: 
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active)
            else:
                if addon_prefs.use_internal_icon_btd == True:
                    row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon=addon_prefs.icon_btd) 
                else:
                    row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon_value=icon_snap_active.icon_id) 

        if addon_prefs.tpc_use_center_editor == True: 
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center)
            else:
                if addon_prefs.use_internal_icon_btg == True:
                    row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon=addon_prefs.icon_btg) 
                else:           
                    row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon_value=icon_snap_center.icon_id) 

        if addon_prefs.tpc_use_perpendic_editor == True: 
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic)
            else:
                if addon_prefs.use_internal_icon_bth == True:
                    row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon=addon_prefs.icon_bth) 
                else:          
                    row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon_value=icon_snap_perpendic.icon_id) 


     
        # MODAL BUTTONS #
        if addon_prefs.tpc_use_grid_modal_editor == True:
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm).mode = "GRID"
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm, icon_value=icon_snap_grid.icon_id).mode = "GRID"

        if context.mode == 'OBJECT':            
            if addon_prefs.tpc_use_place_modal_editor == True:
                if addon_prefs.toggle_editor_menu_name == 'namend': 
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_placem).mode = "PLACE"
                else:
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_placem, icon_value=icon_snap_place.icon_id).mode = "PLACE"
        else:           
            if addon_prefs.tpc_use_retopo_modal_editor == True:              
                if addon_prefs.toggle_editor_menu_name == 'namend': 
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom).mode = "RETOPO"
                else:
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom, icon_value=icon_snap_retopo.icon_id).mode = "RETOPO"   
          
        if addon_prefs.tpc_use_center_modal_editor == True:   
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm).mode = "CENTER"
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm, icon_value=icon_snap_center.icon_id).mode = "CENTER"  
          
        if addon_prefs.tpc_use_perpendic_modal_editor == True:  
            if addon_prefs.toggle_editor_menu_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm).mode = "PERPENDICULAR"
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm, icon_value=icon_snap_perpendic.icon_id).mode = "PERPENDICULAR"  


    # USE PANEL #
    if addon_prefs.toggle_editor_layout == 'panel':
        
        if addon_prefs.toggle_editor_menu_name == 'icon':            
            row.popover(panel="VIEW3D_PT_snapset_panel_ui", text="", icon_value=icon_snap_set.icon_id) 

        if addon_prefs.toggle_editor_menu_name == 'namend':            
            row.popover(panel="VIEW3D_PT_snapset_panel_ui", text="SnapSet")   

        if addon_prefs.toggle_editor_menu_name == 'both':                         
            row.popover(panel="VIEW3D_PT_snapset_panel_ui", text=" SnapSet", icon_value=icon_snap_set.icon_id)    


    # USE MENUS #
    if addon_prefs.toggle_editor_layout == 'menu':

        if addon_prefs.toggle_editor_menu_name == 'icon':            
            row.menu("VIEW3D_MT_snapset_menu_editor", text="", icon_value=icon_snap_set.icon_id) 

        if addon_prefs.toggle_editor_menu_name == 'namend':            
            row.menu("VIEW3D_MT_snapset_menu_editor", text="SnapSet")   

        if addon_prefs.toggle_editor_menu_name == 'both':                         
            row.menu("VIEW3D_MT_snapset_menu_editor", text=" SnapSet", icon_value=icon_snap_set.icon_id)    



    # layout spacer
    if addon_prefs.toggle_editor_separator_append == True:
        row.separator(factor=addon_prefs.factor_separator_append)      
   


class VIEW3D_PT_snapset_panel_editor(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_label = "Snapset"
    #bl_ui_units_x = 8

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(context, layout)


# UI: HEADER MENU # 
class VIEW3D_HT_snapset_header(bpy.types.Header):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    @classmethod
    def poll(self, context):
       return 
       
    def draw(self, context):
        layout = self.layout.row(align=True) 
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_item_editor(self, context)


            
# UI: EDITOR MENU # 
class VIEW3D_MT_snapset_menu_editor(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_snapset_menu_editor"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(context, layout)







