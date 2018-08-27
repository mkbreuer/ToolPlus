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

# LOAD MODUL #    
import bpy
from bpy import *
from os.path import dirname


from . import keymap_align
from . import keymap_boolean
from . import keymap_delete
from . import keymap_editing
from . import keymap_origin
from . import keymap_resurface
from . import keymap_sculpt
from . import keymap_selection


# RESURFACE #
class View3D_TP_KeyMap(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_resurface"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_rsf.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# ALIGN #
class View3D_TP_KeyMap_Align(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_align"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_align.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# BOOLEAN #
class View3D_TP_KeyMap_Boolean(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_boolean"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_boolean.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# DELETE #
class View3D_TP_KeyMap_Delete(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_delete"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_delete.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}
    

# EDITING #
class View3D_TP_KeyMap_Editing(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_edit"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_edit.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# ORIGIN #
class View3D_TP_KeyMap_Origin(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_origin"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_origin.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# PIEMENU #
class View3D_TP_KeyMap_Pie_3D(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_pie_3d"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_pie_3d.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# SCULPT #
class View3D_TP_KeyMap_Sculpt(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_sculpt"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_sculpt.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# SELECTION #
class View3D_TP_KeyMap_Selection(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_selection"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_selection.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}
    

# RELAX #
class View3D_TP_KeyMap_Selection(bpy.types.Operator):
    bl_idname = "tp_ops.key_map_relax"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = keymap_relax.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}    
























# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()