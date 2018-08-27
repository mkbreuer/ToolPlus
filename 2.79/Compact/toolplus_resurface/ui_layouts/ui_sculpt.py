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

from .. ui_menus.menu_sculpt import *



# MASK DEFAULT TOOLS #
def draw_sculpt_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface                  
        tp_sculpt = context.window_manager.tp_props_remesh                
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)
 
 
        box = col.box().column(1)      
        
        box.separator()    

        row = box.row(1)       
                
        props = row.operator("paint.hide_show", text="BBox Hide", icon ="BORDER_RECT")
        props.action = 'HIDE'
        props.area = 'INSIDE'

        row.operator("view3d.select_border", text="Box Mask", icon ="IMAGE_ZDEPTH") 


        row = box.row(1)

        props = row.operator("paint.hide_show", text="BBox Show", icon ="BORDERMOVE")
        props.action = 'SHOW'
        props.area = 'INSIDE' 

        props = row.operator("paint.hide_show", text="Hide Masked", icon ="BRUSH_TEXMASK")
        props.area = 'MASKED'
        props.action = 'HIDE'


        box.separator()  

        row = box.row(1)
        
        props = row.operator("paint.mask_flood_fill", text="Fill Mask", icon ="MATCAP_08")
        props.mode = 'VALUE'
        props.value = 1

        props = row.operator("paint.hide_show", text="Show All", icon ="SOLID")
        props.action = 'SHOW'
        props.area = 'ALL'


        row = box.row(1)
        row.operator("paint.mask_flood_fill", text="Invert Mask", icon ="FILE_REFRESH").mode='INVERT'                

        props = row.operator("paint.mask_flood_fill", text="Clear Mask", icon ="BRUSH_TEXFILL")
        props.mode = 'VALUE'
        props.value = 0    

        box.separator() 
        box = layout.box().column(1)              
        box.separator()    
           
        row = box.row(1)
        
        is_mirror = False    
        for mode in bpy.context.object.modifiers :
            if mode.type == 'MULTIRES' :
                is_mirror = True

        if is_mirror == False:        
            row.operator("tp_ops.multires_add", text="Add MultiRes", icon="MOD_MULTIRES")     
           
            box.separator()         
       
        if is_mirror == True:
            
            if tp_props.display_multiresset:            
                row.prop(tp_props, "display_multiresset", text="", icon="MOD_MULTIRES")
            else:
                row.prop(tp_props, "display_multiresset", text="", icon="MOD_MULTIRES")            
           
            row.operator("tp_ops.multires_subdiv", text="SubDiv").mode='subdiv'
            row.operator("tp_ops.multires_subdiv", text="Reset").mode='reset'            
            row.operator("tp_ops.remove_mods_multires", text="" , icon='X')             
            row.operator("tp_ops.apply_mods_multires", text="", icon='FILE_TICK')                    
            
            box.separator()
          
            row = box.row(1)           
            row.scale_x = 1             
            row.operator("tp_ops.subsurf_0")
            row.operator("tp_ops.subsurf_1")
            row.operator("tp_ops.subsurf_2")            
            row.operator("tp_ops.subsurf_3")
            row.operator("tp_ops.subsurf_4")
            row.operator("tp_ops.subsurf_5")
            row.operator("tp_ops.subsurf_6")            
           
            box.separator()

            
            if tp_props.display_multiresset:  
                    
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
                            
                            split = box.split()
                            col = split.column()
                            col.prop(mo, "levels", text="Preview")
                            col.prop(mo, "sculpt_levels", text="Sculpt")
                            col.prop(mo, "render_levels", text="Render")

                            col = split.column()                          
                            col.prop(mo, "use_subsurf_uv", text="SubDiv UV")
                            col.prop(mo, "show_only_control_edges", text="Iso Line")

                            box.separator()
                            
                else:
                    pass

       

        is_mirror = False    
        for mode in bpy.context.object.modifiers :
            if mode.type == 'MULTIRES' :
                is_mirror = True
        if is_mirror == False:        
   
            box.separator()

            row = box.row(1) 
            row.operator("tp_ops.mask_extract", text="Extract Mask", icon='MOD_MASK')
           
            button_wire_off = icons.get("icon_wire_off")                
            row.operator("tp_ops.resphere", text="", icon_value=button_wire_off.icon_id)

            row = box.row(1) 
            row.prop(tp_sculpt, "extractStyleEnum", text="")
            row.prop(tp_sculpt, "extractDepthFloat", text="Depth")
            
            row = box.row(1)             
            row.prop(tp_sculpt, "extractOffsetFloat", text="Offset")
            row.prop(tp_sculpt, "extractSmoothIterationsInt", text="Smooth")

            box.separator()


        box.separator()

        row = box.row(1) 
        row.operator("tp_ops.smooth_remesh", text='', icon='MOD_REMESH')
        row.operator("tp_ops.remesh", text='Remesh')

        is_remesh = False        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'REMESH' :
                is_remesh  = True

        if is_remesh  == True:
            row.prop(bpy.context.active_object.modifiers["Remesh"], "show_viewport", text="")  
            row.operator("tp_ops.remove_smooth_remesh", text="" , icon='X')                                 
            row.operator("tp_ops.apply_smooth_remesh", text="", icon='FILE_TICK')  
            obj = context.active_object

            mo_types = []
            append = mo_types.append
 
            row = box.row(1)             
            for mo in obj.modifiers:
           
                if mo.type == 'REMESH':
                    row.prop(mo, "octree_depth", text="Depth")
               
                if mo.type == 'SMOOTH':
                    row.prop(mo, "iterations", text="Smooth") 
        else:                 
 
            row.prop(tp_sculpt, 'remeshPreserveShape', text="KeepShape") 
            
            row = box.row(1) 
            row.prop(tp_sculpt, 'remeshDepthInt', text="Depth")
            row.prop(tp_sculpt, 'remeshSubdivisions', text="Smooth")


        box.separator()
        box.separator()

        row = box.row(1) 
        if tp_props.display_sculpt_decimate:
            row.prop(tp_props, "display_sculpt_decimate", text="", icon='MOD_DECIM')
        else:
            row.prop(tp_props, "display_sculpt_decimate", text="", icon='MOD_DECIM')

        row.operator("tp_ops.mod_decimate", text='Decimate')

        is_decimate = False        
        for mode in bpy.context.object.modifiers :
            if mode.type == 'DECIMATE' :
                is_decimate  = True

        if is_decimate  == True:
            row.prop(bpy.context.active_object.modifiers["Decimate"], "show_viewport", text="")              
            row.operator("tp_ops.remove_mods_decimate", text="" , icon='X')                                 
            row.operator("tp_ops.apply_mods_decimate", text="", icon='FILE_TICK')              
            
            obj = context.active_object
            mo_types = []
            append = mo_types.append

            row = box.row(1)  
            
            for mo in obj.modifiers:           
                if mo.type == 'DECIMATE':
                    row.prop(mo, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')    
                    row.prop(mo, "ratio")
                     
        else:                 
            pass
        

        if tp_props.display_sculpt_decimate:
           
            if is_decimate  == True:
                   
                    box.separator()  
                                     
                    row = box.row(1)
                    row.label(text="Mask", icon="BRUSH_MASK") 
                    row.operator("tp_ops.decimate_mask_paint", text="", icon="BRUSH_DATA")
                    row.operator("tp_ops.decimate_mask_areas", text="", icon="DISCLOSURE_TRI_RIGHT")
                    row.operator("tp_ops.decimate_mask_remove", text="", icon="DISCLOSURE_TRI_DOWN")
            else:
                box.separator() 
                               
                row = box.column(1) 
                row.label("no modifier active!")  


        box.separator()
        box.separator()
       
        row = box.row(1) 
        if tp_props.display_sculpt_noise:
            row.prop(tp_props, "display_sculpt_noise", text="", icon='ASSET_MANAGER')
        else:
            row.prop(tp_props, "display_sculpt_noise", text="", icon='ASSET_MANAGER')

        row.operator("tp_ops.add_displace_noise", text='Noise')

        is_displace = False        
        for mode in bpy.context.object.modifiers:
            if mode.type == 'DISPLACE':
                is_displace  = True

        if is_displace  == True:   
            row.prop(bpy.context.active_object.modifiers["Displace"], "show_viewport", text="")             
            row.operator("tp_ops.remove_mods_displace", text="" , icon='X')                                 
            row.operator("tp_ops.apply_mods_displace", text="", icon='FILE_TICK')              
            
            obj = context.active_object
            mo_types = []
            append = mo_types.append

            row = box.row(1)  
            
            for mo in obj.modifiers:           
                if mo.type == 'DISPLACE':
                    row.prop(mo, "strength")
                    row.prop(mo, "mid_level")
                                    
            
            box.separator()             
            
            row = box.row(1)
            row.label(text="Mask", icon="BRUSH_MASK") 
            row.operator("tp_ops.displace_mask_paint", text="", icon="BRUSH_DATA")    
            row.operator("tp_ops.displace_mask_areas", text="", icon="DISCLOSURE_TRI_RIGHT")            
            row.operator("tp_ops.displace_mask_remove", text="", icon="DISCLOSURE_TRI_DOWN")
  
  
        else:                 
            pass

        if tp_props.display_sculpt_noise:

            box.separator()            
            
            is_displace = False        
            for mode in bpy.context.object.modifiers:
                if mode.type == 'DISPLACE':
                    is_displace  = True

            if is_displace  == True:    
      
                row = box.row(1) 
                tex = bpy.data.textures["Sculpt_Noise"]

                box.prop(tex, "musgrave_type")    
                box.prop(tex, "noise_basis", "Noise:")                                 
                
                box.separator()               
               
                row = box.row(1)  
                
                row.prop(tex, "noise_scale", text="Size")         
                row.prop(tex, "noise_intensity", text="Intensity") 

                row = box.row(1)   
                row.prop(tex, "dimension_max", text="Dimension")
                row.prop(tex, "octaves")
               
                row = box.row(1)          
                row.prop(tex, "nabla")
                row.prop(tex, "lacunarity")

                
                musgrave_type = tex.musgrave_type
               
                col = box.column()           
                if musgrave_type in {'HETERO_TERRAIN', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL'}:
                    col.prop(tex, "offset")
               
                if musgrave_type in {'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL'}:
                    col.prop(tex, "gain")

            else:                     
                row = box.row(1)
                row.label(text="no displace active", icon="INFO") 

        box.separator()



# SCULPT EDIT #
def draw_sculpt_edit_ui(self, context, layout):
        
        tp_props = context.window_manager.tp_props_resurface            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)


        is_mirror = False    
        for mode in bpy.context.object.modifiers :
            if mode.type == 'MULTIRES' :
                is_mirror = True
        if is_mirror == False:   

            box = col.box().column(1) 
                      
            if not tp_props.display_sculpt_edit: 
            
                row = box.row(1)
                row.prop(tp_props, "display_sculpt_edit", text="", icon="TRIA_RIGHT", emboss = False)                
                
                row.label("Editing")                  
                row.operator("tp_ops.bool_freeze", text='', icon='RESTRICT_VIEW_ON')
                row.operator("tp_ops.bool_unfreeze", text='', icon='RESTRICT_VIEW_OFF')  
                row.menu("tp_menu.sculpt_edit", text='', icon='SNAP_FACE')
                         
            else:
                
                row = box.row(1)
                row.prop(tp_props, "display_sculpt_edit", text="", icon="TRIA_RIGHT", emboss = False)                
                
                row.label("Editing")                               

                box.separator()
                
                row = box.row(1) 
                row.operator("sculpt.geometry_smooth", text="Smooth")
                row.operator("sculpt.geometry_laplacian_smooth", text="Laplacian")
                 
                row = box.row(1) 
                row.operator("sculpt.geometry_decimate", text="Decimate")
                row.operator("sculpt.geometry_displace", text="Displace")
                 
                row = box.row(1) 
                row.operator("sculpt.geometry_subdivide_faces", text="Subdiv")
                row.operator("sculpt.geometry_subdivide_faces_smooth", text="SmoothDiv")
                 
                row = box.row(1) 
                row.operator("sculpt.geometry_beautify_faces", text="Beautify")

                box.separator()
                box.separator()
                
                row = box.row(1)             
                row.operator("tp_ops.bool_freeze", text='Freeze', icon='RESTRICT_VIEW_ON')
                row.operator("tp_ops.bool_unfreeze", text='UnFreeze', icon='RESTRICT_VIEW_OFF')  

                box.separator()


# SCULPT MASK #
def draw_sculpt_mask_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface            

        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)

        box = col.box().column(1) 
                  
        if not tp_props.display_sculpt_mask: 
        
            row = box.row(1)
            row.prop(tp_props, "display_sculpt_mask", text="", icon="TRIA_RIGHT", emboss = False)                
            
            row.label("Mask")                  
            row.menu("tp_menu.sculpt_mask", text="", icon='MOD_MASK')      

        else:
            
            row = box.row(1)
            row.prop(tp_props, "display_sculpt_mask", text="", icon="TRIA_RIGHT", emboss = False)                
            
            row.label("Mask")                  

            box.separator()
            
            row = box.row(1)                     
            row.operator("mesh.masktovgroup", text = "Mask to VertGrp", icon = 'MOD_MASK')
            
            row = box.row(1)               
            row.operator("mesh.masktovgroup_remove", text = "Remove", icon = 'DISCLOSURE_TRI_DOWN')
            row.operator("mesh.masktovgroup_append", text = "Append", icon = 'DISCLOSURE_TRI_RIGHT')      
          
            box.separator()
            box.separator()
           

            row = box.row(1)     
            row.operator("mesh.vgrouptomask", text = "VrtGrp to Mask", icon='MOD_MASK') 

            row = box.row(1)           
            row.operator("mesh.vgrouptomask_remove", text = "Remove", icon = 'DISCLOSURE_TRI_DOWN')
            row.operator("mesh.vgrouptomask_append", text = "Append", icon = 'DISCLOSURE_TRI_RIGHT')

            box.separator()
            box.separator()
          
            row = box.row(1) 
            row.operator("mesh.mask_from_edges", text = "Mask by Edges", icon = 'MOD_MASK')
            
            row = box.column(1)
            row.prop(context.scene, "mask_edge_angle", text = "Edge Angle",icon='MOD_MASK',slider = True)
            row.prop(context.scene ,"mask_edge_strength", text = "Mask Strength", icon='MOD_MASK',slider = True)
    

            box.separator()
            box.separator()
          
            row = box.row(1) 
            row.operator("mesh.mask_from_cavity", text = "Mask by Cavity", icon = 'MOD_MASK')
            
            row = box.column(1)
            row.prop(context.scene, "mask_cavity_angle", text = "Cavity Angle",icon='MOD_MASK',slider = True)
            row.prop(context.scene, "mask_cavity_strength", text = "Mask Strength", icon='MOD_MASK',slider = True)
            

            box.separator()
            box.separator()
           
            row = box.row(1) 
            row.operator("mesh.mask_smooth_all", text = "Mask Smooth", icon = 'MOD_MASK')
            
            row = box.column(1)
            row.prop(context.scene, "mask_smooth_strength", text = "Mask Smooth Strength", icon='MOD_MASK',slider = True)

            box.separator()            
                      