# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*

from os.path import dirname
from . import ui_keymap

class VIEW3D_OT_KeyMap_SnapFlat(bpy.types.Operator):
    bl_idname = "tpc_ops.keymap_snapflat"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = ui_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}
