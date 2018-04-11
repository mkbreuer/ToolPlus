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
from .. icons.icons import load_icons  


class VIEW3D_TP_Header_Station_Menu(bpy.types.Menu):
    bl_label = "Station"
    bl_idname = "VIEW3D_TP_Header_Station_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   
       
        layout.operator_context = 'INVOKE_REGION_WIN'    
      
        #layout.label("")  

        obj = context.active_object        
        obj_type = obj.type    
        is_mesh = (obj_type in {'MESH'})  

        layout.scale_y = 1.5
     
        button_snap_ruler = icons.get("icon_snap_ruler") 
        layout.operator("tp_ops.np_020_point_distance", text='Point Distance', icon_value = button_snap_ruler.icon_id)


        if context.mode == 'OBJECT':

            button_snap_grab = icons.get("icon_snap_grab") 
            layout.operator("tp_ops.np_020_point_move", text='Point Move', icon_value=button_snap_grab.icon_id)                   
    
            
        if is_mesh and context.mode == 'OBJECT':

            button_snap_rotate = icons.get("icon_snap_rotate") 
            layout.operator("tp_ops.np_020_roto_move", text='Roto Move', icon_value=button_snap_rotate.icon_id)
     
            button_snap_scale = icons.get("icon_snap_scale") 
            layout.operator("tp_ops.np_020_point_scale", text='Point Scale', icon_value=button_snap_scale.icon_id)

            button_snap_abc = icons.get("icon_snap_abc") 
            layout.operator("tp_ops.np_020_point_align", text='Point Align', icon_value=button_snap_abc.icon_id) 


        if is_mesh:

            button_snap_line = icons.get("icon_snap_line") 
            layout.operator("tp_ops.snapline", text='SnapLine', icon_value=button_snap_line.icon_id) 
            
            
        layout.separator()                
        
        layout.label("Snap Transform")            

