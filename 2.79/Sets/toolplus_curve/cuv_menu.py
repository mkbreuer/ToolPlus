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
import bpy, os
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


from toolplus_curve.menus.menu_curve     import *
from toolplus_curve.menus.menu_selection import *


class VIEW3D_TP_Curve_Menu(bpy.types.Menu):
    bl_label = "Curves"
    bl_idname = "VIEW3D_TP_Curve_Menu"   

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_CURVE' or 'EDIT_SURFACE' or 'OBJECT'))   

    def draw(self, context):
        layout = self.layout
        
        icons = load_icons()          
        
        scene = context.scene
        toolsettings = context.tool_settings

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = 1.2    
                           
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences

        obj = context.active_object
        if obj:
            obj_type = obj.type    

            if obj.type in {'CURVE', 'NURBS', 'SURFACE','TEXT','MBALL'}: 
               
                if context.user_preferences.addons[addon_key].preferences.tab_showhide == True:
                
                    if context.mode == 'EDIT_CURVE':                                 
                        layout.menu("tp_menu.curve_select")                
                        layout.menu("tp_menu.curve_delete")                                               
                        layout.menu("VIEW3D_MT_edit_curve_showhide", text= "Show / Hide") 
                    else:
                        layout.menu("tp_menu.curve_select") 
                        layout.menu("VIEW3D_MT_object_showhide", text = "Show / Hide") 
                                    
                    layout.separator() 
        
                layout.prop(context.object.data, "dimensions", text="")      
                layout.menu("tp_menu.curve_spline_type")
                layout.menu("tp_menu.curve_handle_type")
                layout.menu("tp_menu.curve_options")

                layout.separator()

                layout.operator("tp_batch.bevel_props","Bevel")  
               
                if context.mode == 'OBJECT':                    
                    layout.menu("tp_menu.curve_bevel_objects")  

                layout.separator()

                if context.mode == 'EDIT_CURVE':                                      
                    layout.menu("tp_menu.curve_subdiv")
               
                layout.menu("tp_menu.curve_editing")
                layout.menu("tp_menu.curve_material")
                layout.menu("tp_menu.curve_transform")

                if context.mode == 'EDIT_CURVE':    
                   
                    layout.separator()

                    layout.operator("curve.normals_make_consistent")

                    layout.separator()

                    layout.menu("VIEW3D_MT_hook")


            if context.mode == 'OBJECT':      
               
                if obj.type in {'CURVE', 'NURBS', 'SURFACE','TEXT','MBALL'}: 
                     layout.separator()  
                     layout.operator("object.convert",text="Convert to Mesh").target="MESH"                      
                else:
                     layout.menu("tp_menu.curve_material")                     
                     layout.operator("object.convert", text="Convert to Curve").target="CURVE"                
                            