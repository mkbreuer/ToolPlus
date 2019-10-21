# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons    

from bpy.types import Menu



class VIEW3D_Resurface_Pie_Menu(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "META SCT"
    bl_idname = "tp_menu.pie_resurface"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        settings = context.tool_settings
        toolsettings = context.tool_settings  
        scn = context.scene         
        self.scn = context.scene 
        scene = context.scene                 
        view = context.space_data
        
        obj = context.object
        obj = context.active_object
        obj = bpy.context.scene.objects.active                


####### Object mode -----------------------------------------------        

        ob = context       
        if ob.mode == 'OBJECT':
            # Object mode

            pie = layout.menu_pie()


#O1 # Left ------------------------------------------------ 

            box = pie.split().box().column()
            box.scale_x = 0.65
            
            row = box.row(align=True)
            row.scale_x = 0.9
            row.operator_menu_enum("object.modifier_add", "type", text="Modif", icon="MODIFIER")                       
            row.operator("object.automirror", text="AutoMirror", icon="MOD_WIREFRAME")

            row = box.row(align=True)
            row.scale_x = 0.8
            row.prop(context.scene, "AutoMirror_threshold", text="")            
            row.prop(context.scene, "AutoMirror_axis", text="")            
            row.prop(context.scene, "AutoMirror_orientation", text="")         


            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_viewport_on", "",icon = 'RESTRICT_VIEW_OFF')
            row.operator("view3d.display_modifiers_viewport_off","",icon = 'VISIBLE_IPO_OFF')                    
            row.operator("view3d.fullmirror", text="X-Clip")            
            union = row.operator("mesh.boolean", "Union      ")
            union.modOp = 'UNION'

            
            row = box.row(align=True)
            row.scale_x = 1.5 
            row.operator("view3d.display_modifiers_delete","", icon = 'X') 
            row.operator("view3d.display_modifiers_apply","",  icon = 'FILE_TICK')                      
            row.operator("view3d.fullmirrory", text="Y-Clip")
            intersect = row.operator("mesh.boolean", "Intersect")
            intersect.modOp = 'INTERSECT'

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_expand","", icon = 'DISCLOSURE_TRI_DOWN_VEC')           
            row.operator("view3d.display_modifiers_collapse","", icon = 'DISCLOSURE_TRI_RIGHT_VEC')             
            row.operator("view3d.fullmirrorz", text="Z-Clip")                                              
            difference = row.operator("mesh.boolean", "Difference")
            difference.modOp = 'DIFFERENCE'   
           


#O2 # Right ------------------------------------------------  
         
            box = pie.split().box().column()
            box.scale_x = 0.95            
            
            row = box.row(align=True)
            row.scale_x = 1.7
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")         
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")
            
            row = box.row(align=True)
            row.scale_x = 1.7
            row.operator("snape.increment", "", icon = "SNAP_INCREMENT")        
            row.operator("snape.vertex", "", icon = "SNAP_VERTEX")        
            row.operator("snape.edge", "", icon = "SNAP_EDGE")        
            row.operator("snape.face", "", icon = "SNAP_FACE")
            row.operator("snape.volume", "", icon = "SNAP_VOLUME") 


            row = box.row(align=True)
            row.scale_x = 1.3
            toolsettings = context.tool_settings
            
            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"            
            row.menu("htk_pivotorient", "Orientation", icon = "EMPTY_DATA")
                    
            row.prop(toolsettings, "use_snap_align_rotation", text="", icon="SNAP_NORMAL")               
          
            row = box.row(align=True)
            row.scale_x = 1.3
            
            snap_meta = toolsettings.use_snap            
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"              
            row.menu("htk_snaptarget", "Snap Target", icon = "SNAP_ON")           
            row.prop(toolsettings, "use_snap_project", text="", icon="RETOPO")
            
            row = box.row(align=True)
            row.scale_x = 1.55             
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "use_proportional_edit_objects","", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True) 
            row.operator("view3d.ruler", text="Ruler")#, icon="NOCURVE")

            row = box.row(align=True)    
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")             


            
#O3 # Bottom ------------------------------------------------    
       
            box = pie.split().box().column()
            box.scale_x = 0.7

        ####--- LINE 01 ---####                
            row = box.row(align=True)                                     
            row.alignment = 'CENTER'
            row.scale_x = 1.4
            row.operator("object.simplearewo",text="Replicator  ")    
            row.operator("mft.radialclone", text=  "Rad. Clone ", icon='CURSOR')            
                               
            row.label("")                         
            row.operator("object.join",text="Join          ", icon ="FULLSCREEN_EXIT")                       
            row.operator("object.make_links_data", text="Set Instance").type ="OBDATA"                       
           
            row.label("")                 
            row.operator("wm.read_homefile", text="New      ", icon='NEW')
            row.operator("wm.open_mainfile", text="Open   ", icon='FILE_FOLDER')                         
                               
            
        ####--- LINE 02 ---####               
            row = box.row(align=True)                      
            row.alignment = 'CENTER'
            row.scale_x = 1.4   
            row.menu("VIEW3D_MT_object_parent","Parent          ", icon ="LINK_AREA")               
            row.menu("VIEW3D_MT_object_group", "Group        ", icon="GROUP")             
             
            row.label("") 
            row.operator("object.duplicate_move", "Duplicate")
            row.operator("object.duplicate_move_linked", " Dupli.Linked")                
  
            row.label("")
            row.operator("wm.link", text="Link      ", icon='LINK_BLEND')                         
            row.operator("wm.append", text="Append", icon='APPEND_BLEND')              
                                   
   
        ####--- LINE 03 ---####              
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.4                     
            row.menu("VIEW3D_MT_object_constraints", icon ="CONSTRAINT_DATA")
            row.menu("VIEW3D_MT_object_track","Track        ", icon ="CONSTRAINT") 
                                
            row.label("")
            row.operator("object.convert",text="to Mesh ", icon = "OUTLINER_DATA_MESH").target="MESH"  
            row.operator("object.convert",text="to Curve   ", icon = "OUTLINER_DATA_CURVE").target="CURVE"              
                                            
            row.label("")
            row.menu("VIEW3D_MT_make_links", text="M-Links", icon="LINKED")            
            row.menu("VIEW3D_MT_make_single_user", "M-Single", icon ="UNLINKED")             
                         
                               

        ####--- LINE 04 ---####             
            row = box.row(align=True)
            #row.alignment = 'CENTER'
            scn = context.scene             
            row.prop(scn, "mod_list",text = "")                    
            row.operator("ba.delete_data_obs","DelOrphan", icon ="PANEL_CLOSE")        

            row.label("")           
            row.menu("htk_modifly", text="Flymode          ", icon='MOD_SOFT')      
            row.operator_menu_enum("object.make_links_data", "type", text="Link Data    ")                                                             
   
            row.label("   ")
            row.menu("INFO_MT_file_import","Import      ", icon='IMPORT')
            row.menu("INFO_MT_file_export","Export    ", icon='EXPORT')  

           
        ####--- LINE 06 ---####                           
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5     
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:          
                if obj.type == 'CURVE':                
                    row.operator("curvetools2.operatorintersectcurves", text = "Intersect Curve  ")
                    row.operator("curvetools2.operatorbirail", text = " Birail Curve ")             
                    
                    row.label("")            
                    row.operator("curvetools2.operatorloftcurves", text = "Loft Curve   "  )
                    row.operator("curvetools2.operatorsweepcurves", text = "Sweep Curve   ")    
                    
                    row.label("")
                    scn = context.scene  
                    row.operator("curvetools2.operatorselectioninfo", text = "Info")
                    row.prop(context.scene.curvetools, "NrSelectedObjects", text = "")  
                    row.operator("curvetools2.operatororigintospline0start", text = "", icon ="PARTICLE_TIP")            
             
               
                
