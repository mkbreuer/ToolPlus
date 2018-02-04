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



class VIEW3D_TP_ReCoPlanar_Menu(bpy.types.Menu):
    bl_label = "ReCoPlanar"
    bl_idname = "VIEW3D_TP_ReCoPlanar_Menu"   

    def draw(self, context):
        layout = self.layout

        icons = load_icons()          
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'


        button_relocal = icons.get("icon_relocal") 
        layout.operator("tp_ops.set_new_local", icon_value=button_relocal.icon_id) 

        button_recenter = icons.get("icon_recenter") 
        layout.operator("tp_ops.recenter", icon_value=button_recenter.icon_id)  

        button_reposition = icons.get("icon_reposition") 
        layout.operator("tp_ops.reposition", icon_value=button_reposition.icon_id)
      
        button_center = icons.get("icon_center") 
        layout.operator("tp_ops.relocate", text="ReLocate", icon_value=button_center.icon_id)

        button_bloc = icons.get("icon_bloc") 
        layout.operator("tp_ops.copy_local_transform", text="ReTransform", icon_value=button_bloc.icon_id ) 