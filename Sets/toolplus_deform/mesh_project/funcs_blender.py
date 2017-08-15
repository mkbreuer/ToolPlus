
import bpy, bmesh
from math import *
from mathutils import *

def findViewRotation(context) :
	"""
	Function that finds the camera orientation from a 3D view context
	Fetches the right-handed orientation matrix from the quaternion (axis is not aligned with camera directions)
	"""
	if context.area.type == 'VIEW_3D':
		cQuat = context.area.spaces[0].region_3d.view_rotation
		return cQuat.to_matrix()
	return Matrix.Identity(3)		
		
def findViewAxis(context) :
	"""
	Function that finds the camera right/up/forward axis from a 3D view context
	"""
	m = Matrix.Identity(3)
	if context.area.type == 'VIEW_3D':
		cQuat = context.area.spaces[0].region_3d.view_rotation
		m[1] = cQuat * Vector((0,1,0))
		m[2] = cQuat * Vector((0,0,-1))
		m[1].normalize()
		m[2].normalize()
		m[0] = m[2].cross(m[1]).normalized()
	return m
	
def findViewForward(context) :
	"""
	Function that finds the camera orientation from a 3D view context
	"""
	if context.area.type == 'VIEW_3D':
		cQuat = context.area.spaces[0].region_3d.view_rotation
		#Return camera rot as 4x4 matrix:
		return cQuat * Vector((0,0, -1))
	return Vector((0,0, -1))
def findViewPos(context) :
	"""
	Function that finds the camera position from a 3D view context
	"""
	if context.area.type == 'VIEW_3D':
		#Return camera position
		return context.area.spaces[0].region_3d.view_location + findViewForward(context) * -1 * context.area.spaces[0].region_3d.view_distance
	return Vector((0,0, 0))

def getUVKey(bmesh) :
	"""
	Fetches the UV layer key from a bmesh
	"""
	return bmesh.loops.layers.uv.active
	
def viewTypeOrtho(context) :
	""" Returns True if camera mode is orthographic
	"""
	#C.screen.areas[2].spaces[0].region_3d.view_perspective
	if context.area.type == 'VIEW_3D':
		return context.area.spaces[0].region_3d.view_perspective == 'ORTHO'
	return False
def viewTypePersp(context) :
	""" Returns True if camera mode is perspective
	"""
	if context.area.type == 'VIEW_3D':
		return context.area.spaces[0].region_3d.view_perspective == 'PERSP'
	return False

def createBmesh(ob = None, matrix = None, triangulate = False, scene = None, applyModifier = False) :
	"""
	Create a bmesh from a mesh object.
	ob: 			Object to create the bmesh from (should be type = 'Mesh')
	matrix:			Transformation matrix applied to the verts, if None verts originates from origo (Default: None)
	triangulate:	True if the mesh faces should be triangulated (Default: False)
	scene:			Scene related to the object, required if modifiers is applied (Default: None)
	applyModifier:	True if modifiers should be applied to the mesh, scene req. (Default: False)
	Return:			A bmesh object, if no mesh object sent it is empty.
	"""

	bm = bmesh.new()
	
	if ob is not None and ob.type == 'MESH' :
		if applyModifier and scene is not None:
			bm.from_object(ob, scene)
		else :
			bm.from_mesh(ob.data)
		#Transform verts to specified basis:
		if matrix is not None:
			bm.transform(matrix)
		#Triangulate the faces!
		if triangulate :
			bmesh.ops.triangulate(bm, faces = bm.faces)
		
		#Some derp functions we need to call to use lists:
		bm.verts.ensure_lookup_table()
		bm.edges.ensure_lookup_table()
		bm.faces.ensure_lookup_table()

	return bm

def createEmptyMeshCopy(ob, context, obTag = "_Copy", meshTag = "_CopyMesh", copyTransform = True):
	"""
	Create a empty mesh copy of the object, creating a object without mesh data.
	ob:			Object to copy
	context:		Context the object is linked to (visible)
	obTag:			String appended to the name of the copied objects.
	meshTag:		String appended to the name of the contained mesh object created (appended to ob name).
	copyTransform:	True if object transform is applied to the mesh (Default: True)
	Return:		A blender object 
	"""
	
	#Creates a copy of a mesh with relevant data, if the object is not a mesh an empty mesh will be returned.
	
	mesh = bpy.data.meshes.new(ob.name + meshTag) 		# create a new mesh with the name
	newOb = bpy.data.objects.new(ob.name + obTag, mesh)	# create an object with that mesh
	if	copyTransform :
		newOb.matrix_world = ob.matrix_world			# Copy the transformation matrix of the object 

	#If object is not a mesh return the empty
	if ob.type != 'MESH':
		return newOb
	# Link object to the scene
	if context is not None :
		context.scene.objects.link(newOb)
	#Copy modifiers:
	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = ob
	newOb.select = True
	bpy.ops.object.make_links_data(type='MODIFIERS')  						
	return newOb

def createMesh(bmesh, scene = None, matrix = None, name = "Object") :
	"""
	Create a blender mesh object from a specified bmesh and context
	bmesh:		Mesh to create a object for
	scene:		Scene the new object will be added to
	name:		Name of the object added 
	"""
	mesh = bpy.data.meshes.new(name + "_Mesh") 		# create a new mesh with the name
	newOb = bpy.data.objects.new(name, mesh)	# create an object with that mesh
	if matrix is not None :
		newOb.matrix_world = matrix
	#Link to scene
	if scene is not None :
		scene.objects.link(newOb)         	
	bmesh.to_mesh(newOb.data)					
	return newOb
	
def setMesh(bmesh, ob, matrix = None) :
	""" Update a mesh from a bmesh object
	"""
	#Before setting mesh data assign matrix:
	if matrix is not None :
		ob.matrix_world = matrix
	bmesh.normal_update()
	bmesh.to_mesh(ob.data)
	return ob
def setNamedMesh(bmesh, object_name, scene = None, matrix = None) :
	""" Update a mesh from a bmesh object name
	"""
	try :
		ob = getObject(object_name)
		#Before setting mesh data assign matrix:
		if matrix is not None :
			ob.matrix_world = matrix
		bmesh.normal_update()
		bmesh.to_mesh(ob.data)
		return ob
	except :
		return createMesh(bmesh, scene, object_name)

def verify_list(object) :
	""" Creates a list of a object
	"""
	try :
		return list(object)
	except :
		list = []
		list.append(object)
		return list
def origin_to_geometry(object) :
	""" Sets the origin of specified objects
	"""
	#Generate a context with ObjectBase elems that is being operated on:
	#ob_list =  verify_list(object)
	#tmpContext = {'visible_objects': ob_list}
	#Call operator
	bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY')
	
def getObject(object_name, scene = None) :
	""" Fetch a object from it's name
	"""
	if scene is None :
		return bpy.data.objects[object_name]
	return scene.objects[object_name]
	
def deleteObject(object, scene) :
	""" Delete a blender object that is visible in the specified scene
	"""
	scene.objects.unlink(object)
	bpy.data.objects.remove(object)