#O4 # Top ------------------------------------------------ 

            box = pie.split().box().column()         
            box.scale_x = 0.65

 
    ####--- LINE 01 ---####                   
            row = box.row(align=True)
            row.alignment ="CENTER"
            row.scale_x = 1.65            
            row.operator("screen.region_quadview", text = "", icon = "SPLITSCREEN")                        
            row.operator("object.bounding_boxers",text="", icon="BBOX")   
            row.menu("INFO_MT_curve_add",text="",icon='OUTLINER_OB_CURVE') 
            row.menu("INFO_MT_mesh_add",text="",icon='OUTLINER_OB_MESH')                          
            row.menu("INFO_MT_surface_add",text="",icon='OUTLINER_OB_SURFACE')                             
            row.operator("object.empty_add",text="",icon="OUTLINER_OB_EMPTY")            
            row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")                 
    

        ####--- LINE 02 ---####
            row = box.row(align=True)
            row.alignment ="CENTER"
            row.scale_x = 1.55                                   
            row.operator("screen.redo_last", text="Settings")            
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')                                                              
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
            row.operator("ed.undo_history", text="History  ")                                     

   
    
        ####--- LINE 04 ---####
            row = box.row(align=True)
            row.alignment ="CENTER"
            row.scale_x = 1.55                                     
            
            row.operator("retopo.latticeapply", text = " ", icon="OUTLINER_DATA_LATTICE")            
            row.operator("view3d.select_border", text=" ", icon="BORDER_RECT") 
            row.operator("view3d.select_circle", text=" ", icon="BORDER_LASSO")                         
            row.operator("mesh.snap_utilities_move", text = " ", icon="NDOF_TRANS")           
            row.menu("VIEW3D_MT_object_showhide", " ", icon = "VISIBLE_IPO_ON")                                                              
            row.operator("mesh.snap_utilities_rotate", text = " ", icon="NDOF_TURN")             
            row.operator("view3d.zoom_border"," ", icon = "ZOOM_PREVIOUS" )
            row.operator("view3d.view_all"," ", icon = "ZOOM_OUT" )                        
            row.operator("retopo.freeze", text = " ", icon ="RESTRICT_SELECT_ON")
                                                     
                                                             

#O5 # Top_Left ------------------------------------------------ 
           
            box = pie.split().box().column()
            box.scale_x = 1.1

            row = box.row(align=True)
            row.scale_x = 1
            #row.operator("freeze_transform.selected", text=" ", icon="NDOF_DOM")   
            row.operator("object.align_tools", text="Adv. Aligner", icon="ROTATE")
            row = box.row(align=True)
            row.scale_x = 2.1
            row.operator("object.align_objects_scale_all",text="", icon='MAN_SCALE')  
            row.operator("object.align_rotation_all",text="", icon='MAN_ROT')
            row.operator("object.align_location_all",text="", icon='MAN_TRANS')
                   
            row = box.row(align=True)
            row.scale_x = 1.2          
            row.operator("object.align_location_x",text="X")
            row.operator("object.align_location_y",text="Y")
            row.operator("object.align_location_z",text="Z") 
                         
            row = box.row(align=True)
            row.scale_x = 0.85  
            row.menu("VIEW3D_MT_transform_object")
            row.menu("VIEW3D_MT_object_clear")
            row.menu("VIEW3D_MT_object_apply")                       
        
            

#O6 # Top_Right ------------------------------------------------ 
 
            box = pie.split().box().column()
            box.scale_x = 1.2
            
            row = box.row(align=True)                      
            row.operator("object.editmode_toggle", text="Fast ", icon = "EDIT")    
            row.operator("object.delete", text="Delete", icon="PANEL_CLOSE").use_global=False
                         
            
            row = box.row(align=True)
            #row.scale_x = 1.6                       
            row.operator("object.origin_set", text=" ", icon="OBJECT_DATAMODE").type='ORIGIN_GEOMETRY'
            row.operator("object.origin_set", text=" ", icon="FORCE_FORCE").type='ORIGIN_CURSOR'                             
            row.menu("originsetupmenu_obm", text="Origin", icon ="LAYER_ACTIVE") 

            row = box.row(align=True)
            #row.scale_x = 1.6              
            row.operator("view3d.snap_cursor_to_center", " ", icon = "OUTLINER_DATA_EMPTY") 
            row.operator("view3d.snap_cursor_to_active", " ", icon = "PMARKER")           
            row.menu("mtk_snaptocursor","Cursor", icon ="OUTLINER_DATA_EMPTY")           

            row = box.row(align=True)
            #row.scale_x = 1.6              
            row.operator("view3d.snap_selected_to_cursor"," ", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor"," ", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect","Select", icon ="RESTRICT_SELECT_OFF")


            
#O7 # Bottom_Left ------------------------------------------------    
            box = pie.split().box().column()
            box.scale_x = 1.17          
            
            row = box.row(align=True) 
            row.scale_x = 0.675
         
            
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:                                                       
                row.prop(obj, "show_x_ray", text="X-Ray  ")      
            
            row.operator("object.shade_flat", text=" ", icon="SOLID")
            row.operator("object.shade_smooth", text=" ", icon="SMOOTH")
            row.operator("object.wire_all", text=" ", icon='WIRE')            
            
                  
            row = box.row(align=True) 
            row.scale_x = 0.7
            row.prop(view, "show_backface_culling", text="Backface")               

                     
            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")
            row.operator("view3d.modifiers_subsurf_level_2")


            row = box.row(align=True)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
                  
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")
            row.operator("view3d.modifiers_subsurf_level_5")

            row = box.row(align=True)
            row.scale_x = 0.6                       
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")   
            row.prop(context.space_data, "viewport_shade","", expand=False)
            


