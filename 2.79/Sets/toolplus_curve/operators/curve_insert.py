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

# LOAD MODUL #
import bpy, bmesh
from bpy import *
from bpy.props import *
from mathutils import *
 
 
def tp_curve_insert_choise(object):
    #initial set 
    if object == "Torus.png":
        bpy.ops.mesh.primitive_torus_add()

    elif object == "Icosphere.png":
        bpy.ops.mesh.primitive_ico_sphere_add()

    elif object == "Cone.png":
        bpy.ops.mesh.primitive_cone_add()
        


def tp_curve_preview_insert(self, context):
    wm = context.window_manager
    object = wm.TP_Curves_Insert_Previews
    obj_list = []    
    second_obj = ""
    
    if context.object.mode == 'OBJECT':
        tp_curve_insert_choise(object)#initial set
        
    elif context.object.mode == 'EDIT':        
        bpy.ops.object.mode_set(mode='OBJECT')  
        
        ref_obj = bpy.context.active_object
        
        if len(context.selected_objects) == 2:
            obj1, obj2 = context.selected_objects
            second_obj = obj1 if obj2 == ref_obj else obj2
        
            bpy.data.objects[second_obj.name].select=False

        bpy.ops.object.duplicate_move()
        bpy.context.active_object.name = "Dummy"
        obj = context.active_object
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')    
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
        copy_cursor = bpy.context.scene.cursor_location.copy()  
        
        bm = bmesh.new()
        bm.from_mesh(obj.data)
          
        selected_faces = [f for f in bm.faces if f.select]
     
        for face in selected_faces:
     
            face_location = face.calc_center_median()
     
            loc_world_space = obj.matrix_world * Vector(face_location)
     
            z = Vector((0,0,1))
     
            angle = face.normal.angle(z)
     
            axis = z.cross(face.normal)
            bpy.context.scene.cursor_location = loc_world_space

            tp_curve_insert_choise(object)#initial set
                 
            bpy.ops.transform.rotate(value=angle, axis=axis)
            obj_list.append(context.object.name)
     
        bm.to_mesh(obj.data)
     
        bm.free()
        
        bpy.context.scene.cursor_location = copy_cursor
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects["Dummy"]         
        bpy.data.objects["Dummy"].select = True
        bpy.ops.object.delete(use_global=False)
        
        bpy.context.scene.objects.active = bpy.data.objects[obj_list[0]]
        
        for obj in obj_list:
            bpy.data.objects[obj].select=True
            bpy.ops.make.link()  
        
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects[ref_obj.name]
        if second_obj:
            bpy.data.objects[second_obj.name].select=True   
        bpy.data.objects[ref_obj.name].select=True
     
        bpy.ops.object.mode_set(mode='EDIT')
        del(obj_list[:])
 


class VIEW3D_TP_Make_Link(bpy.types.Operator):
    bl_idname = "make.link"
    bl_label = "Make Link"
    bl_description = ""
    bl_options = {"REGISTER"}
    
    
    
    def execute(self, context):
        bpy.ops.object.make_links_data(type='OBDATA')
        bpy.ops.object.make_links_data(type='MODIFIERS')

        return {"FINISHED"}




# REGISTRY #        
def register():
    
    WindowManager.TP_Curves_Insert_Previews = EnumProperty(items=load_icons, update = tp_curve_preview_insert)

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)
    
    del WindowManager.TP_Curves_Insert_Previews

if __name__ == "__main__":
    register()



