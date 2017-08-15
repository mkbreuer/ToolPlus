bl_info = {
    "name": "UV-Image Tool Pie Menu",
    "author": "MKB",
    "version": (1, 0),
    "blender": (2, 7, 8),
    "location": "Image Editor",
    "description": "Pie Menu for UV-Image Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}




import bpy, os
from bpy import *
from bpy.props import *
from rna_prop_ui import PropertyPanel
from bpy.types import Menu, Operator



class VIEW3D_TP_UV_EditSpace_Pie(Menu):
    bl_label = "T+ UV"
    bl_idname = "tp_pie.uv_editspace" 
   
    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return sima.show_uvedit and not context.tool_settings.use_uv_sculpt

    def draw(self, context):
        layout = self.layout
        wm = bpy.context.window_manager
        scn = context.scene
        
        icons = icon_collections["main"]
        
        toolsettings = context.tool_settings
        settings = context.tool_settings
	
        #row.operator_context = 'INVOKE_REGION_WIN'
        
        pie = layout.menu_pie()


#Box1_Left 

        box = pie.split().box().column()
        box.scale_x = 0.9 
        
        row = box.row(1)

        button_edit_weld = icons.get("icon_edit_weld")                                            
        row.operator("uv.weld", text=" ", icon_value=button_edit_weld.icon_id)   

        button_edit_stitch = icons.get("icon_edit_stitch")                    
        row.operator("uv.stitch", text=" ", icon_value=button_edit_stitch.icon_id)    
                    
        row = box.row(1)
        
        button_edit_join = icons.get("icon_edit_join")                
        row.operator("uv.uv_face_join", text=" ", icon_value=button_edit_join.icon_id) 

        button_edit_rip = icons.get("icon_edit_rip")            
        row.operator("uv.uv_face_rip", text=" ", icon_value=button_edit_rip.icon_id)

        row = box.row(1) 
        
        button_edit_seams = icons.get("icon_edit_seams")               
        row.operator("uv.mark_seam", text=" ", icon_value=button_edit_seams.icon_id)

        button_edit_seams_island = icons.get("icon_edit_seams_island")                                        
        row.operator("uv.seams_from_islands", text=" ", icon_value=button_edit_seams_island.icon_id)  

        row = box.row(1)
       
        row.operator("uv.pin", text=" ", icon="UNPINNED").clear=True                                    
        row.operator("uv.pin", text=" ", icon="PINNED").clear=False 
                
        row = box.row(1)

        button_uv_show_stretch = icons.get("icon_uv_show_stretch")   
        row.prop(context.space_data.uv_editor, "show_stretch",text=" ", icon_value=button_uv_show_stretch.icon_id)   

        button_uv_stretch = icons.get("icon_uv_stretch")   
        row.operator("uv.minimize_stretch", text=" ", icon_value=button_uv_stretch.icon_id)   



#Box2_Right

        box = pie.split().box().column()
        box.scale_x = 0.55        
        
        row = box.row(1)
        row.operator("tp_ops.pivot_bounding_box", " ", icon="ROTATE")
        row.operator("tp_ops.pivot_3d_cursor", " ", icon="CURSOR")
        row.operator("tp_ops.pivot_median", " ", icon="ROTATECENTER")
        row.operator("tp_ops.pivot_individual", " ", icon="ROTATECOLLECTION")
                    
        row = box.row(1)
        row.operator("tp_ops.mode_vertex", " ", icon="UV_VERTEXSEL")    
        row.operator("tp_ops.mode_edge", " ", icon="UV_EDGESEL")    
        row.operator("tp_ops.mode_face", " ", icon="UV_FACESEL") 
        row.operator("tp_ops.mode_island", " " , icon="UV_ISLANDSEL")    
                
        row = box.row(1)
        row.prop(toolsettings, "use_uv_select_sync", text="sync")              
        row.template_edit_mode_selection()
        
        #row.prop(uvedit, "show_stretch", text="", icon ='MOD_TRIANGULATE')  
        #row.prop(uvedit, "sticky_select_mode", icon_only=True)                               

        row = box.row()
        
        snap_meta = toolsettings.use_snap            
        if snap_meta == False:
            row.operator("wm.context_toggle", text=" ", icon="SNAP_OFF").data_path = "tool_settings.use_snap"
        else: 
            row.operator("wm.context_toggle", text=" ", icon="SNAP_ON").data_path = "tool_settings.use_snap"              

        row.operator("tp_ops.snap_vertex", " ", icon = "SNAP_VERTEX") 
        row.operator("tp_ops.snap_increment", " ", icon = "SNAP_INCREMENT")         

                
        row = box.row()             
        toolsettings = context.tool_settings            
        row.prop(toolsettings, "proportional_edit", icon_only=True)
        row.prop(toolsettings, "proportional_edit_falloff", icon_only=True) 
        
        mesh = context.edit_object.data
        row.prop_search(mesh.uv_textures, "active", mesh, "uv_textures", text="")          


#Box3_Bottom

        box = pie.split().box().column()
        #box.scale_x = 1

        row = box.row(1)

        button_align_scale_eq = icons.get("icon_align_scale_eq")                       
        row.operator("uv.equalize_scale", text=" ", icon_value=button_align_scale_eq.icon_id)
   
        button_align_vertical_center = icons.get("icon_align_vertical_center") 
        row.operator("uv.align_horizontal_axis", text=" ", icon_value=button_align_vertical_center.icon_id)

        button_align_bottom = icons.get("icon_align_bottom")
        row.operator("uv.align_low_margin", text=" ", icon_value=button_align_bottom.icon_id)  

        button_align_right = icons.get("icon_align_right")
        row.operator("uv.align_right_margin", text=" ", icon_value=button_align_right.icon_id)  


        row = box.row(1)

        row.operator("uv.average_islands_scale", text=" ", icon = "MAN_SCALE")  
       
        button_align_horizontal_center = icons.get("icon_align_horizontal_center")
        row.operator("uv.align_vertical_axis", text=" ", icon_value=button_align_horizontal_center.icon_id) 
 
        button_align_top = icons.get("icon_align_top")
        row.operator("uv.align_top_margin" , text=" ", icon_value=button_align_top.icon_id)

        button_align_left = icons.get("icon_align_left")
        row.operator("uv.align_left_margin" , text=" ", icon_value=button_align_left.icon_id)


        row = box.row(1)
 
        button_distribute_vertical = icons.get("icon_distribute_vertical")
        row.operator("uv.equalize_vertical_gap", text=' ', icon_value=button_distribute_vertical.icon_id)

        button_distribute_heights = icons.get("icon_distribute_heights")
        row.operator("uv.distribute_center_vertically", text=' ', icon_value=button_distribute_heights.icon_id)  

        button_distribute_down = icons.get("icon_distribute_down")
        row.operator("uv.distribute_bedges_vertically", text=' ', icon_value=button_distribute_down.icon_id)

        button_distribute_right = icons.get("icon_distribute_right")
        row.operator("uv.distribute_redges_horizontally", text=' ', icon_value=button_distribute_right.icon_id) 


        row = box.row(1)

        button_distribute_horizontal = icons.get("icon_distribute_horizontal")
        row.operator("uv.equalize_horizontal_gap", text=' ', icon_value=button_distribute_horizontal.icon_id)

        button_distribute_widths = icons.get("icon_distribute_widths")
        row.operator("uv.distribute_center_horizontally", text=' ', icon_value=button_distribute_widths.icon_id)

        button_distribute_up = icons.get("icon_distribute_up")
        row.operator("uv.distribute_tedges_vertically", text=' ', icon_value=button_distribute_up.icon_id)

        button_distribute_left = icons.get("icon_distribute_left")              
        row.operator("uv.distribute_ledges_horizontally", text=' ', icon_value=button_distribute_left.icon_id)



#Box4_Top

        box = pie.split().box().column()
        box.scale_x = 0.75  
        
        row = box.row(1)
        row.alignment = 'CENTER'
        row.scale_x = 1.55

        #row.operator("uv.export_layout", text=" ", icon = "IMASEL")
        button_select_box = icons.get("icon_select_box")   
        row.operator("uv.select_border", text=" ", icon_value=button_select_box.icon_id).pinned=False        

        row.operator("ed.undo", text="", icon="LOOP_BACK") 
        row.menu("IMAGE_MT_uvs_showhide","", icon="VISIBLE_IPO_ON")        
        row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                 
        
        row.operator("ed.undo_history", text=" ", icon = "LOAD_FACTORY")        
                
        row = box.row(1)                

        button_select_all = icons.get("icon_select_all")   
        row.operator("uv.select_all", text=" ", icon_value=button_select_all.icon_id).action='SELECT'

        button_select_invert = icons.get("icon_select_invert")   
        row.operator("uv.select_all", text=" ", icon_value=button_select_invert.icon_id).action='INVERT'

        button_select_link = icons.get("icon_select_link")   
        row.operator("uv.select_linked", text=" ", icon_value=button_select_link.icon_id)

        button_select_pinned = icons.get("icon_select_pinned")   
        row.operator("uv.select_pinned", text=" ", icon_value=button_select_pinned.icon_id)

        button_select_split = icons.get("icon_select_split")   
        row.operator("uv.select_split", text=" ", icon_value=button_select_split.icon_id)    
   


#Box5_Top_Left

        box = pie.split().box().column()
        #box.scale_x = 1
        
        row = box.row(1)
        #row.scale_x = 0.9
      
        button_uv_mirror = icons.get("icon_uv_mirror")           
        row.operator("mesh.faces_mirror_uv", text=" ", icon_value=button_uv_mirror.icon_id)

        button_mirror_y = icons.get("icon_mirror_y")
        row.operator("uv.rotateoneeighty", text=" ", icon_value=button_mirror_y.icon_id)    

        button_mirror_x = icons.get("icon_mirror_x")
        row.operator("transform.mirror", text=" ", icon_value=button_mirror_x.icon_id).constraint_axis=(True, False, False)
     
        row = box.row(1)    
              
        button_rotation_one_eighty = icons.get("icon_rotation_one_eighty")           
        row.operator("uv.align_rotation", text=" ", icon_value=button_rotation_one_eighty.icon_id)           

        button_rotation_minus_ninety = icons.get("icon_rotation_minus_ninety")           
        row.operator("uv.rotatednineminus", text=" ", icon_value=button_rotation_minus_ninety.icon_id)              

        button_rotation_plus_ninety = icons.get("icon_rotation_plus_ninety")
        row.operator("uv.rotatednine", text=" ", icon_value=button_rotation_plus_ninety.icon_id) 



#Box6_Top_Right 

        box = pie.split().box().column()
        box.scale_x = 1.05
        
        row = box.row(1)
        #row.scale_x = 0.9
        #row.menu("View_Custom_Menu", text = "Editor View", icon = "PLUG" )        
        row.operator("screen.screen_full_area", text = "FSc ", icon = "FULLSCREEN_ENTER") 
        row.operator("screen.screen_full_area", text = "FW  ", icon = "FULLSCREEN_ENTER").use_hide_panels = True        
        
        row = box.row(1)        
        row.prop(toolsettings, "use_uv_sculpt")


#Box7_Bottom_Left


        box = pie.split().box().column()
        #box.scale_x = 1.05
        
        row = box.row(1)
        #row.scale_x = 0.9


        button_snap_grid_noneq = icons.get("icon_snap_grid_noneq")
        row.operator("uv.uv_squares_by_shape", text=" ", icon_value=button_snap_grid_noneq.icon_id)

        button_snap_grid_eq = icons.get("icon_snap_grid_eq")
        row.operator("uv.uv_squares", text=" ", icon_value=button_snap_grid_eq.icon_id)

        button_snap_grid_pack = icons.get("icon_snap_grid_pack")
        row.operator("uv.pack_islands", text=" ", icon_value=button_snap_grid_pack.icon_id)

        row = box.row(1)   

        button_uv_reset = icons.get("icon_uv_reset")   
        row.operator("uv.reset", text=" ", icon_value=button_uv_reset.icon_id)   
      
        row.operator("uv.unwrap", text= " ", icon = "GROUP_UVS")

        button_edit_remove = icons.get("icon_edit_remove")                               
        row.operator("uv.remove_doubles", text=" ", icon_value=button_edit_remove.icon_id) 









#Box8_Bottom_Right

        box = pie.split().box().column()
        #box.scale_x = 1.1
        
        row = box.row(1)
        #row.scale_x = 0.9

        button_align_y_axis = icons.get("icon_align_y_axis")
        row.operator("uv.align", text=" ", icon_value=button_align_y_axis.icon_id).axis='ALIGN_X'
        
        button_align_x_axis = icons.get("icon_align_x_axis")
        row.operator("uv.align", text=" ", icon_value=button_align_x_axis.icon_id).axis='ALIGN_Y'

        row.operator("uv.align", text=" ", icon ="AUTO").axis='ALIGN_AUTO'

        row = box.row(1)

        button_straighten_y = icons.get("icon_straighten_y")
        row.operator("uv.align", text=" ", icon_value=button_straighten_y.icon_id).axis='ALIGN_T'

        button_straighten_x = icons.get("icon_straighten_x")
        row.operator("uv.align", text=" ", icon_value=button_straighten_x.icon_id).axis='ALIGN_U'

        row.operator("uv.align", text=" ", icon ="AUTO").axis='ALIGN_S'






      
class VIEW3D_TP_UV_Sculpt_Pie(Menu):
    bl_label = "T+ UV"
    bl_idname = "tp_pie.uv_sculpt" 
    
    def draw(self, context):
        layout = self.layout        
        
        toolsettings = context.tool_settings
        uvsculpt = toolsettings.uv_sculpt
        brush = uvsculpt.brush

        settings = context.tool_settings
	
        #row.operator_context = 'INVOKE_REGION_WIN'
        
        pie = layout.menu_pie()
        

#Box1_Left

        box = pie.split().box().column()
        box.scale_x = 1
                
        row = box.row(1)
        row.prop(uvsculpt, "show_brush")

        row = box.row(1)
        row.prop(toolsettings, "uv_sculpt_lock_borders")

        row = box.row(1)
        row.prop(toolsettings, "uv_sculpt_all_islands")
        


#Box2_Right

        box = pie.split().box().column()
        box.scale_x = 1
        
        row = box.row(1)
        #row.scale_x = 1.55          

        row.prop(toolsettings, "use_uv_sculpt")
        
        row = box.row(1)
        
        
        row.prop(toolsettings, "uv_sculpt_tool","")
        
        if toolsettings.uv_sculpt_tool == 'RELAX':
            row = box.row(1)
            row.prop(toolsettings, "uv_relax_method","")
        
 

#Box3_Bottom

        box = pie.split().box().column()
        box.scale_x = 0.65
        
        row = box.row(1)
        #row.scale_x = 1.55   
        
        row = box.row(1)
        row.scale_x = 1.55        
        upr = context.tool_settings.unified_paint_settings 
        row.prop(upr, "size", text="Radius", slider=False)         
        row.prop(upr, "use_pressure_size", text="") 


        row = box.row(1)
        row.scale_x = 1.55
        ups = context.tool_settings.uv_sculpt.brush             
        row.prop(ups, "strength", text="Strength", slider=False) 
        row.prop(upr, "use_pressure_strength", text="") 



#Box4_Top 
        
        box = pie.split().box().column()

        row = box.row(1)
        row.alignment ='CENTER'
        row.scale_x = 1.55              
        
        row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER").use_hide_panels = True                     
        row.operator("ed.redo", text="", icon="LOOP_FORWARDS")            
        row.operator("uv.select_border", text="", icon='BORDER_RECT')                                     
        row.operator("ed.undo", text="", icon="LOOP_BACK")                                                                     
        row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")     


        row = box.row(1)
        row.alignment ='CENTER'

        row.scale_y = 1.25             

        row.operator("brush.curve_preset", icon='SMOOTHCURVE', text=" ").shape = 'SMOOTH'
        row.operator("brush.curve_preset", icon='SPHERECURVE', text=" ").shape = 'ROUND'
        row.operator("brush.curve_preset", icon='ROOTCURVE', text=" ").shape = 'ROOT'
        row.operator("brush.curve_preset", icon='SHARPCURVE', text=" ").shape = 'SHARP'
        row.operator("brush.curve_preset", icon='LINCURVE', text=" ").shape = 'LINE'
        row.operator("brush.curve_preset", icon='NOCURVE', text=" ").shape = 'MAX'   






# Registry 

icon_collections = {}

def register_icons():
    import bpy.utils.previews
    
    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    mkb_icons.load("my_image1", os.path.join(icons_dir, "icon_image1.png"), 'IMAGE')
    mkb_icons.load("my_image2", os.path.join(icons_dir, "icon_image2.png"), 'IMAGE')

    mkb_icons.load("icon_triangle_left", os.path.join(icons_dir, "triangle_left.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_right", os.path.join(icons_dir, "triangle_right.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_up", os.path.join(icons_dir, "triangle_up.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_down", os.path.join(icons_dir, "triangle_down.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_left_up", os.path.join(icons_dir, "triangle_corner_left_up.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_right_up", os.path.join(icons_dir, "triangle_corner_right_up.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_left_down", os.path.join(icons_dir, "triangle_corner_left_down.png"), 'IMAGE')
    mkb_icons.load("icon_triangle_corner_right_down", os.path.join(icons_dir, "triangle_corner_right_down.png"), 'IMAGE')

    mkb_icons.load("icon_align_bottom", os.path.join(icons_dir, "align_bottom.png"), 'IMAGE')
    mkb_icons.load("icon_align_horizontal_center", os.path.join(icons_dir, "align_horizontal_center.png"), 'IMAGE')
    mkb_icons.load("icon_align_left", os.path.join(icons_dir, "align_left.png"), 'IMAGE')
    mkb_icons.load("icon_align_right", os.path.join(icons_dir, "align_right.png"), 'IMAGE')
    mkb_icons.load("icon_align_scale_eq", os.path.join(icons_dir, "align_scale_eq.png"), 'IMAGE')
    mkb_icons.load("icon_align_top", os.path.join(icons_dir, "align_top.png"), 'IMAGE')
    mkb_icons.load("icon_align_vertical_center", os.path.join(icons_dir, "align_vertical_center.png"), 'IMAGE')

    mkb_icons.load("icon_align_x_axis", os.path.join(icons_dir, "align_x_axis.png"), 'IMAGE')
    mkb_icons.load("icon_align_y_axis", os.path.join(icons_dir, "align_y_axis.png"), 'IMAGE')

    mkb_icons.load("icon_distribute_down", os.path.join(icons_dir, "distribute_down.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_heights", os.path.join(icons_dir, "distribute_heights.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_horizontal", os.path.join(icons_dir, "distribute_horizontal.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_left", os.path.join(icons_dir, "distribute_left.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_right", os.path.join(icons_dir, "distribute_right.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_up", os.path.join(icons_dir, "distribute_up.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_vertical", os.path.join(icons_dir, "distribute_vertical.png"), 'IMAGE')
    mkb_icons.load("icon_distribute_widths", os.path.join(icons_dir, "distribute_widths.png"), 'IMAGE')
    
    mkb_icons.load("icon_edit_join", os.path.join(icons_dir, "edit_join.png"), 'IMAGE')
    mkb_icons.load("icon_edit_match", os.path.join(icons_dir, "edit_match.png"), 'IMAGE')
    mkb_icons.load("icon_edit_remove", os.path.join(icons_dir, "edit_remove.png"), 'IMAGE')
    mkb_icons.load("icon_edit_rip", os.path.join(icons_dir, "edit_rip.png"), 'IMAGE')
    mkb_icons.load("icon_edit_seams", os.path.join(icons_dir, "edit_seams.png"), 'IMAGE')
    mkb_icons.load("icon_edit_seams_island", os.path.join(icons_dir, "edit_seams_island.png"), 'IMAGE')
    mkb_icons.load("icon_edit_stitch", os.path.join(icons_dir, "edit_stitch.png"), 'IMAGE')
    mkb_icons.load("icon_edit_weld", os.path.join(icons_dir, "edit_weld.png"), 'IMAGE')

    mkb_icons.load("icon_mirror_x", os.path.join(icons_dir, "mirror_x.png"), 'IMAGE')
    mkb_icons.load("icon_mirror_y", os.path.join(icons_dir, "mirror_y.png"), 'IMAGE')

    mkb_icons.load("icon_rotation_minus_ninety", os.path.join(icons_dir, "rotation_minus_ninety.png"), 'IMAGE')
    mkb_icons.load("icon_rotation_one_eighty", os.path.join(icons_dir, "rotation_one_eighty.png"), 'IMAGE')
    mkb_icons.load("icon_rotation_plus_ninety", os.path.join(icons_dir, "rotation_plus_ninety.png"), 'IMAGE')

    mkb_icons.load("icon_select_all", os.path.join(icons_dir, "select_all.png"), 'IMAGE')
    mkb_icons.load("icon_select_box", os.path.join(icons_dir, "select_box.png"), 'IMAGE')
    mkb_icons.load("icon_select_invert", os.path.join(icons_dir, "select_invert.png"), 'IMAGE')
    mkb_icons.load("icon_select_link", os.path.join(icons_dir, "select_link.png"), 'IMAGE')
    mkb_icons.load("icon_select_pinned", os.path.join(icons_dir, "select_pinned.png"), 'IMAGE')
    mkb_icons.load("icon_select_split", os.path.join(icons_dir, "select_split.png"), 'IMAGE')

    mkb_icons.load("icon_snap_grid_eq", os.path.join(icons_dir, "snap_grid_eq.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid_noneq", os.path.join(icons_dir, "snap_grid_noneq.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid_pack", os.path.join(icons_dir, "snap_grid_pack.png"), 'IMAGE')

    mkb_icons.load("icon_straighten_x", os.path.join(icons_dir, "straighten_x.png"), 'IMAGE')
    mkb_icons.load("icon_straighten_y", os.path.join(icons_dir, "straighten_y.png"), 'IMAGE')

    mkb_icons.load("icon_uv_mirror", os.path.join(icons_dir, "uv_mirror.png"), 'IMAGE')
    mkb_icons.load("icon_uv_reset", os.path.join(icons_dir, "uv_reset.png"), 'IMAGE')
    mkb_icons.load("icon_uv_show_stretch", os.path.join(icons_dir, "uv_show_stretch.png"), 'IMAGE')
    mkb_icons.load("icon_uv_stretch", os.path.join(icons_dir, "uv_stretch.png"), 'IMAGE')

    
    icon_collections['main'] = mkb_icons

    bpy.utils.register_class(VIEW3D_TP_UV_EditSpace_Pie)    
    bpy.utils.register_class(VIEW3D_TP_UV_Sculpt_Pie) 
    #bpy.utils.unregister_module(__name__)


def unregister_icons():
    for icon in icon_collections.values():
        bpy.utils.previews.remove(icon)
    icon_collections.clear() 

    bpy.utils.unregister_class(VIEW3D_TP_UV_EditSpace_Pie)    
    bpy.utils.unregister_class(VIEW3D_TP_UV_Sculpt_Pie) 
    #bpy.utils.unregister_module(__name__)
   

#if __name__ == "__main__":
    #register()
