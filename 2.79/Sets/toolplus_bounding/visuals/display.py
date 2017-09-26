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

#bl_info = {
#    "authors": "Jordi Vall-llovera Medina, Jhon Wallace, Meta Androcto, saidenka, MKB",

#    "name": "Display Tools",
#    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Display_Tools",

#    "name": "Modfier Tools",
#    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/modifier_tools",
#    "tracker_url": "https://developer.blender.org/maniphest/task/edit/form/2/",





import bpy
from bpy import*
from bpy.props import *


class VIEW3D_TP_Visual_Render_On_Off(bpy.types.Operator):
    '''render on / off'''
    bl_idname = "tp_ops.mods_render"
    bl_label = "Render"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        is_apply = True
        message_a = ""

        for mod in context.active_object.modifiers:
            if (mod.show_render):
                is_apply = False
                break
        for obj in context.selected_objects:
            for mod in obj.modifiers:
                mod.show_render = is_apply

        if is_apply:
            message_a = "All Render ON"
        else:
            message_a = "All Render OFF"

        self.report(type={"INFO"}, message=message_a)
                    
        return {'FINISHED'}
        
        

class VIEW3D_TP_Visual_Modifier_On_Off(bpy.types.Operator):
    '''view on / off'''
    bl_idname = "tp_ops.mods_view"
    bl_label = "View"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        is_apply = True
        message_a = ""

        for mod in context.active_object.modifiers:
            if (mod.show_viewport):
                is_apply = False
                break
        for obj in context.selected_objects:
            for mod in obj.modifiers:
                mod.show_viewport = is_apply

        if is_apply:
            message_a = "All View ON"
        else:
            message_a = "All View OFF"

        self.report(type={"INFO"}, message=message_a)

                    
        return {'FINISHED'}
    


class VIEW3D_TP_Visual_Edit_On_Off(bpy.types.Operator):
    '''edit on / off'''
    bl_idname = "tp_ops.mods_edit"
    bl_label = "Edit"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        is_apply = True
        message_a = ""

        for mod in context.active_object.modifiers:
            if (mod.show_in_editmode):
                is_apply = False
                break
        for obj in context.selected_objects:
            for mod in obj.modifiers:
                mod.show_in_editmode = is_apply

        if is_apply:
            message_a = "All Edit ON"
        else:
            message_a = "All Edit OFF"

        self.report(type={"INFO"}, message=message_a)

                    
        return {'FINISHED'}
        


class VIEW3D_TP_Visual_Cage_On_Off(bpy.types.Operator):
    '''cage  on / off'''
    bl_idname = "tp_ops.mods_cage"
    bl_label = "Cage"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        is_apply = True
        message_a = ""

        for mod in context.active_object.modifiers:
            if (mod.show_on_cage):
                is_apply = False
                break
        for obj in context.selected_objects:
            for mod in obj.modifiers:
                mod.show_on_cage = is_apply

        if is_apply:
            message_a = "All Cage ON"
        else:
            message_a = "All Cage OFF"

        self.report(type={"INFO"}, message=message_a)

                    
        return {'FINISHED'}
    
    



class VIEW3D_TP_Visual_Display_DrawWire(bpy.types.Operator):
    """Draw Type Wire"""
    bl_idname = "tp_ops.draw_wire"
    bl_label = "Draw Type Wire"

    def execute(self, context):
        bpy.context.object.draw_type = 'WIRE'       
        return {'FINISHED'}


class VIEW3D_TP_Visual_Display_DrawSolid(bpy.types.Operator):
    """Draw Type Solid"""
    bl_idname = "tp_ops.draw_solid"
    bl_label = "Draw Type Solid"

    def execute(self, context):
        bpy.context.object.draw_type = 'SOLID'       
        return {'FINISHED'}


class VIEW3D_TP_Visual_Wire_All(bpy.types.Operator):
    """Wire on all objects in the scene"""
    bl_idname = "tp_ops.wire_all"
    bl_label = "Wire on All Objects"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        
        for obj in bpy.data.objects:
            if obj.show_wire:
                obj.show_all_edges = False
                obj.show_wire = False            
            else:
                obj.show_all_edges = True
                obj.show_wire = True
                             
        return {'FINISHED'} 
    


class VIEW3D_TP_Visual_Wire_On(bpy.types.Operator):
    '''Wire on'''
    bl_idname = "tp_ops.wire_on"
    bl_label = "Wire on"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        selection = bpy.context.selected_objects  
         
        if not(selection): 
            for obj in bpy.data.objects:
                obj.show_wire = True
                obj.show_all_edges = True
                
        else:
            for obj in selection:
                obj.show_wire = True
                obj.show_all_edges = True 
        return {'FINISHED'}


class VIEW3D_TP_Visual_Wire_Off(bpy.types.Operator):
    '''Wire off'''
    bl_idname = "tp_ops.wire_off"
    bl_label = "Wire off"
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):
        selection = bpy.context.selected_objects  
        
        if not(selection): 
            for obj in bpy.data.objects:
                obj.show_wire = False
                obj.show_all_edges = False
                
        else:
            for obj in selection:
                obj.show_wire = False
                obj.show_all_edges = False   

        return {'FINISHED'}
    



# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    


