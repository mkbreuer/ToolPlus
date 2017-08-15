import sys
from math import *
from mathutils import *

class TriBias :
	bias = 0.00001

def averageTexCoord(triFace, uvw, uv_lay) :
	""" Calculates the Texture UV coordinates from the specified barycentric coords
	"""
	uv = triFace.loops[0][uv_lay].uv * uvw[0]
	uv += triFace.loops[1][uv_lay].uv * uvw[1]
	uv += triFace.loops[2][uv_lay].uv * uvw[2]
	return uv

def uv_Area(triFace, uv_lay) :
	"""	Calculates the uv triangle area
	"""
	p0 = triFace.loops[0][uv_lay].uv
	#Calculate: edge.length * edge.length * 0.5
	return (triFace.loops[1][uv_lay].uv - p0).length * (triFace.loops[2][uv_lay].uv - p0).length * 0.5 

def averageNorm(face, uvw) :
	"""	Calculates the average normal of a point in the face using the specified barycentric coordinates
	"""
	nor = face.verts[0].normal * uvw.x + face.verts[1].normal * uvw.y + face.verts[2].normal * uvw.z
	nor.normalize()
	return nor

def averageCo(face, uvw) :
	"""	Calculates the average point in the face using the specified barycentric coordinates
	"""
	return face.verts[0].co * uvw.x + face.verts[1].co * uvw.y + face.verts[2].co * uvw.z

def pointInTriangle(point, p0,p1,p2) :
	"""
	Checks if the point is in the triangle, both must be in the same plane
	Returns true/false and the barycentric coordinates
	"""
	v0 = p1-p0
	v1 = p2-p0
	v2 = point - p0
	
	d00 = v0.dot(v0)
	d01 = v0.dot(v1)
	d11 = v1.dot(v1)
	d20 = v2.dot(v0)
	d21 = v2.dot(v1)
	
	invDenom = 1.0 / (d00 * d11 - d01 * d01)
	
	v = (d11 * d20 - d01 * d21) * invDenom
	w = (d00 * d21 - d01 * d20) * invDenom
	u = 1.0 - v - w
	return (u > 0 and v > 0 and w > 0, u,v,w)

def rayTriIntersection(origin, dir, mTri):
	"""
	Calculates if a ray intersects the triangle and returns the barycentric coordinates:
	#(func not verified)
	#origin
	"""
	p0 = mTri.verts[0].co
	e1 = mTri.verts[1].co - p0
	e2 = mTri.verts[2].co - p0
	
	q = dir.cross(e2)
	#Find the squared area of the triangle:
	a = e1.dot(q)
	#Avoid division by 0, triangles without area
	if a > -TriBias.bias and a < TriBias.bias :
		return None
	#Pre-divide the area, the u,v area calculations can then be multiplied to find the area partition
	f = 1 / a
	s = origin - p0
	#Calculate the barycentric coordinate by calculating the squared area of u
	u = f * s.dot(q)
	if u < 0 :
		return None #No intersection!
	#Calculate v partition
	r = s.cross(e1)
	v = f * d.dot(r)
	if v < 0 or u + v > 1 :
		return None #No intersection!
	#Find w, since u and v are signed inward the area they represented is inside the triangle
	#Thus w can be found by subtraction:
	w = 1 - u - v
	#Intersection distance:
	t = f * e2.dot(r)
	return (t, Vector(u,v,w))
	
def calculateBarycentricCoord2D(v0,v1,v2, point) :
	"""
	Calculates the barycentric coordinates from a triangle in 2D space
	v0,v1,v2:	The three points of the triangle
	point:		The point that should be tested with the triangle
	Return: Touple with bool if point is inside triangle, then vector containing the uvw barycentric coordinates.
	"""
	e0 = v1-v0
	e1 = v2-v0
	e2 = point - v0
	
	d = (e0.x * e1.y - e1.x * e0.y)
	if  d > -TriBias.bias and d < TriBias.bias :
		return (False, Vector((0,)*3))
	d = 1 / d
	v = (e2.x * e1.y - e1.x * e2.y) * d
	w = (e0.x * e2.y - e2.x * e0.y) * d
	u = 1 - v - w
	return (u > 0 and v > 0 and w > 0, Vector((u,v,w)))
	
	
def separatingTriAxis2D(tri_a0, tri_a1, tri_p, pList) :
	"""
	Separating axis function calculating if a set of points is separated from a axis segment
	tri_a0, tri_a1:	First 2 points in triangle defining the axis edge
	tri_p:			Third point in triangle
	pList:			List of 2D points that should be separated on the defined axis 
	Return:			True if the points intersect over the axis segment
	"""
	#Calculate the axis and the "segment" the axis points overlap:
	axis = tri_a1 - tri_a0;
	axis.x, axis.y = -axis.y, axis.x #Take the normal of the axis
	dot_inv = axis.dot(axis) #Axis dot 
	if dot_inv == 0 :
		return False #Axis has length ~0
	dot_inv = 1 / dot_inv #Inverse
	
	#Project one of the points generating axis (Note! only one needed):
	proj = axis.dot(tri_a0)
	pa_min =  proj * dot_inv #Project point distance on axis
	
	#Project the third point on the triangle:
	proj = axis.dot(tri_p)
	pa_max =  proj * dot_inv #Project point distance on axis
	
	
	#Swap if necessary: Finding min/max span of tri on axis
	if pa_max < pa_min :
		pa_max, pa_min = pa_min, pa_max
	
	
	#Calculate the segment on the axis the points overlap
	pp_min = sys.float_info.max
	pp_max = sys.float_info.min
	for p in pList :
		proj = axis.dot(p)
		pp =  proj * dot_inv #Project point distance on axis: squared length
		pp_min = min(pp_min, pp)
		pp_max = max(pp_max, pp)
	
	#Check if the points overlapps the axis "segment":
	return pp_min <= pa_max and pp_max >= pa_min
	
def	collideTriAARect2D(p0, p1, p2, rectMin, rectMax) :
	"""
	Function checking if a tri intersects a AxisAligned rectangle using the separating axis theorem
	p0,p1,p2:	2D points defining the triangle
	rectMin:	Point defining the min point in the rectangle
	rectMax:	Point defining the max point in the rectangle
	"""
	minT = minVec(p0, p1,p2)
	maxT = maxVec(p0,p1,p2)
	#If the vectors projected on the X axis do not overlap we have no collision:
	if not (rectMin.x <= maxT.x and rectMax.x >= minT.x) :
		return False;
	#If the vectors projected on the Y axis do not overlap we have no collision:
	if not (rectMin.y <= maxT.y and rectMax.y >= minT.y) :
		return False;

	#Create a set of points from the four corners of the rectangle:
	pset = (Vector((rectMax.x, rectMin.y)), 
			Vector((rectMin.x, rectMin.y)),
			Vector((rectMax.x, rectMax.y)),
			Vector((rectMin.x, rectMax.y)))
	#Check for a separating axis on the triangle!
	return separatingTriAxis2D(p0, p1, p2, pset) and separatingTriAxis2D(p1, p2, p0, pset) and separatingTriAxis2D(p2, p0, p1, pset)