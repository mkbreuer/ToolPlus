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



# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



from os.path import dirname
from . import re_keymap

class View3D_TP_KeyMap(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_recoplanar"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = re_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}
    
    
    
class VIEW3D_TP_UnLock_All(bpy.types.Operator):
    """lock and unloak all selected objects"""
    bl_idname = "tp_ops.lock_all"
    bl_label = "(Un)Lock"
    bl_options = {"REGISTER", 'UNDO'}   

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    # allows two buttons in the panel
    lock_mode = bpy.props.StringProperty(default="")

    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
 
        if "lock" in self.lock_mode:                 
            for obj in selected:
                # make each selected active  
                bpy.context.scene.objects.active = obj  
                                           
                # lock all transform
                bpy.context.object.lock_location[0] = True
                bpy.context.object.lock_location[1] = True
                bpy.context.object.lock_location[2] = True
                bpy.context.object.lock_rotation[0] = True
                bpy.context.object.lock_rotation[1] = True
                bpy.context.object.lock_rotation[2] = True
                bpy.context.object.lock_scale[0] = True
                bpy.context.object.lock_scale[1] = True
                bpy.context.object.lock_scale[2] = True


        if "unlock" in self.lock_mode:
            for obj in selected:
                # make each selected active 
                bpy.context.scene.objects.active = obj     
                
                # unlock all transform
                bpy.context.object.lock_location[0] = False
                bpy.context.object.lock_location[1] = False
                bpy.context.object.lock_location[2] = False
                bpy.context.object.lock_rotation[0] = False
                bpy.context.object.lock_rotation[1] = False
                bpy.context.object.lock_rotation[2] = False
                bpy.context.object.lock_scale[0] = False
                bpy.context.object.lock_scale[1] = False
                bpy.context.object.lock_scale[2] = False
                  
        return {'FINISHED'}






class View3D_TP_Purge_Mesh(bpy.types.Operator):
    '''Purge all orphaned meshdata'''
    bl_idname="tp_ops.purge_mesh_data"
    bl_label="Purge MeshData"
    bl_options = {"REGISTER", 'UNDO'}    

    def execute(self, context):

        target_coll = eval("bpy.data.meshes")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}
 


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()



