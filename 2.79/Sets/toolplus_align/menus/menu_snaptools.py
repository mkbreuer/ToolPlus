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


class VIEW3D_TP_SnapTools_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_SnapTools_Menu"
    bl_label = "SnapTools"

    def draw(self, context):
        layout = self.layout
   
        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.scale_y = 1.3

        if context.mode == 'EDIT_MESH': 

            button_align_planar = icons.get("icon_align_planar") 
            layout.operator("mesh.face_make_planar", "Planar Faces", icon_value=button_align_planar.icon_id)   
            
            button_align_con_face = icons.get("icon_align_con_face") 
            layout.operator("mesh.rot_con", "Square Rotation", icon_value=button_align_con_face.icon_id)   

            button_snap_offset = icons.get("icon_snap_offset")  
            layout.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   

            button_origin_mesh = icons.get("icon_origin_mesh")                
            layout.operator("tp_ops.origin_transform", "Advanced", icon_value=button_origin_mesh.icon_id)   
           


        else:

            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:

                    button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                    layout.operator("object.align_by_faces", text="Face to Face", icon_value=button_snap_face_to_face.icon_id)  

                    button_snap_drop_down = icons.get("icon_snap_drop_down") 
                    layout.operator("object.drop_on_active", text="Drop on Active", icon_value=button_snap_drop_down.icon_id) 

                    button_snap_offset = icons.get("icon_snap_offset")  
                    layout.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   

                else:
                    pass
            else:
                pass


        if context.mode == 'OBJECT': 
            
            layout.separator() 

            button_origin_distribute = icons.get("icon_origin_distribute")  
            layout.operator("object.distribute_osc", "Distribute", icon_value=button_origin_distribute.icon_id)                   

            button_align_advance = icons.get("icon_align_advance")
            layout.operator("tp_origin.align_tools", "Align Advance", icon_value=button_align_advance.icon_id)    

