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

def draw_insert_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_curve        
      
        icons = load_icons()

        my_button_one = icons.get("icon_image1")

        col = layout.column(1)  
       
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences
      
        if context.mode == "OBJECT":


            if context.user_preferences.addons[addon_key].preferences.curve_primitiv == True:

                box = col.box().column(1)  
                
                box.separator() 
                                 
                row = box.row(1) 
                row.alignment = 'CENTER'               
                sub = row.row(1)
                sub.scale_x = 1.2
                sub.scale_y = 1.2
                sub.menu("INFO_MT_mesh_add",text="",icon='OUTLINER_OB_MESH')              
                sub.menu("INFO_MT_curve_add",text="",icon='OUTLINER_OB_CURVE')
                sub.menu("INFO_MT_surface_add",text="",icon='OUTLINER_OB_SURFACE')
                sub.menu("INFO_MT_metaball_add",text="",icon="OUTLINER_OB_META")
                sub.operator("object.camera_add",icon='OUTLINER_OB_CAMERA',text="")   
                sub.menu("INFO_MT_armature_add",text="",icon="OUTLINER_OB_ARMATURE")
                          
                row = box.row(1)
                row.alignment = 'CENTER'               
                sub = row.row(1)
                sub.scale_x = 1.2
                sub.scale_y = 1.2
                sub.operator("object.empty_add",text="",icon="OUTLINER_OB_EMPTY")          
                sub.operator("object.add",text="",icon="OUTLINER_OB_LATTICE").type="LATTICE"
                sub.operator("object.text_add",text="",icon="OUTLINER_OB_FONT")
                sub.operator("object.lamp_add",icon='OUTLINER_OB_LAMP',text="")
                sub.operator("object.speaker_add",icon='OUTLINER_OB_SPEAKER',text="")
                sub.operator_menu_enum("object.effector_add", "type", text="",icon="SOLO_ON")    
                
                box.separator() 

             
            box = col.box().column(1)   
            
            box.separator() 
           
            """ Add Curve """
            row = box.row(1)
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.2
            sub.scale_y = 1.2
            sub.operator("curve.primitive_bezier_curve_add",icon='CURVE_BEZCURVE',text="")
            sub.operator("curve.primitive_bezier_circle_add",icon='CURVE_BEZCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_curve_add",icon='CURVE_NCURVE',text="")
            sub.operator("curve.primitive_nurbs_circle_add",icon='CURVE_NCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_path_add",icon='CURVE_PATH',text="")   


            """ Add Surface """    
            row = box.row(1)
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.2
            sub.scale_y = 1.2
            sub.operator("surface.primitive_nurbs_surface_circle_add",icon='SURFACE_NCIRCLE',text="")
            sub.operator("surface.primitive_nurbs_surface_surface_add",icon='SURFACE_NSURFACE',text="")
            sub.operator("surface.primitive_nurbs_surface_cylinder_add",icon='SURFACE_NCYLINDER',text="")
            sub.operator("surface.primitive_nurbs_surface_sphere_add",icon='SURFACE_NSPHERE',text="")
            sub.operator("surface.primitive_nurbs_surface_torus_add",icon='SURFACE_NTORUS',text="")
            
            box.separator()  
            box.separator()  
      
            row = box.row(1)
            row.scale_y = 1.2
            if tp_props.display_curve_2d:            
                row.prop(tp_props, "display_curve_2d", text="2D", icon="TRIA_DOWN")
            else:
                row.prop(tp_props, "display_curve_2d", text="2D", icon="TRIA_RIGHT")    
                                            
            if tp_props.display_curve_2d:   
                
                box.separator()                                                
                box.separator()                                                

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.simple", text="Point").Simple_Type="Point"
                row.operator("curve.simple", text="Line").Simple_Type="Line"
                
                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.simple", text="Distance").Simple_Type="Distance"        
                row.operator("curve.simple", text="Angle").Simple_Type="Angle"        

                row = box.row(1)        
                row.scale_y = 1.2
                row.operator("curve.simple", text="Circle").Simple_Type="Circle"        
                row.operator("curve.simple", text="Ellipse").Simple_Type="Ellipse"

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.simple", text="Arc").Simple_Type="Arc"       
                row.operator("curve.simple", text="Sector").Simple_Type="Sector"

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.simple", text="Segment").Simple_Type="Segment"        
                row.operator("curve.simple", text="Rectangle").Simple_Type="Rectangle"

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.simple", text="Rhomb").Simple_Type="Rhomb"
                row.operator("curve.simple", text="Polygon").Simple_Type="Polygon"

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.simple", text="PolygonAB").Simple_Type="Polygon_ab"
                row.operator("curve.simple", text="Trapezoid").Simple_Type="Trapezoid"
                            
                obj = context.active_object
                if obj:
                    obj_type = obj.type                
                    if obj.type in {'CURVE'}: 
                        
                        box.separator() 

                        row = box.column(1)
                        row.scale_y = 1.2                     
                        row.operator("curve.simplify", text="Simplify")              

                box.separator() 
                box.separator() 
                box = col.box().column(1) 
 
 
            
            row = box.row(1)
            row.scale_y = 1.2
            if tp_props.display_curve_3d:            
                row.prop(tp_props, "display_curve_3d", text="3D", icon="TRIA_DOWN")
            else:
                row.prop(tp_props, "display_curve_3d", text="3D", icon="TRIA_RIGHT")    
                                            
            if tp_props.display_curve_3d:                       

                box.separator()         
                box.separator()         
               
                row = box.row(1)
                row.scale_y = 1.2
                row.operator("mesh.curveaceous_galore", text="Galore")
                row.operator("curve.spirals", text="Spirals")

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.curlycurve", text="Curly")
                row.operator("curve.formulacurves", text="Formula")

                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.wires", text="Wires")
                row.operator("curve.dial_scale", text="Dial/Scale")            
                
                
                row = box.row(1)     
                row.scale_y = 1.2                
                row.operator("object.pipe_nightmare", text="PipeTech")
                sub = row.row(1)
                sub.scale_x = 0.5
                sub.scale_y = 1.2                
                sub.operator("mesh.primitive_pipe_add", text="Pipe")
                button_baply = icons.get("icon_baply")     
                sub.operator("mesh.convert_pipe_to_mesh", text=" ", icon_value=button_baply.icon_id)               
             
#                row = box.row(1)     
#                row.scale_y = 1.2    
#                row.operator("mesh.primitive_tube_add", text="Tupe")   
 
                                           
                box.separator() 
                box.separator() 
                box = col.box().column(1)    
                                     

            row = box.row(1)
            row.scale_y = 1.2   
            if tp_props.display_curve_plants:            
                row.prop(tp_props, "display_curve_plants", text="Plants", icon="TRIA_DOWN")
            else:
                row.prop(tp_props, "display_curve_plants", text="Plants", icon="TRIA_RIGHT")    
                                            
            if tp_props.display_curve_plants:  

                box.separator() 
                box.separator() 

                row = box.column(1) 
                row.scale_y = 1.2
                row.operator("curve.tree_add", text="Sapling Tree")       
                row.operator("mesh.add_iterative_tree", text="Iterative Tree")
                
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
                              row.operator("mesh.addleaves", text="Iterative Leaves")    

           
                    if obj.type in {'MESH'}:   
                        
                        row.operator("curve.ivy_gen", text="Ivy to Mesh").updateIvy = True
                        
                box.separator() 
                box.separator() 
                box = col.box().column(1)    
                                                       

           
            row = box.row(1)
            row.scale_y = 1.2   
            if tp_props.display_curve_knots:            
                row.prop(tp_props, "display_curve_knots", text="Knots", icon="TRIA_DOWN")
            else:
                row.prop(tp_props, "display_curve_knots", text="Knots", icon="TRIA_RIGHT")    
                                            
            if tp_props.display_curve_knots:  
                
                box.separator()
                box.separator()
               
                row = box.row(1)
                row.scale_y = 1.2
                row.operator("curve.torus_knot_plus", text="Torus Knot")
                row.operator("mesh.add_braid", text="Braid Knot")
                                        
                row = box.row(1)  
                row.scale_y = 1.2   

                obj = context.active_object
                if obj:
                    obj_type = obj.type                
                    if obj.type in {'MESH'}:                           
                                               
                        row.operator("curve.celtic_links", text="Celtic")
                        row.operator("object.add_bounce_spline", text="Bounce")
                        
                        row = box.row(1)
                        row.scale_y = 1.2     
                        row.operator("object.add_spirofit_spline")
                
                row.operator("object.add_catenary_curve")
      
                box.separator() 
                box.separator() 
                box = col.box().column(1)    


            row = box.row(1)
            row.scale_y = 1.2   
            if tp_props.display_curve_more:            
                row.prop(tp_props, "display_curve_more", text="Various", icon="TRIA_DOWN")
            else:
                row.prop(tp_props, "display_curve_more", text="Various", icon="TRIA_RIGHT")    
                                            
            if tp_props.display_curve_more:                       

                box.separator()  
                box.separator()  

                row = box.row(1)      
                row.label(text="Surfaces")

                row = box.row(1)        
                row.scale_y = 1.2
                row.operator("object.add_surface_wedge", text="Wedge")
                row.operator("object.add_surface_cone", text="Cone")

                row = box.row(1)             
                row.scale_y = 1.2
                row.operator("object.add_surface_star", text="Star")
                row.operator("object.add_surface_plane", text="Plane")
                
                box.separator() 
                box.separator() 

                row = box.row(1)      
                row.label(text="Text / Mesh")

                row = box.row(1)              
                row.scale_y = 1.2
                row.operator("object.name_objects", text="Name")
                row.operator("object.vertices_numbers3d", text="VertNumb")
        
                box.separator() 

                if context.selected_objects:
                    if context.selected_objects[0].type == 'MESH':
                        
                        row = box.column(1)                    
                        row.scale_y = 1.2
                        row.operator("object.connect2objects", text="Connect 2 Mesh")
                        row.prop(bpy.context.scene, "shift_verts", text="shift")
                        row.prop(bpy.context.scene, "hook_or_not", text="hook new vertices?")

                box.separator() 
                box.separator() 
                box = col.box().column(1)   



            row = box.row(1)
            row.scale_y = 1.2   
            if tp_props.display_curve_material:            
                row.prop(tp_props, "display_curve_material", text="Material", icon="TRIA_DOWN")
            else:
                row.prop(tp_props, "display_curve_material", text="Material", icon="TRIA_RIGHT")    
                                            
            if tp_props.display_curve_material:                       

                box.separator()  
              
                box = col.box().column(1)  

                box.separator() 

                row = box.row(1)                                                                                                                                  
                row.operator("tp_ops.material_color","", icon="MATERIAL")                                                                                  
                row.menu("tp_ops.material_list", text="List", icon="COLLAPSEMENU")    

                obj = context.active_object     
                if obj:          
                    if len(context.object.material_slots) > 0:

                        #row = box.row(1)                                           
                        #row.template_ID(context.object, "active_material", new="material.new")
                        row.menu("MATERIAL_MT_specials", icon='DOWNARROW_HLT', text="")        
                        
                        box.separator()   
                                                
                        row = box.row()                
                        row.template_list("MATERIAL_UL_matslots", "", context.object, "material_slots", context.object, "active_material_index", rows=4)             
                       
                        split = row.split(1)
                        row = split.column(1)
                        row.operator("object.material_slot_add", icon='ZOOMIN', text="")
                        row.operator("tp_ops.remove_all_material", text="", icon="ZOOMOUT")   
                        row.operator("object.material_slot_move", icon='TRIA_UP', text="").direction = 'UP'
                        row.operator("object.material_slot_move", icon='TRIA_DOWN', text="").direction = 'DOWN'             
                        row.operator("tp_ops.purge_unused_material", text="", icon="PANEL_CLOSE")      

            box.separator()
            box.separator()



        if context.mode == "EDIT_MESH":

            box = col.box().column(1)                         
            
            box.separator() 
            
            row = box.row(1)    
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.2  
            sub.scale_y = 1.2
            sub.operator("mesh.primitive_plane_add",icon='MESH_PLANE',text="")
            sub.operator("mesh.primitive_cube_add",icon='MESH_CUBE',text="")
            sub.operator("mesh.primitive_circle_add",icon='MESH_CIRCLE',text="")
            sub.operator("mesh.primitive_uv_sphere_add",icon='MESH_UVSPHERE',text="")
            sub.operator("mesh.primitive_ico_sphere_add",icon='MESH_ICOSPHERE',text="")        
                             
            row = box.row(1)   
            row.alignment = 'CENTER'                        

            sub = row.row(1)
            sub.scale_x = 1.2 
            sub.scale_y = 1.2
            sub.operator("mesh.primitive_cylinder_add",icon='MESH_CYLINDER',text="")
            sub.operator("mesh.primitive_torus_add",icon='MESH_TORUS',text="")
            sub.operator("mesh.primitive_cone_add",icon='MESH_CONE',text="")
            sub.operator("mesh.primitive_grid_add",icon='MESH_GRID',text="")
            sub.operator("mesh.primitive_monkey_add",icon='MESH_MONKEY',text="") 

            box.separator() 
            box.separator() 

            row = box.column(1) 
            row.operator("tp_ops.edgetubes", text="Tube to Edges")                          
            row.operator("tp_ops.2facetube", text="Tube between 2 Faces")    
            
            box.separator() 

      
        if context.mode =='EDIT_CURVE':

            box = col.box().column(1)  
            
            box.separator() 

            row = box.row(1)         
            row.alignment = 'CENTER'               

            sub = row.row(1)
            sub.scale_x = 1.2      
            sub.scale_y = 1.2
            sub.operator("curve.primitive_bezier_curve_add",icon='CURVE_BEZCURVE',text="")
            sub.operator("curve.primitive_bezier_circle_add",icon='CURVE_BEZCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_curve_add",icon='CURVE_NCURVE',text="")
            sub.operator("curve.primitive_nurbs_circle_add",icon='CURVE_NCIRCLE',text="")
            sub.operator("curve.primitive_nurbs_path_add",icon='CURVE_PATH',text="")  
            sub.operator("curve.draw", icon='LINE_DATA',text="")
         
            box.separator() 
            
            row = box.row(1) 
            row.operator("curve.simplify", text="Simplify Curve", icon="BLANK1")
            
            box.separator() 
            
        if context.mode == 'EDIT_SURFACE':
             
            box = col.box().column(1) 
            
            box.separator() 

            row = box.row(1) 
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.2   
            sub.scale_y = 1.2
            sub.operator("surface.primitive_nurbs_surface_curve_add",icon='SURFACE_NCURVE',text="") 
            sub.operator("surface.primitive_nurbs_surface_circle_add",icon='SURFACE_NCIRCLE',text="")
            sub.operator("surface.primitive_nurbs_surface_surface_add",icon='SURFACE_NSURFACE',text="")
            sub.operator("surface.primitive_nurbs_surface_cylinder_add",icon='SURFACE_NCYLINDER',text="")
            sub.operator("surface.primitive_nurbs_surface_sphere_add",icon='SURFACE_NSPHERE',text="")
            sub.operator("surface.primitive_nurbs_surface_torus_add",icon='SURFACE_NTORUS',text="")   
            
            box.separator() 
            

            
class VIEW3D_TP_Curve_Insert_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_Insert_Panel_TOOLS"
    bl_label = "Insert"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_insert_ui(self, context, layout) 



class VIEW3D_TP_Curve_Insert_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_Insert_Panel_UI"
    bl_label = "Insert"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_insert_ui(self, context, layout) 





