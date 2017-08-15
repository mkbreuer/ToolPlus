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



def draw_display_compact_panel_layout(self, context, layout):
        tp = context.window_manager.tp_collapse_menu_display       
        icons = load_icons()
  
        wm = context.window_manager 
        view = context.space_data
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 
        gs = scene.game_settings

        Display_Title = context.user_preferences.addons[__package__].preferences.tab_title
        if Display_Title == 'on':

            obj = context.active_object     
            if obj:
               obj_type = obj.type
               
               box = layout.box().column(1)
               row = box.row(1)                                        
               row.alignment = "CENTER"
                              
               if obj_type in {'MESH'}:                                   
                   row.label("MESH") 
                                      
               if obj_type in {'LATTICE'}:                                     
                   row.label("LATTICE") 

               if obj_type in {'CURVE'}:                                       
                   row.label("CURVE")               
                   
               if obj_type in {'SURFACE'}:                                       
                   row.label("SURFACE")                 
                   
               if obj_type in {'META'}:                                      
                   row.label("MBall")                 
                   
               if obj_type in {'FONT'}:                                       
                   row.label("FONT")  
                                                  
               if obj_type in {'ARMATURE'}:                                        
                   row.label("ARMATURE") 

               if obj_type in {'EMPTY'}:
                   row.label("EMPTY") 

               if obj_type in {'CAMERA'}:
                  row.label("CAMERA") 

               if obj_type in {'LAMP'}:
                   row.label("LAMP") 

               if obj_type in {'SPEAKER'}:
                   row.label("SPEAKER") 

        Display_World = context.user_preferences.addons[__package__].preferences.tab_world
        if Display_World == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tp.display_world:            
                row.prop(tp, "display_world", text="", icon="WORLD")
                row.label("Shade")                
            else:
                row.prop(tp, "display_world", text="", icon="WORLD")                
                row.label("Shade")

                row.prop(context.space_data, "show_only_render", text="", icon ="RESTRICT_RENDER_OFF")    
                row.operator("tp_ops.toggle_silhouette", text="", icon ="MATCAP_08")               
                row.prop(context.space_data, "use_matcap", text="", icon ="MATCAP_01") 
                row.prop(context.space_data.fx_settings, "use_ssao", text="", icon="GROUP")

   
            if tp.display_world:                                                  
               
                box.separator()           
             
                row = box.row(1)
                row.alignment = 'CENTER'           
                row.operator("tp_ops.toggle_silhouette", text="", icon ="MATCAP_08")      
                row.prop(bpy.context.space_data, 'viewport_shade', text='', expand=True)

                box.separator()   

                row = box.row()
                row.prop(context.space_data, "show_world", "World")# ,icon ="WORLD")

                if context.space_data.show_world:        
               
                    if tp.display_world_set:            
                        row.prop(tp, "display_world_set", text="", icon="TRIA_UP_BAR")
                    else:
                        row.prop(tp, "display_world_set", text="", icon="TRIA_DOWN_BAR")    

                    sub = row.row(1)
                    sub.scale_x = 0.1 
                    sub.prop(context.scene.world, "horizon_color", "")
                                   
                    box.separator() 

                    if tp.display_world_set: 
                        
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

                        if tp.display_aoccl:            
                            col.prop(tp, "display_aoccl", text="", icon="TRIA_UP_BAR")
                        else:  
                            col.prop(tp, "display_aoccl", text="", icon="TRIA_DOWN_BAR")    

                        sub = col.row(1)
                        sub.scale_x = 0.1           
                        sub.prop(context.space_data.fx_settings.ssao, "color","")
                    
                        if tp.display_aoccl:

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

                    if tp.display_grid:            
                        row.prop(tp, "display_grid", text="", icon="TRIA_UP_BAR")
                    else:
                        row.prop(tp, "display_grid", text="", icon="TRIA_DOWN_BAR")    

                sub = row.row(1)
                sub.scale_x = 0.157
                sub.prop(context.space_data, "show_axis_x", text="X", toggle=True)
                sub.prop(context.space_data, "show_axis_y", text="Y", toggle=True)
                sub.prop(context.space_data, "show_axis_z", text="Z", toggle=True)

                box.separator() 
             
                if tp.display_grid: 
                    
                    box.separator() 
                   
                    row = box.column(1)
                    row.prop(context.space_data, "grid_lines", text="Lines")
                    row.prop(context.space_data, "grid_scale", text="Scale")
                    row.prop(context.space_data, "grid_subdivisions", text="Subdivisions")
                   
                    box.separator() 



                box = layout.box().column(1)   

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
                    
                    box = layout.box().column(1)  
                    
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


               

        Display_View = context.user_preferences.addons[__package__].preferences.tab_view
        if Display_View == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tp.display_view:            
                row.prop(tp, "display_view", text="", icon="VIEW3D")
                row.label("Screen")
            else:
                row.prop(tp, "display_view", text="", icon="VIEW3D")                
                row.label("Screen")
               
                row.operator("wm.window_fullscreen_toggle", text = "", icon = "FULLSCREEN_ENTER")                
                row.operator("screen.screen_full_area", text = "", icon = "GO_LEFT")   
                row.operator("wm.window_duplicate", text="", icon = "SCREEN_BACK")
                row.operator("screen.region_quadview", text="", icon = "SPLITSCREEN")


            if tp.display_view:  
                          
                box.separator() 
                
                row = box.row(1)  
                row.operator_context = 'INVOKE_REGION_WIN'  
                row.operator("wm.window_fullscreen_toggle", text = "Full Screen", icon = "FULLSCREEN_ENTER")    
                row.operator("screen.screen_full_area", text = "Full Area", icon = "GO_LEFT")    
               
                row = box.row(1) 
                row.operator("wm.window_duplicate", text="Dupli View", icon = "SCREEN_BACK")
                row.operator("screen.region_quadview", text="Quad View", icon = "SPLITSCREEN")

                row = box.row(1) 
             
                if tp.display_lens:            
                    row.prop(tp, "display_lens", text="Clip/Lens", icon="CHECKBOX_HLT")
                else:
                    row.prop(tp, "display_lens", text="Clip/Lens", icon="CHECKBOX_DEHLT")   

                if tp.display_navi:            
                    row.prop(tp, "display_navi", text="Navigation", icon="CHECKBOX_HLT")
                else:
                    row.prop(tp, "display_navi", text="Navigation", icon="CHECKBOX_DEHLT")    


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

                
                if tp.display_lens: 
                    
                    box = layout.box().column(1)  

                    row = box.column(1)
                    row.prop(context.space_data, "lens")

                    box.separator() 
                    
                    row = box.column(1)
                    row.prop(context.space_data, "clip_start", text="ClipStart")
                    row.prop(context.space_data, "clip_end", text="ClipEnd")


                if tp.display_navi: 

                    box = layout.box().column(1) 

                    row = box.row(1)
                    row.alignment = 'CENTER'     
                    row.operator("view3d.viewnumpad", text=" ", icon='CAMERA_DATA').type = 'CAMERA'
                    row.operator("view3d.view_selected", text=" ", icon='ZOOM_SELECTED')
                    row.operator("view3d.view_center_cursor", text=" ", icon='FORCE_FORCE')        
                    row.operator("view3d.view_all", text=" ", icon='MANIPUL').center = True
                 
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

                    #box.separator()       

                    box = layout.box().column(1)  
                    
                    row = box.row(1)  
                    row.operator("view3d.localview", text="Global/Local", icon='WORLD')
                    row.operator("view3d.view_persportho", text="Persp/Ortho", icon='VIEW3D')             

                    box.separator()                             

                    row = box.column(1)
                    row.prop(context.space_data, "lock_object", text="View to:")

                    box.separator() 
                 


        Display_Restrict = context.user_preferences.addons[__package__].preferences.tab_restrict
        if Display_Restrict == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tp.display_restrict:            
                row.prop(tp, "display_restrict", text="", icon="BORDER_RECT")
                row.label("Restrict")
            else:
                row.prop(tp, "display_restrict", text="", icon="BORDER_RECT")                
                row.label("Restrict")

                row.operator("tp_ops.unfreeze_selected", text="", icon = 'RESTRICT_SELECT_ON')         
                obj = context.active_object
                if obj:
                    row.prop(context.object, "hide_select", text="", icon = "RESTRICT_SELECT_OFF")
                    row.prop(context.object, "hide_render", text="", icon = "RESTRICT_RENDER_OFF")
                else:
                    pass
                row.menu("VIEW3D_MT_object_showhide", "", icon = "VISIBLE_IPO_ON")   

            if tp.display_restrict:            
               
                box.separator() 

                obj = context.active_object
                if obj:

                    row = box.row(1)
                    row.prop(context.object, "hide_select", text="Select", icon = "RESTRICT_SELECT_OFF")
                    row.prop(context.object, "hide_render", text="Render", icon = "RESTRICT_RENDER_OFF")
                else:
                    pass

                row = box.row(1)
                row.operator("tp_ops.unfreeze_selected", text="Unfreeze All", icon = 'RESTRICT_SELECT_ON') 
                
                box.separator() 
                               
                row = box.row(1) 
                row.operator("object.hide_view_set", "Hide Select", icon = 'RESTRICT_VIEW_ON').unselected=False
                row.operator("object.hide_view_set", "Hide UnSelect", icon = 'RESTRICT_VIEW_ON').unselected=True
               
                row = box.row(1) 
                row.operator("object.hide_view_clear", "Show All Hidden", icon = 'RESTRICT_VIEW_OFF')
               
                box.separator() 





        Display_Display = context.user_preferences.addons[__package__].preferences.tab_display
        if Display_Display == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tp.display_display:            
                row.prop(tp, "display_display", text="", icon="ZOOM_SELECTED")
                row.label("Display")
            else:
                row.prop(tp, "display_display", text="", icon="ZOOM_SELECTED")                
                row.label("Display")

                obj = context.active_object     
                if obj:
                    obj_type = obj.type
                                                                          
                    if obj_type in {'ARMATURE', 'POSE','LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER'}: 
 
                        row.prop(context.object, "show_bounds", text="", icon='SNAP_PEEL_OBJECT')                     
                        row.prop(context.object, "show_x_ray", text="", icon ="META_CUBE")
 
                    else:
                        
                        obj = context.object
                        if obj:               
                            if obj.draw_type == 'WIRE':
                                row.operator("tp_ops.draw_solid", text="", icon='GHOST_DISABLED')     
                            else:
                                row.operator("tp_ops.draw_wire", text="", icon='GHOST_ENABLED')        
                        else:
                            row.label("", icon="BLANK1")  
                        
                        if obj:
                            active_wire = obj.show_wire 
                            if active_wire == True:
                                row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
                            else:                       
                                row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID')
                        else:
                            row.label("", icon="BLANK1")  

                        if obj:                  
                            row.prop(context.object, "show_x_ray", text="", icon ="META_CUBE")

                            obj_type = obj.type                    
                            if obj_type in {'MESH'}:   
                                row.prop(context.space_data, "show_backface_culling", text="", icon ="MOD_LATTICE")         
                        else:
                            pass

            if tp.display_display: 

                box.separator()
                
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
                          
                            box.separator() 


                    if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:
             
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



                   
        
     
 
        Display_Shade = context.user_preferences.addons[__package__].preferences.tab_shade
        if Display_Shade == 'on':                                         

            GEOM_Smooth = ['SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

            obj = context.active_object     
            if obj:
                obj_type = obj.type                                                                
                if obj_type not in GEOM_Smooth:

                    box = layout.box().column(1)
                    
                    row = box.row(1)
                    if tp.display_shade:            
                        row.prop(tp, "display_shade", text="", icon="MOD_EDGESPLIT")
                        row.label("Smooth")
                    else:
                        row.prop(tp, "display_shade", text="", icon="MOD_EDGESPLIT")                
                        row.label("Smooth")
                          
                        obj = context.active_object     
                        if obj:
                           obj_type = obj.type
                                          
                           if obj and obj_type in {'MESH'}:
                               
                               row.prop(context.active_object.data, "use_auto_smooth", text="",icon="AUTO")

                       
                        if context.mode == 'EDIT_MESH':          

                            row.operator("mesh.faces_shade_flat", text="", icon="MESH_CIRCLE") 
                            row.operator("mesh.faces_shade_smooth", text="", icon="SMOOTH")  
                            row.operator("mesh.normals_make_consistent", text="", icon="SNAP_NORMAL")  
                        
                        if context.mode == 'OBJECT':             
              
                            row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
                            row.operator("object.shade_smooth", text="", icon="SMOOTH")  
                            row.operator("tp_ops.rec_normals", text="", icon="SNAP_NORMAL") 


                        if context.mode == 'EDIT_CURVE':
                            
                            row.operator("curve.normals_make_consistent",text="", icon='SNAP_NORMAL')     
                    
                 
                    if tp.display_shade: 
                    
                                     
                        if context.mode == 'EDIT_MESH':          

                            box.separator()  

                            row = box.row(1) 
                            row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                            row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 
                            
                            row = box.row(1)
                            row.prop(context.active_object.data, "show_double_sided",icon="GHOST")    
                            row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                        
                            row = box.row(1)
                            row.active = context.active_object.data.use_auto_smooth
                            row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")  

                            box.separator()   
                            box.separator()   

                            row = box.row(1) 
                            row.operator("mesh.mark_sharp", text="VertSharp", icon='SNAP_VERTEX').use_verts = True          
                            props = row.operator("mesh.mark_sharp", text="Clear", icon='X')
                            props.use_verts = True
                            props.clear = True
                            
                            row = box.row(1)  
                            row.operator("mesh.mark_sharp", text="EdgeSharp", icon='SNAP_EDGE')
                            row.operator("mesh.mark_sharp", text="Clear", icon='X').clear = True

                            box.separator()   
                            box.separator() 
                      
                            row = box.row(1)
                            row.operator("mesh.normals_make_consistent",text="Rec. Normals", icon='SNAP_NORMAL')
                            row.operator("mesh.flip_normals", text="Flip", icon = "FILE_REFRESH")            

                            row = box.row(1)
                            row.operator("mesh.normals_make_consistent", text="Rec-Inside").inside = True        
                            row.operator("mesh.normals_make_consistent", text="Rec-Outside").inside = False             
                                   
                            row = box.row(1)
                            row.prop(context.active_object.data, "show_normal_vertex", text="", icon='VERTEXSEL')
                            row.prop(context.active_object.data, "show_normal_loop", text="", icon='LOOPSEL')
                            row.prop(context.active_object.data, "show_normal_face", text="", icon='FACESEL')
                             
                            row.active = context.active_object.data.show_normal_vertex or context.active_object.data.show_normal_face
                            row.prop(context.scene.tool_settings, "normal_size", text="Size")  
                            
                            box.separator()  
                        
                        else:            

                            box.separator() 
                            
                            if context.mode == 'OBJECT': 
                                
                                row = box.row(1)  
                                row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                                row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
                           
                                box.separator() 
                                
                                obj = context.active_object     
                                if obj:
                                   obj_type = obj.type
                                                  
                                   if obj and obj_type in {'MESH'}:

                                       row = box.row(1)
                                       row.prop(context.active_object.data, "show_double_sided",icon="GHOST")    
                                       row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                                    
                                       row = box.row(1)
                                       row.active = context.active_object.data.use_auto_smooth
                                       row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")   
                    
                                   else:
                                       pass                            

                                box.separator() 
                                
                                row = box.row(1)  
                                row.operator("tp_ops.rec_normals", text="Consistent Normals", icon="SNAP_NORMAL")  


                            if context.mode == 'EDIT_CURVE':
                                
                                row = box.row(1)  
                                row.operator("curve.normals_make_consistent",text="Recalculate Normals", icon='SNAP_NORMAL')     


                        box.separator() 



        Display_Material = context.user_preferences.addons[__package__].preferences.tab_material
        if Display_Material == 'on':                                         

            obj = context.active_object     
            if obj:
                obj_type = obj.type

                if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:

                    box = layout.box().column(1)
                    
                    row = box.row(1)
                    if tp.display_material:            
                        row.prop(tp, "display_material", text="", icon="MATERIAL_DATA")
                        row.label("Material")
                    else:
                        row.prop(tp, "display_material", text="", icon="MATERIAL_DATA")                
                        row.label("Material")
                    
                        row.operator("tp_ops.material_add", text="", icon='ZOOMIN')
                      
                        if bpy.context.scene.render.engine == 'CYCLES':
                            if len(context.object.material_slots) > 0:                            
                                sub = row.row(1)
                                sub.scale_x = 0.35 
                                sub.prop(context.object.active_material, "diffuse_color", text="")  
                            else:
                                pass   
                     
                        else:
                            
                            obj = context.active_object
                            if obj:                   
                                sub = row.row(1)
                                sub.scale_x = 0.35 
                                sub.prop(context.object, "color", text="")                     
                            else:
                                pass          
                        row.menu("tp_ops.material_list", text="", icon="COLLAPSEMENU")


                    if tp.display_material: 
                             
                        box.separator() 

                        row = box.row(1)  
                        row.operator("tp_ops.material_add", text="Add Material", icon='ZOOMIN')
                        row.operator("tp_ops.remove_all_material", text="Remove", icon="ZOOMOUT")   
                      
                        row = box.row(1)                  
                        row.label("Object Color")               
                        if bpy.context.scene.render.engine == 'CYCLES':
                            row.prop(context.object.active_material, "diffuse_color", text="")  
                        else:
                            row.prop(context.object, "color", text="")                     
                      
                        row = box.row(1)                  
                        row.operator("tp_ops.purge_unused_material", text="Purge Unused", icon="PANEL_CLOSE")             
                        row.menu("tp_ops.material_list", text="MatList", icon="COLLAPSEMENU")             


        Display_Modifier = context.user_preferences.addons[__package__].preferences.tab_modifier
        if Display_Modifier == 'on':                                         

            GEOM_MOD = ['META', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

            obj = context.active_object     
            if obj:
                obj_type = obj.type                                                                
                if obj_type not in GEOM_MOD:

                    box = layout.box().column(1)
                    
                    row = box.row(1)
                    if tp.display_modifier:            
                        row.prop(tp, "display_modifier", text="", icon="MODIFIER")
                        row.label("Modifier")
                    else:
                        row.prop(tp, "display_modifier", text="", icon="MODIFIER")                
                        row.label("Modifier")
                    
         
                        
                        if context.mode == 'OBJECT':
                        
                            row.operator("tp_ops.mods_render","", icon = 'RESTRICT_RENDER_OFF') 
                            row.operator("tp_ops.mods_view","", icon = 'RESTRICT_VIEW_OFF')                                                                       
                        
                        if context.active_object.mode == 'EDIT':
                        
                            row.operator("tp_ops.mods_edit","", icon='EDITMODE_HLT')                                                    
                            row.operator("tp_ops.mods_cage","", icon='OUTLINER_OB_MESH')                  
                        
                        row.operator("tp_ops.remove_mod", text="", icon='X') 
                        row.operator("tp_ops.apply_mod", text="", icon='FILE_TICK')  


                    if tp.display_modifier: 
                             
                        box.separator() 

                        row = box.row(1) 
                        row.operator_menu_enum("object.modifier_add", "type","Add Modifier", icon="BLANK1")          

                        box.separator() 

                        obj = context.active_object
                        if obj:
                            mod_list = obj.modifiers
                            if mod_list:

                                row.operator("tp_ops.mods_render","", icon = 'RESTRICT_RENDER_OFF') 
                                row.operator("tp_ops.mods_view","", icon = 'RESTRICT_VIEW_OFF')                                                                       
                                
                                if context.active_object.mode == 'EDIT':
                                
                                    row.operator("tp_ops.mods_edit","", icon='EDITMODE_HLT')                                                    
                                    row.operator("tp_ops.mods_cage","", icon='OUTLINER_OB_MESH')                  
                                
                                row.operator("tp_ops.remove_mod", text="", icon='X') 
                                row.operator("tp_ops.apply_mod", text="", icon='FILE_TICK')          

                        else:
                            pass

                        box.separator()           

                        obj = context.active_object
                        if obj:
                            mod_list = obj.modifiers
                            if mod_list:

                                row = box.row(1)

                                row.prop(context.scene, "tp_mods_type", text="")
                                row.operator("tp_ops.remove_mods_type", text="Remove by Type")                           
                 

                                if context.mode == 'OBJECT':

                                    row = box.row(1)
                                    row.operator("scene.to_all", text="To Childs", icon='LINKED').mode = "modifier, children"    
                                    row.operator("scene.to_all", text="To Selected", icon='FRAME_NEXT').mode = "modifier, selected"

                                box.separator() 

                        else:
                            pass



                        box = layout.box().column(1)
                        
                        row = box.row(1)
                        if tp.display_subsurf:            
                            row.prop(tp, "display_subsurf", text="", icon="MOD_SUBSURF")
                        else:
                            row.prop(tp, "display_subsurf", text="", icon="MOD_SUBSURF")
                            
                        row.label("SubSurf")
                       
                        if len(context.selected_objects) == 1:
                            
                            is_subsurf = False
                            
                            for mode in bpy.context.object.modifiers :
                                if mode.type == 'SUBSURF' :
                                    is_subsurf = True
                            
                            if is_subsurf == True:
                             
                                if context.mode == 'EDIT_MESH':
                                    row.operator("transform.edge_crease", text="", icon='IPO_EASE_IN_OUT')   

                                row.operator("tp_ops.remove_mods_subsurf", text="" , icon='X')             
                                row.operator("tp_ops.apply_mods_subsurf", text="", icon='FILE_TICK')                                                                                                                                             
                   
                        else: 
                            pass 
                      

                        box.separator()  
                        
                        row = box.row(1)
                        row.scale_x = 0.6             
                        row.operator("tp_ops.subsurf_0")
                        row.operator("tp_ops.subsurf_1")
                        row.operator("tp_ops.subsurf_2")            
                        row.operator("tp_ops.subsurf_3")
                        row.operator("tp_ops.subsurf_4")
                        row.operator("tp_ops.subsurf_5")
                        #row.operator("tp_ops.subsurf_6")


                        
                        box.separator() 
                        
                        if tp.display_subsurf: 
                                            
                            obj = context.active_object
                            if obj:
                 
                                mo_types = []
                                append = mo_types.append

                                for mo in obj.modifiers:
                                    if mo.type == 'SUBSURF':
                                        append(mo.type)

                                        #box.label(mo.name)

                                        row = box.row(1)
                                        row.prop(mo, "use_subsurf_uv",text="UVs")
                                        row.prop(mo, "show_only_control_edges",text="Optimal")                    
                                        #row.prop(mo, "use_opensubdiv",text="OPSubdiv")                    
                                        #row.prop(system, "opensubdiv_compute_type", text="")

                                        box.separator() 

                            else:
                                pass
                            

                        obj = context.active_object     
                        if obj:
                            obj_type = obj.type
                                                                                  
                            if obj_type in {'MESH'}:

                                box = layout.box().column(1)
                                
                                row = box.row(1)

                                if tp.display_dim:            
                                    row.prop(tp, "display_dim", text="", icon="MAN_SCALE")            
                                    row.label("CopyDim") 
                                
                                else:
                                    row.prop(tp, "display_dim", text="", icon="MOD_WIREFRAME")                
                                    row.label("MirrorCut") 
                                                       
                                    row.prop(context.scene, "tp_mirror", text="", icon ="MOD_MIRROR")   
                                    if bpy.context.scene.tp_mirror == True:
                                        row.prop(context.scene, "tp_apply", text="", icon ="FILE_TICK")                     
                                    else:
                                        pass
                                    row.prop(context.scene, "tp_sculpt", text="", icon ="SCULPTMODE_HLT")   
                                    row.prop(context.scene, "tp_edit", text="", icon ="EDIT")            
                                                

                                if tp.display_dim:  
                                
                                    box.separator()  
                                   
                                    row = box.row(1)
                                    row.operator("tp_ops.copy_dimension_axis", text = "x > y").tp_axis='tp_x_y'
                                    row.operator("tp_ops.copy_dimension_axis", text = "y > x").tp_axis='tp_y_x'
                                    row.operator("tp_ops.copy_dimension_axis", text = "z > x").tp_axis='tp_z_x'            

                                    row = box.row(1)           
                                    row.operator("tp_ops.copy_dimension_axis", text = "x > z").tp_axis='tp_x_z'
                                    row.operator("tp_ops.copy_dimension_axis", text = "y > z").tp_axis='tp_y_z'
                                    row.operator("tp_ops.copy_dimension_axis", text = "z > y").tp_axis='tp_z_y'

                                    box.separator()                 

                                else:
                                    
                                    box.separator()                    
                                                       
                                    row = box.row(1)         
                                    row.operator("tp_ops.mods_positiv_x_symcut", text="+X")
                                    row.operator("tp_ops.mods_positiv_y_symcut", text="+Y")
                                    row.operator("tp_ops.mods_positiv_z_symcut", text="+Z")

                                    row = box.row(1)             
                                    row.operator("tp_ops.mods_negativ_x_symcut", text="-- X")
                                    row.operator("tp_ops.mods_negativ_y_symcut", text="-- Y")
                                    row.operator("tp_ops.mods_negativ_z_symcut", text="-- Z")
                                 
                                    box.separator() 

                                    row = box.row(1)             
                                    row.operator("tp_ops.mods_negativ_xy_symcut", text="+Xy")
                                    row.operator("tp_ops.mods_negativ_xz_symcut", text="+Xz")
                                    row.operator("tp_ops.mods_negativ_yz_symcut", text="+Yz")

                                    row = box.row(1)             
                                    row.operator("tp_ops.mods_positiv_xy_symcut", text="-- Xy")
                                    row.operator("tp_ops.mods_positiv_xz_symcut", text="-- Xz")
                                    row.operator("tp_ops.mods_positiv_yz_symcut", text="-- Yz")
                             
                                    box.separator()  
                              
                                    row = box.row(1)             
                                    row.operator("tp_ops.mods_positiv_xyz_symcut", text="+XYZ")          
                                    row.operator("tp_ops.mods_negativ_xyz_symcut", text="-XYZ")
                     
                                    if context.mode == 'EDIT_MESH':
                                        row.operator("tp_ops.normal_symcut", text="Normal")
                                   
                                    box.separator() 

                    
                                obj = context.active_object
                                if obj:
                     
                                    mo_types = []            
                                    append = mo_types.append

                                    for mo in context.active_object.modifiers:
                                                                      
                                        if mo.type == 'MIRROR':
                                            append(mo.type)
                                            #box.label(mo.name)

                                            row = box.row(1)
                                            row.prop(mo, "use_x")
                                            row.prop(mo, "use_y")
                                            row.prop(mo, "use_z")
                                            
                                            row = box.row(1)
                                            row.prop(mo, "use_mirror_merge", text="Merge")
                                            row.prop(mo, "use_clip", text="Clipping")
                             
                                            box.separator() 

                                            row.operator("tp_ops.remove_mod_mirror", text="", icon='X') 
                                            row.operator("tp_ops.apply_mod_mirror", text="", icon='FILE_TICK')

                                else:
                                    pass

                        else:
                            pass                
                 
                        


        box = layout.box().column(1)
        
        row = box.row(1)

        if tp.display_overlay:            
            row.prop(tp, "display_overlay", text="Overlay", icon="LINK_AREA")
        else:
            row.prop(tp, "display_overlay", text="Overlay", icon="LINK_AREA")    
            
        if tp.display_flymode:            
            row.prop(tp, "display_flymode", text="FlyMode", icon="MOD_SOFT")
        else:
            row.prop(tp, "display_flymode", text="FlyMode", icon="MOD_SOFT")                            


        GEOM_UV = ['CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type not in GEOM_UV:

                row = box.row(1)              

                if tp.display_unwrap:            
                    row.prop(tp, "display_unwrap", text="Unwrap", icon="MOD_UVPROJECT")
                else:
                    row.prop(tp, "display_unwrap", text="Unwrap", icon="MOD_UVPROJECT")                            

                if tp.display_uvmagic:
                    row.prop(tp, "display_uvmagic", text="Magic UVs", icon='GROUP_UVS')
                else:
                    row.prop(tp, "display_uvmagic", text="Magic UVs", icon='GROUP_UVS')      


                if tp.display_unwrap:


                    box = layout.box().column(1)  

                    row = box.column(1)
                    row.label(text="UV Mapping:")

                    box.separator()

                    if context.mode == 'OBJECT':

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

                        box.separator()  
                                                                       
                        row = box.column(1) 
                        row.operator("uv.uv_equalize" , text ="UV Equalize", icon = 'MOD_UVPROJECT')           
                        row.operator("uthe.main_operator", text = "UV HardEdges", icon = 'MOD_EDGESPLIT')

                        box.separator()
                                                                


                    if context.mode == 'EDIT_MESH': 
                                
                        row = box.row(1)        
                        row.operator("mesh.mark_seam").clear = False
                        row.operator("mesh.mark_seam", text="Clear Seam").clear = True

                        box.separator()
                        box.separator()
                                    
                          
                        row = box.row(1)
                        row.operator("uv.unwrap", text="Unwrap")
                        row.operator("uv.reset",text="Reset")
                                    
                    row = box.row(1)
                    row.operator("uv.smart_project", text="Smart UV Project")
                                    
                    row = box.row(1)
                    row.operator("uv.lightmap_pack", text="Lightmap Pack")
                                    
                    if context.mode == 'EDIT_MESH': 
                        
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

                    row = box.row(1)
                    row.operator("uv.cpuv_copy_uv")
                    row.operator("uv.cpuv_paste_uv")
             
                    row = box.column(1)
                    if context.mode == 'EDIT_MESH': 

                        row.operator("uv.flip_rotate")
                        row.operator("uv.transfer_uv_copy")
                        row.operator("uv.transfer_uv_paste")
                        row.operator("uv.cpuv_selseq_copy_uv")
                        row.operator("uv.cpuv_selseq_paste_uv")

                    row.operator("uv.cpuv_uvmap_copy_uv_op")
                    row.operator("uv.cpuv_uvmap_paste_uv_op")

                    box.separator()  


        if tp.display_flymode:   

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



        if tp.display_overlay:    
          
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




        Display_History = context.user_preferences.addons[__package__].preferences.tab_history 
        if Display_History == 'on':
            
            box = layout.box().column(1)  

            row = box.row(1)        
            row.operator("view3d.ruler", text="Ruler", icon="NOCURVE")   
             
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
           
            box.separator()   




class VIEW3D_TP_Display_Compact_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Display_Compact_Panel_TOOLS"
    bl_label = "Display Tools"
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
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_display_compact_panel_layout(self, context, layout) 



class VIEW3D_TP_Display_Compact_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Display_Compact_Panel_UI"
    bl_label = "Display Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'  

        draw_display_compact_panel_layout(self, context, layout) 


