__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


class VIEW3D_TP_Relax_Menu(bpy.types.Menu):
    bl_label = "Relax :) "
    bl_idname = "tp_menu.relax_base"   

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))

    def draw(self, context):
        layout = self.layout

        icons = load_icons()          

        layout.operator_context = 'INVOKE_REGION_WIN'

        button_relax_vertices = icons.get("icon_relax_vertices") 
        layout.operator("mesh.vertices_smooth","Vertices", icon_value=button_relax_vertices.icon_id) 

        button_relax_laplacian = icons.get("icon_relax_laplacian")
        layout.operator("mesh.vertices_smooth_laplacian","Laplacian", icon_value=button_relax_laplacian.icon_id)  

        button_relax_shrinkwrap = icons.get("icon_relax_shrinkwrap")
        layout.operator("mesh.shrinkwrap_smooth","Shrinkwrap", icon_value=button_relax_shrinkwrap.icon_id)         

        layout.separator()      

        button_relax_planar = icons.get("icon_relax_planar")  
        layout.operator("mesh.face_make_planar", "Planar Faces", icon_value=button_relax_planar.icon_id) 

        layout.separator()    

        button_relax_looptools = icons.get("icon_relax_looptools")
        layout.operator("edit_mesh.looptools_relax", text="LoopTool Relax", icon_value=button_relax_looptools.icon_id)
