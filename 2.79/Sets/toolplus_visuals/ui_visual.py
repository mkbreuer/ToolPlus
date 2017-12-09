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


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons


types_category = [("tp_v0"   ," "   ,""   ,"COLLAPSEMENU"          ,0),
                  ("tp_v1"   ," "   ,""   ,"SPLITSCREEN"           ,1), 
                  ("tp_v2"   ," "   ,""   ,"WORLD"                 ,2),
                  ("tp_v3"   ," "   ,""   ,"MATERIAL_DATA"         ,3),
                  ("tp_v4"   ," "   ,""   ,"MESH_UVSPHERE"         ,4),
                  ("tp_v5"   ," "   ,""   ,"SMOOTH"                ,5),
                  ("tp_v6"   ," "   ,""   ,"SNAP_NORMAL"           ,6)]

bpy.types.Scene.tp_visual_category = bpy.props.EnumProperty(name = " ", default = "tp_v0", items = types_category)


def draw_visual_layout(self, context, layout):
        tp_props = context.window_manager.tp_props_visual            
        tp_display = context.scene.display_props      
        tp_orphan = context.scene.orphan_props      
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        view = context.space_data
        scene = context.scene
        gs = scene.game_settings
        obj = context.object

        col = layout.column(align=True)


        box = col.box().column(1)
        
        row = box.row(1)  
        row.prop(context.scene, 'tp_visual_category',  emboss = False, expand = True) #icon_only=True,
  
        if scene.tp_visual_category == "tp_v0": 
            pass

        if scene.tp_visual_category == "tp_v1": 

            wm = context.window_manager 
            view = context.space_data
            ob = context.object  
            obj = context.object
            scene = context.scene
            scn = context.scene
            rs = bpy.context.scene 
            gs = scene.game_settings

            box = col.box().column(1)

            box.separator() 

            row = box.row(1)  
            row.operator_context = 'INVOKE_REGION_WIN'  
            row.operator("wm.window_fullscreen_toggle", text = "Full Screen", icon = "FULLSCREEN_ENTER")    
            row.operator("screen.screen_full_area", text = "Full Area", icon = "GO_LEFT")    
           
            row = box.row(1) 
            row.operator("wm.window_duplicate", text="Dupli View", icon = "SCREEN_BACK")
            row.operator("screen.region_quadview", text="Quad View", icon = "SPLITSCREEN")
            
            if context.space_data.region_quadviews:
            
                row.operator_context = 'INVOKE_REGION_WIN'
            
                box.separator()        
              
                row = box.row(1)          
                region = context.space_data.region_quadviews[2]
                row.prop(region, "lock_rotation")
                sub = row.row(1)        
                sub.enabled = region.lock_rotation
                sub.prop(region, "show_sync_view")
                sub1 = row.row(1)  
                sub1.enabled = region.lock_rotation and region.show_sync_view
                sub1.prop(region, "use_box_clip")
 
            box.separator() 
           
            row = box.row(1) 
         
            if tp_props.display_lens:            
                row.prop(tp_props, "display_lens", text="Clip/Lens", icon="CHECKBOX_HLT")
            else:
                row.prop(tp_props, "display_lens", text="Clip/Lens", icon="CHECKBOX_DEHLT")   

            if tp_props.display_navi:            
                row.prop(tp_props, "display_navi", text="Navigation", icon="CHECKBOX_HLT")
            else:
                row.prop(tp_props, "display_navi", text="Navigation", icon="CHECKBOX_DEHLT")    

            box.separator()

                            
            if tp_props.display_lens: 
                
                box = col.box().column(1)  

                row = box.column(1)
                row.prop(context.space_data, "lens")

                box.separator() 
                
                row = box.column(1)
                row.prop(context.space_data, "clip_start", text="ClipStart")
                row.prop(context.space_data, "clip_end", text="ClipEnd")

                box.separator() 
         
            if tp_props.display_navi: 

                box = col.box().column(1) 

                row = box.row(1)
                row.alignment = 'CENTER'     
                row.operator("view3d.viewnumpad", text=" ", icon='CAMERA_DATA').type = 'CAMERA'
                row.operator("view3d.view_selected", text=" ", icon='ZOOM_SELECTED')
                row.operator("view3d.view_center_cursor", text=" ", icon='FORCE_FORCE')        
                row.operator("view3d.view_all", text=" ", icon='MANIPUL').center = True

                box.separator() 
             
                row = box.row(1) 

                box = row.box()

                box.label(text='Pan:')
                rowr = box.row(1)
                rowr.operator('opr.pan_up_view1', text='', icon='TRIA_DOWN')
                rowr.operator('opr.pan_down_view1', text='', icon='TRIA_UP')

                rowr = box.row(1)
                rowr.operator('opr.pan_right_view1', text='', icon='BACK')
                rowr.operator('opr.pan_left_view1', text='', icon='FORWARD')

                rowr = box.row(1)
                rowr.label(text='Zoom:')
                
                rowr = box.row(1)
                rowr.operator('opr.zoom_in_view1', text='', icon='ZOOMIN')
                rowr.operator('opr.zoom_out_view1', text='', icon='ZOOMOUT')

                box.separator()   

                rowr = box.row(1)

                rowr = box.row()

                box = row.box()
                box.label(text='Orbit:')

                rowr = box.row(1)
                rowr.operator('opr.orbit_up_view1', text='', icon='TRIA_DOWN')
                rowr.operator('opr.orbit_down_view1', text='', icon='TRIA_UP')  

                rowr = box.row(1)
                rowr.operator('opr.orbit_right_view1', text='', icon='BACK')
                rowr.operator('opr.orbit_left_view1', text='', icon='FORWARD')

                rowr = box.row(1)
                rowr.label(text='Roll:')
                
                rowr = box.row(1)
                rowr.operator('opr.roll_left_view1', text='', icon='ZOOMIN')
                rowr.operator('opr.roll_right_view1', text='', icon='ZOOMOUT')

                box.separator()                 
             
                rowr = box.row(1)

                rowr = box.row()

                box = row.box()
                box.label(text='View:')
                
                rowr = box.column(1)        
                rowr.operator("view3d.viewnumpad", text="Front").type='FRONT'
                rowr.operator("view3d.viewnumpad", text="Back").type='BACK'
                rowr.operator("view3d.viewnumpad", text="Left").type='LEFT'
                rowr.operator("view3d.viewnumpad", text="Right").type='RIGHT'
                rowr.operator("view3d.viewnumpad", text="Top").type='TOP'
                rowr.operator("view3d.viewnumpad", text="Bottom").type='BOTTOM'

                box.separator()                      
                
                box = col.box().column(1)   
                
                box.separator() 

                row = box.row(1)  
                row.operator("view3d.localview", text="Global/Local", icon='WORLD')
                row.operator("view3d.view_persportho", text="Persp/Ortho", icon='VIEW3D')             

                box.separator()                             

                row = box.column(1)
                row.prop(context.space_data, "lock_object", text="View to:")

                box.separator() 
             
                         
            box = col.box().column(1)     

            row = box.row(1)           
            row.label("", icon ="MESH_ICOSPHERE")
            row.label("Simplify")
            
            row.label("")
            
            if bpy.context.scene.render.use_simplify == True:
                row.prop(context.scene.render, "use_simplify", text="", icon='TRIA_UP_BAR')    
            else:
                row.prop(context.scene.render, "use_simplify", text="", icon='TRIA_DOWN_BAR')                                   
                           
            box.separator()
            
            if bpy.context.scene.render.use_simplify == True:

                rd = context.scene.render   
                             
                if bpy.context.scene.render.engine == 'CYCLES':

                    box.active = context.scene.render.use_simplify
     
                    row = box.column(1) 
                    row.label(text="Viewport:")
                    row.prop(context.scene.render, "simplify_subdivision", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles", text="Child Particles")

                    box.separator()

                    row = box.column(1) 
                    row.label(text="Render:")

                    row.prop(context.scene.render, "simplify_subdivision_render", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles_render", text="Child Particles")

                    col = box.column()
                    col.prop(context.scene.cycles, "use_camera_cull")
                   
                    subsub = col.column()
                    subsub.active = context.scene.cycles.use_camera_cull
                    subsub.prop(context.scene.cycles, "camera_cull_margin")

                else:

                    box.active = context.scene.render.use_simplify

                    row = box.column(1) 
                    row.label(text="Viewport:")
                    row.prop(context.scene.render, "simplify_subdivision", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles", text="Child Particles")

                    box.separator()

                    row = box.column(1) 
                    row.label(text="Render:")
                    row.prop(context.scene.render, "simplify_subdivision_render", text="Subdivision")
                    row.prop(context.scene.render, "simplify_child_particles_render", text="Child Particles")
                    row.prop(context.scene.render, "simplify_shadow_samples", text="Shadow Samples")
                    row.prop(context.scene.render, "simplify_ao_sss", text="AO and SSS")                
                    row.prop(context.scene.render, "use_simplify_triangulate")    

                box.separator()
           
            
            box = col.box().column(1)     
                
            row = box.row(1)
            row.label("", icon ="MOD_SOFT")             
            row.label("FastNavi") 

            row.label("")

            if tp_props.display_fastnav:            
                row.prop(tp_props, "display_fastnav", text="", icon="TRIA_UP_BAR")
            else:
                row.prop(tp_props, "display_fastnav", text="", icon="TRIA_DOWN_BAR")   

            box.separator()  
            
            row = box.row(1) 
            row.operator("tp_ops.fast_navigate_operator",'Play', icon = "PLAY")
            row.operator("tp_ops.fast_navigate_stop",'Pause', icon = "PAUSE")

            if tp_props.display_fastnav: 

                row = box.row(1)                   
                row.prop(tp_display,"OriginalMode", "")
                row.prop(tp_display,"FastMode", "")

                box.separator() 
                
                row = box.row(1)         
                row.prop(tp_display,"EditActive", "Edit mode")
                
                box.separator() 

                row = box.row(1)            
                row.prop(tp_display,"Delay")
                row.prop(tp_display,"DelayTimeGlobal")

                box.separator() 

                row = box.row(1)
                row.prop(tp_display,"ShowParticles", "Particles")
                row.prop(tp_display,"ParticlesPercentageDisplay")                   
         
            box.separator()  



        if scene.tp_visual_category == "tp_v2": 
            
            box = col.box().column(1) 
            
            box.separator()   

            row = box.row(1)
            row.alignment = 'CENTER'           

            button_matcap = icons.get("icon_matcap")
            row.operator("tp_ops.toggle_silhouette", text="",icon_value=button_matcap.icon_id)      
            
            row.prop(bpy.context.space_data, 'viewport_shade', text='', expand=True)

            box.separator()   
            box.separator()   

            row = box.row()
            row.prop(context.space_data, "show_only_render", text="Render") 

            row = box.row()
            row.prop(context.space_data, "show_world", "World")# ,icon ="WORLD")

            if context.space_data.show_world:        
           
                if tp_props.display_world_set:            
                    row.prop(tp_props, "display_world_set", text="", icon="TRIA_UP_BAR")
                else:
                    row.prop(tp_props, "display_world_set", text="", icon="TRIA_DOWN_BAR")    

                sub = row.row(1)
                sub.scale_x = 0.1 
                sub.prop(context.scene.world, "horizon_color", "")
                               
                box.separator() 

                if tp_props.display_world_set:         

                    row = box.column(1)
                    row.label("Lamp Settings")  
                    row.prop(context.scene.world, "exposure")
                    row.prop(context.scene.world, "color_range")
                    #row.prop(context.scene.world, "horizon_color", "")

                    box.separator()

            col = box.column()
            if view.viewport_shade == 'SOLID':
                
                col = box.row()
                col.prop(view, "use_matcap")
                if view.use_matcap:
                    sub = col.row(1)
                    sub.scale_y = 0.2
                    sub.scale_x = 1
                    sub.template_icon_view(context.space_data, "matcap_icon")
                    
                    box.separator()

            fx_settings = view.fx_settings
            if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:

                col = box.row()
                col.prop(context.space_data.fx_settings, "use_ssao", text="Ambient Occlusion")
                
                if context.space_data.fx_settings.use_ssao:

                    if tp_props.display_aoccl:            
                        col.prop(tp_props, "display_aoccl", text="", icon="TRIA_UP_BAR")
                    else:  
                        col.prop(tp_props, "display_aoccl", text="", icon="TRIA_DOWN_BAR")    

                    sub = col.row(1)
                    sub.scale_x = 0.1           
                    sub.prop(context.space_data.fx_settings.ssao, "color","")
                
                    if tp_props.display_aoccl:

                        box.separator()
                        
                        col = box.column(1)
                        col.prop(context.space_data.fx_settings.ssao, "factor")
                        col.prop(context.space_data.fx_settings.ssao, "distance_max")
                        col.prop(context.space_data.fx_settings.ssao, "attenuation")
                        col.prop(context.space_data.fx_settings.ssao, "samples")
                        #col.prop(context.space_data.fx_settings.ssao, "color","")               
                    
                    box.separator()

            row = box.row()
            if view.viewport_shade == 'SOLID':
                row.prop(view, "show_textured_solid")
                
            if view.viewport_shade == 'TEXTURED' or context.mode == 'PAINT_TEXTURE':
                if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                    row.prop(view, "show_textured_shadeless")
                    
            if not scene.render.use_shading_nodes:
                row = box.row()
                row.prop(gs, "material_mode", text="")
            
            box.separator()                     
            
            col = layout.column(align=True)           
            box = col.box().column(1) 

            row = box.row(1)              
            row.prop(context.space_data, "show_floor", text="", icon ="GRID")  
            row.label("Grid Floor")  
            
            row.label(" ")
            
            if tp_props.display_grid:            
                row.prop(tp_props, "display_grid", text="", icon="TRIA_UP_BAR")
            else:
                row.prop(tp_props, "display_grid", text="", icon="TRIA_DOWN_BAR") 
           
            box.separator()  
         
            if tp_props.display_grid: 
                                
                row = box.row(1)                 

                sub = row.row(1)
                sub.alignment = 'CENTER'
                sub.scale_x = 0.5
                sub.prop(context.space_data, "show_axis_x", text="X", toggle=True)
                sub.prop(context.space_data, "show_axis_y", text="Y", toggle=True)
                sub.prop(context.space_data, "show_axis_z", text="Z", toggle=True)

                box.separator() 
               
                row = box.column(1)
                row.prop(context.space_data, "grid_lines", text="Lines")
                row.prop(context.space_data, "grid_scale", text="Scale")
                row.prop(context.space_data, "grid_subdivisions", text="Subdivisions")
               
                box.separator() 

                                    
            col = layout.column(align=True)
            box = col.box().column(1)  

            row = box.row(1)              
            row.label("", icon='LAMP_SPOT')  
            row.label("OpenGL")  

            row.label(" ")             
  
            p = context.scene.opengl_lights_properties
            if context.scene.opengl_lights_properties == True:
                row.prop(p, "edit", "", icon = "TRIA_UP_BAR")
            else:
                row.prop(p, "edit", "", icon = "TRIA_DOWN_BAR")


            box.separator()                

            row = box.row(1)  
            row.menu("VIEW3D_MT_opengl_lights_presets", text=bpy.types.VIEW3D_MT_opengl_lights_presets.bl_label, icon = "COLLAPSEMENU")
            row.operator("scene.opengl_lights_preset_add", text="", icon='ZOOMIN')
            row.operator("scene.opengl_lights_preset_add", text="", icon='ZOOMOUT').remove_active = True      
                         
            system = bpy.context.user_preferences.system
            
            def opengl_lamp_buttons(column, lamp):
               
                split = column.split(percentage=0.1)
                split.prop(lamp, "use", text="", icon='OUTLINER_OB_LAMP' if lamp.use else 'LAMP_DATA')
                
                col = split.column()
                col.active = lamp.use
                
                row = col.row()
                row.label(text="Diffuse:")
                row.prop(lamp, "diffuse_color", text="")
                
                row = col.row()
                row.label(text="Specular:")
                row.prop(lamp, "specular_color", text="")
                
                col = split.column()           
                col.active = lamp.use
                col.prop(lamp, "direction", text="")
            
            
            if(p.edit):
                box.separator()   
                
                box = col.box().column(1)  
                
                column = box.column()
                
                split = column.split(percentage=0.1)
                split.label()
                split.label(text="Colors:")
                split.label(text="Direction:")
                
                lamp = system.solid_lights[0]
                opengl_lamp_buttons(column, lamp)
                
                lamp = system.solid_lights[1]
                opengl_lamp_buttons(column, lamp)
                
                lamp = system.solid_lights[2]
                opengl_lamp_buttons(column, lamp)


            box.separator() 


        if scene.tp_visual_category == "tp_v3": 
                 
            box = col.box().column(1)  

            box.separator() 

            row = box.row(1)                                 
            row.operator("tp_ops.material_one","Add", icon="MESH_UVSPHERE")                                                                                  
            sub = row.row(1)
            sub.scale_x = 0.5   
            sub.prop(context.window_manager, 'col_mat_surface') 
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


                    row = box.row(1)
                    row.prop(tp_props,"index_count_sw")
                    
                    sub = row.row(1)
                    sub.scale_x = 0.5                    
                    sub.prop(tp_props,"new_swatch", text="")
                    row.operator('tp_mat.set_colors', text='Replace', icon="COLOR")

                    box.separator()         


            box.separator() 

            box = col.box().column(1)

            row = box.row(1)  
            row.label(text="More Materials...")                     
            
            if tp_props.display_more_mat:            
                row.prop(tp_props, "display_more_mat", text="", icon="TRIA_UP_BAR")                   
            else:
                row.prop(tp_props, "display_more_mat", text="", icon="TRIA_DOWN_BAR")    
                     
            if tp_props.display_more_mat:   
                                      
                box.separator()                 
                              
                row = box.row(1)    
                row.operator("tp_ops.material_wire","WireMat")                                                                                                           
                row.prop(context.window_manager, 'col_material_surface') 
                row.prop(context.window_manager, 'col_material_wire')                                       

                box.separator()      
                  
                obj = context.active_object     
                if obj:              
 
                    if len(context.object.material_slots) > 0:


                        box = col.box().column(1)                    

                        row = box.row(1)                                  
                        row.label("Color Contrast")   

                        row = box.row(1)
                        row.prop(tp_props, "index_count")       
                        row.prop(tp_props, "mat_switch", text="")      
                       
                        button_switch = icons.get("icon_switch")
                        row.operator('tp_mat.set_color_constrast', text='', icon_value=button_switch.icon_id).mat_mode = 'INVERT'
                        row.operator('tp_mat.set_color_constrast', text='', icon="COLOR")

                        box.separator()   


                        obj = context.active_object     
                        if obj:

                            box = col.box().column(1)  
                            
                            box.separator()
                            
                            row = box.row(1)                                  
                            row.label("Obj-Color")            
                            if bpy.context.scene.render.engine == 'CYCLES':
                                row.prop(context.object.active_material, "diffuse_color", text="")  
                            else: 
                                row.prop(context.object, "color", text="")                     
                            
                            active_objcolor = bpy.context.object.active_material.use_object_color
                            if active_objcolor == True:
                                row.prop(context.object.active_material, "use_object_color", text="", icon = 'OUTLINER_OB_LAMP')              
                            else:                       
                                row.prop(context.object.active_material, "use_object_color", text="", icon = 'OUTLINER_DATA_LAMP')  
                                                
                            box.separator()  

                        else:
                            pass            

                        box = col.box().column(1) 
                         
                        box.separator()
                        
                        row = box.row(1) 
                        scene = context.scene
                        rd = scene.render
                        rl = rd.layers.active
                        row.label("Override")
                        row.prop(rl, "material_override", text="")

                        box.separator()              



        if scene.tp_visual_category == "tp_v4": 

            obj = context.active_object     
            if obj:
                obj_type = obj.type
                                                                      
                if obj_type in {'ARMATURE', 'POSE','LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER'}:

                    ob = context.object
                    if ob: 

                        box = col.box().column(1) 
                        
                        box.separator() 
                        
                        row = box.row(1)
                        row.prop(ob, "show_bounds", text="ShowBounds", icon='SNAP_PEEL_OBJECT') 
                        row.prop(ob, "draw_bounds_type", text="")  

                        box.separator() 
                        
                        row = box.row(1) 
                        row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")                    
                      
                        box.separator() 


                if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:


                    box = col.box().column(1)
                    
                    box.separator() 
                    
                    row = box.row(1)                                                          
                    row.operator("tp_ops.wt_selection_handler_toggle", text="Wire Auto Toggle", icon='WIRE')

                    box.separator()


                    row = box.row(1)                                                          
                    row.operator("tp_ops.edge_wire_all", text="Wire all", icon='WIRE')
                    
                    obj = context.active_object
                    if obj:
                        active_wire = obj.show_wire 
                        if active_wire == True:
                            row.operator("tp_ops.edge_wire_off", "Wire off", icon = 'MESH_PLANE')              
                        else:                       
                            row.operator("tp_ops.edge_wire_on", "Wire on", icon = 'MESH_GRID')
                    else:
                        row.label("", icon="BLANK1")            
                   
                    box.separator() 


                    box = col.box().column(1)
                    
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
                        row.prop(ob, "show_bounds", text="Bounds", icon='SNAP_PEEL_OBJECT') 
                        row.prop(ob, "draw_bounds_type", text="")    
                   
                    else:
                        row.label("", icon="BLANK1") 


                    if context.mode == 'EDIT_MESH':          
                        
                        box.separator()   
                                                
                        box = col.box().column(1)

                        row = box.row(1) 
                        row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")            
                        row.prop(context.space_data, "show_backface_culling", text="Backface", icon ="MOD_LATTICE")                      

                        row = box.row(1)         
                        row.prop(context.space_data, "use_occlude_geometry", text="Occlude", icon='ORTHO')    
                        if context.space_data.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
                            row.prop(context.space_data, "show_occlude_wire", text="Hidden", icon ="OUTLINER_DATA_LATTICE")      

                        box.separator()   
                                                
                        
                        box = col.box().column(1)
                        
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

                        box.separator()                         
                        
                        
                        box = col.box().column(1) 
                        
                        row = box.row(1)  
                        row.label(text="More Overlays...")                     
                        
                        if tp_props.display_more:            
                            row.prop(tp_props, "display_more", text="", icon="TRIA_UP_BAR")                   
                        else:
                            row.prop(tp_props, "display_more", text="", icon="TRIA_DOWN_BAR")    
                                                       
                            box.separator()
                        
                        if tp_props.display_more: 
                              
                            box.separator()
                         
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


                    EDITM = ["EDIT_CURVE", "EDIT_SURFACE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]

                    if context.mode in EDITM:

                        box.separator()  

                        row = box.row(1)          
                        row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")
         


                elif obj_type in {'EMPTY', 'FORCE'}:  

                    box = col.box().column(1)  

                    box.separator() 
                    
                    row = box.row(1)    

                    ob = context.object
                    row.prop(ob, "empty_draw_type", text="Display")

                    box.separator()    
                   
                    row = box.row(1)               
                    row.prop(ob, "empty_draw_size", text="Size")                
               

                elif obj_type in {'LATTICE'}:  

                    box = layout.box().column(1)   
                    
                    box.separator() 
                    
                    row = box.row(1)          
                    row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")    

                    box.separator()                         

            else:
                pass


        if scene.tp_visual_category == "tp_v5": 

            if context.mode == 'OBJECT': 
                
                
                box = col.box().column(1) 
                
                box.separator() 
                                    
                row = box.row(1)  
                row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
           
                box.separator() 
                
                obj = context.active_object     
                if obj:
                   obj_type = obj.type
                                  
                   if obj and obj_type in {'MESH'}:
                                             
                       box = col.box().column(1)  
                       
                       box.separator()
                       
                       row = box.row(1)  
                       row.prop(context.active_object.data, "show_double_sided", text="DoubleSide",icon="GHOST")   
                       row.prop(context.active_object.data, "use_auto_smooth", text="AutoSmooth",icon="AUTO")
                       
                       row = box.row(1)                         
                       row.active = context.active_object.data.use_auto_smooth
                       row.prop(context.active_object.data, "auto_smooth_angle", text="AutoSmooth Angle")   
                  
                       box.separator() 

                   else:
                        pass                            

                box.separator() 


            else:
                                       
                if context.mode == 'EDIT_MESH':          
                    
                    box = col.box().column(1) 

                    box.separator() 

                    row = box.row(1) 
                    row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                    row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 

                    box.separator() 
                    
                    
                    box = col.box().column(1) 
                  
                    box.separator() 
                    
                    row = box.row(1)  
                    row.prop(context.active_object.data, "show_double_sided", text="DoubleSide",icon="GHOST")  
                    row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                
                    row = box.row(1)
                    row.active = context.active_object.data.use_auto_smooth
                    row.prop(context.active_object.data, "auto_smooth_angle", text="AutoSmooth Angle")  

                    box.separator() 
                    
                    
                    box = col.box().column(1) 

                    row = box.row(1) 
                    row.operator("mesh.mark_sharp", text="SharpVerts", icon='SNAP_VERTEX').use_verts = True          
                    props = row.operator("mesh.mark_sharp", text="", icon='X')
                    props.use_verts = True
                    props.clear = True
                    
                    row = box.row(1)  
                    row.operator("mesh.mark_sharp", text="SharpEdges", icon='SNAP_EDGE')
                    row.operator("mesh.mark_sharp", text="", icon='X').clear = True

                    box.separator()   

                else:
                    
                    box = col.box().column(1) 
            
                    box.separator() 
                                        
                    row = box.row(1)  
                    row.operator("tp_ops.curve_shade", text="Flat", icon="MESH_CIRCLE").shade_mode='flat'
                    row.operator("tp_ops.curve_shade", text="Smooth", icon="SMOOTH").shade_mode='smooth'  
               
                    box.separator()             

                

        if scene.tp_visual_category == "tp_v6": 

            if context.mode == 'OBJECT': 

                box = col.box().column(1)  

                box.separator() 

                row = box.column(1)  
                row.operator("object.hide_view_clear", text="Show Hidden", icon="VISIBLE_IPO_ON")   
                row.operator("object.hide_view_set", text="Hide Selected", icon="VISIBLE_IPO_OFF").unselected=False   
                row.operator("object.hide_view_set", text="Hide Unselected", icon="VISIBLE_IPO_OFF").unselected=True   
             
                box.separator()

                
                box = col.box().column(1)  

                row = box.column(1)  

                button_remove_doubles = icons.get("icon_remove_doubles")
                row.operator("tp_ops.remove_doubles", text="Remove Doubles",icon_value=button_remove_doubles.icon_id)                 
                row.operator("tp_ops.rec_normals", text="Recalculate Normals", icon="SNAP_NORMAL")   

                row.separator()                 
                
                row.operator("tp_ops.calculate_weighted_normals", text="Calc. Weighted Normals", icon="BLANK1") 
                row.operator("tp_ops.editnormals_transfer", text="Transfer Vertex Normals", icon="BLANK1")     
             
                box.separator()

                box = col.box().column(1)  

                row = box.row(1)               
                row.prop(tp_orphan, "mod_list")
                row.operator("tp_ops.delete_data_obs","Purge", icon ="GHOST_DISABLED")            
             
                box.separator()


            if context.mode == 'EDIT_MESH':  

                box = col.box().column(1)  

                box.separator() 

                row = box.column(1)
               
                button_flip = icons.get("icon_flip")
                row.operator("mesh.flip_normals", text="Flip Normals", icon_value=button_flip.icon_id)  
               
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



            if context.mode == 'EDIT_CURVE':
                
                
                box = col.box().column(1)  

                box.separator()   

                box = col.box().column(1)  
                
                row = box.column(1)
                row.operator("curve.normals_make_consistent",text="Recalculate Normals", icon='SNAP_NORMAL')        

                box.separator() 
                
                
                
                box = col.box().column(1)  
                
                row = box.row(1)   
                row.prop(context.object.data, "show_handles", text="Handles", icon='IPO_BEZIER')
                row.prop(context.object.data, "show_normal_face", text="Normals", icon='SNAP_NORMAL')
               
                if context.object.data.show_normal_face == True:  

                    row = box.column(1)
                    row.prop(context.scene.tool_settings, "normal_size", text="Size")                                   

                box.separator()   


            if context.mode == 'EDIT_SURFACE':
                                
                box = col.box().column(1)  
              
                box.separator() 
                
                row = box.column(1)                
                row.operator("curve.cyclic_toggle")
                row.operator("curve.switch_direction")
               
                box.separator()            