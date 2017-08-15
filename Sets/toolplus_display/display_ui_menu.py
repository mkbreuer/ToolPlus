__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"


import bpy
from bpy import *
from . icons.icons import load_icons             


class VIEW3D_TP_Display_OSD_MENU(bpy.types.Menu):
    bl_label = "Display Tools"
    bl_idname = "tp_menu.display_osd"
    
    def draw(self, context):
        layout = self.layout                         
                 
        layout.prop(bpy.context.space_data, 'viewport_shade', text="")
        layout.menu("VIEW3D_TP_Shade_Menu", icon = "WORLD")                 
        layout.menu("VIEW3D_TP_Screen_Menu", icon = "VIEW3D")                 
        layout.menu("VIEW3D_TP_Restrict_Menu", icon = "BORDER_RECT")         
        layout.menu("VIEW3D_TP_Display_Menu", icon = "ZOOM_SELECTED")         
        layout.menu("VIEW3D_TP_Smooth_Menu", icon = "MOD_EDGESPLIT")         
        layout.menu("VIEW3D_TP_Material_Menu", icon = "MATERIAL_DATA")         
        layout.menu("VIEW3D_TP_Modifier_Menu", icon = "MODIFIER")         
        layout.menu("VIEW3D_TP_Overlay_Menu", icon = "LINK_AREA")         
        layout.menu("VIEW3D_TP_Flymode_Menu", icon = "MOD_SOFT")                 
 
        layout.separator() 

        if context.mode == 'EDIT_MESH':
            layout.menu("VIEW3D_TP_Measure_Menu", icon = "ALIGN")  
            
        layout.operator("view3d.ruler", icon = "NOCURVE")




class VIEW3D_TP_Modifier_Menu(bpy.types.Menu):
    bl_label = "Modifier"
    bl_idname = "VIEW3D_TP_Modifier_Menu"  
    bl_space_type = 'VIEW_3D'
    
    def draw(self, context):
        layout = self.layout
     
        obj = context.active_object
      
        icons = load_icons()
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.operator_menu_enum("object.modifier_add", "type", text="New", icon='MODIFIER')            

        if obj:
            mod_list = obj.modifiers
            if mod_list:
                layout.menu("VIEW3D_TP_Visual_SubMenu", text="Visual", icon='RESTRICT_VIEW_OFF')
            else:
                pass         

        layout.separator()       
       
        layout.menu("VIEW3D_TP_SubSurf_SubMenu", text="Subsurf", icon='MOD_SUBSURF')

        if obj:
            if obj.type in {'MESH'}:
                layout.menu("VIEW3D_TP_SymDim_Plus_SubMenu", text="SymDim Plus", icon='MOD_WIREFRAME')
                layout.menu("VIEW3D_TP_SymDim_Minus_SubMenu", text="SymDim Minus", icon='MOD_WIREFRAME')
            else:
                pass 
       
        if obj:
            mod_list = obj.modifiers
            if mod_list:

                if context.mode == 'OBJECT':

                    layout.separator() 
                    
                    layout.operator("scene.to_all", text="Copy to Childs", icon='LINKED').mode = "modifier, children"    
                    layout.operator("scene.to_all", text="Copy to Selected", icon='FRAME_NEXT').mode = "modifier, selected"

                layout.separator()

                obj = context.object      
                if obj.mode == 'OBJECT':
                    layout.operator("tp_ops.apply_mod", icon = 'FILE_TICK', text="Apply all")
                       
                if obj.mode == 'EDIT':
                    layout.operator("tp_ops.apply_mod", icon = 'FILE_TICK', text="Apply all")        
                
                layout.operator("tp_ops.remove_mod", icon = 'PANEL_CLOSE', text="Delete all")
                
               
                layout.separator()

                layout.prop(context.scene, "tp_mods_type", text="")
                layout.operator("tp_ops.remove_mods_type", text="Remove by Type", icon='PANEL_CLOSE')                           
     
                layout.separator()

                layout.operator("tp_ops.collapse_mod", icon = 'TRIA_RIGHT', text="HoverCollapse")  
                layout.operator("tp_ops.expand_mod", icon = 'TRIA_DOWN', text="HoverExpand")

            else:
                pass



    
     


