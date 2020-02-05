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
import bpy, os
from bpy import*
from bpy.props import *
#from .ui_utils import get_addon_prefs
#from .ui_utils import get_addon_props

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  
  
# How to ignore naming index in modifiers? 
# https://blender.stackexchange.com/questions/165032/how-to-ignore-naming-index-in-modifiers
def func_processing_custom(self, global_prefs):
    view_layer = bpy.context.view_layer
    selected = bpy.context.selected_objects 

    for obj in selected:
        view_layer.objects.active = obj
        
        prefix = global_prefs.mod_string                       
        for key, modifier in obj.modifiers.items():
            if key.startswith(prefix):
                          
                if global_prefs.mod_list_lock == True:
                    
                    if (modifier.type == global_prefs.mod_list):
                    
                        if global_prefs.mod_processing == "RENDER":                                                        
                            if modifier.show_render == True:                         
                                modifier.show_render = False
                            else:
                                modifier.show_render = True   
                        
                        if global_prefs.mod_processing == "UNHIDE":                                                        
                            if modifier.show_viewport == True:                         
                                modifier.show_viewport = False
                            else:
                                modifier.show_viewport = True

                        if global_prefs.mod_processing == "EDIT":                                                        
                            if modifier.show_in_editmode == True:                         
                                modifier.show_in_editmode = False
                            else:
                                modifier.show_in_editmode = True

                        if global_prefs.mod_processing == "CAGE":                                                        
                            if modifier.show_on_cage == True:                         
                                modifier.show_on_cage = False
                            else:
                                modifier.show_on_cage = True

                        if global_prefs.mod_processing == "STACK":  
                            if modifier.show_expanded == True:
                                modifier.show_expanded = False                                            
                            else:
                                modifier.show_expanded = True
                   
                        name = modifier.name
      
                        if global_prefs.mod_processing == "UP":   
                            bpy.ops.object.modifier_move_up(modifier=name)

                        if global_prefs.mod_processing == "DOWN":   
                            bpy.ops.object.modifier_move_down(modifier=name)

                        if global_prefs.mod_processing == "APPLY": 
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier=name)
                       
                        if global_prefs.mod_processing == "REMOVE":   
                            bpy.ops.object.modifier_remove(modifier=name)  
                                               
                        print(self)
                        self.report({'INFO'}, "Modifier adjusted!")  

                
                else:
                    
                    if global_prefs.mod_processing == "RENDER":                                                        
                        if modifier.show_render == True:                         
                            modifier.show_render = False
                        else:
                            modifier.show_render = True   
                    
                    if global_prefs.mod_processing == "UNHIDE":                                                        
                        if modifier.show_viewport == True:                         
                            modifier.show_viewport = False
                        else:
                            modifier.show_viewport = True

                    if global_prefs.mod_processing == "EDIT":                                                        
                        if modifier.show_in_editmode == True:                         
                            modifier.show_in_editmode = False
                        else:
                            modifier.show_in_editmode = True

                    if global_prefs.mod_processing == "CAGE":                                                        
                        if modifier.show_on_cage == True:                         
                            modifier.show_on_cage = False
                        else:
                            modifier.show_on_cage = True

                    if global_prefs.mod_processing == "STACK":  
                        if modifier.show_expanded == True:
                            modifier.show_expanded = False                                            
                        else:
                            modifier.show_expanded = True


                    name = modifier.name
  
                    if global_prefs.mod_processing == "UP":   
                        bpy.ops.object.modifier_move_up(modifier=name)

                    if global_prefs.mod_processing == "DOWN":   
                        bpy.ops.object.modifier_move_down(modifier=name)

                    if global_prefs.mod_processing == "APPLY": 
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=name)
                   
                    if global_prefs.mod_processing == "REMOVE":   
                        bpy.ops.object.modifier_remove(modifier=name)  
                                           
                    print(self)
                    self.report({'INFO'}, "Modifier adjusted!")  
  


 
