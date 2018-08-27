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
from . icons.icons import load_icons    

# LOAD UI #
from .ui_layouts.ui_title                  import draw_title_ui
from .ui_layouts.ui_pivot                  import draw_pivot_ui
from .ui_layouts.ui_add                    import draw_add_ui
from .ui_layouts.ui_edit                   import draw_edit_ui
from .ui_layouts.ui_origin                 import draw_origin_ui
from .ui_layouts.ui_shrinkwrap             import draw_shrinkwrap_ui
from .ui_layouts.ui_surface_constraint     import draw_surface_constraint_ui
from .ui_layouts.ui_snaphot                import draw_snapshot_ui
from .ui_layouts.ui_symdim                 import draw_symdim_ui
from .ui_layouts.ui_boolean                import draw_boolean_ui
from .ui_layouts.ui_align                  import draw_align_ui
from .ui_layouts.ui_align                  import draw_axis_ui
from .ui_layouts.ui_pencil                 import draw_pencil_ui
from .ui_layouts.ui_copy                   import draw_copy_ui
from .ui_layouts.ui_biped                  import draw_biped_ui
from .ui_layouts.ui_recoplanar             import draw_recoplanar_ui
from .ui_layouts.ui_spacing                import draw_spacing_ui
from .ui_layouts.ui_relax                  import draw_relax_ui
from .ui_layouts.ui_check                  import draw_check_ui
from .ui_layouts.ui_transform              import draw_transform_ui
from .ui_layouts.ui_convert                import draw_convert_ui
from .ui_layouts.ui_modifier               import draw_modifier_ui
from .ui_layouts.ui_visual                 import draw_visual_ui

from .ui_layouts.ui_mira import draw_miratools_ui
from .ui_layouts.ui_mira import draw_miraguide_ui
from .ui_layouts.ui_mira import draw_mirastretch_ui
from .ui_layouts.ui_mira import draw_mirawrap_ui

from .ui_layouts.ui_custom                 import draw_custom_ui
from .ui_layouts.ui_lattice                import draw_lattice_ui
from .ui_layouts.ui_curve                  import draw_curve_ui

from .ui_layouts.mesh_brush.ui_display_properties  import draw_display_properties_ui
from .ui_layouts.mesh_brush.ui_falloff             import draw_falloff_ui
from .ui_layouts.mesh_brush.ui_mesh_brush          import draw_mesh_brush_ui
from .ui_layouts.mesh_brush.ui_options             import draw_options_ui
from .ui_layouts.mesh_brush.ui_symmetry            import draw_symmetry_ui
from .ui_layouts.ui_smooth_vertices                import draw_smooth_vertices_ui



# LOAD PANEL #
EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'LATTICE', 'META', 'FONT', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']



