# ##### BEGIN GPL LICENSE BLOCK #####
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


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons

import addon_utils


# LOAD MENUS #
from toolplus_align.menus.menu_pivot        import  (VIEW3D_TP_Pivot_Menu)
from toolplus_align.menus.menu_snapset      import  (VIEW3D_TP_SnapSet_Menu)
from toolplus_align.menus.menu_origin       import  (VIEW3D_TP_Origin_Menu_Align)
from toolplus_align.menus.menu_transform    import  (VIEW3D_TP_Location_Menu, VIEW3D_TP_Rotation_Menu, VIEW3D_TP_Scale_Menu)
from toolplus_align.menus.menu_axis         import  (VIEW3D_TP_Axis_Menu)
from toolplus_align.menus.menu_snaptools    import  (VIEW3D_TP_SnapTools_Menu)
from toolplus_align.menus.menu_station      import  (VIEW3D_TP_Station_Menu)
from toolplus_align.menus.menu_gstretch     import  (VIEW3D_TP_Align_Menu_Gstretch)
from toolplus_align.menus.menu_edit         import  (VIEW3D_TP_Align_Menu_Space, VIEW3D_TP_Align_Menu_LoopTools, VIEW3D_TP_Align_Menu_Relax)
from toolplus_align.menus.menu_mirror       import  (VIEW3D_TP_Mirror_Menu, VIEW3D_TP_ModMirror_Menu)