#O8 # Bottom_Right ------------------------------------------------ 

            box = pie.split().box().column()
            box.scale_x = 0.95
            row = box.row(align=True)           

            row.operator("object.loops1", text="X ", icon="ARROW_LEFTRIGHT")
            row.operator("object.distribute_osc", text="DIS  ", icon="ALIGN") 
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:               
                row.prop(obj, "show_name", text="Name ")                     
            
            
            row = box.row(align=True)
            row.scale_x = 1           
            row.operator("object.loops2", text="Y ", icon="ARROW_LEFTRIGHT")
            row.operator("object.align_by_faces", text="F2F  ", icon="SNAP_SURFACE")            
            
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:                         
                row.prop(obj, "show_wire", text="Wire  ")     
              
                            
            row = box.row(align=True)          
            row.operator("object.loops3", text="Z ", icon="ARROW_LEFTRIGHT")                   
            row.operator("object.drop_on_active", text="D2A", icon="SNAP_SURFACE") 
            row.prop(view, "show_all_objects_origin", "Origin")
            

            row = box.row(align=True)  
            row.operator("objects.multiedit_enter_operator") 

            sce = bpy.context.scene
            row.prop(sce, "Preserve_Location_Rotation_Scale", "G/R/S  ")  
            
 






#######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  ######

        elif ob.mode == 'EDIT_MESH':
            mesh = context.active_object.data 
            # Edit mode

# E1 # Left ------------------------------------------------ 
            
            box = pie.split().box().column()
            box.scale_x = 0.82
            
            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")                       
            row.operator("object.automirror", text="", icon="MOD_WIREFRAME")
            row.operator("view3d.fullmirror", text="X-Clip")              
            row.operator("mesh.vert_connect", text="Connect", icon ="MESH_DATA") 
            
            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_delete","", icon = 'X') 
            row.operator("view3d.display_modifiers_apply_edm","", icon = 'FILE_TICK')            
            row.operator("view3d.fullmirrory", text="Y-Clip")                                             
            row.operator("mesh.vertex_distribute",text=" Spread ", icon="PARTICLE_POINT")              
            
            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_viewport_off","",icon = 'VISIBLE_IPO_OFF')
            row.operator("view3d.display_modifiers_viewport_on","",icon = 'RESTRICT_VIEW_OFF')
            row.operator("view3d.fullmirrorz", text="Z-Clip")        
            row.operator("mesh.vertex_align",text="Straight", icon="ALIGN")    
                                       
            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_edit_off","",icon = 'SNAP_VERTEX')
            row.operator("view3d.display_modifiers_edit_on","", icon = 'EDITMODE_HLT')                                   
            row.menu("VIEW3D_MT_edit_mesh_tinycad","CAD   ", icon ="GRID")                  
            row.operator("mesh.vertices_smooth", text="Smooth ", icon ="SPHERECURVE")                           
             
            row = box.row(align=True)
            row.scale_x = 1.4        
            row.operator("view3d.display_modifiers_cage_off","",icon = 'OUTLINER_DATA_MESH')
            row.operator("view3d.display_modifiers_cage_on","",icon = 'OUTLINER_OB_MESH')            
            row.operator("object.easy_lattice", text="E-LT", icon ="OUTLINER_OB_LATTICE")                
            row.operator("mesh.bridge_edge_loops", "Bridge", icon = 'SOUND')              
                                                                                          
            row = box.row(align=True)
            row.scale_x = 0.75       
            row.operator("mesh.singleplane_x",text="X-Plane")      
            row.operator("mesh.singleplane_y",text="Y-Plane")       
            row.operator("mesh.singleplane_z",text="Z-Plane")                         
                   
            row.operator("mesh.intersect", " ", icon='ZOOMIN').use_separate = False
            row.operator("mesh.intersect", " ", icon='ZOOMOUT').use_separate = True


                        
# E2 # Right ------------------------------------------------            

            box = pie.split().box().column()
            box.scale_x = 0.85           
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")         
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")
            
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon = "SNAP_INCREMENT")        
            row.operator("snape.vertex", "", icon = "SNAP_VERTEX")        
            row.operator("snape.edge", "", icon = "SNAP_EDGE")        
            row.operator("snape.face", "", icon = "SNAP_FACE")
            row.operator("snape.volume", "", icon = "SNAP_VOLUME") 


            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data        
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "use_mesh_automerge", text="", icon='AUTOMERGE_ON')           
            row.menu("htk_pivotorient", "Orientation", icon = "EMPTY_DATA")                    
            row.prop(toolsettings, "use_snap_self", text="")
                         
            
            row = box.row(align=True)
            row.scale_x = 1.3
            
            snap_meta = toolsettings.use_snap            
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"              
            row.menu("htk_snaptarget", "Snap Target", icon = "SNAP_ON")           
            row.prop(toolsettings, "use_snap_project", text="")
            
            
            row = box.row(align=True)             
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True) 
            row.operator("view3d.ruler", text="Ruler")#, icon="NOCURVE")
            row.prop(view, "use_occlude_geometry", text="L2V") 
           
            row = box.row(align=True)    
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho") 

                 

