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


# to hide an button in the header, place a rhombus in front of the line

# example 1 > with default operator > hide one line:

        #row.operator("object.transform_apply", text="", icon="FILE_TICK").location=True

# example 2 > operator with custom icons > hide two lines:

        #button_origin_center_view = icons.get("icon_origin_center_view")
        #row.operator("object.transform_apply", text="", icon_value=button_origin_center_view.icon_id).location=True



# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    

from . menus.menu_options import (VIEW3D_TP_Header_Options_Menu)
from . menus.menu_display import (VIEW3D_TP_Header_Display_Menu)
from . menus.menu_ruler   import (VIEW3D_TP_Header_Ruler_Menu)
from . menus.menu_shading import (VIEW3D_TP_Header_Shading_Menu)
from . menus.menu_station import (VIEW3D_TP_Header_Station_Menu)
from . menus.menu_custom  import (VIEW3D_TP_Header_Custom_Menu)

from . menus.menu_snapset import (VIEW3D_TP_Header_SnapSet_Menu)
from . menus.menu_snapto  import (VIEW3D_TP_Header_CursorTo_Menu)
from . menus.menu_snapto  import (VIEW3D_TP_Header_SelectTo_Menu)

from . origin.origin_menu  import (VIEW3D_TP_Origin_Menu)
from . origin.origin_menu  import (VIEW3D_TP_Origin_Advanced_Menu)


EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE"]


def draw_origin_button_menu_layout(self, context, layout):
          
        icons = load_icons()

        button_origin_center_view = icons.get("icon_origin_center_view")
        row.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

        button_origin_cursor = icons.get("icon_origin_cursor")
        row.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

        button_origin_edm = icons.get("icon_origin_edm")            
        row.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

        button_origin_obj = icons.get("icon_origin_obj")   
        row.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)            

        if context.mode == 'EDIT_MESH':

            button_origin_ccc = icons.get("icon_origin_ccc")            
            row.operator("tp_ops.origin_ccc","3P-Center", icon_value=button_origin_ccc.icon_id)       
             
            button_origin_bbox = icons.get("icon_origin_bbox")       
            row.operator("tp_ops.bbox_origin_set","BBox Origin", icon_value=button_origin_bbox.icon_id)