class VIEW3D_TP_SubSurf_SubMenu(bpy.types.Menu):
    bl_label = "Mirror Subsurf"
    bl_idname = "VIEW3D_TP_SubSurf_SubMenu"
    
    def draw(self, context):
        layout = self.layout
       
        layout.operator("tp_ops.subsurf_0")
        layout.operator("tp_ops.subsurf_1")
        layout.operator("tp_ops.subsurf_2")            
        layout.operator("tp_ops.subsurf_3")
        layout.operator("tp_ops.subsurf_4")
        layout.operator("tp_ops.subsurf_5")
        layout.operator("tp_ops.subsurf_6")

        is_subsurf = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'SUBSURF' :
                is_subsurf = True
        
        if is_subsurf == True:

            layout.separator()
            
            layout.operator("tp_ops.apply_mods_subsurf", text="Apply", icon='FILE_TICK')  
            layout.operator("tp_ops.remove_mods_subsurf", text="Remove" , icon='X')             




class VIEW3D_TP_SymDim_Plus_SubMenu(bpy.types.Menu):
    bl_label = "SymDim"
    bl_idname = "VIEW3D_TP_SymDim_Plus_SubMenu"
    
    def draw(self, context):
        layout = self.layout

        layout.operator("tp_ops.mods_positiv_x_symcut", "+X")
        layout.operator("tp_ops.mods_positiv_y_symcut", "+Y")
        layout.operator("tp_ops.mods_positiv_z_symcut", "+Z")        

        layout.separator()

        layout.operator("tp_ops.mods_positiv_xy_symcut", "+XY")
        layout.operator("tp_ops.mods_positiv_xz_symcut", "+XZ")
        layout.operator("tp_ops.mods_positiv_yz_symcut", "+YZ")
        layout.operator("tp_ops.mods_positiv_xyz_symcut", "+XYZ")

        obj = context.active_object
        if obj:
                     
            for mo in context.active_object.modifiers:                                              
                if mo.type == 'MIRROR':                    
                    
                    layout.separator()

                    layout.operator("tp_ops.apply_mod_mirror", text="Apply", icon='FILE_TICK')
                    layout.operator("tp_ops.remove_mod_mirror", text="Remove", icon='X') 
        else:
            pass



class VIEW3D_TP_SymDim_Minus_SubMenu(bpy.types.Menu):
    bl_label = "SymDim"
    bl_idname = "VIEW3D_TP_SymDim_Minus_SubMenu"
    
    def draw(self, context):
        layout = self.layout
                
        layout.operator("tp_ops.mods_negativ_x_symcut", "-- X")
        layout.operator("tp_ops.mods_negativ_y_symcut", "-- Y")    
        layout.operator("tp_ops.mods_negativ_z_symcut", "-- Z")

        layout.separator()    

        layout.operator("tp_ops.mods_negativ_xy_symcut", "-- XY")
        layout.operator("tp_ops.mods_negativ_xz_symcut", "-- XZ")
        layout.operator("tp_ops.mods_negativ_yz_symcut", "-- YZ")
        layout.operator("tp_ops.mods_negativ_xyz_symcut", "-- XYZ")

        obj = context.active_object
        if obj:
                     
            for mo in context.active_object.modifiers:                                              
                if mo.type == 'MIRROR':

                    layout.separator()

                    layout.operator("tp_ops.apply_mod_mirror", text="Apply", icon='FILE_TICK')
                    layout.operator("tp_ops.remove_mod_mirror", text="Remove", icon='X') 
        else:
            pass



class VIEW3D_TP_Visual_SubMenu(bpy.types.Menu):
    bl_label = "Visual Modifier"
    bl_idname = "VIEW3D_TP_Visual_SubMenu"
    
    def draw(self, context):
        layout = self.layout                         
    
        layout.operator("tp_ops.mods_view","View", icon = 'RESTRICT_VIEW_OFF')                                                                       
        layout.operator("tp_ops.mods_edit","Edit", icon='EDITMODE_HLT')                                                    
        layout.operator("tp_ops.mods_cage","Cage", icon='OUTLINER_OB_MESH')      
        layout.operator("tp_ops.mods_render","Render", icon = 'RESTRICT_RENDER_OFF') 



