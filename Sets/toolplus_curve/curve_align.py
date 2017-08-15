# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Transform",
    "category": "3DMish",
    "author": "3DMish (Mish7913@gmail.com)",
    "version": (0, 2, 6),
    "blender": (2, 78, 0),
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "description": "Copy / Paste / Paste Mirror Transform object, vertex, edge and faces.",
    }
    
import bpy
import bmesh
import mathutils
import math
from mathutils import Vector

"""
class MishTransform(bpy.types.Panel):	
	bl_category 	= "3DMish"
	bl_label 		= "Transform"
	bl_space_type 	= "VIEW_3D"
	bl_region_type 	= "TOOLS"

	def draw(self, context):
		Gcol = self.layout.column(align=True)
		Rcol = Gcol.row(align=True)
		Rcol.operator("3dmish.copy", icon="COPYDOWN")
		Rcol.operator("3dmish.paste", icon="PASTEDOWN")
		Gcol.operator("3dmish.paste_mirror", icon="PASTEFLIPDOWN")
		Gcol.prop(context.scene, 'TRS', text = "")
		
		LBcol = self.layout.column(align=True)
		Lcol = LBcol.row(align=True)
		Lcol.prop(context.scene, 'LOC', text = "")
		Lcol.prop(context.scene, 'ROT', text = "")
		Xcol = LBcol.row(align=True)
		Xcol.prop(context.scene, 'lX')
		Xcol.prop(context.scene, 'rX')
		Ycol = LBcol.row(align=True)
		Ycol.prop(context.scene, 'lY')
		Ycol.prop(context.scene, 'rY')
		Zcol = LBcol.row(align=True)
		Zcol.prop(context.scene, 'lZ')
		Zcol.prop(context.scene, 'rZ')
"""
	
class MishTransformCopy(bpy.types.Operator):
	bl_idname 		= '3dmish.copy'
	bl_label 		= 'Copy'
	bl_description  = 'Copy Location'

	def execute(self, context):
		vertL = (0, 0, 0); vertR = (0, 0, 0)
		if bpy.context.active_object.mode == 'OBJECT':
			if not bpy.context.scene.TRS == "oR": vertL = bpy.context.active_object.location
			if not bpy.context.scene.TRS == "oL": vertR = bpy.context.active_object.rotation_euler
		elif bpy.context.active_object.mode == 'EDIT':
			bm = bmesh.from_edit_mesh(bpy.context.active_object.data)
			verts_sel = [v.co for v in bm.verts if v.select]
			vertL = sum(verts_sel, Vector()) / len(verts_sel)
		elif bpy.context.active_object.mode == 'POSE':
			if not bpy.context.scene.TRS == "oR": vertL = bpy.context.active_pose_bone.location
			if not bpy.context.scene.TRS == "oL": vertR = bpy.context.active_pose_bone.rotation_euler
		if not bpy.context.scene.TRS == "oR": bpy.context.scene.lX = vertL[0];      bpy.context.scene.lY = vertL[1];      bpy.context.scene.lZ = vertL[2]
		if not bpy.context.scene.TRS == "oL": bpy.context.scene.rX = vertR[0]*57.3; bpy.context.scene.rY = vertR[1]*57.3; bpy.context.scene.rZ = vertR[2]*57.3
		return {'FINISHED'}
        
