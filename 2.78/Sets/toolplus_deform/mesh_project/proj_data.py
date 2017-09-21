#  proj_data.py (c) 2016 Mattias Fredriksson
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####
import bpy, bmesh

from math import *
from mathutils import *
from .funcs_tri import *
from .funcs_math import *
from .funcs_blender import *
from .bound import *
from .partition_grid import *

class Setting :
	"""
	Static variables related to the script, set from the blender settings on main class execution.
	Functions call them statically since they are not related to the main class object.
	May not be the best solution but it works!
	"""
	bias = 0.00001
	smooth = True
	scalar = Vector((1,1,1))
	moveXY = Vector((0,0))
	rotation = 0
	depth = 0
	proj_type = None
	keepRelative = False
	partitions_per_face = 0.25
	
	def __init__(self) :
		self.bias = Setting.bias
		self.smooth = Setting.smooth
		self.scalar = Setting.scalar
		self.moveXY = Setting.moveXY
		self.rotation = Setting.rotation
		self.depth = Setting.depth
		self.proj_type = Setting.proj_type
		self.keepRelative = Setting.keepRelative
		self.partitions_per_face = Setting.partitions_per_face
	
	def copy() :
		"""	Return a copy of the settings
		"""
		return Setting()

class SourceMeshData :
	"""	Object containing the projection information of a single mesh object
	"""
	def __init__(self, bmesh, object, bounds) :
		#Source mesh, defines the original mesh transformed into the "projection basis"
		self.bmeshSource = bmesh
		#The target bmesh, transformed on every execute
		self.bmesh = bmesh.copy()
		self.bounds = bounds
		self.ob_name = object.name

