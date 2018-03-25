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


# taken form tinycad: CCEN without mesh creation
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
    v1_ = ((v1 - edge1_mid) * mat_rot) + edge1_mid
    v2_ = ((v2 - edge1_mid) * mat_rot) + edge1_mid
    v3_ = ((v3 - edge2_mid) * mat_rot) + edge2_mid
    v4_ = ((v4 - edge2_mid) * mat_rot) + edge2_mid

    r = geometry.intersect_line_line(v1_, v2_, v3_, v4_)
    if r:
        p1, _ = r
        # cp = transform_matrix * (p1 + origin)
        cp = transform_matrix * p1
        bpy.context.scene.cursor_location = cp
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




# OPERATOR #

class VIEW3D_TP_CircleCenterCursor(bpy.types.Operator):
    """circle center of three selected vertices"""
    bl_idname = 'tp_ops.tinycad_ccc'
    bl_label = 'circle center from selected'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        obj = context.active_object
        return obj is not None and obj.type == 'MESH' and obj.mode == 'EDIT'

    def execute(self, context):
        obj = bpy.context.object
        pts = get_three_verts_from_selection_(obj)
        generate_3PT_mode_1_(pts, obj)
        return {'FINISHED'}



class View3D_TP_Origin_to_CCC(bpy.types.Operator):
    '''Set Origin to 3point Circle Center'''
    bl_idname = "tp_ops.origin_ccc"
    bl_label = "Origin to 3PCC"
    bl_options = {"REGISTER", 'UNDO'}   

    #tp_mode = bpy.props.BoolProperty(name="Switch Mode",  description=" ", default=True, options={'SKIP_SAVE'})    

    def execute(self, context):

        #check for mesh selections
        object = context.object
        object.update_from_editmode()
        mesh_bm = bmesh.from_edit_mesh(object.data)
        selected_verts = [v for v in mesh_bm.verts if v.select]

        # check if local view
        if context.space_data.local_view is not None:
           
            # jump out from local view
            bpy.ops.view3d.localview()

            print(self)
            self.report({'INFO'}, 'Not possible in local mode!')  
 
        # check wich select mode is active        
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False): 
            if len(selected_verts) >= 3:            

                # cursor 3point circle center
                bpy.ops.tp_ops.tinycad_ccc()
                
                bpy.ops.mesh.select_all(action='TOGGLE')
                
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')        
                bpy.ops.object.editmode_toggle()

            else:            
                print(self)
                self.report({'INFO'}, 'Need 3 Verts!')  
        else:
            pass       
    
        return{'FINISHED'}  




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()