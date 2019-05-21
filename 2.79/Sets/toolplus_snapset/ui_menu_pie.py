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


class VIEW3D_MT_SnapSet_Menu_Pencil(bpy.types.Menu):
    bl_label = "Annotate"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Pencil"

    def draw(self, context):
        layout = self.layout
      
        icons = load_icons()  
        

        layout.operator("gpencil.draw", icon='GREASEPENCIL', text="Draw").mode = 'DRAW'
        layout.operator("gpencil.draw", icon='LINE_DATA', text="Line").mode = 'DRAW_STRAIGHT'
        layout.operator("gpencil.draw", icon='MESH_DATA', text="Poly").mode = 'DRAW_POLY'
        layout.operator("gpencil.draw", icon='FORCE_CURVE', text="Erase").mode = 'ERASER' 


        layout.separator()
        
        layout.operator("gpencil.layer_add", text="Add Layer", icon="ZOOMIN")
        layout.operator("gpencil.layer_remove", text="Remove Layer", icon="ZOOMOUT")

        layout.separator()

        layout.operator("gpencil.data_unlink", text="Data Unlink", icon="UNLINKED")





# UI: HOTKEY MENU PIE # 
class VIEW3D_MT_SnapSet_Menu_Pie(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Pie"

    def draw(self, context):
        layout = self.layout
       
        menu_prefs = context.user_preferences.addons[__package__].preferences

        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()      

        #Box 1 L
        row = pie.split().column()
        row.scale_x = 1.1       

        if menu_prefs.use_internal_icon_btd == True:
            row.operator("tpc_ot.snapset_button_d", text=menu_prefs.name_btd, icon=menu_prefs.icon_btd) 
        else:
            button_snap_active = icons.get("icon_snap_active")            
            row.operator("tpc_ot.snapset_button_d", text=menu_prefs.name_btd, icon_value=button_snap_active.icon_id) 

        
        #Box 2 R
        row = pie.split().column()
        row.scale_x = 1.1
        if menu_prefs.use_internal_icon_bte == True:
            row.operator("tpc_ot.snapset_button_e", text=menu_prefs.name_bte, icon=menu_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            row.operator("tpc_ot.snapset_button_e", text=menu_prefs.name_bte, icon_value=button_snap_closest.icon_id)
            
       
        #Box 3 B
        row = pie.split().column()
        row.scale_x = 1.1
        if menu_prefs.use_internal_icon_btc == True:     
            row.operator("tpc_ot.snapset_button_c", text=menu_prefs.name_btc, icon=menu_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tpc_ot.snapset_button_c", text=menu_prefs.name_btc, icon_value=button_snap_cursor.icon_id) 

     
        #Box 4 T 
        box = pie.split().column(align = False)
        box.scale_x = 0.65
        
        row = box.row(align = False)
             
        if menu_prefs.use_show_manipulator == True:  
            row.operator("wm.context_toggle", text=" ", icon='MANIPUL').data_path = "space_data.show_manipulator" 

        if menu_prefs.use_manipulator_all == True:  
            row.operator("tpc_ot.manipulator_all", " ", icon = 'NDOF_DOM')

        row.operator("tpc_ot.manipulator_move", text=" ", icon="MAN_TRANS")
                      
        row.operator("tpc_ot.manipulator_rotation", text=" ", icon="MAN_ROT")

        row.operator("tpc_ot.manipulator_scale", text=" ", icon="MAN_SCALE")
             
        if menu_prefs.use_ruler_button == True:   
            row.operator("view3d.ruler", text=" ", icon="NOCURVE")   
      
        if menu_prefs.use_pencil_menu == True:   
            row.menu("VIEW3D_MT_SnapSet_Menu_Pencil", text=" ", icon="GREASEPENCIL") 
 
        row = box.row(align = False)      

        if bpy.context.space_data.pivot_point == 'BOUNDING_BOX_CENTER':   
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATE", emboss = menu_prefs.tpc_use_emposs).tpc_pivot="BOUNDING_BOX_CENTER"
        else:
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATE").tpc_pivot="BOUNDING_BOX_CENTER"
            
        if bpy.context.space_data.pivot_point == 'CURSOR':                   
            row.operator("tpc_ot.set_pivot", text=" ", icon="CURSOR", emboss = menu_prefs.tpc_use_emposs).tpc_pivot="CURSOR"
        else:
            row.operator("tpc_ot.set_pivot", text=" ", icon="CURSOR").tpc_pivot="CURSOR"
        
        if bpy.context.space_data.pivot_point == 'ACTIVE_ELEMENT':              
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTACTIVE", emboss = menu_prefs.tpc_use_emposs).tpc_pivot="ACTIVE_ELEMENT"
        else:                
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTACTIVE").tpc_pivot="ACTIVE_ELEMENT"

        if bpy.context.space_data.pivot_point == 'INDIVIDUAL_ORIGINS':               
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATECOLLECTION", emboss = menu_prefs.tpc_use_emposs).tpc_pivot="INDIVIDUAL_ORIGINS"
        else:
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATECOLLECTION").tpc_pivot="INDIVIDUAL_ORIGINS"

        if bpy.context.space_data.pivot_point == 'MEDIAN_POINT':       
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATECENTER", emboss = menu_prefs.tpc_use_emposs).tpc_pivot="MEDIAN_POINT" 
        else:                
            row.operator("tpc_ot.set_pivot", text=" ", icon="ROTATECENTER").tpc_pivot="MEDIAN_POINT" 


        #Box 5 LT
        box = pie.split().column(align = False)
        box.scale_x = 0.65

        row = box.row(align = False)

        if bpy.context.scene.tool_settings.snap_element == 'VERTEX':            
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VERTEX", emboss = menu_prefs.tpc_use_emposs).tpc_snape="VERTEX"       
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VERTEX").tpc_snape="VERTEX"        

        if bpy.context.scene.tool_settings.snap_element == 'EDGE':
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_EDGE", emboss = menu_prefs.tpc_use_emposs).tpc_snape="EDGE"        
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_EDGE").tpc_snape="EDGE"        

        if bpy.context.scene.tool_settings.snap_element == 'FACE':
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_FACE", emboss = menu_prefs.tpc_use_emposs).tpc_snape="FACE"
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_FACE").tpc_snape="FACE" 
          
     
        row = box.row(align = False)
      
        if bpy.context.scene.tool_settings.snap_element == 'VOLUME':
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VOLUME", emboss = menu_prefs.tpc_use_emposs).tpc_snape="VOLUME" 
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VOLUME").tpc_snape="VOLUME"  

        if bpy.context.scene.tool_settings.snap_element == 'INCREMENT':                                    
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_INCREMENT", emboss = menu_prefs.tpc_use_emposs).tpc_snape="INCREMENT"        
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_INCREMENT").tpc_snape="INCREMENT"        
        
        if bpy.context.scene.tool_settings.use_snap == True:                                    
            row.operator("tpc_ot.snap_use", text=" ", icon = "SNAP_ON", emboss = menu_prefs.tpc_use_emposs).mode="unuse_snap"        
        else:
            row.operator("tpc_ot.snap_use", text=" ", icon = "SNAP_OFF").mode="use_snap"     


        #Box 6 RT 
        box = pie.split().column(align = False)
        box.scale_x = 0.75         

        row = box.row(align = False)
        
        if bpy.context.space_data.transform_orientation == 'GLOBAL':         
            row.operator("tpc_ot.orient_axis", text="GLO", emboss = menu_prefs.tpc_use_emposs).tpc_axis="GLOBAL"        
        else:        
            row.operator("tpc_ot.orient_axis", text="GLO").tpc_axis="GLOBAL"        

        if bpy.context.space_data.transform_orientation == 'LOCAL':   
            row.operator("tpc_ot.orient_axis", text="LOC", emboss = menu_prefs.tpc_use_emposs).tpc_axis="LOCAL"
        else:
            row.operator("tpc_ot.orient_axis", text="LOC").tpc_axis="LOCAL"

        if bpy.context.space_data.transform_orientation == 'NORMAL':   
            row.operator("tpc_ot.orient_axis", text="NOR", emboss = menu_prefs.tpc_use_emposs).tpc_axis="NORMAL"
        else:    
            row.operator("tpc_ot.orient_axis", text="NOR").tpc_axis="NORMAL"

      
        row = box.row(align = False)

        if bpy.context.space_data.transform_orientation == 'GIMBAL':   
            row.operator("tpc_ot.orient_axis", text="GIM", emboss = menu_prefs.tpc_use_emposs).tpc_axis="GIMBAL"
        else:    
            row.operator("tpc_ot.orient_axis", text="GIM").tpc_axis="GIMBAL"                 

        if bpy.context.space_data.transform_orientation == 'VIEW':   
            row.operator("tpc_ot.orient_axis", text="VIW", emboss = menu_prefs.tpc_use_emposs).tpc_axis="VIEW"
        else:    
            row.operator("tpc_ot.orient_axis", text="VIW").tpc_axis="VIEW"    

        if bpy.context.space_data.transform_orientation == 'CURSOR':   
            row.operator("tpc_ot.orient_axis", text="CUR", emboss = menu_prefs.tpc_use_emposs).tpc_axis="CURSOR"
        else:    
            row.operator("tpc_ot.orient_axis", text="CUR").tpc_axis="CURSOR"    


        #Box 7 LB 
        row = pie.split().column()
        row.scale_x = 1.1                    
        if context.mode == 'OBJECT':
            if menu_prefs.tpc_use_place_modal == True:
                button_snap_place = icons.get("icon_snap_place")
                row.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "place"

            if menu_prefs.tpc_use_place == True:
                if menu_prefs.use_internal_icon_btb == True:   
                    row.operator("tpc_ot.snapset_button_b", text=menu_prefs.name_btb, icon=menu_prefs.icon_btb)
                else:
                    button_snap_place = icons.get("icon_snap_place")
                    row.operator("tpc_ot.snapset_button_b", text=menu_prefs.name_btb, icon_value=button_snap_place.icon_id)

        else:
            if menu_prefs.tpc_use_retopo_modal == True:              
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "retopo"   

            if menu_prefs.tpc_use_retopo == True:
                if menu_prefs.use_internal_icon_btf == True:   
                    row.operator("tpc_ot.snapset_button_f", text=menu_prefs.name_btf, icon=menu_prefs.icon_btf)    
                else:
                    button_snap_retopo = icons.get("icon_snap_retopo")
                    row.operator("tpc_ot.snapset_button_f", text=menu_prefs.name_btf, icon_value=button_snap_retopo.icon_id)    
           
          

        #Box 8 RB
        row = pie.split().column()
        row.scale_x = 1.1
        if menu_prefs.tpc_use_grid_modal == True:
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "grid"

        if menu_prefs.tpc_use_grid == True:
            if menu_prefs.use_internal_icon_bta == True:  
                row.operator("tpc_ot.snapset_button_a", text=menu_prefs.name_bta, icon=menu_prefs.icon_bta)
            else:
                button_snap_grid = icons.get("icon_snap_grid")
                row.operator("tpc_ot.snapset_button_a", text=menu_prefs.name_bta, icon_value=button_snap_grid.icon_id)



