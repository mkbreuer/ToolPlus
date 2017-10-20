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
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



def draw_add_curve_panel_layout(self, context, layout):

        icons = load_icons()

        my_button_one = icons.get("icon_image1")

        if context.mode == "OBJECT":


            box = layout.box().column(1)  
                 
            row = box.row(1) 
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1
            sub.menu("INFO_MT_mesh_add",text="",icon='OUTLINER_OB_MESH')              
            sub.menu("INFO_MT_curve_add",text="",icon='OUTLINER_OB_CURVE')
            sub.menu("INFO_MT_surface_add",text="",icon='OUTLINER_OB_SURFACE')
            sub.menu("INFO_MT_metaball_add",text="",icon="OUTLINER_OB_META")
            sub.operator("object.camera_add",icon='OUTLINER_OB_CAMERA',text="")   
            sub.menu("INFO_MT_armature_add",text="",icon="OUTLINER_OB_ARMATURE")
                      
            row = box.row(1)
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1
            sub.operator("object.empty_add",text="",icon="OUTLINER_OB_EMPTY")          
            sub.operator("object.add",text="",icon="OUTLINER_OB_LATTICE").type="LATTICE"
            sub.operator("object.text_add",text="",icon="OUTLINER_OB_FONT")
            sub.operator("object.lamp_add",icon='OUTLINER_OB_LAMP',text="")
            sub.operator("object.speaker_add",icon='OUTLINER_OB_SPEAKER',text="")
            sub.operator_menu_enum("object.effector_add", "type", text="",icon="SOLO_ON")    

            
            box = layout.box().column(1)   

            #row = box.row()
               
            #sub = row.row(1)
            #sub.scale_x = 0.35
            #sub.scale_y = 0.34
            #sub.template_icon_view(context.window_manager , "TP_Curves_Insert_Previews")            

           
            """ Add Curve """
            row = box.row(1)
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1
            sub.operator("curve.primitive_bezier_curve_add",icon='CURVE_BEZCURVE',text="")
            sub.operator("curve.primitive_bezier_circle_add",icon='CURVE_BEZCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_curve_add",icon='CURVE_NCURVE',text="")
            sub.operator("curve.primitive_nurbs_circle_add",icon='CURVE_NCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_path_add",icon='CURVE_PATH',text="")   


            """ Add Surface """    
            row = box.row(1)
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1
            sub.operator("surface.primitive_nurbs_surface_circle_add",icon='SURFACE_NCIRCLE',text="")
            sub.operator("surface.primitive_nurbs_surface_surface_add",icon='SURFACE_NSURFACE',text="")
            sub.operator("surface.primitive_nurbs_surface_cylinder_add",icon='SURFACE_NCYLINDER',text="")
            sub.operator("surface.primitive_nurbs_surface_sphere_add",icon='SURFACE_NSPHERE',text="")
            sub.operator("surface.primitive_nurbs_surface_torus_add",icon='SURFACE_NTORUS',text="")

      
                                    

            box = layout.box().column(1)                                                 

            row = box.row(1)
            row.label("2D Curves")

            row = box.row(1)
            row.operator("curve.simple", text="Point", icon_value=my_button_one.icon_id).Simple_Type="Point"
            row.operator("curve.simple", text="Line", icon_value=my_button_one.icon_id).Simple_Type="Line"
            
            row = box.row(1)
            row.operator("curve.simple", text="Distance", icon_value=my_button_one.icon_id).Simple_Type="Distance"        
            row.operator("curve.simple", text="Angle", icon_value=my_button_one.icon_id).Simple_Type="Angle"        

            row = box.row(1)        
            row.operator("curve.simple", text="Circle", icon_value=my_button_one.icon_id).Simple_Type="Circle"        
            row.operator("curve.simple", text="Ellipse", icon_value=my_button_one.icon_id).Simple_Type="Ellipse"

            row = box.row(1)
            row.operator("curve.simple", text="Arc", icon_value=my_button_one.icon_id).Simple_Type="Arc"       
            row.operator("curve.simple", text="Sector", icon_value=my_button_one.icon_id).Simple_Type="Sector"

            row = box.row(1)
            row.operator("curve.simple", text="Segment", icon_value=my_button_one.icon_id).Simple_Type="Segment"        
            row.operator("curve.simple", text="Rectangle", icon_value=my_button_one.icon_id).Simple_Type="Rectangle"

            row = box.row(1)
            row.operator("curve.simple", text="Rhomb", icon_value=my_button_one.icon_id).Simple_Type="Rhomb"
            row.operator("curve.simple", text="Polygon", icon_value=my_button_one.icon_id).Simple_Type="Polygon"

            row = box.row(1)
            row.operator("curve.simple", text="PolygonAB", icon_value=my_button_one.icon_id).Simple_Type="Polygon_ab"
            row.operator("curve.simple", text="Trapezoid", icon_value=my_button_one.icon_id).Simple_Type="Trapezoid"
          
            box.separator() 
          
            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'CURVE'}: 

                    row = box.column(1)                     
                    row.operator("curve.simplify", text="Simplify", icon_value=my_button_one.icon_id)              

                    box.separator() 



            box = layout.box().column(1)                         
           
            row = box.row(1)
            row.label("3D Curves")                    
           
            row = box.row(1)
            row.operator("mesh.curveaceous_galore", text="Galore", icon_value=my_button_one.icon_id)
            row.operator("curve.spirals", text="Spirals", icon_value=my_button_one.icon_id)

            row = box.row(1)
            row.operator("curve.curlycurve", text="Curly", icon_value=my_button_one.icon_id)
            row.operator("curve.formulacurves", text="Formula", icon_value=my_button_one.icon_id)

            row = box.row(1)
            row.operator("curve.wires", text="Wires", icon_value=my_button_one.icon_id)
            row.operator("curve.dial_scale", text="Dial/Scale", icon_value=my_button_one.icon_id)            
            
            row = box.row(1)     
            row.operator("mesh.primitive_pipe_add", text="Pipe", icon_value=my_button_one.icon_id)
            row.operator("object.pipe_nightmare", text="PipeTech", icon_value=my_button_one.icon_id)

            row = box.row(1)
            row.operator("curve.torus_knot_plus", text="Torus Knot", icon_value=my_button_one.icon_id)
            row.operator("mesh.add_braid", text="Braid Knot", icon_value=my_button_one.icon_id)

            box.separator() 
                    
            row = box.column(1)  
                       
            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'MESH'}:   
                      
                    row.operator("curve.celtic_links", text="Celtic Links", icon="FORCE_VORTEX")
                    row.operator("object.add_bounce_spline", icon="FORCE_HARMONIC")
                    row.operator("object.add_spirofit_spline", icon="FORCE_MAGNETIC")
            
            row.operator("object.add_catenary_curve", icon="FORCE_CURVE")
  
            box.separator() 


            box = layout.box().column(1)                         

            row = box.row(1)
            row.label("Plants")

            row = box.column(1)
            row.operator("curve.tree_add", text="Sapling Tree", icon_value=my_button_one.icon_id)       
                
            row = box.row(1)
            row.operator("mesh.add_iterative_tree", text="Iterative Tree", icon_value=my_button_one.icon_id)

            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'CURVE'}: 
                    
                    show = bpy.context.object.data.dimensions
                    if show == '3D':
                         
                        active_bevel = bpy.context.object.data.bevel_depth            
                        if active_bevel == 0.0:         
                           pass
                        else:
                          row = box.row(1)        
                          row.operator("mesh.addleaves", text="Iterative Leaves", icon_value=my_button_one.icon_id)    

            box.separator() 
         
            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'MESH'}:   
                    
                    row = box.column(1) 
                    row.operator("curve.ivy_gen", text="Ivy to Mesh", icon_value=my_button_one.icon_id).updateIvy = True
                    
                    box.separator() 



            box = layout.box().column(1)                         

            row = box.row(1)      
            row.label(text="Surfaces")

            row = box.row(1)        
            row.operator("object.add_surface_wedge", text="Wedge", icon_value=my_button_one.icon_id)
            row.operator("object.add_surface_cone", text="Cone", icon_value=my_button_one.icon_id)

            row = box.row(1)             
            row.operator("object.add_surface_star", text="Star", icon_value=my_button_one.icon_id)
            row.operator("object.add_surface_plane", text="Plane", icon_value=my_button_one.icon_id)
            
            box.separator() 

            box = layout.box().column(1) 

            row = box.row(1)      
            row.label(text="Text / Mesh")

            row = box.row(1)              
            row.operator("object.name_objects", text="Name",icon="OUTLINER_DATA_FONT")
            row.operator("object.vertices_numbers3d", text="VertNumb",icon="MESH_DATA")
        
            row = box.row(1)               
            row.operator("mesh.primitive_tube_add", text="Tupe", icon_value=my_button_one.icon_id)  
    
            box.separator() 

            if context.selected_objects:
                if context.selected_objects[0].type == 'MESH':
                    
                    row = box.column(1)                    
                    row.operator("object.connect2objects", text="Connect 2 Mesh",icon="MESH_DATA")
                    row.prop(bpy.context.scene, "shift_verts", text="shift")
                    row.prop(bpy.context.scene, "hook_or_not", text="hook new vertices?")

                    box.separator()


        if context.mode == "EDIT_MESH":

            box = layout.box().column(1)                         

            row = box.row(1)    
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.7  
            sub.operator("mesh.primitive_plane_add",icon='MESH_PLANE',text="")
            sub.operator("mesh.primitive_cube_add",icon='MESH_CUBE',text="")
            sub.operator("mesh.primitive_circle_add",icon='MESH_CIRCLE',text="")
            sub.operator("mesh.primitive_uv_sphere_add",icon='MESH_UVSPHERE',text="")
            sub.operator("mesh.primitive_ico_sphere_add",icon='MESH_ICOSPHERE',text="")        
                             
            row = box.row(1)   
            row.alignment = 'CENTER'                        

            sub = row.row(1)
            sub.scale_x = 1.7  
            sub.operator("mesh.primitive_cylinder_add",icon='MESH_CYLINDER',text="")
            sub.operator("mesh.primitive_torus_add",icon='MESH_TORUS',text="")
            sub.operator("mesh.primitive_cone_add",icon='MESH_CONE',text="")
            sub.operator("mesh.primitive_grid_add",icon='MESH_GRID',text="")
            sub.operator("mesh.primitive_monkey_add",icon='MESH_MONKEY',text="") 

            box.separator() 

            row = box.row(1)             
            row.operator("mesh.add_curvebased_tube", text="Tube between 2 Faces", icon_value=my_button_one.icon_id)    

      
        if context.mode =='EDIT_CURVE':

            box = layout.box().column(1)  
            row = box.row(1)         
            row.alignment = 'CENTER'               

            sub = row.row(1)
            sub.scale_x = 1.2      
            sub.operator("curve.primitive_bezier_curve_add",icon='CURVE_BEZCURVE',text="")
            sub.operator("curve.primitive_bezier_circle_add",icon='CURVE_BEZCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_curve_add",icon='CURVE_NCURVE',text="")
            sub.operator("curve.primitive_nurbs_circle_add",icon='CURVE_NCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_path_add",icon='CURVE_PATH',text="")  
            sub.operator("curve.draw", icon='LINE_DATA',text="")
         
            box.separator() 
            
            row = box.row(1) 
            row.operator("curve.simplify", text="Simplify Curves", icon_value=my_button_one.icon_id)


        if context.mode == 'EDIT_SURFACE':
             
            box = layout.box()
            row = box.row(1) 
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.2   

            sub.operator("surface.primitive_nurbs_surface_curve_add",icon='SURFACE_NCURVE',text="") 
            sub.operator("surface.primitive_nurbs_surface_circle_add",icon='SURFACE_NCIRCLE',text="")
            sub.operator("surface.primitive_nurbs_surface_surface_add",icon='SURFACE_NSURFACE',text="")
            sub.operator("surface.primitive_nurbs_surface_cylinder_add",icon='SURFACE_NCYLINDER',text="")
            sub.operator("surface.primitive_nurbs_surface_sphere_add",icon='SURFACE_NSPHERE',text="")
            sub.operator("surface.primitive_nurbs_surface_torus_add",icon='SURFACE_NTORUS',text="")   

            
            
class VIEW3D_TP_Add_Curve_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Add_Curve_Panel_TOOLS"
    bl_label = "Add"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_add_curve_panel_layout(self, context, layout) 



class VIEW3D_TP_Add_Curve_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Add_Curve_Panel_UI"
    bl_label = "Add"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_add_curve_panel_layout(self, context, layout) 