# E3 # Bottom ------------------------------------------------             

            box = pie.split().box().column()
            
            row = box.row(align=True)
            box.scale_x = 0.75


        ####--- LINE 01 ---####                
            row = box.row(align=True)
            
            row.operator("mesh.fill_grid","Grid Fill     ", icon = "MESH_GRID")                                                                           
             
            row.label("")             
            row.operator("mesh.select_mode", text="Vertices", icon='VERTEXSEL').type = 'VERT'
            row.operator("mesh.select_mode", text="Edge", icon='EDGESEL').type = 'EDGE'
            row.operator("mesh.select_mode", text="Face", icon='FACESEL').type = 'FACE' 
             
            row.label("")
            row.operator_menu_enum('mesh.offset_edges', 'geometry_mode',text="EdgeOffset")                              

            
        ####--- LINE 02 ---####               
            row = box.row(align=True)

            row.operator("faceinfillet.op0_id",  text="FaceFillet   ", icon="CLIPUV_HLT")
                                                          
            row.label(" ") 
            row.scale_x = 0.94                              
            row.operator("mesh.subdivide",text="1").number_cuts=1
            row.operator("mesh.subdivide",text="2").number_cuts=2
            row.operator("mesh.subdivide",text="3").number_cuts=3
            row.operator("mesh.subdivide",text="4").number_cuts=4
            row.operator("mesh.subdivide",text="5").number_cuts=5
            row.operator("mesh.subdivide",text="6").number_cuts=6    
                         
            row.label("   ") 
            row.operator('fillet.op0_id', text = 'EdgeFillet ')              
        
        
        ####--- LINE 03 ---####              
            row = box.row(align=True)
            row.operator("mesh.rot_con", "F-Rotate     ", icon ="LINKED") 

            row.label("")
            row.operator("mesh.quads_convert_to_tris",text="Tri", icon="OUTLINER_OB_MESH")                       
            row.operator("mesh.unsubdivide", text="Un-Subdivide")
            row.operator("mesh.tris_convert_to_quads",text="Quad", icon="OUTLINER_OB_LATTICE")              

            row.label("")
            row.operator("mesh.face_split_by_edges", "EdgeSplit  ")             
   
       

        ####--- LINE 04 ---####             
            row = box.row(align=True)           
            row.scale_x = 1

            row.operator('object.mextrude', text="F-MultiExt ", icon ="NLA_PUSHDOWN")  
            
            row.label("") 
            row.operator("mesh.solidify", "Solidify", icon ="MOD_SOLIDIFY")                                                               
            row.operator("mesh.spin", "Spin", icon ="MOD_SIMPLEDEFORM")
            row.operator("transform.tosphere", " Sphere", icon = "MESH_UVSPHERE")                           
            
            row.label("")
            row.operator("mesh.normals_make_consistent",text="Recalc.  ", icon='SNAP_NORMAL')   

        
        ####--- LINE 05 ---####              
            row = box.row(align=True)          
            row.scale_x = 1

            row.operator("gpencil.surfsk_add_surface", text="Bsurface     ", icon = 'MOD_DYNAMICPAINT') 
            
            row.label("")              
            row.operator("mesh.sct_mesh_brush", text = "Brush ", icon = 'BRUSH_DATA')                                            
            row.operator("mesh.sct_smooth_vertices", text = "Smooth", icon = 'MOD_SMOOTH')   
            row.operator("mesh.sct_shrinkwrap", text = "Shrink ", icon = 'MOD_SHRINKWRAP') 

            row.label("")              
            row.operator("mesh.flip_normals", text="Flip Norm", icon = "FILE_REFRESH")  



        ####--- LINE 06 ---####              
            row = box.row(align=True)
            row.alignment = "CENTER"            
            row.scale_x = 1.25
            
            row.operator("mesh.looptools_flatten")               
            row.operator("mesh.looptools_relax")                           
            row.operator("mesh.looptools_space")
            row.operator("mesh.looptools_circle")                          
            row.operator("mesh.looptools_curve") 
            row.operator("mesh.looptools_bridge", text="Bridge").loft = False
            row.operator("mesh.looptools_bridge", text="Loft").loft = True 
            row.operator("mesh.looptools_gstretch")
            
                              


            
# E4 # Top ------------------------------------------------ 

            box = pie.split().box().column()         
            box.scale_x = 0.81

        ####--- LINE 01 ---####                 
            row = box.row(align=True)     
            row.operator("screen.region_quadview", text = " ", icon = "SPLITSCREEN")              
 
            row.operator("screen.redo_last", text="  Settings")
            
            row.scale_x = 1.55
            row.operator("ed.undo", text="", icon="LOOP_BACK")            
            
            row.menu("INFO_MT_mesh_add",text="", icon="MESH_DATA")                                      
            
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                                     

            row.operator("ed.undo_history", text="  History  ")                
            row.operator("screen.screen_full_area", text = " ", icon = "FULLSCREEN_ENTER") 
                                                  
    
        ####--- LINE 02 ---####     
            row = box.row(align=True)                                   
     
            row.menu("pie.selection",text="Selection")
                 
            row.operator("mesh.loop_multi_select",text=" Ring  ", icon ="COLLAPSEMENU").ring=True                          
            
            row.scale_x = 1.55                       
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')             
         
            row.operator("mesh.loop_multi_select",text=" Loop ", icon ="ZOOMOUT").ring=False    
            row.operator("mesh.faces_select_linked_flat", text="LF-Faces")             

 

            
        ####--- LINE 03 ---####               
            row = box.row(align=True)
        
            row.operator("mesh.select_nth","Checker")                         
            
            row.operator("view3d.select_border", text=" ", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text=" ", icon="BORDER_LASSO")             
            row.operator("mesh.snap_utilities_move", text = " ", icon="NDOF_TRANS")
            row.menu("VIEW3D_MT_edit_mesh_showhide", " ", icon = "VISIBLE_IPO_ON")                                                              
            row.operator("mesh.snap_utilities_rotate", text = " ", icon="NDOF_TURN")  
            row.operator("view3d.zoom_border"," ", icon = "ZOOM_PREVIOUS" )
            row.operator("view3d.view_all"," ", icon = "ZOOM_OUT" )                                               
            row.operator("meshlint.select", "Meshlint") 
       
       
                     


