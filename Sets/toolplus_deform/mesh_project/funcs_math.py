
import sys

from math import *
from mathutils import *

class Point :
	"""
	Point containing integers
	"""
	def __init__(self, x, y) :
		self.X = x
		self.Y = y
	def __str__(self) :
		return "<Point (%d, %d)>" % (self.X, self.Y)

def clamp(value) :
	"""
	Clamp value to 0-1 range
	"""
	return min(max(value,0), 1)

def lerp(a, b, factor) :
	"""	Lerp between value a->b with specified factor
	"""
	return (1-factor) * a + factor * b
def lerpVector(vec0, vec1, amount) :
	"""	
	Lerp between the two vectors
	vec0, vec1:	Vectors lerped with 0 = vec0 and 1 = vec1
	amount:		Lerp amount
	"""
	return vec0 + (vec1 - vec0) * amount 

def findMinMax(mesh) :
	"""	
	Find the minimum and maximum point in the mesh
	Returns (min, max)
	"""
	vMin = Vector((sys.float_info.max, sys.float_info.max, sys.float_info.max))
	vMax = Vector((-sys.float_info.max, -sys.float_info.max, -sys.float_info.max))
	for vert in mesh.verts:
		vMin = minVec(vert.co, vMin)
		vMax = maxVec(vert.co, vMax)
	return (vMin, vMax)
		
def minVec(v0, v1) :
	"""	Compare and return the minimal vector combination:
	"""
	vLen = min(len(v0), len(v1))
	v = Vector((0,)*vLen)
	for i in range(vLen) :
		v[i] = min(v0[i], v1[i])
	return v
def minVec_x3(v0, v1, v2) :
	"""	Compare and return the minimal vector combination:
	"""
	vLen = min(len(v0), len(v1), len(v2))
	v = Vector((0,)*vLen)
	for i in range(vLen) :
		v[i] = min(v0[i], v1[i], v2[i])
	return v

def maxVec(v0, v1) :
	"""	Compare and return the maximal vector combination:
	"""
	vLen = min(len(v0), len(v1))
	v = Vector((0,)*vLen)
	for i in range(vLen) :
		v[i] = max(v0[i], v1[i])
	return v
def maxVec_x3(v0, v1, v2) :
	"""	Compare and return the maximal vector combination:
	"""
	vLen = min(len(v0), len(v1), len(v2))
	v = Vector((0,)*vLen)
	for i in range(vLen) :
		v[i] = max(v0[i], v1[i], v2[i])
	return v
	
def rotateVec2(vec, angle) :
	"""	Rotate CCW by angle
	"""
	theta = radians(angle);
	cs = cos(theta);
	sn = sin(theta);
	return Vector((vec.x * cs - vec.y * sn, vec.x * sn + vec.y * cs))

def orthoNormalizeVec2(vecA, vecB) :
	"""	
	Ortho-normalize the vectors using Gram-Smith. 	
	Making vecB orthogonal to vecA (and  vice versa) and normalize both.
	Returns: Touple of the vectors in same order.
	"""
	vecA.normalize()
	vecB = vecB - vecB.dot(vecA) * vecA
	return (vecA, vecB / vecB.length)

def orthoNormalizeVec3(vecA, vecB, vecC) :
	"""	
	Ortho-normalize the vectors using Gram-Smith. 	
	Returns: Touple of the vectors in same order.
	"""
	vecA.normalize()
	vecB = vecB - vecB.dot(vecA) * vecA
	vecB /= vecB.length
	
	vecC = vecC - vecC.dot(vecB) * vecB - vecC.dot(vecA) * vecA
	vecC /= vecC.length
	return (vecA, vecB, vecC)

#Return the signed component of the value:
def sign(value):
	if value > 0 :
		return 1
	elif value < 0 :
		return -1
	return 0
	
def scaleMatrix(scaleVec, size = 4) :
	"""
	Generate a scaling matrix from a vector defining the scale on each axis
	"""
	mat = Matrix.Identity(size)
	mat[0].x = scaleVec.x
	mat[1].y = scaleVec.y
	if size > 2 :
		mat[2].z = scaleVec.z
	return mat
	
def distanceEdge(e0, e1, point) :
	"""
	Returns the distance to a line segment defined between two points and a point in space
	e0,e1:	Two points defining the segment
	point:	Point in space to check distance to
	"""
	point = point - e0
	segment = e1 - e0
	t = segment.dot(point) / segment.dot(segment)
	if t < 0 : #Point "behind" segment
		return point.length
	if t > 1 : #Point "passed" segment
		return (point - e1).length
	#Line is closest:
	return (point - t * segment).length
	