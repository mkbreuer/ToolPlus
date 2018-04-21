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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



# KEYMAP TO EDITOR #
from os.path import dirname
from .. import align_keymap

class View3D_TP_KeyMap(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_align"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = align_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}



# ADDON CHECK #
import addon_utils

class VIEW3D_TP_Looptools(bpy.types.Operator):
   """enable looptools (save user settings be required for a permant activation)"""
   bl_label = "Looptools"
   bl_idname = "tp_ops.enable_looptools"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        loop_tools_addon = "mesh_looptools"
        state = addon_utils.check(loop_tools_addon)
        if not state[0]:
            bpy.ops.wm.addon_enable(module=loop_tools_addon)
            print(self)
            self.report({'INFO'}, "LoopTools activated!") 

        return {'FINISHED'}

class VIEW3D_TP_TinyCAD(bpy.types.Operator):
   """enable tiny cad (save user settings be required for a permant activation)"""
   bl_label = "TinyCAD"
   bl_idname = "tp_ops.enable_tinycad"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        mesh_tiny_cad_addon = "mesh_tiny_cad"
        state = addon_utils.check(mesh_tiny_cad_addon)
        if not state[0]:
            bpy.ops.wm.addon_enable(module=mesh_tiny_cad_addon)
            print(self)
            self.report({'INFO'}, "TinyCAD activated!") 

        return {'FINISHED'}


    
# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()



