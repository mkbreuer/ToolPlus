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



"""
bl_info = {
        'name': "Kjartans Scripts",
        'author': "Kjartan Tysdal",
        'location': '"Shift+Q" and also in EditMode "W-Specials/ KTools"',
        'description': "Adds my personal collection of small handy scripts (mostly modeling tools)",
        'category': "Mesh",
        'blender': (2, 7, 6),
        'version': (0, 2, 7),
        'wiki_url': 'http://www.kjartantysdal.com/scripts',
}
"""

import bpy, bmesh 
from bpy.props import *


        
#Adds growLoop to the Addon  

class growLoop(bpy.types.Operator):
        """Grows the selected edges in both directions """          
        bl_idname = "mesh.grow_loop"                
        bl_label = "Grow Loop"               
        bl_options = {'REGISTER', 'UNDO'} 

        grow = IntProperty(name="Grow Selection", description="How much to grow selection", default= 1, min=1, soft_max=10)
        
        def execute(self, context):
                
                grow = self.grow
                sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                
                for x in range(grow):
                        if sel_mode[2] == True:
                        
                                edge_sel = []
                                border = []
                                interior = []
                                face_org = []
                                face_loop = []
                                face_grow = []
                                face_sel = []
                                mesh_edges = bpy.context.active_object.data.edges
                                mesh_faces = bpy.context.active_object.data.polygons

                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')   

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)

                                for e in bm.edges:
                                        if e.select:
                                                edge_sel.append(e.index)

                                for f in bm.faces:
                                        if f.select:
                                                face_org.append(f.index)

                                bpy.ops.mesh.region_to_loop()

                                for e in bm.edges:
                                        if e.select:
                                                border.append(e.index)
                                                


                                for e in edge_sel:
                                        if e not in border:
                                                interior.append(e)

                                bmesh.update_edit_mesh(me, True, False)


                                bpy.ops.mesh.select_all(action='DESELECT')

                                #Select the interior edges
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)


                                for e in interior:
                                        mesh_edges[e].select = True

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                                bpy.ops.mesh.loop_multi_select(ring=True)
                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)

                                for f in bm.faces:
                                        if f.select:
                                                face_loop.append(f.index)

                                bmesh.update_edit_mesh(me, True, False)

                                bpy.ops.mesh.select_all(action='DESELECT')


                                # Select original faces
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                for x in face_org:
                                        mesh_faces[x].select = True
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)


                                bpy.ops.mesh.select_more(use_face_step=False)

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)

                                for f in bm.faces:
                                        if f.select:
                                                face_grow.append(f.index)

                                for f in face_grow:
                                        if f in face_loop:
                                                face_sel.append(f)
                                                
                                for f in face_org:
                                        face_sel.append(f)
                                                
                                bmesh.update_edit_mesh(me, True, False)

                                bpy.ops.mesh.select_all(action='DESELECT')

                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                                for f in face_sel:
                                        mesh_faces[f].select = True

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                        else:
                                mesh = bpy.context.active_object.data.edges

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)
                                org_sel = []
                                grow_sel = []
                                loop_sel = []
                                sel = []

                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')

                                for e in bm.edges:
                                        if e.select:
                                                org_sel.append(e.index)
                                                
                                bpy.ops.mesh.select_more(use_face_step=False)

                                for e in bm.edges:
                                        if e.select:
                                                grow_sel.append(e.index)

                                bpy.ops.mesh.select_all(action='DESELECT')

                                bmesh.update_edit_mesh(me, True, False)
                                
                                # Select the original edges
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                for e in org_sel:
                                        mesh[e].select = True                               
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                                
                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)
                                bpy.ops.mesh.loop_multi_select(ring=False)

                                for e in bm.edges:
                                        if e.select:
                                                loop_sel.append(e.index)

                                bmesh.update_edit_mesh(me, True, False)

                                bpy.ops.mesh.select_all(action='DESELECT')

                                for x in loop_sel:
                                        if x in grow_sel:
                                                sel.append(x)
                                                
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                for e in sel:
                                        mesh[e].select = True                               
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)  
                        
                        bpy.context.tool_settings.mesh_select_mode = sel_mode
                
                return {'FINISHED'}

#Adds extendLoop to the Addon    

