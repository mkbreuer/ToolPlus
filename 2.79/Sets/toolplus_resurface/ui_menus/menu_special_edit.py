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

# ADDON CHECK #
import addon_utils



# SUB MENUS #

class VIEW3D_TP_SubDivide(bpy.types.Menu):
    bl_label = "Subdivide"
    bl_idname = "tp_menu.subdivide"
    
    def draw(self, context):
        layout = self.layout
            
        split = layout.split()
     
        col = split.column()
        col.operator("mesh.subdivide",text="1-Cut").number_cuts=1
        col.operator("mesh.subdivide",text="2-Cuts").number_cuts=2
        col.operator("mesh.subdivide",text="3-Cuts").number_cuts=3
        col.operator("mesh.subdivide",text="4-Cuts").number_cuts=4
        col.operator("mesh.subdivide",text="5-Cuts").number_cuts=5
        col.operator("mesh.subdivide",text="6-Cuts").number_cuts=6 
        
        col = split.column()
        col.operator("mesh.subdivide", text="1-Smooth").smoothness = 1.0
        col.operator("mesh.subdivide", text="2-Smooth").smoothness = 2.0
        col.operator("mesh.subdivide", text="4-Smooth").smoothness = 4.0
        col.operator("mesh.subdivide", text="6-Smooth").smoothness = 6.0
        col.operator("mesh.subdivide", text="8-Smooth").smoothness = 8.0
        col.operator("mesh.subdivide", text="10-Smooth").smoothness =10.0




class VIEW3D_TP_Menu_Special_Edit(bpy.types.Menu):
    bl_label = "Special"
    bl_idname = "tp_menu.special_edit"    

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        if context.mode == 'EDIT_MESH':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')  
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")
            
            layout.separator() 

            tinycad_addon = "mesh_tiny_cad" 
            state = addon_utils.check(tinycad_addon)
            if not state[0]:
                pass                         
            else: 
                layout.menu("VIEW3D_MT_edit_mesh_tinycad")            


            loop_tools_addon = "mesh_looptools" 
            state = addon_utils.check(loop_tools_addon)
            if not state[0]:
                pass                         
            else: 
                layout.menu("VIEW3D_MT_edit_mesh_looptools", icon='RIGHTARROW_THIN')
                    

            layout.separator() 
        
            layout.menu("tp_menu.subdivide", text="Subdivide", icon='PARTICLE_POINT') 
            layout.operator("mesh.unsubdivide", text="Un-Subdivide")                                   


            layout.separator()

            layout.operator("mesh.merge", text="Merge...", icon = "FULLSCREEN_EXIT")
            layout.operator("mesh.remove_doubles")

            
            layout.separator()
            
            layout.operator("mesh.spin", icon ="ANIM_DATA")
            layout.operator("mesh.screw")
            
            layout.separator()

            props = layout.operator("mesh.knife_tool", text="Knife", icon = "LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False
            props = layout.operator("mesh.knife_tool", text="Select")
            props.use_occlude_geometry = False
            props.only_selected = True
            layout.operator("mesh.knife_project")
          
            layout.separator() 
            
            layout.operator("mesh.bisect")  

            layout.separator()              
            
            layout.operator("mesh.bevel", text="Bevel", icon = "SPHERECURVE")        
            layout.operator("mesh.inset")        
            layout.operator("mesh.bridge_edge_loops")     
        
            layout.separator()        
        
            layout.operator("mesh.vertices_smooth", text="Vertices Smooth", icon = "CURVE_DATA")        
            layout.operator("mesh.vertices_smooth_laplacian", text="Laplacian Smooth")            

            layout.separator()        
      
            layout.operator_menu_enum("mesh.separate", "type", text="Separate")

            layout.separator()       

            layout.operator("mesh.symmetrize")
            layout.operator("mesh.symmetry_snap")

            layout.separator() 
                  
            layout.operator("mesh.blend_from_shape")
            layout.operator("mesh.shape_propagate_to_all")
            layout.operator("mesh.shortest_path_select")
            layout.operator("mesh.sort_elements")






























