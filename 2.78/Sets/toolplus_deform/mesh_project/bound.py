
import copy
from math import *
from mathutils import *
from .funcs_math import *
class Bounds :
	"""
	Bounds holds the bounding box of the source mesh (in aligned local space).
	It also holds rectangle min/max boundary and a 2D orientation base on the projection target uv map.
	The source mesh will then be projected onto the face covering the uv coordinate found by
	fitting the source mesh box over the oriented rectangle on the uv map
	"""

	def __init__(self, vMin, vMax, xAxis, yAxis, texOrigo, texMin, texMax):
		self.vMin = vMin
		self.vMax = vMax
		self.xAxis = xAxis
		self.yAxis = yAxis
		self.texMin = texMin
		self.texMax = texMax
		self.vSize = vMax - vMin
		self.uvSize = texMax - texMin
		self.texOrigo = texOrigo
				
	def calcUVPoint(self, co) :
		"""
		Function that calculates the uv-tex coord a point inside the bounds will project onto.
		Returns (u,v,depth)
		"""
		vOffset = co - self.vMin
		#Calculate the uv offset by interpolating the rectangle with the offset difference on the mesh:
		uv = Vector((
		self.texMin.x + self.uvSize.x * (vOffset.x / self.vSize.x),
		self.texMin.y + self.uvSize.y * (vOffset.y / self.vSize.y)))
		#Set the uv offset in the basis of the mapping:
		uv = uv.x * self.xAxis + uv.y * self.yAxis
		uv += self.texOrigo
		return Vector((uv.x, uv.y, vOffset.z))
	
	def scale(self, scalar) :
		"""
		Scale uv mapping
		"""
		self.texMax.x *= scalar.x
		self.texMin.x *= scalar.x
		self.texMax.y *= scalar.y
		self.texMin.y *= scalar.y
		self.uvSize = self.texMax - self.texMin
	
	def ensureMeshRatio(self) :
		"""
		Function that scales the mapping to the mesh size ratio between the X,Y axis.
		Fits the ratio inside the current mapped target area.
		"""
		ratio = self.vSize.x / self.vSize.y
		
		deltaX = self.uvSize.x - self.uvSize.y * ratio
		deltaY = self.uvSize.y - self.uvSize.x / ratio
		#Fit the axis that will shrink the mesh:
		if deltaY < deltaX :
			#Fit x axis:
			self.texMin.x += deltaX * 0.5
			self.texMax.x -= deltaX * 0.5
			self.uvSize.x -= deltaX
		else :
			#Fit y axis:
			self.texMin.y += deltaY * 0.5
			self.texMax.y -= deltaY * 0.5
			self.uvSize.y -= deltaY
			
		
	
	def move(self, vec2) :
		"""
		Move the uv mapping
		"""
		self.texOrigo += vec2
	
	#Rotate the uv mapping:
	def rotate(self, angle) :
		self.xAxis = rotateVec2(self.xAxis, angle)
		self.yAxis = rotateVec2(self.yAxis, angle)
		
		
	def From_Corners(texUL, texUR, texBR, texBL, texOrigo, vMin, vMax) :
		"""
		Calculates the mapping target 
		texUL, texUR, texBR, texBL:	UV coordinates for the mesh corners (Upper-, Lower- Right/Left) projected on the target.
		texOrigo:	Mesh origo projected onto the target. Determines rotation point.
		vMin, vMax:	Min/Max points on the mesh.
		"""
		
		
		#Average the points between the corners and calculate the vector from origo:
		y_up = (texUL - texUR) * 0.5 + texUR - texOrigo
		y_down = (texBL - texBR) * 0.5 + texBR - texOrigo
 		
		x_right = (texUR - texBR) * 0.5 + texBR - texOrigo
		x_left = (texUL - texBL) * 0.5 + texBL - texOrigo		
		
		#Find a orthonormal basis averaged between the four points defining the axis:
		yAxis = y_up - y_down
		xAxis = x_right - x_left
		#Verify there is a projection target
		if yAxis.length == 0 or xAxis.length == 0:
			return None
		
		#Find a basis orthonormalized (based) to both of the averaged x & y axis:
		y_yAxis, y_xAxis = orthoNormalizeVec2(yAxis, xAxis)
		x_xAxis, x_yAxis = orthoNormalizeVec2(xAxis, yAxis)
		
		#Take the average between the two basis:
		xAxis = (x_xAxis - y_xAxis) * 0.5 + y_xAxis
		xAxis.normalize()
		yAxis = rotateVec2(xAxis, 90)
		#xAxis, yAxis = orthoNormalizeVec2(xAxis, yAxis)
		
		
		#Calculate rect bounds by projecting onto the axis:
		texMin = Vector((xAxis.dot(x_left), yAxis.dot(y_down)))
		texMax = Vector((xAxis.dot(x_right), yAxis.dot(y_up)))
				
		return Bounds(vMin, vMax, xAxis, yAxis, texOrigo, texMin, texMax)
		
	def copy(self) :
		return copy.deepcopy(self)