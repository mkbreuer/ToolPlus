# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  
from .ui_utils import get_addon_prefs

def draw_snapset_menu_ui(context, layout):

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
    icon_snap_pcursor = icons.get("icon_snap_pcursor") 
    icon_snap_custom = icons.get("icon_snap_custom")    

    addon_prefs = get_addon_prefs()
   
    layout.operator_context = 'INVOKE_REGION_WIN'
 
    tx_snapset_grid      = addon_prefs.name_bta
    tx_snapset_place     = addon_prefs.name_btb
    tx_snapset_cursor    = addon_prefs.name_btc
    tx_snapset_closet    = addon_prefs.name_btd
    tx_snapset_active    = addon_prefs.name_bte
    tx_snapset_retopo    = addon_prefs.name_btf
    tx_snapset_center    = addon_prefs.name_btg
    tx_snapset_perpendic = addon_prefs.name_bth
    tx_snapset_pcursor   = addon_prefs.name_bti
    tx_snapset_custom    = addon_prefs.name_btM

    tx_snapset_gridm      = "Grid*"
    tx_snapset_placem     = "Place*"
    tx_snapset_retopom    = "Retopo*"
    tx_snapset_centerm    = "MidPoint*"
    tx_snapset_perpendicm = "Perpendic*"
    tx_snapset_pcursorm   = "PlaceCursor*"
    tx_snapset_customM    = "Custom*"
                  

    if addon_prefs.toggle_special_type_layout != 'switch': 

        if addon_prefs.toggle_special_type_layout == 'column': 

            row = layout.column(align=addon_prefs.row_align_special)    
            row.scale_y = addon_prefs.ui_scale_y_special
          

        if addon_prefs.toggle_special_type_layout == 'flow': 
          
            row = layout.column_flow(columns=2, align=addon_prefs.row_align_special)  
            row.scale_y = addon_prefs.ui_scale_y_special
         
  
        if addon_prefs.tpc_use_grid_special == True:           
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid)
            else:
                if addon_prefs.use_internal_icon_bta == True:  
                    row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon=addon_prefs.icon_bta)
                else:                
                    row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon_value=icon_snap_grid.icon_id)
     
     
        # mode switch       
        if context.mode == 'OBJECT':
            if addon_prefs.tpc_use_place_special == True:
                if addon_prefs.toggle_special_name == 'namend': 
                    row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place)
                else:
                    if addon_prefs.use_internal_icon_btb == True:   
                        row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon=addon_prefs.icon_btb)
                    else:
                        row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon_value=icon_snap_place.icon_id)
        else:
            if addon_prefs.tpc_use_retopo_special == True:
                if addon_prefs.toggle_special_name == 'namend': 
                    row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo)
                else:
                    if addon_prefs.use_internal_icon_btf == True:   
                        row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon=addon_prefs.icon_btf)    
                    else:
                        row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon_value=icon_snap_retopo.icon_id)               


       
        if addon_prefs.tpc_use_cursor_special == True:
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor)
            else:
                if addon_prefs.use_internal_icon_btc == True:     
                    row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon=addon_prefs.icon_btc) 
                else:       
                    row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon_value=icon_snap_cursor.icon_id) 

        if addon_prefs.tpc_use_closest_special == True:
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet)
            else:
                if addon_prefs.use_internal_icon_bte == True:
                    row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon=addon_prefs.icon_bte)
                else:           
                    row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon_value=icon_snap_closest.icon_id)
                

        if addon_prefs.tpc_use_active_special == True: 
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active)
            else:
                if addon_prefs.use_internal_icon_btd == True:
                    row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon=addon_prefs.icon_btd) 
                else:
                    row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon_value=icon_snap_active.icon_id) 

        if addon_prefs.tpc_use_center_special == True: 
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center)
            else:
                if addon_prefs.use_internal_icon_btg == True:
                    row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon=addon_prefs.icon_btg) 
                else:           
                    row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon_value=icon_snap_center.icon_id) 

        if addon_prefs.tpc_use_perpendic_special == True: 
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic)
            else:
                if addon_prefs.use_internal_icon_bth == True:
                    row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon=addon_prefs.icon_bth) 
                else:          
                    row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon_value=icon_snap_perpendic.icon_id) 

        if addon_prefs.tpc_use_pcursor_special == True:
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.place_cursor", text=tx_snapset_pcursor)
            else:
                if addon_prefs.use_internal_icon_bti == True:     
                    row.operator("tpc_ot.place_cursor", text=tx_snapset_pcursor, icon=addon_prefs.icon_bti) 
                else:       
                    row.operator("tpc_ot.place_cursor", text=tx_snapset_pcursor, icon_value=icon_snap_pcursor.icon_id) 




        if addon_prefs.toggle_special_type_layout == 'flow': 
            row.label(text='')
       
        if addon_prefs.toggle_special_type_layout == 'column':            
            if addon_prefs.tpc_use_separator_modal_special == True:             
                row.separator()

        # MODAL BUTTONS #
        if addon_prefs.tpc_use_grid_modal_special == True:
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm).mode = "GRID"
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm, icon_value=icon_snap_grid.icon_id).mode = "GRID"

        if context.mode == 'OBJECT':            
            if addon_prefs.tpc_use_place_modal_special == True:
                if addon_prefs.toggle_special_name == 'namend': 
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_placem).mode = "PLACE"
                else:
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_placem, icon_value=icon_snap_place.icon_id).mode = "PLACE"
        else:           
            if addon_prefs.tpc_use_retopo_modal_special == True:              
                if addon_prefs.toggle_special_name == 'namend': 
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom).mode = "RETOPO"
                else:
                    row.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom, icon_value=icon_snap_retopo.icon_id).mode = "RETOPO"   
          
        if addon_prefs.tpc_use_center_modal_special == True:   
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm).mode = "CENTER"
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm, icon_value=icon_snap_center.icon_id).mode = "CENTER"  
          
        if addon_prefs.tpc_use_perpendic_modal_special == True:  
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm).mode = "PERPENDICULAR"
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm, icon_value=icon_snap_perpendic.icon_id).mode = "PERPENDICULAR"                  

        if addon_prefs.tpc_use_pcursor_modal_special == True:  
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.place_cursor_modal", text=tx_snapset_pcursorm) 
            else:
                row.operator("tpc_ot.place_cursor_modal", text=tx_snapset_pcursorm, icon_value=icon_snap_pcursor.icon_id)
       
        if addon_prefs.tpc_use_custom_modal_special == True:  
            if addon_prefs.toggle_special_name == 'namend': 
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_customM).mode = "CUSTOM"  
            else:
                row.operator("tpc_ot.snapset_modal", text=tx_snapset_customM, icon_value=icon_snap_custom.icon_id).mode = "CUSTOM"  

        if addon_prefs.tpc_use_settings_special == True:  
            if addon_prefs.toggle_special_type_layout == 'column':                 
                if addon_prefs.tpc_use_separator_settings_special == True:  
                    row.separator()

            if addon_prefs.toggle_special_name == 'namend':         
                row.operator("preferences.addon_show", text="Settings").module="view3d_snapset"
            else:
                row.operator("preferences.addon_show", text="Settings", icon="LAYER_USED").module="view3d_snapset"






    if addon_prefs.toggle_special_type_layout == 'switch': 

        # DIRECT VERSION #
        if addon_prefs.toggle_layout_type == True:
                         
            if addon_prefs.tpc_use_grid == True:           
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid)
                else:
                    if addon_prefs.use_internal_icon_bta == True:  
                        layout.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon=addon_prefs.icon_bta)
                    else:                
                        layout.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon_value=icon_snap_grid.icon_id)
         
         
            # mode switch       
            if context.mode == 'OBJECT':
                if addon_prefs.tpc_use_place == True:
                    if addon_prefs.toggle_special_name == 'namend': 
                        layout.operator("tpc_ot.snapset_button_b", text=tx_snapset_place)
                    else:
                        if addon_prefs.use_internal_icon_btb == True:   
                            layout.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon=addon_prefs.icon_btb)
                        else:
                            layout.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon_value=icon_snap_place.icon_id)
            else:
                if addon_prefs.tpc_use_retopo == True:
                    if addon_prefs.toggle_special_name == 'namend': 
                        layout.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo)
                    else:
                        if addon_prefs.use_internal_icon_btf == True:   
                            layout.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon=addon_prefs.icon_btf)    
                        else:
                            layout.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon_value=icon_snap_retopo.icon_id)               


           
            if addon_prefs.tpc_use_cursor == True:
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor)
                else:
                    if addon_prefs.use_internal_icon_btc == True:     
                        layout.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon=addon_prefs.icon_btc) 
                    else:       
                        layout.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon_value=icon_snap_cursor.icon_id) 

            if addon_prefs.tpc_use_closest == True:
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet)
                else:
                    if addon_prefs.use_internal_icon_bte == True:
                        layout.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon=addon_prefs.icon_bte)
                    else:           
                        layout.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon_value=icon_snap_closest.icon_id)
                    

            if addon_prefs.tpc_use_active == True: 
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_button_d", text=tx_snapset_active)
                else:
                    if addon_prefs.use_internal_icon_btd == True:
                        layout.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon=addon_prefs.icon_btd) 
                    else:
                        layout.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon_value=icon_snap_active.icon_id) 

            if addon_prefs.tpc_use_center == True: 
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_button_g", text=tx_snapset_center)
                else:
                    if addon_prefs.use_internal_icon_btg == True:
                        layout.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon=addon_prefs.icon_btg) 
                    else:           
                        layout.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon_value=icon_snap_center.icon_id) 

            if addon_prefs.tpc_use_perpendic == True: 
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic)
                else:
                    if addon_prefs.use_internal_icon_bth == True:
                        layout.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon=addon_prefs.icon_bth) 
                    else:          
                        layout.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon_value=icon_snap_perpendic.icon_id) 
            
            if addon_prefs.tpc_use_pcursor == True: 
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.place_cursor", text=tx_snapset_pcursor)
                else:
                    if addon_prefs.use_internal_icon_bti == True:
                        layout.operator("tpc_ot.place_cursor", text=tx_snapset_pcursor, icon=addon_prefs.icon_bti) 
                    else:          
                        layout.operator("tpc_ot.place_cursor", text=tx_snapset_pcursor, icon_value=icon_snap_pcursor.icon_id)   
  

        else:

            # MODAL BUTTONS #
            if addon_prefs.tpc_use_grid_modal == True:
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm).mode = "GRID"
                else:
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm, icon_value=icon_snap_grid.icon_id).mode = "GRID"

            if context.mode == 'OBJECT':            
                if addon_prefs.tpc_use_place_modal == True:
                    if addon_prefs.toggle_special_name == 'namend': 
                        layout.operator("tpc_ot.snapset_modal", text=tx_snapset_placem).mode = "PLACE"
                    else:
                        layout.operator("tpc_ot.snapset_modal", text=tx_snapset_placem, icon_value=icon_snap_place.icon_id).mode = "PLACE"
            else:           
                if addon_prefs.tpc_use_retopo_modal == True:              
                    if addon_prefs.toggle_special_name == 'namend': 
                        layout.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom).mode = "RETOPO"
                    else:
                        layout.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom, icon_value=icon_snap_retopo.icon_id).mode = "RETOPO"   
              
            if addon_prefs.tpc_use_center_modal == True:   
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm).mode = "CENTER"
                else:
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm, icon_value=icon_snap_center.icon_id).mode = "CENTER"  
              
            if addon_prefs.tpc_use_perpendic_modal == True:  
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm).mode = "PERPENDICULAR"
                else:
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm, icon_value=icon_snap_perpendic.icon_id).mode = "PERPENDICULAR"  

            if addon_prefs.tpc_use_pcursor_modal_special == True:  
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.place_cursor_modal", text=tx_snapset_pcursorm) 
                else:
                    layout.operator("tpc_ot.place_cursor_modal", text=tx_snapset_pcursorm, icon_value=icon_snap_pcursor.icon_id)

            if addon_prefs.tpc_use_custom_modal == True:  
                if addon_prefs.toggle_special_name == 'namend': 
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_customM).mode = "CUSTOM"  
                else:
                    layout.operator("tpc_ot.snapset_modal", text=tx_snapset_customM, icon_value=icon_snap_custom.icon_id).mode = "CUSTOM"  

 

        if addon_prefs.tpc_use_separator_settings_special == True:              
            layout.separator()

        if addon_prefs.tpc_use_settings_special == True:          
            if addon_prefs.toggle_special_name == 'namend':         
                layout.operator("preferences.addon_show", text="Settings").module="view3d_snapset"
            else:
                layout.operator("preferences.addon_show", text="Settings", icon="LAYER_USED").module="view3d_snapset"

        layout.prop(addon_prefs, "toggle_layout_type", text="", icon='GRIP')
        #layout.popover(panel="VIEW3D_PT_snapset_header_panel", text=" SnapSet")            



# UI: HOTKEY MENU # 
class VIEW3D_MT_snapset_menu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_snapset_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(context, layout)
        #layout.popover(panel="VIEW3D_PT_snapset_panel_ui", text="Menu Panel")  


class VIEW3D_MT_snapset_menu_panel(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_snapset_menu_panel"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(context, layout)


# LAYOUT # 
def draw_snapset_item_special(self, context):
    layout = self.layout

    icons = load_icons()

    addon_prefs = get_addon_prefs()
  
    if addon_prefs.toggle_special_type == 'append':
        if addon_prefs.toggle_special_separator == True:
            layout.separator()      

    if addon_prefs.toggle_special_icon == True:
        button_snap_set = icons.get("icon_snap_set")
        layout.menu("VIEW3D_MT_snapset_menu_special", text="SnapSet", icon_value=button_snap_set.icon_id)      
    else:
        layout.menu("VIEW3D_MT_snapset_menu_special", text="SnapSet")      
    
    if addon_prefs.toggle_special_type == 'prepend':
        if addon_prefs.toggle_special_separator == True:
            layout.separator()      

            
# MENU # 
class VIEW3D_MT_snapset_menu_special(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_snapset_menu_special"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(context, layout)










                  




        