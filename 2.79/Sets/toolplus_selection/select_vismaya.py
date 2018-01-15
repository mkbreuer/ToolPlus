#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****




#bl_info = {
#    'name' : 'Vismaya Tools-v1.1',
#    'author' : 'Project Vismaya',
#    'version' : (0, 1),
#    'blender' : (2, 56, 2),
#    'location' : 'View3D > Toolbar',
#    'description' : 'Vismaya Tools v1.1',
#    'category' : '3D View'}

import bpy

from bpy.types import Operator, Panel
from bpy.props import (StringProperty,
                       EnumProperty,
                       FloatProperty,
                       BoolProperty)
import os
from bpy_extras.io_utils import ExportHelper
from platform import system as currentOS

mesh = 0
curve =0
lamp =0
bone = 0
camera =0
particles = 0
pfopath=""
opps=0
opps1=0



########### Freeze Transformation ###########

class Set_Freezetransform(bpy.types.Operator):
    """set transform values to zero"""
    bl_idname = "freeze_transform.selected"
    bl_label = "Freeze Transform"	
    bl_options = {'REGISTER', 'UNDO'}
        
    def execute(self, context):       
   
        str = context.active_object.type       
        if str.startswith('EMPTY') or str.startswith('SPEAKER') or str.startswith('CAMERA')or str.startswith('LAMP')or str.startswith('FONT'):                 
            #Location
            context.active_object.delta_location+=context.active_object.location
            context.active_object.location=[0,0,0]       
            
            #Rotation
            
            rotX=bpy.context.active_object.rotation_euler.x
            rotDeltaX=bpy.context.active_object.delta_rotation_euler.x
            bpy.context.active_object.delta_rotation_euler.x=rotX+rotDeltaX    
                
            rotY=bpy.context.active_object.rotation_euler.y
            rotDeltaY=bpy.context.active_object.delta_rotation_euler.y
            bpy.context.active_object.delta_rotation_euler.y=rotDeltaY+rotY           
         
            rotZ= bpy.context.active_object.rotation_euler.z
            rotDeltaZ=bpy.context.active_object.delta_rotation_euler.z
            bpy.context.active_object.delta_rotation_euler.z= rotDeltaZ+rotZ  
                        
            rquatW = context.active_object.rotation_quaternion.w
            rquatX = context.active_object.rotation_quaternion.x
            rquatY = context.active_object.rotation_quaternion.y
            rquatZ = context.active_object.rotation_quaternion.z
            
            drquatW = context.active_object.delta_rotation_quaternion.w
            drquatX = context.active_object.delta_rotation_quaternion.x
            drquatY = context.active_object.delta_rotation_quaternion.y
            drquatZ = context.active_object.delta_rotation_quaternion.z
            
            context.active_object.delta_rotation_quaternion.w = 1.0
            context.active_object.delta_rotation_quaternion.x = rquatX + drquatX
            context.active_object.delta_rotation_quaternion.y = rquatY + drquatY
            context.active_object.delta_rotation_quaternion.z = rquatZ + drquatZ
            
            context.active_object.rotation_quaternion.w = 1.0
            context.active_object.rotation_quaternion.x = 0.0
            context.active_object.rotation_quaternion.y = 0.0
            context.active_object.rotation_quaternion.z = 0.0
            
            bpy.context.active_object.rotation_euler.x = 0        
            bpy.context.active_object.rotation_euler.y = 0
            bpy.context.active_object.rotation_euler.z = 0
                      
            #Scale        
            context.active_object.delta_scale.x += (context.active_object.scale.x-1) * context.active_object.delta_scale.x
            context.active_object.delta_scale.y += (context.active_object.scale.y-1) * context.active_object.delta_scale.y
            context.active_object.delta_scale.z += (context.active_object.scale.z-1) * context.active_object.delta_scale.z
            context.active_object.scale=[1,1,1]   
            
            return {'FINISHED'}  
        else:            
            context.active_object.delta_location+=context.active_object.location
            context.active_object.location=[0,0,0]
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True)                   
        
            return {'FINISHED'}




############### Freeze/ UnFreeze Objects ##############

class OBJECT_OT_mesh_all(bpy.types.Operator):
	"""restrict viewport selection"""
	bl_idname = "object.mesh_all"
	bl_label = "Freez / UnFreez Mesh"

	def execute(self, context):
		objects = []
		eligible_objects = []
		objects = bpy.context.scene.objects
		#objects = scene.objects 
		#Only Specific Types? + Filter layers
		for obj in objects:
			for i in range(0,20):
				if obj.layers[i]:
					if obj.type == 'MESH':
						if obj not in eligible_objects:
							eligible_objects.append(obj)                     
		objcts = eligible_objects
		if mesh == 0:
			global mesh
			mesh = 1
			for obj in objcts: # deselect all objects
				obj.hide_select = True
		else:
			global mesh
			mesh = 0
			for obj in objcts: # deselect all objects
				obj.hide_select = False
		return {'FINISHED'}


