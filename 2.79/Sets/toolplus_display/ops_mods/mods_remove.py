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

"""
bl_info = {
    "name": "TP Remove Modifier by Type",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "VIEW3D",
    "description": "Remove Modifier by Type",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}
"""


import bpy



class VIEW3D_TP_Remove_Modifier_Type(bpy.types.Operator):
    """remove modifier by type"""
    bl_idname = "tp_ops.remove_mods_type"
    bl_label = "Mods Type Remove"
    bl_options = {'REGISTER', 'UNDO'}


    bpy.types.Scene.tp_mods_type = bpy.props.EnumProperty(                            
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
                                   description="modfier type for remove")

  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active

                #modifiers = obj.modifiers
                     
                for modifier in obj.modifiers: 
                                     
                    if scene.tp_mods_type == "armature":
                        if (modifier.type == 'ARMATURE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "array":
                        if (modifier.type == 'ARRAY'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "bevel":
                        if (modifier.type == 'BEVEL'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "boolean":
                        if (modifier.type == 'BOOLEAN'):
                            obj.modifiers.remove(modifier)
                   
                    if scene.tp_mods_type == "build":
                        if (modifier.type == 'BUILD'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "mesh_cache":
                        if (modifier.type == 'MESH_CACHE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "cast":
                        if (modifier.type == 'CAST'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "cloth":
                        if (modifier.type == 'CLOTH'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "collision":
                        if (modifier.type == 'COLLISION'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "curve":
                        if (modifier.type == 'CURVE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "decimate":
                        if (modifier.type == 'DECIMATE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "displace":
                        if (modifier.type == 'DISPLACE'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "dynamic_paint":
                        if (modifier.type == 'DYNAMIC_PAINT'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "edge_split":
                        if (modifier.type == 'EDGE_SPLIT'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "explode":
                        if (modifier.type == 'EXPLODE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "fluid_simulation":
                        if (modifier.type == 'FLUID_SIMULATION'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "hook":
                        if (modifier.type == 'HOOK'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "laplaciandeform":
                        if (modifier.type == 'LAPLACIANDEFORM'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "laplaciansmooth":
                        if (modifier.type == 'LAPLACIANSMOOTH'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "lattice":
                        if (modifier.type == 'LATTICE'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "mask":
                        if (modifier.type == 'MASK'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "mesh_deform":
                        if (modifier.type == 'MESH_DEFORM'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "mirror":
                        if (modifier.type == 'MIRROR'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "multires":
                        if (modifier.type == 'MULTIRES'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "ocean":
                        if (modifier.type == 'OCEAN'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "particle_instance":
                        if (modifier.type == 'PARTICLE_INSTANCE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "particle_system":
                        if (modifier.type == 'PARTICLE_SYSTEM'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "screw":
                        if (modifier.type == 'SCREW'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "shrinkwrap":
                        if (modifier.type == 'SHRINKWRAP'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "simple_deform":
                        if (modifier.type == 'SIMPLE_DEFORM'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "smoke":
                        if (modifier.type == 'SMOKE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "smooth":
                        if (modifier.type == 'SMOOTH'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "soft_body":
                        if (modifier.type == 'SOFT_BODY'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "solidify":
                        if (modifier.type == 'SOLIDIFY'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "subsurf":
                        if (modifier.type == 'SUBSURF'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "surface":
                        if (modifier.type == 'SURFACE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "uv_project":
                        if (modifier.type == 'UV_PROJECT'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "warp":
                        if (modifier.type == 'WARP'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "wave":
                        if (modifier.type == 'WAVE'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "remesh":
                        if (modifier.type == 'REMESH'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "vertex_weight_edit":
                        if (modifier.type == 'VERTEX_WEIGHT_EDIT'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "vertex_weight_mix":
                        if (modifier.type == 'VERTEX_WEIGHT_MIX'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "vertex_weight_proximity":
                        if (modifier.type == 'VERTEX_WEIGHT_PROXIMITY'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "skin":
                        if (modifier.type == 'SKIN'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "triangulate":
                        if (modifier.type == 'TRIANGULATE'):
                            obj.modifiers.remove(modifier)
                                                                                                                            
                    if scene.tp_mods_type == "uv_warp":
                        if (modifier.type == 'UV_WARP'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "wireframe":
                        if (modifier.type == 'WIREFRAME'):
                            obj.modifiers.remove(modifier)

  
        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                                
                    if scene.tp_mods_type == "armature":
                        if (modifier.type == 'ARMATURE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "array":
                        if (modifier.type == 'ARRAY'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "bevel":
                        if (modifier.type == 'BEVEL'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "boolean":
                        if (modifier.type == 'BOOLEAN'):
                            obj.modifiers.remove(modifier)
                   
                    if scene.tp_mods_type == "build":
                        if (modifier.type == 'BUILD'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "mesh_cache":
                        if (modifier.type == 'MESH_CACHE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "cast":
                        if (modifier.type == 'CAST'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "cloth":
                        if (modifier.type == 'CLOTH'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "collision":
                        if (modifier.type == 'COLLISION'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "curve":
                        if (modifier.type == 'CURVE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "decimate":
                        if (modifier.type == 'DECIMATE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "displace":
                        if (modifier.type == 'DISPLACE'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "dynamic_paint":
                        if (modifier.type == 'DYNAMIC_PAINT'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "edge_split":
                        if (modifier.type == 'EDGE_SPLIT'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "explode":
                        if (modifier.type == 'EXPLODE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "fluid_simulation":
                        if (modifier.type == 'FLUID_SIMULATION'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "hook":
                        if (modifier.type == 'HOOK'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "laplaciandeform":
                        if (modifier.type == 'LAPLACIANDEFORM'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "laplaciansmooth":
                        if (modifier.type == 'LAPLACIANSMOOTH'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "lattice":
                        if (modifier.type == 'LATTICE'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "mask":
                        if (modifier.type == 'MASK'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "mesh_deform":
                        if (modifier.type == 'MESH_DEFORM'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "mirror":
                        if (modifier.type == 'MIRROR'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "multires":
                        if (modifier.type == 'MULTIRES'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "ocean":
                        if (modifier.type == 'OCEAN'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "particle_instance":
                        if (modifier.type == 'PARTICLE_INSTANCE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "particle_system":
                        if (modifier.type == 'PARTICLE_SYSTEM'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "screw":
                        if (modifier.type == 'SCREW'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "shrinkwrap":
                        if (modifier.type == 'SHRINKWRAP'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "simple_deform":
                        if (modifier.type == 'SIMPLE_DEFORM'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "smoke":
                        if (modifier.type == 'SMOKE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "smooth":
                        if (modifier.type == 'SMOOTH'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "soft_body":
                        if (modifier.type == 'SOFT_BODY'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "solidify":
                        if (modifier.type == 'SOLIDIFY'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "subsurf":
                        if (modifier.type == 'SUBSURF'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "surface":
                        if (modifier.type == 'SURFACE'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "uv_project":
                        if (modifier.type == 'UV_PROJECT'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "warp":
                        if (modifier.type == 'WARP'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "wave":
                        if (modifier.type == 'WAVE'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "remesh":
                        if (modifier.type == 'REMESH'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "vertex_weight_edit":
                        if (modifier.type == 'VERTEX_WEIGHT_EDIT'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "vertex_weight_mix":
                        if (modifier.type == 'VERTEX_WEIGHT_MIX'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "vertex_weight_proximity":
                        if (modifier.type == 'VERTEX_WEIGHT_PROXIMITY'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "skin":
                        if (modifier.type == 'SKIN'):
                            obj.modifiers.remove(modifier)

                    if scene.tp_mods_type == "triangulate":
                        if (modifier.type == 'TRIANGULATE'):
                            obj.modifiers.remove(modifier)
                                                                                                                            
                    if scene.tp_mods_type == "uv_warp":
                        if (modifier.type == 'UV_WARP'):
                            obj.modifiers.remove(modifier)
                            
                    if scene.tp_mods_type == "wireframe":
                        if (modifier.type == 'WIREFRAME'):
                            obj.modifiers.remove(modifier)

                            

        return {'FINISHED'}

        
        



    
def register():
    
    bpy.utils.register_module(__name__)

def unregister():
   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


