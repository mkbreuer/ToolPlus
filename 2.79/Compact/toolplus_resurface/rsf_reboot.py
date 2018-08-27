# Add-on information
bl_info = {
	"name" : "Reboot",
	"author" : "(saidenka) meta-androcto",
	"version" : (0,1),
	"blender" : (2, 7),
	"location" : "File Menu",
	"description" : "Reboot Blender without save",
	"warning" : "",
	"wiki_url" : "",
	"tracker_url" : "",
	"category" : "Development"
}


import bpy
import os, sys
import subprocess


class RestartBlender(bpy.types.Operator):
	bl_idname = "wm.restart_blender"
	bl_label = "Reboot Blender"
	bl_description = "Blender Restart"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		py = os.path.join(os.path.dirname(__file__), "console_toggle.py")
		filepath = bpy.data.filepath
		if (filepath != ""):
			subprocess.Popen([sys.argv[0], filepath, '-P', py])
		else:
			subprocess.Popen([sys.argv[0],'-P', py])
		bpy.ops.wm.quit_blender()
		return {'FINISHED'}






def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(RestartBlender.bl_idname, icon="PLUGIN")
    layout.separator()




def register():
    bpy.utils.register_module(__name__)


    bpy.types.INFO_MT_file.prepend(menu_func)




def unregister():
    bpy.utils.register_module(__name__)


    bpy.types.INFO_MT_file.remove(menu_func)


if __name__ == "__main__":
    register()