# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


class VIEW3D_MT_SnapSet_Menu_Panel(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Panel"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        addon_prefs = context.preferences.addons[__package__].preferences

        if addon_prefs.tpc_use_grid == True:
            if addon_prefs.use_internal_icon_bta == True:  
                layout.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon=addon_prefs.icon_bta)
            else:
                button_snap_grid = icons.get("icon_snap_grid")
                layout.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon_value=button_snap_grid.icon_id)
 
        if addon_prefs.tpc_use_grid_modal_panel == True:
            button_snap_grid = icons.get("icon_snap_grid")
            layout.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "GRID"

                    
        if context.mode == 'OBJECT':

            if addon_prefs.tpc_use_place == True:
                if addon_prefs.use_internal_icon_btb == True:   
                    layout.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon=addon_prefs.icon_btb)
                else:
                    button_snap_place = icons.get("icon_snap_place")
                    layout.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon_value=button_snap_place.icon_id)
            
            if addon_prefs.tpc_use_grid_modal_panel == True:
                button_snap_place = icons.get("icon_snap_place")
                layout.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "PLACE"

        else:
            if addon_prefs.tpc_use_retopo == True:
                if addon_prefs.use_internal_icon_btf == True:   
                    layout.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon=addon_prefs.icon_btf)    
                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    layout.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon_value=button_snap_retopo.icon_id)    
           
            if addon_prefs.tpc_use_retopo_modal_panel == True:              
                button_snap_retopo = icons.get("icon_snap_retopo")
                layout.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "RETOPO"   
          

        if addon_prefs.use_internal_icon_btc == True:     
            layout.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon=addon_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            layout.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon_value=button_snap_cursor.icon_id) 


        if addon_prefs.use_internal_icon_bte == True:
            layout.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon=addon_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            layout.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon_value=button_snap_closest.icon_id)
            

        if addon_prefs.tpc_use_active == True: 
            if addon_prefs.use_internal_icon_btd == True:
                layout.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon=addon_prefs.icon_btd) 
            else:
                button_snap_active = icons.get("icon_snap_active")            
                layout.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon_value=button_snap_active.icon_id) 
                


def draw_snapset_ui(self, context, layout):

    icons = load_icons()
    
    addon_prefs = context.preferences.addons[__package__].preferences

    layout.operator_context = 'INVOKE_REGION_WIN'    

    col = layout.column(align=True)
 
    box = col.box().column(align=True) 

    # USE BUTTONS #
    if addon_prefs.tab_display_buttons_pl == 'on': 
              
        # NAMES / ICONS #  
        if addon_prefs.tab_display_name_pl == 'both_id':  

            tx_snapset_active = addon_prefs.name_btd
            tx_snapset_closet = addon_prefs.name_bte
            tx_snapset_cursor = addon_prefs.name_btc
            tx_snapset_grid   = addon_prefs.name_bta
            tx_snapset_place  = addon_prefs.name_btb
            tx_snapset_retopo = addon_prefs.name_btf


        if addon_prefs.tab_display_name_pl == 'icon_id':  
   
            tx_snapset_active = " "
            tx_snapset_closet = " "
            tx_snapset_cursor = " "
            tx_snapset_grid   = " "
            tx_snapset_place  = " "
            tx_snapset_retopo = " "
 

        # OPTIONS #  
        if addon_prefs.tab_display_name_pl == 'both_id':  
            row = box.column(align=True)
        else:
            row = box.row(align=True)

        #row.scale_y = 1.5
    
        if addon_prefs.tpc_use_grid == True:
            if addon_prefs.use_internal_icon_bta == True:  
                row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon=addon_prefs.icon_bta)
            else:
                button_snap_grid = icons.get("icon_snap_grid")
                row.operator("tpc_ot.snapset_button_a", text=tx_snapset_grid, icon_value=button_snap_grid.icon_id)
 
        if addon_prefs.tpc_use_grid_modal_panel == True:
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "GRID"


        if context.mode == 'OBJECT':

            if addon_prefs.tpc_use_place == True:
                if addon_prefs.use_internal_icon_btb == True:   
                    row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon=addon_prefs.icon_btb)
                else:
                    button_snap_place = icons.get("icon_snap_place")
                    row.operator("tpc_ot.snapset_button_b", text=tx_snapset_place, icon_value=button_snap_place.icon_id)
            
            if addon_prefs.tpc_use_place_modal_panel == True:
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "PLACE"

        else:
            if addon_prefs.tpc_use_retopo == True:
                if addon_prefs.use_internal_icon_btf == True:   
                    row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon=addon_prefs.icon_btf)    
                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    row.operator("tpc_ot.snapset_button_f", text=tx_snapset_retopo, icon_value=button_snap_retopo.icon_id)    
           
            if addon_prefs.tpc_use_retopo_modal_panel == True:              
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "RETOPO"  


        if addon_prefs.use_internal_icon_btc == True:     
            row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon=addon_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tpc_ot.snapset_button_c", text=tx_snapset_cursor, icon_value=button_snap_cursor.icon_id) 


        if addon_prefs.use_internal_icon_bte == True:
            row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon=addon_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tpc_ot.snapset_button_e", text=tx_snapset_closet, icon_value=button_snap_closest.icon_id)
            

        if addon_prefs.tpc_use_active == True: 
            if addon_prefs.use_internal_icon_btd == True:
                row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon=addon_prefs.icon_btd) 
            else:
                button_snap_active = icons.get("icon_snap_active")            
                row.operator("tpc_ot.snapset_button_d", text=tx_snapset_active, icon_value=button_snap_active.icon_id) 




    # USE MENUS #
    else:

        # NAMES / ICONS #  
        if addon_prefs.tab_display_name_pl == 'both_id':  
                                                
            tx_snapset = " SnapSet"
  
        if addon_prefs.tab_display_name_pl == 'icon_id':  
  
            tx_snapset = " "

       
        # OPTIONS #  
        row = box.row(align=True)

        if addon_prefs.tab_display_buttons_pl == 'off':  
            if addon_prefs.tab_display_name_pl == 'icon_id': 
                row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATE").tpc_pivot="BOUNDING_BOX_CENTER"
                row.operator("tpc_ot.set_pivot", text=" ", icon="CURSOR").tpc_pivot="CURSOR"
                row.operator("tpc_ot.set_pivot", text=" ", icon="ROTACTIVE").tpc_pivot="ACTIVE_ELEMENT"
                row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATECOLLECTION").tpc_pivot="INDIVIDUAL_ORIGINS"
                row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATECENTER").tpc_pivot="MEDIAN_POINT"  

        else:
            pass

        button_snap_set = icons.get("icon_snap_set") 
        row.menu("VIEW3D_MT_SnapSet_Menu_Panel", text= tx_snapset, icon_value=button_snap_set.icon_id) 



