# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


#bl_info = {
#	"name": "Render: Wireframe",
#	"author": "marvin.k.breuer (MKB)",
#	"version": (0, 1),
#	"blender": (2, 78),
#	"location": "VIEWD3D",
#	"description": "add wireframe modifier",
#	"warning": "",
#	"wiki_url": "",
#	"tracker_url": "",
#	"category": 'ToolPlus'}


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

def ops_render_wire(context):
    
    bpy.ops.object.duplicate_move()
        
    bpy.context.object.name = bpy.context.object.name + "_wireframe"
    bpy.context.object.data.name = bpy.context.object.name + "_wireframe"
    dupli_ob = bpy.context.object.name    

    bpy.ops.object.select_all(action='DESELECT')    
    bpy.ops.object.select_pattern(pattern=dupli_ob) 
    bpy.context.scene.objects.active = bpy.data.objects[dupli_ob]  


    bpy.ops.object.modifier_add(type='WIREFRAME')
    bpy.context.object.modifiers["Wireframe"].thickness = 0.05


    # Get material
    mat = bpy.data.materials.get("MATWire")
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name="MATWire")
 
    # Assign it to object
    ob = bpy.context.active_object             
                   
    if ob.data.materials:
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)
    
    mat.diffuse_color = (0, 0, 0)


class VIEW3D_RENDER_WIREFRAME(bpy.types.Operator):
    """create duplication as wireframe with black material"""
    bl_idname = "tp_ops.render_wireframe"
    bl_label = "Render Wireframe"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        ops_render_wire(context)
        return {'FINISHED'}



# REGISTRY #        
def register():
    bpy.utils.register_class(VIEW3D_RENDER_WIREFRAME)

def unregister():
    bpy.utils.unregister_class(VIEW3D_RENDER_WIREFRAME)

if __name__ == "__main__":
    register()
