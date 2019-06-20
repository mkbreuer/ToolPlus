# LOAD UI #   
from view3d_snapset.ui_menu import VIEW3D_MT_SnapSet_Menu


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  



# UI: MENU FOR HEADER (HIDDEN) # 
class VIEW3D_MT_SnapSet_Options_Menu(bpy.types.Menu):
    bl_label = "SnapSet Options"
    bl_idname = "VIEW3D_MT_SnapSet_Options_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        addon_prefs = context.preferences.addons[__package__].preferences   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = addon_prefs.ui_scale_y     

        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')   

        layout.separator() 

        layout.prop(addon_prefs, 'tab_display_name', text="")
        
        layout.separator()  
    
        layout.prop(addon_prefs, 'tab_display_buttons', text="")




def draw_snapset_header_layout(self, context, layout):
          
    icons = load_icons()
    
    addon_prefs = context.preferences.addons[__package__].preferences

    layout.scale_y = addon_prefs.ui_scale_y

    # USE BUTTONS #
    if addon_prefs.tab_display_buttons == 'on': 
                  
        # NAMES / ICONS #  
        if addon_prefs.tab_display_name == 'both_id':  

            tx_snapset_grid   = "Grid"
            tx_snapset_place  = "Place"
            tx_snapset_retopo = "Retopo"
            tx_snapset_cursor = "Cursor"
            tx_snapset_active = "Active"
            tx_snapset_closet = "Closest"

        if addon_prefs.tab_display_name == 'icon_id':  
   
            if addon_prefs.tab_header_type == 'buttons': 

                tx_snapset_active = ""
                tx_snapset_closet = ""
                tx_snapset_cursor = ""
                tx_snapset_grid   = ""
                tx_snapset_place  = ""
                tx_snapset_retopo = ""
           
            else:
                
                tx_snapset_active = " "
                tx_snapset_closet = " "
                tx_snapset_cursor = " "
                tx_snapset_grid   = " "
                tx_snapset_place  = " "
                tx_snapset_retopo = " "
 


        # OPTIONS #  
        if addon_prefs.tab_layout_direction == True: 
            row = layout.row(align=True)
        else:
            row = layout.column(align=True)            
            
        button_snap_active = icons.get("icon_snap_active")
        row.operator("tpc_ot.snapset_button_d", text= tx_snapset_active, icon_value=button_snap_active.icon_id) 

        button_snap_closest = icons.get("icon_snap_closest")
        row.operator("tpc_ot.snapset_button_e", text= tx_snapset_closet, icon_value=button_snap_closest.icon_id)

        button_snap_cursor = icons.get("icon_snap_cursor")           
        row.operator("tpc_ot.snapset_button_c", text= tx_snapset_cursor, icon_value=button_snap_cursor.icon_id) 
 
        button_snap_grid = icons.get("icon_snap_grid")
        row.operator("tpc_ot.snapset_button_a", text= tx_snapset_grid, icon_value=button_snap_grid.icon_id)
                    
        if context.mode == 'OBJECT':
            button_snap_place = icons.get("icon_snap_place")
            row.operator("tpc_ot.snapset_button_b", text= tx_snapset_place, icon_value=button_snap_place.icon_id)

        else:
            button_snap_retopo = icons.get("icon_snap_retopo")
            row.operator("tpc_ot.snapset_button_f", text= tx_snapset_retopo, icon_value=button_snap_retopo.icon_id)    
        
        if addon_prefs.tab_layout_direction == True:  
            if addon_prefs.tab_display_name == 'icon_id':             
                    
                layout.separator() 
              
                row = layout.row(align=True) 
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_BOUNDBOX").tpc_pivot="BOUNDING_BOX_CENTER"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_CURSOR").tpc_pivot="CURSOR"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_ACTIVE").tpc_pivot="ACTIVE_ELEMENT"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_INDIVIDUAL").tpc_pivot="INDIVIDUAL_ORIGINS"
                row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_MEDIAN").tpc_pivot="MEDIAN_POINT"  



    # USE MENUS #
    else:

        # NAMES / ICONS #  
        if addon_prefs.tab_display_name == 'both_id':  
                                                
            tx_snapset = " SnapSet"
  
        if addon_prefs.tab_display_name == 'icon_id':  
  
            tx_snapset = ""

       
        # OPTIONS #  
        layout = layout.row(align=True)

        button_snap_set = icons.get("icon_snap_set") 
        layout.menu("VIEW3D_MT_SnapSet_Menu", text= tx_snapset, icon_value=button_snap_set.icon_id) 




# UI: HEADER MENU # 
class VIEW3D_MT_SnapSet_Header_Menu(bpy.types.Menu):
    bl_label = " SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Header_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'       
        
        draw_snapset_header_layout(self, context, layout)


# UI: HEADER PANEL # 
class VIEW3D_PT_SnapSet_Header_Panel(bpy.types.Panel):
    bl_label = " SnapSet"
    bl_idname = "VIEW3D_PT_SnapSet_Header_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
  
    def draw(self, context):
        layout = self.layout.box().column(align=True)
        layout.operator_context = 'INVOKE_REGION_WIN'       
        
        draw_snapset_header_layout(self, context, layout)



# UI: HEADER LAYOUT # 
class VIEW3D_HT_SnapSet_Header_Menu(bpy.types.Header):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    @classmethod
    def poll(self, context):
       return s
       
    def draw(self, context):
        layout = self.layout        
     
        layout.operator_context = 'INVOKE_REGION_WIN'    

        icons = load_icons()

        addon_prefs = context.preferences.addons[__package__].preferences
                
        button_snap_set = icons.get("icon_snap_set")                

        if addon_prefs.tab_header_type == 'menu':                        
            if addon_prefs.tab_header_text == True:                        
                layout.menu("VIEW3D_MT_SnapSet_Header_Menu", text=" SnapSet", icon_value=button_snap_set.icon_id)      
            else:
                layout.menu("VIEW3D_MT_SnapSet_Header_Menu", text="", icon_value=button_snap_set.icon_id)               
      
        elif addon_prefs.tab_header_type == 'panel':  
            if addon_prefs.tab_header_text == True:  
                layout.popover(panel="VIEW3D_PT_SnapSet_Header_Panel", text=" SnapSet", icon_value=button_snap_set.icon_id)
            else:
                layout.popover(panel="VIEW3D_PT_SnapSet_Header_Panel", text="", icon_value=button_snap_set.icon_id)

        elif addon_prefs.tab_header_type == 'buttons':                        
            draw_snapset_header_layout(self, context, layout)