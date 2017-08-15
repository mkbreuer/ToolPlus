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
        'name': "Shrinkwrap Smooth",
        'author': "Kjartan Tysdal",
        'location': 'EditMode"',
        'description': "modeling tool",
        'category': "Mesh",
        'blender': (2, 7, 6),
        'version': (0, 2, 7),
        'wiki_url': 'http://www.kjartantysdal.com/scripts',
}


import bpy, bmesh 
from bpy.props import IntProperty, BoolProperty


class shrinkwrapSmooth(bpy.types.Operator):
        """Smooths the selected vertices by keep the original shape"""            
        bl_idname = "mesh.shrinkwrap_smooth"                
        bl_label = "Shrinkwrap Smooth"               
        bl_options = {'REGISTER', 'UNDO'} 

        pin = BoolProperty(name="Pin Selection Border", description="Pins the outer edge of the selection.", default = True)  
        subsurf = IntProperty(name="Subsurf Levels", description="More reliable, but slower results", default = 0, min = 0, soft_max = 4)  

        def execute(self, context):
                
                iterate = 6
                pin = self.pin
                data = bpy.context.object.data.name

                # Set up for vertex weight
                bpy.context.scene.tool_settings.vertex_group_weight = 1
                v_grps = len(bpy.context.object.vertex_groups.items())
                
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                org_ob = bpy.context.object.name

                # Create intermediate object
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False)
                bpy.context.object.data = bpy.data.meshes[data]
                tmp_ob = bpy.context.object.name


                bpy.ops.object.duplicate(linked=False)
                shrink_ob = bpy.context.object.name

                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=tmp_ob)
                bpy.context.scene.objects.active = bpy.data.objects[tmp_ob] 

                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                
                if v_grps >= 1:
                    for x in range(v_grps):
                        bpy.ops.object.vertex_group_add()
                    

                if pin == True:
                        bpy.ops.object.vertex_group_assign_new()
                        org_id = bpy.context.object.vertex_groups.active_index
                        
                        bpy.ops.object.vertex_group_assign_new()
                        sel = bpy.context.object.vertex_groups.active.name
                        sel_id = bpy.context.object.vertex_groups.active_index
                        
                        bpy.ops.mesh.region_to_loop()
                        bpy.ops.object.vertex_group_remove_from(use_all_groups=False, use_all_verts=False)
                        
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.mesh.region_to_loop()
                        bpy.ops.object.vertex_group_remove_from(use_all_groups=False, use_all_verts=False)
                        
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.vertex_group_select(sel_id)
                        
                        
                else:
                        bpy.ops.object.vertex_group_assign_new()
                        sel = bpy.context.object.vertex_groups.active.name    


                for x in range(iterate):
                        bpy.ops.object.modifier_add(type='SHRINKWRAP')
                        mod_id = (len(bpy.context.object.modifiers)-1)
                        shrink_name = bpy.context.object.modifiers[mod_id].name

                        bpy.context.object.modifiers[shrink_name].target = bpy.data.objects[shrink_ob]
                        bpy.context.object.modifiers[shrink_name].vertex_group = sel
                        
                        bpy.context.object.modifiers[shrink_name].wrap_method = 'PROJECT'
                        bpy.context.object.modifiers[shrink_name].use_negative_direction = True
                        bpy.context.object.modifiers[shrink_name].subsurf_levels = self.subsurf
                

                        bpy.ops.mesh.vertices_smooth(factor=1, repeat=1)


                        bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                        bpy.ops.object.convert(target='MESH')
                        bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                        

                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                
                
                
                bpy.ops.object.vertex_group_remove(all = False)
                bpy.ops.object.modifier_remove(modifier=shrink_name)

                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=shrink_ob)
                bpy.context.scene.objects.active = bpy.data.objects[shrink_ob] 

                #Delete all geo inside Shrink_Object
                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.delete(type='VERT')
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.delete(use_global=True)

                bpy.ops.object.select_pattern(pattern=tmp_ob)
                bpy.context.scene.objects.active = bpy.data.objects[tmp_ob] 


                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)

                if pin == True:
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.vertex_group_select(org_id)

                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.delete(use_global=False)


                bpy.ops.object.select_pattern(pattern=org_ob)
                bpy.context.scene.objects.active = bpy.data.objects[org_ob] 

                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                
                # Fix for Blender remembering the previous selection
                bpy.ops.object.vertex_group_assign_new()
                bpy.ops.object.vertex_group_remove(all = False)
                

                return {'FINISHED'}

#Adds buildCorner to the Addon      

class buildCorner(bpy.types.Operator):
        """Builds corner topology / select => 2 faces = L/R Mousemove for Offset"""
        bl_idname = "mesh.build_corner"
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





#Register and Unregister all the operators
def register():
        bpy.utils.register_class(shrinkwrapSmooth)

def unregister():
        bpy.utils.unregister_class(shrinkwrapSmooth)


if __name__ == "__main__":
        register()
 
 
