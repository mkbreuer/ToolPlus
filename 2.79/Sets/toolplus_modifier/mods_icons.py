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

from .mods_ui import draw_mods_layout

bpy.types.Scene.tp_modly_type = bpy.props.EnumProperty(                            
                      items = [("non",                      "",                  "", "MODIFIER",           0),                                                        
                               ("wireframe",                "",                "", "MOD_WIREFRAME",      1),                             
                               ("triangulate",              "",              "", "MOD_TRIANGULATE",    2),                                 
                               ("subsurf",                  "",                  "", "MOD_SUBSURF",        3),                            
                               ("solidify",                 "",                 "", "MOD_SOLIDIFY",       4),                             
                               ("skin",                     "",                     "", "MOD_SKIN",           5),                              
                               ("screw",                    "",                    "", "MOD_SCREW",          6),                               
                               ("remesh",                   "",                   "", "MOD_REMESH",         7),                                  
                               ("multires",                 "",                 "", "MOD_MULTIRES",       8),                                  
                               ("mirror",                   "",                   "", "MOD_MIRROR",         9),                                                                   
                               ("mask",                     "",                     "", "MOD_MASK",          10),                                  
                               ("edge_split",               "",               "", "MOD_EDGESPLIT",     11),                                   
                               ("decimate",                 "",                 "", "MOD_DECIM",         12),                                  
                               ("build",                    "",                    "", "MOD_BUILD",         13), 
                               ("boolean",                  "",                  "", "MOD_BOOLEAN",       14),  
                               ("bevel",                    "",                    "", "MOD_BEVEL",         15), 
                               ("array",                    "",                    "", "MOD_ARRAY",         16),                                   
                            
                               ("all",                      "",              "", "MODIFIER",          17),
                               ("uv_warp",                  "",                  "", "MOD_UVPROJECT",     19),                                                                      
                               ("uv_project",               "",               "", "MOD_UVPROJECT",     20),
                               ("wave",                     "",                     "", "MOD_WAVE",          21),                                   
                               ("warp",                     "",                     "", "MOD_WARP",          22),                                   
                               ("smooth",                   "",                   "", "MOD_SMOOTH",        23),                                   
                               ("simple_deform",            "",            "", "MOD_SIMPLEDEFORM",  24),                                   
                               ("shrinkwrap",               "",               "", "MOD_SHRINKWRAP",    25),                                   
                               ("mesh_deform",              "",              "", "MOD_MESHDEFORM",    26),                                   
                               ("lattice",                  "",                  "", "MOD_LATTICE",       27),
                               ("laplaciandeform",          "",         "", "MOD_MESHDEFORM",    28),
                               ("laplaciansmooth",          "",         "", "MOD_SMOOTH",        29),
                               ("hook",                     "",                     "", "HOOK",              30),  
                               ("displace",                 "",                 "", "MOD_DISPLACE",      31),
                               ("curve",                    "",                    "", "MOD_CURVE",         32),
                               ("cast",                     "",                     "", "MOD_CAST",          33),                                    
                               ("armature",                 "",                 "", "MOD_ARMATURE",      34),                                   
                                          
                               ("vertex_weight_proximity",  "",  "", "MOD_VERTEX_WEIGHT", 35),
                               ("vertex_weight_mix",        "",        "", "MOD_VERTEX_WEIGHT", 36),
                               ("vertex_weight_edit",       "",       "", "MOD_VERTEX_WEIGHT", 37),
                               ("mesh_cache",               "",               "", "MOD_MESHDEFORM",    38),                                   
                               ("surface",                  "",                  "", "PHYSICS",           39),                               
                               ("soft_body",                "",                "", "MOD_SOFT",          40),
                               ("smoke",                    "",                    "", "MOD_SMOKE",         41),
                               ("particle_system",          "",          "", "MOD_PARTICLES",     42),
                               ("particle_instance",        "",        "", "MOD_PARTICLES",     43),
                               ("ocean",                    "",                    "", "MOD_OCEAN",         44),
                               ("fluid_simulation",         "",         "", "MOD_FLUIDSIM",      45),
                               ("explode",                  "",                  "", "MOD_EXPLODE",       46),
                               ("dynamic_paint",            "",            "", "MOD_DYNAMICPAINT",  47),
                               ("collision",                "",                "", "MOD_PHYSICS",       48),
                               ("cloth",                    "",                    "", "MOD_CLOTH",         49)],  

                               name = "Modifier Type", 
                               default = "non", 
                               description="change modifier type")
                               
                               
