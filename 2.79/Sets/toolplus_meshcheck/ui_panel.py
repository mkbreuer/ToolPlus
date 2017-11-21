# ##### BEGIN GPL LICENSE BLOCK #####
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

from toolplus_meshcheck.check_meshlint import *
from toolplus_meshcheck.check_meshmat import *

import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

import bmesh
from . import report


class MeshCheckBar:

    _type_to_icon = {
        bmesh.types.BMVert: 'VERTEXSEL',
        bmesh.types.BMEdge: 'EDGESEL',
        bmesh.types.BMFace: 'FACESEL',
        }

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object
        return obj and obj.type == 'MESH' and context.mode in {'OBJECT','EDIT_MESH'} and isModelingMode

    @staticmethod
    def draw_report(layout, context):
        """Display Reports"""
        info = report.info()
        if info:
            obj = context.edit_object

            layout.label("Output:")
            
            box = layout.box()
            col = box.column(align=False)
            # box.alert = True
            for i, (text, data) in enumerate(info):
                if obj and data and data[1]:
                    bm_type, bm_array = data
                    col.operator("mesh.print3d_select_report",
                                 text=text,
                                 icon=MeshCheckBar._type_to_icon[bm_type]).index = i
                    layout.operator("mesh.select_non_manifold", text='Non Manifold Extended')
                else:
                    col.label(text)


    def draw(self, context):
        layout = self.layout

        scene = context.scene
        print_3d = scene.print_3d


        layout = self.layout.column_flow(1)  

        scene = context.scene
        print_3d = scene.print_3d

        tp_props = context.window_manager.tp_props_meshcheck 
        tp_orphan = context.scene.orphan_props 
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        icons = load_icons()


        col = layout.column(align=True)
        
#        box = col.box().column(1)

#        row = box.row(1)
#                  
#        row.prop(bpy.context.space_data, 'viewport_shade', text='', expand=True)

#        if context.mode == "EDIT_MESH":

