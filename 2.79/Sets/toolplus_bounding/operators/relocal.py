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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *

import bmesh
import math
import mathutils
from mathutils import Vector
from functools import reduce


# LOCAL ORIENTATION #
def local_rotate(mesh, mat):
    for v in mesh.vertices:
        vec = mat * v.co
        v.co = vec


# ALIGN TO FACE #
#"author": "Tom Rethaller"
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

def align_to_active_faces(from_obj, to_obj):

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



# LISTS FOR SELECTED & DUPLICATIONS #
name_list = []
new_list = []



def set_local_operator(self, context):
    active = bpy.context.active_object            
    selected = bpy.context.selected_objects

    n = len(selected)
    if n == 1:    

        for obj in selected:
            
            name_list.append(obj.name)

            # add new dummy
            bpy.ops.view3d.snap_cursor_to_center()
            bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0))

            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.select_face_by_sides(type='GREATER')
            bpy.ops.object.editmode_toggle()
            
            bpy.context.object.name = "local_dummy"
            bpy.context.object.data.name = "local_dummy"

            new_list.append("local_dummy")
           
            bpy.ops.object.select_all(action = 'DESELECT') 
            bpy.data.objects["local_dummy"].select = True    

            # set first in list active
            bpy.data.objects[obj.name].select = True 
            bpy.context.scene.objects.active = selected[0]
                                    
            # set dummy to selected face
            objs_to_move = [o for o in context.selected_objects if o != context.active_object]
            for o in objs_to_move:
                align_to_active_faces(o, context.active_object)   

            # Set Euler mode
            bpy.context.object.rotation_mode = 'XYZ'
         
            # set second in list active                
            bpy.context.scene.objects.active = bpy.data.objects["local_dummy"]


            active_source = bpy.context.active_object            
            selected_target = bpy.context.selected_objects

            mat_source = active_source.rotation_euler.to_matrix()
            mat_source.invert()

            for ob in selected_target:
                if ob != selected_target:
                    mat_ob = ob.rotation_euler.to_matrix()
                    if ob.type == 'MESH':                
                        mat = mat_source * mat_ob
                        local_rotate(ob.data, mat)
                        ob.rotation_euler = active_source.rotation_euler



            bpy.ops.object.select_all(action = 'DESELECT') 
            bpy.data.objects["local_dummy"].select = True            
            bpy.ops.object.delete()

            # set first in list active
            bpy.data.objects[obj.name].select = True 
            bpy.context.scene.objects.active = selected[0]

            
    else:
        self.report({'INFO'}, 'select only 1 object')

    return



# OPERATOR SET LOCAL #
class VIEWD3D_TP_SET_LOCAL(bpy.types.Operator):
    """ set local orientation to 1 selected face """
    bl_idname = "tp_ops.set_new_local"
    bl_label = "ReLocal"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    widget = bpy.props.EnumProperty(
        items=[("tp_0"    ,"None"      ,"None"   ),
               ("tp_1"    ,"Local"     ,"Local"  ),
               ("tp_2"    ,"Global"    ,"Global" )],
               name = "Widget Orientation",
               default = "tp_0",    
               description = "widget orientation")
               
                 
    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(1)   

        row = box.row(1)
        row.label(text="Widget:")
        row.prop(self, "widget", expand = True)        
       
        box.separator()   


    def execute(self, context):

        if context.space_data.local_view:
           # stay in local view           
            bpy.ops.view3d.localview()                                                       
            if bpy.context.object.mode == "EDIT":
                bpy.ops.object.editmode_toggle()                                 
                set_local_operator(self, context)                        
                bpy.ops.object.editmode_toggle()
            else:
                set_local_operator(self, context)   
            bpy.ops.view3d.localview()

        else:
            if bpy.context.object.mode == "EDIT":
                bpy.ops.object.editmode_toggle()                                 
                set_local_operator(self, context)                        
                bpy.ops.object.editmode_toggle()
            else:
                set_local_operator(self, context)   


        # set widget orientation
        if self.widget == "tp_0":
            pass            
        elif self.widget == "tp_1":
            bpy.context.space_data.transform_orientation = 'LOCAL'            
        else:
            bpy.context.space_data.transform_orientation = 'GLOBAL'  
            
        del name_list[:]
        return {'FINISHED'}



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()




