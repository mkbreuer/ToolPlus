# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# "Display Layers", by "author": "Vincent Gires",
# http://vincentgires.com/tools/blender/addons/display_layers/v012/display_layers.py


import bpy
from bpy import*
from bpy.props import *


bpy.types.Scene.tp_funcly_type = bpy.props.EnumProperty(                            
                      items = [("unhide",      "(Un)Hide",     "",   "RESTRICT_VIEW_OFF",     1),                                 
                               ("apply",       "Apply",        "",   "FILE_TICK",             2),                                 
                               ("remove",      "Remove",       "",   "X",                     3),  
                               ("render",      "Render ",      "",   "RESTRICT_RENDER_OFF",   4), 
                               ("down",        "Down",         "",   "TRIA_DOWN",             5),
                               ("up",          "UP",           "",   "TRIA_UP",               6)], 
 
                               name = "Modifier Function Type", 
                               default = "unhide", 
                               description="modifier function type")


bpy.types.Scene.tp_modly_type = bpy.props.EnumProperty(                            
                      items = [("non",                      "NonModi",                  "", "MODIFIER",           0),                                                        
                               ("wireframe",                "Wireframe",                "", "MOD_WIREFRAME",      1),                             
                               ("triangulate",              "Triangulate",              "", "MOD_TRIANGULATE",    2),                                 
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
                            
                               ("all",                      "AllModifier",              "", "MODIFIER",          17),
                               ("uv_warp",                  "UV Warp",                  "", "MOD_UVPROJECT",     19),                                                                      
                               ("uv_project",               "UV Project",               "", "MOD_UVPROJECT",     20),
                               ("wave",                     "Wave",                     "", "MOD_WAVE",          21),                                   
                               ("warp",                     "Warp",                     "", "MOD_WARP",          22),                                   
                               ("smooth",                   "Smooth",                   "", "MOD_SMOOTH",        23),                                   
                               ("simple_deform",            "Simple Deform",            "", "MOD_SIMPLEDEFORM",  24),                                   
                               ("shrinkwrap",               "Shrinkwrap",               "", "MOD_SHRINKWRAP",    25),                                   
                               ("mesh_deform",              "Mesh Deform",              "", "MOD_MESHDEFORM",    26),                                   
                               ("lattice",                  "Lattice",                  "", "MOD_LATTICE",       27),
                               ("laplaciandeform",          "Laplacian Deform",         "", "MOD_MESHDEFORM",    28),
                               ("laplaciansmooth",          "Laplacian Smooth",         "", "MOD_SMOOTH",        29),
                               ("hook",                     "Hook",                     "", "HOOK",              30),  
                               ("displace",                 "Displace",                 "", "MOD_DISPLACE",      31),
                               ("curve",                    "Curve",                    "", "MOD_CURVE",         32),
                               ("cast",                     "Cast",                     "", "MOD_CAST",          33),                                    
                               ("armature",                 "Armature",                 "", "MOD_ARMATURE",      34),                                   
                                          
                               ("vertex_weight_proximity",  "Vertex Weight Proximity",  "", "MOD_VERTEX_WEIGHT", 35),
                               ("vertex_weight_mix",        "Vertex Weight Mix",        "", "MOD_VERTEX_WEIGHT", 36),
                               ("vertex_weight_edit",       "Vertex Weight Edit",       "", "MOD_VERTEX_WEIGHT", 37),
                               ("mesh_cache",               "Mesh Cache",               "", "MOD_MESHDEFORM",    38),                                   
                               ("surface",                  "Surface",                  "", "PHYSICS",           39),                               
                               ("soft_body",                "Soft Body",                "", "MOD_SOFT",          40),
                               ("smoke",                    "Smoke",                    "", "MOD_SMOKE",         41),
                               ("particle_system",          "Particle System",          "", "MOD_PARTICLES",     42),
                               ("particle_instance",        "Particle Instance",        "", "MOD_PARTICLES",     43),
                               ("ocean",                    "Ocean",                    "", "MOD_OCEAN",         44),
                               ("fluid_simulation",         "Fluid Simulation",         "", "MOD_FLUIDSIM",      45),
                               ("explode",                  "Explode",                  "", "MOD_EXPLODE",       46),
                               ("dynamic_paint",            "Dynamic Paint",            "", "MOD_DYNAMICPAINT",  47),
                               ("collision",                "Collision",                "", "MOD_PHYSICS",       48),
                               ("cloth",                    "Cloth",                    "", "MOD_CLOTH",         49)],  

                               name = "Modifier Type", 
                               default = "non", 
                               description="change modifier type")


