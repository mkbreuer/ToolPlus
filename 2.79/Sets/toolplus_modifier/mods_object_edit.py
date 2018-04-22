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


def draw_mods_object_edit_layout(self, context, layout):
      
    tp_props = context.window_manager.tp_collapse_menu_modifier         
       
    icons = load_icons()

    button_apply = icons.get("icon_apply")   
              
    ob = context.object  
    obj = context.object
    scene = context.scene
    scn = context.scene
    rs = bpy.context.scene 

    col = layout.column(align=True)  
           
    box = col.box().column(1)  
        
    row = box.row(1) 
    row.operator_menu_enum("object.modifier_add", "type","   Add new Modifier", icon="MODIFIER")          

    obj = context.active_object
    if obj:
        mod_list = obj.modifiers
        if mod_list:

            box.separator() 
                            
            row = box.row(1) 
            row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF') 
            row.operator("tp_ops.mods_view"," ", icon = 'RESTRICT_VIEW_OFF')                                                                       
            row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
            row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  
            row.operator("tp_ops.remove_mod", text=" ", icon='X') 
            row.operator("tp_ops.apply_mod", text=" ", icon='FILE_TICK')          

    else:
        pass

    
    Display_Subsurf = context.user_preferences.addons[__package__].preferences.tab_subsurf
    if Display_Subsurf == True:

        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_subsurf:            
            row.prop(tp_props, "display_subsurf", text="", icon="MOD_SUBSURF")
        else:
            row.prop(tp_props, "display_subsurf", text="", icon="MOD_SUBSURF")
            
        row.label("SubSurf")
       
        if len(context.selected_objects) == 1:
            
            is_subsurf = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'SUBSURF' :
                    is_subsurf = True
            
            if is_subsurf == True:
             
                for mod in [m for m in ob.modifiers if m.type == 'SUBSURF']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")

                if context.mode == 'EDIT_MESH':
                    row.operator("transform.edge_crease", text="", icon='IPO_EASE_IN_OUT')   

                row.operator("tp_ops.remove_mods_subsurf", text="" , icon='PANEL_CLOSE')                              
                row.operator("tp_ops.apply_mods_subsurf", text="", icon_value=button_apply.icon_id)                                                                                                                                             

                box.separator()  
                
                row = box.row(1)
                row.scale_x = 0.6             
                row.operator("tp_ops.subsurf_0")
                row.operator("tp_ops.subsurf_1")
                row.operator("tp_ops.subsurf_2")            
                row.operator("tp_ops.subsurf_3")
                row.operator("tp_ops.subsurf_4")
                row.operator("tp_ops.subsurf_5")
                row.operator("tp_ops.subsurf_6")


            else:
                row.operator("tp_ops.subsurf_2", text="", icon='DISCLOSURE_TRI_RIGHT') 
   
        else: 
            pass 
      

        box.separator() 
        
        if not tp_props.display_subsurf: 
                            
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
                        
                        row = box.row(1)                                
                        row.prop(mo, "use_opensubdiv",text="OpenSubdiv")                    

                        box.separator() 

            else:
                pass
            

 
    Display_SimCut = context.user_preferences.addons[__package__].preferences.tab_automirror
    if Display_SimCut == True:

        obj = context.object
        if obj:
            if obj.type in {'MESH'}:
                
                if not tp_props.display_symdim:  
                    
                    box = col.box().column(1)
                    
                    row = box.row(1)                        
                    row.prop(tp_props, "display_symdim", text="", icon="MOD_WIREFRAME")            
                    row.label("AutoSym") 
                                           
                    if scene.tp_sym_default == True:
                        row.prop(scene, "tp_sym_default", text="", icon ="PAUSE")              
                    else:             
                        row.prop(scene, "tp_mirror", text="", icon ="MOD_MIRROR")   
                        if scene.tp_mirror == True:
                            row.prop(scene, "tp_apply", text="", icon ="FILE_TICK")                     
                        else:
                            pass
                        

                    row.prop(scene, "tp_sculpt", text="", icon ="SCULPTMODE_HLT")   
                    row.prop(scene, "tp_edit", text="", icon ="EDIT")      


                    box = col.box().column(1)                
                                       
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
                    row.operator("tp_ops.mods_negativ_xyz_symcut", text="+XYZ")          
                    row.operator("tp_ops.mods_positiv_xyz_symcut", text="-XYZ")
                    
                    if context.mode == 'EDIT_MESH':
                        row.operator("tp_ops.normal_symcut", text="Normal")
                   

                    box.separator()  
              
                    row = box.row(1) 
                    row.prop(scene, "tp_sym_default", text="use symmetrize", icon ="PAUSE")  

                    box.separator() 

                    is_mirror = False
                    
                    for mode in bpy.context.object.modifiers :
                        if mode.type == 'MIRROR' :
                            is_mirror = True
                    
                    if is_mirror == True:

                        row = box.row()  
                        row.alignment = 'CENTER'              
                        row.prop(bpy.context.active_object.modifiers["Mirror"], "show_viewport", text="")                                                                     
                        
                        obj = context.active_object
                        if obj.mode in {'EDIT'}:                
                            row.operator("tp_ops.mods_edit","", icon='EDITMODE_HLT')                                                    
                            row.operator("tp_ops.mods_cage","", icon='OUTLINER_OB_MESH')                 

                        row.operator("tp_ops.remove_mods_mirror", text="", icon='X') 
                        row.operator("tp_ops.apply_mods_mirror", text="", icon='FILE_TICK')

                        box.separator()      

                        for mode in bpy.context.object.modifiers :
                            if mode.type == 'MIRROR' :              
                                if mode.use_mirror_merge is True:                              
                                    row = box.row()  
                                    row.alignment = 'CENTER'              
                                    row.prop(bpy.context.active_object.modifiers["Mirror"], "merge_threshold", text="Merge")           
                                    box.separator()  
                    
                else:    
                    
                    box = col.box().column(1)
                    
                    row = box.row(1)   
                    row.prop(tp_props, "display_symdim", text="", icon="MOD_WIREFRAME")                
                    row.label("AutoSym")                                

                    display_symdim_lr = context.user_preferences.addons[__package__].preferences.tap_symdim_lr        
                    if display_symdim_lr == True:

                        row.operator("tp_ops.mods_negativ_x_symcut", text="", icon='DISCLOSURE_TRI_RIGHT')
                    else:
                        row.operator("tp_ops.mods_positiv_x_symcut", text="", icon='DISCLOSURE_TRI_RIGHT')

                    box.separator()  

                               
        else:
            box = col.box().column(1)
            
            row = box.row(1)                   
            row.label("nothing selected", icon ="INFO")                   
 


    

    Display_Mirror = context.user_preferences.addons[__package__].preferences.tab_mirror
    if Display_Mirror == True:
    
        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_mirror:            
            row.prop(tp_props, "display_mirror", text="", icon="MOD_MIRROR")
        else:
            row.prop(tp_props, "display_mirror", text="", icon="MOD_MIRROR")
      
        row.label("Mirror")                              

        obj = context.active_object
        if obj:
 
            is_mirror = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'MIRROR' :
                    is_mirror = True
            
            if is_mirror == True:
                for mod in [m for m in ob.modifiers if m.type == 'MIRROR']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")  

                row.operator("tp_ops.remove_mods_mirror", text="" , icon='PANEL_CLOSE')             
                if context.mode == 'EDIT_MESH': 
                    row.operator("tp_ops.apply_mods_mirror_edm", text="", icon_value=button_apply.icon_id)                                                                                                                                               
                else:
                    row.operator("tp_ops.apply_mods_mirror", text="", icon_value=button_apply.icon_id)                                                                                                                                               
            else:
                row.operator("tp_ops.mod_mirror_x", "", icon='DISCLOSURE_TRI_RIGHT')   

        else:
            pass
            
        box.separator()              
        
        if not tp_props.display_mirror:             
            
            obj = context.active_object
            if obj:
 
                mo_types = []            
                append = mo_types.append

                for mo in obj.modifiers:
                                                  
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
            else:
                pass

    
    Display_Bevel = context.user_preferences.addons[__package__].preferences.tab_bevel
    if Display_Bevel == True:
    
        obj = context.active_object
        if obj:
            if obj.type in {'MESH'}:
                
                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_bevel:            
                    row.prop(tp_props, "display_bevel", text="", icon="MOD_BEVEL")
                else:
                    row.prop(tp_props, "display_bevel", text="", icon="MOD_BEVEL")
                    
                row.label("Bevel")

                is_bevel = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'BEVEL' :
                        is_bevel = True
                
                if is_bevel == True:
                    for mod in [m for m in ob.modifiers if m.type == 'BEVEL']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")                         
                   
                    if context.mode == 'EDIT_MESH':
                        row.operator("transform.edge_bevelweight", text="", icon='COLLAPSEMENU')   
                    row.operator("tp_ops.remove_mods_bevel", text="" , icon='PANEL_CLOSE')             
                  
                    if context.mode == 'EDIT_MESH': 
                        row.operator("tp_ops.apply_mods_bevel_edm", text="", icon_value=button_apply.icon_id)                                                                                                                                              
                    else:
                        row.operator("tp_ops.apply_mods_bevel", text="", icon_value=button_apply.icon_id)                                                                                                                                              
   
                else: 
                    row.operator("tp_ops.mods_bevel", "", icon='DISCLOSURE_TRI_RIGHT')  
      
                box.separator()  
                
                if not tp_props.display_bevel: 

                    obj = context.active_object
                    if obj:
     
                        mo_types = []
                        append = mo_types.append

                        for mo in obj.modifiers:
                                        
                            if mo.type == 'BEVEL':
                                
                                append(mo.type)
                                
                                row = box.row(1)  
                                row.prop(mo, "profile", text="")
                                row.prop(mo, "segments", text="")
                                row.prop(mo, "width", text="")

                                row = box.row(1)  
                                row.label(text="profile")                       
                                row.label(text="segments")
                                row.label(text="width")
                
                                box.separator() 
                                
                                row = box.row(1)
                                row.prop(mo, "limit_method", expand=True)
                               
                                if mo.limit_method == 'ANGLE':
                                    row = box.row(1)
                                    row.prop(mo, "angle_limit")
                                
                                elif mo.limit_method == 'VGROUP':
                                    row = box.row(1)
                                    row.prop_search(mo, "vertex_group", context.object, "vertex_groups", text="")
                               
                                box.separator() 
                                
                                row = box.row(1)
                                row.prop(mo, "offset_type", expand=True)


                    else:
                        pass
        else:
            pass


    Display_Solidify = context.user_preferences.addons[__package__].preferences.tab_solidify
    if Display_Solidify == True:
    
        obj = context.active_object
        if obj:
            if obj.type in {'MESH'}:
            
                box = col.box().column(1)
                                
                row = box.row(1)
                if tp_props.display_solidify:            
                    row.prop(tp_props, "display_solidify", text="", icon="MOD_SOLIDIFY")
                else:
                    row.prop(tp_props, "display_solidify", text="", icon="MOD_SOLIDIFY")
                               
                row.label("Solidify")

                is_solidify = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'SOLIDIFY':
                        is_solidify = True
                
                if is_solidify == True:                            
                    for mod in [m for m in ob.modifiers if m.type == 'SOLIDIFY']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")                              
                    row.operator("tp_ops.remove_mods_solidify", text="" , icon='PANEL_CLOSE')             
                    if context.mode == 'EDIT_MESH': 
                        row.operator("tp_ops.apply_mods_solidify_edm", text="", icon_value=button_apply.icon_id)                                                                                                                                            
                    else:
                        row.operator("tp_ops.apply_mods_solidify", text="", icon_value=button_apply.icon_id)                                                                                                                                            
                else:   
                    row.operator("tp_ops.mods_solidify", "", icon='DISCLOSURE_TRI_RIGHT')  

   
                box.separator()  
                
                if not tp_props.display_solidify:  
                                              
                    obj = context.active_object
                    if obj:
     
                        mo_types = []
                        append = mo_types.append

                        for mo in obj.modifiers:
                                        
                            if mo.type == 'SOLIDIFY':
                                
                                append(mo.type)
                                
                                row = box.column(1)  
                                row.prop(mo, "thickness")
                                row.prop(mo, "thickness_clamp")        
                                row.prop(mo, "offset")
                                
                                row = box.row(1)
                                row.prop(mo, "use_rim", text ="Fill")
                                row.prop(mo, "use_rim_only", text ="Rim")    
                                row.prop(mo, "use_even_offset", text ="Even")
                
                                box.separator() 

                    else:
                        pass

        else:
            pass



    Display_Screw = context.user_preferences.addons[__package__].preferences.tab_screw
    if Display_Screw == True:    


        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_screw:            
            row.prop(tp_props, "display_screw", text="", icon="MOD_SCREW")
        else:
            row.prop(tp_props, "display_screw", text="", icon="MOD_SCREW")
                                 
        row.label("Skrew")
       
        is_sdeform = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'SCREW':
                is_sdeform = True
        
        if is_sdeform == True:
            for mod in [m for m in ob.modifiers if m.type == 'SCREW']:   
                row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")              
            row.operator("tp_ops.remove_mods_screw", text="" , icon='PANEL_CLOSE')                                 
            row.operator("tp_ops.apply_mods_screw", text="", icon_value=button_apply.icon_id)                                                                                                                                          
        else:   
            row.operator("tp_ops.mod_screw", "", icon='DISCLOSURE_TRI_RIGHT')                   
        
        box.separator()  

        if not tp_props.display_screw: 

            box.separator()  
            
            obj = context.active_object
            if obj:
                   
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                                
                    if mo.type == 'SCREW':
                        
                        append(mo.type)
                        
                        row = box.row(1) 
                        row.prop(mo, "steps")                        
                                             
                        sub = row.row(1)                      
                        sub.active = (mo.object is None or mo.use_object_screw_offset is False)
                        sub.prop(mo, "screw_offset")                       
                       
                        row = box.row(1)                         
                        row.prop(mo, "angle")
                        row.prop(mo, "iterations")
                     
                        box.separator()                          
                      
                        row = box.row(1)
                        row.prop(mo, "axis")  
                        row.prop(mo, "use_smooth_shade", text="Smooth")

                        box.separator()  
                        
                        row = box.row(1)
                        row.prop(mo, "object", text="AxisOb")                       
                        sub = row.row(1)
                        sub.active = (mo.object is not None)
                        sub.prop(mo, "use_object_screw_offset", text="Object")
                                               
                        box.separator()  

                        row = box.row()                        
                        row.prop(mo, "use_merge_vertices", text ="Merge")
                        sub = row.row(1)
                        sub.active = mo.use_merge_vertices
                        sub.prop(mo, "merge_threshold", text ="threshold")
                        
                        if tp_props.display_screw:                         

                            box.separator()  
                            
                            row = box.row(1) 
                            row.prop(mo, "render_steps")
                            
                            row = box.row(1)
                            row.prop(mo, "use_stretch_u")                                                                                 
                            row.prop(mo, "use_normal_calculate")                           
 
                            row = box.row(1)                                                          
                            row.prop(mo, "use_stretch_v")
                            row.prop(mo, "use_normal_flip")

                        box.separator()  

        else:                         
            pass                            





    Display_Simple = context.user_preferences.addons[__package__].preferences.tab_simple
    if Display_Simple == True:
    
        obj = context.active_object
        if obj:
            if obj.type in {'MESH'}:
            
                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_sdeform:            
                    row.prop(tp_props, "display_sdeform", text="", icon="MOD_SIMPLEDEFORM")
                else:
                    row.prop(tp_props, "display_sdeform", text="", icon="MOD_SIMPLEDEFORM")
                                         
                row.label("SDeform")
               

                is_sdeform = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'SIMPLE_DEFORM':
                        is_sdeform = True
                
                if is_sdeform == True:
                    row.operator("tp_ops.remove_mods_sdeform", text="" , icon='PANEL_CLOSE')                                 
                    if context.mode == 'EDIT_MESH': 
                        row.operator("tp_ops.apply_mods_sdeform", text="", icon_value=button_apply.icon_id)                                                                                                                                          
                    else:
                        row.operator("tp_ops.apply_mods_sdeform", text="", icon_value=button_apply.icon_id)                                                                                                                                          
                else:   
                    row.operator("tp_ops.mod_sdeform", "", icon='DISCLOSURE_TRI_RIGHT')                   


                box.separator()  

                if not tp_props.display_sdeform:    
                
                    obj = context.active_object
                    if obj:
                           
                        mo_types = []
                        append = mo_types.append

                        for mo in obj.modifiers:
                                        
                            if mo.type == 'SIMPLE_DEFORM':
                                
                                append(mo.type)
                                
                                row = box.row(1)  
                                row.prop(mo, "deform_method", expand=True)
                                
                                box.separator() 
                              
                                row = box.row(1)  
                                row.prop_search(mo, "vertex_group", ob, "vertex_groups", text="VGrp")
                                row.prop(mo, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

                                row = box.row(1)  
                                row.prop(mo, "origin", text="Axis")
                                row.label(text="", icon ="BLANK1")

                                if mo.deform_method in {'TAPER', 'STRETCH', 'TWIST'}:
                                    
                                    row = box.row(1) 
                                    row.prop(mo, "lock_x")
                                    row.prop(mo, "lock_y")

                                box.separator() 
                                
                                row = box.row(1)                         
                                if mo.deform_method in {'TAPER', 'STRETCH'}:
                                    row.scale_x = 3
                                    row.prop(mo, "factor", text="Deform Factor:")
                                else:
                                    row.prop(mo, "angle", text="Deform Angle:")
                                
                                box.separator() 
                                
                                row = box.row(1) 
                                row.prop(mo, "limits", slider=True, text="Limits")

                                box.separator() 
                            
                    else:                         
                        pass                            
       
        else:
            pass   





    Display_Lattice = context.user_preferences.addons[__package__].preferences.tab_lattice
    if Display_Lattice == True:    

        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_lattice:            
            row.prop(tp_props, "display_lattice", text="", icon="MOD_LATTICE")
        else:
            row.prop(tp_props, "display_lattice", text="", icon="MOD_LATTICE")
            
        row.label("Lattice")

        is_lattice = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'LATTICE' :
                is_lattice = True



        obj = context.active_object     
        if obj:
            obj_type = obj.type
   
            if obj_type in {'LATTICE'}:
            
                box.separator()
                
                if not tp_props.display_lattice: 
                
                    box.separator()                       
                     
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
                  
                    box.separator()    


            else:                                

                if is_lattice == True:
                 
                    if context.mode == 'OBJECT':
                        row.prop(bpy.context.active_object.modifiers["latticeeasytemp"], "show_viewport", text="")
                        row.operator("tp_ops.remove_mods_lattice", text="" , icon='PANEL_CLOSE')                                              
                        row.operator("retopo.latticeapply", text = "", icon_value=button_apply.icon_id)  

                else:
                    if context.mode == 'EDIT_LATTICE':
                        pass
                    else:
                        row.operator("object.easy_lattice", text="", icon = "DISCLOSURE_TRI_RIGHT")       

                box.separator()
                
                if not tp_props.display_lattice:   

                    box.separator()                      
                                 
                    obj = context.active_object
                    if obj:

                        mo_types = []
                        append = mo_types.append

                        for mo in obj.modifiers:
                                        
                            if mo.type == 'LATTICE':
                                
                                append(mo.type)

                                box.separator()
                                
                                row = box.row(1)                            
                                row.prop(mo, "strength", slider=True)

                                box.separator()
                                
                                if tp_props.display_lattice: 
                                
                                    row = box.column(1)
                                    row.label(text="Object:")
                                    row.prop(mo, "object", text="")

                                    row = box.column(1)
                                    row.label(text="VertexGroup:")  
                                    row.prop_search(mo, "vertex_group", ob, "vertex_groups", text="")

                                    box.separator() 

                    else:
                        pass

                   
                    if is_lattice == True:                   
                    
                        box.separator()                                       
                        
                        row = box.row()         
                        if tp_props.display_vertgrp:                       
                            row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")
                        else:
                            row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")                     
                            
                        box.separator() 
                        
                        if not tp_props.display_vertgrp:                                          
                                
                            row = box.row()
                            
                            obj = context.object
                            if obj:
                                row.template_list("MESH_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=4)           

                            split = row.split(1)
                            row = split.column(1)
                            row.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                            row.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                            row.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                            row.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                            row.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                

                            box.separator()   

                            row = box.row()
                           
                            sub = row.row(align=True)
                            sub.operator("object.vertex_group_assign", text="Assign")
                            sub.operator("object.vertex_group_remove_from", text="Remove")

                            sub = row.row(align=True)
                            sub.operator("object.vertex_group_select", text="Select")                    
                            sub.operator("object.vertex_group_deselect", text="Deselect")
                          
                            box.separator()   
                            
                            row = box.row(1)
                            row.prop(context.tool_settings, "vertex_group_weight", text="Weight")

                            box.separator()   





   
    Display_Array = context.user_preferences.addons[__package__].preferences.tab_array
    if Display_Array == True:     

        box = col.box().column(1)
                        
        row = box.row(1)
        if tp_props.display_array:            
            row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
        else:
            row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
       
        row.label("Array")  

        if len(context.selected_objects) == 1:

            is_array = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'ARRAY':
                    is_array = True
            
            if is_array == True:

                for mod in [m for m in ob.modifiers if m.type == 'ARRAY']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")
                                            
                row.operator("tp_ops.remove_mods_array", text="" , icon='PANEL_CLOSE')                                                                                                                                                     
                row.operator("tp_ops.apply_mods_array", text="", icon_value=button_apply.icon_id)                                                                                                                                          
            else:   
                sub = row.row(1)
                sub.scale_x = 0.3                 
                sub.operator("tp_ops.x_array",  text="X")
                sub.operator("tp_ops.y_array",  text="Y")
                sub.operator("tp_ops.z_array",  text="Z")

        else:
            pass
                             
        box.separator() 
       
        if not tp_props.display_array:
            
            if is_array == True:
                
                row = box.row(1)          
                row.operator("tp_ops.x_array",  text="X")
                row.operator("tp_ops.y_array",  text="Y")
                row.operator("tp_ops.z_array",  text="Z")                    
              
                box.separator()                     
                box.separator()                     
      
            obj = context.active_object
            if obj:
 
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                    if mo.type == 'ARRAY':
                        if mo.fit_type == 'FIXED_COUNT':
                            append(mo.type)

                            split = box.split()

                            row = box.row(1)
                            row.label(mo.name)  
                            row.prop(mo, "count")
                            
                            box.separator() 
                            
                            row = box.row(1)  
                            row.prop(mo, "relative_offset_displace", text="")
                            
                            row = box.row(1) 
                            row.prop(mo, "start_cap", text="")
                            row.prop(mo, "end_cap", text="")  
                                                 
                            box.separator() 
            else:
                pass                                           


    Display_Transform = context.user_preferences.addons[__package__].preferences.tab_transform
    if Display_Transform == True:
        
        if context.mode == 'OBJECT':  
            
            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_apply:            
                row.prop(tp_props, "display_apply", text="", icon="MANIPUL")
            else:
                row.prop(tp_props, "display_apply", text="", icon="MANIPUL")
                         
            row.label("Apply")  

            sub = row.row(1)
            sub.scale_x = 0.3           

            button_move = icons.get("icon_apply_move") 
            props = sub.operator("object.transform_apply", text=" ", icon_value=button_move.icon_id)
            props.location=True
            props.rotation=False
            props.scale=False

            button_rota = icons.get("icon_apply_rota") 
            props = sub.operator("object.transform_apply", text=" ", icon_value=button_rota.icon_id)             
            props.location=False
            props.rotation=True
            props.scale=False
            
            button_scale = icons.get("icon_apply_scale") 
            props = sub.operator("object.transform_apply", text=" ", icon_value=button_scale.icon_id)
            props.location=False
            props.rotation=False
            props.scale=True        
                    
            if not tp_props.display_apply: 
               
                box = col.box().column(1)
                
                row = box.column_flow(2)
                row.label("Transforms to Deltas")  
                row.operator("object.transforms_to_deltas", text="Location").mode='LOC'
                row.operator("object.transforms_to_deltas", text="Rotation").mode='ROT' 
                row.operator("object.transforms_to_deltas", text="All").mode='ALL'
                row.operator("object.transforms_to_deltas", text="Scale").mode='SCALE'                    
                row.operator("object.anim_transforms_to_deltas", text="Animated")
                
                box.separator() 
               
                row = box.column(1)
                row.operator("object.visual_transform_apply")
                row.operator("object.duplicates_make_real")
                                              
            box.separator()                     


    Display_Shade = context.user_preferences.addons[__package__].preferences.tab_shade
    if Display_Shade == True:                                         

        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_display:            
            row.prop(tp_props, "display_display", text="", icon="WORLD")
        else:
            row.prop(tp_props, "display_display", text="", icon="WORLD")
            
        row.label("Display") 


        obj = context.active_object
        if obj:
            active_wire = obj.show_wire 
            if active_wire == True:
                row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
            else:                       
                row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID')
        else:
            row.label("", icon="BLANK1")  



        if context.mode == 'EDIT_MESH':          

            row.operator("mesh.faces_shade_flat", text="", icon="MESH_CIRCLE") 
            row.operator("mesh.faces_shade_smooth", text="", icon="SMOOTH")  
            row.operator("mesh.normals_make_consistent", text="", icon="SNAP_NORMAL")  
        
        else:            
  
            row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
            row.operator("object.shade_smooth", text="", icon="SMOOTH")  
            row.operator("tp_ops.rec_normals", text="", icon="SNAP_NORMAL") 

        
        if not tp_props.display_display: 
        
            box.separator()
            
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
                    row.operator("tp_ops.draw_solid", text="Solid Shade", icon='GHOST_DISABLED')     
                else:
                    row.operator("tp_ops.draw_wire", text="Wire Shade", icon='GHOST_ENABLED')        
            else:
                row.label("", icon="BLANK1")  
 
            ob = context.object
            if ob: 
                row.prop(ob, "draw_type", text="")
                
                row = box.row(1)
                row.prop(ob, "show_bounds", text="ShowBounds", icon='STICKY_UVS_LOC') 
                row.prop(ob, "draw_bounds_type", text="")    
           
            else:
                row.label("", icon="BLANK1") 

            
            if context.mode == 'EDIT_MESH':          
                
                box.separator() 
                
                row = box.row(1)  
                row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 
                
                row = box.row(1)  
                row.operator("mesh.normals_make_consistent", text="Consistent Normals", icon="SNAP_NORMAL")  
            
            else:            
                
                box.separator() 
                
                if context.mode == 'OBJECT': 
                    
                    row = box.row(1)  
                    row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                    row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
               
                row = box.row(1)  
                row.operator("tp_ops.rec_normals", text="Consistent Normals", icon="SNAP_NORMAL")  

            box.separator() 


