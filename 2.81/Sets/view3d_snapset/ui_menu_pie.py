# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  
from .ui_utils import get_addon_prefs

# ADDON CHECK #
import addon_utils   
from . ui_utils import addon_exists

class VIEW3D_MT_snapset_menu_pencil(bpy.types.Menu):
    bl_label = "Annotate"
    bl_idname = "VIEW3D_MT_snapset_menu_pencil"

    def draw(self, context):
        layout = self.layout
      
        icons = load_icons()  
        
        icon_snap_annotate = icons.get("icon_snap_annotate")
        layout.operator("wm.tool_set_by_id", text="Free", icon_value=icon_snap_annotate.icon_id).name = "builtin.annotate"

        icon_snap_annotate_line = icons.get("icon_snap_annotate_line")
        layout.operator("wm.tool_set_by_id", text="Line", icon_value=icon_snap_annotate_line.icon_id).name = "builtin.annotate_line"

        icon_snap_annotate_polygon = icons.get("icon_snap_annotate_polygon")
        layout.operator("wm.tool_set_by_id", text="Polygon", icon_value=icon_snap_annotate_polygon.icon_id).name = "builtin.annotate_polygon"

        icon_snap_annotate_eraser = icons.get("icon_snap_annotate_eraser")
        layout.operator("wm.tool_set_by_id", text="Eraser", icon_value=icon_snap_annotate_eraser.icon_id).name = "builtin.annotate_eraser"

        layout.separator()
        
        layout.operator("gpencil.data_add", text="Add Layer", icon="ADD")
        layout.operator("gpencil.layer_remove", text="Remove Layer", icon="REMOVE")

        layout.separator()

        layout.operator("gpencil.data_unlink", text="Data Unlink", icon="UNLINKED")



