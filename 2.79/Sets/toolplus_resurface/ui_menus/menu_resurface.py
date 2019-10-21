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


def draw_resurface_menu_layout(self, context, layout):
          
        icons = load_icons()

        layout.operator("view3d.sct_pick_surface_constraint", text="Pick Up", icon="HAND")




class VIEW3D_TP_ReSurface_Menu(bpy.types.Menu):
    bl_label = "ReSurface"
    bl_idname = "VIEW3D_TP_ReSurface_Menu"   

    def draw(self, context):
        layout = self.layout

        icons = load_icons()          
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
      
  
        ob = context
        if ob.mode == 'OBJECT':

#        button_align_zero = icons.get("icon_align_zero")                
#        layout.operator("tp_ops.zero_axis", "ZeroAxis", icon_value=button_align_zero.icon_id)      

            layout.operator("view3d.sct_pick_surface_constraint", text="Pick Up", icon="HAND")
    
        if ob.mode == 'EDIT_MESH':

            layout.operator("view3d.sct_pick_surface_constraint", text="Pick Up", icon="HAND")
           
            layout.separator()

            layout.operator("mesh.sct_mesh_brush", text="Sculpt", icon="MOD_DYNAMICPAINT")
            layout.operator("mesh.sct_smooth_vertices", text="Smooth", icon="MOD_SMOOTH")
            layout.operator("mesh.sct_shrinkwrap", text="Shrink", icon="MOD_SHRINKWRAP")


#        if ob.mode == 'EDIT_CURVE':
#            
#            draw_resurface_menu_layout(self, context, layout) 
#     
#        if ob.mode == 'EDIT_SURFACE':
#            
#            draw_resurface_menu_layout(self, context, layout) 

#        if ob.mode == 'EDIT_METABALL':
#            
#            draw_resurface_menu_layout(self, context, layout) 
#   
#        if ob.mode == 'EDIT_LATTICE':
#            
#            draw_resurface_menu_layout(self, context, layout)             
#                 
#        if  context.mode == 'PARTICLE':
#       
#            draw_resurface_menu_layout(self, context, layout) 

#        if ob.mode == 'EDIT_ARMATURE':

#            draw_resurface_menu_layout(self, context, layout)             

#        if context.mode == 'POSE':

#            draw_resurface_menu_layout(self, context, layout) 
#             
#        layout.separator()
#       