class ProjectionData :
	""" Object creating and storing the projection information
	"""

	def __init__(self, ob_target, cameraRotInv, cameraAxis, cameraPos, ortho, warning) :
		#Use name for comparison objects will corrupt between execute calls
		self.target_ob = ob_target.name
		self.cameraRotInv = cameraRotInv
		self.cameraAxis = cameraAxis
		self.cameraPos = cameraPos
		self.ortho = ortho
		self.warning = warning
	
	def free(self) :
		self.bmesh.free()
		self.free_source(self)
	def free_source(self) :
		for meshData in self.meshList :
			meshData.bmesh.free()
			meshData.bmeshSource.free()
	
	def generateTargetData(self, object, context) :
		"""	Generates projection information for the target mesh
		"""
		if object is None :
			self.warning.report({'ERROR'}, "No active mesh object found to use as projection target.")
			return False
		elif object.type != 'MESH':
			self.warning.report({'ERROR'}, "Active object was not a mesh. Select an appropriate mesh object as projection target")
			return False
		#Create a bmesh copy to project on with the modifiers applied and vertices in world space !
		self.bmesh = createBmesh(object, object.matrix_world, True, context.scene, True)
		#Find active uv layer ID and generate a grid for the uv map:
		self.uv_lay = getUVKey(self.bmesh)
		if self.uv_lay is None :
			self.warning.report({'ERROR'}, "No active UV layer found on the target surface. Make sure there is an unwrapped UV Map available to project on.")
			return False
		#Create a bvh tree of the bmesh, used for specific projection calls.
		self.bvh = bvhtree.BVHTree.FromBMesh(self.bmesh, epsilon = Setting.bias)
		#Generate partition grid
		self.uv_grid = PartitionGrid2D.from_bmesh_uv(self.bmesh, self.uv_lay, 1 / Setting.partitions_per_face , Setting.bias)
		return True
	
	def ray_cast_target(self, origin, maxDist = 10000) :
		"""	
		Cast a ray on the target mesh BVH tree.
		Returns the bmesh face, distance and the barycentric coordinates of intersection
		"""
		(loc, nor, ind, dist) = self.bvh.ray_cast(origin, self.getCameraAxis(origin), maxDist)
		if loc is None :
			return (None, None, None)
		#Calculate the barycentric coordinates with the rayTri intersection method
		(valid, u, v, w) = pointInTriangle(loc, self.bmesh.faces[ind].verts[0].co, self.bmesh.faces[ind].verts[1].co, self.bmesh.faces[ind].verts[2].co)
		if not valid :
			return (None, None, None)
		return (self.bmesh.faces[ind], dist, Vector((u,v,w)))
	
	def generateSourceData(self, ob_list, scene) :
		"""
		Generate the oriented bmesh and pre-calculate the projection information for a list of objects that should be projected
		ob_list: list of objects containing the meshes that should be projected
		"""
		meshList = []
		for ob in ob_list : 
			if ob.type == 'MESH' and ob.name != self.target_ob :
				data = self.createSourceBmesh(ob, scene)
				if data is not None :
					meshList.append(data)
		self.meshList = meshList	
		return True
	
	def createSourceBmesh(self, object, scene):
		"""	Function that calculates the bmesh of a mesh object to be projected onto the target
		"""
		#Find the orientation basis of the projected mesh aligned with camera view:
		loc, meshRot, sca = object.matrix_world.decompose()
		meshRot = meshRot.to_matrix()
		#
		if Setting.proj_type == 'ZISUP' :
			rot = Matrix.Identity(3)
			axis = zUpFindAxis(meshRot.transposed(), self.cameraAxis)
		elif Setting.proj_type == 'CAMERA' :
			rot = self.cameraRotInv * meshRot
			axis = self.cameraAxis.copy()
		elif Setting.proj_type == 'AXISALIGNED' or Setting.proj_type is None :
			rot, axis = axisAlignRotationMatrix(self.cameraRotInv * meshRot,  meshRot.transposed())
		
		#Create a bm mesh copy of the mesh!
		bmesh = createBmesh(object, (rot * scaleMatrix(sca, 3)).to_4x4())
		#Calculate bounds
		bounds = self.calculateBounds(bmesh, axis, object.location, object.name)
		if bounds is None :
			return None
		return SourceMeshData(bmesh, object, bounds)
	
	def projectMeshData(self, context) :
		"""
		Function projecting each mesh using the gathered data and updates the mesh object.
		"""
		obList = []
		#Loop over the gathered mesh data and start projecting it
		for meshData in self.meshList :
			if meshData.bounds == None :
				return 0
			#Copy and transform the bounds to the settings
			bounds = meshData.bounds.copy()
			if Setting.keepRelative :
				bounds.ensureMeshRatio()
			bounds.move(Setting.moveXY)
			bounds.rotate(Setting.rotation)
			bounds.scale(Setting.scalar.xy)
						
			bmesh = meshData.bmesh
			
			i = 0
			count_success = 0 #Keeps track of successfull verts projected
			count_partial = 0 
			for vert in bmesh.verts :
				(face, success, partial_success) = self.projectVert(vert, meshData.bmeshSource.verts[i], bounds)
				count_partial += partial_success
				count_success += success
				i += 1
			
			#Finalize the projection by assigning the bmesh into the blender object 
			#Validate one vert was projected first:
			if count_success > 0 :
				ob = setNamedMesh(bmesh, meshData.ob_name, context.scene, Matrix.Identity(4))
				#createMesh(meshData.bmeshSource, context.scene)
				obList.append(ob)
				blen = len(bmesh.verts)
				if blen - count_partial != 0:
					self.warning.report({'WARNING'}, "Mesh: %s has %d vertices that did not project succesfully and are selected. Verify no holes in UV map or try lowering target mesh density" %(meshData.ob_name, blen - count_partial))
				if blen - count_success != 0:
					self.warning.report({'WARNING'}, "Mesh: %s has %d vertices that failed to be projected. Validate that the target uv map covers the projection area" %(meshData.ob_name, blen - count_success))
			#No vert was projected
			else :
				self.warning.report({'WARNING'}, "Mesh: %s could not be projected." %meshData.ob_name)
		#Finally set the origin to geometry
		#origin_to_geometry(obList)
			
	def projectVert(self, vert, vertSource, bounds) :
		"""	Calculate the projection of a single vert (also sets the vert.co)
		vert:		Vert being updated
		vertSource:	Vert in the "projection basis", unpoluted from any changes.
		bounds:		The projection target data
		"""
		
		#Find the uv coordinates by comparing the vertex position to the mesh bounds.
		#The relation is then compared to the uv map target
		uv = bounds.calcUVPoint(vertSource.co)
		(intersect, uvw, face) = self.uv_grid.trace_point_uv(uv.xy)
		#If intersection occured project it
		if intersect:
			vert.co = calcVertProjPoint(face, uvw, uv.z * Setting.scalar.z)
			vert.select_set(False)
			return (face, True, True)
		#If no intersection use the closest tri in the triangle
		else :
			(dist, face, edge, uvw) = self.uv_grid.trace_close_uv(uv.xy)
			vert.select_set(True)
			if face is None : #No face in partition
				return (face, False, False)
			vert.co = calcVertProjPointClamp(face, uvw, uv.z * Setting.scalar.z)
			return (face, True, False)
	
	
	#Find the bounds of a specified mesh
	def calculateBounds(self, mesh, alignedAxis, meshPos, meshName) :
		"""
		Calculates the projection target area and the mesh source box.
		mesh:			The source mesh being projected
		alignedAxis: 	The axis that defines the min/max area
		meshPos:		The mesh center point in world coordinates.
		meshName:		Mesh name, used to print warning info
		"""
		#Min/Max box of the mesh
		(vMin, vMax) = findMinMax(mesh)
		center = (vMax - vMin) * 0.5 + vMin
		
				
		#Calculate the corners of the mesh in the basis aligned with view rotation (note* inverted Z). 
		#Currently the points will be slightly distorted, as the mesh on screen is not algined with camera (A axis alignment is applied)
		#To fix this the rotation difference between camera and mesh origin could be applied to the min/max projection points (not bounds!)
		#Note* only orthographic support for now
		corners = []
		corners.append(vMin.x * alignedAxis[0] + vMax.y * alignedAxis[1] + meshPos)	#topL
		corners.append(vMax.x * alignedAxis[0] + vMax.y * alignedAxis[1] + meshPos)	#topR
		corners.append(vMax.x * alignedAxis[0] + vMin.y * alignedAxis[1] + meshPos)	#botR
		corners.append(vMin.x * alignedAxis[0] + vMin.y * alignedAxis[1] + meshPos)	#botL
		
		#Project center point onto target and calculate the texture coordinates of the intersection point:
		(cFace, dist, uvw) = self.ray_cast_target(meshPos)
		if cFace == None :
			self.warning.report({'WARNING'}, "Mesh: %s center point did not project onto the target" %(meshName))
			return None
		centerTex = averageTexCoord(cFace, uvw, self.uv_lay)
		
		#Project the corners onto target uvmap and get texcoord min/max bounds the mesh will be projected between:
		for i in range(len(corners)):
			#Tries to find a projection onto the target mesh for a corner
			corners[i] = self.traceUVTarget(corners[i], meshPos, centerTex)
			if corners[i] == None :
				self.warning.report({'WARNING'}, "Mesh: %s could not project onto the target properly. Verify that target area is uv mapped or that mesh is between the camera and target" %(meshName))
				return None
		#Calculate and return bounds:
		bound = Bounds.From_Corners(corners[0], corners[1], corners[2], corners[3], centerTex, vMin, vMax)
		if bound is None:
			self.warning.report({'WARNING'}, "Mesh: %s projection target area is 0, verify the uv map and that the mesh is projected onto the target object" %(meshName))
		return bound
	
	def getCameraAxis(self, target) :
		"""	Calculates the projection ray direction
		"""
		if self.ortho :
			return self.cameraAxis[2]
		else :
			dir = target - self.cameraPos
			dir.normalize()
			return dir
	
	def traceUVTarget(self, corner, centerPos, centerTex) :
		"""
		Function tracing rays from positions between the mesh corner and it's center to
		find the uv map relation the corner should be projected onto.
		The function starts by tracing at the corner and if failed, it continues to trace at
		the halfway mesh center halway point.
		If a trace is successfull and is not first, the relation between the found uv coordinates, 
		"halway" and center point is assumed equal to the scalar applied to the mesh halfway point
		corner:		One of the mesh corners to trace from
		centerPos:	The center position of the mesh
		centerTex:	Uv coordinate from the successfully traced center position
		"""
		for x in range(5) :
			mult = pow(0.5, x)
			#Calculate the point between corner and center for this trace:
			trace_pos = (corner - centerPos) * mult + centerPos
			(face, dist, uvw) = self.ray_cast_target(trace_pos)
			if face != None and uv_Area(face, self.uv_lay) > 0:
				tex = averageTexCoord(face, uvw, self.uv_lay)
				#Scale the result back by assuming the relation on the uv map and mesh is identic:
				return (tex - centerTex) / mult + centerTex
		return None