# FUNCTIONS #

def apply_layer_settings(context):
    scene = bpy.context.scene
    selected = bpy.context.selected_objects 
    active_layer_index = context.scene.display_layers_collection_index

    for obj in context.scene.objects:
        if obj.use_display_layer:

            layer = context.scene.display_layers_collection[obj.display_layer]

   
            if layer.display:
                obj.hide = False
            else:
                obj.hide = True

            if layer.select:
                obj.hide_select = False
            else:
                obj.hide_select = True

            if layer.render:
                obj.hide_render = False
            else:
                obj.hide_render = True

            if layer.wire:
                obj.show_wire = True
                obj.show_all_edges = True
            else:
                obj.show_wire = False
                obj.show_all_edges = False



            if layer.mody:
                                                 
               enabled = obj.use_display_layer

               if enabled:    
         
                    contx = bpy.context.copy()
                    contx['object'] = obj
                   
                    for mod in obj.modifiers:
                        contx['modifier'] = mod
                        name = contx['modifier'].name

                        if scene.tp_modly_type == "all":
                                
                            if scene.tp_funcly_type == "render":                                                        
                               mod.show_render = False                         
                               
                            if scene.tp_funcly_type == "unhide":                                                        
                               mod.show_viewport = False                         

     
                        if scene.tp_modly_type == "armature":
                            if (mod.type == 'ARMATURE'):
      
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "array":
                            
                            if (mod.type == 'ARRAY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                                          
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "bevel":
                            if (mod.type == 'BEVEL'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                        
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                        
                        
                        if scene.tp_modly_type == "boolean":
                            if (mod.type == 'BOOLEAN'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "build":
                            if (mod.type == 'BUILD'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "mesh_cache":
                            if (mod.type == 'MESH_CACHE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "cast":
                            if (mod.type == 'CAST'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "cloth":
                            if (mod.type == 'CLOTH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                
                        if scene.tp_modly_type == "collision":
                            if (mod.type == 'COLLISION'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "curve":
                            if (mod.type == 'CURVE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "decimate":
                            if (mod.type == 'DECIMATE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False

                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                        

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "displace":
                            if (mod.type == 'DISPLACE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                
                        if scene.tp_modly_type == "dynamic_paint":
                            if (mod.type == 'DYNAMIC_PAINT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False                                        

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "edge_split":
                            if (mod.type == 'EDGE_SPLIT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "explode":
                            if (mod.type == 'EXPLODE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "fluid_simulation":
                            if (mod.type == 'FLUID_SIMULATION'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                                
                        if scene.tp_modly_type == "hook":
                            if (mod.type == 'HOOK'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "laplaciandeform":
                            if (mod.type == 'LAPLACIANDEFORM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "laplaciansmooth":
                            if (mod.type == 'LAPLACIANSMOOTH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass                                     


                        if scene.tp_modly_type == "lattice":
                            if (mod.type == 'LATTICE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "mask":
                            if (mod.type == 'MASK'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                        
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "mesh_deform":
                            if (mod.type == 'MESH_DEFORM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                
                        if scene.tp_modly_type == "mirror":
                            if (mod.type == 'MIRROR'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "multires":
                            if (mod.type == 'MULTIRES'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "ocean":
                            if (mod.type == 'OCEAN'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "particle_instance":
                            if (mod.type == 'PARTICLE_INSTANCE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "particle_system":
                            if (mod.type == 'PARTICLE_SYSTEM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "screw":
                            if (mod.type == 'SCREW'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                
                        if scene.tp_modly_type == "shrinkwrap":
                            if (mod.type == 'SHRINKWRAP'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "simple_deform":
                            if (mod.type == 'SIMPLE_DEFORM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                
                        if scene.tp_modly_type == "smoke":
                            if (mod.type == 'SMOKE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "smooth":
                            if (mod.type == 'SMOOTH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "soft_body":
                            if (mod.type == 'SOFT_BODY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "solidify":
                            if (mod.type == 'SOLIDIFY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False
                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "subsurf":
                            if (mod.type == 'SUBSURF'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "surface":
                            if (mod.type == 'SURFACE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "uv_project":
                            if (mod.type == 'UV_PROJECT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "warp":
                            if (mod.type == 'WARP'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "wave":
                            if (mod.type == 'WAVE'):

                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "remesh":
                            if (mod.type == 'REMESH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        passt


                        if scene.tp_modly_type == "vertex_weight_edit":
                            if (mod.type == 'VERTEX_WEIGHT_EDIT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                                
                        if scene.tp_modly_type == "vertex_weight_mix":
                            if (mod.type == 'VERTEX_WEIGHT_MIX'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "vertex_weight_proximity":
                            if (mod.type == 'VERTEX_WEIGHT_PROXIMITY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "skin":
                            if (mod.type == 'SKIN'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "triangulate":
                            if (mod.type == 'TRIANGULATE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "uv_warp":
                            if (mod.type == 'UV_WARP'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "wireframe":
                            if (mod.type == 'WIREFRAME'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == True:                         
                                        obj.modifiers[name].show_render = False
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == True:                         
                                        obj.modifiers[name].show_viewport = False

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



            else:

               enabled = obj.use_display_layer

               if enabled:    

                    contx = bpy.context.copy()
                    contx['object'] = obj

                    for mod in obj.modifiers:
                        contx['modifier'] = mod
                        name = contx['modifier'].name

                        if scene.tp_modly_type == "all":
                                
                            if scene.tp_funcly_type == "render":                                                        
                               mod.show_render = True                         
                               
                            if scene.tp_funcly_type == "unhide":                                                        
                               mod.show_viewport = True                                    
     
                            
                            # HOW TO SEPARATE THE OPERATORS? #
                            if scene.tp_funcly_type == "apply": 
                                for obj in context.scene.objects:
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = mod.name)
                                    else:
                                        pass
                           
                            if scene.tp_funcly_type == "remove":                                                                  
                                for obj in context.scene.objects:
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = mod.name)   
                                    else:
                                        pass
       


                        if scene.tp_modly_type == "armature":
                            if (mod.type == 'ARMATURE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    for obj in context.scene.objects:
                                        if obj.use_display_layer and obj.display_layer == active_layer_index:
                                            obj.select = True
                                            bpy.context.scene.objects.active = obj 
                                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = mod.name)
                                        else:
                                            pass
                               
                                if scene.tp_funcly_type == "remove":                                                                  
                                    for obj in context.scene.objects:
                                        if obj.use_display_layer and obj.display_layer == active_layer_index:
                                            obj.select = True
                                            bpy.context.scene.objects.active = obj 
                                            bpy.ops.object.modifier_remove(modifier = mod.name)   
                                        else:
                                            pass

                                if scene.tp_funcly_type == "up":   
                                    for obj in context.scene.objects:
                                        if obj.use_display_layer and obj.display_layer == active_layer_index:
                                            obj.select = True
                                            bpy.context.scene.objects.active = obj 
                                            bpy.ops.object.modifier_move_up(modifier = name)  
                                        else:
                                            pass

                                if scene.tp_funcly_type == "down":   
                                    for obj in context.scene.objects:
                                        if obj.use_display_layer and obj.display_layer == active_layer_index:
                                            obj.select = True
                                            bpy.context.scene.objects.active = obj 
                                            bpy.ops.object.modifier_move_down(modifier = name) 
                                        else:
                                            pass



                        if scene.tp_modly_type == "array":                            
                            if (mod.type == 'ARRAY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  
                              

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass
       



                        if scene.tp_modly_type == "bevel":
                            if (mod.type == 'BEVEL'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  


                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass
                                        


                        if scene.tp_modly_type == "boolean":
                            if (mod.type == 'BOOLEAN'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "build":
                            if (mod.type == 'BUILD'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "mesh_cache":
                            if (mod.type == 'MESH_CACHE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "cast":
                            if (mod.type == 'CAST'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "cloth":
                            if (mod.type == 'CLOTH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                layer_operator(context)


                                
                        if scene.tp_modly_type == "collision":
                            if (mod.type == 'COLLISION'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "curve":
                            if (mod.type == 'CURVE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "decimate":
                            if (mod.type == 'DECIMATE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  

                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                        

                        if scene.tp_modly_type == "displace":
                            if (mod.type == 'DISPLACE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                                
                        if scene.tp_modly_type == "dynamic_paint":
                            if (mod.type == 'DYNAMIC_PAINT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "edge_split":
                            if (mod.type == 'EDGE_SPLIT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "explode":
                            if (mod.type == 'EXPLODE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "fluid_simulation":
                            if (mod.type == 'FLUID_SIMULATION'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                                
                        if scene.tp_modly_type == "hook":
                            if (mod.type == 'HOOK'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "laplaciandeform":
                            if (mod.type == 'LAPLACIANDEFORM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "laplaciansmooth":
                            if (mod.type == 'LAPLACIANSMOOTH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                                                                                                         
                                        obj.modifiers[name].show_viewport = True  
                             
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        passt



                        if scene.tp_modly_type == "lattice":
                            if (mod.type == 'LATTICE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "mask":
                            if (mod.type == 'MASK'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "mesh_deform":
                            if (mod.type == 'MESH_DEFORM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                                
                        if scene.tp_modly_type == "mirror":
                            if (mod.type == 'MIRROR'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "multires":
                            if (mod.type == 'MULTIRES'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "ocean":
                            if (mod.type == 'OCEAN'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "particle_instance":
                            if (mod.type == 'PARTICLE_INSTANCE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "particle_system":
                            if (mod.type == 'PARTICLE_SYSTEM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "screw":
                            if (mod.type == 'SCREW'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass

                                
                        if scene.tp_modly_type == "shrinkwrap":
                            if (mod.type == 'SHRINKWRAP'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  
                                        
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "simple_deform":
                            if (mod.type == 'SIMPLE_DEFORM'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                                
                        if scene.tp_modly_type == "smoke":
                            if (mod.type == 'SMOKE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "smooth":
                            if (mod.type == 'SMOOTH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "soft_body":
                            if (mod.type == 'SOFT_BODY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "solidify":
                            if (mod.type == 'SOLIDIFY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "subsurf":
                            if (mod.type == 'SUBSURF'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "surface":
                            if (mod.type == 'SURFACE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  
                               
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "uv_project":
                            if (mod.type == 'UV_PROJECT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "warp":
                            if (mod.type == 'WARP'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True 
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass
                                    

                        if scene.tp_modly_type == "wave":
                            if (mod.type == 'WAVE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  
                                                                                
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "remesh":
                            if (mod.type == 'REMESH'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "vertex_weight_edit":
                            if (mod.type == 'VERTEX_WEIGHT_EDIT'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                layer_operator(context)
                                        
                                
                        if scene.tp_modly_type == "vertex_weight_mix":
                            if (mod.type == 'VERTEX_WEIGHT_MIX'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "vertex_weight_proximity":
                            if (mod.type == 'VERTEX_WEIGHT_PROXIMITY'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass



                        if scene.tp_modly_type == "skin":
                            if (mod.type == 'SKIN'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  
             
                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "triangulate":
                            if (mod.type == 'TRIANGULATE'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True   
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "uv_warp":
                            if (mod.type == 'UV_WARP'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass


                        if scene.tp_modly_type == "wireframe":
                            if (mod.type == 'WIREFRAME'):
                                
                                if scene.tp_funcly_type == "render":                                                        
                                    if mod.show_render == False:                         
                                        obj.modifiers[name].show_render = True  
                                
                                if scene.tp_funcly_type == "unhide":                                                        
                                    if mod.show_viewport == False:                         
                                        obj.modifiers[name].show_viewport = True  

                                # OPERATOR #
                                if scene.tp_funcly_type == "apply": 
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                    else:
                                        pass
                                   
                                if scene.tp_funcly_type == "remove":                                                                  
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_remove(modifier = name)   
                                    else:
                                        pass

                                if scene.tp_funcly_type == "up":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_up(modifier = name)  
                                    else:
                                        pass

                                if scene.tp_funcly_type == "down":   
                                    if obj.use_display_layer and obj.display_layer == active_layer_index:
                                        obj.select = True
                                        bpy.context.scene.objects.active = obj 
                                        bpy.ops.object.modifier_move_down(modifier = name) 
                                    else:
                                        pass








def move_layer(context, layers_collection, index, direction):

    tmp_name = layers_collection[index].name
    tmp_display = layers_collection[index].display
    tmp_select = layers_collection[index].select
    tmp_render = layers_collection[index].render
    tmp_wire = layers_collection[index].wire
    tmp_mody = layers_collection[index].mody

    layers_collection[index].name = layers_collection[index + direction].name
    layers_collection[index].display = layers_collection[index + direction].display
    layers_collection[index].select = layers_collection[index + direction].select
    layers_collection[index].render = layers_collection[index + direction].render
    layers_collection[index].wire = layers_collection[index + direction].wire
    layers_collection[index].mody = layers_collection[index + direction].mody

    layers_collection[index + direction].name = tmp_name
    layers_collection[index + direction].display = tmp_display
    layers_collection[index + direction].select = tmp_select
    layers_collection[index + direction].render = tmp_render
    layers_collection[index + direction].wire = tmp_wire
    layers_collection[index + direction].mody = tmp_mody

    context.scene.display_layers_collection_index = index + direction

    for obj in context.scene.objects:

        if obj.display_layer == index:
            obj.display_layer = index + direction

        elif obj.display_layer == index + direction:
            obj.display_layer = index






# UI LIST #
class layers_collection_UL(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        layer = item

        layout.prop(layer, "name", text="", icon_value=icon, emboss=False)

        icon_render = 'RESTRICT_VIEW_OFF' if layer.display else 'RESTRICT_VIEW_ON'
        layout.prop(item, "display", text="", icon=icon_render, emboss=False)

        icon_render = 'RESTRICT_RENDER_OFF' if layer.render else 'RESTRICT_RENDER_ON'
        layout.prop(item, "render", text="", icon=icon_render, emboss=False)

        icon_render = 'MESH_UVSPHERE' if layer.wire else 'WIRE'
        layout.prop(item, "wire", text="", icon=icon_render, emboss=False)

        icon_select = 'UNLOCKED' if layer.select else 'LOCKED'
        layout.prop(item, "select", text="", icon=icon_select, emboss=False)

        icon_mody = 'MODIFIER' if layer.mody else 'MODIFIER'
        layout.prop(item, "mody", text="", icon=icon_mody, emboss=False)



# OPERATOR: ADD LAYER#
class layers_add(bpy.types.Operator):
    bl_idname = "add_layer_from_collection.btn"
    bl_label = "Add"
    bl_description = "Add layer"

    def execute(self, context):
        my_item = context.scene.display_layers_collection.add()
        my_item.name = "Layer" + str(len(context.scene.display_layers_collection))

        context.scene.display_layers_collection_index = len(context.scene.display_layers_collection) - 1

        return{'FINISHED'}



# OPERATOR: REMOVE LAYER #
class layers_remove(bpy.types.Operator):
    bl_idname = "remove_layer_from_collection.btn"
    bl_label = "Remove"
    bl_description = "Remove layer"

    def execute(self, context):
        index = context.scene.display_layers_collection_index
        context.scene.display_layers_collection.remove(index)

        # change all index of object higher than removed index
        for obj in context.scene.objects:
            if obj.display_layer > index:
                obj.display_layer = obj.display_layer - 1

            elif obj.display_layer == index:
                obj.use_display_layer = False

        return{'FINISHED'}



# OPERATOR: UP #
class layers_up(bpy.types.Operator):
    bl_idname = "up_layer_from_collection.btn"
    bl_label = "Up"
    bl_description = "Up layer"

    @classmethod
    def poll(cls, context):
        return context.scene.display_layers_collection_index > 0 and context.scene.display_layers_collection.items()

    def execute(self, context):

        layers_collection = context.scene.display_layers_collection
        index = context.scene.display_layers_collection_index
        direction = -1
        move_layer(context, layers_collection, index, direction)

        return{'FINISHED'}



# OPERATOR: DOWN #
class layers_down(bpy.types.Operator):
    bl_idname = "down_layer_from_collection.btn"
    bl_label = "Down"
    bl_description = "Down layer"

    @classmethod
    def poll(cls, context):
        return len(bpy.context.scene.display_layers_collection) > context.scene.display_layers_collection_index + 1

    def execute(self, context):

        layers_collection = context.scene.display_layers_collection
        index = context.scene.display_layers_collection_index
        direction = 1
        move_layer(context, layers_collection, index, direction)

        return{'FINISHED'}



# OPERATOR: ASSIGN TO LAYER #
class layers_assignSelectedObjects(bpy.types.Operator):
    bl_idname = "assign_layer.btn"
    bl_label = "Assign"
    bl_description = "Assign layer to selected objects"

    @classmethod
    def poll(cls, context):
        return context.object and context.scene.display_layers_collection.items()

    def execute(self, context):
        selected_objects = context.selected_objects
        active_object = context.active_object
        active_layer_index = context.scene.display_layers_collection_index

        for obj in selected_objects:
            obj.display_layer = active_layer_index
            obj.use_display_layer = True

        apply_layer_settings(context)       

        return{'FINISHED'}



# OPERATOR: REMOVE FROM LAYER #
class layers_removeSelectedObjects(bpy.types.Operator):
    bl_idname = "remove_layer.btn"
    bl_label = "Remove"
    bl_description = "Remove selected objects from layer"

    @classmethod
    def poll(cls, context):
        return context.object and context.scene.display_layers_collection.items()

    def execute(self, context):
        selected_objects = context.selected_objects
        active_object = context.active_object
        active_layer_index = context.scene.display_layers_collection_index

        for obj in selected_objects:
            obj.use_display_layer = False

        apply_layer_settings(context)

        return{'FINISHED'}



# OPERATOR: DELETE ALL LAYERS #
class layers_select_objects(bpy.types.Operator):
    bl_idname = "clear_display_layers_collection.btn"
    bl_label = "Clear"
    bl_description = "Clear layers"

    @classmethod
    def poll(cls, context):
        return context.object and context.scene.display_layers_collection.items()

    def execute(self, context):
        context.scene.display_layers_collection.clear()
        return{'FINISHED'}





# REGISTER #
def register():
    bpy.utils.register_module(__name__)
    
# UNREGISTER #
def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()






