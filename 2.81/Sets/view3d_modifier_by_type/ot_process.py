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
from .ui_utils import get_addon_prefs
from .ui_utils import get_addon_props


EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  

  
def func_processing_add(self, global_prefs):
    view_layer = bpy.context.view_layer
    selected = bpy.context.selected_objects 
                               
    for obj in selected:
        view_layer.objects.active = obj
                                                                               
        mod_type = bpy.context.object.modifiers.get(global_prefs.mod_list)   
        if not mod_type :   
            bpy.ops.object.modifier_add(type=global_prefs.mod_list)

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
                            if modifier.show_viewport == True:                         
                                modifier.show_in_editmode = False
                            else:
                                modifier.show_in_editmode = True

                        if global_prefs.mod_processing == "CAGE":                                                        
                            if modifier.show_viewport == True:                         
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
                        if modifier.show_viewport == True:                         
                            modifier.show_in_editmode = False
                        else:
                            modifier.show_in_editmode = True

                    if global_prefs.mod_processing == "CAGE":                                                        
                        if modifier.show_viewport == True:                         
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
                        if modifier.show_viewport == True:                         
                            modifier.show_in_editmode = False
                        else:
                            modifier.show_in_editmode = True

                    if global_prefs.mod_processing == "CAGE":                                                        
                        if modifier.show_viewport == True:                         
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
    """copy, apply & remove modifier by type"""
    bl_idname = "tpc_ot.modifier_by_type"
    bl_label = "Modifier by Type"
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

#        if global_prefs.mod_processing == "ADD" or global_prefs.mod_list == "NONE":
#            pass
#        else:

        if context.mode in EDIT:
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



class VIEW3D_OT_clear_string(bpy.types.Operator):
    """selection buttons for repattern lights"""
    bl_idname = "tpc_ot.clear_string"
    bl_label = "Clear string"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
  
        bpy.data.window_managers["WinMan"].global_props_modbytype.mod_string = ""
        #bpy.data.window_managers["WinMan"].global_props_modbytype.mod_string = ""
        print(self)
        self.report({'INFO'}, "String removed!") 

        return {'FINISHED'}


# REGISTER #
classes = (
    VIEW3D_OT_modifier_by_type,
    VIEW3D_OT_clear_string,
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
