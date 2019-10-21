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

"""
bl_info = {
    "name": "TP Modifier Stack Type",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "VIEW3D",
    "description": "Modifier Stack Type",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}
"""

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



bpy.types.Scene.tp_mods_type_stack = bpy.props.EnumProperty(                            
                      items = [("wireframe",                "Wireframe",                "", "MOD_WIREFRAME",      1),                             
                               ("triangulate",              "Triangulate",              "", "MOD_UVPROJECT",      2),                                 
                               ("subsurf",                  "Subsurf",                  "", "MOD_SUBSURF",        3),                            
                               ("solidify",                 "Solidify",                 "", "MOD_SOLIDIFY",       4),                             
                               ("skin",                     "Skin",                     "", "MOD_SKIN",           5),                              
                               ("screw",                    "Screw",                    "", "MOD_SCREW",          6),                               
                               ("remesh",                   "Remesh",                   "", "MOD_REMESH",         7),                                  
                               ("multires",                 "Multires",                 "", "MOD_MULTIRES",       8),                                  
                               ("mirror",                   "Mirror",                   "", "MOD_MIRROR",         9),                                                                   
                               ("mask",                     "Mask",                     "", "MOD_MASK",          10),                                  
                               ("edge_split",               "Edge Split",               "", "MOD_EDGESPLIT",     11),                                   
                               ("decimate",                 "Decimate",                 "", "MOD_DECIM",         12),                                  
                               ("build",                    "Build",                    "", "MOD_BUILD",         13), 
                               ("boolean",                  "Boolean",                  "", "MOD_BOOLEAN",       14),  
                               ("bevel",                    "Bevel",                    "", "MOD_BEVEL",         15), 
                               ("array",                    "Array",                    "", "MOD_ARRAY",         16),                                   
                             
                               ("uv_warp",                  "UV Warp",                  "", "MOD_UVPROJECT",     17),                                                                      
                               ("uv_project",               "UV Project",               "", "MOD_UVPROJECT",     18),
                               ("wave",                     "Wave",                     "", "MOD_WAVE",          19),                                   
                               ("warp",                     "Warp",                     "", "MOD_WARP",          20),                                   
                               ("smooth",                   "Smooth",                   "", "MOD_SMOOTH",        21),                                   
                               ("simple_deform",            "Simple Deform",            "", "MOD_SIMPLEDEFORM",  22),                                   
                               ("shrinkwrap",               "Shrinkwrap",               "", "MOD_SHRINKWRAP",    23),                                   
                               ("mesh_deform",              "Mesh Deform",              "", "MOD_MESHDEFORM",    24),                                   
                               ("lattice",                  "Lattice",                  "", "MOD_LATTICE",       25),
                               ("laplaciandeform",          "Laplacian Deform",         "", "MOD_MESHDEFORM",    26),
                               ("laplaciansmooth",          "Laplacian Smooth",         "", "MOD_SMOOTH",        27),
                               ("hook",                     "Hook",                     "", "HOOK",              28),  
                               ("displace",                 "Displace",                 "", "MOD_DISPLACE",      29),
                               ("curve",                    "Curve",                    "", "MOD_CURVE",         30),
                               ("cast",                     "Cast",                     "", "MOD_CAST",          31),                                    
                               ("armature",                 "Armature",                 "", "MOD_ARMATURE",      32),                                   
            
                               ("vertex_weight_proximity",  "Vertex Weight Proximity",  "", "MOD_VERTEX_WEIGHT", 33),
                               ("vertex_weight_mix",        "Vertex Weight Mix",        "", "MOD_VERTEX_WEIGHT", 34),
                               ("vertex_weight_edit",       "Vertex Weight Edit",       "", "MOD_VERTEX_WEIGHT", 35),
                               ("mesh_cache",               "Mesh Cache",               "", "MOD_MESHDEFORM",    36),                                   
                               ("surface",                  "Surface",                  "", "PHYSICS",           37),                               
                               ("soft_body",                "Soft Body",                "", "MOD_SOFT",          38),
                               ("smoke",                    "Smoke",                    "", "MOD_SMOKE",         39),
                               ("particle_system",          "Particle System",          "", "MOD_PARTICLES",     40),
                               ("particle_instance",        "Particle Instance",        "", "MOD_PARTICLES",     41),
                               ("ocean",                    "Ocean",                    "", "MOD_OCEAN",         42),
                               ("fluid_simulation",         "Fluid Simulation",         "", "MOD_FLUIDSIM",      43),
                               ("explode",                  "Explode",                  "", "MOD_EXPLODE",       44),
                               ("dynamic_paint",            "Dynamic Paint",            "", "MOD_DYNAMICPAINT",  45),
                               ("collision",                "Collision",                "", "MOD_PHYSICS",       46),
                               ("cloth",                    "Cloth",                    "", "MOD_CLOTH",         47)], 

                               name = "Modifier Type", 
                               default = "array", 
                               description="modifier properties")



