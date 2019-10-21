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


class VIEW3D_TP_VertAdditional_Menu(bpy.types.Menu):
    bl_label = "Additional"
    bl_idname = "tp_menu.additional"
    
    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("mesh.convex_hull")
        layout.operator("mesh.blend_from_shape")
        layout.operator("mesh.shape_propagate_to_all")        



class VIEW3D_TP_Menu_Vert_Edit(bpy.types.Menu):
    bl_label = "Vertices Edit"
    bl_idname = "tp_menu.vert_edit"   


    def draw(self, context):
        settings = context.tool_settings
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'        

 
        layout.operator("mesh.fill_holes", icon="MOD_TRIANGULATE") 

        layout.separator()   
        
        layout.operator("mesh.merge", icon="AUTOMERGE_ON")
        layout.operator("mesh.vert_connect", text="Connect Vert")        
        layout.operator("mesh.vert_connect_path", text="Connect Path")  
               
        layout.separator()                 
    
        layout.operator("mesh.rip_move", icon="FULLSCREEN_ENTER")
        layout.operator("mesh.rip_move_fill")        
        layout.operator("mesh.rip_edge_move") 
                
        layout.separator()

        layout.operator("mesh.bevel", icon="MOD_BEVEL").vertex_only = True 

        layout.separator() 
        
        layout.operator("transform.vert_slide", text="Vertices Slide", icon="PARTICLE_PATH")     
        layout.operator("mesh.vertices_smooth")
                    
        layout.separator()                     

        layout.operator("mesh.split", icon = "MOD_DISPLACE")
        layout.operator_menu_enum("mesh.separate", "type")

        layout.separator()
        
        layout.operator("mesh.mark_sharp", text="Mark Sharp", icon="SNAP_VERTEX").use_verts = True        
        op = layout.operator("mesh.mark_sharp", text="Clear Sharp")
        op.use_verts = True
        op.clear = True
        
        layout.separator() 
                 
        layout.menu("tp_menu.additional", icon = "RESTRICT_SELECT_OFF")  
        
        layout.separator()

        layout.menu("VIEW3D_MT_hook", icon = "HOOK")         
        
        layout.separator()

        layout.menu("vgroupmenu", icon = "GROUP_VERTEX")
        layout.menu("MESH_MT_vertex_group_specials", text="Vertex Group Specials")
           













