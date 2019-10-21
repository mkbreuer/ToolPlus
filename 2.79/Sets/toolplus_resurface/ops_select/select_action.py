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

import re, math
from mathutils import Vector
from math import pi


#by panecake
class VIEW3D_TP_CycleThrough(bpy.types.Operator):
    """cycle through selected objects"""
    bl_idname = "tp_ops.cycle_selected"
    bl_label = "Cycle through Selected"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        selection = bpy.context.selected_objects

        if not bpy.context.active_object.select:
            if len(selection):
                bpy.context.scene.objects.active = selection[0]
        else:
            for i, o in enumerate(selection):
                if o == bpy.context.active_object:
                    bpy.context.scene.objects.active = selection[(i+1) % len(selection)]
                    break
        
        return {'FINISHED'}


    
class VIEW3D_TP_ThroughSelected(bpy.types.Operator):
    """cycle through selected objects"""
    bl_idname = "tp_ops.through_selectd"
    bl_label = "Cycle through Selected"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        selection = bpy.context.selected_objects
                
        for i, o in enumerate(selection):
            if o == bpy.context.active_object:
                bpy.context.scene.objects.active = selection[(i+1) % len(selection)]
                bpy.ops.boolean.grease_symm()
                break                
        
        return {'FINISHED'}




def get_AllObjectsInSelection():   
    return bpy.context.selected_objects

def get_hideSelectObjects(object_list):
    for i in object_list:
        i.hide_select = True
    bpy.ops.object.select_all(action='DESELECT')
    return True 

class VIEW3D_TP_Freeze(bpy.types.Operator):
    bl_idname = "tp_ops.freeze_selected"
    bl_label = "Freeze Selection"
    bl_description = "Disables Selection"
   
    def execute(self, context):
        selection = get_AllObjectsInSelection()
        n = len(selection)
        if n > 0:
            get_hideSelectObjects(selection)
            self.report({'INFO'}, "%d Object%s frozen." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        return{'FINISHED'} 



def get_AllObjectsInScene():   
    return bpy.data.objects

def get_dehideSelectObjects(object_list):
    hidedObjs = []
    for i in object_list:
        if i.hide_select == True:
            i.hide_select = False
            hidedObjs.append(i)
    return hidedObjs

def get_highlightObjects(selection_list):
    
   for i in selection_list:
        bpy.data.objects[i.name].select = True         

class VIEW3D_TP_Unfreeze(bpy.types.Operator):
    bl_idname = "tp_ops.unfreeze_selected"
    bl_label = "Unfreeze All"
    bl_description = "Enables Selection"
   
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        selection = get_AllObjectsInScene()
        n = len(selection)

        if n > 0:
            freezed_array = get_dehideSelectObjects(selection)
            get_highlightObjects(freezed_array)
            self.report({'INFO'}, "%d Object%s released." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        
        return{'FINISHED'} 




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()