def func_processing(self, global_prefs):
    view_layer = bpy.context.view_layer
    selected = bpy.context.selected_objects 

    for obj in selected:      
        view_layer.objects.active = obj

        mod_type = global_prefs.mod_list                       
        for modifier in obj.modifiers.values():
            if modifier.type == mod_type: 

                if (modifier.type == global_prefs.mod_list) or global_prefs.mod_list in global_prefs.mod_mode:

                    if global_prefs.mod_processing == "RENDER":                                                        
                        if modifier.show_render == True:                         
                            modifier.show_render = False
                        else:
                            modifier.show_render = True   
                    
                    if global_prefs.mod_processing == "UNHIDE":                                                        
                        if modifier.show_viewport == True:                         
                            modifier.show_viewport = False
                        else:
                            modifier.show_viewport = True

                    if global_prefs.mod_processing == "EDIT":                                                        
                        if modifier.show_in_editmode == True:                         
                            modifier.show_in_editmode = False
                        else:
                            modifier.show_in_editmode = True

                    if global_prefs.mod_processing == "CAGE":                                                        
                        if modifier.show_on_cage == True:                         
                            modifier.show_on_cage = False
                        else:
                            modifier.show_on_cage = True

                    if global_prefs.mod_processing == "STACK":  
                        if modifier.show_expanded == True:
                            modifier.show_expanded = False                                            
                        else:
                            modifier.show_expanded = True
                                                
                    if global_prefs.mod_processing == "REMOVE":   
                        obj.modifiers.remove(modifier)   

                    print(self)
                    self.report({'INFO'}, " Modifier adjusted!")  

   
    obj_list = [obj for obj in selected]
    for obj in obj_list:
        obj.select_set(state=True)                   
        view_layer.objects.active = obj     

        context = bpy.context.copy()
        context['object'] = obj    
        
        for mod in obj.modifiers: 
            context['modifier'] = mod
            name = context['modifier'].name   

            if (mod.type == global_prefs.mod_list):

                if global_prefs.mod_processing == "UP":   
                    bpy.ops.object.modifier_move_up(modifier=name)

                if global_prefs.mod_processing == "DOWN":   
                    bpy.ops.object.modifier_move_down(modifier=name)

                if global_prefs.mod_processing == "APPLY": 
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=name)
               
              


class VIEW3D_OT_modifier_by_type(bpy.types.Operator):
    """> adjust modifier by type or as group"""
    bl_idname = "tpc_ot.modifier_by_type"
    bl_label = "Modifier Processing"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        
        global_prefs = get_addon_props()  

        box = layout.box().column(align=False)             
      
        box.separator()
      
        row = box.row(align=True)        
        row.label(text="Custom:")   
        row.prop(global_prefs, "mod_string", text="")
            
        if global_prefs.mod_string !='':  
            row.operator("tpc_ot.clear_string", text="", icon='X')  
            
        box.separator()
     
        row = box.row(align=True)        
        row.label(text="Modifier:") 
        row.prop(global_prefs, "mod_list", text="")

        if global_prefs.mod_string !='':
            if global_prefs.mod_list_lock == True:
                ico='LOCKED'
            else:
                ico='UNLOCKED'                                      
            row.prop(global_prefs, "mod_list_lock", text="", icon=ico)   

        box.separator()

        row = box.row(align=True)
        row.label(text="Process:")   
        row.prop(global_prefs, "mod_processing", text="")
        
        box.separator()


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        #addon_prefs = get_addon_prefs()
        global_prefs = get_addon_props()  
        
        view_layer = bpy.context.view_layer  
        selected = bpy.context.selected_objects 

        # store active # 
        target = view_layer.objects.active    

        if global_prefs.mod_processing == "ADD" and global_prefs.mod_list != "NONE":
            func_processing_add(self, global_prefs) 

        else:        
            if bpy.context.mode in EDIT:
                bpy.ops.object.editmode_toggle()              

                if global_prefs.mod_string != '':
                    func_processing_custom(self, global_prefs)                                  
                else:
                    func_processing(self, global_prefs) 
                               
                bpy.ops.object.editmode_toggle()   

            else:                   
                oldmode = bpy.context.mode                     
                bpy.ops.object.mode_set(mode='OBJECT')  
                           
                if global_prefs.mod_string != '':
                    func_processing_custom(self, global_prefs)                                  
                else:
                    func_processing(self, global_prefs) 
                             
                bpy.ops.object.mode_set(mode=oldmode)     

        # reload active #     
        view_layer.objects.active = target
        return {'FINISHED'}