# UI: HOTKEY MENU PIE # 
class VIEW3D_MT_snapset_menu_pie(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_snapset_menu_pie"

    def draw(self, context):
        layout = self.layout
       
        addon_prefs = get_addon_prefs()

        icons = load_icons()  

        layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()      

        #Box 1 L
        row = pie.split().column()
        row.scale_x = addon_prefs.ui_scale_x_b1       
        row.scale_y = addon_prefs.ui_scale_y_b1       

        if addon_prefs.tpc_use_active_pie == True:
            if addon_prefs.use_internal_icon_btd == True:
                row.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon=addon_prefs.icon_btd) 
            else:
                icon_snap_active = icons.get("icon_snap_active")            
                row.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon_value=icon_snap_active.icon_id) 

        if addon_prefs.tpc_use_closest_pie == True:
            if addon_prefs.use_internal_icon_bte == True:
                row.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon=addon_prefs.icon_bte)
            else:           
                icon_snap_closest = icons.get("icon_snap_closest")
                row.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon_value=icon_snap_closest.icon_id)
             
        
        #Box 2 R
        row = pie.split().column()
        row.scale_x = addon_prefs.ui_scale_x_b2   
        row.scale_y = addon_prefs.ui_scale_y_b2   

        if addon_prefs.tpc_use_cursor_pie == True:
            if addon_prefs.use_internal_icon_btc == True:     
                row.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon=addon_prefs.icon_btc) 
            else:       
                icon_snap_cursor = icons.get("icon_snap_cursor")           
                row.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon_value=icon_snap_cursor.icon_id) 
      
        if addon_prefs.tpc_use_custom_modal_pie == True:
            if addon_prefs.use_internal_icon_btM == True:     
                row.operator("tpc_ot.snapset_modal", text=addon_prefs.name_btM, icon=addon_prefs.icon_btM).mode = "CUSTOM"  
            else:       
                icon_snap_custom = icons.get("icon_snap_custom")             
                row.operator("tpc_ot.snapset_modal", text=addon_prefs.name_btM, icon_value=icon_snap_custom.icon_id).mode = "CUSTOM"  
           

        #Box 3 B
        box = pie.split().column(align = False)
        box.scale_x = addon_prefs.ui_scale_x_b3   
        box.scale_y = addon_prefs.ui_scale_y_b3   

        row = box.row(align = False)       

        if addon_prefs.tpc_use_center_modal_pie == True:       
            icon_snap_center = icons.get("icon_snap_center")
            row.operator("tpc_ot.snapset_modal", text="MidPoint*", icon_value=icon_snap_center.icon_id).mode = "CENTER"  
       
        if addon_prefs.tpc_use_perpendic_modal_pie == True:             
            icon_snap_perpendic = icons.get("icon_snap_perpendic")
            row.operator("tpc_ot.snapset_modal", text="Perpendic*", icon_value=icon_snap_perpendic.icon_id).mode = "PERPENDICULAR"  

        row = box.row(align = False)
 
        if addon_prefs.tpc_use_center_pie == True:   
            if addon_prefs.use_internal_icon_btg == True:
                row.operator("tpc_ot.snapset_button_g", text=addon_prefs.name_btg, icon=addon_prefs.icon_btg)
            else:           
                icon_snap_center = icons.get("icon_snap_center")
                row.operator("tpc_ot.snapset_button_g", text=addon_prefs.name_btg, icon_value=icon_snap_center.icon_id)

        if addon_prefs.tpc_use_perpendic_pie == True: 
            if addon_prefs.use_internal_icon_bth == True:
                row.operator("tpc_ot.snapset_button_h", text=addon_prefs.name_bth, icon=addon_prefs.icon_bth)
            else:           
                icon_snap_perpendic = icons.get("icon_snap_perpendic")
                row.operator("tpc_ot.snapset_button_h", text=addon_prefs.name_bth, icon_value=icon_snap_perpendic.icon_id)
             
       
        # ADDON CHECK #
        if context.mode == 'OBJECT':
            
            if addon_prefs.toggle_addon_align_tools == True:   

                align_addon = "space_view3d_align_tools" 
                align_state = addon_utils.check(align_addon)
                if not align_state[0]:   
                    box.separator()                  
                    
                    row = box.row(align = False)
                    row.operator_context = 'INVOKE_REGION_WIN'
                    row.operator("preferences.addon_show", text="", icon="FRAME_NEXT").module="space_view3d_align_tools"                  
                    row.operator("tpc_ot.activate_align_tools", text="Activate: Align Tools", icon="ERROR")              

                else:  

                    box.separator()  

                    if addon_prefs.toggle_align_tools_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Align Location:")
                        row = box.column_flow(columns=4, align=True)
                    else:
                        row = box.column_flow(columns=5, align=True)                        
                        row.label(text="Loc:")
               
                    row.operator("object.align_location_x", text="X")
                    row.operator("object.align_location_y", text="Y")
                    row.operator("object.align_location_z", text="Z")
                    row.operator("object.align_location_all", text="All")


                    if addon_prefs.toggle_align_tools_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Align Rotation:")
                        row = box.column_flow(columns=4, align=True)
                    else:
                        row = box.column_flow(columns=5, align=True)                        
                        row.label(text="Rot:")
                        
                    row.operator("object.align_rotation_x", text="X")
                    row.operator("object.align_rotation_y", text="Y")
                    row.operator("object.align_rotation_z", text="Z")
                    row.operator("object.align_rotation_all", text="All")


                    if addon_prefs.toggle_align_tools_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Align Scale:")
                        row = box.column_flow(columns=4, align=True)
                    else:
                        row = box.column_flow(columns=5, align=True)                        
                        row.label(text="Scl:")

                    row.operator("object.align_objects_scale_x", text="X")
                    row.operator("object.align_objects_scale_y", text="Y")
                    row.operator("object.align_objects_scale_z", text="Z")
                    row.operator("object.align_objects_scale_all", text="All")
                
                    box.separator() 

                    if addon_prefs.toggle_align_tools_compact == False:  
                        row = box.row(align = True)
                        row.label(text="Align Tools:")

                    row = box.row(align = False)
                    if bpy.context.active_object is not None:
                        row.operator("object.align_tools", text="Advanced")
                    else:
                        row.label(text="No Selection!")                                  
                    row.operator("object.align", text="Loc + Rot: XYZ")
                  

                    if addon_prefs.toggle_mirror_func == True:                         

                        box.separator() 
                    
                        row = box.row(align=True)        
                        row.operator_context = 'EXEC_REGION_WIN'       
                        
                        props = row.operator('transform.mirror', text="X-Mirror")
                        props.orient_type=addon_prefs.orient
                        props.constraint_axis=(True, False, False)

                        props = row.operator('transform.mirror', text="Y-Mirror")
                        props.orient_type=addon_prefs.orient
                        props.constraint_axis=(False, True, False)

                        props = row.operator('transform.mirror', text="Z-Mirror")
                        props.orient_type=addon_prefs.orient
                        props.constraint_axis=(False, False, True)
                        
                        row = box.row(align=True)
                        row.label(text="Mirror Orientation")     
                        row.prop(addon_prefs, 'orient', text="")   



        if context.mode == 'EDIT_MESH':
            
            if addon_prefs.toggle_addon_alignmesh == False and addon_prefs.toggle_addon_looptools == True: 

                looptools_addon = "mesh_looptools" 
                looptools_state = addon_utils.check(looptools_addon)
                if not looptools_state[0]:
                    box.separator()  

                    row = box.row(align=True)
                    row.operator_context = 'INVOKE_REGION_WIN'
                    row.operator("preferences.addon_show", text="", icon="FRAME_NEXT").module="mesh_looptools"         
                    row.operator("tpc_ot.activate_looptools", text="Activate: LoopTools", icon="ERROR")
                else:   
                    box.separator()  

                    icon_align_looptools = icons.get("icon_align_looptools")   
                    row = box.row(align=True)                    
                    if addon_prefs.toggle_looptools_menu_type == False:                        
                        row.menu("VIEW3D_MT_edit_mesh_looptools", text="LoopTools", icon_value=icon_align_looptools.icon_id)
                    else:
                        row.popover(panel="VIEW3D_PT_tools_looptools", text="LoopTools", icon_value=icon_align_looptools.icon_id)
 
          
            if addon_prefs.toggle_addon_alignmesh == False and addon_prefs.toggle_mirror_func == True: 

                    box.separator() 
                
                    row = box.row(align=True)        
                    row.operator_context = 'EXEC_REGION_WIN'       
                    
                    props = row.operator('transform.mirror', text="X-Mirror")
                    props.orient_type=addon_prefs.orient
                    props.constraint_axis=(True, False, False)

                    props = row.operator('transform.mirror', text="Y-Mirror")
                    props.orient_type=addon_prefs.orient
                    props.constraint_axis=(False, True, False)

                    props = row.operator('transform.mirror', text="Z-Mirror")
                    props.orient_type=addon_prefs.orient
                    props.constraint_axis=(False, False, True)
                    
                    row = box.row(align=True)
                    row.label(text="Mirror Orientation")     
                    row.prop(addon_prefs, 'orient', text="")  


           
            if addon_prefs.toggle_addon_alignmesh == True:  

                alignmesh_addon = "view3d_alignmesh" 
                alignmesh_state = addon_utils.check(alignmesh_addon)
                if not alignmesh_state[0]:
                    box.separator()  

                    row = box.row(align=True)
                    row.operator_context = 'INVOKE_REGION_WIN'
                    row.operator("preferences.addon_show", text="", icon="FRAME_NEXT").module="view3d_alignmesh"                  
                    row.operator("tpc_ot.activate_align_mesh", text="Activate: Mesh Align", icon="ERROR") 
                else:  
 
                    box.separator()  
                   
                    if addon_prefs.toggle_alignmesh_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Align to Axis: 0")

                    row = box.row(align=True)

                    button_align_x = icons.get("icon_align_x") 
                    props = row.operator("tpc_ops.align_mesh", text="X", icon_value=button_align_x.icon_id)
                    props.use_align_axis='axis_x'
                    props.set_pivot='ACTIVE_ELEMENT'

                    button_align_y = icons.get("icon_align_y")
                    props = row.operator("tpc_ops.align_mesh",text="Y", icon_value=button_align_y.icon_id)
                    props.use_align_axis='axis_y'
                    props.set_pivot='ACTIVE_ELEMENT'

                    button_align_z = icons.get("icon_align_z")
                    props = row.operator("tpc_ops.align_mesh",text="Z", icon_value=button_align_z.icon_id)
                    props.use_align_axis='axis_z'   
                    props.set_pivot='ACTIVE_ELEMENT'

                    row = box.row(align=True)

                    button_align_xy = icons.get("icon_align_xy") 
                    props = row.operator("tpc_ops.align_mesh", text="Xy", icon_value=button_align_xy.icon_id)
                    props.use_align_axis='axis_xy'
                    props.set_pivot='ACTIVE_ELEMENT'

                    button_align_zy = icons.get("icon_align_zy") 
                    props = row.operator("tpc_ops.align_mesh", text="Zy", icon_value=button_align_zy.icon_id)
                    props.use_align_axis='axis_zy'
                    props.set_pivot='ACTIVE_ELEMENT'

                    button_align_zx = icons.get("icon_align_zx")
                    props = row.operator("tpc_ops.align_mesh", text="Zx", icon_value=button_align_zx.icon_id)
                    props.use_align_axis='axis_zx'
                    props.set_pivot='ACTIVE_ELEMENT'    

                    box.separator()   
                 
                    if addon_prefs.toggle_alignmesh_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Align & Distribute:")

                    row = box.row(align=True)

                    icon_align_straigten = icons.get("icon_align_straigten") 
                    row.operator('tpc_ot.vertex_align', text="Straight", icon_value=icon_align_straigten.icon_id)

                    icon_align_distribute = icons.get("icon_align_distribute") 
                    row.operator('tpc_ot.vertex_distribute', text="Evenly", icon_value=icon_align_distribute.icon_id)

                    icon_align_both = icons.get("icon_align_both") 
                    row.operator('tpc_ot.vertex_inline', text="Both", icon_value=icon_align_both.icon_id)

                    if addon_prefs.toggle_alignmesh_compact == False:  
                        box.separator()                           
                        
                        row = box.row(align = False)
                        row.label(text="Align to active Normal & Mirror over Edge")

                    row = box.row(align=True)

                    button_align_n = icons.get("icon_align_n") 
                    props = row.operator("tpc_ops.align_mesh", text="Align to Normal", icon_value=button_align_n.icon_id)
                    props.use_align_axis='axis_n'
                    props.set_pivot='ACTIVE_ELEMENT'
                  
                    row.operator("tpc_ot.mirror_over_edge", text="Edge Mirror", icon='ARROW_LEFTRIGHT')
                    
                    if addon_prefs.toggle_mirror_func == True:                         
                    
                        row = box.row(align=True)        
                        row.operator_context = 'EXEC_REGION_WIN'       
                        
                        props = row.operator('transform.mirror', text="X-Mirror")
                        props.orient_type=addon_prefs.orient
                        props.constraint_axis=(True, False, False)

                        props = row.operator('transform.mirror', text="Y-Mirror")
                        props.orient_type=addon_prefs.orient
                        props.constraint_axis=(False, True, False)

                        props = row.operator('transform.mirror', text="Z-Mirror")
                        props.orient_type=addon_prefs.orient
                        props.constraint_axis=(False, False, True)
                        
                        row = box.row(align=True)
                        row.label(text="Mirror Orientation")     
                        row.prop(addon_prefs, 'orient', text="")     

                    box.separator()  

                    if addon_prefs.toggle_alignmesh_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Relax & LoopTools")
            
                    row = box.row(align=True)

                    icon_align_vertices = icons.get("icon_align_vertices") 
                    props = row.operator('mesh.vertices_smooth', text="SVerts", icon_value=icon_align_vertices.icon_id)
                    props.factor=0.5
                    props.repeat=1
                    props.xaxis=True
                    props.yaxis=True
                    props.zaxis=True

                    icon_align_smooth = icons.get("icon_align_smooth") 
                    row.operator('tpc_ot.shrinkwrap_smooth', text="SFaces", icon_value=icon_align_smooth.icon_id)
                                                       
                    if addon_prefs.toggle_addon_looptools == True: 

                        looptools_addon = "mesh_looptools" 
                        looptools_state = addon_utils.check(looptools_addon)
                        if not looptools_state[0]:
                            row.operator("preferences.addon_show", text="Activate: LoopTools", icon="ERROR").module="mesh_looptools"         
                        else:   
                            sub = row.row(align=True)
                            sub.scale_x = 0.945 

                            icon_align_looptools = icons.get("icon_align_looptools")                             
                            if addon_prefs.toggle_looptools_menu_type == False:                                                            
                                sub.menu("VIEW3D_MT_edit_mesh_looptools", text="LPTools", icon_value=icon_align_looptools.icon_id)
                            else:
                                sub.popover(panel="VIEW3D_PT_tools_looptools", text="LPTools", icon_value=icon_align_looptools.icon_id)        

                 
                    box.separator()       
                   
                    if addon_prefs.toggle_alignmesh_compact == False:  
                        row = box.row(align = False)
                        row.label(text="Modal: Linked Face")

                    row = box.row(align=True)

                    button_align_x = icons.get("icon_align_x") 
                    props = row.operator("tpc_ops.snapflat_modal", text="FX*", icon_value=button_align_x.icon_id)
                    props.mode='flatten_x'
                    props.mesh_select_mode=addon_prefs.mesh_select_mode

                    button_align_y = icons.get("icon_align_y")
                    props = row.operator("tpc_ops.snapflat_modal",text="FY*", icon_value=button_align_y.icon_id)
                    props.mode='flatten_y'
                    props.mesh_select_mode=addon_prefs.mesh_select_mode

                    button_align_z = icons.get("icon_align_z")
                    props = row.operator("tpc_ops.snapflat_modal",text="FZ*", icon_value=button_align_z.icon_id)
                    props.mode='flatten_z'
                    props.mesh_select_mode=addon_prefs.mesh_select_mode 
             
                    if addon_prefs.toggle_addon_looptools == True:  
                      
                        looptools_addon = "mesh_looptools" 
                        looptools_state = addon_utils.check(looptools_addon)
                        if not looptools_state[0]:
                            row.operator("preferences.addon_show", text="Activate: LoopTools", icon="ERROR").module="mesh_looptools"                  
                        else:   
              
                            row = box.row(align=True)
                            sub = row.row(align=True)
                            sub.scale_x = 1                            
                            icon_align_flatten = icons.get("icon_align_flatten") 
                            props = sub.operator("tpc_ops.snapflat_modal", text=" LPT Flatten*", icon_value=icon_align_flatten.icon_id)
                            props.mode='flatten_lpt'
                            props.mesh_select_mode=addon_prefs.mesh_select_mode
                            props.threshold=addon_prefs.threshold
                                                       
                            if addon_exists("view3d_alignmesh"):
                                from view3d_alignmesh.ui_utils import get_preferences
                                preference = get_preferences()                               
                               
                                sub1 = row.row(align=True)
                                sub1.scale_x = 0.75
                                sub1.prop(preference, "threshold", text="Threshold:")      


                            box.separator()   

                            if addon_prefs.toggle_alignmesh_compact == False:  
                                row = box.row(align = False)
                                row.label(text="Modal: Boundary Loops")
                            
                            row = box.row(align=True)  

                            props = row.operator("tpc_ops.snapflat_modal", text="Select*", icon='RESTRICT_SELECT_OFF')
                            props.mode='snap_for_select'                          
                            props.mesh_select_mode=addon_prefs.mesh_select_mode
                            props.threshold=addon_prefs.threshold

                            props = row.operator("tpc_ops.snapflat_modal", text="Seam*", icon='UV_FACESEL')
                            props.mode='snap_for_uvs'                          
                            props.mesh_select_mode=addon_prefs.mesh_select_mode
                            props.threshold=addon_prefs.threshold
                           
                            props = row.operator("tpc_ops.snapflat_modal", text="Sharp*", icon='SHADING_BBOX')                         
                            props.mode='snap_for_sharp'
                            props.mesh_select_mode=addon_prefs.mesh_select_mode
                            props.threshold=addon_prefs.threshold

                                                                  

                    if addon_exists("view3d_alignmesh"):
                        from view3d_alignmesh.ui_utils import get_preferences
                        preference = get_preferences()    
                        
                        box.separator()                       
                        
                        row = box.row(align = False)
                        row.label(text="Modals finish with:")     
                        row.prop_enum(preference, "mesh_select_mode", "vertices", text="", icon ='VERTEXSEL')  
                        row.prop_enum(preference, "mesh_select_mode", "edges", text="", icon ='EDGESEL')
                        row.prop_enum(preference, "mesh_select_mode", "faces", text="", icon ='FACESEL')



        #Box 4 T 
        box = pie.split().column(align = False)
        box.scale_x = addon_prefs.ui_scale_x_b4
        box.scale_y = addon_prefs.ui_scale_y_b4
        
        row = box.row(align = False)
        
        icon_snap_move = icons.get("icon_snap_move")
        row.operator("wm.tool_set_by_id", text=" ", icon_value=icon_snap_move.icon_id).name = "builtin.move"
        
        icon_snap_rotate = icons.get("icon_snap_rotate")                
        row.operator("wm.tool_set_by_id", text=" ", icon_value=icon_snap_rotate.icon_id).name = "builtin.rotate"

        icon_snap_scale = icons.get("icon_snap_scale")
        row.operator("wm.tool_set_by_id", text=" ", icon_value=icon_snap_scale.icon_id).name = "builtin.scale"

        icon_snap_measure = icons.get("icon_snap_measure")                
        row.operator("wm.tool_set_by_id", text=" ", icon_value=icon_snap_measure.icon_id).name = "builtin.measure"   
        
        icon_snap_annotate = icons.get("icon_snap_annotate")                
        row.menu("VIEW3D_MT_snapset_menu_pencil", text=" ", icon_value=icon_snap_annotate.icon_id) 
 
        row = box.row(align = False)      

        if bpy.context.scene.tool_settings.transform_pivot_point == 'BOUNDING_BOX_CENTER':   
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_BOUNDBOX", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="BOUNDING_BOX_CENTER"
        else:
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_BOUNDBOX").tpc_pivot="BOUNDING_BOX_CENTER"
            
        if bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':                   
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_CURSOR", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="CURSOR"
        else:
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_CURSOR").tpc_pivot="CURSOR"
        
        if bpy.context.scene.tool_settings.transform_pivot_point == 'ACTIVE_ELEMENT':              
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_ACTIVE", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="ACTIVE_ELEMENT"
        else:                
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_ACTIVE").tpc_pivot="ACTIVE_ELEMENT"

        if bpy.context.scene.tool_settings.transform_pivot_point == 'INDIVIDUAL_ORIGINS':               
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_INDIVIDUAL", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="INDIVIDUAL_ORIGINS"
        else:
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_INDIVIDUAL").tpc_pivot="INDIVIDUAL_ORIGINS"

        if bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':       
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_MEDIAN", emboss = addon_prefs.tpc_use_emposs).tpc_pivot="MEDIAN_POINT" 
        else:                
            row.operator("tpc_ot.set_pivot", text=" ", icon="PIVOT_MEDIAN").tpc_pivot="MEDIAN_POINT" 



        #Box 5 LT
        box = pie.split().column(align = False)
        box.scale_x = addon_prefs.ui_scale_x_b5
        box.scale_y = addon_prefs.ui_scale_y_b5

        tool_settings = context.tool_settings
        snap_items = bpy.types.ToolSettings.bl_rna.properties["snap_elements"].enum_items
        snap_elements = tool_settings.snap_elements
        if len(snap_elements) == 1:
            if snap_elements == {"INCREMENT"}:
                text = "Increment"
            if snap_elements == {"VERTEX"}:
                text = "Vertex"
            if snap_elements == {"EDGE"}:
                text = "Edge"
            if snap_elements == {"FACE"}:
                text = "Face"
            if snap_elements == {"VOLUME"}:
                text = "Volume"
            if snap_elements == {"EDGE_MIDPOINT"}:
                text = "MidPoint"
            if snap_elements == {"EDGE_PERPENDICULAR"}:
                text = "Perpendic"                         
          
            for elem in snap_elements:
                icon = snap_items[elem].icon
                break
        else:
            text = "Mix"
            icon = 'NONE'
        del snap_items, snap_elements

        if addon_prefs.tpc_show_snapping_panel == True:
            row = box.row(align = False)
            row.popover(panel="VIEW3D_PT_snapping", icon=icon, text=text)

        row = box.row(align = False)

        if bpy.context.scene.tool_settings.snap_elements == {'EDGE_MIDPOINT'}:            
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_MIDPOINT", emboss = addon_prefs.tpc_use_emposs).tpc_snape="EDGE_MIDPOINT"       
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_MIDPOINT").tpc_snape="EDGE_MIDPOINT"     

        if bpy.context.scene.tool_settings.snap_elements == {'FACE'}:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_FACE", emboss = addon_prefs.tpc_use_emposs).tpc_snape="FACE"
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_FACE").tpc_snape="FACE" 

        if bpy.context.scene.tool_settings.snap_elements == {'EDGE'}:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_EDGE", emboss = addon_prefs.tpc_use_emposs).tpc_snape="EDGE"        
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_EDGE").tpc_snape="EDGE"        

        if bpy.context.scene.tool_settings.snap_elements == {'VERTEX'}:            
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VERTEX", emboss = addon_prefs.tpc_use_emposs).tpc_snape="VERTEX"       
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VERTEX").tpc_snape="VERTEX"     


        row = box.row(align = False)
      
        if bpy.context.scene.tool_settings.snap_elements == {'EDGE_PERPENDICULAR'}:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_PERPENDICULAR", emboss = addon_prefs.tpc_use_emposs).tpc_snape="EDGE_PERPENDICULAR" 
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_PERPENDICULAR").tpc_snape="EDGE_PERPENDICULAR"  

        if bpy.context.scene.tool_settings.snap_elements == {'VOLUME'}:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VOLUME", emboss = addon_prefs.tpc_use_emposs).tpc_snape="VOLUME" 
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_VOLUME").tpc_snape="VOLUME"  

        if bpy.context.scene.tool_settings.snap_elements == {'INCREMENT'}:                                    
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_INCREMENT", emboss = addon_prefs.tpc_use_emposs).tpc_snape="INCREMENT"        
        else:
            row.operator("tpc_ot.snap_element", text=" ", icon = "SNAP_INCREMENT").tpc_snape="INCREMENT"        
        
        if bpy.context.scene.tool_settings.use_snap == True:                                    
            row.operator("tpc_ot.snap_use", text=" ", icon = "SNAP_ON", emboss = addon_prefs.tpc_use_emposs).mode="unuse_snap"        
        else:
            row.operator("tpc_ot.snap_use", text=" ", icon = "SNAP_OFF").mode="use_snap"    


        #Box 6 RT 
        box = pie.split().column(align = False)
        box.scale_x = addon_prefs.ui_scale_x_b6         
        box.scale_y = addon_prefs.ui_scale_y_b6         

        if addon_prefs.tpc_show_orientation_panel == True:
            obj = context.active_object
            object_mode = 'OBJECT' if obj is None else obj.mode
            has_pose_mode = ((object_mode == 'POSE') or (object_mode == 'WEIGHT_PAINT' and context.pose_object is not None))
            tool_settings = context.tool_settings
            scene = context.scene

            if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL'} or has_pose_mode:
                row = box.row(align = False)
                orient_slot = scene.transform_orientation_slots[0]
                row.prop_with_popover(orient_slot, "type", text="", panel="VIEW3D_PT_transform_orientations")

            #if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL'} or has_pose_mode:
                #row = box.row(align = False)
                #row.prop(tool_settings, "transform_pivot_point", text="", icon_only=True)
            #row.label(text="Pivot")


        row = box.row(align = False)
        
        if bpy.context.scene.transform_orientation_slots[0].type == 'GLOBAL':         
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GLOBAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="GLOBAL"        
        else:        
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GLOBAL").tpc_axis="GLOBAL"        

        if bpy.context.scene.transform_orientation_slots[0].type == 'LOCAL':   
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_LOCAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="LOCAL"
        else:
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_LOCAL").tpc_axis="LOCAL"

        if bpy.context.scene.transform_orientation_slots[0].type == 'NORMAL':   
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_NORMAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="NORMAL"
        else:    
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_NORMAL").tpc_axis="NORMAL"
      
        row.operator("tpc_ot.set_orientation", text=" ", icon="ZOOM_IN", emboss = addon_prefs.tpc_use_emposs)


        row = box.row(align = False)

        if bpy.context.scene.transform_orientation_slots[0].type == 'GIMBAL':   
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GIMBAL", emboss = addon_prefs.tpc_use_emposs).tpc_axis="GIMBAL"
        else:    
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_GIMBAL").tpc_axis="GIMBAL"                 

        if bpy.context.scene.transform_orientation_slots[0].type == 'VIEW':   
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_VIEW", emboss = addon_prefs.tpc_use_emposs).tpc_axis="VIEW"
        else:    
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_VIEW").tpc_axis="VIEW"    

        if bpy.context.scene.transform_orientation_slots[0].type == 'CURSOR':   
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_CURSOR", emboss = addon_prefs.tpc_use_emposs).tpc_axis="CURSOR"
        else:    
            row.operator("tpc_ot.orient_axis", text=" ", icon="ORIENTATION_CURSOR").tpc_axis="CURSOR"    

        layout.operator_context = 'INVOKE_REGION_WIN'
        scene = bpy.context.scene
        orient_slot = scene.transform_orientation_slots[0]
        custom_orient = orient_slot.custom_orientation
        if custom_orient:    
            row.operator("transform.delete_orientation", text=" ", icon='PANEL_CLOSE')
            
            if addon_prefs.tpc_show_orientation_name == True:
                row = box.row(align = False)   
                row.prop(custom_orient, "name", text="")
        
        else:
            row.label(text=" ", icon="BLANK1")


        #Box 7 LB 
        row = pie.split().column()
        row.scale_x = addon_prefs.ui_scale_x_b7                    
        row.scale_y = addon_prefs.ui_scale_y_b7                    
   
        if context.mode == 'OBJECT':
            if addon_prefs.tpc_use_place_modal_pie == True:
                icon_snap_place = icons.get("icon_snap_place")
                row.operator("tpc_ot.snapset_modal", text="Place*", icon_value=icon_snap_place.icon_id).mode = "PLACE"

            if addon_prefs.tpc_use_place_pie == True:
                if addon_prefs.use_internal_icon_btb == True:   
                    row.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon=addon_prefs.icon_btb)
                else:
                    icon_snap_place = icons.get("icon_snap_place")
                    row.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon_value=icon_snap_place.icon_id)

        else:
            if addon_prefs.tpc_use_retopo_modal_pie == True:              
                icon_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tpc_ot.snapset_modal", text="Retopo*", icon_value=icon_snap_retopo.icon_id).mode = "RETOPO"   

            if addon_prefs.tpc_use_retopo_pie == True:
                if addon_prefs.use_internal_icon_btf == True:   
                    row.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon=addon_prefs.icon_btf)    
                else:
                    icon_snap_retopo = icons.get("icon_snap_retopo")
                    row.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon_value=icon_snap_retopo.icon_id)    
           
          

        #Box 8 RB
        row = pie.split().column()
        row.scale_x = addon_prefs.ui_scale_x_b8
        row.scale_y = addon_prefs.ui_scale_y_b8

        if addon_prefs.tpc_use_grid_modal_pie == True:
            icon_snap_grid = icons.get("icon_snap_grid")
            row.operator("tpc_ot.snapset_modal", text="Grid*", icon_value=icon_snap_grid.icon_id).mode = "GRID"

        if addon_prefs.tpc_use_grid_pie == True:
            if addon_prefs.use_internal_icon_bta == True:  
                row.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon=addon_prefs.icon_bta)
            else:
                icon_snap_grid = icons.get("icon_snap_grid")
                row.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon_value=icon_snap_grid.icon_id)



