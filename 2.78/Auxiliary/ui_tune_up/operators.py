#BLENDER OPERATORS
import bpy, bmesh
from bpy.props import *
from ui_tune_up.utils import dd
from ui_tune_up.select_paired_rings import MESH_OT_select_pair_rings
print(30*"-")
##on edit mode, pressing M key will toggle mark seams over selection
class MESH_OT_smart_mark_seam(bpy.types.Operator):
	"""Toggle Mark Seam on selected edges"""
	bl_idname = "mesh.smart_mark_seam"
	bl_label = "Smart Mark Seam"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None and context.mode == "EDIT_MESH"

	def execute(self, context):
		obj = context.object
		spc = context.space_data
		#print("marking seam", spc.type)
		me = bmesh.from_edit_mesh(obj.data)
	
		if spc.type == "IMAGE_EDITOR" and not context.tool_settings.use_uv_select_sync:
			bpy.ops.uv.mark_seam()
			return {'FINISHED'}
	
	
		clear = False
		for e in me.edges:
			if e.select and e.seam:
				clear = True
				break
				
		bpy.ops.mesh.mark_seam(clear = clear)
		
		return {'FINISHED'}
#
##toggle pin uv
class UV_OT_smart_pin(bpy.types.Operator):
	"""Toggle pin uv"""
	bl_idname = "uv.smart_pin"
	bl_label = "Smart UV Pin"

	@classmethod
	def poll(cls, context):
		return context.space_data.type == "IMAGE_EDITOR" and context.mode == "EDIT_MESH"

	def execute(self, context):
		obj = context.object
		me = bmesh.from_edit_mesh(obj.data)
		uv_layer = me.loops.layers.uv.active
		clear = False
		for f in me.faces:
			for l in f.loops:
				uv = l[uv_layer]
				if uv.select and uv.pin_uv:
					print(uv.uv, uv.pin_uv)
					clear = True
					break
			if clear:
				break
		
		print("pining", clear)
		bmesh.update_edit_mesh(obj.data)
		bpy.ops.uv.pin(clear = clear)
		return {'FINISHED'}
			
class UV_OT_smart_select(bpy.types.Operator):
	"""Syncs mesh selection modes to the UV Editor"""
	bl_idname = "uv.smart_select"
	bl_label = "Smart UV Select"

	value = StringProperty()
	
	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		ts = context.tool_settings
		sync = ts.use_uv_select_sync
		mode = self.value
		
		if not sync:
			ts.uv_select_mode = mode
			#print("selecting all")
			#bpy.ops.mesh.select_all()
		else:
			if mode != "ISLAND":
				ts.mesh_select_mode = [mode == "VERTEX", mode == "EDGE", mode == "FACE"]
			
		return {'FINISHED'}

#overrides default add bdezier curve
class CURVE_OT_primitive_bezier_curve_add(bpy.types.Operator):
	"""Adds a bezier curve"""
	bl_idname = "curve.primitive_bezier_curve_add"
	bl_label = "Construct a Bezier Curve"

	@classmethod
	def poll(cls, context):
		return context.area.type == "VIEW_3D" and context.mode == "OBJECT"

	def execute(self, context):
		scn = context.scene
		name = "BezierCurve"
		curve = bpy.data.curves.new(name, "CURVE")
		curve.dimensions = "3D"
		spline = curve.splines.new("BEZIER")
		points = spline.bezier_points
		points[0].handle_left_type = "AUTO"
		points[0].handle_right_type = "AUTO"
		points.add()
		points[1].handle_left_type = "AUTO"
		points[1].handle_right_type = "AUTO"
		points[1].co = [2,0,0]
		obj = bpy.data.objects.new(name, curve)
		obj.location = scn.cursor_location
		bpy.ops.object.select_all(action = "DESELECT")
		scn.objects.link(obj)
		obj.select = True
		scn.objects.active = obj
		return {'FINISHED'}
	

class CURVE_OT_select_path(bpy.types.Operator):
	"""Select curve path"""
	bl_idname = "curve.select_path"
	bl_label = "Curve Select Path"

	@classmethod
	def poll(cls, context):
		return context.mode == "EDIT_CURVE"
	
	def invoke(self, context, event):
		bpy.ops.view3d.select(toggle=True, location = (event.mouse_region_x, event.mouse_region_y))
		obj = context.object
		spline = obj.data.splines.active
		if spline:
			if spline.type == "BEZIER":
				points = spline.bezier_points
				selection = [i for i, p in enumerate(points) if p.select_control_point == True]
				if len(selection)>1:
					for i in range(min(selection), max(selection)):
						points[i].select_control_point = True
						points[i].select_left_handle = True
						points[i].select_right_handle = True

			else:
				points = spline.points
				selection = [i for i, p in enumerate(points) if p.select == True]
				if len(selection)>1:
					for i in range(min(selection), max(selection)):
						points[i].select = True
		return {'FINISHED'}

class GRAPH_OT_show_toggle(bpy.types.Operator):
	"""Show/Hide selected animation curves"""
	bl_idname = "graph.show_toggle"
	bl_label = "Toggle Animation Curves"
		
	cmd = StringProperty(default = "hide")
	
	@classmethod
	def poll(cls, context):
		return context.object is not None and context.space_data.type == "GRAPH_EDITOR"

	def execute(self, context):
		cmd = self.cmd
		obj = context.object
		
		fcurves = obj.animation_data.action.fcurves
	
		if cmd == "hide":
			for c in fcurves:
				if c.select:
					c.hide = True
		elif cmd == "solo":
			for c in fcurves:
				if c.select:
					c.hide = False
				else:
					c.hide = True
		elif cmd == "unhide":
			for c in fcurves:
				c.hide = False
		
		return {'FINISHED'}
	
import sys, inspect
classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

def setup_operators():
	for name, cls in classes:
		try:
			bpy.utils.register_class(cls)
		except Exception as e:
			print(e)
	dd("operators loaded")
	
def register():
	setup_operators()	
			
def unregister():
	for name, cls in classes:
		try:
			bpy.utils.unregister_class(cls)
		except Exception as e:
			print(e)
			
if __name__ == "__main__":
	register()
