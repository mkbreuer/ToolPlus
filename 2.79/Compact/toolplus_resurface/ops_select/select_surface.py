"""
bl_info = {
    "name": "Mesh check",
    "author": "Clarkx, Cedric Lepiller, CoDEmanX, Pistiwique",
    "version": (0, 1, 0),
    "blender": (2, 75, 0),
    "description": "Custom Menu to show faces, tris, Ngons on the mesh",
    "category": "",}
"""   

import bpy
from bpy.props import* 
 
class FaceTypeSelect(bpy.types.Operator):
    bl_idname = "object.face_type_select"
    bl_label = "Face type select"
    bl_options = {'REGISTER', 'UNDO'}
    
    face_type = bpy.props.EnumProperty(
            items=(('tris', 'Tris', ""),
                   ('ngons', 'Ngons', "")),
                   default='ngons'
                   )
 
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'
 
    def execute(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        context.tool_settings.mesh_select_mode=(False, False, True)
        
        if self.face_type == "tris":
            bpy.ops.mesh.select_face_by_sides(number=3, type='EQUAL')
        else:
            bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER')
 
        return {'FINISHED'}