# UI: MAIN MENU # 
class VIEW3D_TP_Header_Menus(bpy.types.Header):
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
       return 
       
    def draw(self, context):
        layout = self.layout       
    
        #tp_props = context.window_manager.tp_props_header

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'    

        view = context.space_data        
        obj = context.active_object        
        if obj:
            obj_type = obj.type

            is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})        
            is_mesh = (obj_type in {'MESH'})   

        row = layout.row(1)


        # USE BUTTONS #
        display_buttons = context.user_preferences.addons[__package__].preferences.tab_display_gui
        if display_buttons == 'buttons': 


            # OPTIONS #  
            row.menu("VIEW3D_TP_Header_Options_Menu", text="", icon= "SCRIPTWIN")     

            row.separator()


            # RULER #  
            display_ruler = context.user_preferences.addons[__package__].preferences.tab_display_ruler
            if display_ruler == 'on':

                button_ruler_triangle = icons.get("icon_ruler_triangle") 
                row.operator("view3d.ruler", text='', icon_value = button_ruler_triangle.icon_id)     

                row.separator()


            # SNAP SET #   
            display_snap_set = context.user_preferences.addons[__package__].preferences.tab_display_snapset
            if display_snap_set == 'on': 

                row.separator()

                #button_snap_active = icons.get("icon_snap_active")
                #row.operator("tp_ops.active_snap", text="", icon_value=button_snap_active.icon_id) 

                button_snap_active = icons.get("icon_snap_active")
                row.operator("tp_ops.closest_snap", text="", icon_value=button_snap_active.icon_id)

                button_snap_cursor = icons.get("icon_snap_cursor")           
                row.operator("tp_ops.active_3d", text="", icon_value=button_snap_cursor.icon_id) 
         
                button_snap_grid = icons.get("icon_snap_grid")
                row.operator("tp_ops.grid", text="", icon_value=button_snap_grid.icon_id)
                            
                if context.mode == 'OBJECT':
                    button_snap_place = icons.get("icon_snap_place")
                    row.operator("tp_ops.place", text="", icon_value=button_snap_place.icon_id)

                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    row.operator("tp_ops.retopo", text="", icon_value=button_snap_retopo.icon_id)    
            
           
            # SNAP TO #   
            display_snap = context.user_preferences.addons[__package__].preferences.tab_display_snap
            if display_snap == 'on':  

                row.separator()

                button_cursor_center = icons.get("icon_cursor_center")            
                row.operator("view3d.snap_cursor_to_center", text="", icon_value = button_cursor_center.icon_id)

                button_cursor_active_obm = icons.get("icon_cursor_active_obm")           
                row.operator("view3d.snap_cursor_to_selected", text="", icon_value = button_cursor_active_obm.icon_id)

                if context.mode == 'OBJECT':
                   
                    button_snap_set = icons.get("icon_snap_set")            
                    row.operator("tp_ops.header_set_cursor", text="", icon_value = button_snap_set.icon_id)  
  
                button_select_cursor = icons.get("icon_select_cursor")    
                row.operator("view3d.snap_selected_to_cursor", text="", icon_value = button_select_cursor.icon_id).use_offset=False


            # ORIGIN TO #   
            display_origin = context.user_preferences.addons[__package__].preferences.tab_display_origin
            if display_origin == 'on':  
                
                row.separator()
                
                ob = context
                if ob.mode == 'OBJECT':

                    button_origin_center_view = icons.get("icon_origin_center_view")
                    row.operator("object.transform_apply", text="", icon_value=button_origin_center_view.icon_id).location=True

                    button_origin_cursor = icons.get("icon_origin_cursor")
                    row.operator("tp_ops.origin_set_cursor", text="", icon_value=button_origin_cursor.icon_id)

                    button_origin_tomesh = icons.get("icon_origin_tomesh")
                    row.operator("tp_ops.origin_tomesh", text="", icon_value=button_origin_tomesh.icon_id)

                    button_origin_meshto = icons.get("icon_origin_meshto")
                    row.operator("tp_ops.origin_meshto", text="", icon_value=button_origin_meshto.icon_id)

                    if len(bpy.context.selected_objects) == 1: 
                        
                        button_origin_tosnap = icons.get("icon_origin_tosnap")         
                        row.operator("tp_ops.origin_modal", text="", icon_value=button_origin_tosnap.icon_id)

                    button_origin_mass = icons.get("icon_origin_mass")           
                    row.operator("tp_ops.origin_set_mass", text="", icon_value=button_origin_mass.icon_id)

                    if len(bpy.context.selected_objects) == 1: 

                        button_origin_bbox = icons.get("icon_origin_bbox")                               
                        row.operator("object.bbox_origin_modal_ops", text="", icon_value=button_origin_bbox.icon_id)                                
                               
                    if len(bpy.context.selected_objects) > 1: 
                        obj = context.active_object
                        if obj:
                            obj_type = obj.type
                            
                            if obj.type in {'MESH'}:

                                button_origin_bbox = icons.get("icon_origin_bbox")   
                                row.operator("tp_ops.bbox_origin_set","", icon_value=button_origin_bbox.icon_id)
              

                if ob.mode == 'EDIT_MESH':

                    draw_origin_button_menu_layout(self, context, layout) 
                                

                if ob.mode == 'EDIT_CURVE':
                    
                    draw_origin_button_menu_layout(self, context, layout) 
             
                if ob.mode == 'EDIT_SURFACE':
                    
                    draw_origin_button_menu_layout(self, context, layout) 

                if ob.mode == 'EDIT_METABALL':
                    
                    draw_origin_button_menu_layout(self, context, layout) 
           
                if ob.mode == 'EDIT_LATTICE':
                    
                    draw_origin_button_menu_layout(self, context, layout)             
                         
                if  context.mode == 'PARTICLE':
               
                    draw_origin_button_menu_layout(self, context, layout) 

                if ob.mode == 'EDIT_ARMATURE':

                    draw_origin_button_menu_layout(self, context, layout)             

                if context.mode == 'POSE':

                    draw_origin_button_menu_layout(self, context, layout) 


            # ALIGN TO #   
            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_advanced
            if display_advanced == 'on':  
               
                row.separator()                
                
                ob = context
                if ob.mode in EDIT:   

                    button_origin_mesh = icons.get("icon_origin_mesh")                
                    row.operator("tp_ops.origin_transform", "", icon_value=button_origin_mesh.icon_id)               
                else:
                    button_origin_distribute = icons.get("icon_origin_distribute")  
                    row.operator("object.distribute_osc", "", icon_value=button_origin_distribute.icon_id)

                    button_origin_align = icons.get("icon_origin_align")                
                    row.operator("tp_origin.align_tools", "", icon_value=button_origin_align.icon_id)  

                button_align_zero = icons.get("icon_align_zero")                
                row.operator("tp_ops.zero_axis", "", icon_value=button_align_zero.icon_id)      


            row.separator()
            
            # NP POINT DISTANCE #       
            display_point_distance = context.user_preferences.addons[__package__].preferences.tab_display_point_distance
            if display_point_distance == 'on':  

                button_snap_ruler = icons.get("icon_snap_ruler") 
                row.operator("tp_ops.np_020_point_distance", text='', icon_value = button_snap_ruler.icon_id)

            if context.mode == 'OBJECT':

                display_point_move = context.user_preferences.addons[__package__].preferences.tab_display_point_move
                if display_point_move == 'on':  

                    button_snap_grab = icons.get("icon_snap_grab") 
                    row.operator("tp_ops.np_020_point_move", text='', icon_value=button_snap_grab.icon_id)                   
            
            
            if is_mesh and context.mode == 'OBJECT':


                display_roto_move = context.user_preferences.addons[__package__].preferences.tab_display_roto_move
                if display_roto_move == 'on':  

                    button_snap_rotate = icons.get("icon_snap_rotate") 
                    row.operator("tp_ops.np_020_roto_move", text='', icon_value=button_snap_rotate.icon_id)

                display_point_scale = context.user_preferences.addons[__package__].preferences.tab_display_point_scale
                if display_point_scale == 'on':   
 
                    button_snap_scale = icons.get("icon_snap_scale") 
                    row.operator("tp_ops.np_020_point_scale", text='', icon_value=button_snap_scale.icon_id)


                display_point_align = context.user_preferences.addons[__package__].preferences.tab_display_point_align
                if display_point_align == 'on':  

                    button_snap_abc = icons.get("icon_snap_abc") 
                    row.operator("tp_ops.np_020_point_align", text='', icon_value=button_snap_abc.icon_id) 


            # SNAPLINE #   
            display_snapline = context.user_preferences.addons[__package__].preferences.tab_display_snapline
            if display_snapline == 'on':  

                if is_mesh:

                    button_snap_line = icons.get("icon_snap_line") 
                    row.operator("tp_ops.snapline", text='', icon_value=button_snap_line.icon_id)    


            # DISPLAY #  
            display_objects = context.user_preferences.addons[__package__].preferences.tab_display_objects
            if display_objects == 'on':  
                
                row.separator()
                

                if obj:

                    row.operator("tp_ops.header_display_set", text="",  icon="META_CUBE")

                    button_draw_wire = icons.get("icon_draw_wire") 
                    row.operator("tp_ops.header_set_wire", text="", icon_value = button_draw_wire.icon_id)


            # SHADING #  
            display_shading = context.user_preferences.addons[__package__].preferences.tab_display_shading
            if display_shading == 'on':  

               row.separator()
                
               if context.mode == 'OBJECT':
                   row.operator("object.shade_smooth", text="", icon="SMOOTH")
                   row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
               else:
                   row.operator("mesh.faces_shade_smooth", text="", icon="SMOOTH")
                   row.operator("mesh.faces_shade_flat", text="", icon="MESH_CIRCLE") 

               if is_mesh:
                   row.prop(context.active_object.data, "use_auto_smooth", text="", icon="AUTO") 
                   row.prop(context.active_object.data, "show_double_sided", text="", icon="GHOST")




            # VIEW #
            display_view = context.user_preferences.addons[__package__].preferences.tab_display_view
            if display_view == 'on':                  
                    
                row = layout.row(1)
                row.operator_context = 'INVOKE_REGION_WIN'                
                
                row.prop(view, "use_matcap", text="", icon ="MATCAP_01")
                row.prop(context.space_data.fx_settings, "use_ssao", text="", icon="GROUP")
                row.prop(view, "show_only_render", text="", icon ="SCENE")
                row.prop(view, "show_world", text="", icon ="WORLD")
                row.prop(view, "show_floor", text="", icon ="GRID")


            # WINDOWS #
            display_window = context.user_preferences.addons[__package__].preferences.tab_display_window
            if display_window == 'on':  

                row = layout.row(1)
                row.operator_context = 'INVOKE_REGION_WIN'                
                  
                row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")                
                row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")

                if view.region_quadviews:
                    
                    region = view.region_quadviews[2]
                   
                    row = layout.row(align=True)
                    row.prop(region, "lock_rotation")
                   
                    row = layout.row(align=True)
                    row.enabled = region.lock_rotation               
                    row.prop(region, "show_sync_view")
                   
                    row = layout.row(align=True)
                    row.enabled = region.lock_rotation and region.show_sync_view
                    row.prop(region, "use_box_clip")         


            # HISTORY #               
            display_header_history = context.user_preferences.addons[__package__].preferences.tab_display_history
            if display_header_history == 'on': 

                row = layout.row(1)
                row.operator("ed.undo", text="", icon="FRAME_PREV")
                row.operator("ed.undo_history", text="", icon="COLLAPSEMENU")
                row.operator("ed.redo", text="", icon="FRAME_NEXT")


            # SAVE #           
            display_header_save = context.user_preferences.addons[__package__].preferences.tab_display_save
            if display_header_save == 'on': 

                row = layout.row(1)
                row.operator("wm.save_mainfile",text="",icon="FILE_TICK") 
                row.operator("wm.save_as_mainfile",text="",icon="SAVE_AS")     
            



        # USE RADIO BUTTONS #
        display_radio = context.user_preferences.addons[__package__].preferences.tab_display_gui
        if display_radio == 'radio': 


            view = context.space_data
            scene = context.scene        
            gs = scene.game_settings
            mode_string = context.mode
            edit_object = context.edit_object
            obj = context.active_object
            
            toolsettings = context.tool_settings

            row = layout.row(align=True)
            
            if not scene.render.use_shading_nodes:
                row.prop(gs, "material_mode", text="")

            if view.viewport_shade == 'SOLID':
                row.prop(view, "show_textured_solid", text="Texture")
                row.prop(view, "show_only_render", text="Render")
                row.prop(view, "show_floor", text="Grid")
                row.prop(view, "use_matcap")
              
                if view.use_matcap:
                    sub = row.row(align=True)
                    sub.scale_x = 0.25
                    sub.scale_y = 0.2
                    sub.template_icon_view(view, "matcap_icon")

            elif view.viewport_shade == 'TEXTURED':
                if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                    row.prop(view, "show_textured_shadeless")        

            
            row.prop(view, "show_backface_culling", text="Backface")
            if obj and obj.mode == 'EDIT' and view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
                row.prop(view, "show_occlude_wire", text="Hidden")


            row = layout.row(align=True)
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")

            if view.region_quadviews:
                region = view.region_quadviews[2]
                col = layout.column()
                col.prop(region, "lock_rotation")
                row = layout.row(align=True)
                row.enabled = region.lock_rotation
                row.prop(region, "show_sync_view")
                row = layout.row(align=True)
                row.enabled = region.lock_rotation and region.show_sync_view
                row.prop(region, "use_box_clip")





        # USE MENUS #
        display_menus = context.user_preferences.addons[__package__].preferences.tab_display_gui
        if display_menus == 'menus': 


            # NAMES / ICONS #  
            display_name = context.user_preferences.addons[__package__].preferences.tab_display_name
            if display_name == 'both_id':  

                # CUSTOM #                         
                ico_custom = "LAMP_DATA"                               
                tx_custom = " Custom"
                       
                # RULER #                         
                ico_ruler = "NOCURVE"                               
                tx_ruler = " Ruler"
                       
                # DISPLAY #
                ico_display = "SNAP_FACE"                             
                tx_display = " Display"

                # SHADING #
                ico_shading = "SMOOTH"                               
                tx_shading = " Shading"

                 # CURSOR TO #
                ico_cursorto = "CURSOR"                               
                tx_cursorto = " CursorTo"    
  
                # SELECT TO #
                ico_selectto = "RESTRICT_SELECT_OFF"                               
                tx_selectto = " SelectTo"  
                
                # ORIGIN TO #
                ico_originto = "VERTEXSEL"                               
                tx_originto = " OriginTo" 
                
                # ADVANCED #
                ico_advanced = "ALIGN"                               
                tx_advanced = " AlignTo" 

                # SNAPSET #
                ico_snapset = "FORCE_FORCE"                               
                tx_snapset = " SnapSet"                  
                  
                # STATION #
                ico_station = "SNAP_ON"                               
                tx_station = " Station"  
 
 
            elif display_name == 'icon_id':  

                # CUSTOM #                         
                ico_custom = "LAMP_DATA"                               
                tx_custom = ""

                # RULER #            
                ico_ruler = "NOCURVE"         
                tx_ruler = ""
            
                # DISPLAY #
                ico_display = "SNAP_FACE"                              
                tx_display = ""
              
                # SHADING #
                ico_shading = "SMOOTH"                               
                tx_shading = "" 

                 # CURSOR TO #
                ico_cursorto = "CURSOR"                               
                tx_cursorto = ""    
  
                # SELECT TO #
                ico_selectto = "RESTRICT_SELECT_OFF"                               
                tx_selectto = ""  

                # ORIGIN TO #
                ico_originto = "VERTEXSEL"                               
                tx_originto = "" 
                
                # ADVANCED #
                ico_advanced = "ALIGN"                               
                tx_advanced = "" 

                # SNAPSET #
                ico_snapset = "FORCE_FORCE"                               
                tx_snapset = ""                  
                  
                # STATION #
                ico_station = "SNAP_ON"                               
                tx_station = ""  

            elif display_name == 'text_id': 

                # CUSTOM #                    
                ico_custom = "NONE"
                tx_custom = "Custom"

                # RULER #                    
                ico_ruler = "NONE"
                tx_ruler = "Ruler"

                # DISPLAY #
                ico_display = "NONE"                               
                tx_display = "Display"
                
                # SHADING #
                ico_shading = "NONE"                               
                tx_shading = "Shading"                
                
                # CURSOR TO #
                ico_cursorto = "NONE"                               
                tx_cursorto = "CursorTo"    
  
                # SELECT TO #
                ico_selectto = "NONE"                               
                tx_selectto = "SelectTo"  
                
                # ORIGIN TO #
                ico_originto = "NONE"                               
                tx_originto = " OriginTo"  
               
                # ADVANCED #
                ico_advanced = "NONE"                               
                tx_advanced = " AlignTo" 
 
                # SNAPSET #
                ico_snapset = "NONE"                               
                tx_snapset = "SnapSet"                  
                  
                # STATION #
                ico_station = "NONE"                               
                tx_station = "Station"                  



            # OPTIONS #  
            row.menu("VIEW3D_TP_Header_Options_Menu", text="", icon= "SCRIPTWIN")         
            
            row.separator()
           
            # CUSTOM #  
            display_custom = context.user_preferences.addons[__package__].preferences.tab_display_custom
            if display_custom == 'on':

                row.menu("VIEW3D_TP_Header_Custom_Menu", text= tx_custom, icon= ico_custom)

                row.separator()       

  
            # RULER #  
            display_ruler = context.user_preferences.addons[__package__].preferences.tab_display_ruler
            if display_ruler == 'on':

                row.menu("VIEW3D_TP_Header_Ruler_Menu", text= tx_ruler, icon= ico_ruler)

                row.separator()          
                

            # SNAP TO #   
            display_snap = context.user_preferences.addons[__package__].preferences.tab_display_snap
            if display_snap == 'on':  

                row.menu("VIEW3D_TP_Header_CursorTo_Menu", text= tx_cursorto, icon= ico_cursorto)

                row.separator()
               
                row.menu("VIEW3D_TP_Header_SelectTo_Menu", text= tx_selectto, icon= ico_selectto)
               
                row.separator()
          
    

             # SNAPSET #   
            display_snapset = context.user_preferences.addons[__package__].preferences.tab_display_snapset
            if display_snapset == 'on': 
              
                row.menu("VIEW3D_TP_Header_SnapSet_Menu", text= tx_snapset, icon= ico_snapset)

                row.separator()     

            
            # ORIGIN TO #   
            display_origin = context.user_preferences.addons[__package__].preferences.tab_display_origin
            if display_origin == 'on':  
                
                row.menu("VIEW3D_TP_Origin_Menu", text= tx_originto, icon= ico_originto)

                row.separator()

           
            # ALIGN TO #   
            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_advanced
            if display_advanced == 'on':  
                
                row.menu("VIEW3D_TP_Origin_Advanced_Menu", text= tx_advanced, icon= ico_advanced)

                row.separator()


            # NP STATION # 
            display_station = context.user_preferences.addons[__package__].preferences.tab_display_station
            if display_station == 'on':  
     
                row.menu("VIEW3D_TP_Header_Station_Menu", text= tx_station, icon= ico_station)

                row.separator()


            # DISPLAY #  
            display_objects = context.user_preferences.addons[__package__].preferences.tab_display_objects
            if display_objects == 'on':  
        
                if obj:
                    row.menu("VIEW3D_TP_Header_Display_Menu", text= tx_display, icon= ico_display)

                    row.separator()


            # SHADING #  
            display_shading = context.user_preferences.addons[__package__].preferences.tab_display_shading
            if display_shading == 'on':  
                
                row.menu("VIEW3D_TP_Header_Shading_Menu", text= tx_shading, icon= ico_shading)

                row.separator()
