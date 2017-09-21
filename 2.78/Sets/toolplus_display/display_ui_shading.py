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


class VIEW3D_TP_3D_Shade_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Shade / UVs"
    bl_idname = "VIEW3D_TP_3D_Shade_Panel_TOOLS"
    bl_label = "Display"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

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

        draw_3d_shade_panel_layout(self, context, layout) 



class VIEW3D_TP_3D_Shade_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_3D_Shade_Panel_UI"
    bl_label = "Display"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

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

        draw_3d_shade_panel_layout(self, context, layout) 




def draw_3d_shade_panel_layout(self, context, layout):
    icons = load_icons()

    tp = context.window_manager.tp_collapse_menu_display  
            
    view = context.space_data
    scene = context.scene
    gs = scene.game_settings
    obj = context.object

    obj = context.active_object     
    if obj:
        obj_type = obj.type
                                                              
        if obj_type in {'ARMATURE', 'POSE','LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER'}:

            ob = context.object
            if ob: 

                box = layout.box().column(1)  
                
                row = box.row(1)
                row.prop(ob, "show_bounds", text="ShowBounds", icon='SNAP_PEEL_OBJECT') 
                row.prop(ob, "draw_bounds_type", text="")  

                box.separator() 
                
                row = box.row(1) 
                row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")                    
              


        elif obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:
 
            box = layout.box().column(1)  

            row = box.row(1)                                                          
            row.operator("tp_ops.wire_all", text="Wire all", icon='WIRE')
            
            obj = context.active_object
            if obj:
                active_wire = obj.show_wire 
                if active_wire == True:
                    row.operator("tp_ops.wire_off", "Wire Select", icon = 'MESH_PLANE')              
                else:                       
                    row.operator("tp_ops.wire_on", "Wire Select", icon = 'MESH_GRID')
            else:
                row.label("", icon="BLANK1")            
           
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


        elif obj_type in {'LAMP'}:  
                                               
              box = layout.box().column(1) 
              
              row = box.row(1)
              row.prop(context.object.data, "type", expand=True)
              
              box.separator() 
             
              if bpy.context.scene.render.engine == 'CYCLES':
                  lamp = context.object.data
                  clamp = context.object.data.cycles
                  cscene = context.scene.cycles

                  row = box.column(1)
                 
                  if context.object.data.type in {'POINT', 'SUN', 'SPOT'}:
                      row.prop(context.object.data, "shadow_soft_size", text="Size")
               
                  elif context.object.data.type == 'AREA':
                      row.prop(context.object.data, "shape", text="")


                      if context.object.data.shape == 'SQUARE':
                          row.prop(context.object.data, "size")
                    
                      elif context.object.data.shape == 'RECTANGLE':
                          row.prop(context.object.data, "size", text="Size X")
                          row.prop(context.object.data, "size_y", text="Size Y")

                  if not (context.object.data.type == 'AREA' and context.object.data.cycles.is_portal):
                      sub = box.column(1)
                     
                      if bpy.context.scene.cycles.progressive == 'BRANCHED_PATH':
                          sub.prop(context.object.data.cycles, "samples")
                      sub.prop(context.object.data.cycles, "max_bounces")


                  row = box.column(1)
                  row.active = not (context.object.data.type == 'AREA' and context.object.data.cycles.is_portal)
                  row.prop(context.object.data.cycles, "cast_shadow")
                  row.prop(context.object.data.cycles, "use_multiple_importance_sampling", text="Multiple Importance")

                  if context.object.data.type == 'AREA':
                      row.prop(context.object.data.cycles, "is_portal", text="Portal")

                  if context.object.data.type == 'HEMI':
                      row.label(text="Not supported, interpreted as sun lamp")
                  
                  box = layout.box().column(1)  

                  if not panel_node_draw(box, context.object.data, 'OUTPUT_LAMP', 'Surface'):
                                                       
                      row = box.column(1)
                      row.prop(context.object.data, "color")
                     
                  box.separator() 
                      
                  if context.object.data.type == 'SPOT':                          

                    box = layout.box().column(1)  
                     
                    row = box.row(1)
                    row.alignment = "CENTER"
                    row.label("Spot Shape", icon ="MESH_CONE")               
                     
                    row = box.row(1) 
                              
                    row = box.column(1)
                    row.prop(context.object.data, "spot_size", text="Size")
                    row.prop(context.object.data, "spot_blend", text="Blend", slider=True)

                    row.prop(context.object.data, "show_cone")


              else:
                  row = box.row(1)
                  row.prop(context.object.data, "color", text="")
                  row.prop(context.object.data, "energy")

                  if context.object.data.type in {'POINT', 'SPOT'}:

                      row = box.row(1)
                      row.prop(context.object.data, "falloff_type", text="")
                      row.prop(context.object.data, "distance")

                      if context.object.data.falloff_type == 'LINEAR_QUADRATIC_WEIGHTED':                   
                          row = box.row(1)
                          row.prop(context.object.data, "linear_attenuation", slider=True, text="Linear")
                          row.prop(context.object.data, "quadratic_attenuation", slider=True, text="Quadratic")

                      row = box.row(1)
                      row.prop(context.object.data, "use_sphere")

                  if context.object.data.type == 'AREA':
                      row = box.row(1)
                      row.prop(context.object.data, "distance")
                      row.prop(context.object.data, "gamma")                   


              box.separator()                         



        elif obj_type in {'CAMERA'}:  
            
            layout.operator_context = 'INVOKE_REGION_WIN'
            
            box = layout.box().column(1) 

            row = box.row(1)       
            row.operator("view3d.viewnumpad", text="Active Camera").type = 'CAMERA'  
            row.operator("view3d.object_as_camera", text="Set Camera")

            row = box.row(1)     
            row.operator("view3d.camera_to_view", text="Cam to View")
            row.operator("view3d.camera_to_view_selected", text="Cam to Selected")       
            
            box.separator()
                              
            row = box.row(1)
            row.prop(context.space_data, "camera", text="")
            row.prop(context.space_data, "lock_camera", text="Lock Cam")

         
            box = layout.box().column(1) 

            row = box.row(1)                         
            row.prop(context.object.data, "type", expand=True)
                                  
            row = box.row(1)              
            row.prop(context.object.data, "draw_size", text="Size")  
        
            box.separator()
                                  
            row = box.row(1) 
            if context.object.data.type == 'PERSP':
              
                if context.object.data.lens_unit == 'MILLIMETERS':
                    row.prop(context.object.data, "lens")
              
                elif context.object.data.lens_unit == 'FOV':
                    row.prop(context.object.data, "angle")
                    
                row.prop(context.object.data, "lens_unit", text="")

            elif context.object.data.type == 'ORTHO':
                row.prop(context.object.data, "ortho_scale")

            elif context.object.data.type == 'PANO':
                
                if  context.scene.render.engine == 'CYCLES':

                    row.prop(context.object.data.cycles, "panorama_type", text="Type")
                   
                    if context.object.data.cycles.panorama_type == 'FISHEYE_EQUIDISTANT':
                        row.prop(context.object.data.cycles, "fisheye_fov")
                   
                    elif context.object.data.cycles.panorama_type == 'FISHEYE_EQUISOLID':
                        
                        row = box.row()
                        row.prop(context.object.data.cycles, "fisheye_lens", text="Lens")
                        row.prop(context.object.data.cycles, "fisheye_fov")
                  
                    elif context.object.data.cycles.panorama_type == 'EQUIRECTANGULAR':
                    
                        row = box.row()
                      
                        sub = row.column(1)
                        sub.prop(context.object.data.cycles, "latitude_min")
                        sub.prop(context.object.data.cycles, "latitude_max")
                      
                        sub = row.column(1)
                        sub.prop(context.object.data.cycles, "longitude_min")
                        sub.prop(context.object.data.cycles, "longitude_max")
                
                elif context.scene.render.engine == 'BLENDER_RENDER':
                    row = box.row()
                 
                    if context.object.data.lens_unit == 'MILLIMETERS':
                        row.prop(context.object.data, "lens")
                 
                    elif context.object.data.lens_unit == 'FOV':
                        row.prop(context.object.data, "angle")
                  
                    row.prop(context.object.data, "lens_unit", text="")

            split = box.split()

            col = split.column(1)
            col.label(text="Shift:")
            col.prop(context.object.data, "shift_x", text="X")
            col.prop(context.object.data, "shift_y", text="Y")

            col = split.column(1)
            col.label(text="Clipping:")
            col.prop(context.object.data, "clip_start", text="Start")
            col.prop(context.object.data, "clip_end", text="End")
                                                    
            box = layout.box().column(1) 

            row = box.row(1)  
            row.menu("CAMERA_MT_presets", text=bpy.types.CAMERA_MT_presets.bl_label)
            row.operator("camera.preset_add", text="", icon='ZOOMIN')
            row.operator("camera.preset_add", text="", icon='ZOOMOUT').remove_active = True

            box.label(text="Sensor:")

            split = box.split()

            col = split.column(1)
            if context.object.data.sensor_fit == 'AUTO':
                col.prop(context.object.data, "sensor_width", text="Size")
            
            else:
                sub = col.column(1)
                sub.active = context.object.data.sensor_fit == 'HORIZONTAL'
                sub.prop(context.object.data, "sensor_width", text="Width")
                sub = col.column(1)
                sub.active = context.object.data.sensor_fit == 'VERTICAL'
                sub.prop(context.object.data, "sensor_height", text="Height")

            col = split.column(1)
            col.prop(context.object.data, "sensor_fit", text="")
  
            box.separator()                         
           
           
            box = layout.box().column(1)   

            row = box.column_flow(2)       
            row.prop(context.object.data, "show_guide", text="Composition guides")           
            row.prop(context.object.data, "show_limits", text="Limits")
            row.prop(context.object.data, "show_mist", text="Mist")
            row.prop(context.object.data, "show_sensor", text="Sensor")
            row.prop(context.object.data, "show_name", text="Name")      
            row.prop(context.object.data, "show_passepartout", text="Passepartout")                          
            row.prop(context.object.data, "passepartout_alpha", text="Alpha", slider=True)
   
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



        box = layout.box().column(1)
        
        row = box.row(1)

        if tp.display_overlay_pl:            
            row.prop(tp, "display_overlay_pl", text="Overlay", icon="LINK_AREA")
        else:
            row.prop(tp, "display_overlay_pl", text="Overlay", icon="LINK_AREA")    
            
        if tp.display_flymode_pl:            
            row.prop(tp, "display_flymode_pl", text="FlyMode", icon="MOD_SOFT")
        else:
            row.prop(tp, "display_flymode_pl", text="FlyMode", icon="MOD_SOFT")                            



        if tp.display_flymode_pl:   

            box = layout.box().column(1)      
                
            row = box.row()             
            row.alignment = 'CENTER'
            row.label("Fast HighRes Navigation") 
     
            box.separator()  
            
            row = box.row(1) 
            row.operator("view3d.fast_navigate_operator",'PLAY', icon = "PLAY")
            row.operator("view3d.fast_navigate_stop",'PAUSE', icon = "PAUSE")

            row = box.row(1)                   
            row.prop(context.scene,"OriginalMode", "")
            row.prop(context.scene,"FastMode", "")
            
            row = box.row(1)         
            row.prop(context.scene,"EditActive", "Edit mode")
            
            row = box.row(1)            
            row.prop(context.scene,"Delay")
            row.prop(scene,"DelayTimeGlobal")

            row = box.row(1)
            row.prop(context.scene,"ShowParticles")
            row.prop(context.scene,"ParticlesPercentageDisplay")                   
     
            box.separator()                         



        if tp.display_overlay_pl:    
          
            box = layout.box().column(1)    
            
            obj = context.active_object
            if obj:

                row = box.row(1)
                row.prop(context.object, "show_name", text="Name", icon ="OUTLINER_DATA_FONT")
                row.prop(context.object, "show_axis", text="Axis", icon ="OUTLINER_DATA_EMPTY") 
                
                box.separator() 
            else:
                pass


            if context.mode == "OBJECT":

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


        
        
               