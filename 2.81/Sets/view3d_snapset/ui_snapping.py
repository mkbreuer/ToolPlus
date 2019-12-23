# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
from .ui_utils import get_addon_prefs


def draw_snapset_snapping_layout(self, context):

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
    icon_snap_custom = icons.get("icon_snap_custom")   
    
    addon_prefs = get_addon_prefs()

    layout = self.layout
    
    layout.operator_context = 'INVOKE_REGION_WIN'    
          
    if addon_prefs.toggle_snapping_type in ['menu', 'buttons']: 

        tx_snapset_grid      = addon_prefs.name_bta
        tx_snapset_place     = addon_prefs.name_btb
        tx_snapset_cursor    = addon_prefs.name_btc
        tx_snapset_closet    = addon_prefs.name_btd
        tx_snapset_active    = addon_prefs.name_bte
        tx_snapset_retopo    = addon_prefs.name_btf
        tx_snapset_center    = addon_prefs.name_btg
        tx_snapset_perpendic = addon_prefs.name_bth
        tx_snapset_custom    = addon_prefs.name_btM
  
        tx_snapset_gridm      = "Grid*"
        tx_snapset_placem     = "Place*"
        tx_snapset_retopom    = "Retopo*"
        tx_snapset_centerm    = "MidPoint*"
        tx_snapset_perpendicm = "Perpendic*"
        tx_snapset_customM    = "Custom*"

    else:  
            
        tx_snapset_grid      = " "
        tx_snapset_place     = " "
        tx_snapset_cursor    = " "            
        tx_snapset_closet    = " "
        tx_snapset_active    = " "
        tx_snapset_retopo    = " "                  
        tx_snapset_center    = " "
        tx_snapset_perpendic = " "   
        tx_snapset_custom    = " "   

        tx_snapset_gridm      = " "
        tx_snapset_placem     = " "
        tx_snapset_retopom    = " "
        tx_snapset_centerm    = " "
        tx_snapset_perpendicm = " "
        tx_snapset_custoM     = " "


    if addon_prefs.toggle_snapping_type in ['buttons', 'icons']: 

        if addon_prefs.toggle_snapping_type_layout == 'column': 
            row = layout.column(align=addon_prefs.row_align_snapping_hor)    

        if addon_prefs.toggle_snapping_type_layout == 'flow': 
            row = layout.column_flow(columns=2, align=addon_prefs.row_align_snapping_hor)               

        if addon_prefs.toggle_snapping_type_layout == 'row':   
            row = layout.row(align=addon_prefs.row_align_snapping_hor)         

        if addon_prefs.toggle_snapping_type_layout == 'rows':   
            row = layout.row(align=addon_prefs.row_align_snapping_hor)         
    
    else:
        if addon_prefs.toggle_snapping_type_layout == 'column': 
            row = layout.column(align=addon_prefs.row_align_snapping_hor)    

        if addon_prefs.toggle_snapping_type_layout == 'flow': 
            row = layout.column_flow(columns=2, align=addon_prefs.row_align_snapping_hor)               

        if addon_prefs.toggle_snapping_type_layout == 'row':   
            row = layout.row(align=addon_prefs.row_align_snapping_hor)         

        if addon_prefs.toggle_snapping_type_layout == 'rows':   
            row = layout.row(align=addon_prefs.row_align_snapping_hor)        

    row.scale_y = addon_prefs.ui_scale_y_snapping

    if addon_prefs.tpc_use_grid_snapping == True:
        if addon_prefs.use_internal_icon_bta == True:  
            row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon=addon_prefs.icon_bta)
        else:
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon_value=button_snap_grid.icon_id)
 
 
    if context.mode == 'OBJECT':

        if addon_prefs.tpc_use_place_snapping == True:
            if addon_prefs.use_internal_icon_btb == True:   
                row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon=addon_prefs.icon_btb)
            else:
                row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon_value=icon_snap_place.icon_id)

    else:
        if addon_prefs.tpc_use_retopo_snapping == True:
            if addon_prefs.use_internal_icon_btf == True:   
                row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon=addon_prefs.icon_btf)    
            else:
                row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon_value=icon_snap_retopo.icon_id)    
       

    if addon_prefs.tpc_use_cursor_snapping == True:
        if addon_prefs.use_internal_icon_btc == True:     
            row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon=addon_prefs.icon_btc) 
        else:             
            row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon_value=icon_snap_cursor.icon_id) 


    if addon_prefs.tpc_use_closest_snapping == True:
        if addon_prefs.use_internal_icon_bte == True:
            row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon=addon_prefs.icon_bte)
        else:           
            row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon_value=icon_snap_closest.icon_id)

            
    if addon_prefs.toggle_snapping_type_layout == 'rows':   
        layout = self.layout.column(align=True) 
        row = layout.row(align=True)           


    if addon_prefs.tpc_use_active_snapping == True: 
        if addon_prefs.use_internal_icon_btd == True:
            row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon=addon_prefs.icon_btd) 
        else:       
            row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon_value=icon_snap_active.icon_id) 

    if addon_prefs.tpc_use_center_snapping == True: 
        if addon_prefs.use_internal_icon_btg == True:
            row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon=addon_prefs.icon_btg) 
        else:           
            row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon_value=icon_snap_center.icon_id) 

    if addon_prefs.tpc_use_perpendic_snapping == True: 
        if addon_prefs.use_internal_icon_bth == True:
            row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon=addon_prefs.icon_bth) 
        else:      
            row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon_value=icon_snap_perpendic.icon_id) 

    if addon_prefs.tpc_use_custom_snapping == True: 
        if addon_prefs.use_internal_icon_btM == True: 
            row.operator("preferences.addon_show", text=tx_snapset_custom, icon="LAYER_USED").module="view3d_snapset"                
        else:
            row.operator("preferences.addon_show", text=tx_snapset_custom, icon="LAYER_USED").module="view3d_snapset"
 

    
    # HIDDEN MODAL BUTTONS #
    """
    if addon_prefs.tpc_use_grid_modal_snapping == True:
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm).mode = "GRID"
    else:
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_gridm, icon_value=icon_snap_grid.icon_id).mode = "GRID"

    if context.mode == 'OBJECT':            
        if addon_prefs.tpc_use_place_modal_snapping == True:
            row.operator("tpc_ot.snapset_modal", text=tx_snapset_placem).mode = "PLACE"
        else:
            row.operator("tpc_ot.snapset_modal", text=tx_snapset_placem, icon_value=icon_snap_place.icon_id).mode = "PLACE"
    else:           
        if addon_prefs.tpc_use_retopo_modal_snapping == True:              
            row.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom).mode = "RETOPO"
        else:
            row.operator("tpc_ot.snapset_modal", text=tx_snapset_retopom, icon_value=icon_snap_retopo.icon_id).mode = "RETOPO"   
      
    if addon_prefs.tpc_use_center_modal_snapping == True:   
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm).mode = "CENTER"
    else:
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_centerm, icon_value=icon_snap_center.icon_id).mode = "CENTER"  
      
    if addon_prefs.tpc_use_perpendic_modal_snapping == True:   
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm).mode = "PERPENDICULAR"
    else:
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_perpendicm, icon_value=icon_snap_perpendic.icon_id).mode = "PERPENDICULAR"  
    
    if addon_prefs.tpc_use_custom_modal_snapping == True:  
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_customM).mode = "CUSTOM"  
    else:
        row.operator("tpc_ot.snapset_modal", text=tx_snapset_customM, icon_value=icon_snap_custom.icon_id).mode = "CUSTOM"  

    if addon_prefs.tpc_use_settings_snapping == True:  
        row.operator("preferences.addon_show", text="Settings").module="view3d_snapset"
    else:
        row.operator("preferences.addon_show", text="Settings", icon="LAYER_USED").module="view3d_snapset"
    """

 



# UI: SNAPPING MENU # icon_snap_perpendic
class VIEW3D_MT_snapset_menu_snapping(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_snapset_menu_snapping"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_snapping_layout(self, context)



def draw_snapset_snapping(self, context):
    layout = self.layout
    
    icons = load_icons()
    
    addon_prefs = context.preferences.addons[__package__].preferences

    layout.scale_y = addon_prefs.ui_scale_y_snapping
    
    layout.operator_context = 'INVOKE_REGION_WIN'    
    
    if addon_prefs.toggle_snapping_type in ['buttons', 'icons']: 
       
        row = layout.column(align=True)
        row.label(text="SnapSet")
       
        draw_snapset_snapping_layout(self, context)

    else:

        row = layout.row(align=True)
        
        button_snap_set = icons.get("icon_snap_set") 
        row.menu("VIEW3D_MT_snapset_menu_snapping", text= " SnapSet")#, icon_value=button_snap_set.icon_id) 
        row.operator("preferences.addon_show", text="", icon="LAYER_USED").module="view3d_snapset"




