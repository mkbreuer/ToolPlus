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
#


bl_info = {
        'name': "EdgeRing Dissolve",
        'author': "Kjartan Tysdal (ktools), Marvin K. Breuer (MKB)",
        'location': "EditMode > Delete Menu",
        'description': "dissolve of edge ring loops",
        'category': "Mesh",
        'blender': (2, 7, 9),
        'version': (0, 1, 0),
        'wiki_url': 'http://www.kjartantysdal.com/scripts',
        'wiki_url': 'https://github.com/mkbreuer/ToolPlus',
}



# LOAD MODUL #    
import bpy, bmesh 
from bpy import *
from bpy.props import *



class VIEW3D_TP_EdgeRing_Dissolve(bpy.types.Operator):
    """select 1 or 2 edges [ it > select edge rings > deselect nth > select loops > dissolve edges ]"""
    bl_idname = "tp_ops.dissolve_edge_loops"
    bl_label = "EdgeRing Dissolve"
    bl_options = {'REGISTER', 'UNDO'}

    loop = bpy.props.BoolProperty(name="Ring or Loop",  description="select ring or edge loop", default=True, options={'SKIP_SAVE'})    
    checker = bpy.props.IntProperty(name="Nth Checker",  description="deselect every nth selected", min=1, max=50, default=1) 
    offset = bpy.props.IntProperty(name="Offset Nth",  description="offset nth", min=0, max=50, default=0) 
    grow = bpy.props.IntProperty(name="Grow Loop", description="How much to grow selection", default= 0, min=0, soft_max=50)   

    def draw(self, context):
        layout = self.layout   
        
        col = layout.column(1)   
        box = col.box().column(1)   

        row = box.column(1)                
        row.prop(self,'loop', text="Ring or Loop")     
        row.prop(self,'checker', text="Nth Checker")     
        row.prop(self,'offset', text="Offset Nth")     
        row.prop(self,'grow', text="Grow Loop")     

        box.separator() 


    def execute(self, context):

        #check for mesh selections
        object = context.object
        object.update_from_editmode()

        mesh_bm = bmesh.from_edit_mesh(object.data)

        selected_faces = [f for f in mesh_bm.faces if f.select]
        selected_edges = [e for e in mesh_bm.edges if e.select]
        selected_verts = [v for v in mesh_bm.verts if v.select]

        # check wich select mode is active  
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True): 
            # check verts selection value  
            self.report({'WARNING'}, "Only EdgeMode!")
            return {'CANCELLED'}
              
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False): 
            self.report({'WARNING'}, "Only EdgeMode!")
            return {'CANCELLED'}

      
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):   
            # to be sure that only edge are selectable
            #bpy.ops.mesh.select_mode(type="EDGE") 
            
            if len(selected_edges) == 1:                  
                bpy.ops.mesh.loop_multi_select(ring=self.loop)  


            if len(selected_edges) == 2:  
                # used ktools path ring
                bpy.ops.tp_ops.path_select_ring_for_dissolve()                 
            
                       
            if len(selected_edges) > 2:                
                self.report({'WARNING'}, "Select only 1-2 Edges!")
                return {'CANCELLED'}


            bpy.ops.mesh.select_nth(nth=self.checker, skip=1, offset=self.offset)
            
            # used ktools loop grow
            bpy.ops.tp_ops.grow_loop_for_dissolve(grow=self.grow)

            #bpy.ops.mesh.loop_multi_select(ring=False)                
            bpy.ops.mesh.delete_edgeloop()


        return {'FINISHED'}




class VIEW3D_TP_Grow_Loop_for_dissolve(bpy.types.Operator):
        #'author': "Kjartan Tysdal (ktools)"
        #'wiki_url': 'http://www.kjartantysdal.com/scripts'
        """Grows the selected edges in both directions """          
        bl_idname = "tp_ops.grow_loop_for_dissolve"                
        bl_label = "Grow Loop"               
        bl_options = {'REGISTER', 'UNDO'} 

        grow = IntProperty(name="Grow Selection", description="How much to grow selection", default= 1, min=1, soft_max=10)
        
        def execute(self, context):
                
            grow = self.grow
            sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
            
            for x in range(grow):

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




class VIEW3D_TP_Path_Select_Ring_for_dissolve(bpy.types.Operator):
    #'author': "Kjartan Tysdal (ktools)"
    #'wiki_url': 'http://www.kjartantysdal.com/scripts'
    """Selects the shortest edge ring path / only edge mode"""
    bl_idname = "tp_ops.path_select_ring_for_dissolve"
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
            bm.edges.ensure_lookup_table()# added
            bm.select_history.add(bm.edges[active_edge])
            
            
            if self.collapse:
                bpy.ops.mesh.merge(type='COLLAPSE', uvs=True)
            
            bmesh.update_edit_mesh(me, True, False)
            
            return {'FINISHED'}
        
        else:
            self.report({'WARNING'}, "This tool only workins in edge mode.")
            return {'CANCELLED'}






# TO MENU #
def draw_menu_func(self, context):

    #self.layout.separator()
    self.layout.operator("tp_ops.dissolve_edge_loops")



# REGISTRY #        
def register():    
    bpy.utils.register_class(VIEW3D_TP_EdgeRing_Dissolve)
    bpy.utils.register_class(VIEW3D_TP_Grow_Loop_for_dissolve)
    bpy.utils.register_class(VIEW3D_TP_Path_Select_Ring_for_dissolve)

    bpy.types.VIEW3D_MT_edit_mesh_delete.append(draw_menu_func)


def unregister():   
    bpy.utils.unregister_class(VIEW3D_TP_EdgeRing_Dissolve)
    bpy.utils.unregister_class(VIEW3D_TP_Grow_Loop_for_dissolve)
    bpy.utils.unregister_class(VIEW3D_TP_Path_Select_Ring_for_dissolve)

    bpy.types.VIEW3D_MT_edit_mesh_delete.remove(draw_menu_func)

if __name__ == "__main__":
    register()















