import bpy
from bpy.props import *
print(30*"-")

# PANELS 

#simplify curves moved to animation editor
class SimplifyCurvesPanel(bpy.types.Panel):
	"""Creates a Panel in the Object properties window"""
	bl_label = "Simplify Curves"
	bl_idname = "GRAPH_PT_simplify"
	bl_space_type = 'GRAPH_EDITOR'
	bl_region_type = 'UI'
	#bl_context = "object"

	def draw(self, context):
		layout = self.layout

		obj = context.object

		row = layout.row()
		row.operator("graph.simplify")

# HEADERS
def purge(collection):
	removed = 0
	for item in collection:
		if item.users == 0 and item.use_fake_user == False:
			print("%s: %s removed." % (item.__class__.__name__, item.name))
			collection.remove(item)
			removed += 1
	return removed

class PurgeBlendData(bpy.types.Operator):
	"""Purge Blend Data"""
	bl_idname = "wm.purge_data"
	bl_label = "Purge unusued datablocks"

	@classmethod
	def poll(cls, context):
		return True

	def execute(self, context):
		area = context.area
		# print(area.type)
		
		removed = 0
		if area.type == "VIEW_3D":
			removed = purge(bpy.data.meshes)
			removed += purge(bpy.data.curves)
			removed += purge(bpy.data.materials)
			removed += purge(bpy.data.textures)
			removed += purge(bpy.data.cameras)
			removed += purge(bpy.data.lamps)
			
		elif area.type == "DOPESHEET_EDITOR":
			removed = purge(bpy.data.actions)
		
		elif area.type == "IMAGE_EDITOR":
			removed += purge(bpy.data.images)
			removed += purge(bpy.data.textures)
			
		self.report({'INFO'}, "%s items removed" %(removed,))					
		return {'FINISHED'}

def draw_purge_data(self, context):
		layout = self.layout
		layout.separator()
		layout.operator("wm.purge_data", icon = "GHOST_DISABLED", text = "")

class PurgeView3D(bpy.types.Header):
	'''Purge objects, and object data'''
	bl_label = "Purge"
	bl_space_type = "VIEW_3D"

class PurgeDopesheetEditor(bpy.types.Header):
	'''Purge objects, and object data'''
	bl_label = "Purge"
	bl_space_type = "DOPESHEET_EDITOR"

class PurgeImageEditor(bpy.types.Header):
	'''Purge objects, and object data'''
	bl_label = "Purge"
	bl_space_type = "IMAGE_EDITOR"

headers = [PurgeView3D, PurgeImageEditor, PurgeDopesheetEditor]
for h in headers:
	h.draw = draw_purge_data

import sys, inspect
classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
	
def setup_ui():
	
	for c in classes:
		cls = c[1]
		try:
			bpy.utils.register_class(cls)
		except Exception as e:
			print(e)
	
	from ui_tune_up.utils import operator_exists
	prefs = bpy.context.user_preferences

	#enable curve simplify addon
	if not operator_exists("graph.simplify") and "curve_simplify" in [a.module for a in prefs.addons]:
		bpy.ops.wm.addon_enable(module = "curve_simplify")
		
	print("ui done.")

def register():
	setup_ui()
	
def unregister():
	pass

if __name__ == "__main__":
	register()