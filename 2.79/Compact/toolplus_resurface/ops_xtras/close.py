# ##### BEGIN GPL LICENSE BLOCK #####
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

import bpy
from bpy import*
from bpy.props import *


class VIEW3D_TP_Purge_Mesh(bpy.types.Operator):
    '''Purge orphaned mesh'''
    bl_idname="purge.unused_mesh_data"
    bl_label="Purge Mesh"
    bl_options = {"REGISTER", 'UNDO'}    

    def execute(self, context):

        target_coll = eval("bpy.data.meshes")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}




class VIEW3D_TP_CloseFaces(bpy.types.Operator):
    """Close selected face or border with triangle or quads"""
    bl_idname = "mesh.close_faces"
    bl_label = "Close Face & Border"
    bl_options = {'REGISTER', 'UNDO'}
    
    tris = bpy.props.BoolProperty(name="Tris", description="", default=True) 
    quads = bpy.props.BoolProperty(name="Quads", description="", default=False) 
    inset = bpy.props.IntProperty(name="Inset", description="", default=0, min=0, soft_max=100, step=1) 
    
    def draw(self, context):
        layout = self.layout.column(1)       

        row = layout.column(1)      
        row.prop(self, 'tris', text="Tris", icon ="OUTLINER_DATA_MESH")  
        row.prop(self, 'quads', text="Quads", icon ="OUTLINER_DATA_LATTICE")          
        row.prop(self, 'inset', text="Inset", icon ="PROP_OFF")  


    def execute(self, context):

        for i in range(self.tris):       
            bpy.ops.mesh.edge_face_add()             
            bpy.ops.mesh.poke()
       
        for i in range(self.quads):   
            bpy.ops.mesh.edge_face_add()
            bpy.ops.mesh.region_to_loop()
             
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

            me = bpy.context.object.data
            bm = bmesh.new()    
            bm.from_mesh(me)  

            face_sel = []
            edge_sel = []
            
            for v in bm.faces:
                    if v.select:
                            face_sel.append(v.index)
            for v in bm.edges:
                    if v.select:
                            edge_sel.append(v.index)
            
            bm.to_mesh(me)
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.mesh.loop_to_region()

            bpy.ops.mesh.edge_face_add()
                    
            bpy.ops.mesh.poke()
            
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            
            bpy.ops.object.vertex_group_assign_new()
            sel_id = bpy.context.object.vertex_groups.active_index

            bpy.ops.mesh.region_to_loop()
            bpy.ops.object.vertex_group_remove_from()

            bpy.ops.mesh.select_nth(nth=2, skip=1)

            bpy.ops.object.vertex_group_select(sel_id)

            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            bpy.ops.mesh.dissolve_mode(use_verts=False)

            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.object.vertex_group_select()
            bpy.ops.mesh.select_more()

            bpy.ops.object.vertex_group_remove(all = False)
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')


        for i in range(self.inset):       
            bpy.ops.mesh.inset(thickness=0.025)   

        #print(self)
        #self.report({'INFO'}, "CloseFace")  
        return {'FINISHED'}        

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 100)  




# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():  
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 