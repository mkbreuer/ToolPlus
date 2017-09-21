
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons
    


class VIEW3D_TP_OpenGL_Panel_TOOLS(bpy.types.Panel):
    """OpenGL Lights Presets Panel""" 
    bl_category = "Shade / UVs"
    bl_idname = "VIEW3D_TP_OpenGL_Panel_TOOLS"
    bl_label = "World"
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

        draw_opengl_panel_layout(self, context, layout) 



class VIEW3D_TP_OpenGL_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_OpenGL_Panel_UI"
    bl_label = "World"
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

        draw_opengl_panel_layout(self, context, layout) 




def draw_opengl_panel_layout(self, context, layout):
    tp = context.window_manager.tp_collapse_menu_display  
            
    icons = load_icons()

    wm = context.window_manager 
    view = context.space_data
    scene = context.scene
    gs = scene.game_settings
    obj = context.object

    box = layout.box().column(1)  

    row = box.row(1)              
    row.alignment = 'CENTER'
    row.label("Viewport", icon='VIEW3D')  

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

    box.separator() 
    
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



    if tp.display_lens: 
        
        box = layout.box().column(1)  

        row = box.column(1)
        row.prop(context.space_data, "lens")

        box.separator() 
        
        row = box.column(1)
        row.label(text="Clip:")
        row.prop(context.space_data, "clip_start", text="Start")
        row.prop(context.space_data, "clip_end", text="End")


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
     





    box = layout.box().column(1)   

    row = box.row(1)              
    row.alignment = 'CENTER'
    row.label("Shading", icon='LAMP_SPOT')  

    box.separator()                

    row = box.row(1)
    row.alignment = 'CENTER'           
    row.operator("tp_ops.toggle_silhouette", text="", icon ="MATCAP_08")      
    row.prop(bpy.context.space_data, 'viewport_shade', text='', expand=True)

    box.separator()   

    row = box.row()
    row.prop(context.space_data, "show_only_render", text="Render")#, icon ="RESTRICT_RENDER_OFF")    
    
    row = box.row()
    row.prop(context.space_data, "show_world", "World")# ,icon ="WORLD")

    if context.space_data.show_world:        
   
        if tp.display_world:            
            row.prop(tp, "display_world", text="", icon="TRIA_UP_BAR")
        else:
            row.prop(tp, "display_world", text="", icon="TRIA_DOWN_BAR")    

        sub = row.row(1)
        sub.scale_x = 0.1 
        sub.prop(context.scene.world, "horizon_color", "")
                       
        box.separator() 

        if tp.display_world: 
            
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
    

    #box.separator()

    row = box.row()
    row.prop(context.space_data, "show_floor", text="Grid Floor")#, icon ="GRID")  

    if context.space_data.show_floor:  

        if tp.display_grid:            
            row.prop(tp, "display_grid", text="", icon="TRIA_UP_BAR")
        else:
            row.prop(tp, "display_grid", text="", icon="TRIA_DOWN_BAR")    

    sub = row.row(1)
    sub.scale_x = 0.156
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