class VIEW3D_TP_Align_Menu(bpy.types.Menu):
    bl_label = "Align"
    bl_idname = "tp_menu.align_main"   
       
    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        layout.scale_y = 1.2

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        
        layout.operator_context = 'INVOKE_REGION_WIN'        

        # PIVOT #
        Display_Pivot = context.user_preferences.addons[addon_key].preferences.tab_pivot_menu
        if Display_Pivot == True:  
 
            layout.menu("VIEW3D_TP_Pivot_Menu", text="Pivot", icon="CURSOR")  


        button_snap_set = icons.get("icon_snap_set")           
        layout.menu("VIEW3D_TP_SnapSet_Menu", text="SnapSet", icon_value=button_snap_set.icon_id)  
          

        # ORIGIN #
        Display_Origin = context.user_preferences.addons[addon_key].preferences.tab_origin_menu
        if Display_Origin == True: 

            layout.separator()   

            layout.menu("VIEW3D_TP_Origin_Menu_Align", text="Origin", icon="LAYER_ACTIVE")   


        # ALIGN TO #
        Display_Align_to = context.user_preferences.addons[addon_key].preferences.tab_align_to_menu
        if Display_Align_to == True:  

            layout.separator()

            if context.mode == 'OBJECT':
             
                layout.menu("VIEW3D_TP_Location_Menu", text="Move", icon ="MAN_TRANS")   
                layout.menu("VIEW3D_TP_Rotation_Menu", text="Rotate", icon ="MAN_ROT")  
                layout.menu("VIEW3D_TP_Scale_Menu", text="Scale", icon ="MAN_SCALE")  

            else:
     
                layout.menu("VIEW3D_TP_Axis_Menu", text="To Axis", icon ="MANIPUL")   
           


        # TOOLS #
        Display_Aligner = context.user_preferences.addons[addon_key].preferences.tab_aligner_menu
        if Display_Aligner == True: 

            layout.separator()

            button_origin_align = icons.get("icon_origin_align") 
            layout.menu("VIEW3D_TP_SnapTools_Menu", text="Tools", icon_value=button_origin_align.icon_id)      



        if context.mode == 'OBJECT':

           
             # NP STATION #
            Display_Station = context.user_preferences.addons[addon_key].preferences.tab_station_menu
            if Display_Station == True:           
           
                button_snap_grab = icons.get("icon_snap_grab") 
                layout.menu("VIEW3D_TP_Station_Menu", text="Station", icon_value=button_snap_grab.icon_id)  
           
           
            # INTERPOLATE #
            Display_Interpolate = context.user_preferences.addons[addon_key].preferences.tab_interpolate_menu
            if Display_Interpolate == True:    
                        
                obj = context.active_object     
                if obj:
                   obj_type = obj.type
                                  
                   if obj_type in {'MESH'}:           
               
                        layout.separator()
                          
                        layout.operator("mesh.wplsmthdef_snap", text="Save M-State", icon ="SHAPEKEY_DATA")



        if context.mode == 'EDIT_MESH':
       
            # INTERPOLATE #
            Display_Interpolate = context.user_preferences.addons[addon_key].preferences.tab_interpolate_menu
            if Display_Interpolate == True: 

                layout.separator()

                layout.operator("mesh.wplsmthdef_apply", text="Apply S-Deform", icon ="FRAME_NEXT")


            # SPACE #
            Display_Space = context.user_preferences.addons[addon_key].preferences.tab_space_menu
            if Display_Space == True: 

                layout.separator()
               
                button_align_straigten = icons.get("icon_align_straigten") 
                layout.menu("VIEW3D_TP_Align_Menu_Space", text="Space", icon_value=button_align_straigten.icon_id)   

            

            # TINYCAD #            
            Display_TinyCAD = context.user_preferences.addons[addon_key].preferences.tab_tinycad_menu
            if Display_TinyCAD == True:

                layout.separator()
            
                mesh_tiny_cad_addon = "mesh_tiny_cad" 
                state = addon_utils.check(mesh_tiny_cad_addon)
                if not state[0]:                                         
                    layout.operator("tp_ops.enable_tinycad", text="!_Activate TinyCAD_!", icon='BLANK1')                 
                else:             
                    button_tinycad = icons.get("icon_tinycad")           
                    layout.menu("VIEW3D_MT_edit_mesh_tinycad", text="TinyCAD", icon_value=button_tinycad.icon_id)   



            # LOOPTOOLS #            
            Display_Looptools = context.user_preferences.addons[addon_key].preferences.tab_looptools_menu
            if Display_Looptools == True:
            
                loop_tools_addon = "mesh_looptools" 
                state = addon_utils.check(loop_tools_addon)
                if not state[0]:                                         
                    layout.operator("tp_ops.enable_looptools", text="!_Activate Looptools_!", icon='BLANK1')                 
                else:             

                    layout.separator()

                    button_align_circle = icons.get("icon_align_circle")           
                    layout.menu("VIEW3D_TP_Align_Menu_LoopTools", text="LoopTools", icon_value=button_align_circle.icon_id)   
                 
                    layout.menu("VIEW3D_TP_Align_Menu_Gstretch", text="GStretch", icon="GREASEPENCIL")   
              

            # MESHMACHINE #
            Display_MESHmachine = context.user_preferences.addons[addon_key].preferences.tab_machine_menu
            if Display_MESHmachine == True: 

                layout.separator()
            
                layout.menu("VIEW3D_TP_Machine_Align_Menu", text="MESHmachine", icon="MOD_BEVEL")   


            # RELAX # 
            Display_Relax = context.user_preferences.addons[addon_key].preferences.tab_relax_menu 
            if Display_Relax == True:

                layout.separator()

                button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
                layout.menu("VIEW3D_TP_Align_Menu_Relax", text="Smooth Relax", icon_value=button_align_shrinkwrap.icon_id)   



        # MIRROR # 
        Display_Mirror = context.user_preferences.addons[addon_key].preferences.tab_mirror_menu
        if Display_Mirror == True: 

            layout.separator()

            button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
            layout.menu("VIEW3D_TP_Mirror_Menu", text="Mirror", icon_value=button_align_mirror_obm.icon_id)   
            layout.menu("VIEW3D_TP_ModMirror_Menu", text="Mirror", icon="MOD_MIRROR")   


        # ZERO TO #
        Display_Zero_to = context.user_preferences.addons[addon_key].preferences.tab_zero_to_menu
        if Display_Zero_to == True:  

            layout.separator()
           
            button_align_zero = icons.get("icon_align_zero")                
            layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)      