#            row = box.row(1)          
#            layout.operator_context = 'INVOKE_REGION_WIN'
#            row.operator("mesh.select_mode", text="Vert", icon='VERTEXSEL').type = 'VERT'
#            row.operator("mesh.select_mode", text="Edge", icon='EDGESEL').type = 'EDGE'
#            row.operator("mesh.select_mode", text="Face", icon='FACESEL').type = 'FACE'  


        box = col.box().column(1)         

        row = box.row(1)

        if tp_props.display_measure_toggle:
            row.prop(tp_props, "display_measure_toggle", text="", icon='TRIA_DOWN')
            row.label(text='Ruler')

            button_ruler_triangle = icons.get("icon_ruler_triangle")       
            row.operator("tp_ops.np_020_point_distance", text="", icon_value=button_ruler_triangle.icon_id)       


        else:
            row.prop(tp_props, "display_measure_toggle", text="", icon='TRIA_RIGHT')    
            row.label(text='Ruler')
            
            button_ruler_triangle = icons.get("icon_ruler_triangle")       
            row.operator("tp_ops.np_020_point_distance", text="", icon_value=button_ruler_triangle.icon_id)       


        if tp_props.display_measure_toggle:
            
            box = col.box().column(1)
            
            row = box.column(1)            
            row.operator("view3d.ruler", text="Default Ruler", icon="ALIGN")  
            
            button_ruler_triangle = icons.get("icon_ruler_triangle")       
            row.operator("tp_ops.np_020_point_distance", text="Point Distance", icon_value=button_ruler_triangle.icon_id)       

            box.separator()   
            
            if context.mode == "EDIT_MESH":

                box = col.box().column(1)
                
                row = box.row(1)
                row.prop(context.active_object.data, "show_extra_edge_length", text="Edge Length")
                row.prop(context.active_object.data, "show_extra_face_area", text="Face Area")

                row = box.row(1)
                row.prop(context.active_object.data, "show_extra_edge_angle", text="Edge Angle")
                row.prop(context.active_object.data, "show_extra_face_angle", text="Face Angle")

                box.separator()   



        box = col.box().column(1)

        row = box.row(1)

        if not tp_props.display_print3d_toggle:
            row.prop(tp_props, "display_print3d_toggle", text="", icon='TRIA_RIGHT')
            row.label(text='Check All')
            row.operator('mesh.print3d_check_all', text='', icon='UV_SYNC_SELECT')  

        else:
            row.prop(tp_props, "display_print3d_toggle", text="", icon='TRIA_DOWN')    
            row.label(text='Check All')
            row.operator('mesh.print3d_check_all', text='', icon='UV_SYNC_SELECT')   

            box = col.box().column(1)

            row = box.row(1)  

            row = box.row(1)
            row.label("Separate Checks:")
            
            row = box.row(1)
            row.operator("mesh.print3d_check_solid", text="Solid")
            row.operator("mesh.print3d_check_intersect", text="Intersections")
            
            row = box.row(1)
            row.operator("mesh.print3d_check_degenerate", text="Degenerate")
            row.prop(print_3d, "threshold_zero", text="")
           
            row = box.row(1)
            row.operator("mesh.print3d_check_distort", text="Distorted")
            row.prop(print_3d, "angle_distort", text="")

            row = box.row(1)       
            row.operator("mesh.print3d_check_thick", text="Thickness")
            row.prop(print_3d, "thickness_min", text="")

            row = box.row(1)       
            row.operator("mesh.print3d_check_sharp", text="Edge Sharp")
            row.prop(print_3d, "angle_sharp", text="")
           
            row = box.row(1)
            row.operator("mesh.print3d_check_overhang", text="Overhang")
            row.prop(print_3d, "angle_overhang", text="")

            box.separator()


         
        box = col.box().column(1)         

        row = box.row(1)

        if tp_props.display_meshlint_toggle:
            row.prop(tp_props, "display_meshlint_toggle", text="", icon='TRIA_DOWN')
            row.label(text='Clean Up')
            row.operator("mesh.print3d_clean_non_manifold", text='', icon='LOOPSEL')         


        else:
            row.prop(tp_props, "display_meshlint_toggle", text="", icon='TRIA_RIGHT')    
            row.label(text='Clean Up')
            row.operator("mesh.print3d_clean_non_manifold", text='', icon='LOOPSEL')         


        if tp_props.display_meshlint_toggle:
            
            box = col.box().column(1)

            row = box.row(1)  
            row.label("Multi Cleaner:")

            row = box.row(1)  
            row.operator("mesh.print3d_clean_isolated", text="Remove Isolated")
            row.operator("mesh.print3d_clean_non_manifold", text="Make Manifold")               
         
            row = box.row(1)  
            row.operator("mesh.print3d_clean_distorted", text="Triangulate")
            row.prop(print_3d, "angle_distort", text="")

            box.separator()

            if context.mode == "OBJECT":

                box = col.box().column(1)  

                row = box.row(1)               
                row.prop(tp_orphan, "mod_list")
                row.operator("tp_ops.delete_data_obs","Scene Purge", icon ="GHOST_DISABLED")            
             
                box.separator()


            if context.mode == "EDIT_MESH":
                
                box = col.box().column(1)

                row = box.row(1)  
                row.label("Single Cleaner:")

                row = box.row(1)                  
                row.operator("mesh.fill_holes",text="Fill Holes")  
                row.operator("mesh.remove_doubles",text="Rem. Doubles")    
 
                row = box.row(1)             
                row.operator("mesh.select_loose",text="Select Loose")
                row.operator("mesh.delete_loose",text="Delete Loose") 

                row = box.row(1)   
                row.operator("mesh.decimate", text="Decimate")
                row.operator("mesh.face_make_planar", text="Planar Faces")

                box.separator()

                row = box.column(1)   
                row.operator("mesh.dissolve_limited", text="Dissolve Limited")
                row.operator("mesh.dissolve_degenerate", text="Dissolve Degenerate")
 
                box.separator()

                row = box.column(1)    
                row.operator("mesh.vert_connect_nonplanar")
                row.operator("mesh.vert_connect_concave")

                box.separator()





        box = col.box().column(1)  

        if not tp_props.display_mcheck_toggle: 
            row = box.row(1)   
            row.prop(tp_props, "display_mcheck_toggle", text="", icon="TRIA_RIGHT")                
            row.label("Mesh Mat")

            mesh_check = bpy.context.window_manager.mesh_check
            row.prop(mesh_check, "display_faces", text='', icon='GROUP_VCOL')
            
        else:
            row = box.row(1)   
            row.prop(tp_props, "display_mcheck_toggle", text="", icon="TRIA_RIGHT")                
            row.label("Mesh Mat")   

            row.prop(context.window_manager.mesh_check, "display_faces", text='', icon='GROUP_VCOL')


            box = col.box().column(1)   

            row = box.row(1)
            button_tris = icons.get("icon_check_triangle")                
            row.operator("object.face_type_select", text="Tris", icon_value=button_tris.icon_id).face_type = 'tris'
            
            button_ngon = icons.get("icon_check_ngon")                
            row.operator("object.face_type_select", text="Ngons",icon_value=button_ngon.icon_id).face_type = 'ngons'

            box.separator()
            
            row = box.row()
            mesh_check = bpy.context.window_manager.mesh_check
            row.prop(mesh_check, "mesh_check_use", text="MeshCheck")
            row.prop(mesh_check, "display_faces", text="Colored")            

            box.separator()

            if mesh_check.display_faces:
                
                row = box.row()
                row.prop(mesh_check, "edge_width")
                row.prop(mesh_check, "face_opacity")
                
                box.separator()
                
                row = box.row()
                row.label(text="Custom Colors:", icon="COLOR")

                row = box.row(1)
                row.label(text="", icon_value=button_tris.icon_id)
                row.prop(mesh_check, "custom_tri_color", text="")

                row = box.row(1)
                row.label(text="", icon_value=button_ngon.icon_id)
                row.prop(mesh_check, "custom_ngons_color", text="")

                box.separator()

                row = box.row(1)
                if bpy.app.debug:
                    obj_data = getattr(context.active_object, "data", None)
                    if obj_data:
                        row.prop(obj_data, "show_extra_indices",
                                 icon="LINENUMBERS_ON", toggle=True)

                if context.mode == 'EDIT_MESH' and not context.space_data.use_occlude_geometry:
                    row.prop(mesh_check, "finer_lines_behind_use", icon="ORTHO")

                box.separator() 




        box = col.box().column(1) 
       
        if not tp_props.display_shade_toggle:
            row = box.row(1)
            row.prop(tp_props, "display_shade_toggle", text="", icon='TRIA_RIGHT')
            row.label(text="Mesh Shade")
                  
            row.prop(context.active_object.data, "use_auto_smooth", text="",icon="AUTO") 

        else:
            row = box.row(1)                      
            row.prop(tp_props, "display_shade_toggle", text="", icon='TRIA_DOWN')
            row.label(text="Mesh Shade")
           
            row.prop(context.active_object.data, "use_auto_smooth", text="",icon="AUTO") 
          
            box = col.box().column(1) 

            if context.mode == "OBJECT":

                row = box.row(1)  
                row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
           
                box.separator() 
                
                obj = context.active_object     
                if obj:
                   obj_type = obj.type
                                  
                   if obj and obj_type in {'MESH'}:

                       box = col.box().column(1)  

                       row = box.row(1)
                       row.prop(context.active_object.data, "show_double_sided", text="DoubleSide",icon="GHOST")   
                       row.prop(context.active_object.data, "use_auto_smooth", text="AutoSmooth",icon="AUTO")
                    
                       row = box.row(1)
                       row.active = context.active_object.data.use_auto_smooth
                       row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")   
                  
                       box.separator() 

                       box = col.box().column(1)  
                       
                       row = box.row(1)
                       row.label("Refresh Normals:")

                       row = box.column(1)               
                       row.operator("tp_ops.rec_normals", text="Recalculate Normals", icon="SNAP_NORMAL")   
                     
                       box.separator()



            else:

                row = box.row(1) 
                row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 

                box.separator() 

                box = col.box().column(1) 

                row = box.row(1)
                row.prop(context.active_object.data, "show_double_sided",icon="GHOST")     
                row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
            
                row = box.row(1)
                row.active = context.active_object.data.use_auto_smooth
                row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")  

                box.separator() 

 
                box = col.box().column(1)
                
                row = box.row(1)
                row.label("Refresh Normals:")

                row = box.column(1)               

                row.operator("mesh.flip_normals", text="Flip Normals", icon='FILE_REFRESH')                 
                row.operator("mesh.normals_make_consistent",text="Recalulate Normals", icon='SNAP_NORMAL')
                       
                box.separator()        
                
                row = box.row(1)
                row.operator("mesh.normals_make_consistent", text="Rec-Inside").inside = True        
                row.operator("mesh.normals_make_consistent", text="Rec-Outside").inside = False             
                       
                box.separator()

                row = box.row(1)
                row.operator("mesh.set_normals_from_faces", text="Set Normals from Faces")

                box.separator()
                
                

                box = col.box().column(1)  

                row = box.row(1)
                row.label("Show Normal Lines:")
                
                box.separator()   
                              
                row = box.row(1)
                row.prop(context.active_object.data, "show_normal_vertex", text="", icon='VERTEXSEL')
                row.prop(context.active_object.data, "show_normal_loop", text="", icon='LOOPSEL')
                row.prop(context.active_object.data, "show_normal_face", text="", icon='FACESEL')
                 
                row.active = context.active_object.data.show_normal_vertex or context.active_object.data.show_normal_face
                row.prop(context.scene.tool_settings, "normal_size", text="Size")  
                
                if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True): 

                    box.separator()  
                    box.separator()  
                         
                    row = box.column(1)
                    row.operator("mesh.select_similar",text="Select Similar Normals", icon='RESTRICT_SELECT_OFF').type='NORMAL'

                box.separator() 


        if context.mode == "EDIT_MESH":

            box = col.box().column(1) 
           
            if not tp_props.display_analsye_toggle:
                row = box.row(1)
                row.prop(tp_props, "display_analsye_toggle", text="", icon='TRIA_RIGHT')
                row.label(text="Mesh Analyse")
                row.prop(context.active_object.data, "show_statvis", text="", icon='OUTLINER_DATA_LAMP')
            
            else:
                row = box.row(1)                      
                row.prop(tp_props, "display_analsye_toggle", text="", icon='TRIA_DOWN')
                row.label(text="Mesh Analyse")
                row.prop(context.active_object.data, "show_statvis", text="", icon='OUTLINER_DATA_LAMP')

                
                box = col.box().column(1) 
                
                row = box.column(1)  
                
                mesh = context.active_object.data
                statvis = context.tool_settings.statvis
                row.active = mesh.show_statvis

                row.prop(statvis, "type")

                box.separator() 

                row = box.column(1) 
              
                statvis_type = statvis.type
              
                if statvis_type == 'OVERHANG':
                    
                    row = box.row(1)
                    row.prop(statvis, "overhang_min", text="")
                    row.prop(statvis, "overhang_max", text="")

                    box.separator() 
                    
                    row = box.row(1) 
                    row.prop(statvis, "overhang_axis", expand=True)
               
                elif statvis_type == 'THICKNESS':
                    
                    row = box.row(1)           
                    row.prop(statvis, "thickness_min", text="")
                    row.prop(statvis, "thickness_max", text="")
                    
                    box.separator() 

                    row = box.row(1)  
                    row.prop(statvis, "thickness_samples")
               
                elif statvis_type == 'INTERSECT':
                    pass
                
                elif statvis_type == 'DISTORT':
                   
                    row = box.row(1)
                    row.prop(statvis, "distort_min", text="")
                    row.prop(statvis, "distort_max", text="")
               
                elif statvis_type == 'SHARP':
                   
                    row = box.row(1)
                    row.prop(statvis, "sharp_min", text="")
                    row.prop(statvis, "sharp_max", text="")

                box.separator() 



        if context.mode == "OBJECT":
            
            box = col.box().column(1)  

            if not tp_props.display_export_toggle: 
                row = box.row(1)   
                row.prop(tp_props, "display_export_toggle", text="", icon="TRIA_RIGHT")                
                row.label("Mesh Export")
               
            
                row.operator("mesh.print3d_export", text="", icon='EXPORT')
            else:
                row = box.row(1)   
                row.prop(tp_props, "display_export_toggle", text="", icon="TRIA_RIGHT")                
                row.label("Mesh Export")   
                
                row.operator("mesh.print3d_export", text="", icon='EXPORT')

                box = col.box().column(1)

                row = box.row(1)
                row.label("Export Path:")
                row.prop(print_3d, "use_apply_transform", text="", icon='MAN_TRANS')
                row.prop(print_3d, "use_apply_scale", text="", icon='MAN_SCALE')
                row.prop(print_3d, "use_export_texture", text="", icon='FILE_IMAGE')

                row = box.row(1)
                row.prop(print_3d, "export_path", text="")

                row = box.row(1)
                row.prop(print_3d, "export_format", text="")
                row.operator("mesh.print3d_export", text="Export", icon='EXPORT')

                box.separator() 

        # OUTPUT #
        MeshCheckBar.draw_report(layout, context)




class VIEW3D_TP_MeshCheck_TOOLS(bpy.types.Panel, MeshCheckBar):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_MeshCheck_TOOLS"
    bl_label = "MeshCheck"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}
    

class VIEW3D_TP_MeshCheck_UI(bpy.types.Panel, MeshCheckBar):
    bl_idname = "VIEW3D_TP_MeshCheck_UI"
    bl_label = "MeshCheck"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_MeshCheck_PROPS(bpy.types.Panel, MeshCheckBar):
    bl_idname = "VIEW3D_TP_MeshCheck_PROPS"
    bl_label = "MeshCheck"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}
    



        