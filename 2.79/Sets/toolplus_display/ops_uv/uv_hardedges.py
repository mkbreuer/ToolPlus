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
    "name": "UVs_to_Hard_Edges",
    "author": "Ferran M.Clar",
    "version": (0, 1),
    "blender": (2, 7, 4),
    "location": "3D View -> Tools Panel",
    "description": "Sets the object UV islands borders' edges to hard edges and an Edge Split modifier",
    "category": "Object"}


import bpy
import bmesh


class UTHE_MainOperator(bpy.types.Operator):
    bl_idname = "uthe.main_operator"
    bl_label = "Split SK"
    bl_description = "Sets the object UV islands borders' edges to hard edges and an Edge Split modifier"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self,context):

        uv_maps = context.active_object.data.uv_textures.keys()
        if uv_maps:


            if context.active_object.mode != 'EDIT':
                bpy.ops.object.mode_set(mode = 'EDIT')
                
            bpy.ops.uv.seams_from_islands()

            bpy.ops.object.mode_set(mode = 'OBJECT')
            
            mesh = bpy.context.object.data
            
            bm = bmesh.new()
            bm.from_mesh(mesh)

            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_all(action='DESELECT')
            edges = []

            for edge in bm.edges:
                
                if edge.seam:
                    edge.smooth = False

                    
            bpy.ops.mesh.mark_sharp()

            bpy.ops.object.mode_set(mode = 'OBJECT')

            bm.to_mesh(mesh)
            bm.free()

    #        bpy.ops.object.mode_set(mode = 'EDIT')
            
            edgeSplit = context.object.modifiers.new(name = "EdgeSplit", type = 'EDGE_SPLIT')
            edgeSplit.use_edge_angle = False
            edgeSplit.use_edge_sharp = True

        else:
            
            msg ="!Need UVs"
            self.report( {"INFO"}, msg  )            
        
        return {'FINISHED'}

"""
class UTHE_Panel(bpy.types.Panel):
    bl_idname = "uvs_to_hardedges_panel"
    bl_label = "SUVs to hard edges panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Shading / UVs"
    
    @classmethod
    def poll(cls,context):
        return(context.active_object.type == 'MESH')
        #return((context.active_object.type == 'MESH') and (context.active_object.mode == 'EDIT'))
    
    def draw(self, context):
        layout = self.layout
        add = layout.row()
        add.operator("uthe.main_operator", text = "UVs to Hard Edges", icon = 'MOD_EDGESPLIT')
"""    
def register():
    
    bpy.utils.register_class(UTHE_MainOperator)
    #bpy.utils.register_class(UTHE_Panel)
    
def unregister():
    
    bpy.utils.unregister_class(UTHE_MainOperator)
    #bpy.utils.unregister_class(UTHE_Panel)

if __name__ == "__main__":
    register()