class VIEW3D_TP_Shade_Menu(bpy.types.Menu):
    bl_label = "Shade"
    bl_idname = "VIEW3D_TP_Shade_Menu"

    def draw(self, context):
        layout = self.layout

        view = context.space_data
        scene = context.scene 
        gs = scene.game_settings 
        
                             
        layout.prop(view, "show_world", "World")# ,icon ="WORLD")

        if view.show_world:        

            layout.menu("VIEW3D_TP_World_SubMenu")#, icon = "MOD_CURVE") 

            layout.separator()

        if view.viewport_shade == 'SOLID':
            
            layout.prop(view, "use_matcap")
            
            if view.use_matcap:
                sub = layout.row(1)
                sub.scale_y = 0.2
                sub.scale_x = 1
                sub.template_icon_view(context.space_data, "matcap_icon")
                
                layout.separator()


        if view.show_only_render:        
            layout.operator("tp_ops.toggle_silhouette", text="Silhouette", icon ="CHECKBOX_HLT")
        else:
            layout.operator("tp_ops.toggle_silhouette", text="Silhouette", icon ="CHECKBOX_DEHLT")


        fx_settings = view.fx_settings
        if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:

            layout.prop(view.fx_settings, "use_ssao", text="Ambient Occlusion")
            
            if view.fx_settings.use_ssao:
              
                layout.menu("VIEW3D_TP_AOccl_SubMenu")#, icon = "MOD_CURVE")           

                layout.separator()      
        

        layout.separator()

        if view.viewport_shade == 'SOLID':
            layout.prop(view, "show_textured_solid")
            
        if view.viewport_shade == 'TEXTURED' or context.mode == 'PAINT_TEXTURE':
            if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                layout.prop(view, "show_textured_shadeless")

        if not scene.render.use_shading_nodes:
            layout.prop(gs, "material_mode", text="")
        

        layout.separator()

        layout.prop(context.space_data, "show_floor", text="Grid Floor")#, icon ="GRID")  

        if context.space_data.show_floor:
              
            layout.menu("VIEW3D_TP_Grid_SubMenu")#, icon = "MOD_CURVE") 

        layout.separator() 

        layout.prop(view, "show_axis_x", text="X Axis", toggle=True)
        layout.prop(view, "show_axis_y", text="Y Axis", toggle=True)
        layout.prop(view, "show_axis_z", text="Z Axis", toggle=True)




class VIEW3D_TP_World_SubMenu(bpy.types.Menu):
    bl_label = "World Props"
    bl_idname = "VIEW3D_TP_World_SubMenu"

    def draw(self, context):
        layout = self.layout

        scene = context.scene 

        layout.label("Color")
        layout.prop(scene.world, "horizon_color", "")
            
        layout.separator()            

        layout.label("Lamp Settings")  
        layout.prop(scene.world, "exposure")
        layout.prop(scene.world, "color_range")




class VIEW3D_TP_AOccl_SubMenu(bpy.types.Menu):
    bl_label = "AOccl Props"
    bl_idname = "VIEW3D_TP_AOccl_SubMenu"

    def draw(self, context):
        layout = self.layout

        view = context.space_data

        layout.label("Color")
        layout.prop(view.fx_settings.ssao, "color","")

        layout.separator()

        layout.prop(view.fx_settings.ssao, "factor")
        layout.prop(view.fx_settings.ssao, "distance_max")
        layout.prop(view.fx_settings.ssao, "attenuation")
        layout.prop(view.fx_settings.ssao, "samples")


class VIEW3D_TP_Grid_SubMenu(bpy.types.Menu):
    bl_label = "Grid Props"
    bl_idname = "VIEW3D_TP_Grid_SubMenu"

    def draw(self, context):
        layout = self.layout

        view = context.space_data

        layout.prop(view, "grid_lines", text="Lines")
        layout.prop(view, "grid_scale", text="Scale")
        layout.prop(view, "grid_subdivisions", text="Subdivision")




class VIEW3D_TP_Quad_SubMenu(bpy.types.Menu):
    bl_label = "Quad Props"
    bl_idname = "VIEW3D_TP_Quad_SubMenu"

    def draw(self, context):
        layout = self.layout

        view = context.space_data

        layout.operator_context = 'INVOKE_REGION_WIN'  
           
        region = view.region_quadviews[2]
        layout.prop(region, "lock_rotation")
       
        layout1 = layout.row(1)        
        layout1.enabled = region.lock_rotation
        layout1.prop(region, "show_sync_view")
        
        layout2 = layout.row(1)  
        layout2.enabled = region.lock_rotation and region.show_sync_view
        layout2.prop(region, "use_box_clip")   



