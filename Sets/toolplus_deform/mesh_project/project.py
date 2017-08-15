#  uv_project.py (c) 2016 Mattias Fredriksson
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

import bpy, time, sys

from math import *
from mathutils import *
from .funcs_math import *
from .funcs_blender import *
from bpy.props import * #Property objects


class ProjectMesh(bpy.types.Operator):
    """ Projects selected to active / for redo apply transform"""
    bl_idname = "mesh.project_onto_selected_mesh"
    bl_label = "Project Mesh(es) onto Active"
    bl_info = "Projects a selected mesh(es) onto the active mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    proj_type_enum = [
        ("AXISALIGNED", "Axis Aligned", "The projected mesh(es) will be rotated so it's axis with the smallest angel toward the camera will face the it", 1),
        ("CAMERA", "Camera View", "The mesh will be projected as is, where each vertice distance from the projection surface will be determined by the furthest point from the camera (plane)", 2),
        ("ZISUP", "Z is Up", "The projected mesh(es) will be rotated so the Z axis will face the camera", 3),
        ]
    
    displayExecutionTime = False
    
    proj_type = EnumProperty(items=proj_type_enum, 
            name = "Projection Alignment",
            description="Determines how the mesh will be aligned related to camera view before projection onto the surface. ",)
    depthOffset = FloatProperty(name="Depth Offset",
            description="Move the projection closer/away from target surface by a fixed amount (along camera forward axis)",
            default=0, min=-sys.float_info.max, max=sys.float_info.max, step=1)
    bias = FloatProperty(name="Intersection Bias",
            description="Error marginal for intersection tests, can solve intersection problems",
            default=0.00001, min=0.00001, max=1, step=1)
    
    def invoke(self, context, event) :
        """ 
        Invoke stage, gathering information of the projection objects:
        """
        start_time = time.time()
        #Fetch camera orientations:
        self.cameraRot = findViewRotation(context) 
        self.cameraRotInv = self.cameraRot.transposed()
        self.camAxis = findViewAxis(context)
        self.cameraPos = findViewPos(context)
        self.ortho = viewTypeOrtho(context)
        self.lastOffset = self.depthOffset
    
        target_ob = context.active_object
        #Verify target
        if not target_ob:
            self.report({'ERROR'}, "No active mesh object found to use as projection target.")
            return {'CANCELLED'}
        elif target_ob.type != 'MESH':
            self.report({'ERROR'}, "Active object was not a mesh. Select an appropriate mesh object as projection target")
            return {'CANCELLED'}
        ob_sources = context.selected_objects
        #Verify selection
        self.ob_list = []
        for ob in ob_sources :
            if ob.type == 'MESH' and ob != target_ob :
                self.ob_list.append(SourceMesh(ob))
        if len(self.ob_list) == 0 :
            if len(ob_sources) > 0 :
                self.report({'ERROR'}, "Only mesh objects can be projected, need atleast one project source and an active object as projection target")
            else :
                self.report({'ERROR'}, "No selection to project found, make sure to select one project source and an active object as projection target")
            return {'CANCELLED'}
        #Generate projection info
        self.generate_BVH(target_ob, context.scene)
        self.target_ob = target_ob.name
        
        if ProjectMesh.displayExecutionTime :
            self.report({'INFO'}, "Finished, invoke stage execution time: %.2f seconds ---" % (time.time() - start_time))
        return self.execute(context)
    
    def execute(self, context):
        """
        Project each mesh onto active object
        """
        start_time = time.time()
        
        offset_change =  self.depthOffset != self.lastOffset
        
        self.lastOffset = self.depthOffset
        if not offset_change:
            self.report({'INFO'}, "Executing: Mesh Projection")
            #Project the meshes with the gathered information
            self.project(context.scene)
            #Finished
            if ProjectMesh.displayExecutionTime :
                self.report({'INFO'}, "Finished, project stage execution time: %.2f seconds ---" % (time.time() - start_time))
        #Set offset move it on camera forward axis:
        self.depthChange(context.scene)
        return {'FINISHED'}
        
    def depthChange(self, scene) :
        """ Moves the objects along camera z axis
        """
        mat = Matrix.Translation(self.camAxis[2] * -self.depthOffset)
        for ob in self.ob_list : 
            if ob.bmesh_gen is not None:
                setNamedMesh(ob.bmesh_gen, ob.name, scene, Matrix.Translation(self.camAxis[2] * -self.depthOffset))
    
    def generate_BVH(self, target_ob, scene) :
        #Can't create from object, transformation not applied
        bmesh = createBmesh(target_ob, target_ob.matrix_world, True, scene, True)
        self.bvh = bvhtree.BVHTree.FromBMesh(bmesh, epsilon = self.bias) 
        bmesh.free()
    
    def project(self, scene) :
        """ Project the mesh(es) onto the target
        """
        for ob in self.ob_list : 
            #Create a bm mesh copy of the mesh!
            bmesh = ob.bmesh.copy()
            (vMin, vMax) = findMinMax(bmesh)
            mat = self.orientation(ob)
            #createMesh(bmesh, scene, mat) #Generate a aligned debug mesh
            #Find the furthest point of the mesh along camera forward 
            depthDist = max(self.camAxis[2].dot(mat * vMin), self.camAxis[2].dot(mat * vMax))
            proj_list = [(None,None) for x in range(len(bmesh.verts))]
            non_proj_list = []
            #Project the vertices:
            count = 0
            count_closest = 0
            for vert in bmesh.verts :
                count += self.projectVert(mat, vert, depthDist, proj_list, non_proj_list)
            for vert in non_proj_list :
                count_closest += self.projectClosestConnect(mat, vert, depthDist, proj_list)
            #Finalize the projection by assigning the bmesh into the blender object 
            #Validate one vert was projected first:
            bmesh.select_flush(False)
            
            if count > 0 :
                ob.bmesh_gen = bmesh
                setNamedMesh(bmesh, ob.name, scene, Matrix.Translation(self.camAxis[2] * -self.depthOffset))
                if count_closest > 0:
                    self.report({'WARNING'}, "Mesh: %s has %d vertices that failed to project and used neighbouring vertex result instead. Verify selected verts is projected OK" %(ob.name, count_closest))
                nonProjCount = len(bmesh.verts) - (count + count_closest)
                if nonProjCount != 0:
                    self.report({'WARNING'}, "Mesh: %s has %d vertices that did not project succesfully. Validate that the mesh is covered by the target" %(ob.name, nonProjCount))
            else :
                self.report({'WARNING'}, "Mesh: %s had no vertices projected onto the target. Validate that the mesh is covered by the target" %(ob.name))
    #Done
    
    
    def projectVert(self, transMat, vert, depthDist, proj_list, non_proj) :
        """ Calculate the projection of a single vert (also sets the vert.co)
        transMat:   Object transformation matrix
        vert:       Vert being updated
        """
        co =  transMat * vert.co
        #Find the distance offset to the max point of the mesh along camera axis
        dir = self.getCameraAxis(co)
        #Ray cast:
        (loc, nor, ind, dist) = self.bvh.ray_cast(co, dir, 100000)
        #If intersection occured project it
        if loc is not None:
            offset = -(depthDist - self.camAxis[2].dot(co))
            vert.co = loc + dir * offset
            proj_list[vert.index] = (loc, nor) #Store projection point and normal
            vert.select_set(False)
            return True
        #else:
        non_proj.append(vert)
        vert.select_set(True)
        return False
    
    def projectClosestConnect(self, transMat, vert, depthDist, proj_list) :
        co =  transMat * vert.co
        for edge in vert.link_edges :
            o_vert_ind = edge.other_vert(vert).index
            if proj_list[o_vert_ind][0] is not None :
                dir = self.getCameraAxis(co)
                rel = proj_list[o_vert_ind][1].dot(dir) #Relation between ray dir and plane normal.
                if abs(rel) <  self.bias:
                    continue
                #Plane d value:
                d = -proj_list[o_vert_ind][1].dot(proj_list[o_vert_ind][0])
                #Calculate distance
                dist = (-d - proj_list[o_vert_ind][1].dot(co)) / rel
                
                offset = -(depthDist - self.camAxis[2].dot(co))
                #project
                vert.co = co + dir * (dist + offset)
                return True
        return False
    
    def orientation(self, ob) :
        loc, meshRot, sca = ob.matrix_world.decompose()
        meshRot = meshRot.to_matrix()
        
        #Calc rotation
        if self.proj_type == 'AXISALIGNED' :
            rot = self.cameraRot * alignRotationMatrix(self.cameraRotInv * meshRot)
        elif self.proj_type == 'ZISUP' :
            rot = self.cameraRot * calculateXYPlaneRot(meshRot.transposed(), self.camAxis)
        else : #self.proj_type == 'CAMERA' :
            rot = meshRot
        #Assemble orientation matrix:
        mat = Matrix.Translation(loc) * (rot * scaleMatrix(sca, 3)).to_4x4()
        #mat[3].xyz = loc
        return mat
        
    def getCameraAxis(self, target) :
        """ Calculates the projection ray direction
        """
        if self.ortho :
            return self.camAxis[2]
        else :
            dir = target - self.cameraPos
            dir.normalize()
            return dir  
            
