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


from os.path import dirname
from . import ntransform_keymap

class View3D_TP_KeyMap_Transform(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_ntransform"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = ntransform_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}

  
        
class AlignNormal(bpy.types.Operator):
    """Align selected Mesh to active Face in Normal Z Direction"""
    bl_idname = "mesh.align_normal"
    bl_label = "Align to Normal"
    bl_options = {'REGISTER', 'UNDO'}

    manipul = bpy.props.BoolProperty(name="Set Normal Orientation",  description="Orientation", default=False) 

    def execute(self, context):
        bpy.ops.view3d.pivot_active()
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        for i in range (self.manipul):
            bpy.ops.space.normal()

        return {'FINISHED'}

            


  

# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


