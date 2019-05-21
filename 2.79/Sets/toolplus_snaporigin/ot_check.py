# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# ADDON CHECK #
import addon_utils

class VIEW3D_OT_Activate_Looptools(bpy.types.Operator):
   """enable looptools (save user settings be required for a permant activation)"""
   bl_label = "Looptools"
   bl_idname = "tpc_ot.enable_looptools"
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