# E5 # Top_Left ------------------------------------------------           

            box = pie.split().box().column()
            box.scale_x = 0.97

            row = box.row(align=True)
            row.scale_x = 1
            props = row.operator("mesh.knife_tool", text="Knife         ", icon="LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False
            row.operator("mesh.bisect","Biscet ", icon ="SCULPTMODE_HLT")
            row.operator("mesh.snap_utilities_line","SnapLine", icon="LINE_DATA")                                                             
            
            row = box.row(align=True)
            row.scale_x = 1
            props = row.operator("mesh.knife_tool", text="K-Select", icon="LINE_DATA")        
            props.use_occlude_geometry = False
            props.only_selected = True                        
            row.operator("object.createhole", text="Hole", icon = "RADIOBUT_OFF")
            row.operator("mesh.ext_cut_faces", text="F-Cut  ", icon = "SNAP_EDGE")           
         
                   
            row = box.row(align=True)
            row.scale_x = 1         
            row.operator("mesh.knife_project","K-Project ", icon="LINE_DATA")
            row.operator("mesh.split","  Split ", icon = "RETOPO")             
            row.operator("mesh.loopcut_slide","Loopcut", icon="GRIP")
            
            
            row = box.row(align=True)
            row.scale_x = 1  
            row.menu("VIEW3D_MT_transform", "Transform   ")
            row.operator("mesh.inset",  text="Inset [I]", icon ="CLIPUV_DEHLT")
            row.operator("mesh.merge", text = " Merge  ", icon ="AUTOMERGE_ON")                         
                                 

                   

# E6 # Top_Right ------------------------------------------------ 
 
            box = pie.split().box().column()
            box.scale_x = 1
            
            row = box.row(align=True)         
            row.operator("object.editmode_toggle", text="Fast  ", icon = "OBJECT_DATAMODE") 
            row.menu("mesh.cleandelete",text="Delete", icon="PANEL_CLOSE")    
            
            row = box.row(align=True)
            #row.scale_x = 1.6                       
            row.operator("object.loops7", text=" ", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", text=" ", icon="FORCE_FORCE")                           
            row.menu("originsetupmenu_edm", "Origin ", icon = "LAYER_ACTIVE")
            row.menu("mesh.cleanedge", text="Edges", icon = "SNAP_EDGE")

            row = box.row(align=True)
            #row.scale_x = 1.6              
            row.operator("view3d.snap_cursor_to_center", " ", icon = "OUTLINER_DATA_EMPTY") 
            row.operator("view3d.snap_cursor_to_active", " ", icon = "PMARKER")           
            row.menu("mtk_snaptocursor","Cursor", icon ="OUTLINER_DATA_EMPTY")           
            row.menu("mesh.cleanface", text="Faces", icon = "SNAP_FACE")

            row = box.row(align=True)
            #row.scale_x = 1.6              
            row.operator("view3d.snap_selected_to_cursor"," ", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor"," ", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect","Select     ", icon ="RESTRICT_SELECT_OFF")
            row.menu("mesh.cleandissolve", text="Dissolve", icon = "SNAP_VOLUME")


            
# E7 # Bottom_Left ------------------------------------------------    

            box = pie.split().box().column()
            box.scale_x = 1.17          
            view = context.space_data
            obj = context.object 
            
            row = box.row(align=True) 
            row.scale_x = 0.675
                                           
            row.prop(obj, "show_x_ray", text="X-Ray  ")      
            row.operator("mesh.faces_shade_flat", text=" ", icon="MESH_CIRCLE")               
            row.operator("mesh.faces_shade_smooth", text=" ", icon="SMOOTH")
            row.operator("object.wire_all", text=" ", icon='WIRE')            
            
                  
            row = box.row(align=True) 
            row.scale_x = 0.7
            row.prop(view, "show_occlude_wire","Hidden")               
                     
            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")
            row.operator("view3d.modifiers_subsurf_level_2")


            row = box.row(align=True)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")                   
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")
            row.operator("view3d.modifiers_subsurf_level_5")


            row = box.row(align=True)
            row.scale_x = 0.6                       
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")   

            view = context.space_data        
            row.prop(context.space_data, "viewport_shade","", expand=False)
            

# E8 # Bottom_Right ------------------------------------------------ 

            box = pie.split().box().column()
            box.scale_x = 0.9

            obj = context.object
            obj_type = obj.type
            is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
            is_wire = (obj_type in {'CAMERA', 'EMPTY'})
            is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
            is_dupli = (obj.dupli_type != 'NONE')            
            
            row = box.row(align=True)
            row.scale_x = 1     
            row.operator("mesh.face_align_x", "X      ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y      ", icon='COLOR_GREEN')           
            row.operator("mesh.face_align_z", "Z      ", icon='COLOR_BLUE')
            row.prop(mesh, "show_extra_edge_length", text="E-Length")

            row = box.row(align=True)
            row.scale_x = 1    
            row.operator("mesh.face_align_xy", "Xy  ", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy  ", icon='TRIA_UP_BAR')           
            row.operator("mesh.face_align_xz", "Zx  ", icon='TRIA_LEFT_BAR')
            row.prop(mesh, "show_extra_edge_angle", text="E-Angle")                        
                  
            row = box.row(align=True)
            row.scale_x = 1                
            row.operator("object.loops1",text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2",text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3",text="MZ", icon='ARROW_LEFTRIGHT')            
            row.prop(mesh, "show_extra_face_area", text="F-Area")



            row = box.row(align=True)  
            row.operator("objects.multiedit_exit_operator", "MultiEditExit")
            sce = bpy.context.scene
            row.prop(sce, "Preserve_Location_Rotation_Scale", "G/R/S  ")   
            row.prop(mesh, "show_extra_face_angle", text="F-Angle")              






#######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######

        if ob.mode == 'EDIT_CURVE':
           

#C1 # Left ------------------------------------------------  
                   
            box = pie.split().box().column()            
            
            row = box.row(align=True)
            row.scale_x = 0.9                     
            row.operator("curve.surfsk_reorder_splines", text="Reorder")
            row.operator("curve.spline_type_set", "Spline Type")                           

            row = box.row(align=True)
            row.scale_x = 0.9  
            row.operator("curve.surfsk_first_points", text="First Point")                                 
            row.operator("curve.radius_set", "Radius")            
            
            row = box.row(align=True)
            row.scale_x = 0.9
            row.operator("curve.switch_direction", "Direction")                                 
            row.operator("curve.smooth")

            row = box.row(align=True)
            row.scale_x = 1                    
            row.operator("object.vertex_random")
            row.operator("curve.extrude_move", text="Extrude")

            

# C2 # Right ------------------------------------------------ 

            box = pie.split().box().column()
            box.scale_x = 0.85           
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")         
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")
            
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon = "SNAP_INCREMENT")        
            row.operator("snape.vertex", "", icon = "SNAP_VERTEX")        
            row.operator("snape.edge", "", icon = "SNAP_EDGE")        
            row.operator("snape.face", "", icon = "SNAP_FACE")
            row.operator("snape.volume", "", icon = "SNAP_VOLUME") 


            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data        
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "use_snap_align_rotation", text="", icon = "SNAP_NORMAL" )          
            row.menu("htk_pivotorient", "Orientation", icon = "EMPTY_DATA")                    
            row.prop(toolsettings, "use_snap_self", text="")
                         
            
            row = box.row(align=True)
            row.scale_x = 1.3           
            
            snap_meta = toolsettings.use_snap            
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"              
             
            row.menu("htk_snaptarget", "Snap Target", icon = "SNAP_ON")           
            row.prop(toolsettings, "use_snap_project", text="")
                        
            row = box.row(align=True)                                     
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)           
            row.operator("view3d.ruler", text="Ruler")#, icon="NOCURVE")
           
            row = box.row(align=True)    
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho") 

                 
# C3 # Button ------------------------------------------------  

            box = pie.split().box().column()
            box.scale_x = 1
            
            row = box.row(align=True)            
            row.operator("curvetools2.operatorsplinesjoinneighbouring", text = "Join")
            row.operator("curve.make_segment",  text="Segment")
            row.operator("bpt.bezier_curve_split",  text="Split")         
            row.operator("object._curve_outline",  text="Outline")                                       
            
            row = box.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinMode", text = "")  
            row.operator("curve.separate", "     Separate")
            
            
            row = box.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinDistance", text = "")
            row.prop(context.scene.curvetools, "SplineJoinStartEnd", text = "only start & end")
                      
            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinesremovezerosegment", text = "remove 0-segment splines")            
            
            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinesremoveshort", text = "rem. short")
            row.prop(context.scene.curvetools, "SplineRemoveLength", text = "")



