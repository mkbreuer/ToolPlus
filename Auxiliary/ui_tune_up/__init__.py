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

bl_info = {
	"name": "Tune Up!",
	"author": "Mackraken",
	"version": (0, 5),
	"blender": (2, 72, 0),
	"location": "",
	"description": "Tune up Blender keys, configurations and behaviours",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "User Interface"}

# THIS ADDON PERFORMS SEVERAL CHANGES ON BLENDER INTERFACE, OPERATORS, KEYBOARD AND MENUS, USE WITH CARE.

import bpy, bl_ui, sys, inspect
from bpy.props import *
from math import ceil, floor
from ui_tune_up.utils import dd, load_json, operator_exists, dev
from ui_tune_up.preferences import TUNEUP_OT_manage_configurations, findtype,  clear_prefs_panels
from ui_tune_up.operators import setup_operators, classes as operators
from ui_tune_up.menus import setup_menus
#removes key shortcuts assigned to invalid operators
from ui_tune_up.keyboard import  clear_keyboard
#new headers and panels
from ui_tune_up.ui import setup_ui

#operators idnames
idnames = [(item[1].bl_idname, item[1].__doc__)  for item in operators]

#from ui_tune_up.menus import *
#from ui_tune_up.ui import *

print(30*"-")

def update_destroy(self, context):
	if self.destroy:
		names = self.name.split(".")
		try:
			for i in range(len(names)):
				if i == 0:
					cls = sys.modules[names[i]]
				else:
					cls = getattr(cls, names[i])
			register_class(cls, not self.destroy)
		except Exception as e:
			print(e)
			

class PanelsToDestroyProps(bpy.types.PropertyGroup):
	destroy = BoolProperty(name = "Destroy", default = False, update=update_destroy)


bpy.utils.register_class(PanelsToDestroyProps)
		
def update_search(self, context):
	 #clear prefs panels
	prefs = clear_prefs_panels(context)

	#search for terms
	search = self.panel_input
	if not search:
		return

	res = findtype(search)
	
	#add the items
	print(30*"-")
	print(res)
	for cls in res:
		item = prefs.panels.add()
		item.name = cls
		#print(cls.bl_label, cls.__name__)	

#destroys selected panels on startup
def setup_panels():
	dd("setting panels")
	prefs = bpy.context.user_preferences.addons["ui_tune_up"].preferences
	for item in prefs.panels:
		update_destroy(item, bpy.context)
		
class TUNEUP_addon_preferences(bpy.types.AddonPreferences):
	bl_idname = __name__
	panel_input = StringProperty(name = "Search", update = update_search)
	panels = CollectionProperty(type = PanelsToDestroyProps)

	def draw(self, context):
		layout = self.layout
		panels = self.panels

		#split=layout.split(percentage=0.50)
		#profiles
		box = layout.box()
		row = box.row()
		row.label("Profiles:")
		row.operator("tuneup.manage_configuration", text = "Load").cmd = "LOAD"
		row.operator("tuneup.manage_configuration", text = "Save").cmd = "SAVE"
		row.operator("tuneup.manage_configuration", text = "Open Configs").cmd = "OPEN_CONFIGS"
		#configuration
		box = layout.box()
		row = box.row()
		row.label("Configuration:")
		row.operator("tuneup.manage_configuration", text = "Load Keyboard").cmd = "LOAD_KEYBOARD"
		row.operator("tuneup.manage_configuration", text = "Load Preferences").cmd = "LOAD_PREFERENCES"
		row.operator("tuneup.manage_configuration", text = "Load Panels").cmd = "LOAD_PANELS"
		row.operator("tuneup.manage_configuration", text = "Open Config").cmd = "OPEN_JSON"
		#panels
		box = layout.box()
		row = box.row()
		row.label("Panels to Destroy:")
		row = box.row()
		row.prop(self, "panel_input")
		for p in panels:
			row = box.row(align=True)
			row.prop(p, "destroy")
			row.prop(p, "name", text = "")

		row = box.row()
		row.label(str(len(self.panels)))
		#operators		
		box = layout.box()
		row = box.row()
		row.label("Operators loaded:")
		for op, desc in idnames:
			row = box.row()
			row.label('%s: "%s"' % (op, desc))



import sys, inspect
classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

def register_class(cls, register = True):
	try:
		if register:
			bpy.utils.register_class(cls)
		else:
			bpy.utils.unregister_class(cls)
	except Exception as e:
		print(cls.__name__, e)



def register():
	dd("registering")
	for name, cls in classes:
		register_class(cls)

	setup_panels()
	setup_operators()
	setup_menus()
	setup_ui()
	
#	config = load_json("data.json")
#	setup_keyboard(config['keyboard'])
	
	

			
def unregister():
	print("unregistering")
	for name, cls in classes:
		bpy.utils.unregister_class(cls)
	for op, cls in operators:
		bpy.utils.unregister_class(cls)
	print(operator_exists("uv.smart_select"))
	clear_keyboard()

if __name__ == "__main__":
	register()





