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
from bpy import*
from bpy.props import *

 
class BooleanMeshDeformOperator(bpy.types.Operator):
    '''Binds a deforming mesh to the object'''
    bl_idname = "boolean.mesh_deform"
    bl_label = "Mesh deform"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and len(bpy.context.selected_objects)==2

    def execute(self, context):
        activeObj = context.active_object
        for SelectedObject in bpy.context.selected_objects :
            if SelectedObject != activeObj :
                md = activeObj.modifiers.new('mesh_deform', 'MESH_DEFORM')
                md.object = SelectedObject
                bpy.ops.object.meshdeform_bind(modifier="mesh_deform")
                bpy.context.scene.objects.active = SelectedObject
                SelectedObject.draw_type="WIRE"
                bpy.ops.object.mode_set(mode='EDIT')


        return {'FINISHED'}
    
    
    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()