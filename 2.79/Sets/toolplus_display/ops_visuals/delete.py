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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


class VIEW3D_TP_Visual_Purge_Mesh(bpy.types.Operator):
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
 

class VIEW3D_TP_Visual_Remove_Doubles(bpy.types.Operator):
    """Removes doubles on all selected objects"""
    bl_idname = "tp_ops.remove_doubles"
    bl_label = "Remove Doubles"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):             
        for obj in bpy.context.selected_objects:
            bpy.context.scene.objects.active = obj                 
            if obj:
                obj_type = obj.type
                if obj_type in {'MESH'}:   
                    bpy.ops.object.join()
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.remove_doubles()
                    bpy.ops.mesh.separate(type='LOOSE')
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
                    print(self)
                    self.report({'INFO'}, "Done!")      
                else:
                    print(self)
                    self.report({'INFO'}, "Not possible!")      
            else:
                print(self)
                self.report({'INFO'}, "Not possible!")  
                  
        return {'FINISHED'}




class VIEW3D_TP_Dissolve_LoopsA(bpy.types.Operator):
    """Dissolve Loops / Sel. Edge = Ring > Checker Deselect > Loop > Dissolve"""
    bl_idname = "tp_ops.dissolve_loops_a"
    bl_label = "Rem.Loops+0"

    def execute(self, context):
        
        bpy.ops.mesh.loop_multi_select(ring=True)  
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.delete_edgeloop()

        return {'FINISHED'}


class VIEW3D_TP_Dissolve_LoopsB(bpy.types.Operator):
    """Dissolve Loops / Sel. Edges = Checker Deselect > Loop > Dissolve"""
    bl_idname = "tp_ops.dissolve_loops_b"
    bl_label = "Rem.Loops+1"

    def execute(self, context):
      
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.delete_edgeloop()

        return {'FINISHED'}



#    "author": "CoDEmanX,Albertofx",
from mathutils import Matrix
class VIEW3D_TP_OBJECT_OT_clear_all(bpy.types.Operator):
    """Clear Location, Rotation and Scale"""
    bl_idname = "tp_ops.clear_all"
    bl_label = "Clear All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for ob in context.selected_editable_objects:
            ob.matrix_world = Matrix.Identity(4)
        return {'FINISHED'}


#    "author": "Abel Groenewolt",
class VIEW3D_TP_DeleteFromAllScenes(bpy.types.Operator):
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


# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()