types_mods =  [("tp_ms0"    ," "   ," "   ,"COLLAPSEMENU"        ,0),
               ("tp_ms1"    ," "   ," "   ,"MODIFIER"            ,1), 
               ("tp_ms2"    ," "   ," "   ,"MOD_DISPLACE"        ,2),
               ("tp_ms3"    ," "   ," "   ,"MOD_SMOOTH"          ,3), 
               ("tp_ms4"    ," "   ," "   ,"MOD_REMESH"          ,4), 
               ("tp_ms5"    ," "   ," "   ,"MOD_DECIM"           ,5), 
               ("tp_ms6"    ," "   ," "   ,"MOD_MIRROR"          ,6),
               ("tp_ms7"    ," "   ," "   ,"MOD_MULTIRES"        ,7)]

bpy.types.Scene.tp_msody = bpy.props.EnumProperty(name = " ", default = "tp_ms0", items = types_mods)
                       

                               
types_mods =  [("tp_m0"    ," "   ," "   ,"COLLAPSEMENU"        ,0),
               ("tp_m1"    ," "   ," "   ,"MODIFIER"            ,1), 
               ("tp_m2"    ," "   ," "   ,"MOD_LATTICE"         ,2), 
               ("tp_m3"    ," "   ," "   ,"MOD_SCREW"           ,3), 
               ("tp_m4"    ," "   ," "   ,"MOD_SOLIDIFY"        ,4),
               ("tp_m5"    ," "   ," "   ,"MOD_BEVEL"           ,5),
               ("tp_m6"    ," "   ," "   ,"MOD_MIRROR"          ,6),
               ("tp_m7"    ," "   ," "   ,"MOD_SUBSURF"         ,7)]

bpy.types.Scene.tp_mody = bpy.props.EnumProperty(name = " ", default = "tp_m0", items = types_mods)