# C4 # Top ------------------------------------------------ 
          
            box = pie.split().box().column()
            box.scale_x = 0.6
             
            row = box.row(1)                
            row.scale_x = 1.55            
            row.operator("screen.region_quadview", text = "", icon = "SPLITSCREEN")  
            row.operator("screen.redo_last", text="Settings ")            
            row.operator("ed.undo", text="", icon="LOOP_BACK")            
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')                                     
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                                     
            row.operator("ed.undo_history", text="History")               
            row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER") 
            
            row = box.row(1)
            row.scale_x = 1.55               
            row.operator("curve.select_random", text="Random")
            row.operator("curve.select_nth", text="Checker")                     
            row.menu("INFO_MT_curve_add","", icon='OUTLINER_OB_CURVE')                        
            row.operator("curve.select_linked", text="Linked  ")
            row.operator("curve.select_all", text="Inverse  ").action = 'INVERT'                      
            
            row = box.row(1)                
            row.scale_x = 1.55       
            row.alignment ="CENTER"                    

            row.operator("curve.de_select_first","", icon="NEXT_KEYFRAME")
            row.operator("curve.select_next","", icon="FF")

            row.operator("view3d.select_border", text="", icon="BORDER_RECT") 
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")                         
            row.menu("VIEW3D_MT_edit_curve_showhide", "", icon = "VISIBLE_IPO_ON")                                                              
            row.operator("view3d.zoom_border","", icon = "ZOOM_PREVIOUS" )
            row.operator("view3d.view_all","", icon = "ZOOM_OUT" )                                             

            row.operator("curve.select_previous","", icon="REW")
            row.operator("curve.de_select_last","", icon="PREV_KEYFRAME")



# C5 # Top_Left ------------------------------------------------ 
          
            box = pie.split().box().column()              
            box.scale_x = 0.85            

            row = box.row(align=True)            
            row.operator("curve.normals_make_consistent")            
            
            row = box.row(align=True)
            row.scale_x = 1           
            row.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
            row.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'
                       
            row = box.row(align=True)
            row.scale_x = 1
            row.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'
            row.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'
            
            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinessetresolution", text = "Resolution")
            row.prop(context.scene.curvetools, "SplineResolution", text = "")              


# C6 # Top_Right ------------------------------------------------ 
         
            box = pie.split().box().column()                        
            box.scale_x = 0.95
                                   
            row = box.row(align=True)               
            row.operator("object.editmode_toggle", text="Fast", icon = "OBJECT_DATAMODE")   
            row.operator("curve.delete")            
            
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9","", icon = "EDITMODE_HLT")
            row.operator("object.loops7","", icon = "OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon = "LAYER_ACTIVE")

            
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon = "OUTLINER_DATA_EMPTY") 
            row.operator("view3d.snap_cursor_to_active", "", icon = "PMARKER")  
            row.menu("mtk_snaptocursor","Cursor", icon = "OUTLINER_DATA_EMPTY")

                                                              
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor","", icon="RESTRICT_SELECT_OFF").use_offset = False                
            row.operator("view3d.snap_selected_to_cursor","", icon="STICKY_UVS_VERT").use_offset = True  
            row.menu("mtk_snaptoselect","Select", icon = "RESTRICT_SELECT_OFF")
                                           

# C7 # Bottom_Left ------------------------------------------------ 
          
            box = pie.split().box().column()
            box.scale_x = 1
                                    
            row = box.row(align=True)
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:                                                       
                row.prop(obj, "show_x_ray", text="X-Ray  ")  
            row.operator("object.wire_all", text=" ", icon='WIRE')            
            row.operator("curve.subdivide", text="1").number_cuts=1        
            row.operator("curve.subdivide", text="2").number_cuts=2
            
            row = box.row(align=True)
            row.prop(view, "use_matcap")                        
            row.operator("curve.subdivide", text="3").number_cuts=3
            row.operator("curve.subdivide", text="4").number_cuts=4
            row.operator("curve.subdivide", text="5").number_cuts=5               
                       
            row = box.row(align=True)            
            row.scale_x = 0.6                       
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")                     
            row.prop(context.space_data, "viewport_shade","", expand=False)   
            
            
# C8 # Bottom_Right ------------------------------------------------ 
         
            box = pie.split().box().column()
            box.scale_x = 1            
            
            curve = context.active_object.data

            row = box.row(align=True)
            row.scale_x = 1     
            row.operator("mesh.face_align_x", "X  ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y ", icon='COLOR_GREEN')           
            row.operator("mesh.face_align_z", "Z  ", icon='COLOR_BLUE')
            row.prop(curve, "show_handles", text="Handles")

            row = box.row(align=True)
            row.scale_x = 1    
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')           
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')
            row.prop(curve, "show_normal_face", text="Normals")                         
                  
            row = box.row(align=True)
            row.scale_x = 1                
            row.operator("object.loops1",text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2",text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3",text="MZ", icon='ARROW_LEFTRIGHT')            
            row.prop(context.scene.tool_settings, "normal_size", text="")   
            
            


#######  Surfacemode  #######  Surfacemode  #######  Surfacemode  #######  Surfacemode  #######  Surfacemode  #######
      
        if ob.mode == 'EDIT_SURFACE':


# S1 # Left ------------------------------------------------                     

            box = pie.split().box().column()            
            row = box.row()
            row.operator("curve.extrude", text="Extrude")
            row = box.row()
            row.operator("curve.duplicate_move", text="Duplicate")
            row = box.row()
            row.operator("curve.switch_direction", "Direction")

            
# S2 # Right ------------------------------------------------ 
            
            box = pie.split().box().column()
            box.scale_x = 0.85           
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")         
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")
            
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon = "SNAP_INCREMENT")        
            row.operator("snape.vertex", "", icon = "SNAP_VERTEX")        
            row.operator("snape.edge", "", icon = "SNAP_EDGE")        
            row.operator("snape.face", "", icon = "SNAP_FACE")
            row.operator("snape.volume", "", icon = "SNAP_VOLUME") 


            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data        
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "use_snap_align_rotation", text="", icon = "SNAP_NORMAL" )          
            row.menu("htk_pivotorient", "Orientation", icon = "EMPTY_DATA")                    
            row.prop(toolsettings, "use_snap_self", text="")
                         
            
            row = box.row(align=True)
            row.scale_x = 1.3           
            
            snap_meta = toolsettings.use_snap            
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"              
             
            row.menu("htk_snaptarget", "Snap Target", icon = "SNAP_ON")           
            row.prop(toolsettings, "use_snap_project", text="")
                        
            row = box.row(align=True)                                     
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "proportional_edit_objects", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)           
            row.operator("view3d.ruler", text="Ruler")#, icon="NOCURVE")
           
            row = box.row(align=True)    
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho") 

                 
# S3 # Button ------------------------------------------------  
           
            box = pie.split().box().column()
            box.scale_x = 1
            
            row = box.row(1)                                     
            row.operator("curve.split")
            row.operator("curve.make_segment", "Segment")
            row.operator("curve.separate")
            
            