class draw_layout_resurface:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:
#                return isModelingMode and context.mode in EDIT

        return isModelingMode and context.mode in EDIT


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        UI_ADD = ["OBJECT", "EDIT_CURVE", "EDIT_SURFACE"]
        UI_BRUSHES = ["OBJECT"]
        UI_OBM = ["OBJECT"]
        UI_EDM = ["EDIT_MESH"]
        UI_CEDM = ["EDIT_CURVE", "EDIT_SURFACE"]
        UI_LEDM = ["EDIT_LATTICE"]

        tp_props = context.window_manager.tp_props_resurface
       
        addon = bpy.context.user_preferences.addons[__package__.split(".")[0]]
        props = addon.preferences.mesh_brush

        addon_prefs = context.user_preferences.addons[__package__].preferences
        expand = addon_prefs.expand_snap_settings

        icons = load_icons()    

        # LOADED LAYOUTS ---------------------------------------------------------------------
 
        
        # TITLE # 
        draw_title = context.user_preferences.addons[__package__].preferences.tab_title_ui
        if draw_title == True:  

            draw_title_ui(self, context, layout) 


        ## TOOLS OBJECTMODE ##        
        if context.mode in UI_OBM:   
        
            # ADD # 
            draw_add = context.user_preferences.addons[__package__].preferences.tab_add_ui
            if draw_add == True:  

                box = layout.box().column(1)       
                row = box.row(1) 
                row.alignment = 'CENTER'               
                sub = row.row(1)
                sub.scale_x = 1
                sub.menu("INFO_MT_mesh_add",text="",icon='OUTLINER_OB_MESH')              
                sub.menu("INFO_MT_curve_add",text="",icon='OUTLINER_OB_CURVE')
                sub.menu("INFO_MT_surface_add",text="",icon='OUTLINER_OB_SURFACE')
                sub.menu("INFO_MT_metaball_add",text="",icon="OUTLINER_OB_META")
                sub.operator("object.camera_add",icon='OUTLINER_OB_CAMERA',text="")   
                sub.menu("INFO_MT_armature_add",text="",icon="OUTLINER_OB_ARMATURE")
                #sub.menu("origin.retopo_menu",text="", icon = 'LAYER_ACTIVE') 
                               
                row = box.row(1)
                row.alignment = 'CENTER'               
                sub = row.row(1)
                sub.scale_x = 1
                sub.operator("object.empty_add",text="",icon="OUTLINER_OB_EMPTY")          
                sub.operator("object.add",text="",icon="OUTLINER_OB_LATTICE").type="LATTICE"
                sub.operator("object.text_add",text="",icon="OUTLINER_OB_FONT")
                sub.operator("object.lamp_add",icon='OUTLINER_OB_LAMP',text="")
                sub.operator("object.speaker_add",icon='OUTLINER_OB_SPEAKER',text="")
                sub.operator_menu_enum("object.effector_add", "type", text="",icon="SOLO_ON")    

                    
        # PIVOT #   
        display_pivot = context.user_preferences.addons[__package__].preferences.tab_pivot_ui
        if display_pivot == True:   

            draw_pivot_ui(self, context, layout) 
    

        ## INSERTS ##      
        if context.mode in UI_ADD:
           
            display_insert = context.user_preferences.addons[__package__].preferences.tab_create_ui
            if display_insert == True:

                draw_add_ui(self, context, layout)      


        ## BRUSHES ##  
        if context.mode in UI_BRUSHES:

                col = layout.column(1)
                box = col.box().column(1)                   
                box.separator()        

                if tp_props.display_brushes_obm:

                    row = box.row(1) 
                    row.prop(tp_props, "display_brushes_obm", text="", icon="PROP_CON")                                                                                                       
                    row.label("Brush Properties")                   
                   
                    box.separator()                
             
                else:           

                    row = box.row(1) 
                    sub = row.row(1)
                    sub.alignment = 'CENTER'    
                    sub.scale_x = 2  
                    sub.scale_y = 1.7 

                    sub.prop(tp_props, "display_brushes_obm", text="", icon="PROP_CON") 

                    button_draw_pencil = icons.get("icon_draw_pencil")
                    sub.operator("gpencil.draw", text="", icon_value=button_draw_pencil.icon_id).mode = 'DRAW'
  
                    button_draw_lathe = icons.get("icon_draw_lathe")     
                    sub.operator("tp_ops.curve_lathe", text="", icon_value=button_draw_lathe.icon_id)   

                    button_draw_surface = icons.get("icon_draw_surface")     
                    sub.operator("tp_ops.curve_draw", text="", icon_value=button_draw_surface.icon_id).mode ='surface' 

                    button_draw_curve = icons.get("icon_draw_curve")     
                    sub.operator("tp_ops.curve_draw", text="", icon_value=button_draw_curve.icon_id).mode ='cursor'                

                    button_draw_carver = icons.get("icon_draw_carver")
                    sub.operator("object.carver", text="", icon_value=button_draw_carver.icon_id)
   
                    button_draw_knife = icons.get("icon_draw_knife")   
                    sub.operator("tp_ops.snapline", text="", icon_value=button_draw_knife.icon_id)       

                    box.separator()  


                if tp_props.display_brushes_obm:            

                    # CARVER #  
                    row = box.row(1)                
                    button_draw_carver = icons.get("icon_draw_carver")        
                    if tp_props.display_carver_util: 
                        row.prop(tp_props, "display_carver_util", text="", icon_value=button_draw_carver.icon_id) 
                        row.label("Carver")                     
                    else:                    
                        row.prop(tp_props, "display_carver_util", text="", icon_value=button_draw_carver.icon_id) 
                        row.label("Carver") 
     
                    if tp_props.display_carver_util: 

                        box.separator()     
                        
                        row = box.column() 
                        row.label(text="Select a mesh to carve", icon="LAYER_USED")
                        row.label(text="Run Carver (HotKey or Panel)", icon="LAYER_USED")
                        row.label(text="To finish press [ESC] or [RIGHT CLICK]", icon="LAYER_USED")
                        row.label(text="More keys in addon preferences", icon="LAYER_USED")
                        
                        row.separator()                
                                                        
                        row.prop(context.scene, "ProfilePrefix", text="Profile prefix")
                        row.prop(context.scene, "CarverSolver", text="Solver")

                        box.separator()
                        box = col.box().column(1)    

                 
                 
                    box.separator() 
                       
                    # SNAPLINE #  
                    row = box.row(1)                
                    button_draw_knife = icons.get("icon_draw_knife")               
                    if tp_props.display_snap_util: 
                        row.prop(tp_props, "display_snap_util", text="", icon_value=button_draw_knife.icon_id) 
                        row.label("SnapLine")                     
                    else:                    
                        row.prop(tp_props, "display_snap_util", text="", icon_value=button_draw_knife.icon_id) 
                        row.label("SnapLine") 
     
                    if tp_props.display_snap_util: 

                        box.separator()     
                        
                        row = box.column() 
                        row.prop(addon_prefs, "outer_verts")

                        row.prop(addon_prefs, "incremental")
                        row.prop(addon_prefs, "increments_grid")
                      
                        if addon_prefs.increments_grid:
                            row.prop(addon_prefs, "relative_scale")
                       
                        row.label(text="Line Tool:")
                        row.prop(addon_prefs, "intersect")
                        row.prop(addon_prefs, "create_face")
                        row.prop(addon_prefs, "create_new_obj")

                        box.separator() 
                        box = col.box().column(1)    


                    box.separator() 
                       
                    # CURVE DRAW #
                    row = box.row(1)                
                    button_draw_lathe = icons.get("icon_draw_lathe")
                    if tp_props.display_cdraw: 
                        row.prop(tp_props, "display_cdraw", text="", icon_value=button_draw_lathe.icon_id) 

                        button_draw_surface = icons.get("icon_draw_surface")     
                        row.label(text="", icon_value=button_draw_surface.icon_id)  
                        
                        button_draw_curve = icons.get("icon_draw_curve")     
                        row.label(text="", icon_value=button_draw_curve.icon_id)  
                                                
                        row.label("Curve Draw")                     
 
                    else:                    
                        row.prop(tp_props, "display_cdraw", text="", icon_value=button_draw_lathe.icon_id) 
                        row.label("Curve Draw")                      
    
                        button_draw_surface = icons.get("icon_draw_surface")     
                        row.label(text="", icon_value=button_draw_surface.icon_id)  
                        
                        button_draw_curve = icons.get("icon_draw_curve")     
                        row.label(text="", icon_value=button_draw_curve.icon_id)                          
                        

                    if tp_props.display_cdraw:                         

                        scene = context.scene  

                        row.prop(scene, "add_bevel", text ="", icon="MOD_WARP")   

                        box.separator()

                        row = box.row(1)                  
                        tool_settings = context.tool_settings
                        cps = tool_settings.curve_paint_settings
                        row.prop(cps, "radius_taper_start", text="Start")
                        row.prop(cps, "radius_taper_end", text="End")

                        box.separator()          
                        box.separator()                           
                                                                             
                        row = box.row(1)                              
                        row.prop(scene.tp_props_insert, "add_mat", text ="")                 
                        row.label(text="Add Color:")  
                       
                        row.prop(scene.tp_props_insert, "add_objmat", text ="", icon="GROUP_VCOL")                   
                        
                        obj = context.active_object
                       
                        if scene.tp_props_insert.add_random == False:       
                            if scene.tp_props_insert.add_objmat == False:                     
                                if bpy.context.scene.render.engine == 'CYCLES':
                                    row.prop(scene.tp_props_insert, "add_cyclcolor", text ="")        
                                else:
                                    row.prop(scene.tp_props_insert, "add_color", text ="")       
                            else:
                                
                                if obj:    
                                    if context.object.active_material:  
                                        row.prop(context.object.active_material, "diffuse_color", text="")
                                    else:
                                        row.label(text="")   
                                else:
                                    pass               
                        else:
                           
                            if scene.tp_props_insert.add_objmat == False:                            
                                
                                if bpy.context.scene.render.engine == 'CYCLES':
                                    row.prop(scene.tp_props_insert, "add_cyclcolor", text ="")        
                                else:
                                    row.prop(scene.tp_props_insert, "add_color", text ="")                                                   
                            
                            else:                           
                           
                                if obj:   
                                    if context.object.active_material:  
                                        row.prop(context.object.active_material, "diffuse_color", text="")
                                    else:
                                        row.label(text="")            
                                else:
                                    pass
                                       
                        row.prop(scene.tp_props_insert, "add_random", text ="", icon="FILE_REFRESH")
                      
                       
                        obj = context.active_object     
                        if obj:
                           
                            if len(context.object.material_slots) > 0:

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
                        else:
                            pass     
                                             
                        box.separator()










        ## TOOLS OBJECTMODE ##        
        if context.mode in UI_OBM:             
           
            obj = context.active_object     
            if obj:

                # ORIGIN #
                display_origin = context.user_preferences.addons[__package__].preferences.tab_origin_ui
                if display_origin == True:

                    draw_origin_ui(self, context, layout) 


                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'MESH'}:  
     
                        # SURFACE CONSTRAINT #
                        display_surface = context.user_preferences.addons[__package__].preferences.tab_surface_ui
                        if display_surface == True:
                            
                            draw_surface_constraint_ui(self, context, layout)            


                        # SNAPSHOT #
                        display_snapshot = context.user_preferences.addons[__package__].preferences.tab_snapshot_ui
                        if display_snapshot == True: 

                            draw_snapshot_ui(self, context, layout)

                  
                        # BOOELAN #
                        display_boolean = context.user_preferences.addons[__package__].preferences.tab_boolean_ui
                        if display_boolean == True:  
                            
                            draw_boolean_ui(self, context, layout)


                # ALIGN #
                display_align = context.user_preferences.addons[__package__].preferences.tab_align_ui
                if display_align == True:  
                    
                    draw_align_ui(self, context, layout)


                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'MESH'}:  

                        # SYMDIM #
                        display_symdim = context.user_preferences.addons[__package__].preferences.tab_symdim_ui
                        if display_symdim == True:   
                            
                            draw_symdim_ui(self, context, layout)  


                # COPY #
                display_copy = context.user_preferences.addons[__package__].preferences.tab_copy_ui
                if display_copy == True:  

                    draw_copy_ui(self, context, layout)  


                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'MESH'}:  

                        # MIRAWRAP #
                        display_miratools= context.user_preferences.addons[__package__].preferences.tab_miratools_ui
                        if display_miratools == True:             
                        
                            draw_mirawrap_ui(self, context, layout)
                

                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'MESH'}:  

                        # BIPED #
                        display_skin= context.user_preferences.addons[__package__].preferences.tab_biped_ui
                        if display_skin == True:             
                        
                            draw_biped_ui(self, context, layout)
                            
                                                        
                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'MESH'}:  

                        # RECOPLANAR #
                        display_recoplanar = context.user_preferences.addons[__package__].preferences.tab_recoplanar_ui
                        if display_recoplanar == True:  

                            draw_recoplanar_ui(self, context, layout)  


                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'CURVE'}:  

                        # CURVE #
                        display_curve = context.user_preferences.addons[__package__].preferences.tab_curve_ui 
                        if display_curve == True:  

                            draw_curve_ui(self, context, layout) 


  
                # TRANSFORM #
                display_transform = context.user_preferences.addons[__package__].preferences.tab_transform_ui 
                if display_transform == True:  

                    draw_transform_ui(self, context, layout)           
                          

