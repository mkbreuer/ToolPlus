import bpy
from bpy import *
from bpy.props import *
from .icons.icons import load_icons


from toolplus_bounding.layouts.normal_ui import draw_normal_layout
from toolplus_bounding.layouts.smooth_ui import draw_smooth_layout
from toolplus_bounding.layouts.screen_ui import draw_screen_layout


types_two = [("tp_v0"    ,"  NoN"       ,""   ,"COLLAPSEMENU"          ,0),
             ("tp_v1"    ,"  Screen"   ,""    ,"FULLSCREEN_ENTER"      ,1), 
             ("tp_v2"    ,"  Select"    ,""   ,"RESTRICT_SELECT_OFF"   ,2),
             ("tp_v3"    ,"  Display"   ,""   ,"ZOOM_SELECTED"         ,3),
             ("tp_v4"    ,"  Smooth"    ,""   ,"SNAP_NORMAL"           ,4),
             ("tp_v5"    ,"  Screen"   ,""    ,"BORDERMOVE"            ,5),
             ("tp_v6"    ,"  Material"  ,""   ,"MATERIAL_DATA"         ,6),
             ("tp_v7"    ,"  World"     ,""   ,"WORLD"                 ,7)]



types_one = [("tp_v0"   ," "   ,""   ,"COLLAPSEMENU"          ,0),
             ("tp_v1"   ," "   ,""   ,"SPLITSCREEN"           ,1), 
             ("tp_v2"   ," "   ,""   ,"WORLD"                 ,2),
             ("tp_v3"   ," "   ,""   ,"MATERIAL_DATA"         ,3),
             ("tp_v4"   ," "   ,""   ,"MESH_UVSPHERE"         ,4),
             ("tp_v5"   ," "   ,""   ,"SMOOTH"                ,5),
             ("tp_v6"   ," "   ,""   ,"SNAP_NORMAL"           ,6)]



bpy.types.Scene.tp_points = bpy.props.EnumProperty(name = " ", default = "tp_v0", items = types_one)



def draw_visual_layout(context, layout):
        tp_props = context.window_manager.bbox_window          
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        view = context.space_data
        scene = context.scene
        gs = scene.game_settings
        obj = context.object

        col = layout.column(align=True)


        box = col.box().column(1)
        
        row = box.row(1)  
        row.prop(context.scene, 'tp_points',  emboss = False, expand = True) #icon_only=True,
 
 
        if scene.tp_points == "tp_v0": 
            pass


        if scene.tp_points == "tp_v1": 
            draw_screen_layout(context, layout) 



        if scene.tp_points == "tp_v2": 

            box = col.box().column(1) 

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
                    
                    box.separator()            

                    row = box.column(1)
                    row.label("Lamp Settings")  
                    row.prop(context.scene.world, "exposure")
                    row.prop(context.scene.world, "color_range")
                    row.prop(context.scene.world, "horizon_color", "")

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
                        col.prop(context.space_data.fx_settings.ssao, "color","")               
                    
                    box.separator()


            row = box.row()
            if view.viewport_shade == 'SOLID':
                row.prop(view, "show_textured_solid")
                
            if view.viewport_shade == 'TEXTURED' or context.mode == 'PAINT_TEXTURE':
                if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                    row.prop(view, "show_textured_shadeless")

            if not scene.render.use_shading_nodes:
                sub = row.row(1)
                sub.scale_x = 0.5
                sub.prop(gs, "material_mode", text="")
            

            box.separator()

            row = box.row()
            row.prop(context.space_data, "show_floor", text="Grid Floor")#, icon ="GRID")  

            if context.space_data.show_floor:  

                if tp_props.display_grid:            
                    row.prop(tp_props, "display_grid", text="", icon="TRIA_UP_BAR")
                else:
                    row.prop(tp_props, "display_grid", text="", icon="TRIA_DOWN_BAR")    

            sub = row.row(1)
            sub.scale_x = 0.157
            sub.prop(context.space_data, "show_axis_x", text="X", toggle=True)
            sub.prop(context.space_data, "show_axis_y", text="Y", toggle=True)
            sub.prop(context.space_data, "show_axis_z", text="Z", toggle=True)

            box.separator() 
         
            if tp_props.display_grid: 
                
                box.separator() 
               
                row = box.column(1)
                row.prop(context.space_data, "grid_lines", text="Lines")
                row.prop(context.space_data, "grid_scale", text="Scale")
                row.prop(context.space_data, "grid_subdivisions", text="Subdivisions")
               
                box.separator() 



            col = layout.column(align=True)
            
            box = col.box().column(1)  

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
            
            row = box.row(1) 
            p = context.scene.opengl_lights_properties
            row.prop(p, "edit", "edit opengl light", icon = "LIGHTPAINT")
            
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


        if scene.tp_points == "tp_v3": 
                 
            box = col.box().column(1)  
          
            row = box.row(1)  
            row.operator("tp_ops.material_add", text="Add", icon='ZOOMIN')
            row.menu("tp_ops.material_list", text="MatList", icon="COLLAPSEMENU") 

            row = box.row(1) 
            row.operator("tp_ops.remove_all_material", text="Del.", icon="ZOOMOUT")  
            row.operator("tp_ops.purge_unused_material", text="Purge", icon="PANEL_CLOSE")                  
       
            box.separator()              
            box.separator()              
          
            obj = context.active_object     
            if obj:
                row = box.row(1)                  
                row.label("Object Color")               
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(context.object.active_material, "diffuse_color", text="")  
                else: 
                    row.prop(context.object, "color", text="")                     

            else:
                pass

            box.separator()              
        
            row = box.row(1) 
            scene = context.scene
            rd = scene.render
            rl = rd.layers.active
            row.prop(rl, "material_override", text="Override")

            box.separator()              


        if scene.tp_points == "tp_v4": 

            obj = context.active_object     
            if obj:
                obj_type = obj.type
                                                                      
                if obj_type in {'ARMATURE', 'POSE','LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER'}:

                    ob = context.object
                    if ob: 

                        box = col.box().column(1) 
                        
                        row = box.row(1)
                        row.prop(ob, "show_bounds", text="ShowBounds", icon='SNAP_PEEL_OBJECT') 
                        row.prop(ob, "draw_bounds_type", text="")  

                        box.separator() 
                        
                        row = box.row(1) 
                        row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")                    
                      
                        box.separator() 


                if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:
         
                    box = col.box().column(1)

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


                        display_more = context.user_preferences.addons[__package__].preferences.tab_display_advance
                        if display_more == 'on': 

                            box = layout.box().column(1)   
                       
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

                    row = box.row(1)    

                    ob = context.object
                    row.prop(ob, "empty_draw_type", text="Display")

                    box.separator()    
                   
                    row = box.row(1)               
                    row.prop(ob, "empty_draw_size", text="Size")                
               


                elif obj_type in {'LATTICE'}:  

                    box = layout.box().column(1)   

                    row = box.row(1)          
                    row.prop(context.object, "show_x_ray", text="X-Ray", icon ="META_CUBE")    

                    box.separator()                         



            else:
                pass


        if scene.tp_points == "tp_v5": 
            draw_smooth_layout(context, layout)
            

        if scene.tp_points == "tp_v6": 
            draw_normal_layout(context, layout)             


       