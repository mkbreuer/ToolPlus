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



class VIEW3D_TP_Menu_Face_Visual(bpy.types.Menu):
    bl_label = "Face Visual"
    bl_idname = "tp_menu.face_visual"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))
    
    def draw(self, context):
        layout = self.layout
        with_freestyle = bpy.app.build_options.freestyle

        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene		
        
        layout.operator("mesh.normals_make_consistent", text="Recalculate", icon="SNAP_NORMAL")
        layout.operator("mesh.normals_make_consistent", text="-> Inside").inside = True        
        layout.operator("mesh.normals_make_consistent", text="-> Outside").inside = False

        layout.separator()

        layout.operator("mesh.flip_normals", icon="SNAP_NORMAL") 
		
        layout.separator()
		
        layout.prop(mesh, "show_normal_vertex", text="Show Vertex Normal", icon='VERTEXSEL')
        layout.prop(mesh, "show_normal_face", text="Show Face Normal", icon='FACESEL')		
        layout.prop(context.scene.tool_settings, "normal_size", text="Normal Size")

        layout.separator()

        layout.operator("mesh.uvs_rotate", icon="UV_FACESEL")
        layout.operator("mesh.uvs_reverse")
        layout.operator("view3d.move_uv", text ="Move UV [ALT+G]", icon="UV_FACESEL")
        layout.operator("uv.copy_uv",icon="PASTEFLIPUP")
        layout.operator("uv.paste_uv", icon="PASTEFLIPDOWN") 
		
        layout.separator()
        layout.operator("mesh.colors_rotate", icon="COLOR")
        layout.operator("mesh.colors_reverse")

        layout.separator()

        if with_freestyle and not scene.render.use_shading_nodes:
            layout.operator("mesh.mark_freestyle_face", icon="IPO_SINE").clear = False
            layout.operator("mesh.mark_freestyle_face", text="Clear Freestyle Face").clear = True
			
        layout.separator()

        layout.prop(mesh, "show_extra_face_area", text="Face Area Info", icon="INFO")
        layout.prop(mesh, "show_extra_face_angle", text="Face Angle Info", icon="INFO")