class extendLoop(bpy.types.Operator):
        """Uses the active face or edge to extends the selection in one direction"""            
        bl_idname = "mesh.extend_loop"              
        bl_label = "Extend Loop"                 
        bl_options = {'REGISTER', 'UNDO'} 

        extend = IntProperty(name="Extend Selection", description="How much to extend selection", default= 1, min=1, soft_max=10)
        
        def execute(self, context):
                
                sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                extend = self.extend
                
                for x in range(extend):
                    if sel_mode[2] == True:
                        
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        active_face = bpy.context.object.data.polygons.active # find active face
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        edge_sel = []
                        interior = []
                        face_org = []
                        face_loop = []
                        face_grow = []
                        face_sel = []
                        active_edges = []

                        # Get face selection
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for f in bm.faces:
                                if f.select:
                                        face_org.append(f.index)
                                        
                        face_org.remove(active_face)


                        bmesh.update_edit_mesh(me, True, False)

                        bpy.ops.mesh.select_all(action='DESELECT')
                        mesh = bpy.context.active_object.data.polygons

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        for x in face_org:
                                mesh[x].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)



                        # Get edge selection
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for e in bm.edges:
                                if e.select:
                                        edge_sel.append(e.index)


                        bmesh.update_edit_mesh(me, True, False)


                        # Select Active Face
                        bpy.ops.mesh.select_all(action='DESELECT')
                        mesh = bpy.context.active_object.data.polygons

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh[active_face].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')

                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)


                        # Store the interior edge

                        for e in bm.edges:
                                if e.select:
                                        active_edges.append(e.index)
                                        

                        for e in active_edges:
                                if e in edge_sel:
                                        interior.append(e)

                        bmesh.update_edit_mesh(me, True, False)


                        bpy.ops.mesh.select_all(action='DESELECT')

                        #Select the interior edges
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        mesh = bpy.context.active_object.data.edges

                        for e in interior:
                                mesh[e].select = True

                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)


                        bpy.ops.mesh.loop_multi_select(ring=True)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')


                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for f in bm.faces:
                                if f.select:
                                        face_loop.append(f.index)

                                        
                        bmesh.update_edit_mesh(me, True, False)

                        bpy.ops.mesh.select_all(action='DESELECT')

                        # Select active face
                        mesh = bpy.context.active_object.data.polygons

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh[active_face].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.select_more(use_face_step=False)


                        face_org.append(active_face)

                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for f in bm.faces:
                                if f.select:
                                        face_grow.append(f.index)

                        for f in face_grow:
                                if f in face_loop:
                                        face_sel.append(f)
                                        
                        for f in face_sel:
                                if f not in face_org:
                                        active_face = f
                                        
                        for f in face_org:
                                face_sel.append(f)
                                        
                        bmesh.update_edit_mesh(me, True, False)

                        bpy.ops.mesh.select_all(action='DESELECT')

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        for f in face_sel:
                                mesh[f].select = True
                        bpy.context.object.data.polygons.active = active_face

                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                    elif sel_mode[1] == True:

                        mesh = bpy.context.active_object.data
                        org_sel = []
                        grow_sel = []
                        loop_sel = []
                        sel = []
                        org_verts = []
                        active_verts = []
                        
                        # Get active edge
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for x in reversed(bm.select_history):
                                if isinstance(x, bmesh.types.BMEdge):
                                        active_edge = x.index
                                        break

                        # Store the originally selected edges
                        for e in bm.edges:
                                if e.select:
                                        org_sel.append(e.index)
                                        

                        bmesh.update_edit_mesh(me, True, False)
                                        
                        # Select active edge
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh.edges[active_edge].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        # Get verts of active edge
                        bm = bmesh.from_edit_mesh(me)
                        
                        for v in bm.verts:
                                if v.select:
                                        active_verts.append(v.index)
                                        
                        bmesh.update_edit_mesh(me, True, False)
                        
                        # Select original selection minus active edge
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        for x in org_sel:
                            mesh.edges[x].select = True
                        mesh.edges[active_edge].select = False
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                        bm = bmesh.from_edit_mesh(me)
                        
                        # Store the original vertices minus active edge
                        for v in bm.verts:
                            if v.select:
                                org_verts.append(v.index)
                        
                        
                        # Compare verts
                        for x in active_verts:
                            if x in org_verts:
                                active_verts.remove(x)
                        
                        bmesh.update_edit_mesh(me, True, False)
                        
                        # Select end vertex
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh.vertices[active_verts[0]].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                        
                        # Grow the end vertex and store the edges
                        bpy.ops.mesh.select_more(use_face_step=False)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
                        bm = bmesh.from_edit_mesh(me)
                        
                        for e in bm.edges:
                                if e.select:
                                        grow_sel.append(e.index)

                        bmesh.update_edit_mesh(me, True, False)
                        bpy.ops.mesh.select_all(action='DESELECT')

                        # Run loop of the active edges and store it
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh.edges[active_edge].select = True                   
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.loop_multi_select(ring=False)

                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for e in bm.edges:
                                if e.select:
                                        loop_sel.append(e.index)

                        bmesh.update_edit_mesh(me, True, False)
                        bpy.ops.mesh.select_all(action='DESELECT')

                        # Compare loop_sel vs grow_sel
                        for x in loop_sel:
                                if x in grow_sel:
                                        sel.append(x)


                        # Add original selection to new selection

                        for x in org_sel:
                            if x not in sel:
                                sel.append(x)
                                

                        # Compare org_sel with sel to get the active edge
                        for x in sel:
                            if x not in org_sel:
                                active_edge = x
                                
                        # Select the resulting edges
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        for e in sel:
                                mesh.edges[e].select = True                             
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        # Set the new active edge
                        bm = bmesh.from_edit_mesh(me)

                        bm.edges.ensure_lookup_table()
                        bm.select_history.add(bm.edges[active_edge])
                        bmesh.update_edit_mesh(me, True, False)
                        
                
                return {'FINISHED'}