class VIEW3D_TP_Screen_Menu(bpy.types.Menu):
    bl_label = "Screen"
    bl_idname = "VIEW3D_TP_Screen_Menu"

    def draw(self, context):
        layout = self.layout

        view = context.space_data

        layout.operator_context = 'INVOKE_REGION_WIN'  

        layout.operator("screen.region_quadview", text="Quad View", icon = "SPLITSCREEN")

        if view.region_quadviews:
            
            layout.menu("VIEW3D_TP_Quad_SubMenu")           
            
        layout.separator()   

        layout.operator("screen.screen_full_area", text = "Full Area", icon = "GO_LEFT")  
        layout.operator("wm.window_fullscreen_toggle", text = "Full Screen", icon = "FULLSCREEN_ENTER")      
        layout.operator("wm.window_duplicate", text="Dupli View", icon = "SCREEN_BACK")       

        layout.separator()   
         
        layout.prop(context.space_data, "lens")

        layout.separator() 

        layout.prop(context.space_data, "clip_start", text="ClipStart")
        layout.prop(context.space_data, "clip_end", text="ClipEnd")


class VIEW3D_TP_Restrict_Menu(bpy.types.Menu):
    bl_label = "Restrict"
    bl_idname = "VIEW3D_TP_Restrict_Menu"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'

        obj = context.active_object
        if obj:
            layout.prop(context.object, "hide_select", text="Select")
        else:
            pass

        layout.operator("object.hide_select_clear", text="Clear All", icon = 'RESTRICT_SELECT_ON') 
        
        layout.separator() 
                       
        layout.operator("object.hide_view_set", "Hide Select", icon = 'RESTRICT_VIEW_ON').unselected=False
        layout.operator("object.hide_view_set", "Hide UnSelect", icon = 'RESTRICT_VIEW_ON').unselected=True
        layout.operator("object.hide_view_clear", "Show All Hidden", icon = 'RESTRICT_VIEW_OFF')

        #layout.prop(context.object, "hide", text ="Hide", icon="RESTRICT_VIEW_OFF")

    
        if obj:     

          layout.separator() 

          layout.prop(context.object, "hide_render", text="Render", icon = "RESTRICT_RENDER_OFF")

        else:
            pass




class VIEW3D_TP_Display_Menu(bpy.types.Menu):
    bl_label = "Display"
    bl_idname = "VIEW3D_TP_Display_Menu"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        active_wire = obj.show_wire 
        if active_wire == True:
            layout.operator("tp_ops.wire_off", "Wire off", icon = 'CHECKBOX_HLT')              
        else:                       
            layout.operator("tp_ops.wire_on", "Wire on", icon = 'CHECKBOX_DEHLT')

        layout.operator("tp_ops.wire_all", text="Wire All", icon='RADIOBUT_OFF')
  
        layout.separator()            
       
        if obj.draw_type == 'WIRE':
            layout.operator("tp_ops.draw_solid", text="Solid on", icon='CHECKBOX_HLT')     
        else:
            layout.operator("tp_ops.draw_wire", text="Solid off", icon='CHECKBOX_DEHLT')        
       
        layout.prop(context.object, "draw_type", text="")        

        layout.separator() 

        if obj.show_bounds == True:  
            layout.prop(context.object, "show_bounds", text="ShowBounds", icon='CHECKBOX_HLT') 
        else:
            layout.prop(context.object, "show_bounds", text="ShowBounds", icon='CHECKBOX_DEHLT') 

        layout.prop(context.object, "draw_bounds_type", text="")            


        if context.mode == 'EDIT_MESH':          
           
            layout.separator()               
          
            layout.prop(context.object, "show_x_ray", text="X-Ray")            
            layout.prop(context.space_data, "show_backface_culling", text="Backface")   
            layout.prop(context.space_data, "show_occlude_wire", text="Hidden")      

            layout.separator()   

            layout.prop(context.space_data, "use_occlude_geometry", text="Occlude")   
      
        else:                        
           
            layout.separator()   
          
            layout.prop(context.object, "show_x_ray", text="X-Ray")
        
            obj = context.active_object
            obj_type = obj.type                    
            if obj_type in {'MESH'}:   
                layout.prop(context.space_data, "show_backface_culling", text="Backface")  



