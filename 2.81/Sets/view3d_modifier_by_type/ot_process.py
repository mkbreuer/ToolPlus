# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2020 MKB
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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
#


# LOAD MODUL #    
import bpy
from bpy import*
from bpy.props import *

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  


def get_addon_props():
    addon_global_props = bpy.context.window_manager.global_props_modbytype
    return (addon_global_props)
 
# process modifier
def func_processing(self, global_prefs):
    view_layer = bpy.context.view_layer
    active = view_layer.objects.active
    selected = bpy.context.selected_objects 

    global_prefs = get_addon_props()   

    for obj in selected:
        view_layer.objects.active = obj  
                                          
        if global_prefs.mod_processing == "ADD":
            if global_prefs.mod_list == "NONE":
                pass
            else:                                                                     
                mod_type = bpy.context.object.modifiers.get(global_prefs.mod_list)   
                if not mod_type :   
                    bpy.ops.object.modifier_add(type=global_prefs.mod_list)
        else:
            for obj in selected:

                if global_prefs.mod_string != '':

                    # How to ignore naming index in modifiers? 
                    # https://blender.stackexchange.com/questions/165032/how-to-ignore-naming-index-in-modifiers
                    # thx to robert gützkow for fixing this...
                    
                    prefix = global_prefs.mod_string                       
                    for key, modifier in bpy.context.object.modifiers.items():
                        # iterate through all modifiers check if its name starts with a given prefix
                        if key.startswith(prefix):
                                                      
                            if self.mod_processing == "RENDER" or global_prefs.mod_processing == "RENDER":                                                        
                                if modifier.show_render == True:                         
                                    modifier.show_render = False
                                else:
                                    modifier.show_render = True   
                            
                            if self.mod_processing == "UNHIDE" or global_prefs.mod_processing == "UNHIDE":                                                        
                                if modifier.show_viewport == True:                         
                                    modifier.show_viewport = False
                                else:
                                    modifier.show_viewport = True

                            if self.mod_processing == "EDIT" or global_prefs.mod_processing == "EDIT":                                                        
                                if modifier.show_viewport == True:                         
                                    modifier.show_in_editmode = False
                                else:
                                    modifier.show_in_editmode = True

                            if self.mod_processing == "CAGE" or global_prefs.mod_processing == "CAGE":                                                        
                                if modifier.show_viewport == True:                         
                                    modifier.show_on_cage = False
                                else:
                                    modifier.show_on_cage = True

                            if self.mod_processing == "STACK" or global_prefs.mod_processing == "STACK":  
                                if modifier.show_expanded == True:
                                    modifier.show_expanded = False                                            
                                else:
                                    modifier.show_expanded = True
                                    
                            
                            name = modifier.name
          
                            if self.mod_processing == "UP" or global_prefs.mod_processing == "UP":   
                                bpy.ops.object.modifier_move_up(modifier=name)

                            if self.mod_processing == "DOWN" or global_prefs.mod_processing == "DOWN":   
                                bpy.ops.object.modifier_move_down(modifier=name)

                            if self.mod_processing == "APPLY" or global_prefs.mod_processing == "APPLY": 
                                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=name)
                           
                            if self.mod_processing == "REMOVE" or global_prefs.mod_processing == "REMOVE":   
                                bpy.ops.object.modifier_remove(modifier=name)  
                                                      
                    else:
                        print(self)
                        self.report({'INFO'}, "Modifier not found!")  


                else:

                    context = bpy.context.copy()
                    context['object'] = obj    
                    
                    for mod in obj.modifiers: 
                        context['modifier'] = mod
                        name = context['modifier'].name            
                    
                        if (mod.type == global_prefs.mod_list) or global_prefs.mod_list in global_prefs.mod_mode or (mod.type == self.mod_list) or global_prefs.mod_list in self.mod_mode:

                            for obj in selected: 
                                view_layer.objects.active = obj 

                                if self.mod_processing == "RENDER" or global_prefs.mod_processing == "RENDER":                                                        
                                    if mod.show_render == True:                         
                                        bpy.context.object.modifiers[name].show_render = False
                                    else:
                                        bpy.context.object.modifiers[name].show_render = True   
                                
                                if self.mod_processing == "UNHIDE" or global_prefs.mod_processing == "UNHIDE":                                                        
                                    if mod.show_viewport == True:                         
                                        bpy.context.object.modifiers[name].show_viewport = False
                                    else:
                                        bpy.context.object.modifiers[name].show_viewport = True

                                if self.mod_processing == "EDIT" or global_prefs.mod_processing == "EDIT":                                                        
                                    if mod.show_viewport == True:                         
                                        bpy.context.object.modifiers[name].show_in_editmode = False
                                    else:
                                        bpy.context.object.modifiers[name].show_in_editmode = True

                                if self.mod_processing == "CAGE" or global_prefs.mod_processing == "CAGE":                                                        
                                    if mod.show_viewport == True:                         
                                        bpy.context.object.modifiers[name].show_on_cage = False
                                    else:
                                        bpy.context.object.modifiers[name].show_on_cage = True

                                if self.mod_processing == "UP" or global_prefs.mod_processing == "UP":   
                                    bpy.ops.object.modifier_move_up(modifier = name)

                                if self.mod_processing == "DOWN" or global_prefs.mod_processing == "DOWN":   
                                    bpy.ops.object.modifier_move_down(modifier = name)

                                if self.mod_processing == "APPLY" or global_prefs.mod_processing == "APPLY": 
                                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier = name)
                               
                                if self.mod_processing == "REMOVE" or global_prefs.mod_processing == "REMOVE":   
                                    bpy.ops.object.modifier_remove(modifier=name)  
                               
                                if self.mod_processing == "STACK" or global_prefs.mod_processing == "STACK":  
                                    if mod.show_expanded == True:
                                        bpy.context.object.modifiers[name].show_expanded = False                                            
                                    else:
                                        bpy.context.object.modifiers[name].show_expanded = True