# S4 # Top ------------------------------------------------ 
           
            box = pie.split().box().column()
            box.scale_x = 0.6
             
            row = box.row(1)                
            row.scale_x = 1.55            
            row.operator("screen.region_quadview", text = "", icon = "SPLITSCREEN")  
            row.operator("screen.redo_last", text="Settings ")            
            row.operator("ed.undo", text="", icon="LOOP_BACK")            
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')                                     
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                                     
            row.operator("ed.undo_history", text="History")               
            row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER") 
            
            row = box.row(1)
            row.scale_x = 1.55               
            row.operator("curve.select_random", text="Random")
            row.operator("curve.select_nth", text="Checker")                     
            row.menu("INFO_MT_surface_add","", icon='OUTLINER_OB_SURFACE')                      
            row.operator("curve.select_linked", text="Linked ")
            row.operator("curve.select_all", text="Inverse  ").action = 'INVERT'                      
            
            row = box.row(1)                
            row.scale_x = 1.55       
            row.alignment ="CENTER"                    
 
            row.operator("view3d.select_border", text="", icon="BORDER_RECT") 
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")                         
            row.menu("VIEW3D_MT_edit_curve_showhide", "", icon = "VISIBLE_IPO_ON")                                                              
            row.operator("view3d.zoom_border","", icon = "ZOOM_PREVIOUS" )
            row.operator("view3d.view_all","", icon = "ZOOM_OUT" )                                             



# S5 # Top_Left ------------------------------------------------ 
          
            box = pie.split().box().column()              
            row = box.row()            
            row.menu("VIEW3D_MT_hook")            
            row = box.row()
            row.operator("curve.cyclic_toggle")
            row = box.row()
            row.operator("object.vertex_random")
            

# S5 # Top_Right ------------------------------------------------ 
           
            box = pie.split().box().column()                        
            box.scale_x = 0.85
            
            row = box.row(align=True)               
            row.operator("object.editmode_toggle", text="Fast", icon = "OBJECT_DATAMODE")   
            row.operator("curve.delete")            
            
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9","", icon = "EDITMODE_HLT")
            row.operator("object.loops7","", icon = "OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon = "LAYER_ACTIVE")

            
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon = "OUTLINER_DATA_EMPTY") 
            row.operator("view3d.snap_cursor_to_active", "", icon = "PMARKER")  
            row.menu("mtk_snaptocursor","Cursor", icon = "OUTLINER_DATA_EMPTY")

                                                              
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor","", icon="RESTRICT_SELECT_OFF").use_offset = False                
            row.operator("view3d.snap_selected_to_cursor","", icon="STICKY_UVS_VERT").use_offset = True  
            row.menu("mtk_snaptoselect","Select", icon = "RESTRICT_SELECT_OFF")
        
                                   


# S7 # Bottom_Left ------------------------------------------------ 
          
            box = pie.split().box().column()
            box.scale_x = 1
                                    
            row = box.row(align=True)
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:                                                       
                row.prop(obj, "show_x_ray", text="X-Ray  ")  
            row.operator("object.wire_all", text=" ", icon='WIRE')            
            row.operator("curve.subdivide", text="1").number_cuts=1        
            row.operator("curve.subdivide", text="2").number_cuts=2
            
            row = box.row(align=True)
            row.prop(view, "use_matcap")                        
            row.operator("curve.subdivide", text="3").number_cuts=3
            row.operator("curve.subdivide", text="4").number_cuts=4
            row.operator("curve.subdivide", text="5").number_cuts=5               
                       
            row = box.row(align=True)            
            row.scale_x = 0.6                       
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")                     
            row.prop(context.space_data, "viewport_shade","", expand=False)   
            

# S8 # Bottom_Right ------------------------------------------------  
           
            box = pie.split().box().column()
            row = box.row(align=True)
            row.scale_x = 1            
            row.operator("mesh.face_align_x", "X", icon='TRIA_RIGHT')
            row.operator("object.loops1",text="X", icon='ARROW_LEFTRIGHT')
            row = box.row(align=True)
            row.scale_x = 1            
            row.operator("mesh.face_align_y", "Y", icon='TRIA_UP')
            row.operator("object.loops2",text="Y", icon='ARROW_LEFTRIGHT')                                            
            row = box.row(align=True)
            row.scale_x = 1               
            row.operator("mesh.face_align_z", "Z", icon='SPACE3')
            row.operator("object.loops3",text="Z", icon='ARROW_LEFTRIGHT')  




####### Latticemode ####### Latticemode ####### Latticemode ####### Latticemode ####### Latticemode ####### Latticemode #######

         
        if ob.mode == 'EDIT_LATTICE':


# L1 # Left ------------------------------------------------ 

            box = pie.split().box().column()
            box.scale_x = 1
                        
            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_viewport_on","",icon = 'RESTRICT_VIEW_OFF')
            row.operator("view3d.display_modifiers_viewport_off","",icon = 'VISIBLE_IPO_OFF')            
            row.operator("lattice.flip", text="Flip X").axis = "U"

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_edit_on","", icon = 'EDITMODE_HLT')
            row.operator("view3d.display_modifiers_edit_off","",icon = 'SNAP_VERTEX')
            row.operator("lattice.flip", text="Flip Y").axis = "V"                                     
                                      
            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_cage_on","",icon = 'OUTLINER_OB_MESH')
            row.operator("view3d.display_modifiers_cage_off","",icon = 'OUTLINER_DATA_MESH')                                               
            row.operator("lattice.flip", text="Flip Z").axis = "W"

             
            row = box.row(align=True)
            row.scale_x = 1.5        
            row.operator("view3d.display_modifiers_delete","", icon = 'X') 
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER") 




                        
# L2 # Right ------------------------------------------------            

            box = pie.split().box().column()
            box.scale_x = 0.85           
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")         
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")
            
            
            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon = "SNAP_INCREMENT")        
            row.operator("snape.vertex", "", icon = "SNAP_VERTEX")        
            row.operator("snape.edge", "", icon = "SNAP_EDGE")        
            row.operator("snape.face", "", icon = "SNAP_FACE")
            row.operator("snape.volume", "", icon = "SNAP_VOLUME") 


            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data        
            toolsettings = context.tool_settings            
            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"          
            row.menu("htk_pivotorient", "Orientation", icon = "EMPTY_DATA")                    
            row.prop(toolsettings, "use_snap_self", text="")
                         
            
            row = box.row(align=True)
            row.scale_x = 1.3
            
            snap_meta = toolsettings.use_snap            
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"              
            row.menu("htk_snaptarget", "Snap Target", icon = "SNAP_ON")           
            row.prop(toolsettings, "use_snap_project", text="")
            
            
            row = box.row(align=True)
            row.scale_x = 1.55             
            toolsettings = context.tool_settings            
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True) 
            row.operator("view3d.ruler", text="Ruler")#, icon="NOCURVE")
           
            row = box.row(align=True)    
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho") 

                 

