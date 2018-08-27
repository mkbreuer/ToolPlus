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
from bpy import*
from bpy.props import *

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

def execute_modifier():
    scene = bpy.context.scene
    selected = bpy.context.selected_objects 

    oldmode = bpy.context.mode

    for obj in selected:
                       
        contx = bpy.context.copy()
        contx['object'] = obj                     

    
        for mod in obj.modifiers: 
            contx['modifier'] = mod
            name = contx['modifier'].name
    
            if scene.tp_mods_type == "armature":
                if (mod.type == 'ARMATURE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "array":
                
                if (mod.type == 'ARRAY'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True
                  
                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                                            
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "bevel":
                if (mod.type == 'BEVEL'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)
                            


            if scene.tp_mods_type == "boolean":
                if (mod.type == 'BOOLEAN'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                                       
                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "build":
                if (mod.type == 'BUILD'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "mesh_cache":
                if (mod.type == 'MESH_CACHE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "cast":
                if (mod.type == 'CAST'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "cloth":
                if (mod.type == 'CLOTH'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)

                    
            if scene.tp_mods_type == "collision":
                if (mod.type == 'COLLISION'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "curve":
                if (mod.type == 'CURVE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "decimate":
                if (mod.type == 'DECIMATE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)
                            

            if scene.tp_mods_type == "displace":
                if (mod.type == 'DISPLACE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


                    
            if scene.tp_mods_type == "dynamic_paint":
                if (mod.type == 'DYNAMIC_PAINT'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "edge_split":
                if (mod.type == 'EDGE_SPLIT'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "explode":
                if (mod.type == 'EXPLODE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)



            if scene.tp_mods_type == "fluid_simulation":
                if (mod.type == 'FLUID_SIMULATION'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


                    
            if scene.tp_mods_type == "hook":
                if (mod.type == 'HOOK'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)



            if scene.tp_mods_type == "laplaciandeform":
                if (mod.type == 'LAPLACIANDEFORM'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)



            if scene.tp_mods_type == "laplaciansmooth":
                if (mod.type == 'LAPLACIANSMOOTH'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "lattice":
                if (mod.type == 'LATTICE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)
                    
                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "mask":
                if (mod.type == 'MASK'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)



            if scene.tp_mods_type == "mesh_deform":
                if (mod.type == 'MESH_DEFORM'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


                    
            if scene.tp_mods_type == "mirror":
                if (mod.type == 'MIRROR'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "multires":
                if (mod.type == 'MULTIRES'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "ocean":
                if (mod.type == 'OCEAN'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "particle_instance":
                if (mod.type == 'PARTICLE_INSTANCE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "particle_system":
                if (mod.type == 'PARTICLE_SYSTEM'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "screw":
                if (mod.type == 'SCREW'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    
            if scene.tp_mods_type == "shrinkwrap":
                if (mod.type == 'SHRINKWRAP'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "simple_deform":
                if (mod.type == 'SIMPLE_DEFORM'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)


                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)

                    
            if scene.tp_mods_type == "smoke":
                if (mod.type == 'SMOKE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "smooth":
                if (mod.type == 'SMOOTH'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "soft_body":
                if (mod.type == 'SOFT_BODY'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "solidify":
                if (mod.type == 'SOLIDIFY'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)                        


            if scene.tp_mods_type == "subsurf":
                if (mod.type == 'SUBSURF'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)



            if scene.tp_mods_type == "surface":
                if (mod.type == 'SURFACE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "uv_project":
                if (mod.type == 'UV_PROJECT'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "warp":
                if (mod.type == 'WARP'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "wave":
                if (mod.type == 'WAVE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)
                                                    


            if scene.tp_mods_type == "remesh":
                if (mod.type == 'REMESH'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "vertex_weight_edit":
                if (mod.type == 'VERTEX_WEIGHT_EDIT'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)  
  
                    
            if scene.tp_mods_type == "vertex_weight_mix":
                if (mod.type == 'VERTEX_WEIGHT_MIX'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "vertex_weight_proximity":
                if (mod.type == 'VERTEX_WEIGHT_PROXIMITY'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                            
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "skin":
                if (mod.type == 'SKIN'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True
 
                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "triangulate":
                if (mod.type == 'TRIANGULATE'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)                                                                                                                        


            if scene.tp_mods_type == "uv_warp":
                if (mod.type == 'UV_WARP'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)


            if scene.tp_mods_type == "wireframe":
                if (mod.type == 'WIREFRAME'):
                    
                    if scene.tp_func_type == "render":                                                        
                        if mod.show_render == True:                         
                            obj.modifiers[name].show_render = False
                        else:
                            obj.modifiers[name].show_render = True   
                    
                    if scene.tp_func_type == "unhide":                                                        
                        if mod.show_viewport == True:                         
                            obj.modifiers[name].show_viewport = False
                        else:
                            obj.modifiers[name].show_viewport = True

                    if scene.tp_func_type == "apply": 
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                   
                    if scene.tp_func_type == "remove":   
                        obj.modifiers.remove(mod)

                    if scene.tp_func_type == "up":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_up(modifier = name)

                    if scene.tp_func_type == "down":   
                        for obj in selected: 
                            bpy.context.scene .objects.active = obj 
                            bpy.ops.object.modifier_move_down(modifier = name)




class VIEW3D_TP_Modifier_by_Type(bpy.types.Operator):
    """copy, apply & remove modifier by type"""
    bl_idname = "tp_ops.mods_by_type"
    bl_label = "Modifier by Type"
    bl_options = {'REGISTER', 'UNDO'}

    bpy.types.Scene.tp_func_type = bpy.props.EnumProperty(                            
                          items = [("apply",   "Apply",     "",    "FILE_TICK",             1),                                 
                                   ("remove",  "Remove",    "",    "X",                     2), 
                                   ("render",  "Render",    "",    "RESTRICT_RENDER_OFF",   3), 
                                   ("unhide",  "UnHide",    "",    "RESTRICT_VIEW_OFF",     4), 
                                   ("down",    "Down",      "",    "TRIA_DOWN",             5),
                                   ("up",      "UP",        "",    "TRIA_UP",               6)], 
 
                                   name = "Modifier Function Type", 
                                   default = "apply", 
                                   description="modifier function type")


    bpy.types.Scene.tp_mods_type = bpy.props.EnumProperty(                            
                          items = [("wireframe",                "Wireframe",                "", "MOD_WIREFRAME",      1),                             
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
                                   description="change modifier type")



    # EXECUTE MAIN OPERATOR #
    def execute(self, context):
  
        if context.mode in EDIT:
            bpy.ops.object.editmode_toggle()  
            
            execute_modifier()             
            
            bpy.ops.object.editmode_toggle()   

        else:                   
            oldmode = bpy.context.mode                     
            bpy.ops.object.mode_set(mode='OBJECT')  
           
            execute_modifier()               
          
            bpy.ops.object.mode_set(mode=oldmode)     




        return {'FINISHED'}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()