class VIEW3D_OT_modifier_by_type(bpy.types.Operator):
    """copy, apply & remove modifier by type"""
    bl_idname = "tpc_ot.modifier_by_type"
    bl_label = "Modifier by Type"
    bl_options = {'REGISTER', 'UNDO'}

    mod_mode : StringProperty(default="", options={'HIDDEN'})

    mod_processing : bpy.props.EnumProperty(                            
      items = [("ADD",     "Add",       "",    "ADD",                   0),                                  
               ("RENDER",  "Render",    "",    "RESTRICT_RENDER_OFF",   1), 
               ("UNHIDE",  "(Un)Hide",  "",    "RESTRICT_VIEW_OFF",     2), 
               ("EDIT",    "Edit",      "",    "EDITMODE_HLT",          3), 
               ("CAGE",    "Cage",      "",    "MESH_DATA",             4), 
               ("DOWN",    "Down",      "",    "TRIA_DOWN",             5),
               ("UP",      "Up",        "",    "TRIA_UP",               6),  
               ("APPLY",   "Apply",     "",    "CHECKMARK",             7),                                 
               ("REMOVE",  "Remove",    "",    "X",                     8),
               ("STACK",   "Stack",     "",    "FULLSCREEN_ENTER",      9),
               ("NONE",    "None",      "",    "INFO",                  10)],
               name = "Process All", 
               default = "NONE", 
               description="change modifier processing type")


    mod_list : EnumProperty(                            
      items = [("WIREFRAME",                "Wireframe",                "", "MOD_WIREFRAME",      1),                             
               ("TRIANGULATE",              "Triangulate",              "", "MOD_TRIANGULATE",    2),                                 
               ("SUBSURF",                  "Subsurf",                  "", "MOD_SUBSURF",        3),                            
               ("SOLIDIFY",                 "Solidify",                 "", "MOD_SOLIDIFY",       4),                             
               ("SKIN",                     "Skin",                     "", "MOD_SKIN",           5),                              
               ("SCREW",                    "Screw",                    "", "MOD_SCREW",          6),                               
               ("REMESH",                   "Remesh",                   "", "MOD_REMESH",         7),                                  
               ("MULTIRES",                 "Multires",                 "", "MOD_MULTIRES",       8),                                  
               ("MIRROR",                   "Mirror",                   "", "MOD_MIRROR",         9),                                                                   
               ("MASK",                     "Mask",                     "", "MOD_MASK",          10),                                  
               ("EDGE_SPLIT",               "Edge Split",               "", "MOD_EDGESPLIT",     11),                                   
               ("DECIMATE",                 "Decimate",                 "", "MOD_DECIM",         12),                                  
               ("BUILD",                    "Build",                    "", "MOD_BUILD",         13), 
               ("BOOLEAN",                  "Boolean",                  "", "MOD_BOOLEAN",       14),  
               ("BEVEL",                    "Bevel",                    "", "MOD_BEVEL",         15), 
               ("ARRAY",                    "Array",                    "", "MOD_ARRAY",         16),                                   
             
               ("UV_WARP",                  "UV Warp",                  "", "MOD_UVPROJECT",     17),                                                                      
               ("UV_PROJECT",               "UV Project",               "", "MOD_UVPROJECT",     18),
               ("WAVE",                     "Wave",                     "", "MOD_WAVE",          19),                                   
               ("WARP",                     "Warp",                     "", "MOD_WARP",          20),                                   
               ("SMOOTH",                   "Smooth",                   "", "MOD_SMOOTH",        21),                                   
               ("SIMPLE_DEFORM",            "Simple Deform",            "", "MOD_SIMPLEDEFORM",  22),                                   
               ("SHRINKWRAP",               "Shrinkwrap",               "", "MOD_SHRINKWRAP",    23),                                   
               ("MESH_DEFORM",              "Mesh Deform",              "", "MOD_MESHDEFORM",    24),                                   
               ("LATTICE",                  "Lattice",                  "", "MOD_LATTICE",       25),
               ("LAPLACIANDEFORM",          "Laplacian Deform",         "", "MOD_MESHDEFORM",    26),
               ("LAPLACIANSMOOTH",          "Laplacian Smooth",         "", "MOD_SMOOTH",        27),
               ("HOOK",                     "Hook",                     "", "HOOK",              28),  
               ("DISPLACE",                 "Displace",                 "", "MOD_DISPLACE",      29),
               ("CURVE",                    "Curve",                    "", "MOD_CURVE",         30),
               ("CAST",                     "Cast",                     "", "MOD_CAST",          31),                                    
               ("ARMATURE",                 "Armature",                 "", "MOD_ARMATURE",      32),                                   

               ("VERTEX_WEIGHT_PROXIMITY",  "Vertex Weight Proximity",  "", "MOD_VERTEX_WEIGHT", 33),
               ("VERTEX_WEIGHT_MIX",        "Vertex Weight Mix",        "", "MOD_VERTEX_WEIGHT", 34),
               ("VERTEX_WEIGHT_EDIT",       "Vertex Weight Edit",       "", "MOD_VERTEX_WEIGHT", 35),
               ("MESH_CACHE",               "Mesh Cache",               "", "MOD_MESHDEFORM",    36),                                   
               ("SURFACE",                  "Surface",                  "", "PHYSICS",           37),                               
               ("SOFT_BODY",                "Soft Body",                "", "MOD_SOFT",          38),
               ("SMOKE",                    "Smoke",                    "", "MOD_SMOKE",         39),
               ("PARTICLE_SYSTEM",          "Particle System",          "", "MOD_PARTICLES",     40),
               ("PARTICLE_INSTANCE",        "Particle Instance",        "", "MOD_PARTICLES",     41),
               ("OCEAN",                    "Ocean",                    "", "MOD_OCEAN",         42),
               ("FLUID_SIMULATION",         "Fluid Simulation",         "", "MOD_FLUIDSIM",      43),
               ("EXPLODE",                  "Explode",                  "", "MOD_EXPLODE",       44),
               ("DYNAMIC_PAINT",            "Dynamic Paint",            "", "MOD_DYNAMICPAINT",  45),
               ("COLLISION",                "Collision",                "", "MOD_PHYSICS",       46),
               ("CLOTH",                    "Cloth",                    "", "MOD_CLOTH",         47), 
               
               ("NONE",                      "None",                    "", "INFO",              48)], 

               name = "Modifier Type", 
               default = "NONE", 
               description="change modifier type")
  
 
    def draw(self, context):
        layout = self.layout
        
        global_prefs = get_addon_props()  
       
        col = layout.column(align=True)
        box = col.box().column(align=False)             

        row = box.row(align=True)  
        row.label(text='Processing:')   
        row.prop(global_prefs, 'mod_processing', text='')

        row = box.row(align=True)   
        row.label(text='Modifier Type:')   
        row.prop(global_prefs, 'mod_list', text='')          

        row = box.row(align=True)   
        row.label(text='Modifier Name:')   
        row.prop(global_prefs, 'mod_string', text='')    

        box.separator()
   
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):
  
        global_prefs = get_addon_props()  

        if context.mode in EDIT:
            bpy.ops.object.editmode_toggle()              
            func_processing(self, global_prefs)                     
            bpy.ops.object.editmode_toggle()   

        else:                   
            oldmode = bpy.context.mode                     
            bpy.ops.object.mode_set(mode='OBJECT')             
            func_processing(self, global_prefs)               
            bpy.ops.object.mode_set(mode=oldmode)     

        return {'FINISHED'}



# REGISTER #
classes = (
    VIEW3D_OT_modifier_by_type,
    )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
