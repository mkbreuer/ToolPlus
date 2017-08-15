#  partition_grid.py (c) 2016 Mattias Fredriksson
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

import sys
from math import *
from mathutils import *
from .funcs_tri import *
from .funcs_math import *

class GridRect :
	"""
	A grid partition rectangle. Contains it's boundaries and a set of objects contained/intersecting the grid partition
	"""
	def __init__(self, rect) :
		self.list = []
		self.rect = rect
		self.corners = (rect[0], Vector((rect[0].x, rect[1].y)), rect[1], Vector((rect[1].x, rect[0].y)))
		
	def	separatingTriAxis(self, p0, p1, p2) :
		"""
		Specified separating axis function only checking separation on triangle edges
		p0,p1,p2:	2D points defining the triangle
		Returns: True if intersection
		"""
		#Check for a separating axis on the triangle!
		return separatingTriAxis2D(p0, p1, p2, self.corners) and separatingTriAxis2D(p1, p2, p0, self.corners) and separatingTriAxis2D(p2, p0, p1, self.corners)
	def append(self, obj) :
		"""
		Append a object to the contain/intersect list
		"""
		self.list.append(obj)
	
class  PartitionGrid2D :
	"""
	Partition grid generating a 2D matrix of partitions over a defined area.
	Each partition will then contain a set of objects defined by the use case of the grid.
	Note* 	Semi-Dynamic object for now, it can only hold faces representing a uv map. 
			Functions is semi-designed to hold any type of 2D triangles but it needs a fetch, create & append methods for specific case.
	"""
	
	def __init__(self, partitions, minVec, maxVec) :
		"""
		Initiate the partition grid from the values
		partitions: Point containing number of partitions on X & Y axis (Integers)
		minVec:		Minimum point of the grid
		maxVec:		Maximum point of the grid
		"""
		self.maxP = maxVec
		self.minP = minVec
		self.size = maxVec - minVec
		#Vector containing number of partitions on x, y axis
		self.partitions = partitions
		#Size of a grid partition rectangle
		self.part_size = Vector((self.size.x / partitions.X, self.size.y / partitions.Y))
		#Generate partition grid:
		self.grid = [[GridRect(self.grid_rect(x,y)) for x in range(partitions.X)] for y in range(partitions.Y)] 
		
	def calcIndex(self, point) :
		"""
		Calculates the grid index from a point
		"""
		return Point(floor((point.x - self.minP.x) / self.part_size.x), floor((point.y - self.minP.y) / self.part_size.y))
	def clampIndex(self, point) :
		""" 
		Clamps a grid index to the grid ensuring it fits.
		"""
		if point.X < 0 :
			point.X = 0
		if point.Y < 0 :
			point.Y = 0
		if point.X >= self.partitions.X :
			point.X = self.partitions.X - 1
		if point.Y >= self.partitions.Y :
			point.Y = self.partitions.Y - 1
		return point
	def grid_rect(self, ind_x, ind_y) :
		"""
		Calculates the min, max point of a grid square related to origo
		Returns a touple of two vectors defining the (min, max) points
		"""
		rectMin = Vector((ind_x * self.part_size.x, ind_y * self.part_size.y)) + self.minP
		return (rectMin, rectMin + self.part_size)
	
	def in_grid(self, index) :
		"""
		Function that verifies that a grid index is inside the grid
		"""
		return index.X >= 0 and index.Y >= 0 and index.X < self.partitions.X and index.Y < self.partitions.Y
		
	def append_uv(self, face) :
		"""
		Append a triangle definined by the three points
		face:		The face reference the triangles is related to
		"""
		p0, p1, p2 = face.loops[0][self.uv_lay].uv, face.loops[1][self.uv_lay].uv, face.loops[2][self.uv_lay].uv
		minP = self.calcIndex(minVec_x3(p0,p1,p2)) 
		maxP = self.calcIndex(maxVec_x3(p0,p1,p2))
		#Loop through each grid partition the overlap on x,y axis.
		#If it also overlap on the three triangle edge axis it intersect the partition:
		for y in range(minP.Y, maxP.Y + 1) : #+1 because range does: [min, max)
			for x in range(minP.X, maxP.X + 1) :
				if self.grid[y][x].separatingTriAxis(p0,p1,p2) :
					self.grid[y][x].append(face)
					
	def trace_point_uv(self, point_uv) :
		"""
		Function that trace intersection between a point and uv face in the grid.
		Returns: Touple with bool for intersection + uvw coordinates and the face if intersection occured
		"""
		ind = self.calcIndex(point_uv)
		if self.in_grid(ind) :
			for face in self.grid[ind.Y][ind.X].list :
				#Verify intersection result
				(intersect, uvw) = calculateBarycentricCoord2D(face.loops[0][self.uv_lay].uv, face.loops[1][self.uv_lay].uv, face.loops[2][self.uv_lay].uv, point_uv)
				if intersect :
					return (intersect, uvw, face)			
		#Either outside the grid or no face found to intersect with:
		return (False, None, None)
	def trace_close_uv(self, point_uv) :
		"""
		Traces the closest edge to the point in the grid partition specified by the point
		"""
		ind = self.calcIndex(point_uv)
		dist = sys.float_info.max
		edge = None
		calc_face = None
		if self.in_grid(ind) :
			for face in self.grid[ind.Y][ind.X].list :
				for x in range(3) :
					tmp = distanceEdge(face.loops[x][self.uv_lay].uv, face.loops[(x + 1)%3][self.uv_lay].uv, point_uv)
					if tmp < dist :
						dist = tmp
						edge = (face.loops[x].vert, face.loops[(x + 1)%3].vert)
						calc_face = face
		if calc_face is None :
			return (None, None, None, None)
		(intersect, uvw) = calculateBarycentricCoord2D(calc_face.loops[0][self.uv_lay].uv, calc_face.loops[1][self.uv_lay].uv, calc_face.loops[2][self.uv_lay].uv, point_uv)
		return (dist, calc_face, edge, uvw)
	def from_bmesh_uv(bmesh, uv_lay, face_per_partition = 2, bias = 0.00001) :
		"""
		Construction function that creates a grid representing the specific uv map for the specified bmesh
		bmesh: 	Bmesh to create from
		uv_lay:	Specified uv_layer 
		"""
		#Find uv size:
		minUV = Vector((sys.float_info.max,sys.float_info.max))
		maxUV = Vector((-sys.float_info.min, -sys.float_info.max))
		for face in bmesh.faces :
			for loop in face.loops :
				minUV = minVec(loop[uv_lay].uv, minUV)
				maxUV = maxVec(loop[uv_lay].uv, maxUV)
		#Add epsilon to size so the max points is floored into the grid:
		maxUV += Vector((bias,) * 2)
		size = maxUV - minUV
		#Calculate the number of squares to create:
		num_part = len(bmesh.faces) / face_per_partition
		part_per_size = sqrt(num_part * 4) / (size.x + size.y)
		partitions  = Point(ceil(size.x * part_per_size), ceil(size.y * part_per_size))
		#Apply a bias limit on partition count:
		if size.x / partitions.X < bias * 100 :
			partitions.X = ceil(size.x / (bias * 100))
		if size.y / partitions.Y < bias * 100 :
			partitions.Y = ceil(size.y / (bias * 100))
		grid = PartitionGrid2D(partitions, minUV, maxUV)
		#Define the uv layer for the grid object
		grid.uv_lay = uv_lay
		#Add the uv triangles to the grid:
		for face in bmesh.faces :
			grid.append_uv(face)
		return grid
	def __str__(self) :
		str = "Partition grid X: %d, Y: %d \n" % (self.partitions.X, self.partitions.Y)
		for y in self.grid  :
			str += "["
			for part in y :
				str += "%d," % len(part.list)
			str += "]\n"
		return str