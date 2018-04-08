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

 
# UI: HOTKEY MENU # 
class VIEW3D_TP_SnapSet_Menu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "tp_menu.menu_snapset"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        layout.operator_context = 'INVOKE_REGION_WIN' 

        layout.scale_y = 1.5

        # MODAL TEXT DRAW #  
        display_modal_text = context.user_preferences.addons[__package__].preferences.tab_display_modal

        if display_modal_text == 'on':  

            button_snap_active = icons.get("icon_snap_active")
            layout.operator("tp_ops.active_snap_modal", text="Active", icon_value=button_snap_active.icon_id) 

            button_snap_closest = icons.get("icon_snap_closest")
            layout.operator("tp_ops.closest_snap_modal", text="Closest", icon_value=button_snap_closest.icon_id)

            button_snap_cursor = icons.get("icon_snap_cursor")           
            layout.operator("tp_ops.active_3d_modal", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 
     
            button_snap_grid = icons.get("icon_snap_grid")
            layout.operator("tp_ops.grid_modal", text="GridSnap", icon_value=button_snap_grid.icon_id)
                        
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                layout.operator("tp_ops.place_modal", text="Place", icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                layout.operator("tp_ops.retopo_modal", text="Retopo", icon_value=button_snap_retopo.icon_id)    
     
        else:

            button_snap_active = icons.get("icon_snap_active")
            layout.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 

            button_snap_closest = icons.get("icon_snap_closest")
            layout.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_closest.icon_id)

            button_snap_cursor = icons.get("icon_snap_cursor")           
            layout.operator("tp_ops.active_3d", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 
     
            button_snap_grid = icons.get("icon_snap_grid")
            layout.operator("tp_ops.grid", text="GridSnap", icon_value=button_snap_grid.icon_id)
                        
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                layout.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    
     




# UI: HOTKEY MENU # 
class VIEW3D_TP_SnapSet_Menu_Pie(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "tp_menu.pie_snapset"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()      

        # MODAL TEXT DRAW #  
        display_modal_text = context.user_preferences.addons[__package__].preferences.tab_display_modal

        if display_modal_text == 'on':  

            # 1 L
            row = pie.split().column()

            button_snap_active = icons.get("icon_snap_active")
            row.operator("tp_ops.active_snap_modal", text="Active", icon_value=button_snap_active.icon_id) 

            # 2 R
            row = pie.split().column()

            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tp_ops.closest_snap_modal", text="Closest", icon_value=button_snap_closest.icon_id)
            
            # 3 B
            row = pie.split().column()

            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tp_ops.active_3d_modal", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 

            # 4 T 
            row = pie.split().column()
            row.label("")

            # 5 LT
            row = pie.split().column()
            row.label("")

            # 6 RT 
            row = pie.split().column()        
            row.label("")

            # 7 LB 
            row = pie.split().column()
                        
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tp_ops.place_modal", text="Place", icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tp_ops.retopo_modal", text="Retopo", icon_value=button_snap_retopo.icon_id)    

            # 8 RB
            row = pie.split().column()

            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tp_ops.grid_modal", text="GridSnap", icon_value=button_snap_grid.icon_id)

        else:

            # 1 L
            row = pie.split().column()

            button_snap_active = icons.get("icon_snap_active")
            row.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 

            # 2 R
            row = pie.split().column()

            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_closest.icon_id)
            
            # 3 B
            row = pie.split().column()

            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tp_ops.active_3d", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 

            # 4 T 
            row = pie.split().column()
            row.label("")

            # 5 LT
            row = pie.split().column()
            row.label("")

            # 6 RT 
            row = pie.split().column()        
            row.label("")

            # 7 LB 
            row = pie.split().column()
                        
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    

            # 8 RB
            row = pie.split().column()

            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tp_ops.grid", text="GridSnap", icon_value=button_snap_grid.icon_id)





# UI: SUB MENU SPECIAL # 
def draw_snapset_item_special(self, context):
    layout = self.layout

    icons = load_icons()

    button_snap_set = icons.get("icon_snap_set")
    layout.menu("tp_menu.menu_snapset", text="SnapSet", icon_value=button_snap_set.icon_id)      
    

    
# UI: MENU FOR HEADER # 
class VIEW3D_TP_SnapSet_Menu_Panel(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_TP_SnapSet_Menu_Panel"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
     
        layout.operator_context = 'INVOKE_REGION_WIN'
      
        layout.scale_y = 1.5

        button_snap_active = icons.get("icon_snap_active")
        layout.operator("tp_ops.active_snap", text="Active", icon_value=button_snap_active.icon_id) 

        button_snap_closest = icons.get("icon_snap_closest")
        layout.operator("tp_ops.closest_snap", text="Closest", icon_value=button_snap_closest.icon_id)

        button_snap_cursor = icons.get("icon_snap_cursor")           
        layout.operator("tp_ops.active_3d", text="3D Cursor", icon_value=button_snap_cursor.icon_id) 
 
        button_snap_grid = icons.get("icon_snap_grid")
        layout.operator("tp_ops.grid", text="GridSnap", icon_value=button_snap_grid.icon_id)
                    
        if context.mode == 'OBJECT':
            button_snap_place = icons.get("icon_snap_place")
            layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

        else:
            button_snap_retopo = icons.get("icon_snap_retopo")
            layout.operator("tp_ops.retopo", text="Retopo", icon_value=button_snap_retopo.icon_id)    



# UI: MENU FOR HEADER (HIDDEN) # 
class VIEW3D_TP_SnapSet_Options_Menu(bpy.types.Menu):
    bl_label = "SnapSet Options"
    bl_idname = "VIEW3D_TP_SnapSet_Options_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        expand = panel_prefs.expand_panel_tools       
       
        layout.operator_context = 'INVOKE_REGION_WIN'    

        layout.scale_y = 1.5      

        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')   

        layout.separator() 

        layout.prop(panel_prefs, 'tab_display_name', text="")
        
        layout.separator()  
    
        layout.prop(panel_prefs, 'tab_display_buttons', text="")



# UI: HEADER MENU # 
class VIEW3D_TP_SnapSet_Header_Menu(bpy.types.Header):
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
                tx_snapset_closet = "Closet"
                tx_snapset_cursor = "Cursor"
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
            row.operator("tp_ops.active_snap", text= tx_snapset_active, icon_value=button_snap_active.icon_id) 

            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tp_ops.closest_snap", text= tx_snapset_closet, icon_value=button_snap_closest.icon_id)

            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tp_ops.active_3d", text= tx_snapset_cursor, icon_value=button_snap_cursor.icon_id) 
     
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tp_ops.grid", text= tx_snapset_grid, icon_value=button_snap_grid.icon_id)
                        
            if context.mode == 'OBJECT':
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tp_ops.place", text= tx_snapset_place, icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tp_ops.retopo", text= tx_snapset_retopo, icon_value=button_snap_retopo.icon_id)    
            

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
            row.menu("VIEW3D_TP_SnapSet_Menu_Panel", text= tx_snapset, icon_value=button_snap_set.icon_id) 



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()