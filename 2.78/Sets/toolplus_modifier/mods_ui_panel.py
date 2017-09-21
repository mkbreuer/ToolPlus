# ##### BEGIN GPL LICENSE BLOCK #####
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
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



def draw_modifier_panel_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_menu_modifier        
        icons = load_icons()
  
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 

        Display_Title = context.user_preferences.addons[__package__].preferences.tab_title
        if Display_Title == 'on':

            obj = context.active_object     
            if obj:
               obj_type = obj.type
                              
               if obj_type in {'MESH'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("MESH") 
                                      
               if obj_type in {'LATTICE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("LATTICE") 

               if obj_type in {'CURVE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("CURVE")               
                   
               if obj_type in {'SURFACE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("SURFACE")                 
                   
               if obj_type in {'META'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("MBall")                 
                   
               if obj_type in {'FONT'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("FONT")  
                                                  
               if obj_type in {'ARMATURE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("ARMATURE") 

               if obj_type in {'EMPTY'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("EMPTY") 

               if obj_type in {'CAMERA'}:
                  box = layout.box()
                  row = box.row(1)                                        
                  row.alignment = "CENTER"
                  row.label("CAMERA") 

               if obj_type in {'LAMP'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("LAMP") 

               if obj_type in {'SPEAKER'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("SPEAKER") 

        Display_Pivot = context.user_preferences.addons[__package__].preferences.tab_pivot
        if Display_Pivot == 'on':
          
            box = layout.box()
            
            row = box.row(1)  
            sub = row.row(1)
            sub.scale_x = 7

            sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
            sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
            sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
            sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
            sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")          
            #row.menu("tp_ops.delete_menu", "", icon="PANEL_CLOSE")   
        
        box = layout.box().column(1)  
            
        row = box.row(1) 
        row.operator_menu_enum("object.modifier_add", "type","   Add new Modifier", icon="MODIFIER")          

        obj = context.active_object
        if obj:
            mod_list = obj.modifiers
            if mod_list:

                Display_RemoveType = context.user_preferences.addons[__package__].preferences.tab_remove_type
                if Display_RemoveType == 'on':

                    row = box.row(1)

                    row.prop(context.scene, "tp_mods_type", text="")
                    row.operator("tp_ops.remove_mods_type", text="Remove Type")                           
 
                Display_toall = context.user_preferences.addons[__package__].preferences.tab_toall
                if Display_toall == 'on':
         
                    if context.mode == 'OBJECT':

                        row = box.row(1)
                        row.operator("scene.to_all", text="To Childs", icon='LINKED').mode = "modifier, children"    
                        row.operator("scene.to_all", text="To Selected", icon='FRAME_NEXT').mode = "modifier, selected"
    
            

                box.separator() 
                                
                row = box.row(1) 
                row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF') 
                row.operator("tp_ops.mods_view"," ", icon = 'RESTRICT_VIEW_OFF')                                                                       
                
                 if context.mode == 'EDIT':
                    row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
                    row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  
              
                row.operator("tp_ops.remove_mod", text=" ", icon='X') 
                row.operator("tp_ops.apply_mod", text=" ", icon='FILE_TICK')          

        else:
            pass


        box.separator()

        
        Display_Subsurf = context.user_preferences.addons[__package__].preferences.tab_subsurf
        if Display_Subsurf == 'on':

            box = layout.box().column(1)
            
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
                 
                    if context.mode == 'EDIT_MESH':
                        row.operator("transform.edge_crease", text="", icon='IPO_EASE_IN_OUT')   

                    row.operator("tp_ops.remove_mods_subsurf", text="" , icon='X')             
                    row.operator("tp_ops.apply_mods_subsurf", text="", icon='FILE_TICK')                                                                                                                                             
       
            else: 
                pass 
          

            box.separator()  
            
            row = box.row(1)
            row.scale_x = 0.6             
            row.operator("tp_ops.subsurf_0")
            row.operator("tp_ops.subsurf_1")
            row.operator("tp_ops.subsurf_2")            
            row.operator("tp_ops.subsurf_3")
            row.operator("tp_ops.subsurf_4")
            row.operator("tp_ops.subsurf_5")
            #row.operator("tp_ops.subsurf_6")


            
            box.separator() 
            
            if tp_props.display_subsurf: 
                                
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
                            #row.prop(mo, "use_opensubdiv",text="OPSubdiv")                    
                            #row.prop(system, "opensubdiv_compute_type", text="")

                            box.separator() 

                else:
                    pass
                

        Display_Mirror_Cut = context.user_preferences.addons[__package__].preferences.tab_mirror_cut
        if Display_Mirror_Cut == 'on':

            obj = context.object
            if obj:
                if obj.type in {'MESH'}:

                    box = layout.box().column(1)
                    
                    row = box.row(1)
                    row.label("", icon="MOD_MESHDEFORM")            
                    row.label("AutoCuts")   

                    row.prop(context.scene, "tp_edit", text="", icon ="EDIT")            
                   
                    box.separator()                    
                   
                    row = box.row(1)  
                    row.prop(context.scene, "tp_axis", text="")
                    sub = row.row(1)
                    sub.scale_x = 0.5
                    sub.prop(context.scene, "tp_axis_cut", text="")
                    row.operator("tp_ops.mods_autocut_obm", text="Execute")                           
                   
                    box.separator() 

            else:
                box = layout.box().column(1)
                
                row = box.row(1)                   
                row.label("nothing selected", icon ="INFO")                   
     
 
        Display_AutoMirror = context.user_preferences.addons[__package__].preferences.tab_automirror
        if Display_AutoMirror == 'on':

            obj = context.object
            if obj:
                if obj.type in {'MESH'}:
                    
                    box = layout.box().column(1)
                    
                    row = box.row(1)
                    if tp_props.display_automirror:            
                        row.prop(tp_props, "display_automirror", text="", icon="MOD_WIREFRAME")
                    else:
                        row.prop(tp_props, "display_automirror", text="", icon="MOD_WIREFRAME")
   
                    row.label("AutoMirror")
                   
                    sub = row.row(1)
                    sub.scale_x = 0.75
                    sub.prop(context.scene, "AutoMirror_threshold", text="Thresh") 

                    box.separator() 
                    
                    row = box.row(1)
                    row.prop(context.scene, "AutoMirror_orientation", text="")                                     
                    sub1 = row.row(1)
                    sub1.scale_x = 0.5
                    sub1.prop(context.scene, "AutoMirror_axis", text="")  
                    row.operator("object.automirror", text="Execute")                 

                    box.separator() 

                    if tp_props.display_automirror: 
                                          
                        box = layout.box().column(1) 
                        row = box.row(1)
                        row.prop(context.scene, "AutoMirror_toggle_edit", text="Editmode")
                        row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
                        
                        row = box.row(1)
                        row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                        row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")            

                        box.separator() 
                   
            else:
                box = layout.box().column(1)
                
                row = box.row(1)                   
                row.label("nothing selected", icon ="INFO")                   
     
        

        Display_Mirror = context.user_preferences.addons[__package__].preferences.tab_mirror
        if Display_Mirror == 'on':
        
            box = layout.box().column(1)
            
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
                    row.operator("tp_ops.remove_mods_mirror", text="" , icon='X')             
                    if context.mode == 'EDIT_MESH': 
                        row.operator("tp_ops.apply_mods_mirror_edm", text="", icon='FILE_TICK')                                                                                                                                               
                    else:
                        row.operator("tp_ops.apply_mods_mirror", text="", icon='FILE_TICK')                                                                                                                                               
                else:
                    row.operator("tp_ops.mod_mirror_x", "", icon='PLUS')   

            else:
                pass
                
            box.separator()              
            
            if tp_props.display_mirror:             
                
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
        if Display_Bevel == 'on':
        
            obj = context.active_object
            if obj:
                if obj.type in {'MESH'}:
                    
                    box = layout.box().column(1)
                    
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
                     
                        if context.mode == 'EDIT_MESH':
                            row.operator("transform.edge_bevelweight", text="", icon='COLLAPSEMENU')   
                        row.operator("tp_ops.remove_mods_bevel", text="" , icon='X')             
                        if context.mode == 'EDIT_MESH': 
                            row.operator("tp_ops.apply_mods_bevel_edm", text="", icon='FILE_TICK')                                                                                                                                              
                        else:
                            row.operator("tp_ops.apply_mods_bevel", text="", icon='FILE_TICK')                                                                                                                                              
   
                    else: 
                        row.operator("tp_ops.mods_bevel", "", icon='PLUS')  
          
                    box.separator()  
                    
                    if tp_props.display_bevel: 

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
        if Display_Solidify == 'on':
        
            obj = context.active_object
            if obj:
                if obj.type in {'MESH'}:
                
                    box = layout.box().column(1)
                                    
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
                        row.operator("tp_ops.remove_mods_solidify", text="" , icon='X')             
                        if context.mode == 'EDIT_MESH': 
                            row.operator("tp_ops.apply_mods_solidify_edm", text="", icon='FILE_TICK')                                                                                                                                            
                        else:
                            row.operator("tp_ops.apply_mods_solidify", text="", icon='FILE_TICK')                                                                                                                                            
                    else:   
                        row.operator("tp_ops.mods_solidify", "", icon='PLUS')  

   
                    box.separator()  
                    
                    if tp_props.display_solidify:  
                                                  
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


        Display_Simple = context.user_preferences.addons[__package__].preferences.tab_simple
        if Display_Simple == 'on':
        
            obj = context.active_object
            if obj:
                if obj.type in {'MESH'}:
                
                    box = layout.box().column(1)
                    
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
                        row.operator("tp_ops.remove_mods_sdeform", text="" , icon='X')                                 
                        if context.mode == 'EDIT_MESH': 
                            row.operator("tp_ops.apply_mods_sdeform", text="", icon='FILE_TICK')                                                                                                                                          
                        else:
                            row.operator("tp_ops.apply_mods_sdeform", text="", icon='FILE_TICK')                                                                                                                                          
                    else:   
                        row.operator("tp_ops.mod_sdeform", "", icon='PLUS')                   


                    box.separator()  

                    if tp_props.display_sdeform:    
                    
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



       
        Display_Array = context.user_preferences.addons[__package__].preferences.tab_array
        if Display_Array == 'on':     

            box = layout.box().column(1)
                            
            row = box.row(1)
            if tp_props.display_array:            
                row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
            else:
                row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
           
            row.label("Array")  

            is_array = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'ARRAY':
                    is_array = True
            
            if is_array == True:
                row.operator("tp_ops.remove_mods_array_obm", text="" , icon='X')             
                if context.mode == 'EDIT_MESH': 
                    row.operator("tp_ops.apply_mods_array_edm", text="", icon='FILE_TICK')                                                                                                                                          
                else:
                    row.operator("tp_ops.apply_mods_array_obm", text="", icon='FILE_TICK')                                                                                                                                          

                box.separator()
                
                row = box.row(1)          
                row.operator("tp_ops.x_array",  text="X")
                row.operator("tp_ops.y_array",  text="Y")
                row.operator("tp_ops.z_array",  text="Z")


            else:   
                sub = row.row(1)
                sub.scale_x = 0.3                 
                sub.operator("tp_ops.x_array",  text="X")
                sub.operator("tp_ops.y_array",  text="Y")
                sub.operator("tp_ops.z_array",  text="Z")

                                 
            box.separator() 
           
            if tp_props.display_array: 
          
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
        if Display_Transform == 'on':
            
            if context.mode == 'OBJECT':  
                
                box = layout.box().column(1)
                
                row = box.row(1)
                if tp_props.display_apply:            
                    row.prop(tp_props, "display_apply", text="", icon="MANIPUL")
                else:
                    row.prop(tp_props, "display_apply", text="", icon="MANIPUL")
                             
                row.label("Apply")  

                sub = row.row(1)
                sub.scale_x = 0.3           
                sub.operator("object.transform_apply", text=" ", icon ="MAN_TRANS").location=True
                sub.operator("object.transform_apply", text=" ", icon ="MAN_ROT").rotation=True                
                sub.operator("object.transform_apply", text=" ", icon ="MAN_SCALE").scale=True                             
                
                if tp_props.display_apply: 
                   
                    box = layout.box().column(1)
                    
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
        if Display_Shade == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tp_props.display_display:            
                row.prop(tp_props, "display_display", text="", icon="WORLD")
                row.label("Display")
            else:
                row.prop(tp_props, "display_display", text="", icon="WORLD")                
                row.label("OSD")

                obj = context.active_object
                if obj:               
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text="", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="", icon='GHOST_ENABLED')        
                else:
                    row.label("", icon="BLANK1")  


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
                
                if context.mode == 'OBJECT':             
      
                    row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
                    row.operator("object.shade_smooth", text="", icon="SMOOTH")  
                    row.operator("tp_ops.rec_normals", text="", icon="SNAP_NORMAL") 

            
            if tp_props.display_display: 
            
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
                        row.operator("tp_ops.draw_solid", text="Solid on", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="Solid off", icon='GHOST_ENABLED')        
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


        Display_History = context.user_preferences.addons[__package__].preferences.tab_history 
        if Display_History == 'on':
            
            box = layout.box().column(1)  

            row = box.row(1)        
            row.operator("view3d.ruler", text="Ruler")   
             
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
           
            box.separator()   




class VIEW3D_TP_Modifier_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Origin"
    bl_idname = "VIEW3D_TP_Modifier_Panel_TOOLS"
    bl_label = "T+ Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_modifier_panel_layout(self, context, layout) 



class VIEW3D_TP_Modifier_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Modifier_Panel_UI"
    bl_label = "T+ Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'  

        draw_modifier_panel_layout(self, context, layout) 