class VIEW3D_OT_execute_direct(bpy.types.Operator):
    bl_idname = "tpc_ot.execute_direct"
    bl_label = "Execute (Run)"
    bl_options = {'REGISTER', 'UNDO'}

    mode : StringProperty(name="", description="", default="", options={'SKIP_SAVE','HIDDEN'})

    def execute(self, context):  

        if "RENDER" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "RENDER"
            bpy.ops.tpc.OT_modifier_by_type()

        if "UNHIDE" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "UNHIDE"
            bpy.ops.tpc.OT_modifier_by_type()
        
        if "EDIT" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "EDIT"
            bpy.ops.tpc.OT_modifier_by_type()
       
        if "CAGE" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "CAGE"
            bpy.ops.tpc.OT_modifier_by_type()

        if "STACK" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "STACK"
            bpy.ops.tpc.OT_modifier_by_type()
 
        if "REMOVE" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "REMOVE"
            bpy.ops.tpc.OT_modifier_by_type()

        if "UP" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "UP"
            bpy.ops.tpc.OT_modifier_by_type()

        if "DOWN" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "DOWN"
            bpy.ops.tpc.OT_modifier_by_type()

        if "APPLY" in self.mode:
            bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = "APPLY"
            bpy.ops.tpc.OT_modifier_by_type()
        
        message = "Adjust: %s" % (self.mode)
        self.report({'INFO'}, message)
        print(message)
        return {'FINISHED'}


class VIEW3D_OT_clear_string(bpy.types.Operator):
    bl_idname = "tpc_ot.clear_string"
    bl_label = "Clear String"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):  
        bpy.data.window_managers["WinMan"].global_props_modbytype.mod_string = ""
        print(self)
        self.report({'INFO'}, "String removed!") 

        return {'FINISHED'}


class VIEW3D_OT_reset_all(bpy.types.Operator):
    bl_idname = "tpc_ot.reset_all"
    bl_label = "Reset all"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.window_managers["WinMan"].global_props_modbytype.mod_string = ""  
        bpy.data.window_managers["WinMan"].global_props_modbytype.mod_list = 'NONE'
        bpy.data.window_managers["WinMan"].global_props_modbytype.mod_processing = 'NONE'

        print(self)
        self.report({'INFO'}, "Reset all!") 
        return {'FINISHED'}


