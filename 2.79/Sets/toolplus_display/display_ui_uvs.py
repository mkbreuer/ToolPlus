# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    
    

EDIT = ["OBJECT", "EDIT_MESH"]
GEOM = ['MESH']

class draw_layout_uvs:

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        #layout.operator_context = 'INVOKE_AREA'

        tp = context.window_manager.tp_props_display  

        icons = load_icons()


        if context.mode == 'OBJECT':

            box = layout.box().column(1) 

            obj = context.active_object
            if obj:
                row = box.row()   
                row.template_list("MESH_UL_uvmaps_vcols", "uvmaps", context.object.data, "uv_textures", context.object.data.uv_textures, "active_index", rows=2)
           
                row = row.column(1)
                row.operator("mesh.uv_texture_add", icon='ZOOMIN', text="")
                row.operator("mesh.uv_texture_remove", icon='ZOOMOUT', text="")                  
                if context.space_data.viewport_shade == 'SOLID':
                    row.prop(context.space_data, "show_textured_solid", icon='TEXTURE_SHADED', text="")

                box.separator() 
                box.separator() 

            else:
                pass


                           
            row = box.column(1) 
            row.operator("uv.uv_equalize" , text ="UV Equalize", icon = 'MOD_UVPROJECT')           
            row.operator("uthe.main_operator", text = "UV HardEdges", icon = 'MOD_EDGESPLIT')
            
            row.separator() 

            row.operator("uv.smart_project", text="Smart UV Project")
            row.operator("uv.lightmap_pack", text="Lightmap Pack")


        if context.mode == 'EDIT_MESH':
            
            box = layout.box().column(1) 
              
            row = box.column(1)
            row.label(text="UV Mapping:")

            box.separator()
            
            row = box.row(1)        
            row.operator("mesh.mark_seam").clear = False
            row.operator("mesh.mark_seam", text="Clear Seam").clear = True

            box.separator()
            box.separator()
                        
         
            row = box.row(1)    
            
            if tp.display_unwrap:
                row.prop(tp, "display_unwrap", text="Unwrap", icon='TRIA_DOWN_BAR')
            else:
                row.prop(tp, "display_unwrap", text="Unwrap", icon='TRIA_UP_BAR')          
           

            if tp.display_uvmagic:
                row.prop(tp, "display_uvmagic", text="Magic UVs", icon='TRIA_DOWN_BAR')
            else:
                row.prop(tp, "display_uvmagic", text="Magic UVs", icon='TRIA_UP_BAR')          


            box.separator()
               

            row = box.row(1)    

            if tp.display_unwrap:

                #box = layout.box().column(1) 
              
                row = box.row(1)
                row.operator("uv.unwrap", text="Unwrap")
                row.operator("uv.reset",text="Reset")
                                
                row = box.row(1)
                row.operator("uv.smart_project", text="Smart UV Project")
                                
                row = box.row(1)
                row.operator("uv.lightmap_pack", text="Lightmap Pack")
                                
                row = box.row(1)
                row.operator("uv.follow_active_quads", text="Follow Active Quads")

                box.separator()                                         
                box.separator()                                         
                
                row = box.row(1)
                row.operator("uv.cube_project", text="Cube Project")
                
                row = box.row(1)
                row.operator("uv.cylinder_project", text="Cylinder Project")

                row = box.row(1)
                row.operator("uv.sphere_project", text="Sphere Project")

                row = box.row(1)
                row.operator("uv.tube_uv_unwrap", text="Tube Project")                

                box.separator()
                box.separator()
                                                           
                row = box.row(1)
                row.operator("uv.project_from_view", text="Project from View").scale_to_bounds = False

                row = box.row(1)
                row.operator("uv.project_from_view", text="Project from View > Bounds").scale_to_bounds = True 
                
                box.separator()       

            if tp.display_uvmagic:
                
                box = layout.box().column(1) 
                            
                row = box.column(1)
                row.operator("uv.cpuv_copy_uv")
                row.operator("uv.cpuv_paste_uv")
                row.operator("uv.flip_rotate")
                row.operator("uv.transfer_uv_copy")
                row.operator("uv.transfer_uv_paste")
                row.operator("uv.cpuv_selseq_copy_uv")
                row.operator("uv.cpuv_selseq_paste_uv")

                row.operator("uv.cpuv_uvmap_copy_uv_op")
                row.operator("uv.cpuv_uvmap_paste_uv_op")

                box.separator()  



class VIEW3D_TP_UVS_Panel_TOOLS(bpy.types.Panel, draw_layout_uvs):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_UVS_Panel_TOOLS"
    bl_label = "UVs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_UVS_Panel_UI(bpy.types.Panel, draw_layout_uvs):
    bl_idname = "VIEW3D_TP_UVS_Panel_UI"
    bl_label = "UVs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
