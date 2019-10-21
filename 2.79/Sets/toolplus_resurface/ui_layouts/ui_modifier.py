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

#from ..ops_modifier.mods_ui import draw_mods_layout

types_mods =  [("tp_m0"    ," "   ," "   ,"COLLAPSEMENU"        ,0),
               ("tp_m1"    ," "   ," "   ,"MODIFIER"            ,1), 
               ("tp_m2"    ," "   ," "   ,"MOD_LATTICE"         ,2), 
               ("tp_m3"    ," "   ," "   ,"MOD_SCREW"           ,3), 
               ("tp_m4"    ," "   ," "   ,"MOD_SOLIDIFY"        ,4),
               ("tp_m5"    ," "   ," "   ,"MOD_BEVEL"           ,5),
               ("tp_m6"    ," "   ," "   ,"MOD_MIRROR"          ,6),
               ("tp_m7"    ," "   ," "   ,"MOD_SUBSURF"         ,7)]

bpy.types.Scene.tp_mody = bpy.props.EnumProperty(name = " ", default = "tp_m0", items = types_mods)



def draw_modifier_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        
        icons = load_icons()
  
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 

        col = layout.column(1)

        box = col.box().column(1) 

        row = box.row(1)  
        row.prop(scene, 'tp_mody', emboss = False, expand = True) #icon_only=True,


        if scene.tp_mody == "tp_m0": 
            pass


        if scene.tp_mody == "tp_m1": 
           
            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_addmods:            
                row.prop(tp_props, "display_addmods", text="", icon="MODIFIER")
            else:
                row.prop(tp_props, "display_addmods", text="", icon="MODIFIER")
                
            row.label("Modifier")

         
            row.operator_menu_enum("object.modifier_add", "type","", icon="PLUS") 


            obj = context.active_object
            if obj:
                mod_list = obj.modifiers
                if mod_list:

                                    
                    box = col.box().column(1)
                        
                    row = box.row(1)  
                    row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF') 
                    row.operator("tp_ops.mods_view"," ", icon = 'RESTRICT_VIEW_OFF')                                                                       
                    
                    if obj.mode in {'EDIT'}:
                    
                        row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
                        row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  
                                                       
                    row.operator("tp_ops.remove_mod_all", text=" ", icon='X')     
                    row.operator("tp_ops.apply_mod_all", text=" ", icon='FILE_TICK')          

             
                    if context.mode == 'OBJECT':
                        
                        box.separator() 

                        #row = box.row(1)
                        #row.operator("scene.to_all", text="to Childs", icon='LINKED').mode = "modifier, children"    
                        #row.operator("scene.to_all", text="to Selected", icon='FRAME_NEXT').mode = "modifier, selected"       
                        
                        row = box.row(1)
                        row.label("Adjust Modifier by Type:")
                        
                        row = box.row(1)            
                        row.prop(context.scene, "tp_mods_type", text="")
                        row.prop(context.scene, "tp_func_type", text="")

                        row = box.row(1)
                        row.operator("tp_ops.copy_choosen_mods", text="CopyDial", icon='PASTEDOWN') 
                        row.operator("tp_ops.mods_by_type", text="Execute", icon='FRAME_NEXT')  

                        box.separator()
                        
                        #row = box.row(1) 
                        #draw_mods_layout(self, context, layout)                         
                        
            else:
                pass



        if scene.tp_mody == "tp_m2": 

            col = layout.column(1)

            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_lattice:            
                row.prop(tp_props, "display_lattice", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_lattice", text="", icon="SCRIPTWIN")
                
            row.label("Easy Lattice")


            is_lattice = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'LATTICE' :
                    is_lattice = True

            if is_lattice == True:
             
                if context.mode == 'OBJECT':
                    row.prop(bpy.context.active_object.modifiers["latticeeasytemp"], "show_viewport", text="")
                    row.operator("tp_ops.remove_mods_lattice", text="" , icon='X')                                 
                    button_lattice_apply = icons.get("icon_lattice_apply")                  
                    row.operator("retopo.latticeapply", text = "", icon_value=button_lattice_apply.icon_id)  

            else:
                if context.mode == 'EDIT_LATTICE':
                    pass
                else:
                    row.operator("object.easy_lattice", text="", icon = "PLUS")       

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

           
            box.separator()                                       
            
            row = box.row()         
            if tp_props.display_vertgrp:                       
                row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")
            else:
                row.prop(tp_props, "display_vertgrp", text="Vertex Groups", icon="STICKY_UVS_LOC")                     
                
            if tp_props.display_vertgrp: 
            
                if context.mode == 'OBJECT':
                
                    box.separator()                                       
                    
                    row = box.row()
                    obj = context.object
                    if obj:
                        row.template_list("MESH_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=4)           

                    col = row.column()
                    sub = col.column(1)
                    sub.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                    sub.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                    sub.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                    sub.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                    sub.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                
  
                    box.separator()  
               
                else:

                    box.separator()                                       
                    
                    row = box.row()
                    obj = context.object
                    if obj:                                
                        row.template_list("MESH_UL_vgroups", "", obj, "vertex_groups", obj.vertex_groups, "active_index", rows=4)           

                    col = row.column()
                    sub = col.column(1)
                    sub.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                    sub.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                    sub.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                    sub.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                    sub.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                

                    box.separator()  
                    
                    row = box.row(1)
                    row.operator("object.vertex_group_assign", text="Assign", icon="ZOOMIN") 
                    row.operator("object.vertex_group_remove_from", text="Remove", icon="ZOOMOUT") 

                    row = box.row(1)                    
                    row.operator("object.vertex_group_select", text="Select", icon="RESTRICT_SELECT_OFF")
                    row.operator("object.vertex_group_deselect", text="Deselect", icon="RESTRICT_SELECT_ON")
                    
                    row = box.row(1)
                    row.prop(context.tool_settings, "vertex_group_weight", text="Weight")
  
                    box.separator()   


        if scene.tp_mody == "tp_m3": 
                  

            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_screw:            
                row.prop(tp_props, "display_screw", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_screw", text="", icon="SCRIPTWIN")
                                     
            row.label("Skrew")
           
            is_sdeform = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'SCREW':
                    is_sdeform = True
            
            if is_sdeform == True:
                for mod in [m for m in ob.modifiers if m.type == 'SCREW']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")              
                row.operator("tp_ops.remove_mods_screw", text="" , icon='X')                                 
                row.operator("tp_ops.apply_mods_screw", text="", icon='FILE_TICK')                                                                                                                                          
            else:   
                row.operator("tp_ops.mod_screw", "", icon='PLUS')                   


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









#            box = col.box().column(1)
#            
#            row = box.row(1)
#            if tp_props.display_cast:            
#                row.prop(tp_props, "display_cast", text="", icon="MOD_CAST")
#            else:
#                row.prop(tp_props, "display_cast", text="", icon="MOD_CAST")
#                                     
#            row.label("Cast")
#           
#            is_sdeform = False
#            
#            for mode in bpy.context.object.modifiers :
#                if mode.type == 'CAST':
#                    is_sdeform = True
#            
#            if is_sdeform == True:
#                row.operator("tp_ops.remove_mods_cast", text="" , icon='X')                                 
#                if context.mode == 'EDIT_MESH': 
#                    row.operator("tp_ops.apply_mods_cast", text="", icon='FILE_TICK')                                                                                                                                          
#                else:
#                    row.operator("tp_ops.apply_mods_cast", text="", icon='FILE_TICK')                                                                                                                                          
#            else:   
#                row.operator("tp_ops.mod_cast", "", icon='PLUS')                   


#            box.separator()  
#            
#            obj = context.active_object
#            if obj:
#                   
#                mo_types = []
#                append = mo_types.append

#                for mo in obj.modifiers:
#                                
#                    if mo.type == 'CAST':
#                        
#                        append(mo.type)
#                        
#                        row = box.row(1)  

#                        split = box.split(percentage=0.25)

#                        split.label(text="Cast Type:")
#                        split.prop(mo, "cast_type", text="")

#                        split = box.split(percentage=0.25)

#                        col = split.column()
#                        col.prop(mo, "use_x")
#                        col.prop(mo, "use_y")
#                        col.prop(mo, "use_z")

#                        col = split.column()
#                        col.prop(mo, "factor")
#                        col.prop(mo, "radius")
#                        col.prop(mo, "size")
#                        col.prop(mo, "use_radius_as_size")

#                        if tp_props.display_cast: 

#                            split = box.split()

#                            col = split.column()
#                            col.label(text="Vertex Group:")
#                            col.prop_search(mo, "vertex_group", ob, "vertex_groups", text="")
#                            
#                            col = split.column()
#                            col.label(text="Control Object:")
#                           
#                            col.prop(mo, "object", text="")
#                            if mo.object:
#                                col.prop(mo, "use_transform")

#                        box.separator()  

#            else:                         
#                pass                            





        if scene.tp_mody == "tp_m4": 

            box = col.box().column(1)
                            
            row = box.row(1)
            if tp_props.display_solidify:            
                row.prop(tp_props, "display_solidify", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_solidify", text="", icon="SCRIPTWIN")
                           
            row.label("Solidify")

            is_solidify = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'SOLIDIFY':
                    is_solidify = True
            
            if is_solidify == True:
                
                for mod in [m for m in ob.modifiers if m.type == 'SOLIDIFY']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")                
                    
                row.operator("tp_ops.remove_mods_solidify", text="" , icon='X')                                                                                                                                                       
                row.operator("tp_ops.apply_mods_solidify", text="", icon='FILE_TICK')                                                                                                                                            
            else:   
                row.operator("tp_ops.mods_solidify", "", icon='PLUS')  

   
            box.separator()  
                                                      
            obj = context.active_object
            if obj:
 
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                                
                    if mo.type == 'SOLIDIFY':
                        
                        append(mo.type)
                        
                        row = box.column(1)  
                        row.prop(mo, "thickness")
                        
                        if tp_props.display_solidify:  

                            row.prop(mo, "thickness_clamp")        
                            row.prop(mo, "offset")
                            
                            row = box.row(1)
                            row.prop(mo, "use_rim", text ="Fill")
                            row.prop(mo, "use_rim_only", text ="Rim")    
                            row.prop(mo, "use_even_offset", text ="Even")
            
                        box.separator() 

            else:
                pass




        if scene.tp_mody == "tp_m5": 


            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_bevel:            
                row.prop(tp_props, "display_bevel", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_bevel", text="", icon="SCRIPTWIN")
                
            row.label("Bevel")

            is_bevel = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'BEVEL' :
                    is_bevel = True
            
            if is_bevel == True:
             
                if context.mode == 'EDIT_MESH':
                    row.operator("transform.edge_bevelweight", text="", icon='COLLAPSEMENU')   
                
                for mod in [m for m in ob.modifiers if m.type == 'BEVEL']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")

                row.operator("tp_ops.remove_mods_bevel", text="" , icon='X')                                                                                                                                                          
                row.operator("tp_ops.apply_mods_bevel", text="", icon='FILE_TICK')                                                                                                                                              
   
            else: 
                row.operator("tp_ops.mods_bevel", "", icon='PLUS')  
  
            box.separator()  
            
 

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
        
                        if tp_props.display_bevel:

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
                       
                        box.separator() 

            else:
                pass



        if scene.tp_mody == "tp_m6": 

            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_mirror:            
                row.prop(tp_props, "display_mirror", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_mirror", text="", icon="SCRIPTWIN")
                
            row.label("Mirror")

            is_mirror = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'MIRROR' :
                    is_mirror = True
            
            if is_mirror == True:
                
                for mod in [m for m in ob.modifiers if m.type == 'MIRROR']:   
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")

                row.operator("tp_ops.remove_mods_mirror", text="", icon='X') 
                row.operator("tp_ops.apply_mods_mirror", text="", icon='FILE_TICK')

                box.separator() 
                
            else:   
                box.separator() 
                
                row = box.row(1)
                row.scale_x = 0.6             
                row.operator("tp_ops.mod_mirror_x")
                row.operator("tp_ops.mod_mirror_y")
                row.operator("tp_ops.mod_mirror_z")            

                box.separator() 
                
            obj = context.active_object
            if obj:
 
                mo_types = []            
                append = mo_types.append

                for mo in context.active_object.modifiers:
                                                  
                    if mo.type == 'MIRROR':
                        append(mo.type)
                        #box.label(mo.name)

                        box.separator() 

                        row = box.row(1)
                        row.prop(mo, "use_x")
                        row.prop(mo, "use_y")
                        row.prop(mo, "use_z")
                        
                        row = box.row(1)
                        row.prop(mo, "use_mirror_merge", text="Merge")
                        row.prop(mo, "use_clip", text="Clipping")
                      
                        box.separator() 
                     
                        if mo.use_mirror_merge is True: 
                             
                            row = box.row()  
                            row.alignment = 'CENTER'
                            row.prop(mo, "merge_threshold", text="Merge")                     
                            box.separator()  
         
            else:
                pass

            if tp_props.display_mirror: 
            
                obj = context.active_object
                if obj:
     
                    mo_types = []            
                    append = mo_types.append

                    for mo in context.active_object.modifiers:
                                                      
                        if mo.type == 'MIRROR':
                            append(mo.type)   
                            
                            row = box.row(1)   
                            row.prop(mo, "use_mirror_vertex_groups", text="Vertex Groups")
                           
                            box.separator()                           
                          
                            row = box.row(1) 
                            row.label(text="Textures:")

                            row = box.row(1)
                            row.prop(row, "use_mirror_u", text="U")
                          
                            if mo.use_mirror_u:
                                row.prop(mo, "mirror_offset_u")                            
                          
                            row = box.row(1)                                                        
                            row.prop(row, "use_mirror_v", text="V")
                            
                            if mo.use_mirror_v:
                                row.prop(mo, "mirror_offset_v")
                            
                            box.separator() 
                          
                            row = box.row(1)
                            if mo.use_mirror_merge is True:
                                row.prop(mo, "merge_threshold")
                           
                            box.separator()                          
                         
                            row = box.column(1)                             
                            row.label(text="Mirror Object:")
                            row.prop(mo, "mirror_object", text="")



        if scene.tp_mody == "tp_m7": 

            box = col.box().column(1)
            
            row = box.row(1)
            if tp_props.display_subsurf:            
                row.prop(tp_props, "display_subsurf", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_subsurf", text="", icon="SCRIPTWIN")
                
            row.label("SubSurf")


            is_subsurf = False
            
            for mod in bpy.context.object.modifiers :
                if mod.type == 'SUBSURF' :
                    is_subsurf = True

            if is_subsurf == True:

                for mod in [m for m in ob.modifiers if m.type == 'SUBSURF']:
                    #bpy.ops.object.modifier_apply( modifier = mod.name )            
                
                    row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")             
               
                row.operator("tp_ops.remove_mods_subsurf", text="" , icon='X')             
                row.operator("tp_ops.apply_mods_subsurf", text="", icon='FILE_TICK')                                                                                                                                              
   
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
                            
                            row = box.row(1)
                            row.prop(mo, "use_opensubdiv",text="OPSubdiv")                    
                            row.prop(context.user_preferences.system, "opensubdiv_compute_type", text="")

                            box.separator() 

                else:
                    pass




            """
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
                """                                          