class VIEW3D_TP_Measure_Menu(bpy.types.Menu):
    bl_label = "Measure"
    bl_idname = "VIEW3D_TP_Measure_Menu"

    def draw(self, context):
        layout = self.layout

        data = context.active_object.data

        layout.prop(data, "show_extra_edge_length", text="Edge Length")
        layout.prop(data, "show_extra_edge_angle", text="Edge Angle")

        layout.separator()  

        layout.prop(data, "show_extra_face_area", text="Face Area")
        layout.prop(data, "show_extra_face_angle", text="Face Angle")



class VIEW3D_TP_Smooth_Menu(bpy.types.Menu):
    bl_label = "Smooth"
    bl_idname = "VIEW3D_TP_Smooth_Menu"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        if obj and obj.mode == 'OBJECT':
            layout.operator("object.shade_flat", icon="MESH_CIRCLE")            
            layout.operator("object.shade_smooth", icon="SMOOTH")
        
            layout.separator() 
           
            layout.operator("tp_ops.rec_normals", text="Recalculate Normals", icon="SNAP_NORMAL") 
    
  
        if context.mode == 'EDIT_MESH':
           
            layout.operator("mesh.faces_shade_flat", icon="MESH_CIRCLE")               
            layout.operator("mesh.faces_shade_smooth", icon="SMOOTH")

            layout.separator() 
            
            layout.operator("mesh.normals_make_consistent", text="Recalculate Normals", icon="SNAP_NORMAL")  


        if context.mode == 'EDIT_CURVE':
            
            layout.operator("curve.normals_make_consistent", text="Recalculate Normals", icon="SNAP_NORMAL")          

      
        obj = context.active_object
        obj_type = obj.type                    
        if obj_type in {'MESH'}:   

            layout.separator() 
     
            layout.prop(context.active_object.data, "show_double_sided", "DoubleSided")        

            layout.prop(context.active_object.data, "use_auto_smooth", "AutoSmooth")

            if context.active_object.data.use_auto_smooth == True: 
                layout.prop(context.active_object.data, "auto_smooth_angle", text="Angle")     
            else:
                pass

 

class VIEW3D_TP_Material_Menu(bpy.types.Menu):
    bl_label = "Material"
    bl_idname = "VIEW3D_TP_Material_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 

        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')

        layout.operator("tp_ops.material_add", text="Add Material", icon="MATERIAL")
        layout.menu("tp_ops.material_list", text="Material List", icon="COLLAPSEMENU")        

        obj = context.active_object
        if obj:        
            if is_geometry or is_empty_image:
                    
                layout.separator()            

                layout.label(text="Object Color:", icon="COLOR")

                if bpy.context.scene.render.engine == 'CYCLES':
                    if len(context.object.material_slots) > 0:                            
                        layout.prop(context.object.active_material, "diffuse_color", text="")  
                    else:
                        pass   
             
                else:
                    layout.prop(context.object, "color", text="")                     
 
            else:
                pass      


        layout.separator()          
      
        layout.operator("tp_ops.remove_all_material", text="Delete Slots", icon="ZOOMOUT")   
        layout.operator("tp_ops.purge_unused_material", text="Purge Unused", icon="PANEL_CLOSE")             
    