#Adds extendLoop to the Addon    

class shrinkLoop(bpy.types.Operator):
        """Shrink the selected loop """          
        bl_idname = "mesh.shrink_loop"              
        bl_label = "Shrink Loop"                 
        bl_options = {'REGISTER', 'UNDO'} 

        shrink = IntProperty(name="Shrink Selection", description="How much to shrink selection", default= 1, min=1, soft_max=15)
        
        def execute(self, context):
                
                sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                shrink = self.shrink
                
                for x in range(shrink):
                    if sel_mode[2] == True:
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)
                        mesh = bpy.context.active_object.data

                        sel = []
                        edge_dic = {}
                        vert_list = []
                        end_verts = []
                        org_faces = []
                        cur_faces = []
                        new_faces = []

                        # Store edges and verts
                        for e in bm.edges:
                            if e.select:
                                sel.append(e.index)
                                
                                # Populate vert_list
                                vert_list.append(e.verts[0].index)
                                vert_list.append(e.verts[1].index)
                                
                                # Store dictionary
                                edge_dic[e.index] = [e.verts[0].index, e.verts[1].index]

                        # Store original faces
                        for f in bm.faces:
                            if f.select:
                                org_faces.append(f.index)

                        # Store end verts
                        for v in vert_list:
                            if vert_list.count(v) == 2:
                                end_verts.append(v)
                                
                        # Check verts in dictionary
                        for key, value in edge_dic.items():
                            if value[0] in end_verts:
                                sel.remove(key)
                                continue
                            if value[1] in end_verts:
                                sel.remove(key)


                        bmesh.update_edit_mesh(me, True, False)

                        # Select the resulting edges
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        for e in sel:
                            mesh.edges[e].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')

                        bm = bmesh.from_edit_mesh(me)

                        # Store current faces
                        for f in bm.faces:
                            if f.select:
                                cur_faces.append(f.index)

                        # Compare current and original faces
                        for x in org_faces:
                            if x in cur_faces:
                                new_faces.append(x)

                        bmesh.update_edit_mesh(me, True, False)

                        # Select the resulting faces
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        for e in new_faces:
                            mesh.polygons[e].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    
                    else:
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        sel = []
                        edge_dic = {}
                        vert_list = []
                        end_verts = []

                        # Store edges and verts in dictionary
                        for e in bm.edges:
                            if e.select:
                                sel.append(e.index)
                                
                                # Populate vert_list
                                vert_list.append(e.verts[0].index)
                                vert_list.append(e.verts[1].index)
                                
                                # Store dictionary
                                edge_dic[e.index] = [e.verts[0].index, e.verts[1].index]

                        # Store end verts
                        for v in vert_list:
                            if vert_list.count(v) == 1:
                                end_verts.append(v)
                                
                        # Check verts in dictionary
                        for key, value in edge_dic.items():
                            if value[0] in end_verts:
                                sel.remove(key)
                                continue
                            if value[1] in end_verts:
                                sel.remove(key)


                        bmesh.update_edit_mesh(me, True, False)

                        # Select the resulting edges
                        bpy.ops.mesh.select_all(action='DESELECT')

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh = bpy.context.active_object.data.edges
                        for e in sel:
                            mesh[e].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                
                return {'FINISHED'}




