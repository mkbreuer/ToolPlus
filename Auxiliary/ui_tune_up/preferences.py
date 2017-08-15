import bpy, bl_ui, os
from inspect import ismodule, isclass
from zipfile import ZipFile, ZIP_STORED
from bpy.props import *
from ui_tune_up.utils import dd, load_json
from ui_tune_up.keyboard import setup_keyboard
print(30*"-")

dev = True

dirsep = os.path.sep
root = dirsep.join([bpy.utils.script_paths()[0], "addons", "ui_tune_up", "configs"])

#open path with os file browser
def op(path):
	# if not os.path.isdir(path):
	# 	path = os.path.dirname(path)	
	if os.name == "nt":
		os.startfile(path)
	else:
		import subprocess
		opener ="open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call([opener, path])

#zips a directory
def zipdir(basedir, archivename):
	if not os.path.isdir(basedir):
		print(basedir, "not found")
		return True

	ignored_folders = ["ui_tune_up", "__pycache__"]
	
	with ZipFile(archivename, "w", ZIP_STORED) as z:
		for root, dirs, files in os.walk(basedir):
			dirs[:] = [d for d in dirs if d not in ignored_folders]

			#NOTE: ignore empty directories
			for fn in files:
				#rootdir = os.path.join(root)
				absfn = os.path.join(root, fn)
				
				#zfn = absfn[len(basedir)+len(os.sep):] #XXX: relative path
				zfn = os.path.relpath(absfn, basedir)
				z.write(absfn, zfn)

resource_types = ["USER", "LOCAL", "SYSTEM"]

#saves a configuration profile and custom scripts
def save_config(profile):
	#gather configuration files
	target = os.path.join(root, profile)
		
	if not os.path.exists(target):
		os.makedirs(target)

	for res in resource_types:
		archive = os.path.join(target, res + ".zip")
		source = bpy.utils.resource_path(res) + dirsep
		if res == "LOCAL":
			source = os.path.join(source, "scripts" + dirsep + "addons")
		zipdir(source, archive)
	#if dev: op(target)

#unzips a profile
def extract(zip, dest, overwrite = True):
	
	if os.path.exists(zip):
		#make a backup if posible
		with ZipFile(zip, "r") as z:
			if overwrite:
				for name in z.namelist():
					try:
						z.extract(name, dest)
					except:
						print(name)

			else:
				for name in z.namelist():
					path = os.path.join(dest, name)
					if not os.path.exists(path):
						print(name)
						z.extract(name, dest)

#installs a profile
def load_config(profile):
	for res in resource_types:
		if res == "USER":
			path = bpy.utils.resource_path("USER")
		elif res == "LOCAL":
			path = bpy.utils.resource_path("LOCAL") + dirsep + "scripts" + dirsep + "addons"

		zip = os.path.join(os.path.join(root, profile), res + ".zip")
	
		extract(zip, path)


def get_profiles(self, context):
	dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
	items = [(d, d.capitalize(), "", "", i+1) for i, d in enumerate(dirs)]
	items.insert(0, (" ", "Select Profile", "", "", 0))
	return items

def update_profile(self, context):
	self.profile = self.profiles

#loads user preferences from json config
def setup_preferences(self):
	data = load_json("data.json")
	if isinstance(data, str):
		self.report({"ERROR"}, data)
		return

	preferences = data['preferences']

	prefs = bpy.context.user_preferences
	errors = "."
	for namespace in preferences:
		if hasattr(prefs, namespace):
			spc = getattr(prefs, namespace)
			for attr in preferences[namespace]:
				value = preferences[namespace][attr]
				try:
					setattr(spc, attr, value)
				except Exception as e:
					errors = " with errors, See the console for details."
					print(e)
		else:
			print(namespace, "not found.")
			errors = " with errors, See the console for details."

	self.report({"INFO"}, "Preferences loaded" + errors)

def clear_prefs_panels(context):
	print(__name__)
	# prefs = context.user_preferences.addons[__name__].preferences
	prefs = context.user_preferences.addons["ui_tune_up"].preferences
	panels = prefs.panels
	doclean = True
	dead = 1
	while doclean:
		for i, p in enumerate(panels):
			if not p.destroy:
				panels.remove(i)
				break
		if dead > 100:
			doclean = False
			print("EXCEEDED REMOVING")
			
		if not len([p for p in panels if not p.destroy]):
			doclean = False
			break
		dead += 1
	return prefs

