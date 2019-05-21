# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


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
       
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5      

        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')   

        layout.separator() 

        layout.prop(panel_prefs, 'tab_display_name', text="")
        
        layout.separator()  
    
        layout.prop(panel_prefs, 'tab_display_buttons', text="")



class VIEW3D_MT_SnapSet_Header_Menu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Header_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        menu_prefs = context.user_preferences.addons[__package__].preferences

        if menu_prefs.tpc_use_grid == True:
            if menu_prefs.use_internal_icon_bta == True:  
                layout.operator("tpc_ot.snapset_button_a", text=menu_prefs.name_bta, icon=menu_prefs.icon_bta)
            else:
                button_snap_grid = icons.get("icon_snap_grid")
                layout.operator("tpc_ot.snapset_button_a", text=menu_prefs.name_bta, icon_value=button_snap_grid.icon_id)
 
        if menu_prefs.tpc_use_grid_modal == True:
            button_snap_grid = icons.get("icon_snap_grid")
            layout.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "grid"

                    
        if context.mode == 'OBJECT':

            if menu_prefs.tpc_use_place == True:
                if menu_prefs.use_internal_icon_btb == True:   
                    layout.operator("tpc_ot.snapset_button_b", text=menu_prefs.name_btb, icon=menu_prefs.icon_btb)
                else:
                    button_snap_place = icons.get("icon_snap_place")
                    layout.operator("tpc_ot.snapset_button_b", text=menu_prefs.name_btb, icon_value=button_snap_place.icon_id)
            
            if menu_prefs.tpc_use_place_modal == True:
                button_snap_place = icons.get("icon_snap_place")
                layout.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "place"

        else:
            if menu_prefs.tpc_use_retopo == True:
                if menu_prefs.use_internal_icon_btf == True:   
                    layout.operator("tpc_ot.snapset_button_f", text=menu_prefs.name_btf, icon=menu_prefs.icon_btf)    
                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    layout.operator("tpc_ot.snapset_button_f", text=menu_prefs.name_btf, icon_value=button_snap_retopo.icon_id)    
           
            if menu_prefs.tpc_use_retopo_modal == True:              
                button_snap_retopo = icons.get("icon_snap_retopo")
                layout.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "retopo"   
          

        if menu_prefs.use_internal_icon_btc == True:     
            layout.operator("tpc_ot.snapset_button_c", text=menu_prefs.name_btc, icon=menu_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            layout.operator("tpc_ot.snapset_button_c", text=menu_prefs.name_btc, icon_value=button_snap_cursor.icon_id) 


        if menu_prefs.use_internal_icon_bte == True:
            layout.operator("tpc_ot.snapset_button_e", text=menu_prefs.name_bte, icon=menu_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            layout.operator("tpc_ot.snapset_button_e", text=menu_prefs.name_bte, icon_value=button_snap_closest.icon_id)
            

        if menu_prefs.tpc_use_active == True: 
            if menu_prefs.use_internal_icon_btd == True:
                layout.operator("tpc_ot.snapset_button_d", text=menu_prefs.name_btd, icon=menu_prefs.icon_btd) 
            else:
                button_snap_active = icons.get("icon_snap_active")            
                layout.operator("tpc_ot.snapset_button_d", text=menu_prefs.name_btd, icon_value=button_snap_active.icon_id) 
 



# UI: HEADER MENU # 
class VIEW3D_HT_SnapSet_Header_Menu(bpy.types.Header):
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
       return 
       
    def draw(self, context):
        layout = self.layout       

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5

        # USE BUTTONS #
        display_buttons = context.user_preferences.addons[__package__].preferences.tab_display_buttons
        if display_buttons == 'on': 
           
           
            # NAMES / ICONS #  
            display_name = context.user_preferences.addons[__package__].preferences.tab_display_name
            if display_name == 'both_id':  

                tx_snapset_active = "Active"
                tx_snapset_closet = "Closest"
                tx_snapset_cursor = "Cursor3D"
                tx_snapset_grid   = "Grid"
                tx_snapset_place  = "Place"
                tx_snapset_retopo = "Retopo"


            if display_name == 'icon_id':  
       
                tx_snapset_active = ""
                tx_snapset_closet = ""
                tx_snapset_cursor = ""
                tx_snapset_grid   = ""
                tx_snapset_place  = ""
                tx_snapset_retopo = ""
 

            # OPTIONS #  
            row = layout.row(align=True)

            #row.menu("VIEW3D_TP_SnapSet_Options_Menu", text="", icon= "SCRIPTWIN")     

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
            

        # USE MENUS #
        else:

            # NAMES / ICONS #  
            display_name = context.user_preferences.addons[__package__].preferences.tab_display_name
            if display_name == 'both_id':  
                                                    
                tx_snapset = " SnapSet"
  
            if display_name == 'icon_id':  
      
                tx_snapset = ""

           
            # OPTIONS #  
            row = layout.row(align=True)
            
            #row.menu("VIEW3D_TP_SnapSet_Options_Menu", text="", icon= "SCRIPTWIN")         
            
            button_snap_set = icons.get("icon_snap_set") 
            row.menu("VIEW3D_MT_SnapSet_Header_Menu", text= tx_snapset, icon_value=button_snap_set.icon_id) 