class pathSelectRing(bpy.types.Operator):
    """Selects the shortest edge ring path / only edge mode"""
    bl_idname = "mesh.path_select_ring"
    bl_label = "Path Select Ring"
    bl_options = {'REGISTER', 'UNDO'} 
    
    pick = BoolProperty(name = "Pick Mode", description = "Pick Mode", default = False)
    collapse = BoolProperty(name = "Collapse", description = "Collapses everything between your two selected edges", default = False)

    def draw(self, context):
        layout = self.layout

    
    def execute(self, context):
        
        me = bpy.context.object.data
        bm = bmesh.from_edit_mesh(me)
        mesh = bpy.context.active_object.data
        sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
        
        org_sel = []
        start_end = []
        active_edge = []
        border_sel = []
        vert_sel = []
        face_sel = []
        
        if sel_mode[1]:
            
            bpy.context.tool_settings.mesh_select_mode = [False, True, False]
            
            if self.pick:
                bpy.ops.view3d.select('INVOKE_DEFAULT', extend=True, deselect=False, toggle=False)
            

            # Store the Start and End edges 
            iterate = 0
            for e in reversed(bm.select_history):
                if isinstance(e, bmesh.types.BMEdge):
                    iterate += 1
                    start_end.append(e)
                    if iterate >= 2:
                        break 
            
            if len(start_end) <= 1:
                if self.collapse:
                    bpy.ops.mesh.merge(type='COLLAPSE', uvs=True)
                    return{'FINISHED'}
                return{'CANCELLED'}
            
            # Store active edge
            for e in reversed(bm.select_history):
                if isinstance(e, bmesh.types.BMEdge):
                    active_edge = e.index
                    break 
            
            # Store original edges
            for e in bm.edges:
                if e.select:
                    org_sel.append(e)

            # Store visible faces
            bpy.ops.mesh.select_all(action='SELECT')
            for f in bm.faces:
                if f.select:
                    face_sel.append(f)
            
            
            # Store boundry edges
            bpy.ops.mesh.region_to_loop()

            for e in bm.edges:
                if e.select:
                    border_sel.append(e)

            bpy.ops.mesh.select_all(action='DESELECT')
            
            # Select Start and End edges
            for e in start_end:
                e.select = True
            
            # Hide trick
            bpy.ops.mesh.loop_multi_select(ring=True)
            
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')
            bpy.ops.mesh.hide(unselected=True)
            
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            bpy.ops.mesh.select_all(action='DESELECT')
            for e in start_end:
                e.select = True
            bpy.ops.mesh.shortest_path_select()
            bpy.ops.mesh.select_more()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.reveal()
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='EDGE')

            # Deselect border edges
            for e in border_sel:
                e.select = False
            
            # Add to original selection
            for e in bm.edges:
                if e.select:
                    org_sel.append(e)
            
            # Restore hidden polygons
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            for f in face_sel:
                f.select = True
            bpy.ops.mesh.hide(unselected=True)
            
            
            # Reselect original selection
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            bpy.ops.mesh.select_all(action='DESELECT')
            for e in org_sel:
                e.select = True
            
            # Set active edge
            bm.select_history.add(bm.edges[active_edge])
            
            
            if self.collapse:
                bpy.ops.mesh.merge(type='COLLAPSE', uvs=True)
            
            bmesh.update_edit_mesh(me, True, False)
            
            return {'FINISHED'}
        
        else:
            self.report({'WARNING'}, "This tool only workins in edge mode.")
            return {'CANCELLED'}



def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()