class OBJECT_OT_curve_all(bpy.types.Operator):
	"""restrict viewport selection"""
	bl_idname = "object.curve_all"
	bl_label = "Freez / UnFreez Curve"
	def execute(self, context):
		objects = []
		eligible_objects = []
		objects = bpy.context.scene.objects
		for obj in objects:
			for i in range(0,20):
				if obj.layers[i]:
					if obj.type == 'CURVE':
						if obj not in eligible_objects:
							eligible_objects.append(obj)                     
		objcts = eligible_objects
		if curve == 0:
			global curve
			curve = 1
			for obj in objcts: # deselect all objects
				obj.hide_select = True
		else:
			global curve
			curve = 0
			for obj in objcts: # deselect all objects
				obj.hide_select = False
		return {'FINISHED'} 


class OBJECT_OT_lamp_all(bpy.types.Operator):
	"""restrict viewport selection"""
	bl_idname = "object.lamp_all"
	bl_label = "Freez / UnFreez Lamp"
	def execute(self, context):
		objects = []
		eligible_objects = []
		objects = bpy.context.scene.objects
		#objects = scene.objects 
		#Only Specific Types? + Filter layers
		for obj in objects:
			for i in range(0,20):
				if obj.layers[i]:
					if obj.type == 'LAMP':
						if obj not in eligible_objects:
							eligible_objects.append(obj)                     
		objcts = eligible_objects
		if lamp == 0:
			global lamp
			lamp = 1
			for obj in objcts: # deselect all objects
				obj.hide_select = True
		else:
			global curve
			lamp = 0
			for obj in objcts: # deselect all objects
				obj.hide_select = False

		return {'FINISHED'}


class OBJECT_OT_bone_all(bpy.types.Operator):
	"""restrict viewport selection"""
	bl_idname = "object.bone_all"
	bl_label = "Freez / UnFreez Bone"
	def execute(self, context):
		objects = []
		eligible_objects = []
		objects = bpy.context.scene.objects
		for obj in objects:
			for i in range(0,20):
				if obj.layers[i]:
					if obj.type == 'ARMATURE':
						if obj not in eligible_objects:
							eligible_objects.append(obj)                     
		objcts = eligible_objects
		if bone == 0:
			global bone
			bone = 1
			for obj in objcts: # deselect all objects
				obj.hide_select = True
		else:
			global bone
			bone = 0
			for obj in objcts: # deselect all objects
				obj.hide_select = False
		return {'FINISHED'}


class OBJECT_OT_camera_all(bpy.types.Operator):
	"""restrict viewport selection"""
	bl_idname = "object.camera_all"
	bl_label = "Freez / UnFreez Camera"
	def execute(self, context):
		objects = []
		eligible_objects = []
		objects = bpy.context.scene.objects
		for obj in objects:
			for i in range(0,20):
				if obj.layers[i]:
					if obj.type == 'CAMERA':
						if obj not in eligible_objects:
							eligible_objects.append(obj)                     
		objcts = eligible_objects
		if camera == 0:
			global camera
			camera = 1
			for obj in objcts: # deselect all objects
				obj.hide_select = True
		else:
			global camera
			camera = 0
			for obj in objcts: # deselect all objects
				obj.hide_select = False
		return {'FINISHED'}


class OBJECT_OT_particules_all(bpy.types.Operator):
	"""restrict viewport selection"""
	bl_idname = "object.particles_all"
	bl_label = "Freez / UnFreez Praticles"
	def execute(self, context):
		objects = []
		eligible_objects = []
		objects = bpy.context.scene.objects
		for obj in objects:
			for i in range(0,20):
				if obj.layers[i]:
					if obj.type == 'PARTICLES':
						if obj not in eligible_objects:
							eligible_objects.append(obj)                     
		objcts = eligible_objects
		if particles == 0:
			global particles
			particles = 1
			for obj in objcts: # deselect all objects
				obj.hide_select = True
		else:
			global particles
			particles = 0
			for obj in objcts: # deselect all objects
				obj.hide_select = False
		return {'FINISHED'}


	def invoke(self, context, event):
		return {'RUNNING_MODAL'}


class Freeze_Selected(bpy.types.Operator):
    """Freeze Selected"""
    bl_idname = "view3d.freeze_selected"
    bl_label = "Freeze Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        for obj in bpy.context.selected_objects:
    
            bpy.context.scene.objects.active = obj
    
            bpy.context.object.hide_select = True        

        return{'FINISHED'}


class UnFreeze_Selected(bpy.types.Operator):
    """Un-Freeze Selected"""
    bl_idname = "view3d.unfreeze_selected"
    bl_label = "UnFreeze Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
                 
        for obj in bpy.context.selected_objects:
    
             bpy.context.object.hide_select = False
             
             bpy.context.scene.objects.active = obj        

        return{'FINISHED'}  



class VIEW3D_MTK_FreezeAll(bpy.types.Menu):
    """(Un-) Freeze all by Type"""
    bl_label = "(Un-) Freeze"
    bl_idname = "tp_menu.freezeall"

    def draw(self, context):
        layout = self.layout
    
        col = layout.column(align=True)           
        layout.operator("object.mesh_all", text="Mesh", icon="OBJECT_DATAMODE")
        layout.operator("object.lamp_all",text="Lampe", icon="LAMP")
        layout.operator("object.curve_all",text="Curve", icon="OUTLINER_OB_CURVE")
        layout.operator("object.bone_all",text="Bone", icon="BONE_DATA")
        layout.operator("object.particles_all", text="Particle", icon="MOD_PARTICLES")
        layout.operator("object.camera_all", text="Camera", icon="OUTLINER_DATA_CAMERA")


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)  

if __name__ == "__main__":
    register() 	    
