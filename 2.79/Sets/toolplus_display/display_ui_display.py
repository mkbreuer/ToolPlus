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


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    

from bpy.types import Header, Menu, Panel
from bl_ui.properties_grease_pencil_common import (
        GreasePencilDataPanel,
        GreasePencilPaletteColorPanel,
        )
from bl_ui.properties_paint_common import UnifiedPaintPanel
from bpy.app.translations import contexts as i18n_contexts    


class draw_layout_display:

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode 


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator_context = 'INVOKE_AREA'

        icons = load_icons()

        tp_props = context.window_manager.tp_props_display  
        tp_fly = context.scene.display_props
                
        view = context.space_data
        scene = context.scene
        gs = scene.game_settings
        obj = context.object

        box = layout.box().column(1)
             
 
        obj = context.active_object     
        if obj:
            obj_type = obj.type
                                                                  
            if obj_type in {'ARMATURE', 'POSE','LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER'}:

                ob = context.object
                if ob: 

                    row = box.row(1)
                    row.prop(ob, "show_bounds", text="ShowBounds", icon='SNAP_PEEL_OBJECT') 
                    row.prop(ob, "draw_bounds_type", text="")  

                    box.separator() 
                    
                    row = box.row(1) 
                    row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")                    
                  
                    box.separator() 


            if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:
                             
                row = box.row(1)                                                          
                row.operator("tp_ops.wt_selection_handler_toggle", text="Wire Auto Toggle", icon='WIRE')

                box.separator()                                 
                
                row = box.row(1)                                                          
                row.operator("tp_ops.wire_all", text="Wire all", icon='WIRE')
                
                obj = context.active_object
                if obj:
                    active_wire = obj.show_wire 
                    if active_wire == True:
                        row.operator("tp_ops.edge_wire_off", "Wire Select", icon = 'MESH_PLANE')              
                    else:                       
                        row.operator("tp_ops.edge_wire_on", "Wire Select", icon = 'MESH_GRID')
                else:
                    row.label("", icon="BLANK1")            
               
                box.separator()  

                row = box.row(1)
                
                obj = context.active_object
                if obj:               
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text="Solid on", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="Solid off", icon='GHOST_ENABLED')        
                else:
                    row.label("", icon="BLANK1")  
             
                ob = context.object
                if ob: 
                    row.prop(ob, "draw_type", text="")                      
              
                    row = box.row(1)
                    row.prop(ob, "show_bounds", text="ShowBounds", icon='SNAP_PEEL_OBJECT') 
                    row.prop(ob, "draw_bounds_type", text="")    
               
                else:
                    row.label("", icon="BLANK1") 


                if context.mode == 'EDIT_MESH':          

                    box.separator()     
                    
                    row = box.row(1) 
                    row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")            
                    row.prop(context.space_data, "show_backface_culling", text="Backface", icon ="MOD_LATTICE")                      

                    row = box.row(1)         
                    row.prop(context.space_data, "use_occlude_geometry", text="Occlude", icon='ORTHO')    
                    if context.space_data.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
                        row.prop(context.space_data, "show_occlude_wire", text="Hidden", icon ="OUTLINER_DATA_LATTICE")      

                    box.separator()   
                    
                    box = layout.box().column(1)
                    
                    split = box.split()
                    col = split.column()
                    col.prop(context.active_object.data, "show_extra_edge_length", text="Edge Length")
                    col.prop(context.active_object.data, "show_extra_edge_angle", text="Edge Angle")
                    col = split.column()
                    col.prop(context.active_object.data, "show_extra_face_area", text="Face Area")
                    col.prop(context.active_object.data, "show_extra_face_angle", text="Face Angle")

                    box.separator()   

             
                if context.mode == 'OBJECT':

                    box.separator()  

                    row = box.row(1)          
                    row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")
                    
                    if obj:
                        obj_type = obj.type                    
                        if obj_type in {'MESH'}:   
                            row.prop(context.space_data, "show_backface_culling", text="Backface", icon ="MOD_LATTICE")  


                EDITM = ["EDIT_CURVE", "EDIT_SURFACE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]

                if context.mode in EDITM:

                    box.separator()  

                    row = box.row(1)          
                    row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")
     
     
     
            elif obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:   

                box.separator() 

                box = layout.box().column(1)
             
                row = box.row(1)                  
                row.label("Object Color")               
                row.operator("tp_ops.material_add", text="", icon='ZOOMIN')
                row.operator("tp_ops.remove_all_material", text="", icon="ZOOMOUT")
              
                if bpy.context.scene.render.engine == 'CYCLES':
                    if len(context.object.material_slots) > 0:                            
                        sub = row.row(1)
                        sub.scale_x = 0.5 
                        sub.prop(context.object.active_material, "diffuse_color", text="")  
                    else:
                        pass   
             
                else:
                    sub = row.row(1)
                    sub.scale_x = 0.5 
                    sub.prop(context.object, "color", text="")                     

                row.operator("tp_ops.purge_unused_material", text="", icon="PANEL_CLOSE")     

                box.separator() 
           


            elif obj_type in {'EMPTY', 'FORCE'}:  

                box = layout.box().column(1)   

                row = box.row(1)    

                ob = context.object
                row.prop(ob, "empty_draw_type", text="Display")

                box.separator()    
               
                row = box.row(1)               
                row.prop(ob, "empty_draw_size", text="Size")
        

           
            elif obj_type in {'LATTICE'}:  

                box = layout.box().column(1)   
                 
                row = box.row(1)     
                row.prop(context.object.data, "use_outside")
                row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

                box.separator()                       

                row = box.row(1)
                row.prop(context.object.data, "points_u", text="X")
                row.prop(context.object.data, "points_v", text="Y")
                row.prop(context.object.data, "points_w", text="Z")
             
                row = box.row(1)
                row.prop(context.object.data, "interpolation_type_u", text="")
                row.prop(context.object.data, "interpolation_type_v", text="")
                row.prop(context.object.data, "interpolation_type_w", text="")  

                box.separator()                       

                row = box.row(1)
                row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")
                
                row = box.row(1)          
                row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")    

                box.separator()                         

            box.separator()                    





        box = layout.box().column(1)

        row = box.row(1)

        if tp_props.display_overlay:            
            row.prop(tp_props, "display_overlay", text="Overlay", icon="LINK_AREA")
        else:
            row.prop(tp_props, "display_overlay", text="Overlay", icon="LINK_AREA")    
            
        if tp_props.display_flymode:            
            row.prop(tp_props, "display_flymode", text="FlyMode", icon="MOD_SOFT")
        else:
            row.prop(tp_props, "display_flymode", text="FlyMode", icon="MOD_SOFT")                            


        if tp_props.display_flymode:   

            box = layout.box().column(1)      
                
            row = box.row()             
            row.alignment = 'CENTER'
            row.label("Fast HighRes Navigation") 
     
            box.separator()  
            
            row = box.row(1) 
            row.operator("tp_ops.fast_navigate_operator",'Play', icon = "PLAY")
            row.operator("tp_ops.fast_navigate_stop",'Pause', icon = "PAUSE")

            row = box.row(1)                   
            row.prop(tp_fly,"OriginalMode", "")
            row.prop(tp_fly,"FastMode", "")

            box.separator() 
            
            row = box.row(1)         
            row.prop(tp_fly,"EditActive", "Edit mode")
            
            box.separator() 

            row = box.row(1)            
            row.prop(tp_fly,"Delay")
            row.prop(tp_fly,"DelayTimeGlobal")

            box.separator() 

            row = box.row(1)
            row.prop(tp_fly,"ShowParticles", "Particles")
            row.prop(tp_fly,"ParticlesPercentageDisplay")                   
         
            box.separator()  
            box.separator()                         


        if tp_props.display_overlay:    
          
            box = layout.box().column(1)    
            
            if context.mode == "OBJECT":
                
                obj = context.active_object
                if obj:            
                    
                    row = box.row(1)
                    row.prop(context.object, "show_name", text="Name", icon ="OUTLINER_DATA_FONT")
                    row.prop(context.object, "show_axis", text="Axis", icon ="OUTLINER_DATA_EMPTY") 
      
                    box.separator()
                else:
                    pass


                row = box.column(1)
                display_all = not context.space_data.show_only_render
                row.active = display_all
                row.prop(context.space_data, "show_outline_selected")
                row.prop(context.space_data, "show_all_objects_origin")
                row.prop(context.space_data, "show_relationship_lines")

                obj = context.active_object
                if obj:
                    obj_type = obj.type                         
             
                    if obj_type in {'MESH'}: 
                        row.prop(context.object, "show_transparent", text="Transparency") 
                               
                    if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:                           
                        row.prop(context.object, "show_texture_space", text="Texture Space")

                if view.viewport_shade == 'SOLID':
                    row.prop(view, "show_textured_solid")
           
            if context.mode == "EDIT_MESH":
                split = box.split()

                col = split.column()
                col.prop(context.active_object.data, "show_faces", text="Faces")
                col.prop(context.active_object.data, "show_edges", text="Edges")
                col.prop(context.active_object.data, "show_edge_crease", text="Creases")
               
                if bpy.app.build_options.freestyle:
                    col.prop(context.active_object.data, "show_edge_seams", text="Seams")

                col = split.column()

                if not bpy.app.build_options.freestyle:
                    col.prop(context.active_object.data, "show_edge_seams", text="Seams")
              
                col.prop(context.active_object.data, "show_edge_sharp", text="Sharp", text_ctxt=i18n_contexts.plural)
                col.prop(context.active_object.data, "show_edge_bevel_weight", text="Bevel")
              
                if bpy.app.build_options.freestyle:
                    col.prop(context.active_object.data, "show_freestyle_edge_marks", text="Edge Marks")
                    col.prop(context.active_object.data, "show_freestyle_face_marks", text="Face Marks")                           
                
                col = box.row(1)        
                col.prop(context.active_object.data, "show_weight")
            
            box.separator()     




class VIEW3D_TP_Display_Panel_TOOLS(bpy.types.Panel, draw_layout_display):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Display_Panel_TOOLS"
    bl_label = "Display"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_Display_Panel_UI(bpy.types.Panel, draw_layout_display):
    bl_idname = "VIEW3D_TP_Display_Panel_UI"
    bl_label = "Display"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
            
                   