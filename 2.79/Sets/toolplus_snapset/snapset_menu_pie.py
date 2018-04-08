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



# UI: HOTKEY MENU PIE # 
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
            row.operator("tp_ops.active_3d_modal", text="Cursor3D", icon_value=button_snap_cursor.icon_id) 

            # 4 T 
            row = pie.split().row(1)
            row.scale_x = 0.75
            row.operator("tp_ops.set_pivot", " ", icon="ROTATE").tp_pivot="BOUNDING_BOX_CENTER"
            row.operator("tp_ops.set_pivot", " ", icon="CURSOR").tp_pivot="CURSOR"
            row.operator("tp_ops.set_pivot", " ", icon="ROTACTIVE").tp_pivot="ACTIVE_ELEMENT"
            row.operator("tp_ops.set_pivot", " ", icon="ROTATECOLLECTION").tp_pivot="INDIVIDUAL_ORIGINS"
            row.operator("tp_ops.set_pivot", " ", icon="ROTATECENTER").tp_pivot="MEDIAN_POINT"  


            display_transform = context.user_preferences.addons[__package__].preferences.tab_display_transform
            if display_transform == 'on':  


                # 5 LT
                box = pie.split().column(1)
                box.scale_x = 0.65
               
                row = box.row(1)
                
                if bpy.context.scene.tool_settings.snap_element == 'INCREMENT':                                    
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_INCREMENT", emboss = False).tp_snape="INCREMENT"        
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_INCREMENT").tp_snape="INCREMENT"        

                if bpy.context.scene.tool_settings.snap_element == 'VERTEX':            
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VERTEX", emboss = False).tp_snape="VERTEX"       
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VERTEX").tp_snape="VERTEX"        

                if bpy.context.scene.tool_settings.snap_element == 'EDGE':
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_EDGE", emboss = False).tp_snape="EDGE"        
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_EDGE").tp_snape="EDGE"        

                if bpy.context.scene.tool_settings.snap_element == 'FACE':
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_FACE", emboss = False).tp_snape="FACE"
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_FACE").tp_snape="FACE"

                if bpy.context.scene.tool_settings.snap_element == 'VOLUME':
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VOLUME", emboss = False).tp_snape="VOLUME" 
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VOLUME").tp_snape="VOLUME"             

                row = box.row(1)

                if bpy.context.scene.tool_settings.snap_target == 'CLOSEST':         
                    row.operator("tp_ops.snap_target", "CLO", emboss = False).tp_snapt="CLOSEST"        
                else:        
                    row.operator("tp_ops.snap_target", "CLO").tp_snapt="CLOSEST"        

                if bpy.context.scene.tool_settings.snap_target == 'CENTER':
                    row.operator("tp_ops.snap_target", "CEN", emboss = False).tp_snapt="CENTER"
                else:
                    row.operator("tp_ops.snap_target", "CEN").tp_snapt="CENTER"

                if bpy.context.scene.tool_settings.snap_target == 'MEDIAN':
                    row.operator("tp_ops.snap_target", "MED", emboss = False).tp_snapt="MEDIAN"
                else:    
                    row.operator("tp_ops.snap_target", "MED").tp_snapt="MEDIAN"

                if bpy.context.scene.tool_settings.snap_target == 'ACTIVE':
                    row.operator("tp_ops.snap_target", "ACT", emboss = False).tp_snapt="ACTIVE"
                else:    
                    row.operator("tp_ops.snap_target", "ACT").tp_snapt="ACTIVE"
                              
                row.prop(context.tool_settings, "use_snap", text=" ")  



                # 6 RT 
                box = pie.split().column(1)
                box.scale_x = 0.65        

                row = box.row(1)
                                                          
                row.operator("wm.context_toggle", text=" ", icon='MANIPUL').data_path = "space_data.show_manipulator" 
                row.operator("view3d.manipulator_all", " ", icon = 'NDOF_DOM')
                row.operator("view3d.manipulator_move", " ", icon = 'MAN_TRANS')                    
                row.operator("view3d.manipulator_rota", " ", icon = 'MAN_ROT')                    
                row.operator("view3d.manipulator_scale", " ", icon = 'MAN_SCALE')              

                row = box.row(1)
                
                if bpy.context.space_data.transform_orientation == 'GLOBAL':         
                    row.operator("tp_ops.orient_axis", "GLO", emboss = False).tp_axis="GLOBAL"        
                else:        
                    row.operator("tp_ops.orient_axis", "GLO").tp_axis="GLOBAL"        

                if bpy.context.space_data.transform_orientation == 'LOCAL':   
                    row.operator("tp_ops.orient_axis", "LOC", emboss = False).tp_axis="LOCAL"
                else:
                    row.operator("tp_ops.orient_axis", "LOC").tp_axis="LOCAL"

                if bpy.context.space_data.transform_orientation == 'NORMAL':   
                    row.operator("tp_ops.orient_axis", "NRM", emboss = False).tp_axis="NORMAL"
                else:    
                    row.operator("tp_ops.orient_axis", "NRM").tp_axis="NORMAL"

                if bpy.context.space_data.transform_orientation == 'GIMBAL':   
                    row.operator("tp_ops.orient_axis", "GIM", emboss = False).tp_axis="GIMBAL"
                else:    
                    row.operator("tp_ops.orient_axis", "GIM").tp_axis="GIMBAL"                 

                if bpy.context.space_data.transform_orientation == 'VIEW':   
                    row.operator("tp_ops.orient_axis", "VIW", emboss = False).tp_axis="VIEW"
                else:    
                    row.operator("tp_ops.orient_axis", "VIW").tp_axis="VIEW"    

            
            else:
                
                # 5 TL
                row = pie.split().column()
                row.label("")                

                # 6TR 
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
            row.operator("tp_ops.grid_modal", text="Grid", icon_value=button_snap_grid.icon_id)

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
            row.operator("tp_ops.active_3d", text="Cursor3D", icon_value=button_snap_cursor.icon_id) 

            # 4 T 
            row = pie.split().row(1)
            row.scale_x = 0.75
            row.operator("tp_ops.set_pivot", " ", icon="ROTATE").tp_pivot="BOUNDING_BOX_CENTER"
            row.operator("tp_ops.set_pivot", " ", icon="CURSOR").tp_pivot="CURSOR"
            row.operator("tp_ops.set_pivot", " ", icon="ROTACTIVE").tp_pivot="ACTIVE_ELEMENT"
            row.operator("tp_ops.set_pivot", " ", icon="ROTATECOLLECTION").tp_pivot="INDIVIDUAL_ORIGINS"
            row.operator("tp_ops.set_pivot", " ", icon="ROTATECENTER").tp_pivot="MEDIAN_POINT"  


            display_transform = context.user_preferences.addons[__package__].preferences.tab_display_transform
            if display_transform == 'on':  


                # 5 LT
                box = pie.split().column(1)
                box.scale_x = 0.65
               
                row = box.row(1)
                
                if bpy.context.scene.tool_settings.snap_element == 'INCREMENT':                                    
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_INCREMENT", emboss = False).tp_snape="INCREMENT"        
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_INCREMENT").tp_snape="INCREMENT"        

                if bpy.context.scene.tool_settings.snap_element == 'VERTEX':            
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VERTEX", emboss = False).tp_snape="VERTEX"       
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VERTEX").tp_snape="VERTEX"        

                if bpy.context.scene.tool_settings.snap_element == 'EDGE':
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_EDGE", emboss = False).tp_snape="EDGE"        
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_EDGE").tp_snape="EDGE"        

                if bpy.context.scene.tool_settings.snap_element == 'FACE':
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_FACE", emboss = False).tp_snape="FACE"
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_FACE").tp_snape="FACE"

                if bpy.context.scene.tool_settings.snap_element == 'VOLUME':
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VOLUME", emboss = False).tp_snape="VOLUME" 
                else:
                    row.operator("tp_ops.snap_element", " ", icon = "SNAP_VOLUME").tp_snape="VOLUME"             

                row = box.row(1)

                if bpy.context.scene.tool_settings.snap_target == 'CLOSEST':         
                    row.operator("tp_ops.snap_target", "CLO", emboss = False).tp_snapt="CLOSEST"        
                else:        
                    row.operator("tp_ops.snap_target", "CLO").tp_snapt="CLOSEST"        

                if bpy.context.scene.tool_settings.snap_target == 'CENTER':
                    row.operator("tp_ops.snap_target", "CEN", emboss = False).tp_snapt="CENTER"
                else:
                    row.operator("tp_ops.snap_target", "CEN").tp_snapt="CENTER"

                if bpy.context.scene.tool_settings.snap_target == 'MEDIAN':
                    row.operator("tp_ops.snap_target", "MED", emboss = False).tp_snapt="MEDIAN"
                else:    
                    row.operator("tp_ops.snap_target", "MED").tp_snapt="MEDIAN"

                if bpy.context.scene.tool_settings.snap_target == 'ACTIVE':
                    row.operator("tp_ops.snap_target", "ACT", emboss = False).tp_snapt="ACTIVE"
                else:    
                    row.operator("tp_ops.snap_target", "ACT").tp_snapt="ACTIVE"
                    
                row.prop(context.scene.tool_settings, "use_snap", text=" ") 


                # 6 RT 
                box = pie.split().column(1)
                box.scale_x = 0.65         

                row = box.row(1)
                                                          
                row.operator("wm.context_toggle", text=" ", icon='MANIPUL').data_path = "space_data.show_manipulator" 
                row.operator("view3d.manipulator_all", " ", icon = 'NDOF_DOM')
                row.operator("view3d.manipulator_move", " ", icon = 'MAN_TRANS')                    
                row.operator("view3d.manipulator_rota", " ", icon = 'MAN_ROT')                    
                row.operator("view3d.manipulator_scale", " ", icon = 'MAN_SCALE')              

                row = box.row(1)
                
                if bpy.context.space_data.transform_orientation == 'GLOBAL':         
                    row.operator("tp_ops.orient_axis", "GLO", emboss = False).tp_axis="GLOBAL"        
                else:        
                    row.operator("tp_ops.orient_axis", "GLO").tp_axis="GLOBAL"        

                if bpy.context.space_data.transform_orientation == 'LOCAL':   
                    row.operator("tp_ops.orient_axis", "LOC", emboss = False).tp_axis="LOCAL"
                else:
                    row.operator("tp_ops.orient_axis", "LOC").tp_axis="LOCAL"

                if bpy.context.space_data.transform_orientation == 'NORMAL':   
                    row.operator("tp_ops.orient_axis", "NRM", emboss = False).tp_axis="NORMAL"
                else:    
                    row.operator("tp_ops.orient_axis", "NRM").tp_axis="NORMAL"

                if bpy.context.space_data.transform_orientation == 'GIMBAL':   
                    row.operator("tp_ops.orient_axis", "GIM", emboss = False).tp_axis="GIMBAL"
                else:    
                    row.operator("tp_ops.orient_axis", "GIM").tp_axis="GIMBAL"                 

                if bpy.context.space_data.transform_orientation == 'VIEW':   
                    row.operator("tp_ops.orient_axis", "VIW", emboss = False).tp_axis="VIEW"
                else:    
                    row.operator("tp_ops.orient_axis", "VIW").tp_axis="VIEW"    

            
            else:
                
                # 5 TL
                row = pie.split().column()      
                row.label("")                

                # 6TR 
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
            row.operator("tp_ops.grid", text="Grid", icon_value=button_snap_grid.icon_id)


