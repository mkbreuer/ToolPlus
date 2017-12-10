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
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *   
from bpy.types import WindowManager

 

class VIEW3D_TP_FAKE_OPS(bpy.types.Operator):
    """do nothing"""
    bl_idname = "tp_ops.fake_ops"
    bl_label = "Do Nothing"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print
        return {'FINISHED'}
       

class VIEW3D_TP_OBJECT_OT_hide_select_clear(bpy.types.Operator):
    """Unlocks all visible objects"""
    bl_idname = "object.hide_select_clear"
    bl_label = "Clear All Restrict Select"

    def execute(self, context):
        scn = context.scene
        active_layers = [i for i, l in enumerate(scn.layers) if l]
        for obj in scn.objects:
            for i in active_layers:
                if obj.layers[i] and not obj.hide and obj.hide_select:
                    #unlock them
                    obj.hide_select = False
        
        return {'FINISHED'}



# SELECTION #
def get_AllObjectsInSelection():   
    return bpy.context.selected_objects

def get_hideSelectObjects(object_list):
    for i in object_list:
        i.hide_select = True
    bpy.ops.object.select_all(action='DESELECT')
    return True 

class VIEW3D_TP_Freeze_Selection(bpy.types.Operator):
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

class VIEW3D_TP_Unfreeze_Selection(bpy.types.Operator):
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



# RENDER #
def get_AllObjectsInRender():   
    return bpy.context.selected_objects

def get_hideRenderObjects(object_list):
    for i in object_list:
        i.hide_render = True
    bpy.ops.object.select_all(action='DESELECT')
    return True 

class VIEW3D_TP_Freeze_Render(bpy.types.Operator):
    bl_idname = "tp_ops.freeze_render"
    bl_label = "Freeze Render"
    bl_description = "Disables Render"
   
    def execute(self, context):
        selection = get_AllObjectsInRender()
        n = len(selection)
        if n > 0:
            get_hideRenderObjects(selection)
            self.report({'INFO'}, "%d Object%s frozen." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        return{'FINISHED'} 


def get_AllObjectsInScene():   
    return bpy.data.objects

def get_dehideRenderObjects(object_list):
    hidedObjs = []
    for i in object_list:
        if i.hide_render == True:
            i.hide_render = False
            hidedObjs.append(i)
    return hidedObjs

def get_highlightObjects(selection_list):
    
   for i in selection_list:
        bpy.data.objects[i.name].select = True         

class VIEW3D_TP_Unfreeze_Render(bpy.types.Operator):
    bl_idname = "tp_ops.unfreeze_render"
    bl_label = "Unfreeze All Render"
    bl_description = "Enables Render"
   
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        selection = get_dehideRenderObjects()
        n = len(selection)

        if n > 0:
            freezed_array = get_dehideRenderObjects(selection)
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
