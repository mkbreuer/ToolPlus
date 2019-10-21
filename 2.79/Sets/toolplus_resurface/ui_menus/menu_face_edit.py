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



class VIEW3D_TP_Menu_Face_Edit(bpy.types.Menu):
    bl_label = "Face Edit"
    bl_idname = "tp_menu.face_edit"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        scene = context.scene
        
        layout.operator("mesh.edge_face_add", icon = "MOD_TRIANGULATE")
        layout.operator("mesh.subdivide")
        layout.operator("mesh.unsubdivide")               

        layout.separator()        

        layout.operator("mesh.intersect")
        layout.operator("mesh.intersect_boolean")

        layout.separator()        
        
        layout.operator("mesh.fill", icon = "MOD_MESHDEFORM")
        layout.operator("mesh.fill_grid")        
        layout.operator("mesh.beautify_fill")     

        layout.separator()
        
        layout.menu("VIEW3D_MT_edit_mesh_extrude", icon = "MOD_BOOLEAN")
        layout.operator("mesh.poke",  text="Poke Inset")                
        layout.operator("mesh.inset",  text="Face Inset")
      
        layout.separator()
      
        layout.operator("mesh.face_split_by_edges")        
      
        layout.separator()
                      
        layout.operator("mesh.bevel", icon = "MOD_BEVEL").vertex_only = False
        layout.operator("mesh.solidify")
        layout.operator("mesh.wireframe")        
        
        layout.separator()	

        layout.operator("mesh.face_make_planar", "Planar Faces", icon="MOD_DISPLACE") 

        layout.separator()

        layout.operator("mesh.quads_convert_to_tris", icon="OUTLINER_DATA_MESH")
        layout.operator("mesh.tris_convert_to_quads", icon="OUTLINER_DATA_LATTICE") 
        
            

