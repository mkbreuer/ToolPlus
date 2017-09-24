# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


class VIEW3D_TP_Visual_GRP_Purge(bpy.types.Operator):
    """purge grease pencil layer"""
    bl_idname = "tp_ops.grp_purge"
    bl_label = "Purge"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):        
        bpy.ops.gpencil.data_unlink()
        bpy.context.scene.mod_list = 'grease_pencil'
        bpy.ops.ba.delete_data_obs()

        return {'FINISHED'}


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
        bpy.ops.object.join()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        return {'FINISHED'}



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()



