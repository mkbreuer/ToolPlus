import bpy, bmesh
from bpy.props import *
print(30*"-")

directions = {
	"BOTH": {"name": "Both", "value":-1},
	"FORWARD": {"name": "Forward", "value":0},
	"BACKWARD": {"name": "Backward", "value": 1}
}


items = [(k, directions[k]['name'], "", directions[k]['value']) for k in directions.keys()]

def findring(e, limit = 0, direction = -1, interval=2, prevf=None, starting_edge = None,level = 0):
	
	if limit > 0 and level>=limit*interval: 
		return
	
	#prevents max recursion on not boundary loops
	if level == 0:
		starting_edge = e
		
	for i, f in enumerate(e.link_faces):
		if i == direction and level ==0: continue
		if len(f.edges) == 4 and f.hide == False and f!=prevf:
			for i, fe in enumerate(f.edges):
				if fe == e:
				
					if level%interval - (interval-1) == 0:
							f.edges[i-2].select = True
							
					if not f.edges[i-2].is_boundary and f.edges[i-2]!=starting_edge:
						findring(f.edges[i-2], limit, direction, interval, f, starting_edge, level+1)
					break

class MESH_OT_select_pair_rings(bpy.types.Operator):
	"""Select edges each two rings"""
	bl_idname = "mesh.select_pair_rings"
	bl_label = "Select edges each two rings"
	bl_options = {'REGISTER', 'UNDO'}

	limit = IntProperty(default = 0, min = 0, name = "Limit", description = "Amount of rings to select (0 to disable)")
	direction = EnumProperty(items = items, name = "Direction", default = "BOTH", description = "Direction to select rings")
	interval = IntProperty(default = 2, min = 1, name = "Interval")
	
	@classmethod
	def poll(cls, context):
		return context.active_object is not None and context.mode == "EDIT_MESH"
	
	def draw(self, context):
		layout = self.layout
		layout.prop(self, "limit")
		layout.prop(self, "interval")
		layout.label(MESH_OT_select_pair_rings.direction[1]['name'] +":")
		layout.prop(self, "direction", expand = True)
		
	def execute(self, context):
		#print(dir(MESH_OT_select_pair_rings.direction))
		obj = context.object
		me = bmesh.from_edit_mesh(obj.data)
		edges = [e for e in me.edges if e.select]
		
		direction = directions[self.direction]['value']
		interval = self.interval
		
		#print(direction)
		for e in edges:
			findring(e, self.limit, direction, interval)
			
		bmesh.update_edit_mesh(obj.data)

		return {'FINISHED'}

import sys, inspect
classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

def register():
	for c in classes:
		cls = c[1]
		try:
			bpy.utils.register_class(cls)
		except Exception as e:
			print(e)
			
def unregister():
	for c in classes:
		cls = c[1]
		try:
			bpy.utils.unregister_class(cls)
		except Exception as e:
			print(e)
			
if __name__ == "__main__":
	register()
