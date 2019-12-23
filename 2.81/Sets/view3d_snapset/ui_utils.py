# LOAD MODUL # 
import bpy
import os

# ADDON CHECK #
import addon_utils  

def get_addon_prefs():
    addon_name = os.path.splitext(__package__)[0]
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[addon_name].preferences
    return (addon_prefs)

def get_addon_name():
    return os.path.basename(os.path.dirname(os.path.realpath(__file__)))
	
def addon_exists(name):
    for addon_name in bpy.context.preferences.addons.keys():
        if name in addon_name: return True
    return False	


class VIEW3D_OT_align_tools(bpy.types.Operator):
   """enable align tools (save user settings be required for a permant activation)"""
   bl_label = "AlignTool"
   bl_idname = "tpc_ot.activate_align_tools"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        align_tools_addon = "space_view3d_align_tools"
        state = addon_utils.check(align_tools_addon)
        if not state[0]:
            bpy.ops.preferences.addon_enable(module=align_tools_addon)
            print(self)
            self.report({'INFO'}, "Align Tools activated!") 

        return {'FINISHED'}
			

class VIEW3D_OT_align_mesh(bpy.types.Operator):
   """enable align mesh (save user settings be required for a permant activation)"""
   bl_label = "Align Mesh"
   bl_idname = "tpc_ot.activate_align_mesh"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        alignmesh_addon = "view3d_alignmesh" 
        state = addon_utils.check(alignmesh_addon)
        if not state[0]:
            bpy.ops.preferences.addon_enable(module=alignmesh_addon)
            print(self)
            self.report({'INFO'}, "Align Mesh activated!") 

        return {'FINISHED'}


class VIEW3D_OT_looptools(bpy.types.Operator):
   """enable looptools (save user settings be required for a permant activation)"""
   bl_label = "Looptools"
   bl_idname = "tpc_ot.activate_looptools"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        loop_tools_addon = "mesh_looptools"
        state = addon_utils.check(loop_tools_addon)
        if not state[0]:
            bpy.ops.preferences.addon_enable(module=loop_tools_addon)
            print(self)
            self.report({'INFO'}, "LoopTools activated!") 

        return {'FINISHED'}

