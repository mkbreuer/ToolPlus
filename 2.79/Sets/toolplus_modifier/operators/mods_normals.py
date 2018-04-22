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


class VIEW3D_TP_Normals(bpy.types.Operator):
    """Recalculate Normals for all selected Objects in Objectmode"""
    bl_idname = "tp_ops.rec_normals"
    bl_label = "Recalculate Normals"     

    def execute(self, context):
        print(self)
        self.report({'INFO'}, "Recalculate Normals")   
                        
        for obj in bpy.context.selected_objects:
            
            obj = bpy.context.scene.objects.active                
           
            if obj:
                
                if obj.type in {'MESH'}:                 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent()
                    bpy.ops.object.editmode_toggle()            

      
        return {'FINISHED'}    



def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
     