#
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


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
   

from os.path import dirname
from . import deform_keymap

class View3D_TP_KeyMap(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_deform"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = deform_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


class View3D_TP_Set_Zero_Rotation(bpy.types.Operator):
    """Set Zero Rotation"""
    bl_idname = "tp_ops.zero_rotation"
    bl_label = "Set Zero Rotation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print(self)
        self.report({'INFO'}, "Zero Rotation")  

        bpy.context.object.rotation_euler[0] = 0
        bpy.context.object.rotation_euler[1] = 0
        bpy.context.object.rotation_euler[2] = 0         

        return {'FINISHED'}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()