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

from bpy.app.translations import pgettext_iface as iface_
#from ..ops_modifier.mods_ui import draw_mods_layout

types_mods =  [("tp_ms0"    ," "   ," "   ,"COLLAPSEMENU"        ,0),
               ("tp_ms1"    ," "   ," "   ,"MODIFIER"            ,1), 
               ("tp_ms2"    ," "   ," "   ,"MOD_DISPLACE"        ,2),
               ("tp_ms3"    ," "   ," "   ,"MOD_SMOOTH"          ,3), 
               ("tp_ms4"    ," "   ," "   ,"MOD_REMESH"          ,4), 
               ("tp_ms5"    ," "   ," "   ,"MOD_DECIM"           ,5), 
               ("tp_ms6"    ," "   ," "   ,"MOD_MIRROR"          ,6),
               ("tp_ms7"    ," "   ," "   ,"MOD_MULTIRES"        ,7)]

bpy.types.Scene.tp_msody = bpy.props.EnumProperty(name = " ", default = "tp_ms0", items = types_mods)



def draw_modifier_sculpt_ui(self, context, layout):
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
                row.operator("tp_ops.mod_displace", "", icon='PLUS')  

   
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
                row.operator("tp_ops.mod_smooth", "", icon='PLUS')                   


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
                row.operator("tp_ops.mod_remesh", "", icon='PLUS')    
           
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
                row.operator("tp_ops.mod_decimate", "", icon='PLUS')                   


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

