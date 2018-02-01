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




#bl_info = {
#        'name': "Kjartans Scripts",
#        'author': "Kjartan Tysdal",
#        'location': '"Shift+Q" and also in EditMode "W-Specials/ KTools"',
#        'description': "Adds my personal collection of small handy scripts (mostly modeling tools)",
#        'category': "Mesh",
#        'blender': (2, 7, 6),
#        'version': (0, 2, 7),
#        'wiki_url': 'http://www.kjartantysdal.com/scripts',
#}


# LOAD MODUL #    
import bpy, bmesh 
from bpy import *
from bpy.props import *



#Adds buildCorner to the Addon      
class VIEW_3D_TP_Build_Corner(bpy.types.Operator):
        """Builds corner topology / select => 2 faces = L/R Mousemove for Offset"""
        bl_idname = "tp_ops.build_corner"
        bl_label = "Build Corner"
        bl_options = {'REGISTER', 'UNDO'} 

        offset = IntProperty()
        
        def modal(self, context, event):
                
                if event.type == 'MOUSEMOVE':
                        
                        delta = self.offset - event.mouse_x
                        
                        if delta >= 0:
                                offset = 1
                        else:
                                offset = 0
                                
                        bpy.ops.mesh.edge_face_add()
                                
                        bpy.ops.mesh.poke()
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.object.vertex_group_assign_new()
                        sel_id = bpy.context.object.vertex_groups.active_index

                        bpy.ops.mesh.region_to_loop()
                        bpy.ops.object.vertex_group_remove_from()

                        bpy.ops.mesh.select_nth(nth=2, skip=1, offset=offset)

                        bpy.ops.object.vertex_group_select(sel_id)

                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
                        bpy.ops.mesh.dissolve_mode(use_verts=False)

                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.object.vertex_group_select()
                        bpy.ops.mesh.select_more()

                        bpy.ops.object.vertex_group_remove(all = False)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                                

                elif event.type == 'LEFTMOUSE':
                        return {'FINISHED'}

                elif event.type in {'RIGHTMOUSE', 'ESC'}:
                    bpy.ops.ed.undo()
                    return {'CANCELLED'}

                return {'RUNNING_MODAL'}

        def invoke(self, context, event):
                if context.object:
                        
                        # Check selection
                        
                        bpy.ops.mesh.edge_face_add()
                        bpy.ops.mesh.region_to_loop()
                         
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        me = bpy.context.object.data
                        bm = bmesh.new()     # create an empty BMesh
                        bm.from_mesh(me)     # fill it in from a Mesh

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

                        
                        ###################################
                        
                        edge_sel = len(edge_sel)
                        
                        if edge_sel == 4:
                                return {'FINISHED'}
                        
                        elif edge_sel%2 == 0:
                                self.offset = event.mouse_x
                                context.window_manager.modal_handler_add(self)
                                return {'RUNNING_MODAL'}
                        
                        #elif edge_sel == 5:
                        #    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
                        #    bpy.ops.mesh.tris_convert_to_quads(face_threshold=3.14159, shape_threshold=3.14159)
                        #    return {'FINISHED'}
                                
                        else:
                                bpy.ops.mesh.poke()
                                bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
                                bpy.ops.mesh.tris_convert_to_quads(face_threshold=3.14159, shape_threshold=3.14159)
                                return {'FINISHED'}

                else:
                        self.report({'WARNING'}, "No active object, could not finish")
                        return {'CANCELLED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()