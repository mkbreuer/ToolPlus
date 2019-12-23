# LOAD UI #   
from view3d_snapset.ui_menu import VIEW3D_MT_snapset_menu_panel

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
from .ui_utils import get_addon_prefs

# ADDON CHECK #
import addon_utils  

def draw_snapset_ui(context, layout):
    icons = load_icons()
    
    addon_prefs = get_addon_prefs()
    snap_global = context.window_manager.snap_global_props    

    layout.scale_y = addon_prefs.ui_scale_y_panel
    
    layout.operator_context = 'INVOKE_REGION_WIN'    

    col = layout.column(align=True)
 
    box = col.box().column(align=True) 

    # USE BUTTONS #
    if addon_prefs.toggle_display_buttons_pl == 'on': 
              
        # NAMES / ICONS #  
        if addon_prefs.toggle_display_name_pl == 'both_id':  

            tx_snapset_grid      = addon_prefs.name_bta
            tx_snapset_place     = addon_prefs.name_btb
            tx_snapset_cursor    = addon_prefs.name_btc
            tx_snapset_active    = addon_prefs.name_btd
            tx_snapset_closet    = addon_prefs.name_bte
            tx_snapset_retopo    = addon_prefs.name_btf
            tx_snapset_center    = addon_prefs.name_btg
            tx_snapset_perpendic = addon_prefs.name_bth

        if addon_prefs.toggle_display_name_pl == 'icon_id':  
   
            tx_snapset_grid      = " "
            tx_snapset_place     = " "
            tx_snapset_cursor    = " "
            tx_snapset_active    = " "
            tx_snapset_closet    = " "
            tx_snapset_retopo    = " "
            tx_snapset_center    = " "
            tx_snapset_perpendic = " " 

 
        if snap_global.toggle_dropdown == False:        

            row = box.row(align=True)
            row.label(text="Durables")     

            # DURABLE #  
            if addon_prefs.toggle_display_name_pl == 'both_id':  
                row = box.column(align=True)
            else:
                row = box.row(align=True)
        
            if addon_prefs.tpc_use_grid == True:
                if addon_prefs.use_internal_icon_bta == True:  
                    row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon=addon_prefs.icon_bta)
                else:
                    button_snap_grid = icons.get("icon_snap_grid")
                    row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon_value=button_snap_grid.icon_id)

            if context.mode == 'OBJECT':
                if addon_prefs.tpc_use_place == True:
                    if addon_prefs.use_internal_icon_btb == True:   
                        row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon=addon_prefs.icon_btb)
                    else:
                        button_snap_place = icons.get("icon_snap_place")
                        row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon_value=button_snap_place.icon_id)
            else:
                if addon_prefs.tpc_use_retopo == True:
                    if addon_prefs.use_internal_icon_btf == True:   
                        row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon=addon_prefs.icon_btf)    
                    else:
                        button_snap_retopo = icons.get("icon_snap_retopo")
                        row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon_value=button_snap_retopo.icon_id)    

            if addon_prefs.tpc_use_cursor == True:
                if addon_prefs.use_internal_icon_btc == True:     
                    row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon=addon_prefs.icon_btc) 
                else:       
                    button_snap_cursor = icons.get("icon_snap_cursor")           
                    row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon_value=button_snap_cursor.icon_id)          

            if addon_prefs.tpc_use_active == True: 
                if addon_prefs.use_internal_icon_btd == True:
                    row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon=addon_prefs.icon_btd) 
                else:
                    button_snap_active = icons.get("icon_snap_active")            
                    row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon_value=button_snap_active.icon_id) 

            if addon_prefs.tpc_use_closest == True:
                if addon_prefs.use_internal_icon_bte == True:
                    row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon=addon_prefs.icon_bte)
                else:           
                    button_snap_closest = icons.get("icon_snap_closest")
                    row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon_value=button_snap_closest.icon_id)      

            if addon_prefs.tpc_use_center == True: 
                if addon_prefs.use_internal_icon_btg == True:
                    row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon=addon_prefs.icon_btg) 
                else:
                    icon_snap_center = icons.get("icon_snap_center")            
                    row.operator("tpc_ot.snapset_button_g", text=tx_snapset_center, icon_value=icon_snap_center.icon_id) 

            if addon_prefs.tpc_use_perpendic == True: 
                if addon_prefs.use_internal_icon_bth == True:
                    row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon=addon_prefs.icon_bth) 
                else:
                    icon_snap_perpendic = icons.get("icon_snap_perpendic")            
                    row.operator("tpc_ot.snapset_button_h", text=tx_snapset_perpendic, icon_value=icon_snap_perpendic.icon_id) 
            
            #row.operator("tpc_ot.cursor_object_align") 

        else:          
            row = box.row(align=True)
            row.label(text="Modals*")               
                       
            row = box.column(align=True)
     
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tpc_ot.snapset_modal", text="Grid*", icon_value=button_snap_grid.icon_id).mode = "GRID"
            
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tpc_ot.snapset_modal", text="Place*", icon_value=button_snap_place.icon_id).mode = "PLACE"

            if context.mode == 'EDIT_MESH':       
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tpc_ot.snapset_modal", text="Retopo*", icon_value=button_snap_retopo.icon_id).mode = "RETOPO"          
                           
            icon_snap_center = icons.get("icon_snap_center")
            row.operator("tpc_ot.snapset_modal", text="MidPoint*", icon_value=icon_snap_center.icon_id).mode = "CENTER"  
          
            icon_snap_perpendic = icons.get("icon_snap_perpendic")
            row.operator("tpc_ot.snapset_modal", text="Perpendic*", icon_value=icon_snap_perpendic.icon_id).mode = "PERPENDICULAR"  

            icon_snap_custom = icons.get("icon_snap_custom")    
            row.operator("tpc_ot.snapset_modal", text="Custom*", icon_value=icon_snap_custom.icon_id).mode = "CUSTOM"  



    # USE MENUS #
    else:

        # NAMES / ICONS #  
        if addon_prefs.toggle_display_name_pl == 'both_id':  
                                                
            tx_snapset = " SnapSet"
  
        if addon_prefs.toggle_display_name_pl == 'icon_id':  
  
            tx_snapset = " "
      
        # OPTIONS #  
        row = box.row(align=True)

        if addon_prefs.toggle_display_buttons_pl == 'off':  
            if addon_prefs.toggle_display_name_pl == 'icon_id': 
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_BOUNDBOX").tpc_pivot="BOUNDING_BOX_CENTER"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_CURSOR").tpc_pivot="CURSOR"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_ACTIVE").tpc_pivot="ACTIVE_ELEMENT"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_INDIVIDUAL").tpc_pivot="INDIVIDUAL_ORIGINS"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_MEDIAN").tpc_pivot="MEDIAN_POINT"   
        else:
            pass

        row.menu("VIEW3D_MT_snapset_menu_panel", text= tx_snapset, icon='SNAP_OFF') 


    col = layout.row(align=True)
    col.scale_y = 0.8    
    col.operator("preferences.addon_show", text=" ", icon="LAYER_USED").module="view3d_snapset"

    if addon_prefs.toggle_display_buttons_pl == 'on': 
             
        if snap_global.toggle_dropdown == True:        
            col.prop(snap_global, "toggle_dropdown", text=" ", icon="PINNED")
        else:
            col.prop(snap_global, "toggle_dropdown", text=" ", icon="UNPINNED")