def draw_mods_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_menu_retopo        
        icons = load_icons()

        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
    
        col = layout.column(1)        
     
        box = col.box().column(1)
            
        row = box.row(1)      
        row.prop(context.scene, "tp_mods_type_stack", text="")

        box.separator()
      
        row = box.row(1) 
        
        obj = context.active_object
        if obj:
 
            md_types = []
            append = md_types.append

            if scene.tp_mods_type_stack == "armature":
                if (md.type == 'ARMATURE'):
                    obj.modifiers.remove(md)


            if scene.tp_mods_type_stack == "array":
               
                is_array = False
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'ARRAY':
                        is_array = True                 

                if is_array == True:                                          
                    if tp_props.display_array:            
                        row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
                    else:
                        row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
                else:
                    pass
              
                for md in obj.modifiers:  

                    if (md.type == 'ARRAY'): 
  
                        if tp_props.display_array:
                           
                            append(md.type)  

                            box.label("Array") 
                            
                            box.prop(md, "fit_type")

                            if md.fit_type == 'FIXED_COUNT':
                                box.prop(md, "count")
                            elif md.fit_type == 'FIT_LENGTH':
                                box.prop(md, "fit_length")
                            elif md.fit_type == 'FIT_CURVE':
                                box.prop(md, "curve")

                            box.separator()

                            split = box.split()

                            col = split.column()
                            col.prop(md, "use_constant_offset")
                            sub = col.column()
                            sub.active = md.use_constant_offset
                            sub.prop(md, "constant_offset_displace", text="")

                            col.separator()

                            col.prop(md, "use_merge_vertices", text="Merge")
                            sub = col.column()
                            sub.active = md.use_merge_vertices
                            sub.prop(md, "use_merge_vertices_cap", text="First Last")
                            sub.prop(md, "merge_threshold", text="Distance")

                            col = split.column()
                            col.prop(md, "use_relative_offset")
                            sub = col.column()
                            sub.active = md.use_relative_offset
                            sub.prop(md, "relative_offset_displace", text="")

                            col.separator()

                            col.prop(md, "use_object_offset")
                            sub = col.column()
                            sub.active = md.use_object_offset
                            sub.prop(md, "offset_object", text="")

                            box.separator()

                            box.prop(md, "start_cap")
                            box.prop(md, "end_cap")

                        else:
                            pass

                            



            if scene.tp_mods_type_stack == "bevel":

                is_array = False
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'ARRAY':
                        is_array = True                 

                if is_array == True:                                          
                    if tp_props.display_array:            
                        row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
                    else:
                        row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
                else:
                    pass
              
                for md in obj.modifiers:  

                    if (md.type == 'BEVEL'): 
  
                        if tp_props.display_array:
                           
                            append(md.type)  

                            box.label("Array") 


            if scene.tp_mods_type_stack == "boolean":
                is_array = False
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'ARRAY':
                        is_array = True                 

                if is_array == True:                                          
                    if tp_props.display_array:            
                        row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
                    else:
                        row.prop(tp_props, "display_array", text="", icon="MOD_ARRAY")
                else:
                    pass
              
                for md in obj.modifiers:  

                    if (md.type == 'BOOLEAN'): 
  
                        if tp_props.display_array:
                           
                            append(md.type)  

                            box.label("Array") 

            """
            if scene.tp_mods_type_stack == "build":
                if (md.type == 'BUILD'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "mesh_cache":
                if (md.type == 'MESH_CACHE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "cast":
                if (md.type == 'CAST'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "cloth":
                if (md.type == 'CLOTH'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "collision":
                if (md.type == 'COLLISION'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "curve":
                if (md.type == 'CURVE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "decimate":
                if (md.type == 'DECIMATE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "displace":
                if (md.type == 'DISPLACE'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "dynamic_paint":
                if (md.type == 'DYNAMIC_PAINT'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "edge_split":
                if (md.type == 'EDGE_SPLIT'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "explode":
                if (md.type == 'EXPLODE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "fluid_simulation":
                if (md.type == 'FLUID_SIMULATION'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "hook":
                if (md.type == 'HOOK'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "laplaciandeform":
                if (md.type == 'LAPLACIANDEFORM'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "laplaciansmooth":
                if (md.type == 'LAPLACIANSMOOTH'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "lattice":
                if (md.type == 'LATTICE'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "mask":
                if (md.type == 'MASK'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "mesh_deform":
                if (md.type == 'MESH_DEFORM'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "mirror":
                if (md.type == 'MIRROR'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "multires":
                if (md.type == 'MULTIRES'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "ocean":
                if (md.type == 'OCEAN'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "particle_instance":
                if (md.type == 'PARTICLE_INSTANCE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "particle_system":
                if (md.type == 'PARTICLE_SYSTEM'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "screw":
                if (md.type == 'SCREW'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "shrinkwrap":
                if (md.type == 'SHRINKWRAP'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "simple_deform":
                if (md.type == 'SIMPLE_DEFORM'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "smoke":
                if (md.type == 'SMOKE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "smooth":
                if (md.type == 'SMOOTH'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "soft_body":
                if (md.type == 'SOFT_BODY'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "solidify":
                if (md.type == 'SOLIDIFY'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "subsurf":
                if (md.type == 'SUBSURF'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "surface":
                if (md.type == 'SURFACE'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "uv_project":
                if (md.type == 'UV_PROJECT'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "warp":
                if (md.type == 'WARP'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "wave":
                if (md.type == 'WAVE'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "remesh":
                if (md.type == 'REMESH'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "vertex_weight_edit":
                if (md.type == 'VERTEX_WEIGHT_EDIT'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "vertex_weight_mix":
                if (md.type == 'VERTEX_WEIGHT_MIX'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "vertex_weight_proximity":
                if (md.type == 'VERTEX_WEIGHT_PROXIMITY'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "skin":
                if (md.type == 'SKIN'):
                    obj.modifiers.remove(md)

            if scene.tp_mods_type_stack == "triangulate":
                if (md.type == 'TRIANGULATE'):
                    obj.modifiers.remove(md)
                                                                                                                    
            if scene.tp_mods_type_stack == "uv_warp":
                if (md.type == 'UV_WARP'):
                    obj.modifiers.remove(md)
                    
            if scene.tp_mods_type_stack == "wireframe":
                if (md.type == 'WIREFRAME'):
                    obj.modifiers.remove(md)

            """                    

