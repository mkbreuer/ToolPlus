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
    "name": "Close Faces",
    "author": "MKB",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Editmode > Extrude Menu > ALT+E",
    "description": "Close Faces with Quads or Tris",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"}



import bpy, bmesh
from bpy import*


class CloseFaces(bpy.types.Operator):
    """Close selected face or border with triangle or quads"""
    bl_idname = "mesh.closer"
    bl_label = "Close Face & Border"
    bl_options = {'REGISTER', 'UNDO'}
    
    tris = bpy.props.BoolProperty(name="Tris", description="", default=False) 
    quads = bpy.props.BoolProperty(name="Quads", description="", default=True) 
    inset = bpy.props.IntProperty(name="Inset", description="", default=0, min=0, soft_max=100, step=1) 
    scale = bpy.props.IntProperty(name="Scale", description="", default=0, min=0, soft_max=50, step=1) 
    flat = bpy.props.IntProperty(name="Flat", description="", default=0, min=0, soft_max=100, step=1) 
    moveplus = bpy.props.IntProperty(name="Move+", description="", default=0, min=0, soft_max=1000, step=1) 
    moveminus = bpy.props.IntProperty(name="Move-", description="", default=0, min=0, soft_max=1000, step=1) 
    
    def draw(self, context):
        layout = self.layout.column(1)       

        row = layout.column(1)      
        row.prop(self, 'tris', text="Tris", icon ="OUTLINER_DATA_MESH")  
        row.prop(self, 'quads', text="Quads", icon ="OUTLINER_DATA_LATTICE")          
        row.prop(self, 'inset', text="Inset", icon ="PROP_OFF")  

        row = layout.row(1)  
        row.prop(self, 'scale', text="Scale", icon ="MAN_SCALE")  
        row.prop(self, 'flat', text="Flat", icon ="MOD_DISPLACE")  
        
        row = layout.row(1)  
        row.prop(self, 'moveplus', text="Move+", icon ="MAN_TRANS")  
        row.prop(self, 'moveminus', text="Move-", icon ="MAN_TRANS")  


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
            bpy.ops.mesh.inset(thickness=0.2)   

        for i in range(self.scale):       
            bpy.ops.transform.resize(value=(0.99, 0.99, 0.99), constraint_axis=(True, True, False), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        for i in range(self.flat):       
            bpy.ops.transform.resize(value=(0.99, 0.99, 0.99), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        for i in range(self.moveplus):       
            bpy.ops.transform.translate(value=(0.00, 0.00, 0.01), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
 
        for i in range(self.moveminus):       
            bpy.ops.transform.translate(value=(0.00, 0.00, -0.01), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
  
        return {'FINISHED'}        


def register():

    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()