# L3 # Bottom ------------------------------------------------             

            box = pie.split().box().column()
            
            row = box.row(align=True)                                  
            row.operator("lattice.select_mirror", text="Sel. Mirror")
            row.operator("lattice.select_random", text="Sel. Random")

            row = box.row(align=True)             
            row.operator("lattice.select_all", text="Sel. Inverse").action = 'INVERT'
            row.operator("lattice.select_ungrouped", text="Ungrouped Verts") 



            
# L4 # Top ------------------------------------------------ 

            box = pie.split().box().column()         
            box.scale_x = 0.65
             
            row = box.row(align=True)                           
            row.alignment ='CENTER'
            row.scale_x = 1.55                            
                    
            row.operator("screen.redo_last", text="Settings ") 
            row.operator("ed.undo", text="", icon="LOOP_BACK")            
            row.operator("wm.search_menu", text="", icon='VIEWZOOM') 
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                                                              
            row.operator("ed.undo_history", text="History")   
 
            
            row = box.row(align=True)                           
            row.alignment ='CENTER'
            row.scale_x = 1.55  
            row.operator("screen.region_quadview", text = "", icon = "SPLITSCREEN")  
            row.operator("view3d.select_border", text="", icon="BORDER_RECT") 
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")                         
                                                                           
            row.operator("view3d.zoom_border","", icon = "ZOOM_PREVIOUS" )
            row.operator("view3d.view_all","", icon = "ZOOM_OUT" )    
            row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")  



# L5 # Top_Left ------------------------------------------------           

            box = pie.split().box().column()

            row = box.row(align=True)
            row.menu("VIEW3D_MT_hook", "Set Hook")

            row = box.row(align=True)
            row.operator("object.vertex_parent_set", "Vertex Parent")            
            
            row = box.row(align=True)            
            row.scale_x = 1.1
            row.operator("lattice.make_regular") 


# L6 # Top_Right ------------------------------------------------ 
 
            box = pie.split().box().column()
            row = box.row(align=True)               
            row.operator("object.editmode_toggle", text="Fast Toggle", icon = "OBJECT_DATAMODE")   
            
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9","", icon = "EDITMODE_HLT")
            row.operator("object.loops7","", icon = "OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon = "LAYER_ACTIVE")

            
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon = "OUTLINER_DATA_EMPTY") 
            row.operator("view3d.snap_cursor_to_active", "", icon = "PMARKER")  
            row.menu("mtk_snaptocursor","Cursor", icon = "OUTLINER_DATA_EMPTY")

                                                              
            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor","", icon="RESTRICT_SELECT_OFF").use_offset = False                
            row.operator("view3d.snap_selected_to_cursor","", icon="STICKY_UVS_VERT").use_offset = True  
            row.menu("mtk_snaptoselect","Select", icon = "RESTRICT_SELECT_OFF")

            
# L7 # Bottom_Left ------------------------------------------------    

            box = pie.split().box().column()
            box.scale_x = 1.5         


            row = box.column(align=True)
            row.operator("object.wire_all", text="Wire", icon='WIRE')             
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"             
            row.prop(context.space_data.fx_settings, "use_ssao", text="AO", icon='GROUP') 


                   

# L8 # Bottom_Right ------------------------------------------------ 

            box = pie.split().box().column()
            row = box.row(align=True)

            row.scale_x = 1     
            row.operator("mesh.face_align_x", "X      ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y      ", icon='COLOR_GREEN')           
            row.operator("mesh.face_align_z", "Z      ", icon='COLOR_BLUE')

            row = box.row(align=True)
            row.scale_x = 1    
            row.operator("mesh.face_align_xy", "Xy  ", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy  ", icon='TRIA_UP_BAR')           
            row.operator("mesh.face_align_xz", "Zx  ", icon='TRIA_LEFT_BAR')                    
                  
            row = box.row(align=True)
            row.scale_x = 1                
            row.operator("object.loops1",text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2",text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3",text="MZ", icon='ARROW_LEFTRIGHT')   

        

####### Sculpt menu -----------------------------------------------
                    
        if ob.mode == 'SCULPT':
            box = pie.split().box().column()         
            box.scale_x = 0.65
             
            row = box.row(align=True)                           
            row.alignment ='CENTER'
            row.scale_x = 1.55                            
                    
            row.operator("screen.redo_last", text="Settings ") 
            row.operator("ed.undo", text="", icon="LOOP_BACK")            
            row.operator("wm.search_menu", text="", icon='VIEWZOOM') 
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")                                                              
            row.operator("ed.undo_history", text="History")  
            
            row = box.row(align=True)                           
            row.alignment ='CENTER'
            row.scale_x = 1.55              
            pie.operator_enum("VIEW3D_MT_TransformMenu", icon='MANIPUL')


            



def register():
    bpy.utils.register_class(VIEW3D_SCT_EXT_PIE)
    bpy.utils.register_class(VIEW3D_PIE_Selection)   

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        
        #change here the Location of your Menu_1
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        #change here the Hotkey of your Menu
        kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS')
        
        #your idname for the menu
        kmi.properties.name = "meta.sct_piemenu"
              

def unregister():
    bpy.utils.unregister_class(VIEW3D_SCT_EXT_PIE)
    bpy.utils.unregister_class(VIEW3D_PIE_Selection)   
   
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        
        #change here the Location of your Menu_2
        km = kc.keymaps['3D View']
        
        ##########################
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu_pie':
                if kmi.properties.name == "":
                    km.keymap_items.remove(kmi)
                    break

                
if __name__ == "__main__":
    register()

    #test the script inside blender text editor
    bpy.ops.wm.call_menu_pie(name="VIEW3D_SCT_EXT_PIE")