# Submenus
# https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout.operator_menu_enum
# https://docs.blender.org/api/current/bpy.props.html#bpy.props.EnumProperty
# https://blenderartists.org/t/best-way-to-have-icons-in-an-enumproperty/564437/17?u=mkbreuer
class VIEW3D_OT_modifier_add_mbt(bpy.types.Operator):
    bl_idname = "tpc_ot.modifier_add"
    bl_label = "Modifier to Selected"
    bl_options = {'REGISTER', 'UNDO'}
     
    mod_list : EnumProperty(                         
      items = [
               ("DATA_TRANSFER",            "Data Transfer",            "", "MOD_DATA_TRANSFER",  101),       
               ("MESH_CACHE",               "Mesh Cache",               "", "MOD_MESHDEFORM",     102),                                   
               ("MESH_SEQUENCE_CACHE",      "Mesh Sequence Cache",      "", "MOD_MESHDEFORM",     103),                                            
               ("NORMAL_EDIT",              "Normal Edit",              "", "MOD_UVPROJECT",      104),               
               ("WEIGHTED_NORMAL",          "Weighted Normal",          "", "MOD_UVPROJECT",      105),               
               ("UV_PROJECT",               "UV Project",               "", "MOD_UVPROJECT",      106),               
               ("UV_WARP",                  "UV Warp",                  "", "MOD_UVPROJECT",      107),                                                                      
               ("VERTEX_WEIGHT_EDIT",       "Vertex Weight Edit",       "", "MOD_VERTEX_WEIGHT",  108),
               ("VERTEX_WEIGHT_MIX",        "Vertex Weight Mix",        "", "MOD_VERTEX_WEIGHT",  109),          
               ("VERTEX_WEIGHT_PROXIMITY",  "Vertex Weight Proximity",  "", "MOD_VERTEX_WEIGHT",  110),      
      
               ("WIREFRAME",                "Wireframe",                "", "MOD_WIREFRAME",      201),  
               ("TRIANGULATE",              "Triangulate",              "", "MOD_TRIANGULATE",    202),                                 
               ("SUBSURF",                  "Subsurf",                  "", "MOD_SUBSURF",        203),  
               ("SOLIDIFY",                 "Solidify",                 "", "MOD_SOLIDIFY",       204),                             
               ("SKIN",                     "Skin",                     "", "MOD_SKIN",           205),                              
               ("SCREW",                    "Screw",                    "", "MOD_SCREW",          206),                               
               ("REMESH",                   "Remesh",                   "", "MOD_REMESH",         207),                                  
               ("MULTIRES",                 "Multires",                 "", "MOD_MULTIRES",       208),                                  
               ("MIRROR",                   "Mirror",                   "", "MOD_MIRROR",         209),                                                                   
               ("MASK",                     "Mask",                     "", "MOD_MASK",           210),                                  
               ("EDGE_SPLIT",               "Edge Split",               "", "MOD_EDGESPLIT",      211),                                   
               ("DECIMATE",                 "Decimate",                 "", "MOD_DECIM",          212),                                  
               ("BUILD",                    "Build",                    "", "MOD_BUILD",          213), 
               ("BOOLEAN",                  "Boolean",                  "", "MOD_BOOLEAN",        214),  
               ("BEVEL",                    "Bevel",                    "", "MOD_BEVEL",          215), 
               ("ARRAY",                    "Array",                    "", "MOD_ARRAY",          216),                                   
             
               ("WAVE",                     "Wave",                     "", "MOD_WAVE",           301),                                   
               ("WARP",                     "Warp",                     "", "MOD_WARP",           302),                                   
               ("SURFACE_DEFORM",           "Smooth Deform",            "", "MOD_SMOOTH",         303),
               ("LAPLACIANSMOOTH",          "Smooth Laplacian",         "", "MOD_SMOOTH",         304),
               ("CORRECTIVE_SMOOTH",        "Smooth Corrective",        "", "MOD_SMOOTH",         305),
               ("SMOOTH",                   "Smooth",                   "", "MOD_SMOOTH",         306),                                   
               ("SIMPLE_DEFORM",            "Simple Deform",            "", "MOD_SIMPLEDEFORM",   307),                                   
               ("SHRINKWRAP",               "Shrinkwrap",               "", "MOD_SHRINKWRAP",     308),                                   
               ("MESH_DEFORM",              "Mesh Deform",              "", "MOD_MESHDEFORM",     309),                                   
               ("LATTICE",                  "Lattice",                  "", "MOD_LATTICE",        310),
               ("LAPLACIANDEFORM",          "Laplacian Deform",         "", "MOD_MESHDEFORM",     311),
               ("HOOK",                     "Hook",                     "", "HOOK",               312),  
               ("DISPLACE",                 "Displace",                 "", "MOD_DISPLACE",       313),
               ("CURVE",                    "Curve",                    "", "MOD_CURVE",          314),
               ("CAST",                     "Cast",                     "", "MOD_CAST",           315),                                    
               ("ARMATURE",                 "Armature",                 "", "MOD_ARMATURE",       316),                                   
             
               ("NONE",                     "",                         "", "BLANK1",             400),
               ("SOFT_BODY",                "Soft Body",                "", "MOD_SOFT",           401),
               ("SMOKE",                    "Smoke",                    "", "MOD_SMOKE",          402),
               ("PARTICLE_SYSTEM",          "Particle System",          "", "MOD_PARTICLES",      403),
               ("PARTICLE_INSTANCE",        "Particle Instance",        "", "MOD_PARTICLES",      404),
               ("OCEAN",                    "Ocean",                    "", "MOD_OCEAN",          405),
               ("FLUID_SIMULATION",         "Fluid Simulation",         "", "MOD_FLUIDSIM",       406),
               ("EXPLODE",                  "Explode",                  "", "MOD_EXPLODE",        407),
               ("DYNAMIC_PAINT",            "Dynamic Paint",            "", "MOD_DYNAMICPAINT",   408),
               ("COLLISION",                "Collision",                "", "MOD_PHYSICS",        409),
               ("CLOTH",                    "Cloth",                    "", "MOD_CLOTH",          410)], 
            
              #(identifier,                 name,              description, icon,                 number)   
             
               name = "Modifier Type", 
               default = "NONE", 
               description="change modifier type",
               options={'SKIP_SAVE'}) 


    def draw(self, context):
        layout = self.layout

        box = layout.box().column(align=False)                   
        box.separator()
      
        row = box.row(align=True)        
        row.label(text="Add Modifier:")   
        row.prop(self, "mod_list", text="")
                
        box.separator()

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):
        message = "Added: %s" % (self.mod_list)
        self.report({'INFO'}, message)
        print(message)

        view_layer = bpy.context.view_layer
        selected = bpy.context.selected_objects 
                                   
        for obj in selected:
            view_layer.objects.active = obj       
           
            mod_type = bpy.context.object.modifiers.get(self.mod_list)   
            if not mod_type :   
                bpy.ops.object.modifier_add(type=self.mod_list)

        return {'FINISHED'}


