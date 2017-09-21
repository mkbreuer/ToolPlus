#NEW MENUS! 
#for easy to access common functionality

import bpy
from bpy.props import *


def unlock_objects(scn):
	#look for visible objects
	active_layers = [i for i, l in enumerate(scn.layers) if l]
	for obj in scn.objects:
		for i in active_layers:
			if obj.layers[i] and not obj.hide and obj.hide_select:
				#unlock them
				obj.hide_select = False

#UNLOCKS ALL VISIBLE OBJECTS
class OBJECT_OT_hide_select_clear(bpy.types.Operator):
	"""Unlocks all visible objects"""
	bl_idname = "object.hide_select_clear"
	bl_label = "Clear All Restrict Select"

	def execute(self, context):
		scn = context.scene

		unlock_objects(scn)	

		return {'FINISHED'}

bpy.utils.register_class(OBJECT_OT_hide_select_clear)

#added to object specials 
class ObjectDisplayMenu(bpy.types.Menu):
	bl_label = "Display Menu"
	bl_idname = "OBJECT_MT_display_menu"

	def draw(self, context):
		layout = self.layout
		obj = context.object
		
		if obj:
			layout.prop(obj, "show_name")
			layout.prop(obj, "show_axis")
			layout.prop(obj, "show_wire")
			layout.prop(obj, "show_x_ray")

bpy.utils.register_class(ObjectDisplayMenu)

def object_specials(self, context):
	layout = self.layout
	obj = context.object


	layout.operator("object.hide_select_clear")
	layout.operator_context = 'INVOKE_DEFAULT'
	layout.operator("view3d.ruler")

	if obj.type in  ["MESH", "CURVE"]:
		layout.operator("object.shade_smooth")
		layout.operator("object.shade_flat")
	layout.separator()
	layout.prop_menu_enum(obj, "draw_type", text = "Draw Type")
	layout.menu(ObjectDisplayMenu.bl_idname)
	layout.separator()
	#row.label(text="", icon='RESTRICT_VIEW_OFF')
	layout.prop(obj, "hide", icon="RESTRICT_VIEW_OFF")
	layout.prop(obj, "hide_select", icon = "RESTRICT_SELECT_OFF")
	layout.prop(obj, "hide_render", icon = "RESTRICT_RENDER_OFF")

def curve_specials(self, context):
	layout = self.layout
	curve = context.object.data
	layout.prop(curve, "show_handles")
	layout.prop(curve, "show_normal_face")

screen_icons = {
	"3D View Full": "GROUP",
	"Animation": "IPO",
	"Compositing": "NODETREE",
	"Default": "OBJECT_DATA",
	"Game Logic": "LOGIC",
	"Motion Tracking": "RENDER_ANIMATION",
	"Scripting": "TEXT",
	"UV Editing": "IMAGE_COL",
	"Video Editing": "SEQUENCE",
}

# items = []
# for scr in bpy.data.screens:
# 	print(scr.name)
# for i, scr in enumerate(bpy.data.screens):
# 	items.append((scr.name, screen_icons[scr.name], scr.name, i))
# #descriptin icon identifier name value
# print(items)

# bpy.types.Scene.screens = EnumProperty(items = items)
class WM_OT_change_screen(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "wm.change_screen"
	bl_label = "Selects screen"
	
	screen = StringProperty(default = "")
	
	@classmethod
	def poll(cls, context):
		return len(bpy.data.screens)

	def execute(self, context):
		context.window.screen = bpy.data.screens[self.screen]
		
		return {'FINISHED'}

class WINDOW_MT_screen_types(bpy.types.Menu):
	bl_label = "Screens"
	bl_idname = "WINDOW_MT_screen_types"

	def draw(self, context):
		layout = self.layout
		
		for src in bpy.data.screens:
			if src.name != "temp":
				try:
					icon = screen_icons[src.name]
				except:
					icon = ""
				layout.operator("wm.change_screen", icon = icon, text = src.name).screen = src.name


class LayoutMenu(bpy.types.Menu):
	bl_label = "Layout"
	bl_idname = "WINDOW_MT_layout_menu"

	def draw(self, context):
		layout = self.layout
		area = context.area
		
		row = layout.menu_pie()
		#screen types
		row.menu("WINDOW_MT_screen_types")
		#row.props_enum(context.scene, "screens")

		#properties context
		pareas = [parea for parea in context.screen.areas if parea.type == "PROPERTIES"]
		if pareas:
			parea = pareas[0]
			spc = parea.spaces.active
			row.props_enum(spc , "context")

		#area types
		row.props_enum(area, "type")
		
bpy.utils.register_class(LayoutMenu)

import sys, inspect
classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

def setup_menus():
	register()
	#VIEW3D TOOLS
	bpy.types.VIEW3D_MT_object_specials.append(object_specials)
	bpy.types.VIEW3D_MT_edit_curve_specials.append(curve_specials)
	print("Menus done.")
	
def register():
	for name, cls in classes:
		try:
			bpy.utils.register_class(cls)
		except Exception as e:
			print(e)
	
			
def unregister():
	for name, cls in classes:
		try:
			bpy.utils.unregister_class(cls)
		except Exception as e:
			print(e)
			
if __name__ == "__main__":
	register()
