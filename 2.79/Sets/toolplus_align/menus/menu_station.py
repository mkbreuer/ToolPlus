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


class VIEW3D_TP_Station_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Station_Menu"
    bl_label = "NP STATION"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()
      
        col = split.column()
  
        col.scale_y = 1.3     
 
        button_snap_grab = icons.get("icon_snap_grab") 
        col.operator("tp_ops.np_020_point_move", text='Point Move', icon_value=button_snap_grab.icon_id)
       
        button_snap_rotate = icons.get("icon_snap_rotate") 
        col.operator("tp_ops.np_020_roto_move", text='Point Roto', icon_value=button_snap_rotate.icon_id)

        button_snap_scale = icons.get("icon_snap_scale") 
        col.operator("tp_ops.np_020_point_scale", text='Point Scale', icon_value=button_snap_scale.icon_id)

        obj = context.active_object
        if obj:
            obj_type = obj.type
            
            if obj.type in {'MESH'}:
                
                button_snap_abc = icons.get("icon_snap_abc") 
                col.operator("tp_ops.np_020_point_align", text='Point ABC', icon_value=button_snap_abc.icon_id)

            else:
                pass
        else:
            pass

        button_snap_ruler = icons.get("icon_snap_ruler") 
        col.operator("tp_ops.np_020_point_distance", text=" Point Distance", icon_value=button_snap_ruler.icon_id)  
      




