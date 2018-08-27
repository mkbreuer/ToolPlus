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


class VIEW3D_TP_Closer_Menu(bpy.types.Menu):
    """the functions are depends on the position of the mouse cursor"""
    bl_label = "Closer"
    bl_idname = "VIEW3D_TP_Closer_Menu"   
    
    """
    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))
    """ 

    def draw(self, context):
        settings = context.tool_settings
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'        

        obj = context.object      
        #if obj.mode == 'OBJECT':
            #layout.operator("object.editnormals_transfer", icon="SNAP_NORMAL")  
               
        if obj.mode == 'EDIT':

            layout.operator("screen.redo_last", icon="SCRIPTWIN")
                          
            layout.separator()
                    
            layout.operator("mesh.rip_move", icon="FULLSCREEN_ENTER")
            layout.operator("mesh.rip_move_fill")        
            layout.operator("mesh.rip_edge_move")
            layout.operator("mesh.split")

            layout.separator()

            layout.operator("mesh.shrinkwrap_smooth","Shrinkwrap Smooth", icon ="BLANK1")      
            
            layout.separator()

            layout.operator("mesh.merge","Merge Center").type='CENTER'               
            layout.operator_menu_enum("mesh.merge", "type")  

            layout.separator()
            
            props= layout.operator('mesh.offset_edges', "Offset Edges")
            props.geometry_mode = 'extrude'
            
            layout.operator('faceinfillet.op0_id', text = 'Face Fillet')  

            layout.separator()
            
            #layout.operator("mesh.fill_grid", "Grid Fill")       
 
            props= layout.operator("mesh.closer", "Tri Face")
            props.tris = True
            props.quads = False
             
            props= layout.operator("mesh.closer", "Quad Face")
            props.tris = False
            props.quads = True      
                
            layout.operator('mesh.build_corner', icon ="BLANK1")  










