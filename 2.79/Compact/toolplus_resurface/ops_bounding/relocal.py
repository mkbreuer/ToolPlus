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


# LOAD MODULE #
import bpy, bmesh
from bpy import *
from bpy.props import *


# LOCAL ORIENTATION #
import mathutils
def local_rotate(mesh, mat):
    for v in mesh.vertices:
        vec = mat * v.co
        v.co = vec
        
def Rotate(myMesh, mat):
    for v in myMesh.vertices:
        vec = mat * v.co
        v.co = vec


# LISTS FOR SELECTED & DUPLICATIONS #
name_list = []
new_list = []


def build_cone(self, context):    
    # add new dummy
    bpy.ops.view3d.snap_cursor_to_center()
    bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0))
    # store current mode
    #current_mode = bpy.context.mode
    #bpy.ops.object.mode_set(mode='EDIT')
    
    bpy.ops.object.editmode_toggle()
    
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_face_by_sides(type='GREATER')

    bpy.ops.object.editmode_toggle()
    
    # reload previous mode
    #bpy.ops.object.mode_set(mode=current_mode)  


# OPERATOR SET LOCAL #
class VIEWD3D_TP_SET_LOCAL(bpy.types.Operator):
    """ set local orientation to selected active face """
    bl_idname = "tp_ops.set_new_local"
    bl_label = "SetLocal"
    bl_context = "objectmode"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None


    # WIDGET #
    set_widget = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"None"   ),
               ("tp_w1"    ,"Local"     ,"Local"  ),
               ("tp_w2"    ,"Global"    ,"Global" )],
               name = "Set Widget",
               default = "tp_w1",    
               description = "widget orientation")
               
  
    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        box = layout.box().column(1)   

        row = box.row(1)
        row.label(text="Widget:")
        row.prop(self, "set_widget", expand = True)        
       
        box.separator() 


    def execute(self, context):
        active = bpy.context.active_object            
        selected = bpy.context.selected_objects

                        
        if context.space_data.local_view is not None:
            bpy.ops.view3d.localview()

        n = len(selected)
        if n == 1:
        

            for obj in selected:
                name_list.append(obj.name)
                      
                build_cone(self, context)

                # keep layer
                layers = []
                for i in obj.layers:
                    layers.append(i)
                bpy.ops.object.move_to_layer(layers = layers)
                
                bpy.context.object.name = "local_dummy"
                bpy.context.object.data.name = "local_dummy"

                new_list.append("local_dummy")
               
                bpy.ops.object.select_all(action = 'DESELECT') 
                bpy.data.objects["local_dummy"].select = True    

                # set first in list active
                bpy.data.objects[obj.name].select = True 
                bpy.context.scene.objects.active = selected[0]
                

                # set dummy to selected face
                bpy.ops.object.align_by_faces()
                
                # Set Euler mode
                bpy.context.object.rotation_mode = 'XYZ'
 
                # set second in list active                
                bpy.context.scene.objects.active = bpy.data.objects["local_dummy"]


                source = bpy.context.active_object
                objects = bpy.context.selected_objects
                mat_source = source.rotation_euler.to_matrix()
                mat_source.invert()

                for ob in objects:
                    if ob != source:
                        mat_ob = ob.rotation_euler.to_matrix()
                        if ob.type == 'MESH':                
                            mat = mat_source * mat_ob
                            Rotate(ob.data, mat)
                            ob.rotation_euler = source.rotation_euler



                bpy.ops.object.select_all(action = 'DESELECT') 
                bpy.data.objects["local_dummy"].select = True            
                bpy.ops.object.delete()

                # set first in list active
                bpy.data.objects[obj.name].select = True 
                bpy.context.scene.objects.active = selected[0]

        else:
            self.report({'INFO'}, 'select only 1 object')
    
        del name_list[:]

        # Widget
        if self.set_widget == "tp_w0":
            pass
        if self.set_widget == "tp_w1":
            bpy.context.space_data.transform_orientation = 'LOCAL'              
        if self.set_widget == "tp_w2":
            bpy.context.space_data.transform_orientation = 'GLOBAL'  

        return {'FINISHED'}





#bl_info = { "name": "Align by faces", "author": "Tom Rethaller",
import math
from mathutils import Vector
from functools import reduce

def get_ortho(a,b,c):
    if c != 0.0 and -a != b:
        return [-b-c, a,a]
    else:
        return [c,c,-a-b]

def clamp(v,min,max):
    if v < min:
        return min
    if v > max:
        return max
    return v

def align_faces(from_obj, to_obj):
    fpolys = from_obj.data.polygons
    tpolys = to_obj.data.polygons
    fpoly = fpolys[fpolys.active]
    tpoly = tpolys[tpolys.active]
    
    to_obj.rotation_mode = 'QUATERNION'
    tnorm = to_obj.rotation_quaternion * tpoly.normal
    
    fnorm = fpoly.normal
    axis = fnorm.cross(tnorm)
    dot = fnorm.normalized().dot(tnorm.normalized())
    dot = clamp(dot, -1.0, 1.0)
    
    # Parallel faces need a new rotation vector
    if axis.length < 1.0e-8:
        axis = Vector(get_ortho(fnorm.x, fnorm.y, fnorm.z))
        
    from_obj.rotation_mode = 'AXIS_ANGLE'
    from_obj.rotation_axis_angle = [math.acos(dot) + math.pi, axis[0],axis[1],axis[2]]
    bpy.context.scene.update()  
    
    # Move from_obj so that faces match
    fvertices = [from_obj.data.vertices[i].co for i in fpoly.vertices]
    tvertices = [to_obj.data.vertices[i].co for i in tpoly.vertices]
    
    fbary = from_obj.matrix_world * (reduce(Vector.__add__, fvertices) / len(fvertices))
    tbary = to_obj.matrix_world * (reduce(Vector.__add__, tvertices) / len(tvertices))
    
    from_obj.location = tbary - (fbary - from_obj.location)

    # Set Euler mode
    from_obj.rotation_mode = 'XYZ'


class OBJECT_OT_AlignByFaces(bpy.types.Operator):
    """Align two objects by their highlighted active faces """
    bl_label = "Align by faces"
    bl_description= "Align two objects by their active faces"
    bl_idname = "object.align_by_faces"
    bl_options = {"INTERNAL"}

    @classmethod
    def poll(cls, context):
        for obj in context.selected_objects:
            if obj.type != 'MESH':
                return False
        return True

    def execute(self, context):
        objs_to_move = [o for o in context.selected_objects if o != context.active_object]
        for o in objs_to_move:
            align_faces(o, context.active_object)        
        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
