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
#from .. icons.icons import load_icons    


class VIEW3D_TP_Menu_Edge_Edit(bpy.types.Menu):
    bl_label = "Edge Edit"
    bl_idname = "tp_menu.edge_edit" 
    
    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))    

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'
        with_freestyle = bpy.app.build_options.freestyle
        scene = context.scene
        
        layout.operator("mesh.edge_face_add", icon = "MOD_TRIANGULATE")
        layout.operator("mesh.subdivide")
        layout.operator("mesh.unsubdivide")
                             
        layout.separator()

        layout.operator("mesh.bevel", icon = "MOD_EDGESPLIT").vertex_only = False
        layout.operator("mesh.edge_split")

        layout.separator()
        
        layout.operator("mesh.bridge_edge_loops", icon = "SOUND")
        
        layout.separator()
        
        layout.operator("transform.edge_slide", icon = "IPO_LINEAR")            

        layout.separator()
        
        layout.operator("mesh.edge_rotate", text="Rotate Edge CW", icon = "FILE_REFRESH").use_ccw = False
        layout.operator("mesh.edge_rotate", text="Rotate Edge CCW").use_ccw = True

        layout.separator()
        
        layout.operator("mesh.loop_multi_select",text="Edge Loop", icon="ZOOMOUT").ring=False          
        layout.operator("mesh.loop_multi_select",text="Edge Ring", icon="COLLAPSEMENU").ring=True
        layout.operator("mesh.select_nth") 

        layout.separator()
        
        layout.operator("mesh.region_to_loop")
        layout.operator("mesh.loop_to_region") 





