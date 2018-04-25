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
from bpy.app.translations import pgettext_iface as iface_

def draw_mods_sculpt_layout(self, context, layout):
      
    tp_props = context.window_manager.tp_collapse_menu_modifier         
       
    icons = load_icons()

    button_apply = icons.get("icon_apply")   
              
    ob = context.object  
    obj = context.object
    scene = context.scene
    scn = context.scene
    rs = bpy.context.scene 

    col = layout.column(align=True)  
           
 
    obj = context.active_object
    if obj:
        mod_list = obj.modifiers
        if mod_list:
                            
            box = col.box().column(1)
           
            box.separator()                
           
            row = box.row(1)  
            row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF') 
            row.operator("tp_ops.mods_view"," ", icon = 'RESTRICT_VIEW_OFF')                                                                       
            
            if obj.mode in {'EDIT'}:
            
                row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
                row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  
                                               
            row.operator("tp_ops.remove_mod_all", text=" ", icon='PANEL_CLOSE')     
            row.operator("tp_ops.apply_mod_all", text=" ", icon_value=button_apply.icon_id)          
            
            box.separator()
                        
    else:
        pass



    Display_MultiResolution = context.user_preferences.addons[__package__].preferences.tab_multires
    if Display_MultiResolution == True: 

        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_multires:            
            row.prop(tp_props, "display_multires", text="", icon="MOD_MULTIRES")
        else:
            row.prop(tp_props, "display_multires", text="", icon="MOD_MULTIRES")
                                 
        row.label("MultiRes")
       
        is_multires = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'MULTIRES':
                is_multires = True
        
        if is_multires == True:
            ob = context.object
            for mod in [m for m in ob.modifiers if m.type == 'MULTIRES']:   
                row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
            row.operator("tp_ops.remove_mods_multires", text="" , icon='PANEL_CLOSE')                                 
            row.operator("tp_ops.apply_mods_multires", text="", icon_value=button_apply.icon_id)                                                                                                                                          
        else:   
            row.operator("tp_ops.multires_add", text="", icon="DISCLOSURE_TRI_RIGHT")                

        box.separator()
        
        if is_multires == True:
            
            row = box.row(1)
            row.scale_x = 0.6             
            row.operator("tp_ops.subsurf_0")
            row.operator("tp_ops.subsurf_1")
            row.operator("tp_ops.subsurf_2")            
            row.operator("tp_ops.subsurf_3")
            row.operator("tp_ops.subsurf_4")
            row.operator("tp_ops.subsurf_5")
            row.operator("tp_ops.subsurf_6")
     
            box.separator() 


        if not tp_props.display_multires:  

            box.separator() 
 
            obj = context.active_object
            if obj:
 
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                    if mo.type == 'MULTIRES':
                        append(mo.type)

                        #box.label(mo.name)

                        row = box.row(1)
                        row.prop(mo, "subdivision_type", expand=True)
                        
                        box.separator()
                        
                        row = box.column(1)
                        row.prop(mo, "sculpt_levels", text="Sculpt")
                        row.prop(mo, "levels", text="Preview")
                        row.prop(mo, "render_levels", text="Render")

                        box.separator()

                        row = box.row(1)                
                        row.prop(mo, "use_subsurf_uv", text="Div UVs")
                        row.prop(mo, "show_only_control_edges", text="Iso Line")

                        box.separator()
                        
            else:
                pass



    Display_AutoSym = context.user_preferences.addons[__package__].preferences.tab_autosym
    if Display_AutoSym == True:

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences

        obj = context.object
        if obj:
            if obj.type in {'MESH'}:
                
                if not tp_props.display_symdim:  
                    
                    box = col.box().column(1)
                    
                    row = box.row(1)                        
                    row.prop(tp_props, "display_symdim", text="", icon="MOD_WIREFRAME")            
                
                    row.label("AutoSym")                                            
                   
                    if panel_prefs.autosym_symmetrize == True:
                        row.prop(panel_prefs, "autosym_symmetrize", text="", icon ="PAUSE")              
                    else:             
                        row.prop(panel_prefs, "autosym_mirror", text="", icon ="MOD_MIRROR")   
                   
                        if panel_prefs.autosym_mirror == True:
                            row.prop(panel_prefs, "autosym_apply", text="", icon ="FILE_TICK")                     
                        else:
                            pass
                        
                    row.prop(panel_prefs, "autosym_sculpt", text="", icon ="SCULPTMODE_HLT")   
                    row.prop(panel_prefs, "autosym_edit", text="", icon ="EDIT")      


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
                    row.prop(panel_prefs, "autosym_symmetrize", text="use symmetrize", icon ="PAUSE")  

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
 
 
 


    Display_Smooth = context.user_preferences.addons[__package__].preferences.tab_smooth
    if Display_Smooth == True:
              

        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_smooth:            
            row.prop(tp_props, "display_smooth", text="", icon="MOD_SMOOTH")
        else:
            row.prop(tp_props, "display_smooth", text="", icon="MOD_SMOOTH")
                                 
        row.label("Smooth")
       
        is_smooth = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'SMOOTH':
                is_smooth = True
        
        if is_smooth == True:
            ob = context.object
            for mod in [m for m in ob.modifiers if m.type == 'SMOOTH']:   
                row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
            row.operator("tp_ops.remove_mods_smooth", text="" , icon='PANEL_CLOSE')                                 
            row.operator("tp_ops.apply_mods_smooth", text="", icon_value=button_apply.icon_id)                                                                                                                                          
        else:   
            row.operator("tp_ops.mod_smooth", "", icon='DISCLOSURE_TRI_RIGHT')                   

        box.separator()

        if not tp_props.display_smooth:           

            obj = context.active_object
            if obj:
                   
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                                
                    if mo.type == 'SMOOTH':
                        
                        append(mo.type)
                        
                        row = box.row(1) 
                        row.prop(mo, "iterations") 
                        row.prop(mo, "factor")
                                                                                                                  
                        box.separator()  
                        
                        if tp_props.display_smooth:                         

                            row = box.row(1) 
                            row.label(text="Axis:")
                            row.prop(mo, "use_x")
                            row.prop(mo, "use_y")
                            row.prop(mo, "use_z")

                            row = box.column(1) 
                            row.label(text="Vertex Group:")
                            row.prop_search(mo, "vertex_group", ob, "vertex_groups", text="")

                            box.separator()  



    Display_Remesh = context.user_preferences.addons[__package__].preferences.tab_remesh
    if Display_Remesh == True:

        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_remesh:            
            row.prop(tp_props, "display_remesh", text="", icon="MOD_REMESH")
        else:
            row.prop(tp_props, "display_remesh", text="", icon="MOD_REMESH")
            
        row.label("Remesh")

        is_remesh = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'REMESH' :
                is_remesh  = True

        if is_remesh  == True:
            ob = context.object
            for mod in [m for m in ob.modifiers if m.type == 'REMESH']:   
                row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
            row.operator("tp_ops.remove_mods_remesh", text="" , icon='PANEL_CLOSE')                                 
            row.operator("tp_ops.apply_mods_remesh", text="", icon_value=button_apply.icon_id)                                                                                                                                          
        else:   
            row.operator("tp_ops.mod_remesh", "", icon='DISCLOSURE_TRI_RIGHT')    
                          
        box.separator()               
       
        if not tp_props.display_remesh:     

            obj = context.active_object
            if obj:

                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                                
                    if mo.type == 'REMESH':
                        
                        append(mo.type)

                        box.separator()
                        
                        row = box.column(1)                       
                        row.prop(mo, "mode")
                       
                        box.separator()
                       
                        row = box.row()
                        row.prop(mo, "octree_depth", text="Depth")
                        row.prop(mo, "scale")

                        box.separator()
               
                                                                
                        if tp_props.display_remesh: 
                        
                            row = box.column(1)                       
                            if mo.mode == 'SHARP':
                                row.prop(mo, "sharpness")

                            row.prop(mo, "use_smooth_shade")                      
                            row.prop(mo, "use_remove_disconnected")
                            
                            row = box.row()
                            row.active = mo.use_remove_disconnected
                            row.prop(mo, "threshold")

                            box.separator() 





    Display_Decimate = context.user_preferences.addons[__package__].preferences.tab_decimate
    if Display_Decimate == True:
        
              
        box = col.box().column(1)
        
        row = box.row(1)
        if tp_props.display_decimate:            
            row.prop(tp_props, "display_decimate", text="", icon="MOD_DECIM")
        else:
            row.prop(tp_props, "display_decimate", text="", icon="MOD_DECIM")
                                 
        row.label("Decimate")
       
        is_decimate = False
        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'DECIMATE':
                is_decimate = True
        
        if is_decimate == True:
            ob = context.object
            for mod in [m for m in ob.modifiers if m.type == 'DECIMATE']:   
                row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
            row.operator("tp_ops.remove_mods_decimate", text="" , icon='PANEL_CLOSE')                                 
            row.operator("tp_ops.apply_mods_decimate", text="", icon_value=button_apply.icon_id)                                                                                                                                          
        else:   
            row.operator("tp_ops.mod_decimate", "", icon='DISCLOSURE_TRI_RIGHT')                   
       
        box.separator()

        if not tp_props.display_decimate: 

            obj = context.active_object
            if obj:
                   
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                                
                    if mo.type == 'DECIMATE':
                        
                        append(mo.type)
                        
                        box.separator()  
                        decimate_type = mo.decimate_type
     
                        if decimate_type == 'COLLAPSE':                        
                           
                            row = box.row(1) 
                            row.prop(mo, "ratio")
                            layout_info = row  
                        
                            box.separator()  
                            
                            row = box.row(1)                                                        
                            has_vgroup = bool(mo.vertex_group)
                            row.prop_search(mo, "vertex_group", ob, "vertex_groups", text="")
                            row.prop(mo, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')                                                 
                                               
                        elif decimate_type == 'UNSUBDIV':

                            row = box.row(1)                               
                            row.prop(mo, "iterations")
                            layout_info = row
                        
                        else:
                            row = box.column(1)                                                           
                            row.prop(mo, "angle_limit")
                            row.prop(mo, "use_dissolve_boundaries")
                            layout_info = row
                       
                      
                        if tp_props.display_decimate:  
                                                    
                            box.separator()  

                            decimate_type = mo.decimate_type

                            row = box.row()
                            row.prop(mo, "decimate_type", expand=True)
     
                            if decimate_type == 'COLLAPSE':
                                has_vgroup = bool(mo.vertex_group)

                                split = box.split()
                                
                                col = split.column()
                                row = col.row()
                                row.active = has_vgroup
                                row.prop(mo, "vertex_group_factor")

                                col.prop(mo, "use_collapse_triangulate")
                                
                                row = col.split(percentage=0.75)
                                row.prop(mo, "use_symmetry")
                                row.prop(mo, "symmetry_axis", text="")
                            
                            else:
                                box.label("Delimit:")
                               
                                row = box.row()
                                row.prop(mo, "delimit")
                                
                         
                        box.separator()  
                            
                        layout_info.label(text=iface_("Faces: %d") % mo.face_count, translate=False)


           
            row = box.row()         
            if tp_props.display_vertgrp:                       
                row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")
            else:
                row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")                     
                
            box.separator() 

            if tp_props.display_vertgrp: 

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
                    
                    row = box.row(1)
                    row.prop(context.tool_settings, "vertex_group_weight", text="Weight")
      
                    box.separator()   





