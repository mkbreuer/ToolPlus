# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****
#


#The entire code was written by CoDEmanX, but the idea was mine. Still full credit to CoDEmanX.
#bl_info = {
#    "name": "Clear All",
#    "description": "This script allows you to clear an objects Location, Rotation, and Scale at the same time",
#    "author": "CoDEmanX,Albertofx",
#    "version": (1,0),
#    "blender": (2, 71, 0),
#    "location": "Search Menu",
#    "category": "3D View"
#}

import bpy
from mathutils import Matrix

class OBJECT_OT_clear_all(bpy.types.Operator):
    """Clear Location, Rotation and Scale"""
    bl_idname = "tp_ops.clear_all"
    bl_label = "Clear All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for ob in context.selected_editable_objects:
            ob.matrix_world = Matrix.Identity(4)
        return {'FINISHED'}

# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()