class SourceMesh :
    def __init__(self, object):
        self.name = object.name
        self.matrix_world = object.matrix_world.copy()
        self.bmesh = createBmesh(object)
        self.bmesh_gen = None
    
    def __del__(self) :
        if self.bmesh_gen is not None :
            self.bmesh_gen.free()
        self.bmesh.free()
def calculateXYPlaneRot(meshAxis, camAxis) :
    """ Finds the rotation of the mesh on the camera X,Y plane 
    """
    xAxis = meshAxis[0] - meshAxis[0].dot(camAxis[2]) * camAxis[2]
    xAxis.normalize()
    x = xAxis.dot(camAxis[0])
    y = xAxis.dot(camAxis[1])
    
    angle = atan2(y,x)
    return Matrix.Rotation(angle, 3, Vector((0,0,1))) #Use camAxis[2] if the rotation is applied in world space opposed to camera space
    
def alignRotationMatrix(rotMat) :
    """
    Aligns the axis with largest Z component to (0,0,1) and orthonormalizes the other two axes.
    """
    #Find axis with largest Z component and orthonormalize the other basis vectors to it:
    if abs(rotMat[2][2]) > max(abs(rotMat[1][2]), abs(rotMat[0][2])) :
        #Z axis is depth:
        rotMat[2] = Vector((0,0,sign(rotMat[2][2])))
        rotMat[2], rotMat[0], rotMat[1] = orthoNormalizeVec3(rotMat[2], rotMat[0], rotMat[1])
    elif abs(rotMat[1][2]) > abs(rotMat[0][2]) :
        #Y axis is depth:
        rotMat[1] = Vector((0,0,sign(rotMat[1][2])))
        rotMat[1], rotMat[0], rotMat[2] = orthoNormalizeVec3(rotMat[1], rotMat[0], rotMat[2])
    else :
        #X axis is depth:
        rotMat[0] = Vector((0,0,sign(rotMat[0][2])))
        rotMat[0], rotMat[1], rotMat[2] = orthoNormalizeVec3(rotMat[0], rotMat[1], rotMat[2])
    return rotMat           
                    