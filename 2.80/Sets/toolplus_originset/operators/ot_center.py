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
import math
import bpy
import bmesh
import mathutils
from mathutils import geometry
from mathutils import Vector
from bpy.props import (BoolProperty, IntProperty)
from bpy_extras import view3d_utils

# snippet from tinycad: CCEN without mesh creation
# author:  zeffii (aka Dealga McArdle)
def generate_3PT_mode_1_(pts, obj):
    origin = obj.location
    transform_matrix = obj.matrix_local
    V = Vector

    # construction
    v1, v2, v3, v4 = V(pts[0]), V(pts[1]), V(pts[1]), V(pts[2])
    edge1_mid = v1.lerp(v2, 0.5)
    edge2_mid = v3.lerp(v4, 0.5)
    axis = geometry.normal(v1, v2, v4)
    mat_rot = mathutils.Matrix.Rotation(math.radians(90.0), 4, axis)

    # triangle edges
    v1_ = ((v1 - edge1_mid) @ mat_rot) + edge1_mid
    v2_ = ((v2 - edge1_mid) @ mat_rot) + edge1_mid
    v3_ = ((v3 - edge2_mid) @ mat_rot) + edge2_mid
    v4_ = ((v4 - edge2_mid) @ mat_rot) + edge2_mid

    r = geometry.intersect_line_line(v1_, v2_, v3_, v4_)
    if r:
        p1, _ = r
        # cp = transform_matrix @ (p1 + origin)
        cp = transform_matrix @ p1
        bpy.context.scene.cursor.location = cp
        # generate_gp3d_stroke(cp, axis, obj, radius=(p1-v1).length)
    else:
        print('not on a circle')

def get_three_verts_from_selection_(obj):
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    if hasattr(bm.verts, "ensure_lookup_table"):
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()

    return [v.co[:] for v in bm.verts if v.select]



class VIEW3D_OT_origin_to_circle_center(bpy.types.Operator):
    """[RMB+SHIFT] = select 3 verts set origin to a circle center"""
    bl_idname = "tpc_ops.origin_to_ccc"
    bl_label = "Origin to Circle Center"

    # property to define mouse event
    x : bpy.props.IntProperty()
    
    # print info in system console
    def __init__(self):
        # attribute instance
        self._activElem = None
        self._VertList = None
        print("Start")

    def __del__(self):
        print("End")

    def store(self):            
        # store settings
        self.store_select_x_mode : bpy.context.tool_settings.mesh_select_mode[0]  
        self.store_select_y_mode : bpy.context.tool_settings.mesh_select_mode[1] 
        self.store_select_z_mode : bpy.context.tool_settings.mesh_select_mode[2]              
        store_mode : bpy.context.object.mode

    def modal(self, context, event):

        # call event property
        self.x = event.mouse_x
       
        if event.type == 'RIGHTMOUSE': # confirm modal
                     
            view_layer = bpy.context.view_layer        

            obj = view_layer.objects.active
            obj.update_from_editmode()  
            mesh = obj.data
            bm = bmesh.from_edit_mesh(mesh)
            activElem2Type = bm.select_history.active           
           
            if activElem2Type:                             
                if isinstance(activElem2Type, bmesh.types.BMVert):
                    print("vertex")
                    activElem2=bm.select_history.active.co               

                    selected_verts = [v for v in bm.verts if v.select]                           
                    if len(selected_verts) >= 3:  
                        
                        mat = obj.matrix_world
                        loc = mat @ activElem2                            
                        
                        obj = bpy.context.object
                        pts = get_three_verts_from_selection_(obj)
                        generate_3PT_mode_1_(pts, obj)

                        bpy.ops.mesh.select_all(action='TOGGLE')
                           
                        bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                        bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                        bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                         
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')                                                                                                              
                        bpy.ops.object.mode_set ( mode = self.store_mode )                     
              
                        return {'FINISHED'}

                return {'PASS_THROUGH'}                    
            else:
                return {'PASS_THROUGH'}
           
        if event.type in {'ESC',"TAB",'LEFTTMOUSE'}:
            #self.cancel(context)
            return {'CANCELLED'}

        return {'PASS_THROUGH'}


    def invoke(self, context, event):
      
        #check if something selected
        if context.space_data.type == 'VIEW_3D':
          
            #check if something selected
            if bpy.context.active_object is not None:   
                                             
                self.store_mode = bpy.context.object.mode 
                self.store_select_x_mode = bpy.context.tool_settings.mesh_select_mode[0]  
                self.store_select_y_mode = bpy.context.tool_settings.mesh_select_mode[1] 
                self.store_select_z_mode = bpy.context.tool_settings.mesh_select_mode[2]  

                bpy.context.tool_settings.mesh_select_mode = (True, False, False)   
                bpy.ops.mesh.select_all(action='DESELECT')

                wm = context.window_manager                           
                wm.modal_handler_add(self) 

                # call property
                self.x = event.mouse_x             
                
            else:
                pass   

            return {'RUNNING_MODAL'}

        else:
            self.report({'WARNING'}, "Must be 3D View")  
            return {'CANCELLED'}



def register():
    bpy.utils.register_class(VIEW3D_OT_origin_to_circle_center)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_origin_to_circle_center)

if __name__ == "__main__":
    register()
