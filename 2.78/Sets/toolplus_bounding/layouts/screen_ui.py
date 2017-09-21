import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons


def draw_screen_layout(context, layout):
    icons = load_icons()
    
    wm = context.window_manager 
    view = context.space_data
    ob = context.object  
    obj = context.object
    scene = context.scene
    scn = context.scene
    rs = bpy.context.scene 
    gs = scene.game_settings


    box = layout.box().column(1) 

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
    
    box = layout.box().column(1)  

    row = box.column(1)
    row.prop(context.space_data, "lens")

    box.separator() 
    
    row = box.column(1)
    row.prop(context.space_data, "clip_start", text="ClipStart")
    row.prop(context.space_data, "clip_end", text="ClipEnd")

    box.separator()

    box = layout.box().column(1)      
        
    row = box.row()             
    row.alignment = 'CENTER'
    row.label("Fast HighRes Navigation", icon = "MOD_SOFT") 
 
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