#                # PENCIL #
#                display_pencil = context.user_preferences.addons[__package__].preferences.tab_pencil_ui
#                if display_pencil == True:  

#                    draw_pencil_ui(self, context, layout) 


                obj = context.active_object     
                if obj:
                   obj_type = obj.type                                                   
                   if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:  
               
                        # Convert #
                        display_convert = context.user_preferences.addons[__package__].preferences.tab_convert_ui
                        if display_convert == True: 
                            
                            draw_convert_ui(self, context, layout)         

            

            else:
                pass



        ## TOOLS MESH EDITMODE ##
        if context.mode in UI_EDM:       

            # INSERT #               
            display_insert = context.user_preferences.addons[__package__].preferences.tab_create_ui
            if display_insert == True:

                draw_add_ui(self, context, layout)


            # BRUSHES #
            col = layout.column(1)
            box = col.box().column(1)                   
            box.separator()        

            if tp_props.display_brushes:

                row = box.row(1) 
                row.prop(tp_props, "display_brushes", text="", icon="PROP_CON")                                                                                                       
                row.label("Brush Properties")                   
               
                box.separator()                
         
            else:           

                row = box.row(1) 
                sub = row.row(1)
                sub.alignment = 'CENTER'    
                sub.scale_x = 2  
                sub.scale_y = 1.7 

                sub.prop(tp_props, "display_brushes", text="", icon="PROP_CON") 

                button_draw_mt = icons.get("icon_draw_mt") 
                sub.operator("mesh.retopomt", text="", icon_value=button_draw_mt.icon_id)   

                button_draw_besurface = icons.get("icon_draw_besurface") 
                sub.operator("tp_gpencil.surfsk_add_surface", text="", icon_value=button_draw_besurface.icon_id)     

                button_draw_poly = icons.get("icon_draw_poly")     
                sub.operator("mira.poly_loop", text="", icon_value=button_draw_poly.icon_id)              

                button_draw_fast = icons.get("icon_draw_fast") 
                sub.operator("tp_ops.fastloop", text="", icon_value=button_draw_fast.icon_id)   
 
                button_draw_meshbrush = icons.get("icon_draw_meshbrush") 
                sub.operator("mesh.sct_mesh_brush", text = "", icon_value=button_draw_meshbrush.icon_id)    

                button_draw_knife = icons.get("icon_draw_knife")   
                sub.operator("tp_ops.snapline", text="", icon_value=button_draw_knife.icon_id)       

                box.separator()  


            if tp_props.display_brushes:            
               
                box.separator()   

                # MT-RETOPO #
                row = box.row(1)                
                button_draw_mt = icons.get("icon_draw_mt")
                if tp_props.display_retopo_mt: 
                    row.prop(tp_props, "display_retopo_mt", text="", icon_value=button_draw_mt.icon_id) 
                    row.label("RetopoMT")                     
                else:                    
                    row.prop(tp_props, "display_retopo_mt", text="", icon_value=button_draw_mt.icon_id) 
                    row.label("RetopoMT")

                if tp_props.display_retopo_mt: 
                    
                    box = col.box().column(1)
                    
                    row = box.row(1) 
                    row.prop(context.space_data, "lens")
                    
                    box.separator() 
                    box = col.box().column(1)     
     
        

                # BSURFACE #  
                row = box.row(1)                
                button_draw_besurface = icons.get("icon_draw_besurface")                 
                if tp_props.display_bsurface_edm: 
                    row.prop(tp_props, "display_bsurface_edm", text="", icon_value=button_draw_besurface.icon_id) 
                    row.label("BSurface")                     
                else:                    
                    row.prop(tp_props, "display_bsurface_edm", text="", icon_value=button_draw_besurface.icon_id) 
                    row.label("BSurface") 
                
                if tp_props.display_bsurface_edm:  
                    
                    box = col.box().column(1)

                    row = box.row(1)                                                                     
                    row.operator("tp_gpencil.surfsk_add_surface", text="Add Surface")
                    row.operator("tp_gpencil.surfsk_edit_strokes", text="Edit Strokes")

                    box.separator() 
                    box.separator() 
                    
                    row = box.column(1) 
                    tp_scn = context.scene.tp_bsurfaces 
                    row.prop(tp_scn, "SURFSK_cyclic_cross")
                    row.prop(tp_scn, "SURFSK_cyclic_follow")
                    row.prop(tp_scn, "SURFSK_loops_on_strokes")
                    row.prop(tp_scn, "SURFSK_automatic_join")                               
                    row.prop(tp_scn, "SURFSK_keep_strokes")  
                               
                    box.separator()   
                    box.separator()  

                    box.separator()  
                    
                    row = box.row(1)                          
                    if context.space_data.type == 'VIEW_3D':
                        row.prop(context.tool_settings, "grease_pencil_source", expand=True)
                        
                        row = box.row(1)
                        row.prop_enum(context.tool_settings, "gpencil_stroke_placement_view3d", 'SURFACE')
                        row.prop_enum(context.tool_settings, "gpencil_stroke_placement_view3d", 'VIEW')

                    box.separator() 
                    box = col.box().column(1)     

              
              
                # POLYMESH #                
                row = box.row(1)  
                button_draw_poly = icons.get("icon_draw_poly")               
                if tp_props.display_polymesh: 
                    row.prop(tp_props, "display_polymesh", text="", icon_value=button_draw_poly.icon_id) 
                    row.label("PolyMesh")                     
                else:                    
                    row.prop(tp_props, "display_polymesh", text="", icon_value=button_draw_poly.icon_id) 
                    row.label("PolyMesh")                 
                
                if tp_props.display_polymesh: 
                    
                    box = col.box().column(1)

                    row = box.column(1) 
                    row.prop(context.scene.mi_settings, "surface_snap", text='Toggle Surface Snap', icon ="SNAP_SURFACE")  

                    box.separator() 
                    box = col.box().column(1)     
           

     
                # MESHBRUSH #  
                row = box.row(1)                
                button_draw_meshbrush = icons.get("icon_draw_meshbrush")  
                if tp_props.display_meshbrush: 
                    row.prop(tp_props, "display_meshbrush", text="", icon_value=button_draw_meshbrush.icon_id) 
                    row.label("MeshBrush")                     
                else:                    
                    row.prop(tp_props, "display_meshbrush", text="", icon_value=button_draw_meshbrush.icon_id) 
                    row.label("MeshBrush") 

                if tp_props.display_meshbrush: 

                    box = col.box().column(1)

                    row = box.column(1) 
                    row.prop(props, "iterations")
                    row.prop(props, "radius", slider = True)
                    row.prop(props, "spacing", slider = True)

                    box.separator()
                    
                    row = box.column(1)

                    draw_display_properties_ui(row)
                    draw_falloff_ui(row)
                    draw_options_ui(row)
                    draw_symmetry_ui(row)
                   
                    box.separator() 
                    box = col.box().column(1)                                         
               

               
                # SNAPLINE #  
                row = box.row(1)                
                button_draw_knife = icons.get("icon_draw_knife")               
                if tp_props.display_snap_util: 
                    row.prop(tp_props, "display_snap_util", text="", icon_value=button_draw_knife.icon_id) 
                    row.label("SnapLine")                     
                else:                    
                    row.prop(tp_props, "display_snap_util", text="", icon_value=button_draw_knife.icon_id) 
                    row.label("SnapLine") 
 
                if tp_props.display_snap_util: 

                    box = col.box().column(1)
                    
                    row = box.column() 
                    row.prop(addon_prefs, "outer_verts")

                    row.prop(addon_prefs, "incremental")
                    row.prop(addon_prefs, "increments_grid")
                  
                    if addon_prefs.increments_grid:
                        row.prop(addon_prefs, "relative_scale")
                   
                    row.label(text="Line Tool:")
                    row.prop(addon_prefs, "intersect")
                    row.prop(addon_prefs, "create_face")
                    row.prop(addon_prefs, "create_new_obj")

     

            box.separator() 


            # EDITING #
            display_edit = context.user_preferences.addons[__package__].preferences.tab_edit_ui
            if display_edit == True:

                draw_edit_ui(self, context, layout) 


            # ORIGIN #
            display_origin = context.user_preferences.addons[__package__].preferences.tab_origin_ui
            if display_origin == True:

                draw_origin_ui(self, context, layout) 
           

            # SURFACE CONSTRAINT #
            display_surface = context.user_preferences.addons[__package__].preferences.tab_surface_ui
            if display_surface == True:
                 
                draw_surface_constraint_ui(self, context, layout)   
                draw_shrinkwrap_ui(self, context, layout)                            


            # BOOLEAN #
            display_boolean = context.user_preferences.addons[__package__].preferences.tab_boolean_ui
            if display_boolean == True:   
                
                draw_boolean_ui(self, context, layout)  


            # ALIGN #
            display_align = context.user_preferences.addons[__package__].preferences.tab_align_ui
            if display_align == True:   
                
                draw_align_ui(self, context, layout)  


            # SYMDIM #
            display_symdim = context.user_preferences.addons[__package__].preferences.tab_symdim_ui
            if display_symdim == True:   
                
                draw_symdim_ui(self, context, layout)  


            # MIRASTRETCH # 
            display_mirastretch = context.user_preferences.addons[__package__].preferences.tab_mirastretch_ui
            if display_mirastretch == True: 
                
                draw_mirastretch_ui(self, context, layout)


            # MIRAGUIDE # 
            display_miraguide = context.user_preferences.addons[__package__].preferences.tab_miraguide_ui
            if display_miraguide == True: 
                
                draw_miraguide_ui(self, context, layout)


            # PENCIL #
            display_pencil = context.user_preferences.addons[__package__].preferences.tab_pencil_ui
            if display_pencil == True:  

                draw_pencil_ui(self, context, layout)  
            

            # SPACE #
            display_spacing = context.user_preferences.addons[__package__].preferences.tab_spacing_ui
            if display_spacing == True:  
                
                draw_spacing_ui(self, context, layout)
                

            # RELAX #
            display_relax = context.user_preferences.addons[__package__].preferences.tab_relax_ui
            if display_relax == True:  
                
                draw_relax_ui(self, context, layout)        


            # BIPED #
            display_skin= context.user_preferences.addons[__package__].preferences.tab_biped_ui
            if display_skin == True:             
            
                draw_biped_ui(self, context, layout)
             
          
            # MESHCHECK #           
            display_check = context.user_preferences.addons[__package__].preferences.tab_check_ui
            if display_check == True:  

                draw_check_ui(self, context, layout)  



        ## TOOLS CURVE EDITMODE ##
        if context.mode in UI_CEDM:       
          
            # ORIGIN #
            display_origin = context.user_preferences.addons[__package__].preferences.tab_origin_ui
            if display_origin == True:

                draw_origin_ui(self, context, layout) 

            # ALIGN #
            display_align = context.user_preferences.addons[__package__].preferences.tab_align_ui
            if display_align == True:  
                
                draw_axis_ui(self, context, layout)

            draw_curve_ui(self, context, layout)



        # CUSTOM #
        display_custom = context.user_preferences.addons[__package__].preferences.tab_custom_ui
        if display_custom == True: 
            
            draw_custom_ui(self, context, layout)   

     

        ## TOOLS MESH EDITMODE ##
        if context.mode in UI_EDM:

            # MIRATOOLS COMPLETE # 
            display_miratools= context.user_preferences.addons[__package__].preferences.tab_miratools_ui
            if display_miratools == True: 
                                                   
                draw_miratools_ui(self, context, layout)


        if context.mode in UI_LEDM:
          
            draw_lattice_ui(self, context, layout)
       
        else:

            obj = context.active_object     
            if obj:

                # MODIFIER #
                display_modifier = context.user_preferences.addons[__package__].preferences.tab_modifier_ui
                if display_modifier == True:                                         
                
                    draw_modifier_ui(self, context, layout)   
            else:
                pass



        # VISUALS #    
        display_visual = context.user_preferences.addons[__package__].preferences.tab_visual_ui
        if display_visual == True:

            draw_visual_ui(self, context, layout)       





        # MAIN PANEL ------------------------------------------------------------------------------


        # HISTORY #  
        display_history = context.user_preferences.addons[__package__].preferences.tab_history_ui
        if display_history == True:

            box = layout.box().column(1)  

          
            ## TOOLS OBJECTMODE ##
            if context.mode in UI_OBM:
                
                obj = context.active_object     
                if obj:
                   obj_type = obj.type
                                                       
                   if obj_type in {'MESH'}:  

                       row = box.row(1)
                       row.prop(bpy.context.scene, "Keep_Origin_Point","",icon="NDOF_DOM")
                       row.operator("tp_ops.multiedit_enter_operator", icon="BLANK1")
                       
                       box.separator()
        
         
            ## TOOLS MESH EDITMODE ##            
            if context.mode in UI_EDM:

               row = box.row(1)
               row.prop(bpy.context.scene, "Keep_Origin_Point","",icon="NDOF_DOM")
               row.operator("tp_ops.multiedit_exit_operator", icon="BLANK1")

               box.separator()                       

            row = box.row(1)        
            if tp_props.display_docu:
                row.prop(tp_props, "display_docu", text="", icon='SCRIPTWIN')
            else:
                row.prop(tp_props, "display_docu", text="", icon='SCRIPTWIN')     

            row.operator("view3d.ruler", text="Ruler")            
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="FRAME_PREV")
            row.operator("ed.redo", text="", icon="FRAME_NEXT") 
           
            box.separator()   

            if tp_props.display_docu:                
                
                col = layout.column(align=True)                
               
                box = col.box().column(1)             

                row = box.row(1)
                #row.prop(tp_props, "display_help", text="View Help", icon='INFO')    
                row.operator("wm.url_open", text="Open Wiki", icon='QUESTION').url = "https://github.com/mkbreuer/ToolPlus/wiki"             
            
                box.separator() 

                row = box.row(1)
                wm = context.window_manager    
                row.operator("wm.save_userpref", icon='FILE_TICK')   
                row.operator("wm.restart_blender", text="", icon='LOAD_FACTORY')  
            
                panel_prefs = context.user_preferences.addons[__package__].preferences
                expand = panel_prefs.expand_panel_tools

                box.separator() 
         
                row = box.row(1)                  
                row.prop(panel_prefs, "tools_category", text="Category")   
              
                box.separator() 
               
                row = box.row(1)   
                row.prop(panel_prefs, 'tab_location', expand=True)   
                
                box.separator()  

                panel_prefs = context.user_preferences.addons[__package__].preferences
                expand = panel_prefs.expand_panel_tools
              
                row = box.column_flow(2)
                                                    
                row.prop(panel_prefs, 'tab_add_ui')                                       
                row.prop(panel_prefs, 'tab_title_ui')                                       
                row.prop(panel_prefs, 'tab_pivot_ui')                                       
                row.prop(panel_prefs, 'tab_create_ui')                                       
                row.prop(panel_prefs, 'tab_origin_ui')                                       
                row.prop(panel_prefs, 'tab_surface_ui')
                row.prop(panel_prefs, 'tab_snapshot_ui')
                row.prop(panel_prefs, 'tab_boolean_ui')
                row.prop(panel_prefs, 'tab_align_ui')
                row.prop(panel_prefs, 'tab_symdim_ui')
                row.prop(panel_prefs, 'tab_copy_ui')
                row.prop(panel_prefs, 'tab_edit_ui')
                row.prop(panel_prefs, 'tab_mirastretch_ui')
                row.prop(panel_prefs, 'tab_miraguide_ui')                        
                row.prop(panel_prefs, 'tab_pencil_ui')
                row.prop(panel_prefs, 'tab_spacing_ui')
                row.prop(panel_prefs, 'tab_relax_ui')
                row.prop(panel_prefs, 'tab_check_ui')     
                row.prop(panel_prefs, 'tab_mirawrap_ui')           
                row.prop(panel_prefs, 'tab_recoplanar_ui')          
                row.prop(panel_prefs, 'tab_transform_ui')          
                row.prop(panel_prefs, 'tab_convert_ui')
                row.prop(panel_prefs, 'tab_miratools_ui')
                row.prop(panel_prefs, 'tab_modifier_ui')
                row.prop(panel_prefs, 'tab_biped_ui')     
                row.prop(panel_prefs, 'tab_visual_ui')          
                row.prop(panel_prefs, 'tab_history_ui') 
                row.prop(panel_prefs, 'tab_custom_ui')
                
                box.separator() 
                box = col.box().column(1)  
                box.separator() 

            
            row = box.row(1)             
            row.label( text="", icon = "LAYER_USED")                        
           

            ## MODE TOGGLE ##
            if context.mode in UI_OBM:
                row.operator("object.editmode_toggle", text="Edit", icon = "EDIT")    
            else:
                row.operator("object.editmode_toggle", text="Object", icon = "OBJECT_DATAMODE")                
            row.operator("sculpt.sculptmode_toggle", text="Sculpt", icon = "SCULPTMODE_HLT") 
   
            row.label( text="", icon = "LAYER_USED")

            box.separator()
 

 
# LOAD PANEL #  

class VIEW3D_TP_ReSurface_Panel_TOOLS(bpy.types.Panel, draw_layout_resurface):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_ReSurface_Panel_TOOLS"
    bl_label = "ReSurface"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'   
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_ReSurface_Panel_UI(bpy.types.Panel, draw_layout_resurface):
    bl_idname = "VIEW3D_TP_ReSurface_Panel_UI"
    bl_label = "ReSurface"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  
    bl_options = {'DEFAULT_CLOSED'}

