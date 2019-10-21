# ##### BEGIN MIT LICENSE BLOCK #####
#
# Copyright (c) 2012 Mikhail Rachinskiy
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

#bl_info = {
#	"name": "Switch",
#	"author": "Mikhail Rachinskiy (jewelcourses.com)",
#	"version": (0,5,0),
#	"blender": (2,7,4),
#	"location": "Properties → Modifiers",
#	"description": "Convinient placement and management of certain modifier propierties.",
#	"warning": "",
#	"wiki_url": "http://jewelcourses.com",
#	"tracker_url": "http://jewelcourses.com",
#	"category": "Object"}



# LOAD MODUL #    
import bpy
from bpy.types import (Operator, Panel)

def get_name(name):
	for mo in bpy.context.active_object.modifiers:
		if name == mo.name:
			return mo.name
	return False


class MOD_DISPLAY(Operator):
	'''Copy modifier viewport display state to selected'''
	bl_label = "Switch"
	bl_idname = "switch.mod_display"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		for ob in context.selected_objects:
			for mo in ob.modifiers:
				m_name = get_name(mo.name)
				if m_name:
					mo.show_viewport = context.active_object.modifiers[m_name].show_viewport
		return {'FINISHED'}


class MOD_PROP(Operator):
	'''Copy modifier properties to selected'''
	bl_label = "Switch"
	bl_idname = "switch.mod_prop"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		obj = context.active_object
		for ob in context.selected_objects:
			for mo in ob.modifiers:
				if mo.type == 'ARRAY':
					if mo.name == get_name(mo.name):
						mo.constant_offset_displace = obj.modifiers[mo.name].constant_offset_displace
						mo.count = obj.modifiers[mo.name].count
		return {'FINISHED'}



"""

class SwitchPanel(Panel):
	
	bl_label = "Switch Selected"
	bl_idname = "SWITCH_PANEL"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_options = {'DEFAULT_CLOSED'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def draw(self, context):
		layout = self.layout
		mo_list = context.active_object.modifiers

		box = layout.box()

		if mo_list:

			# Display properties
			###################################

			split = box.split()

			# 1st column
			col = split.column(align=True)
			for mo in mo_list:
				col.prop(mo, "show_viewport", text=mo.type)

			# 2nd column
			col = split.column(align=True)
			col.operator("switch.mod_display", icon="FILE_TICK")

			###################################

			layout.separator()

			# Array properties
			###################################

			mo_types = []
			append = mo_types.append

			for mo in mo_list:
				if mo.type == 'ARRAY':
					append(mo.type)

					box = layout.box()
					box.label(mo.name)

					split = box.split()

			# 1st column
					col = split.column(align=True)
					col.prop(mo, "constant_offset_displace", text="")

			# 2nd column
					col = split.column(align=True)
					col.prop(mo, "count", text="")

			###################################

			if 'ARRAY' in mo_types:
				col = layout.column(align=True)
				split = col.split()
				col = split.column()
				col = split.row()
				col.operator("switch.mod_prop", icon="FILE_TICK")

			###################################


		else:
			box.label('No modifiers on active object')

"""

classes = [
	#SwitchPanel,

	MOD_DISPLAY,
	MOD_PROP,
]


def register():
	for cls in classes:
		bpy.utils.register_class(cls)

def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)

if __name__ == "__main__":
	register()