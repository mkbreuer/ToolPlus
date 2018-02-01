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
#

# LOAD MODUL #    
import bpy


#bl_info = {
#    "name": "Delete From All Scenes",
#    "description": "This will delete an object from all scenes rather than just from the current one.",
#    "author": "Abel Groenewolt",
#    "version": (0,1),
#    "blender": (2, 5, 9),
#    "api": 40791,
#    "location": "Object Tools > Delete From All Scenes panel > Delete from all scenes",
#    "warning": "", # used for warning icon and text in addons panel
#    "category": "Object"}


## operator ##
class DeleteFromAllScenes(bpy.types.Operator):
    bl_idname = "tp_ops.delete_from_all_scenes"
    bl_label = "Delete Object From All Scenes"
    bl_options = {"UNDO"}
    
    ## actual function ## 
    def invoke(self, context, event):
        for i in range (0,len(bpy.context.selected_objects)):
            current_object = bpy.context.selected_objects[0]
            # unlink object from all scenes
            for sce in bpy.data.scenes:
                try:    sce.objects.unlink(current_object)
                except:    pass
        return {"FINISHED"}
    # end invoke
# end operator class


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()