class VIEW3D_TP_Overlay_Menu(bpy.types.Menu):
    bl_label = "Overlay"
    bl_idname = "VIEW3D_TP_Overlay_Menu"

    def draw(self, context):
        layout = self.layout

        view = context.space_data
        scene = context.scene
        rs = bpy.context.scene 
        gs = scene.game_settings
        obj = context.object
        mesh = context.active_object.data        
        with_freestyle = bpy.app.build_options.freestyle

        if obj and obj.mode == 'OBJECT':
              
            layout.prop(obj, "show_axis", text="Axis")        
            layout.prop(obj, "show_name", text="Name")

            layout.separator() 

            layout.prop(context.space_data, "show_outline_selected")
            layout.prop(context.space_data, "show_all_objects_origin")
            layout.prop(context.space_data, "show_relationship_lines")

            layout.separator() 
            
            obj = context.active_object
            if obj:
                obj_type = obj.type                         
         
                if obj_type in {'MESH'}: 
                    layout.prop(context.object, "show_transparent", text="Transparency") 
                           
                if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:                           
                    layout.prop(context.object, "show_texture_space", text="Texture Space")

            if view.viewport_shade == 'SOLID':
                layout.prop(view, "show_textured_solid")
                
            if view.viewport_shade == 'TEXTURED' or context.mode == 'PAINT_TEXTURE':
                if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                    layout.prop(view, "show_textured_shadeless")

            if not scene.render.use_shading_nodes:
                layout.prop(gs, "material_mode", text="")


        if context.mode == 'EDIT_MESH':
    
            layout.prop(mesh, "show_faces", text="Faces")
            layout.prop(mesh, "show_edges", text="Edges")
            layout.prop(mesh, "show_edge_crease", text="Creases")
            layout.prop(mesh, "show_weight", text = "Weights")

            if with_freestyle:
                layout.prop(mesh, "show_edge_seams", text="Seams")

            if not with_freestyle:
                layout.prop(mesh, "show_edge_seams", text="Seams")

            layout.prop(mesh, "show_edge_sharp", text="Sharp")
            layout.prop(mesh, "show_edge_bevel_weight", text="Bevel")  
                
            if with_freestyle:
                layout.prop(mesh, "show_freestyle_edge_marks", text="Edge Marks")
                layout.prop(mesh, "show_freestyle_face_marks", text="Face Marks")              
                   
            if bpy.app.debug:
                layout.prop(mesh, "show_extra_indices") 



        if context.mode == 'EDIT_CURVE':   

            layout.prop(context.object.data, "show_handles", text="Handles")
            layout.prop(context.object.data, "show_normal_face", text="Normals")
           
            if context.object.data.show_normal_face == True:  
                layout.prop(context.scene.tool_settings, "normal_size", text="Size")



class VIEW3D_TP_Flymode_Menu(bpy.types.Menu):
    bl_label = "Flymode"
    bl_idname = "VIEW3D_TP_Flymode_Menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.fast_navigate_operator",'PLAY', icon = "PLAY")
        layout.operator("view3d.fast_navigate_stop",'PAUSE', icon = "PAUSE")

        layout.separator()                  
    
        layout.prop(context.scene,"OriginalMode", "")
        layout.prop(context.scene,"FastMode", "")

        layout.separator()  
         
        layout.prop(context.scene,"EditActive", "Edit mode")

        layout.separator()       
      
        layout.prop(context.scene,"Delay") 
        layout.prop(context.scene,"DelayTimeGlobal")
      
        layout.separator()          
        
        layout.prop(context.scene,"ShowParticles")           
        layout.prop(context.scene,"ParticlesPercentageDisplay")   








class VIEW3D_TP_Display_Mesh_MENU(bpy.types.Menu):
    bl_label = "Display"
    bl_idname = "tp_menu.display_mesh"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
        is_dupli = (obj.dupli_type != 'NONE')

        mesh = context.active_object.data
        
        if obj and obj.mode == 'EDIT':

            layout.operator("wm.context_toggle", text="Limit to Visible", icon="ORTHO").data_path = "space_data.use_occlude_geometry"
            layout.menu("tp_menu.display_overlays", icon ="RETOPO")

            layout.separator() 
          
        
        layout.operator("tp_display.wire_all", text ="Wire all", icon = "CHECKBOX_DEHLT")
        
        if is_geometry or is_dupli:
            layout.prop(obj, "show_wire", text="Wire")
        if obj_type == 'MESH' or is_dupli:
            layout.prop(obj, "show_all_edges")
            
        layout.prop(obj, "show_x_ray", text="X-Ray")

        if obj and obj.mode == 'OBJECT':
            if obj_type == 'MESH' or is_empty_image:
                layout.prop(obj, "show_transparent", text="Transparency")

        layout.separator()
        
        if obj and obj.mode == 'OBJECT':                
            layout.prop(obj, "show_bounds", text="Bounds")
            layout.prop(obj, "draw_bounds_type", text="", icon="BBOX")
            
            layout.separator()
        
        if is_geometry:
            layout.prop(obj, "show_texture_space", text="Texture Space")

        if is_wire:
            layout.active = is_dupli
            layout.label(text="Maximum Dupli Draw Type:")
        else:
            layout.label(text="Maximum Draw Type:")
        layout.prop(obj, "draw_type", text="", icon="BRUSH_DATA")


        

