# https://blenderartists.org/t/how-to-rebuild-the-add-modifier-menu-layout/1204906/2
# Categories start on these modifiers
mods = ('DATA_TRANSFER', 'ARRAY', 'ARMATURE', 'CLOTH')

# Rna enum items are listed in same order as menu.
op = bpy.ops.object.modifier_add
enum_rna = op.get_rna_type().properties['type'].enum_items
mdict = {"Modify": [], "Generate": [], "Deform": [], "Simulate": []}

for item, cat in zip(mods, mdict):
    for mod in enum_rna[enum_rna.find(item):]:
        mod_id = mod.identifier
        # Delimit at next item in mods
        if mod_id != item and mod_id in mods[mods.index(item):]:
            break
        mdict[cat].append((mod_id, mod.name, mod.icon))

# There's an invalid entry called Surface at the end of "Simulate" category. 
# It's a duplicate of Simple Deform so we remove it.
if mdict["Simulate"] and mdict["Simulate"][-1][0] == "SURFACE":
    del mdict["Simulate"][-1]

class VIEW3D_MT_add_modifier_mbt(bpy.types.Menu):
    bl_label = ""
    def draw(self, context):
        layout = self.layout
        split = layout.split()
        for cat, mods in mdict.items():
            col = split.column()
            col.label(text=cat)
            for idx, name, icon in mods:
                col.operator("tpc_ot.modifier_add", text=name, icon=icon).mod_list = idx

# REGISTER #
classes = (
    VIEW3D_MT_add_modifier_mbt,
    VIEW3D_OT_modifier_add_mbt,
    VIEW3D_OT_execute_direct,
    VIEW3D_OT_modifier_by_type,
    VIEW3D_OT_clear_string,
    VIEW3D_OT_reset_all,
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
  
    #bpy.ops.wm.call_menu(name="VIEW3D_MT_tpc_add_modifier")


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