def calcVertProjPoint(face, uvw, depth) :
	"""	
	Calculate the resulting projection point of a vertice being projected onto a face with the barycentric weights
	face:	The face containing the triangle information
	uvw:	The barycentric weights, defining how much each tri corner influences the vertex
	depth:	The distance of the vertex from the plane defined by the tri
	"""
	depth += Setting.depth
	co = averageCo(face, uvw)
	if Setting.smooth :
		return co + averageNorm(face, uvw) * depth
	else :
		return co + face.normal * depth
def calcVertProjPointClamp(face, uvw, depth) :
	"""	
	Calculate the resulting projection point of a vertice being projected onto a face with the barycentric weights
	face:	The face containing the triangle information
	uvw:	The barycentric weights, defining how much each tri corner influences the vertex
	depth:	The distance of the vertex from the plane defined by the tri
	"""
	depth += Setting.depth
	co = averageCo(face, uvw)
	if Setting.smooth :
		uvw.x = clamp(uvw.x)
		uvw.y = clamp(uvw.y)
		uvw.z = clamp(uvw.z)
		return co + averageNorm(face, uvw) * depth
	else :
		return co + face.normal * depth

def zIsUp(rotMat, camAxis) :
	""" 
	Special funcition that keeps the Z axis of the mesh as the depth component but rotates the mesh along x & y axis
	"""
	plane_x = camAxis[2].dot(rotMat[0]) * camAxis[2] + rotMat[0]
	plane_y = camAxis[2].dot(rotMat[1]) * camAxis[2] + rotMat[1]
	plane_x.normalize()
	plane_y.normalize()
	plane_x = Vector((plane_x.dot(rotMat[0]),plane_x.dot(rotMat[1]),0))
	plane_y = Vector((plane_y.dot(rotMat[0]),plane_y.dot(rotMat[1]),0))
	
	rotMat[2], rotMat[0], rotMat[1] = orthoNormalizeVec3(Vector((0,0,1)), plane_x, plane_y)
	return rotMat

