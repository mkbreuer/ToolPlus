# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*

from os.path import dirname
from . import ui_keymap

class VIEW3D_OT_keymap_snapset(bpy.types.Operator):
    bl_idname = "tpc_ot.keymap_snapset"
    bl_label = "Keys in Text Editor"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = ui_keymap.__file__
        bpy.data.texts.load(path)

        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
  
        for window in context.window_manager.windows:
            if len(window.screen.areas) == 1 and window.screen.areas[0].type == 'PREFERENCES':
                window.screen.areas[0].type = 'TEXT_EDITOR'

                bpy.context.space_data.show_line_numbers = True
                bpy.context.space_data.show_syntax_highlight = True
      
        return {"FINISHED"}