def draw_mods_icons_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_menu_modifier        
        icons = load_icons()
  
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 

        col = layout.column(1)

        box = col.box().column(1) 
        

        if context.mode =="SCULPT":

            row = box.row(1)  
            row.prop(scene, 'tp_msody', emboss = False, expand = True) #icon_only=True,


            if scene.tp_msody == "tp_ms0": 
                pass


            if scene.tp_msody == "tp_ms1": 
               
                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_addmods:            
                    row.prop(tp_props, "display_addmods", text="", icon="SCRIPTWIN")
                else:
                    row.prop(tp_props, "display_addmods", text="", icon="SCRIPTWIN")
                    
                row.label("Modifier")

             
                row.operator_menu_enum("object.modifier_add", "type","", icon="DISCLOSURE_TRI_RIGHT") 


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
                            
                else:
                    pass



            if scene.tp_msody == "tp_ms2": 

                box = col.box().column(1)
                                
                row = box.row(1)
                if tp_props.display_sculpt_displace:            
                    row.prop(tp_props, "display_sculpt_displace", text="", icon="SCRIPTWIN")
                else:
                    row.prop(tp_props, "display_sculpt_displace", text="", icon="SCRIPTWIN")
                               
                row.label("Displace")

                is_displace = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'DISPLACE':
                        is_displace = True
                
                if is_displace == True:
                    ob = context.object
                    for mod in [m for m in ob.modifiers if m.type == 'DISPLACE']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
                    row.operator("tp_ops.remove_mods_displace", text="" , icon='X')             
                    row.operator("tp_ops.apply_mods_displace", text="", icon='FILE_TICK')                                                                                                                                            
                else:   
                    row.operator("tp_ops.mod_displace", "", icon='DISCLOSURE_TRI_RIGHT')  

       
                box.separator()  
                                                          
                obj = context.active_object
                if obj:
     
                    mo_types = []
                    append = mo_types.append

                    for mo in obj.modifiers:
                                    
                        if mo.type == 'DISPLACE':
                            
                            append(mo.type)
                            
                            row = box.column(1)  
                            row.prop(mo, "mid_level")
                            row.prop(mo, "strength")
                            
                            if tp_props.display_sculpt_displace:  

                                has_texture = (mo.texture is not None)

                                col = box.column(align=True)
                                col.label(text="Texture:")
                                col.template_ID(mo, "texture", new="texture.new")

                                split = box.split()

                                col = split.column(align=True)
                                col.label(text="Direction:")
                                col.prop(mo, "direction", text="")
                               
                                if mo.direction in {'X', 'Y', 'Z', 'RGB_TO_XYZ'}:
                                    col.label(text="Space:")
                                    col.prop(mo, "space", text="")
                               
                                col.label(text="Vertex Group:")
                                col.prop_search(mo, "vertex_group", ob, "vertex_groups", text="")

                                col = split.column(align=True)
                               
                                col.active = has_texture
                                col.label(text="Texture Coordinates:")
                                col.prop(mo, "texture_coords", text="")
                              
                                if mo.texture_coords == 'OBJECT':
                                    col.label(text="Object:")
                                    col.prop(mo, "texture_coords_object", text="")
                               
                                elif mo.texture_coords == 'UV' and ob.type == 'MESH':
                                    col.label(text="UV Map:")
                                    col.prop_search(mo, "uv_layer", ob.data, "uv_textures", text="")

                            box.separator() 

                else:
                    pass




            if scene.tp_msody == "tp_ms3": 
                      

                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_smooth:            
                    row.prop(tp_props, "display_smooth", text="", icon="SCRIPTWIN")
                else:
                    row.prop(tp_props, "display_smooth", text="", icon="SCRIPTWIN")
                                         
                row.label("Smooth")
               
                is_smooth = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'SMOOTH':
                        is_smooth = True
                
                if is_smooth == True:
                    ob = context.object
                    for mod in [m for m in ob.modifiers if m.type == 'SMOOTH']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
                    row.operator("tp_ops.remove_mods_smooth", text="" , icon='X')                                 
                    row.operator("tp_ops.apply_mods_smooth", text="", icon='FILE_TICK')                                                                                                                                          
                else:   
                    row.operator("tp_ops.mod_smooth", "", icon='DISCLOSURE_TRI_RIGHT')                   


                box.separator()  
                
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



            if scene.tp_msody == "tp_ms4": 

                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_remesh:            
                    row.prop(tp_props, "display_remesh", text="", icon="SCRIPTWIN")
                else:
                    row.prop(tp_props, "display_remesh", text="", icon="SCRIPTWIN")
                    
                row.label("Remesh")

                is_remesh = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'REMESH' :
                        is_remesh  = True

                if is_remesh  == True:
                    ob = context.object
                    for mod in [m for m in ob.modifiers if m.type == 'REMESH']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
                    row.operator("tp_ops.remove_mods_remesh", text="" , icon='X')                                 
                    row.operator("tp_ops.apply_mods_remesh", text="", icon='FILE_TICK')                                                                                                                                          
                else:   
                    row.operator("tp_ops.mod_remesh", "", icon='DISCLOSURE_TRI_RIGHT')    
               
                box.separator()                      
                       
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





            if scene.tp_msody == "tp_ms5": 
                      

                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_decimate:            
                    row.prop(tp_props, "display_decimate", text="", icon="SCRIPTWIN")
                else:
                    row.prop(tp_props, "display_decimate", text="", icon="SCRIPTWIN")
                                         
                row.label("Decimate")
               
                is_decimate = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'DECIMATE':
                        is_decimate = True
                
                if is_decimate == True:
                    ob = context.object
                    for mod in [m for m in ob.modifiers if m.type == 'DECIMATE']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")   
                    row.operator("tp_ops.remove_mods_decimate", text="" , icon='X')                                 
                    row.operator("tp_ops.apply_mods_decimate", text="", icon='FILE_TICK')                                                                                                                                          
                else:   
                    row.operator("tp_ops.mod_decimate", "", icon='DISCLOSURE_TRI_RIGHT')                   


                box.separator()  
                
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







            if scene.tp_msody == "tp_ms6": 

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
                    ob = context.object
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



            if scene.tp_msody == "tp_ms7": 

                box = col.box().column(1)
                
                row = box.row(1)
                if tp_props.display_multires:            
                    row.prop(tp_props, "display_multires", text="", icon="SCRIPTWIN")
                else:
                    row.prop(tp_props, "display_multires", text="", icon="SCRIPTWIN")
                    
                row.label("MultiRes")

                is_multires = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'MULITRES' :
                        is_multires = True

                if is_multires == True:
                    ob = context.object
                    for mod in [m for m in ob.modifiers if m.type == 'MULITRES']:   
                        row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="")            
                    row.operator("tp_ops.remove_mods_mulitres", text="" , icon='X')             
                    row.operator("tp_ops.apply_mods_mulitres", text="", icon='FILE_TICK')                                                                                                                                              
       
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
         
                if tp_props.display_multires:  
                        
                    obj = context.active_object
                    if obj:
         
                        mo_types = []
                        append = mo_types.append

                        for mo in obj.modifiers:
                            if mo.type == 'MULITRES':
                                append(mo.type)

                                #box.label(mo.name)

                                row = box.row(1)

                                box.row().prop(mo, "subdivision_type", expand=True)

                                split = box.split()
                                
                                col = split.column()
                                col.prop(mo, "levels", text="Preview")
                                col.prop(mo, "sculpt_levels", text="Sculpt")
                                col.prop(mo, "render_levels", text="Render")

                                col = split.column()

                                col.enabled = ob.mode != 'EDIT'
                                col.operator("object.multires_subdivide", text="Subdivide")
                                col.operator("object.multires_higher_levels_delete", text="Delete Higher")
                                col.operator("object.multires_reshape", text="Reshape")
                                col.operator("object.multires_base_apply", text="Apply Base")
                                col.prop(mo, "use_subsurf_uv")
                                col.prop(mo, "show_only_control_edges")

                                box.separator() 

                    else:
                        pass



        # ALL OTHER MODE #
        else:

            row = box.row(1)
            row.prop(scene, 'tp_mody', emboss = False, expand = True) 
            
            # How to create column_flow into enum?
            #col.prop(scene, 'tp_modly_type', emboss = False, expand = True) 


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

             
                row.operator_menu_enum("object.modifier_add", "type","", icon="DISCLOSURE_TRI_RIGHT") 


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
                        row.operator("object.easy_lattice", text="", icon = "DISCLOSURE_TRI_RIGHT")       

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
                    row.operator("tp_ops.mod_screw", "", icon='DISCLOSURE_TRI_RIGHT')                   


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
                    row.operator("tp_ops.mods_solidify", "", icon='DISCLOSURE_TRI_RIGHT')  

       
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
                    row.operator("tp_ops.mods_bevel", "", icon='DISCLOSURE_TRI_RIGHT')  
      
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
                    row.operator("tp_ops.mod_sdeform", "", icon='DISCLOSURE_TRI_RIGHT')                   


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

