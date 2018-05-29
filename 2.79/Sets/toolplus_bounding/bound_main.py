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


def draw_panel_layout(context, layout):
    tp_props = context.window_manager.bbox_window
    tp = context.window_manager.tp_props_bbox
    panel_prefs = context.user_preferences.addons[__package__].preferences
    
    icons = load_icons()     
    
    layout.operator_context = 'INVOKE_REGION_WIN'
    
    col = layout.column(1)                                                

    # BOXES #    
    box = col.box().column(1)

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
      
        box.separator()   

        row = box.row(1)
        row.operator("tp_ops.help_bounding_rename", text="", icon="INFO")          
        row.label("ReName:")          
        row.prop(tp, "tp_rename_boxes", text="", icon="SCRIPT")

        box.separator()  

        row = box.column(1)          
        if tp.tp_geom_box == "tp_bb2":
            row.prop(tp, "box_prefix", text="prefix")

            if tp.tp_rename_boxes == True:
                row.prop(tp, "box_name", text="custom")

            if tp.box_meshtype == "tp_00":    
                row.prop(tp, "box_shaded_suffix", text="suffix")

            if tp.box_meshtype == "tp_01":    
                row.prop(tp, "box_shadeless_suffix", text="suffix")

            if tp.box_meshtype == "tp_02":    
                row.prop(tp, "box_wired_suffix", text="suffix")

        else:
            row.prop(tp, "grid_prefix", text="prefix")

            if tp.tp_rename_boxes == True:
                row.prop(tp, "grid_name", text="rename")
            
            if tp.box_meshtype == "tp_00":            
                row.prop(tp, "grid_shaded_suffix", text="suffix")
            
            if tp.box_meshtype == "tp_01":
                row.prop(tp, "grid_shadeless_suffix", text="suffix")
            
            if tp.box_meshtype == "tp_02":
                row.prop(tp, "grid_wired_suffix", text="suffix")

       
        box.separator()              
        box = col.box().column(1)
        box.separator()   

        row = box.row(1)
        row.operator("tp_ops.help_bounding_settings", text="", icon="INFO")          
        row.label("Settings [F6]:")          

        if tp_props.display_bbox_settings: 
            row.prop(tp_props, "display_bbox_settings", text="", icon="SCRIPTWIN") 
            box.separator()
        else:                  
            row.prop(tp_props, "display_bbox_settings", text="", icon="SCRIPTWIN")    

        box.separator()          
        box.separator()  
                    
        row = box.row(1) 
        row.label("Object Type:")               
        row.prop(tp, "tp_geom_box", text="")

        box.separator()   

        row = box.row(1) 
        row.label("Mesh Type:")               
        row.prop(tp, "box_meshtype", text="")
         
        box.separator()              
        box = col.box().column(1)
        box.separator()    

        if tp_props.display_bbox_settings: 
           
            row = box.row(1) 
            row.prop(tp, "box_dim", text="") 
            row.label("Copy Scale")              
                           
            row.separator()
            
            row.prop(tp, "box_dim_apply", text="")     
            row.label("Apply Scale") 
      
            box.separator()

            if tp.tp_geom_box == "tp_bb2":

                box.separator()

                row = box.row(1) 
                row.prop(tp, "box_subdiv_use", text="")
                row.label("Subdivide:") 

                sub = row.row(1)
                sub.scale_x = 1.175
                sub.prop(tp, "box_subdiv")
         
                row = box.row(1)        
                row.label("", icon ="BLANK1") 
                row.label(" ") 
                
                sub = row.row(1)
                sub.scale_x = 1.175         
                sub.prop(tp, "box_subdiv_smooth")


            if tp.tp_geom_box == "tp_bb1": 

                box.separator()
              
                row = box.row(1) 
                row.label("Resolution:") 
                
                sub0 = row.column(1)
                sub0.scale_x = 1

                sub0.prop(tp, "subX")
                sub0.prop(tp, "subY")           
                if tp.box_dim == False:  

                    box.separator()  

                    row = box.row(1) 
                    row.label("Dimension:") 
                  
                    sub0 = row.column(1)
                    sub0.prop(tp, "subR")

            else:
                if tp.box_dim == False:

                    box.separator()

                    row = box.row(1) 
                    row.label("Dimension:") 
                    
                    sub0 = row.column(1)
                    sub0.scale_x = 1

                    if context.space_data.local_view is not None:                
                        sub0.prop(tp, "bcube_rad", text="")
                    else:                
                        sub0.prop(tp, "scale", text="")

            box.separator()
            box.separator()
             
            row = box.row(1) 
            row.label("Copy Rotation:") 
            row.prop(tp, "box_rota", text="") 
                
            if tp.tp_geom_box == "tp_bb1":

                if tp.box_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "bgrid_rota_x")             
                    row.prop(tp, "bgrid_rota_y")             
                    row.prop(tp, "bgrid_rota_z")    
         
            else:

                if tp.box_rota == True:
                    pass
                else:

                    if context.space_data.local_view is not None:
                        #bpy.ops.view3d.localview()
                        row = box.row(1)             
                        row.prop(tp, "bcube_rota_x")             
                        row.prop(tp, "bcube_rota_y")             
                        row.prop(tp, "bcube_rota_z")   

                    else:
                        row = box.row(1)             
                        row.prop(tp, "rotation", text="")  

                
            box.separator()              
            box = col.box().column(1)
            box.separator()       

            row = box.row(1)   
            row.prop(tp, "box_origin", icon="BLANK1", text="")
            row.prop(tp, "box_xray", icon="BLANK1")   

            row = box.row(1)        
            row.prop(tp, "box_smooth", icon="BLANK1")
            row.prop(tp, "box_edges", icon="BLANK1")     


            if tp.tp_geom_box == "tp_bb1":

                box.separator()   
                box = col.box().column(1)      
                box.separator()  

                row = box.row(1) 
                row.prop(tp, "box_sphere_use")

                row = box.row(1) 
                row.prop(tp, "box_sphere")
                            
              
            box.separator()   
            box = col.box().column(1)      
            box.separator()  

            row = box.row(1) 
            row.prop(tp, "box_bevel_use")
            row.prop(tp, "box_verts_use")
                
            row = box.row(1) 
            row.prop(tp, "box_segment")
            
            row = box.row(1)           
            row.prop(tp, "box_offset")
            
            row = box.row(1)            
            row.prop(tp, "box_profile")

            box.separator()
            box = col.box().column(1)      

    box.separator()


    # TUBES #    
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

        box.separator() 
        box = col.box().column(1)
        box.separator() 

        row = box.row(1)
        row.operator("tp_ops.help_bounding_rename", text="", icon="INFO")          
        row.label("ReName:")          
        row.prop(tp, "tp_rename_tubes", text="", icon="SCRIPT")

        box.separator()  

        row = box.column(1)          
        if tp.tp_geom_tube == "tp_add_cyl":   
                     
            row.prop(tp, "bcyl_prefix", text="prefix")

            if tp.tp_rename_tubes == True:   
                row.prop(tp, "bcyl_name", text="custom")

            if tp.tube_meshtype == "tp_00":    
                row.prop(tp, "bcyl_shaded_suffix", text="suffix")

            if tp.tube_meshtype == "tp_01":    
                row.prop(tp, "bcyl_shadeless_suffix", text="suffix")

            if tp.tube_meshtype == "tp_02":    
                row.prop(tp, "bcyl_wired_suffix", text="suffix")


        if tp.tp_geom_tube == "tp_add_cone":

            row.prop(tp, "bcon_prefix", text="prefix")

            if tp.tp_rename_tubes == True:   
                row.prop(tp, "bcon_name", text="rename")
            
            if tp.tube_meshtype == "tp_00":            
                row.prop(tp, "bcon_shaded_suffix", text="suffix")
            
            if tp.tube_meshtype == "tp_01":
                row.prop(tp, "bcon_shadeless_suffix", text="suffix")
            
            if tp.tube_meshtype == "tp_02":
                row.prop(tp, "bcon_wired_suffix", text="suffix")


        if tp.tp_geom_tube == "tp_add_circ":

            row.prop(tp, "bcirc_prefix", text="prefix")

            if tp.tp_rename_tubes == True:       
                row.prop(tp, "bcirc_name", text="rename")
            
            if tp.tube_meshtype == "tp_00":            
                row.prop(tp, "bcirc_shaded_suffix", text="suffix")
            
            if tp.tube_meshtype == "tp_01":
                row.prop(tp, "bcirc_shadeless_suffix", text="suffix")
            
            if tp.tube_meshtype == "tp_02":
                row.prop(tp, "bcirc_wired_suffix", text="suffix")
      

        if tp.tp_geom_tube == "tp_add_tor":

            row.prop(tp, "btor_prefix", text="prefix")
           
            if tp.tp_rename_tubes == True:   
                row.prop(tp, "btor_name", text="rename")
            
            if tp.tube_meshtype == "tp_00":            
                row.prop(tp, "btor_shaded_suffix", text="suffix")
            
            if tp.tube_meshtype == "tp_01":
                row.prop(tp, "btor_shadeless_suffix", text="suffix")
            
            if tp.tube_meshtype == "tp_02":
                row.prop(tp, "btor_wired_suffix", text="suffix")


        box.separator()   
        box = col.box().column(1)      
        box.separator()   
        
        row = box.row(1)
        row.operator("tp_ops.help_bounding_settings", text="", icon="INFO")          
        row.label("Settings [F6]:")          
        
        if tp_props.display_bcyl_settings: 
            row.prop(tp_props, "display_bcyl_settings", text="", icon="SCRIPTWIN") 
            box.separator()
        else:                  
            row.prop(tp_props, "display_bcyl_settings", text="", icon="SCRIPTWIN")    

        box.separator()          
        box.separator()          
       
        row = box.row(1)
        row.label("Object Type:") 
        row.prop(tp, "tp_geom_tube", text="")        

        box.separator()  

        row = box.row(1)  
        row.label("Mesh Type:") 
        row.prop(tp, "tube_meshtype", text="")
        
        if tp.tp_geom_tube == "tp_add_tor":
            pass
        else:
            box.separator() 
         
            row = box.row(1) 
            row.label("Fill Type:") 
            row.prop(tp, "tube_fill", text="")
        
        box.separator()   
        box = col.box().column(1)      
        box.separator()    

        if tp_props.display_bcyl_settings: 

            row = box.row(1) 
            row.label("Copy Scale:")              
            row.prop(tp, "tube_dim", text="")           

            row.label("Apply Scale:") 
            row.prop(tp, "tube_dim_apply", text="")   

            box.separator()                

            if tp.tp_geom_tube == "tp_add_cyl":

                box.separator() 

                row = box.row(1) 
                row.label("Resolution:") 

                sub1 = row.column(1)
                sub1.scale_x = 1
                sub1.prop(tp, "bcyl_res")

                if tp.tube_dim == True:
                    pass
                else:            

                    box.separator()  

                    row = box.row(1) 
                    row.label("Dimension:") 

                    sub1 = row.column(1)

                    sub1.prop(tp, "bcyl_rad")
                    sub1.prop(tp, "bcyl_dep")

            if tp.tp_geom_tube == "tp_add_cone":
                
                box.separator() 

                row = box.row(1) 
                row.label("Resolution:") 

                sub0 = row.column(1)
                sub0.scale_x = 1
                sub0.prop(tp, "bcon_res")

                box.separator()  

                row = box.row(1) 
                row.label("Dimension:") 

                sub0 = row.column(1)
                sub0.prop(tp, "bcon_res2")
                sub0.prop(tp, "bcon_res1")  

                if tp.tube_dim == True:
                    pass
                else:            
                    sub0.prop(tp, "bcon_depth")

            if tp.tp_geom_tube == "tp_add_circ":

                box.separator() 

                row = box.row(1) 
                row.label("Resolution:") 

                sub1 = row.column(1)
                sub1.scale_x = 1
                sub1.prop(tp, "bcirc_res")

                if tp.tube_dim == True:
                    pass
                else:            
                    box.separator()  

                    row = box.row(1) 
                    row.label("Dimension:") 

                    sub1 = row.column(1)

                    sub1.prop(tp, "bcirc_rad")


            if tp.tp_geom_tube == "tp_add_tor":
                    
                box.separator() 

                row = box.row(1) 
                row.label("Resolution:") 

                row = box.column(1) 
                row.prop(tp, "btor_seg1")
                row.prop(tp, "btor_seg2")

                if tp.tube_dim == True:
                    pass
                else:            
                    
                    box.separator() 

                    row = box.row(1) 
                    row.label("Dimension:") 

                    row = box.column(1)         
                    row.prop(tp, "btor_siz1")
                    row.prop(tp, "btor_siz2")

            box.separator()   
            box.separator()  
            
            row = box.row(1) 
            row.label("Copy Rotation:") 
            row.prop(tp, "tube_rota", text="") 
            
            if tp.tp_geom_tube == "tp_add_cyl":

                if tp.tube_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "bcyl_rota_x")             
                    row.prop(tp, "bcyl_rota_y")             
                    row.prop(tp, "bcyl_rota_z")    

     
            if tp.tp_geom_tube == "tp_add_cone":

                if tp.tube_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "bcon_rota_x")             
                    row.prop(tp, "bcon_rota_y")             
                    row.prop(tp, "bcon_rota_z")   
     

            if tp.tp_geom_tube == "tp_add_circ":

                if tp.tube_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "bcirc_rota_x")             
                    row.prop(tp, "bcirc_rota_y")             
                    row.prop(tp, "bcirc_rota_z")  


            if tp.tp_geom_tube == "tp_add_tor":

                if tp.tube_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "btor_rota_x")             
                    row.prop(tp, "btor_rota_y")             
                    row.prop(tp, "btor_rota_z") 


            box.separator()   
            box = col.box().column(1)      
            box.separator()  
            
            row = box.row(1)   
            row.prop(tp, "tube_origin", icon="BLANK1", text="")
            row.prop(tp, "tube_xray", icon="BLANK1")   

            row = box.row(1)        
            row.prop(tp, "tube_smooth", icon="BLANK1")
            row.prop(tp, "tube_edges", icon="BLANK1")               



            if tp.tp_geom_tube == "tp_add_cyl" or tp.tp_geom_tube == "tp_add_cone":

                if tp.tube_fill == "NGON": 

                    box.separator()   
                    box = col.box().column(1)      
                    box.separator()  

                    row = box.row(1) 
                    row.prop(tp, "bvl_extrude_use")

                    row = box.row(1) 
                    row.prop(tp, "bvl_extrude_offset")

                    box.separator()   
                    box = col.box().column(1)      
                    box.separator()  
                 
                    row = box.row(1) 
                    row.prop(tp, "bvl_pipe_use")
                    row.prop(tp, "bvl_pipe_offset")
         
                    box.separator()   
                    box = col.box().column(1)      
                    box.separator()  

                    row = box.row(1) 

                    row.prop(tp, "bvl_bevel_use")
                    row.prop(tp, "bvl_select_all")                
                    row.prop(tp, "bvl_verts_use")
                    
                    row = box.column(1) 
                    row.prop(tp, "bvl_segment")         
                    row.prop(tp, "bvl_offset")           
                    row.prop(tp, "bvl_profile")
                   
                    box.separator()
                  
            box.separator()
            box = col.box().column(1)  

    box.separator() 



    # SPHERE #
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

        box.separator() 
        box = col.box().column(1)
        box.separator() 

        row = box.row(1)
        row.operator("tp_ops.help_bounding_rename", text="", icon="INFO")          
        row.label("ReName:")          
        row.prop(tp, "tp_rename_spheres", text="", icon="SCRIPT")
           
        box.separator()  
        
        row = box.column(1)          
       
        if tp.tp_geom_sphere == "tp_add_sph":
            row.prop(tp, "bsph_prefix", text="prefix")

            if tp.tp_rename_spheres == True:
                row.prop(tp, "bsph_name", text="custom")

            if tp.sphere_meshtype == "tp_00":    
                row.prop(tp, "bsph_shaded_suffix", text="suffix")

            if tp.sphere_meshtype == "tp_01":    
                row.prop(tp, "bsph_shadeless_suffix", text="suffix")

            if tp.sphere_meshtype == "tp_02":    
                row.prop(tp, "bsph_wired_suffix", text="suffix")

        else:
            row.prop(tp, "bico_prefix", text="prefix")

            if tp.tp_rename_spheres == True:
                row.prop(tp, "bico_name", text="rename")
            
            if tp.sphere_meshtype == "tp_00":            
                row.prop(tp, "bico_shaded_suffix", text="suffix")
            
            if tp.sphere_meshtype == "tp_01":
                row.prop(tp, "bico_shadeless_suffix", text="suffix")
            
            if tp.sphere_meshtype == "tp_02":
                row.prop(tp, "bico_wired_suffix", text="suffix")
        
        box.separator() 
        box = col.box().column(1)
        box.separator() 
        
        row = box.row(1)
        row.operator("tp_ops.help_bounding_settings", text="", icon="INFO")          
        row.label("Settings [F6]:")          

        if tp_props.display_bext_settings: 
            row.prop(tp_props, "display_bext_settings", text="", icon="SCRIPTWIN") 
            box.separator()
        else:                  
            row.prop(tp_props, "display_bext_settings", text="", icon="SCRIPTWIN")    
        
        box.separator()          
        box.separator()          
       
        row = box.row(1)
        row.label("Object Type:") 
        row.prop(tp, "tp_geom_sphere", text="")        

        box.separator()  

        row = box.row(1)  
        row.label("Mesh Type:") 
        row.prop(tp, "sphere_meshtype", text="")

        box.separator()  
        box = col.box().column(1)      
        box.separator()   
         
        if tp_props.display_bext_settings: 

            row = box.row(1) 
            row.label("Copy Scale:")              
            row.prop(tp, "sphere_dim", text="")           

            row.label("Apply Scale:") 
            row.prop(tp, "sphere_dim_apply", text="")  

            box.separator()

            if tp.tp_geom_sphere == "tp_add_sph":

                row = box.row(1) 
                row.label("Resolution:") 

                sub1 = row.column(1)
                sub1.scale_x = 1
                sub1.prop(tp, "bsph_seg")
                sub1.prop(tp, "bsph_rig")

                if tp.sphere_dim == True:
                    pass
                else:            
               
                    box.separator()  

                    row = box.row(1) 
                    row.label("Dimension:") 

                    sub1 = row.column(1)

                    sub1.prop(tp, "bsph_siz")

            if tp.tp_geom_sphere == "tp_add_ico":

                row = box.row(1) 
                row.label("Resolution:") 

                sub0 = row.column(1)
                sub0.scale_x = 1
                sub0.prop(tp, "bico_div") 

                if tp.sphere_dim == True:
                    pass
                else:            

                    box.separator()  

                    row = box.row(1) 
                    row.label("Dimension:") 

                    sub0 = row.column(1)
                    sub0.prop(tp, "bico_siz")

            box.separator()
            box.separator()

            row = box.row(1) 
            row.label("Copy Rotation:") 
            row.prop(tp, "sphere_rota", text="") 
            
            if tp.tp_geom_sphere == "tp_add_sph":

                if tp.sphere_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "bsph_rota_x")             
                    row.prop(tp, "bsph_rota_y")             
                    row.prop(tp, "bsph_rota_z")    
     
            else:

                if tp.sphere_rota == True:
                    pass
                else:
                    row = box.row(1)             
                    row.prop(tp, "bico_rota_x")             
                    row.prop(tp, "bico_rota_y")             
                    row.prop(tp, "bico_rota_z")   

            box.separator()   
            box = col.box().column(1)      
            box.separator()  

            row = box.row(1)   
            row.prop(tp, "sphere_origin", icon="BLANK1", text="")
            row.prop(tp, "sphere_xray", icon="BLANK1")   
       
            if tp.sphere_meshtype == "tp_00":

                row = box.row(1)        
                row.prop(tp, "sphere_smooth", icon="BLANK1")
                row.prop(tp, "sphere_edges", icon="BLANK1")                                   

            box.separator()
            
            # SELECT #
            if panel_prefs.tab_display_select == True: 
                box = col.box().column(1)  

    box.separator() 


    # SELECT #
    if panel_prefs.tab_display_select == True: 
                                                       
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

        box.separator() 
        if tp_props.display_select == True:  
     
            box = col.box().column(1)
            box.separator() 

            row = box.row(1) 
            row.operator("tp_ops.help_bounding_select", text="", icon="INFO")          
            row.label("Settings:")          
        
            box.separator() 

            row = box.row(1)
            row.prop(tp, "tp_extend", text="Extend")
            row.prop(tp, "tp_link", text="Linked")      

            box.separator()    
 
            row = box.row(1)
            row.prop(tp, "tp_select_rename", text="")
            row.label(text="Pattern")
            row.prop(tp, "tp_select_custom", text="")      

            box.separator() 
            box.separator() 

            row = box.row(1) 
            row.operator_menu_enum("object.select_linked", "type", text="Linked", icon ="LINKED")                     
            row.operator("tp_ops.unfreeze_restrict", text="Unfreeze", icon="RESTRICT_SELECT_OFF")           
            row.operator("tp_ops.freeze_restrict", text="Freeze", icon="RESTRICT_SELECT_ON") 

            box.separator()
        
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

            box = col.box().column(1)                     
            
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
            row.operator("object.rno_setname", " Set new Name", icon ="FONT_DATA")

            if tp_props.display_rename: 
                row.prop(tp_props, "display_rename", text="", icon="SCRIPTWIN")  
                box.separator()
            else:                  
                row.prop(tp_props, "display_rename", text="", icon="SCRIPTWIN")  
       
            box.separator() 

            if tp_props.display_rename: 
                            
                box = col.box().column(1)                     

                row = box.column(1)              
                row.prop(context.scene, "rno_str_old_string", text="Old: ")
                row.prop(context.scene, "rno_str_new_string", text="New: ")
                
                box.separator()
                
                row = box.row(1)
                button_baply = icons.get("icon_baply")         
                row.operator("object.rno_replace_in_name", "Replace String Name", icon_value=button_baply.icon_id)

                box.separator()

                box = col.box().column(1)                     

                row = box.row(1) 
                row.prop(context.scene,'rno_bool_keepIndex',text='Keep Object Index')
               
                row = box.column(1)
                row.prop(context.scene, "rno_str_prefix")
                row.prop(context.scene, "rno_str_subfix")     

                box.separator()      
                
                row = box.row(1)
                button_baply = icons.get("icon_baply")        
                row.operator("object.rno_add_subfix_prefix", "Add Prefix / Subfix", icon_value=button_baply.icon_id) 

            box.separator()        


    if panel_prefs.tab_display_apply == True: 
        

        if panel_prefs.tab_recoplanar_ui == True: 

            box = col.box().column(1)

            row = box.row(1)                       
            if tp_props.display_transform: 
                row.prop(tp_props, "display_transform", text="", icon="COLLAPSEMENU")  
                box.separator()
            else:                  
                row.prop(tp_props, "display_transform", text="", icon="COLLAPSEMENU")  

      
            row.operator("tp_ops.set_new_local", text = "ReLocal") 
            row.operator("tp_ops.recenter")             
            row.operator("tp_ops.reposition")             

            button_bloc = icons.get("icon_bloc") 
            row.operator("tp_ops.copy_local_transform",text="", icon_value=button_bloc.icon_id ) 

            if tp_props.display_transform: 

                row = box.row(1)                                        
                row.operator("tp_ops.delete_dummy", text=" ", icon="PANEL_CLOSE")       

                row.operator("tp_ops.lock_all", text=" ", icon="LOCKED").lock_mode = "lock"        
                row.operator("tp_ops.lock_all", text=" ", icon="UNLOCKED").lock_mode = "unlock"   

                button_deltas = icons.get("icon_deltas") 
                row.operator("object.transforms_to_deltas", text=" ", icon_value=button_deltas.icon_id).mode='ALL'          

                button_center = icons.get("icon_center") 
                row.operator("tp_ops.relocate", text=" ", icon_value=button_center.icon_id)

                button_move = icons.get("icon_apply_move") 
                row.operator("object.transform_apply", text=" ", icon_value=button_move.icon_id).location=True

                button_rota = icons.get("icon_apply_rota") 
                row.operator("object.transform_apply", text=" ", icon_value=button_rota.icon_id).rotation=True                

                button_scale = icons.get("icon_apply_scale") 
                row.operator("object.transform_apply", text=" ", icon_value=button_scale.icon_id).scale=True  

            box.separator()   

        else:                                            
        
            box = col.box().column(1)

            box.separator()   
            
            row = box.row(1) 
            button_relocal = icons.get("icon_relocal") 
            row.operator("tp_ops.set_new_local", icon_value=button_relocal.icon_id) 

            button_recenter = icons.get("icon_recenter") 
            row.operator("tp_ops.recenter", icon_value=button_recenter.icon_id)   
        
            row = box.row(1) 
         
            button_center = icons.get("icon_center") 
            row.operator("tp_ops.relocate", text="ReLocate", icon_value=button_center.icon_id)    

            button_reposition = icons.get("icon_reposition") 
            row.operator("tp_ops.reposition", icon_value=button_reposition.icon_id)
        
            row = box.row(1)                                        
            row.operator("tp_ops.delete_dummy", text="Delete", icon="PANEL_CLOSE")      

            button_deltas = icons.get("icon_deltas") 
            row.operator("object.transforms_to_deltas", text="DeltaAll", icon_value=button_deltas.icon_id).mode='ALL'          

            box.separator()   

                                                   
            box = col.box().column(1)
            
            box.separator()   
            
            row = box.row(1)                                        
            button_bloc = icons.get("icon_bloc") 
            row.operator("tp_ops.copy_local_transform",text=" ", icon_value=button_bloc.icon_id )  

            row.operator("tp_ops.lock_all", text=" ", icon="LOCKED").lock_mode = "lock"        
            row.operator("tp_ops.lock_all", text=" ", icon="UNLOCKED").lock_mode = "unlock"         

            button_move = icons.get("icon_apply_move") 
            row.operator("object.transform_apply", text=" ", icon_value=button_move.icon_id).location=True

            button_rota = icons.get("icon_apply_rota") 
            row.operator("object.transform_apply", text=" ", icon_value=button_rota.icon_id).rotation=True                

            button_scale = icons.get("icon_apply_scale") 
            row.operator("object.transform_apply", text=" ", icon_value=button_scale.icon_id).scale=True  


            box.separator()