#finds classes in bpy.types
def findtype(name,  by = "bl_label"):
	mods = [
		("bpy.types", bpy.types) ,
		("bl_ui", bl_ui) ,
	]
	classes = []
	name = name.lower()
	for modname, mod in mods:
		for prop in dir(mod):
			cls = getattr(mod, prop)
			if isclass(cls) and bpy.types.Panel in cls.mro():
				if hasattr(cls, by):
					f = getattr(cls, by).lower()
					if by == "__name__":
						print(f, name)
						classes.append(".".join([modname, cls.__name__]))	
					else:
						if f.find(name)>-1:
							classes.append(".".join([modname, cls.__name__]))
	return classes
#if __name__ == "__main__":
#	res = findtype("transform")
#	print(res)
	
def load_panels(self, context):
	data = load_json("data.json")
	if isinstance(data, str):
		self.report({"ERROR"}, data)
		return

	panels = data['panels']
	prefs = clear_prefs_panels(context)
		
	for p in prefs.panels:
		prefs.panels.remove(0)

	for p in panels:
		item = prefs.panels.add()
		item.name = p
		item.destroy = True

	self.report({"INFO"}, "Panels loaded")
		


class TUNEUP_OT_manage_configurations(bpy.types.Operator):
	"""Loads or saves configuration profiles"""
	bl_idname = "tuneup.manage_configuration"
	bl_label = "Manage Configuration"

	cmd = StringProperty(default = "SAVE")
	profiles = EnumProperty(items = get_profiles, name = "Profile Name", update = update_profile)
	profile = StringProperty(default = "")
	
	@classmethod
	def poll(cls, context):
		return True
		#return context.active_object is not None
	def draw(self, context):
		layout = self.layout
		
		if self.cmd == "SAVE":
			layout.label("Save Configuration." , icon = "QUESTION")
			layout.label("This proccess will perform the following actions.")
			layout.label("- Save User Preferences.")
			layout.label("- Save Startup File.")
			layout.label("- Save Installed Addons.")
			layout.prop(self, "profiles", text = "Select or")
			layout.prop(self, "profile", text = "Create profile")
			layout.label("Do you want to proceed?")

		elif self.cmd == "LOAD":
			layout.label("Load Configuration.", icon = "QUESTION")
			layout.label("This proccess will perform the following actions:")
			layout.label("- Overwrite current User Preferences")
			layout.label("- Overwrite current Startup File")
			layout.label("- Install profile addons")
			layout.label("- Ask to restart Blender.")
			layout.label("(Backup is avalaible)")
			layout.prop(self, "profiles")
			layout.label("Do you want to proceed?")
			#layout.prop(self, "profile")
			
			
	def invoke(self, context, event):
		if self.cmd == "LOAD":
			check_backup()
		if self.cmd == "LOAD" or self.cmd == "SAVE":
			print("invoke", self.cmd, self.profile)
			return context.window_manager.invoke_props_dialog(self)
		else:
			print("execute", self.cmd)
			return self.execute(context)
	
	def execute(self, context):
		
		profile = self.profile.strip()
		
		if profile:
			profile = profile.replace(" ", "_")
			profile = profile.replace(dirsep, "")
			profile = profile.lower()
			print("Profile: %s" % profile)
			
			if self.cmd == "SAVE":
				if profile == "backup":
					self.report({'ERROR'}, 'Cant save as backup. Choose another profile.')
					return {'CANCELLED'}
				
				bpy.ops.wm.save_userpref()
				self.report({'INFO'}, "Saving configuration")
				save_config(profile)
				self.report({'INFO'}, "Configuration Saved")
				
			elif self.cmd == "LOAD":
				if not check_backup():
					save_config("backup")
				load_config(profile)
				self.report({'WARNING'}, "Loading configuration")
				bpy.ops.wm.quit_blender("INVOKE_DEFAULT")
				
		if self.cmd == "LOAD_KEYBOARD":
			setup_keyboard(self)
		
		elif self.cmd == "LOAD_PREFERENCES":
			setup_preferences(self)
			
		
		elif self.cmd == "LOAD_PANELS":
			load_panels(self, context)
		
		elif self.cmd == "OPEN_CONFIGS":
			file = os.path.dirname(__file__)
			file = os.path.join(file, "configs")
			op(file)

		elif self.cmd == "OPEN_JSON":
			file = os.path.dirname(__file__)
			file = os.path.join(file, "data.json")
			op(file)
			
		return {'FINISHED'}
			
def check_backup():
	backup = os.path.join(root, "backup")
	print(backup)
	if not os.path.exists(backup):
		save_config("backup")
	return os.path.exists(backup)
	
	
import sys, inspect
classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

def register():
	for name, cls in classes:
		try:
			bpy.utils.register_class(cls)
		except Exception as e:
			print(e)
	
#	bpy.ops.tuneup.save_configuration('INVOKE_DEFAULT')
	
def unregister():
	for name, cls in classes:
		try:
			bpy.utils.unregister_class(cls)
		except Exception as e:
			print(e)
			
if __name__ == "__main__":
	register()
