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


class VIEW3D_TP_Menu_Edge_Visual(bpy.types.Menu):
    bl_label = "Edge Visual"
    bl_idname = "tp_menu.edge_visual" 
    
    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))    

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene		
	
        with_freestyle = bpy.app.build_options.freestyle

        layout.operator("mesh.mark_seam", icon = "UV_EDGESEL").clear = False
        layout.operator("mesh.mark_seam", text="Clear Seam").clear = True

        layout.separator()

        layout.operator("mesh.mark_sharp", icon = "SNAP_EDGE").clear = False
        layout.operator("mesh.mark_sharp", text="Clear Sharp").clear = True

        layout.separator()

        layout.operator("transform.edge_crease", icon="IPO_CIRC")
        layout.operator("transform.edge_bevelweight")

        layout.separator()

        if with_freestyle and not scene.render.use_shading_nodes:
            layout.operator("mesh.mark_freestyle_edge", icon="IPO_SINE").clear = False
            layout.operator("mesh.mark_freestyle_edge", text="Clear Freestyle Edge").clear = True

        layout.separator()            

        layout.prop(mesh, "show_extra_edge_length", text="Edge Length Info", icon="INFO")
        layout.prop(mesh, "show_extra_edge_angle", text="Edge Angle Info", icon="INFO")
		


