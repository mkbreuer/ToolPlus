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


class VIEW3D_TP_Align_Menu_Space(bpy.types.Menu):
    bl_label = "Space"
    bl_idname = "VIEW3D_TP_Align_Menu_Space" 

    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        layout.scale_y = 1.3

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_straigten = icons.get("icon_align_straigten") 
        layout.operator("mesh.vertex_align",text="Straigten", icon_value=button_align_straigten.icon_id) 

        button_align_distribute = icons.get("icon_align_distribute")  
        layout.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_align_distribute.icon_id)                                        
   
        button_align_unbevel = icons.get("icon_align_unbevel") 
        layout.operator("tp_ops.unbevel",text="Unbevel", icon_value=button_align_unbevel.icon_id)     
     
        imdjs_tools_addon = "IMDJS_mesh_tools" 
        state = addon_utils.check(imdjs_tools_addon)
        if not state[0]:
            pass   
        else:  
            button_align_radians = icons.get("icon_align_radians")  
            layout.operator("mesh.round_selected_points", text="Radians", icon_value=button_align_radians.icon_id)  


                

class VIEW3D_TP_Align_Menu_LoopTools(bpy.types.Menu):
    bl_label = "LoopTools"
    bl_idname = "VIEW3D_TP_Align_Menu_LoopTools" 

    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        layout.scale_y = 1.3

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_space = icons.get("icon_align_space")
        layout.operator("mesh.looptools_space", text="LpT  Space", icon_value=button_align_space.icon_id)
       
        button_align_curve = icons.get("icon_align_curve") 
        layout.operator("mesh.looptools_curve", text="LpT  Curve", icon_value=button_align_curve.icon_id)

        button_align_circle = icons.get("icon_align_circle") 
        layout.operator("mesh.looptools_circle", text="LpT  Circle", icon_value=button_align_circle.icon_id)

        button_align_flatten = icons.get("icon_align_flatten")                
        layout.operator("mesh.looptools_flatten", text="LpT  Circle", icon_value=button_align_flatten.icon_id)
 



class VIEW3D_TP_Align_Menu_Relax(bpy.types.Menu):
    bl_label = "Smooth Relax"
    bl_idname = "VIEW3D_TP_Align_Menu_Relax" 

    def draw(self, context):
        layout = self.layout

        icons = load_icons()
    
        layout.scale_y = 1.3
      
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
        expand = panel_prefs.expand_panel_tools

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_align_vertices = icons.get("icon_align_vertices") 
        layout.operator("mesh.vertices_smooth","Smooth Verts", icon_value=button_align_vertices.icon_id) 

        button_align_laplacian = icons.get("icon_align_laplacian")
        layout.operator("mesh.vertices_smooth_laplacian","Smooth Laplacian", icon_value=button_align_laplacian.icon_id)  

        button_align_shrinkwrap = icons.get("icon_align_shrinkwrap")
        layout.operator("mesh.shrinkwrap_smooth","Smooth Shrinkwrap", icon_value=button_align_shrinkwrap.icon_id)                 
               
        Display_Looptools = context.user_preferences.addons[addon_key].preferences.tab_looptools
        if Display_Looptools == 'on':
                
            loop_tools_addon = "mesh_looptools" 
            state = addon_utils.check(loop_tools_addon)
            if not state[0]:
                pass                         
            else: 
                button_align_looptools = icons.get("icon_align_looptools")              
                layout.operator("mesh.looptools_relax", text="LT Smooth Relax", icon_value=button_align_looptools.icon_id)


