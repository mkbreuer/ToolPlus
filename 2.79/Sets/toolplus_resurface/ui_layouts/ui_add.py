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
import addon_utils

icons = load_icons()
types_one =  [("tp_c0"    ," "   ," "   ,"COLLAPSEMENU"         ,0),
              ("tp_c1"    ," "   ," "   , icons["icon_select_object"].icon_id ,1), 
              ("tp_c2"    ," "   ," "   ,"FONT_DATA"            ,2), 
              ("tp_c3"    ," "   ," "   ,"EXPORT"               ,3),
              ("tp_c4"    ," "   ," "   ,"RETOPO"               ,4),
              ("tp_c5"    ," "   ," "   ,"BBOX"                 ,5),
              ("tp_c6"    ," "   ," "   ,"MATCUBE"              ,6)]

bpy.types.Scene.tp_create = bpy.props.EnumProperty(name = " ", default = "tp_c0", items = types_one)


def draw_add_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface            
        tp = context.window_manager.tp_props_bbox      
       
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        ob = context.object  
        obj = context.object
        scene = bpy.context.scene
        scn = context.scene
        rs = scene 

        col = layout.column(1)
         

        if context.mode == 'OBJECT': 

            box = col.box().column(1) 

            row = box.row(1)  
            row.prop(scene, 'tp_create', emboss = False, expand = True) #icon_only=True,


            if scene.tp_create == "tp_c0": 
                pass


            if scene.tp_create == "tp_c1": 
               
                box = col.box().column(1)

                box.separator()  

                row = box.row(1)                                 
                row.operator("view3d.select_border", text="Border", icon="BORDER_RECT") 
                row.operator("view3d.select_circle", text="Cirlce", icon="BORDER_LASSO")           

                box.separator()         

                row = box.row(1)          
                row.operator("object.move_to_layer", text="Move to Layer")  
                row.menu("VIEW3D_MT_object_showhide", "Hide / Show", icon = "VISIBLE_IPO_ON")

                box.separator() 

                row = box.row(1)

                row = box.row(1)
                sub = row.row()
                sub.scale_x = 0.3
                sub.operator("object.select_more",text="+")
                sub.operator("object.select_all",text="All").action = 'TOGGLE'
                sub.operator("object.select_less",text="-")   

                box.separator() 
         
                row = box.row(1)         
                row.operator("object.select_by_layer", text="All by Layer")
                row.operator("tp_ops.cycle_selected", text="CycleThrough")                       
                
                row = box.row(1)
                sub = row.row(1)
                sub.scale_x = 0.5
                sub.operator("view3d.view_selected"," ", icon = "ZOOM_SELECTED" )
                sub.operator("view3d.view_all"," ", icon = "ZOOM_OUT" )  
                row.operator("object.select_linked", text="Get Active").type='OBDATA'

                box.separator() 

                row = box.row(1)    
                row.operator("object.select_mirror", text="Mirror") 
                row.operator("object.select_all", text="Inverse").action = 'INVERT'

                row = box.row(1)              
                row.operator("object.select_random", text="Random")
                row.operator("object.select_camera", text="Camera")            

                box.separator() 

                row = box.row(1) 
                row.operator("object.select_linked", text="Linked", icon="EXPORT") 
                row.operator("object.select_grouped", text="Group", icon="EXPORT")        
            
                row = box.row(1) 
                row.operator("object.select_by_type", text="Type", icon="EXPORT")        
                row.operator("object.select_pattern", text="Name", icon="EXPORT")  

                box.separator() 
                box.separator() 
                                    
                row = box.row(1)
                row.operator("tp_ops.unfreeze_selected", text = "UnFreeze All", icon = "RESTRICT_SELECT_OFF")
                row.operator("tp_ops.freeze_selected", text = "Freeze", icon = "FREEZE")

                row = box.row(1)   
                row.operator("object.mesh_all", text= " ", icon="OBJECT_DATAMODE")
                row.operator("object.lamp_all",text=" ", icon="LAMP")
                row.operator("object.curve_all",text=" ", icon="OUTLINER_OB_CURVE")
                row.operator("object.bone_all",text=" ", icon="BONE_DATA")
                row.operator("object.particles_all", text=" ", icon="MOD_PARTICLES")
                row.operator("object.camera_all", text=" ", icon="OUTLINER_DATA_CAMERA")

                box.separator() 

                
            if scene.tp_create == "tp_c2": 

                    box = col.box().column(1)               
                    
                    row = box.row(1)                 
                    row.label("Rename Active", icon="PMARKER")            
                   
                    box.separator()

                    row = box.row(1)                 
                    row.prop(context.object , "name", text="Name", icon = "COPY_ID") 
                    row.operator("tp_ops.copy_name_to_meshdata", text= "", icon ="PASTEDOWN")

                    row = box.row(1)      
                    row.prop(context.object.data , "name", text="Data", icon = "OUTLINER_DATA_MESH") 
                    row.operator("tp_ops.copy_data_name_to_object", text= "", icon ="COPYDOWN")
                    
                    box.separator()
                    box.separator()                 
                    
                    row = box.row(1)                 
                    row.label("Rename Selected", icon="PMARKER")            
                   
                    box.separator()

                    row = box.row(1) 
                    row.prop(context.scene,"rno_str_new_name", "Name",)
                    
                    box.separator() 
                            
                    row = box.row(1)    
                    row.prop(context.scene,"rno_bool_numbered", text="")
                    row.label("Numbered:")
                    row.prop(context.scene,"rno_str_numFrom")
                    
                    box.separator() 
                            
                    row = box.row(1)
                    row.operator("object.rno_setname", "  Set new Name", icon ="FONT_DATA")

                    if tp_props.display_rename: 
                        row.prop(tp_props, "display_rename", text="", icon="SCRIPTWIN")  
                        box.separator()
                    else:                  
                        row.prop(tp_props, "display_rename", text="", icon="SCRIPTWIN")  
               
                    box.separator() 


                    if tp_props.display_rename: 
                                    
                        box.separator()                    

                        row = box.column(1)              
                        row.prop(context.scene, "rno_str_old_string", text="Old: ")
                        row.prop(context.scene, "rno_str_new_string", text="New: ")
                        
                        box.separator()
                        
                        row = box.row(1)
                        button_baply = icons.get("icon_baply")                          
                        row.operator("object.rno_replace_in_name", "Replace String Name", icon_value=button_baply.icon_id)

                        box.separator()                   
                        box.separator()                   

                        row = box.row(1) 
                        row.prop(context.scene,'rno_bool_keepIndex', text='Keep Object Index')
                       
                        row = box.column(1)
                        row.prop(context.scene, "rno_str_prefix")
                        row.prop(context.scene, "rno_str_subfix")     

                        box.separator()      
                        
                        row = box.row(1)        
                        button_baply = icons.get("icon_baply") 
                        row.operator("object.rno_add_subfix_prefix", "Add Prefix / Subfix", icon_value=button_baply.icon_id) 

                    box.separator()        
                      

            if scene.tp_create == "tp_c3":
                
                
                box = col.box().column(1) 
               
                box.separator()                 
               
                row = box.row(1) 
                row.menu("INFO_MT_file_export", icon='IMPORT')
                row.menu("INFO_MT_file_import", icon='EXPORT')

                row = box.row(1) 
           
                obj = context.active_object     
                if obj:
                   obj_type = obj.type
                                                                 
                   if obj_type in {'CURVE'}:
                       row.operator("export_svg_format.svg", text="Export SVG", icon='IMPORT')

                row.menu("OBJECT_MT_selected_export", text="Export Selected", icon='IMPORT')

               
                asset_flinger_addon = "add_mesh_asset_flinger" 
                state = addon_utils.check(asset_flinger_addon)
                if not state[0]:
                    pass
                else:  
                    row.operator("view3d.asset_flinger", icon='EXPORT')

                box.separator()  
                box.separator()  

                row = box.row(1)            
                row.operator_context = 'INVOKE_AREA'
                row.operator("wm.link", text="Link", icon='LINK_BLEND')
                row.operator("wm.append", text="Append", icon='APPEND_BLEND')
                           
                row = box.row(1)   
                row.operator("object.make_local")
                row.operator("object.proxy_make")
            
                box.separator()  
                box.separator()  

                
                row = box.row(1) 
                if tp_props.display_pathes:
                    row.prop(tp_props, "display_pathes", text="...Pack & Pathes...", icon='SCRIPTWIN')
                else:
                    row.prop(tp_props, "display_pathes", text="...Pack & Pathes...", icon='SCRIPTWIN')

                row.operator('wm.path_open',  text = '', icon = 'FILESEL').filepath = "C:\\Users\Public\Documents"   


                if tp_props.display_pathes:                    

                    box = col.box().column(1) 
                    
                    row = box.row(1)  
                    icon = 'CHECKBOX_HLT' if bpy.data.use_autopack else 'CHECKBOX_DEHLT'
                    row.operator("file.autopack_toggle", text="", icon=icon) 
                    row.label(text="Autom. Pack into .blend") 

                    row = box.column(1)  

                    pack_all = box.row() 
                    pack_all.operator("file.pack_all")
                    pack_all.active = not bpy.data.use_autopack

                    unpack_all = box.row()
                    unpack_all.operator("file.unpack_all")
                    unpack_all.active = not bpy.data.use_autopack
                    
                    box.separator()              

                    box = col.box().column(1) 
                    
                    row = box.column(1)  
                    row.operator("file.make_paths_relative")
                    row.operator("file.make_paths_absolute")   
                    row.operator("file.report_missing_files")
                    row.operator("file.find_missing_files")

                    box.separator()                             





            if scene.tp_create == "tp_c4": 

                box = col.box().column(1) 
               
                box.separator()  
                
                row = box.row(1) 
                row.prop(context.scene, 'tp_retopo_mesh', expand = True)   

                row = box.row(1)
                row.prop(context.scene, "pl_set_mirror")
                row.prop(context.scene, "pl_set_snap")

                box.separator()    
               
                row = box.row(1) 
                row.operator("tp_ops.set_retopo_mesh", text="Set Retopo Mesh", icon = 'RETOPO')   

                box.separator()    
                

            if scene.tp_create == "tp_c5":                                       

                box = col.box().column(1)

                box.separator()  
                
                row = box.row(1)                 

                button_bbox = icons.get("icon_bbox") 
                if tp_props.display_bbox_set: 
                    row.prop(tp_props, "display_bbox_set", text="", icon_value=button_bbox.icon_id) 
                    box.separator()
                else:                  
                    row.prop(tp_props, "display_bbox_set", text="", icon_value=button_bbox.icon_id)    

                row.label("Boxes")
                
                subA = row.row(1)
                subA.scale_x = 1
                subA.prop(tp, "tp_geom_box",text="")
                subA.prop(tp, "box_meshtype",text="")

                button_baply = icons.get("icon_baply")
                row.operator("tp_ops.bbox_cube",text="", icon_value=button_baply.icon_id)      

                if tp_props.display_bbox_set: 

                    box = col.box().column(1)

                    row = box.column(1)        
                    row.label("", icon="INFO")          
                    row.label(">  Bound geometry around selected objects", icon = "LAYER_USED") 
                    row.label(">  Redo Last [F6]: to change settings on the fly", icon = "LAYER_USED") 
                    row.label(">  Settings: stores last used adjustments", icon = "LAYER_USED") 
                    row.label(">  Operator Presets: store or reset all to default values", icon = "LAYER_USED") 
               
                    box.separator()
                    box = col.box().column(1) 

               
                row = box.row(1)
                button_bcyl = icons.get("icon_bcyl") 
                if tp_props.display_bcyl_set: 
                    row.prop(tp_props, "display_bcyl_set", text="", icon_value=button_bcyl.icon_id)  
                    box.separator()
                else:                  
                    row.prop(tp_props, "display_bcyl_set", text="", icon_value=button_bcyl.icon_id)  

                row.label("Tubes")
                
                subB = row.row(1)
                subB.scale_x = 1
                subB.prop(tp, "tp_geom_tube",text="")
                subB.prop(tp, "tube_meshtype",text="")

                button_baply = icons.get("icon_baply") 
                row.operator("tp_ops.bbox_cylinder", text="", icon_value=button_baply.icon_id)
                 
                if tp_props.display_bcyl_set: 

                    box = col.box().column(1)

                    row = box.column(1)        
                    row.label(text="", icon="INFO")          
                    row.label(">  Bound geometry around selected objects", icon = "LAYER_USED") 
                    row.label(">  Redo Last [F6]: to change settings on the fly", icon = "LAYER_USED") 
                    row.label(">  Settings: stores last used adjustments", icon = "LAYER_USED") 
                    row.label(">  Operator Presets: store or reset all to default values", icon = "LAYER_USED")            
                    
                    box.separator()
                    box = col.box().column(1)          
              
              
                row = box.row(1)
                button_bsph = icons.get("icon_bsph") 
                if tp_props.display_bcyl_set: 
                    row.prop(tp_props, "display_bext_set", text="", icon_value=button_bsph.icon_id)  
                    box.separator()
                else:                  
                    row.prop(tp_props, "display_bext_set", text="", icon_value=button_bsph.icon_id)  

                row.label("Spheres")
                
                subB = row.row(1)
                subB.scale_x = 1
                subB.prop(tp, "tp_geom_sphere",text="")
                subB.prop(tp, "sphere_meshtype",text="")

                button_baply = icons.get("icon_baply") 
                row.operator("tp_ops.bbox_sphere", text="", icon_value=button_baply.icon_id)
                 
                if tp_props.display_bext_set: 

                    box = col.box().column(1)

                    row = box.column(1)
                    row.label(text="", icon="INFO")                               
                    row.label(">  Bound geometry around selected objects", icon = "LAYER_USED") 
                    row.label(">  Redo Last [F6]: to change settings on the fly", icon = "LAYER_USED") 
                    row.label(">  Settings: stores last used adjustments", icon = "LAYER_USED") 
                    row.label(">  Operator Presets: store or reset all to default values", icon = "LAYER_USED") 
                                    
                    box.separator()
                    box = col.box().column(1)

                
                row = box.row(1)                 

                button_bsel = icons.get("icon_bsel") 
                if tp_props.display_select: 
                    row.prop(tp_props, "display_select", text="", icon_value=button_bsel.icon_id)  
                    box.separator()
                else:                  
                    row.prop(tp_props, "display_select", text="", icon_value=button_bsel.icon_id)  

                row.label("Select")        

                subA = row.row(1)
                subA.scale_x = 1
                subA.prop(tp, "tp_sel_meshtype", text="")
                subA.prop(tp, "tp_sel", text="")
                
                button_baply = icons.get("icon_baply")       
                row.operator("tp_ops.bbox_select_box",text="", icon_value=button_baply.icon_id) 

                if tp_props.display_select:  

                    box = col.box().column(1)

                    row = box.column(1)
                    row.label(text="", icon="INFO")                               
                    row.label(text="Select all existing boundings in the scene")                               
                    

                box.separator()



            if scene.tp_create == "tp_c6": 

                
                box = col.box().column(1)    

                box.separator()  
                
                row = box.row(1)   
                row.label(text="Mesh:") 
                row.operator("mesh.primitive_ico_sphere_add", icon='MESH_ICOSPHERE', text="")  
                row.operator("mesh.primitive_torus_add", icon='MESH_TORUS', text="")
                row.operator("mesh.primitive_cylinder_add", icon='MESH_CYLINDER', text="")
                row.operator("mesh.primitive_plane_add", icon='MESH_PLANE', text="")
                row.operator("mesh.primitive_cube_add", icon='MESH_CUBE', text="")            
              
                row = box.row(1)
                row.label(text=" ")    
                row.operator("mesh.primitive_monkey_add", icon='MESH_MONKEY', text="")
                row.operator("mesh.primitive_grid_add", icon='MESH_GRID', text="")
                row.operator("mesh.primitive_cone_add", icon='MESH_CONE', text="")
                row.operator("mesh.primitive_circle_add", icon='MESH_CIRCLE', text="")
                row.operator("mesh.primitive_uv_sphere_add" ,icon='MESH_UVSPHERE', text="")

                box.separator()  
                box.separator()  
              
                row = box.row(1)   
                row.label(text="Curve:") 
                #row.operator("curve.new_beveled_curve", icon='PROP_CON', text="")  
                row.operator("tp_ops.beveled_curve", icon='PROP_CON', text="")  

                box.separator()         
                box.separator()         
              
                row = box.row(1)   

                row = box.row(1)   
                row.label(text="Biped:")    

                button_skin_human = icons.get("icon_skin_human")                      
                row.operator("tp_ops.add_skin_human",text="", icon_value=button_skin_human.icon_id)

                button_skin_animal = icons.get("icon_skin_animal")  
                row.operator("tp_ops.add_skin_animal",text="", icon_value=button_skin_animal.icon_id)  

                box.separator()  





        # MESH #     
        if context.mode == 'EDIT_MESH': 

            box = col.box().column(1)       
            
            row = box.row(1) 
            row.alignment = 'CENTER'               
            sub = row.row(1)
            sub.scale_x = 1.9  
            sub.operator("mesh.primitive_plane_add", icon='MESH_PLANE', text="")
            sub.operator("mesh.primitive_cube_add", icon='MESH_CUBE', text="")
            sub.operator("mesh.primitive_circle_add", icon='MESH_CIRCLE', text="")
            sub.operator("mesh.primitive_uv_sphere_add", icon='MESH_UVSPHERE', text="")                 
            sub.operator("mesh.primitive_grid_add", icon='MESH_GRID', text="")   
            sub.operator("mesh.singlevertex",text="", icon = "STICKY_UVS_DISABLE")
              
            row = box.row(1)  
            row.alignment = 'CENTER'                        
            sub = row.row(1)
            sub.scale_x = 1.9 
            sub.operator("mesh.primitive_cylinder_add", icon='MESH_CYLINDER', text="")
            sub.operator("mesh.primitive_torus_add", icon='MESH_TORUS', text="")
            sub.operator("mesh.primitive_cone_add", icon='MESH_CONE', text="")
            sub.operator("mesh.primitive_ico_sphere_add", icon='MESH_ICOSPHERE', text="")   
            sub.operator("tp_ops.edgetubes", text="", icon ="CURVE_DATA") 
            sub.operator("tp_ops.facetube", text="", icon ="CURVE_DATA")           
        
            box.separator()   



        # CURVE #     
        if context.mode == 'EDIT_CURVE': 
                
            box = col.box().column(1)  
              
            row = box.row(1)     
            row.label(text="Curve:") 

            row.operator("curve.primitive_bezier_curve_add", icon='CURVE_BEZCURVE', text="")
            row.operator("curve.primitive_bezier_circle_add", icon='CURVE_BEZCIRCLE', text="")

            box.separator()                 
            box.separator()                 

            row = box.row(1)   
            row.label(text="Nurbs:")  
            row.operator("curve.primitive_nurbs_curve_add", icon='CURVE_NCURVE', text="")
            row.operator("curve.primitive_nurbs_circle_add", icon='CURVE_NCIRCLE', text="")
            row.operator("curve.primitive_nurbs_path_add", icon='CURVE_PATH', text="")    
            
            box.separator()    
            box.separator()    
         
            row = box.row(1)   
            row.label(text="Draw:")  
              
            if not tp_props.display_curve_options: 
                row.prop(tp_props, "display_curve_options", text="", icon="SCRIPTWIN", emboss = False)                
               
                button_draw_bevel = icons.get("icon_draw_bevel")
                row.operator("tp_ops.curve_draw", text="", icon_value=button_draw_bevel.icon_id)    

            else:
                row.prop(tp_props, "display_curve_options", text="", icon="SCRIPTWIN", emboss = False)            
              
                button_draw_bevel = icons.get("icon_draw_bevel")
                row.operator("tp_ops.curve_draw", text="", icon_value=button_draw_bevel.icon_id)                
          
                box.separator()
                box.separator()


                tool_settings = context.tool_settings
                cps = tool_settings.curve_paint_settings

                col = box.column()

                col.prop(cps, "curve_type")

                box.separator()
 
                if cps.curve_type == 'BEZIER':
                    col.label("Bezier Options:")
                    col.prop(cps, "error_threshold")
                    col.prop(cps, "fit_method")
                    col.prop(cps, "use_corners_detect")

                    col = box.column()
                    col.active = cps.use_corners_detect
                    col.prop(cps, "corner_angle")

                box.separator()

                col.label("Pressure Radius:")
                
                row = box.row(align=True)
                rowsub = row.row(align=True)
                rowsub.prop(cps, "radius_min", text="Min")
                rowsub.prop(cps, "radius_max", text="Max")

                row.prop(cps, "use_pressure_radius", text="", icon_only=True)

                box.separator()

                col = box.column()
                col.label("Taper Radius:")
               
                row = box.row(align=True)
                row.prop(cps, "radius_taper_start", text="Start")
                row.prop(cps, "radius_taper_end", text="End")


                box.separator()

                col = box.column()
                col.label("Projection Depth:")
                
                row = box.row(align=True)
                row.prop(cps, "depth_mode", expand=True)

                col = box.column()
                if cps.depth_mode == 'SURFACE':
                    col.prop(cps, "surface_offset")
                    col.prop(cps, "use_offset_absolute")
                    col.prop(cps, "use_stroke_endpoints")
                    
                    if cps.use_stroke_endpoints:
                        colsub = box.column(align=True)
                        colsub.prop(cps, "surface_plane", expand=True)

                box.separator()
                box.separator()                