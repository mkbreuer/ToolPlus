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
    """Removes doubles on all selected objects / optional: join  & separate selected"""
    bl_idname = "tp_ops.remove_doubles"
    bl_label = "Remove Doubles"
    bl_options = {'REGISTER', 'UNDO'}

    do_join_separate = bpy.props.BoolProperty(name="Join  & Separate",  description="join  & separate selected", default=False, options={'SKIP_SAVE'})  
            
    def execute(self, context):             
        for obj in bpy.context.selected_objects:
            bpy.context.scene.objects.active = obj                 
            if obj:
                obj_type = obj.type
                if obj_type in {'MESH'}:   
                  
                    if self.do_join_separate == False:
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.mesh.remove_doubles()
                        bpy.ops.object.editmode_toggle()
                    else:
                        bpy.ops.object.join()
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.mesh.remove_doubles()
                        bpy.ops.mesh.separate(type='LOOSE')
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
                else:
                    print(self)
                    self.report({'INFO'}, "Not possible!")      

        return {'FINISHED'}



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()