class MishTransformPaste(bpy.types.Operator):
	bl_idname 		= '3dmish.paste'
	bl_label 		= 'Paste'
	bl_description  = 'Paste Location'

	def execute(self, context):
		LoX = bpy.context.scene.lX; LoY = bpy.context.scene.lY; LoZ = bpy.context.scene.lZ
		RoX = bpy.context.scene.rX; RoY = bpy.context.scene.rY; RoZ = bpy.context.scene.rZ
		if bpy.context.active_object.mode == 'OBJECT':
			if not bpy.context.scene.TRS == "oR": bpy.context.active_object.location = LoX, LoY, LoZ
			if not bpy.context.scene.TRS == "oL": bpy.context.active_object.rotation_euler = RoX/57.3, RoY/57.3, RoZ/57.3
		elif bpy.context.active_object.mode == 'EDIT':
			vert = (LoX, LoY, LoZ); vert2 = GetPosition(); pX, pY, pZ = BoMeDD(vert, vert2)
			bpy.ops.transform.translate(value=(pX, pY, pZ), constraint_axis=(True, True, True), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
		if bpy.context.active_object.mode == 'POSE':
			if not bpy.context.scene.TRS == "oR": bpy.context.active_pose_bone.location = LoX, LoY, LoZ
			if not bpy.context.scene.TRS == "oL": bpy.context.active_pose_bone.rotation_euler = RoX/57.3, RoY/57.3, RoZ/57.3
		bpy.context.scene.update(); bpy.context.area.tag_redraw()
		if bpy.context.scene.tool_settings.use_keyframe_insert_auto == True:
			bpy.ops.anim.keyframe_insert_menu(type='Location')
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
		return {'FINISHED'}
    
class MishTransformPasteMirror(bpy.types.Operator):
	bl_idname 		= '3dmish.paste_mirror'
	bl_label 		= 'Paste Mirror'
	bl_description  = 'Paste Mirror Location'

	def execute(self, context):
		LoX = bpy.context.scene.lX; LoY = bpy.context.scene.lY; LoZ = bpy.context.scene.lZ
		RoX = bpy.context.scene.rX; RoY = bpy.context.scene.rY; RoZ = bpy.context.scene.rZ
		if bpy.context.active_object.mode == 'OBJECT':
			if not bpy.context.scene.TRS == "oR": 
				if   bpy.context.scene.LOC == "X": bpy.context.active_object.location = -LoX,  LoY,  LoZ
				elif bpy.context.scene.LOC == "Y": bpy.context.active_object.location =  LoX, -LoY,  LoZ
				elif bpy.context.scene.LOC == "Z": bpy.context.active_object.location =  LoX,  LoY, -LoZ
			if not bpy.context.scene.TRS == "oL":
				if   bpy.context.scene.ROT == "X": bpy.context.active_object.rotation_euler = -RoX/57.3,  RoY/57.3,  RoZ/57.3
				elif bpy.context.scene.ROT == "Y": bpy.context.active_object.rotation_euler =  RoX/57.3, -RoY/57.3,  RoZ/57.3
				elif bpy.context.scene.ROT == "Z": bpy.context.active_object.rotation_euler =  RoX/57.3,  RoY/57.3, -RoZ/57.3
		elif bpy.context.active_object.mode == 'EDIT':
			vert = LoX, LoY, LoZ; vert2 = GetPosition(); pX, pY, pZ = BoMeDD(vert, vert2)
			bpy.ops.transform.translate(value=(pX, pY, pZ), constraint_axis=(True, True, True), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
			if   bpy.context.scene.LOC == "X": bpy.ops.transform.translate(value=(-LoX*2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
			elif bpy.context.scene.LOC == "Y": bpy.ops.transform.translate(value=(0, -LoY*2, 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
			elif bpy.context.scene.LOC == "Z": bpy.ops.transform.translate(value=(0, 0, -LoZ*2), constraint_axis=(False, False, True), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
		if bpy.context.active_object.mode == 'POSE':
			if   bpy.context.scene.LOC == "X": bpy.context.active_pose_bone.location = -LoX,  LoY,  LoZ
			elif bpy.context.scene.LOC == "Y": bpy.context.active_pose_bone.location =  LoX, -LoY,  LoZ
			elif bpy.context.scene.LOC == "Z": bpy.context.active_pose_bone.location =  LoX,  LoY, -LoZ
		bpy.context.scene.update(); bpy.context.area.tag_redraw()
		if bpy.context.scene.tool_settings.use_keyframe_insert_auto == True:
			bpy.ops.anim.keyframe_insert_menu(type='Location')
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
		return {'FINISHED'}

def GetPosition():
	bm = bmesh.from_edit_mesh(bpy.context.active_object.data)
	verts_sel = [v.co for v in bm.verts if v.select]
	vert = sum(verts_sel, Vector()) / len(verts_sel)
	return vert

def BoMeDD(Vector1, Vector2):
	if Vector1[0] > Vector2[0]: X = (Vector1[0]-Vector2[0])
	else: X = -(Vector2[0]-Vector1[0])
	if Vector1[1] > Vector2[1]: Y = (Vector1[1]-Vector2[1])
	else: Y = -(Vector2[1]-Vector1[1])
	if Vector1[2] > Vector2[2]: Z = (Vector1[2]-Vector2[2])
	else: Z = -(Vector2[2]-Vector1[2])
	return (X, Y, Z)

def initSceneProperties(X=0, Y=0, Z=0):
	bpy.types.Scene.TRS = bpy.props.EnumProperty(items= (('ALL', 'ALL', 'ALL'), ('oL', 'Only Location', 'Only Location'), ('oR', 'Only Rotation', 'Only Rotation'))) 
	bpy.types.Scene.LOC = bpy.props.EnumProperty(items= (('N', 'None', 'None Mirror'), ('X', 'X Location', 'Mirror X'), ('Y', 'Y Location', 'Mirror Y'), ('Z', 'Z Location', 'Mirror Z'))) 
	bpy.types.Scene.lX = bpy.props.FloatProperty(name = "X", default = 0)
	bpy.types.Scene.lY = bpy.props.FloatProperty(name = "Y", default = 0)
	bpy.types.Scene.lZ = bpy.props.FloatProperty(name = "Z", default = 0)
	bpy.types.Scene.ROT = bpy.props.EnumProperty(items= (('N', 'None', 'None Mirror'), ('X', 'X Rotation', 'Mirror X'), ('Y', 'Y Rotation', 'Mirror Y'), ('Z', 'Z Rotation', 'Mirror Z'))) 
	bpy.types.Scene.rX = bpy.props.FloatProperty(name = "X", default = 0)
	bpy.types.Scene.rY = bpy.props.FloatProperty(name = "Y", default = 0)
	bpy.types.Scene.rZ = bpy.props.FloatProperty(name = "Z", default = 0)
	return
initSceneProperties()

def register():
    bpy.utils.register_class(MishTransform)
    bpy.utils.register_class(MishTransformCopy)
    bpy.utils.register_class(MishTransformPaste)
    bpy.utils.register_class(MishTransformPasteMirror)

def unregister():
	bpy.utils.unregister_class(MishTransform)
	bpy.utils.unregister_class(MishTransformCopy)
	bpy.utils.unregister_class(MishTransformPaste)
	bpy.utils.unregister_class(MishTransformPasteMirror)

if __name__ == "__main__":
    register()