def zUpFindAxis(meshAxis, camAxis) :
	"""	Finds the mesh X,Y axis best aligned with camera view to determine the basis used to place the mesh on the surface (ensures matrix orientation)
	"""
	xDot = meshAxis[0].dot(camAxis[2])
	yDot = meshAxis[1].dot(camAxis[2])
	zDot = meshAxis[2].dot(camAxis[2])
	
	ret = meshAxis.copy()
	if abs(xDot) > max(abs(yDot), abs(zDot)) :
		ret[0] = meshAxis[2] * sign(xDot)
		ret[1] = meshAxis[1]
	elif abs(yDot) > abs(zDot) :
		ret[0] = meshAxis[0]
		ret[1] = meshAxis[2] * sign(yDot)
	else :
		ret[0] = meshAxis[0] * -sign(zDot)
		ret[1] = meshAxis[1]
	return ret
	
	

def axisAlignRotationMatrix(rotMat, meshRot) :
	"""	Align the rotation matrix to the closest world axes and allows organizing a matrix with the same scrabled axis order.
	"""
	rot = meshRot.copy()
	rotMat[0].xyz, rot[0]  = findAxisAlignment(rotMat[0], meshRot)
	rotMat[1].xyz, rot[1] = findAxisAlignment(rotMat[1], meshRot)
	rotMat[2].xyz, rot[2] = findAxisAlignment(rotMat[2], meshRot)
	return rotMat, rot
	
def findAxisAlignment(axis, axisMat) :
	""" 
	Finds the largest component of the axis and returns it as a axis aligned unit vector.
	Also identifies the the relative axis index.
	"""
	if abs(axis[0]) > max(abs(axis[1]), abs(axis[2])) :
		s_val = sign(axis[0])
		return Vector((s_val,0,0)), axisMat[0] * s_val
	elif abs(axis[1]) > abs(axis[2]) :
		s_val = sign(axis[1])
		return Vector((0,s_val,0)), axisMat[1] * s_val
	s_val = sign(axis[2])
	return Vector((0,0,s_val)), axisMat[2] * s_val
	