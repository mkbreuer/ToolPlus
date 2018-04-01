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


class VIEW3D_TP_Header_AOCCL_Menu(bpy.types.Menu):
    """Ambient Occlusion"""
    bl_idname = "VIEW3D_TP_Header_AOCCL_Menu"
    bl_label = " Ambient Occlusion"
    bl_options = {'REGISTER', 'UNDO'}


    def draw(self, context):
        layout = self.layout

        layout.prop(context.space_data.fx_settings.ssao, "factor")
        layout.prop(context.space_data.fx_settings.ssao, "distance_max")
        layout.prop(context.space_data.fx_settings.ssao, "attenuation")
        layout.prop(context.space_data.fx_settings.ssao, "samples")
        layout.label("Set Color:")
        layout.prop(context.space_data.fx_settings.ssao, "color", "")               
  




class VIEW3D_TP_Header_Shading_Menu(bpy.types.Menu):
    bl_label = "Shading"
    bl_idname = "VIEW3D_TP_Header_Shading_Menu"

    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()   

        #button_snap_place = icons.get("icon_snap_place")
        #layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)
 
        view = context.space_data        

        obj = context.object
        obj_type = obj.type

        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_mesh = (obj_type in {'MESH'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
        is_dupli = (obj.dupli_type != 'NONE')

        layout.scale_y = 1.2

        if context.mode == 'OBJECT': 
            

            layout.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
            layout.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  

            if is_mesh:
                
                layout.separator() 

                layout.prop(context.active_object.data, "show_double_sided", text="DoubleSide",icon="GHOST")                      
                layout.prop(context.active_object.data, "use_auto_smooth", text="AutoSmooth",icon="AUTO")
            
                if bpy.context.active_object.data.use_auto_smooth == True:                     
                    layout.prop(context.active_object.data, "auto_smooth_angle", text="AutoSmooth Angle")




            layout.separator() 
            
            if bpy.context.space_data.fx_settings.use_ssao == True:
                layout.menu("VIEW3D_TP_Header_AOCCL_Menu", text="SSAO Setting")

            layout.prop(context.space_data.fx_settings, "use_ssao", text="Ambient Occlusion", icon="GROUP")

            if bpy.context.space_data.use_matcap == True:
                layout.template_icon_view(view, "matcap_icon")             
          
            layout.prop(view, "use_matcap", icon ="MATCAP_01")




        else:
                                   
            if context.mode == 'EDIT_MESH':          
                

                layout.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                layout.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 

                layout.separator() 
      
                layout.prop(context.active_object.data, "auto_smooth_angle", text="AutoSmooth Angle")              
                layout.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                layout.prop(context.active_object.data, "show_double_sided", text="Double Side",icon="GHOST")  

                layout.separator() 
                     
                props = layout.operator("mesh.mark_sharp", text="Clear V-Mark", icon='PANEL_CLOSE')
                props.use_verts = True
                props.clear = True
                layout.operator("mesh.mark_sharp", text="Sharp Verts", icon='SNAP_VERTEX').use_verts = True     

                layout.separator() 
                 

                layout.operator("mesh.mark_sharp", text="Clear E-Sharp", icon='PANEL_CLOSE').clear = True
                layout.operator("mesh.mark_sharp", text="Sharp Edges", icon='SNAP_EDGE')

