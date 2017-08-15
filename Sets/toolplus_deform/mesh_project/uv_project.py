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

from .proj_data import *
from .funcs_blender import *
from bpy.props import * #Property objects

class UVProjectMesh(bpy.types.Operator):
    """Projects selected to active / need uv unwrap"""
    bl_idname = "mesh.project_onto_uvmapped_mesh"
    bl_label = "Project Mesh onto UV Surface"
    bl_info = "Projects a selected mesh object(s) onto the surface of the active mesh, fitting the mesh over the uvmap of the target"
    bl_options = {'REGISTER', 'UNDO'}
    
    proj_type_enum = [
        ("AXISALIGNED", "Axis Aligned", "The mesh axis with smallest angle toward the camera will be placed up on the projection surface", 1),
        ("CAMERA", "Camera View", "The mesh will be projected onto the surface using the camera axis as up. Depth is relative to the furthest and closest point to the camera", 2),
        ("ZISUP", "Z is Up", "Mesh will be placed on the surface with the Z axis pointing up", 3),
        ]
    
    proj_type = EnumProperty(items=proj_type_enum, 
            name = "Surface Alignment",
            description="Determines how the mesh will be aligned on the surface, primarily the axis pointing up/away from the surface. It also affects the x/y axis alignment and how the projection target area is determined.",)
    smooth = BoolProperty(name = "Smooth",
            description="If the mesh will be smoothed over the target surface",
            default=True)
    keepRelative = BoolProperty(name = "Keep Relative Scale",
            description="Scales the surface mapping to the same size ratio of the projected mesh",
            default=False)
    scalar = FloatProperty(name="Scale",
            description="Scale the surface mapping on the projection target",
            default=1,  soft_min= 0.01, soft_max=10, step=2, precision=2)
    depthAdd = FloatProperty(name="Distance/Depth",
            description="Move the projection closer/away from target surface by a fixed amount",
            default=0, min=-sys.float_info.max, max=sys.float_info.max, step=1)
    moveXY = FloatVectorProperty(name="Move", 
            description="Move the UV surface mapping on the projection target", 
            default=(0.0, 0.0), size=2, step=1, precision=4)
    rotation =  FloatProperty(name="Rotate",
            description="Rotate the object over the surface mapping",
            default=0, min=-sys.float_info.max, max=sys.float_info.max, step=8)
    scalarXYZ = FloatVectorProperty(name="Scale Separated", 
            description="Scale each X,Y surface mapping component separately or scale mesh Z axis", 
            default=(1.0, 1.0, 1.0), soft_min= 0.01, soft_max=10, size=3, step=2)
    partitions_per_face = FloatProperty(name="Partitions per face",
            description="Higher value increases invoke stage but execute (updates) runs faster. Higher value increases the numbers of partitions applied to the uv map",
            default=0.5, min=0.1, max=20, step=100)
    biasValue = FloatProperty(name="Intersection Bias",
            description="Error marginal for intersection tests, can solve intersection problems",
            default=0.00001, min=0.00001, max=1, step=1)
    printExecTime = BoolProperty(name = "Print Execution Time",
            description="Prints execution time to the information panel, mutes warning in the last report panel",
            default=False)
        
    def __init__(self):
        return
        
    def __del__(self):
        #Destructor cleanup
        self.projData.free()
    
    def update_setting(self) :
        #Update setting parameters, static object:
        Setting.bias = self.biasValue
        Setting.smooth = self.smooth
        Setting.scalar = Vector((self.scalarXYZ[0] * self.scalar, self.scalarXYZ[1] * self.scalar, self.scalarXYZ[2] * self.scalar))
        Setting.moveXY = Vector((self.moveXY[0], self.moveXY[1]))
        Setting.depth = self.depthAdd
        Setting.proj_type = self.proj_type
        Setting.rotation = self.rotation
        Setting.keepRelative = self.keepRelative
        Setting.partitions_per_face = self.partitions_per_face
        TriBias.bias = self.biasValue
    
    def invoke(self, context, event):
        """
        Generate projection information required to project each mesh.
        Note* blender mesh object references gets corrupted between execute stages.
        """
        
        #Execute stage 1: Gather projection data
        start_time = time.time()
        self.update_setting()
        self.report({'INFO'}, "Executing: Mesh Projection UV")
        
        # Get the active object and validate as mesh
        ob_target = context.active_object
        ob_sources = context.selected_objects
        
        #Verify a list of objects to project.
        proj_list = []
        for ob in ob_sources : 
            if ob.type == 'MESH' and ob != ob_target :
                proj_list.append(ob)
        if len(proj_list) == 0 :
            if len(ob_sources) > 0 :
                self.report({'ERROR'}, "Only mesh objects can be projected, need atleast one project source and one target surface object")
            else :
                self.report({'ERROR'}, "Not enough mesh objects selected, need atleast one source and one target object")
            return {'CANCELLED'}
            
            
        #Find 3d view camera rotation from context:
        cameraRot = findViewRotation(context)
        cameraRotInv = cameraRot.transposed()
        camAxis = findViewAxis(context)
        camPos = findViewPos(context)
        ortho = viewTypeOrtho(context)
        #Generate the object holding the intitial data:
        self.projData = ProjectionData(ob_target, cameraRotInv, camAxis, camPos, ortho,  self)
        #Generate the data for our target ob:
        if not self.projData.generateTargetData(ob_target, context):
            #Error generating target data.
            return {'CANCELLED'}
            
        #Generate projection information of the meshes that is being projected:
        self.projData.generateSourceData(proj_list, context.scene)
        if self.printExecTime :
            self.report({'INFO'}, "Finished, invoke stage execution time: %.2f seconds ---" % (time.time() - start_time))
        return self.execute(context)
        
    
    def execute(self, context):
        """
        Project each mesh according to the gathered information and the settings.
        """
        #Execute Stage 2: Project from gathered data according to settings:
        start_time = time.time()
        #Copy settings for comparisions:
        setting = Setting.copy()
        #Update settings
        self.update_setting()   
        #If axis alignment setting is changed new source data needs to be generated:
        if setting.proj_type != self.proj_type :
            self.projData.free_source()
            self.projData.generateSourceData(context.selected_objects, context.scene)
        elif setting.partitions_per_face != self.partitions_per_face :
            self.projData.generateTargetData(getObject(self.projData.target_ob, context.scene), context)
            self.report({'INFO'}, "Partitions increased: %.2f, mesh not updated. Edit other operator values to update it."% (time.time() - start_time))
            return {'FINISHED'}
        #Project the meshes with the gathered information
        self.projData.projectMeshData(context)
        #Finished
        if self.printExecTime :
            self.report({'INFO'}, "Finished, project stage execution time: %.2f seconds ---" % (time.time() - start_time))
        return {'FINISHED'}