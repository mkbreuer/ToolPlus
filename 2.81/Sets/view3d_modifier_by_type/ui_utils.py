# LOAD MODUL # 
import bpy
import os

# ADDON CHECK #
import addon_utils  

def get_addon_props():
    addon_global_props = bpy.context.window_manager.global_props_modbytype
    return (addon_global_props)

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


class VIEW3D_OT_modifier_tools(bpy.types.Operator):
   """enable modifier tools (save user settings be required for a permant activation)"""
   bl_label = "Modifier Tools"
   bl_idname = "tpc_ot.activate_modifier_tools"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        # check for needed addons
        modifier_tools_addon = "space_view3d_modifier_tools"
        state = addon_utils.check(modifier_tools_addon)
        if not state[0]:
            bpy.ops.preferences.addon_enable(module=modifier_tools_addon)
            print(self)
            self.report({'INFO'}, "Modifier Tools activated!") 

        return {'FINISHED'}
			


