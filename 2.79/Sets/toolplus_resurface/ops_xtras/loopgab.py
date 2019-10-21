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




bl_info = {
    "name": "T+ EdgeGap",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] > Xtras Panel",
    "description": "create a hole or a tube to selectd face or vertex",
    "warning": "to fix uneven hole or tube > use inset or cut a square into an ngon",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}
    
    
    
# LOAD MODULE #
import bpy
import bmesh, os, random
import mathutils
from bpy import*
from bpy.props import *
from bpy.types import WindowManager


# VertexGroup # 
def create_vertex_groups_edges(self, context):
     
    groupName = 'EdgeBorder'
     
    ob = bpy.context.active_object
    me = ob.data
     
    # Try to retrieve the vertex group, and make a new one
    try:
            group_index = ob.vertex_groups[groupName].index
    except:
            group = ob.vertex_groups.new(groupName)
            group_index = group.index
     
    sel = bpy.context.object.vertex_groups.active.name
    sel_id = bpy.context.object.vertex_groups.active_index  

    # get the bmesh data
    bm = bmesh.new()
    bm.from_mesh(me)
     
    # get the custom data layer
    deform_layer = bm.verts.layers.deform.active
    if deform_layer is None: deform_layer = bm.verts.layers.deform.new()
     
    # loop through all selected faces
    for f in bm.faces:
        if f.select:
          
            # add the verts to group
            for v in f.verts:
                v[deform_layer][group_index] = 1


    # bmesh back in the object
    bm.to_mesh(me)
    bm.free()
    

def update_gp_bvl(self, context):
    print("OFFSET: ", VIEW3D_TP_LoopGap.gp_bvl2_offset[1]['max'])
    offset = self.gp_bvl_offset
    if offset > 0.5:
        VIEW3D_TP_LoopGap.gp_bvl2_offset[1]['max'] = offset
        self.gp_bvl2_offset = offset
    else:
        VIEW3D_TP_LoopGap.gp_bvl2_offset[1]['max'] = 100
        
        
        
class VIEW3D_TP_LoopGap(bpy.types.Operator):
    """bevel to selected edge loop"""
    bl_idname = "tp_ops.loopgap"
    bl_label = "LoopGap"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}


    # GAP #
    gp_bvl_offset = bpy.props.FloatProperty(name="Offset",  description="value", default=0.5, min=0.01, max=100)                          
    gp_shrink_fatten = bpy.props.FloatProperty(name="Depth",  description="value", default=2, min=0.01, max=100)   
    gp_shrink_even = bpy.props.BoolProperty(name="Even",  description="even shrink and flatten", default=True)   
    gp_coplanar = bpy.props.BoolProperty(name="Coplanar",  description="coplaner shrink and flatten", default=False)   
                        
    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # TWO #
    gp_two = bpy.props.BoolProperty(name="Create 2",  description="create two gaps", default=False)   

    gp_two_offset = bpy.props.FloatProperty(name="Offset",  description="value", default=0.1, min=0, max=100)                          
    gp_two_segments = bpy.props.IntProperty(name="Segments",  description="value", default=3, min=0, max=10, step=1)                          
    gp_two_profile = bpy.props.FloatProperty(name="Profil",  description="value", default=1, min=0.01, max=1.00)                           
    gp_two_inset = bpy.props.FloatProperty(name="Border",  description="set offset", default=0.2, min=0.01, max=100)

    gp_bvl2_offset = bpy.props.FloatProperty(name="Shift",  description="value", default=0.25, min=0.02, max = 100)#, update=update_gp_bvl)                      
    gp_bvl2_segments = bpy.props.IntProperty(name="Loops",  description="value", default=1, min=0, max=10, step=1)                          


    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # ROUND #
    gp_round = bpy.props.BoolProperty(name="Round",  description="round inner gap", default=False)                          

    gp_rd_offset = bpy.props.FloatProperty(name="Offset",  description="value", default=0.05, min=0.01, max=100)                          
    gp_rd_segments = bpy.props.IntProperty(name="Segments",  description="value", default=2, min=1, max=10, step=1)                          
    gp_rd_profile = bpy.props.FloatProperty(name="Profil",  description="value", default=0.5, min=0.01, max=1.00)                           
    gp_rd_inset = bpy.props.FloatProperty(name="Border",  description="set offset", default=0.2, min=0.01, max=100)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#
    
    # BORDER #
    gp_border_bevel = bpy.props.BoolProperty(name="Bevel",  description="border bevel", default=False)   
    gp_loop_slide = bpy.props.BoolProperty(name="Even",  description="loop slide for bevel", default=False)   

    gp_border_offset = bpy.props.FloatProperty(name="Offset",  description="value", default=0.05, min=0.01, max=100)                          
    gp_border_segments = bpy.props.IntProperty(name="Segments",  description="value", default=2, min=1, max=10, step=1)                          
    gp_border_profile = bpy.props.FloatProperty(name="Profil",  description="value", default=0.5, min=0.00, max=1.00)  
    gp_border_inset = bpy.props.FloatProperty(name="Border",  description="set offset", default=0.2, min=0.01, max=100)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # SELECTION #
    gp_smooth = bpy.props.BoolProperty(name="Smooth Gap",  description="smooth gap", default=False) 

    # SPLIT #
    gp_split = bpy.props.BoolProperty(name="Split Gap",  description="split gap", default=False)       

    gp_meshcheck = bpy.props.BoolProperty(name="MeshCheck",  description="enable mesh analyse: intersect", default=False)       
    

    @classmethod
    def poll(self, context):
        return context.mode == 'EDIT_MESH'

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align = True)

        box = col.box().column(1)             

        row = box.row(1)  
        row.prop(self, 'gp_coplanar')
        row.prop(self, 'gp_shrink_even')          
     
        box.separator()

        row = box.row(1)  
        row.prop(self, 'gp_shrink_fatten')  
        row.prop(self, 'gp_bvl_offset')

        box.separator()
 
        box = col.box().column(1) 
      
        row = box.row(1)  
        row.prop(self, 'gp_two')  

        if self.gp_two == True: 

            box.separator()
            
            row = box.row(1)           
            row.prop(self, 'gp_bvl2_segments')
            row.prop(self, 'gp_bvl2_offset') 

            box.separator()

            row = box.row(1)   
            row.prop(self, 'gp_two_segments')
            row.prop(self, 'gp_two_offset')
         
            row = box.row(1)  
            row.prop(self, 'gp_two_profile')           
            #if self.gp_rd_profile < 1.00:
            row.prop(self, 'gp_two_inset') 
       
        box.separator() 


        box = col.box().column(1)             

        row = box.row(1)  
        row.prop(self, 'gp_round')  
   
        if self.gp_round == True:

            box.separator()  
                        
            row = box.row(1)  
            row.prop(self, 'gp_rd_segments')
            row.prop(self, 'gp_rd_offset')

            row = box.row(1)  
            row.prop(self, 'gp_rd_profile')
            #if self.gp_rd_profile < 1.00:
            row.prop(self, 'gp_rd_inset')

        box.separator()


        box = col.box().column(1)             

        row = box.row(1)  
        row.prop(self, 'gp_border_bevel')  
        
        if self.gp_border_bevel == True:
            row.prop(self, 'gp_loop_slide')
            
            box.separator()

            row = box.row(1)           
            row.prop(self, 'gp_border_segments')
            row.prop(self, 'gp_border_offset')                        
           
            row = box.row(1)  
            row.prop(self, 'gp_border_profile')
            #if self.gp_border_profile < 1.00:
            row.prop(self, 'gp_border_inset')
       
        box.separator()
       
        box = col.box().column(1)             

        row = box.row(1)   
        row.prop(self, 'gp_smooth', text="Smooth")
        row.prop(self, 'gp_split', text="Split")


        box.separator()

     
        box = col.box().column(1)   

        row = box.row()
        row.prop(self, 'gp_meshcheck', icon ="ORTHO")
        row.operator("wm.operator_defaults", text="Reset", icon ="RECOVER_AUTO")  

        box.separator()






    # EXECUTE MAIN OPERATOR #       
    def execute(self, context):                     
    
        #check for mesh selections
        object = context.object
        object.update_from_editmode()

        mesh_bm = bmesh.from_edit_mesh(object.data)

        selected_faces = [f for f in mesh_bm.faces if f.select]
        selected_edges = [e for e in mesh_bm.edges if e.select]
        selected_verts = [v for v in mesh_bm.verts if v.select]

        # check wich select mode is active        
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False): 
            # check verts selection value  
            if len(selected_verts) == 0:
                self.report({'WARNING'}, "Nothing Selected!")
                return {'CANCELLED'}
            else:
                bpy.ops.mesh.region_to_loop()                                     

        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True): 
            # check verts selection value  
            if len(selected_faces) == 0:
                self.report({'WARNING'}, "Nothing Selected!")
                return {'CANCELLED'}
            else:
                bpy.ops.mesh.region_to_loop()   

        # check wich select mode is active        
        if not tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False): 
            print(self)
            self.report({'INFO'}, "EdgeMode") 
        else:                
            # to be sure that only edge are selectable
            bpy.ops.mesh.select_mode(type="EDGE") 
       
        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'


        # enable mesh analyse
        if self.gp_meshcheck == True: 
            bpy.context.object.data.show_statvis = True
            bpy.context.scene.tool_settings.statvis.type = 'INTERSECT'   
        else:
            bpy.context.object.data.show_statvis = False
                        

        # coplanar on
        if self.gp_coplanar == True: 

            bpy.ops.mesh.bevel(offset=self.gp_bvl_offset, segments=1, profile=1, vertex_only=False)  

            bpy.ops.object.editmode_toggle()
            create_vertex_groups_edges(self, context)
            bpy.ops.object.editmode_toggle()

            # create 2 on
            if self.gp_two == True:                 
                bpy.ops.mesh.region_to_loop() 
  
                if self.gp_bvl2_offset >= self.gp_bvl_offset:
                    print(self)
                    self.report({'INFO'}, "!!! Mesh Overlaps !!!")
                    
                    if self.gp_meshcheck == True: 
                        bpy.ops.mesh.bevel(offset=self.gp_bvl2_offset, segments=self.gp_bvl2_segments, profile=1, vertex_only=False) 
                    else:
                        pass
                else:
                    bpy.ops.mesh.bevel(offset=self.gp_bvl2_offset, segments=self.gp_bvl2_segments, profile=1, vertex_only=False) 

                bpy.ops.mesh.inset(use_even_offset=self.gp_shrink_even, thickness=0, depth=self.gp_shrink_fatten*-1)


            # create 2 off          
            else:          
                bpy.ops.mesh.inset(use_even_offset=self.gp_shrink_even, thickness=0, depth=self.gp_shrink_fatten*-1)
     
 
            # add round 
            if self.gp_round == True:
                if self.gp_coplanar == True: 
                    bpy.ops.mesh.region_to_loop()             
 
                bpy.ops.mesh.bevel(offset=self.gp_rd_offset, segments=self.gp_rd_segments, profile=self.gp_rd_profile, vertex_only=False)

                if self.gp_rd_profile < 1.00:                                                       
                    bpy.ops.mesh.inset(thickness=self.gp_rd_inset, use_outset=True, use_edge_rail=True)   


            if self.gp_border_bevel == True:                  
                if self.gp_round == True:                                
                    if self.gp_rd_profile < 1.00:
                        bpy.ops.mesh.select_more()

                bpy.ops.mesh.select_more()               
                bpy.ops.mesh.region_to_loop()   

        # coplanar off
        else:
            
            bpy.ops.mesh.bevel(offset=self.gp_bvl_offset, segments=2, profile=1, vertex_only=False)

            bpy.ops.object.editmode_toggle()
            create_vertex_groups_edges(self, context)
            bpy.ops.object.editmode_toggle()            

            bpy.ops.mesh.select_less() 
 
            # create 2 on
            if self.gp_two == True:   
               
                if self.gp_bvl2_offset >= self.gp_bvl_offset:
                    print(self)
                    self.report({'INFO'}, "!!! Mesh Overlaps !!!")
                   
                    if self.gp_meshcheck == True:                              
                        bpy.ops.mesh.bevel(offset=self.gp_bvl2_offset, segments=self.gp_bvl2_segments, profile=1, vertex_only=False)                     
                    else:
                        pass                    
                else:
                    
                    bpy.ops.mesh.bevel(offset=self.gp_bvl2_offset, segments=self.gp_bvl2_segments, profile=1, vertex_only=False) 
                
                    bpy.ops.mesh.region_to_loop()
                    
                    bpy.ops.transform.shrink_fatten(value=self.gp_shrink_fatten, use_even_offset=self.gp_shrink_even)

                    bpy.ops.mesh.bevel(offset=self.gp_two_offset, segments=self.gp_two_segments, profile=self.gp_two_profile, vertex_only=False)  

                    if self.gp_two_profile < 1.00:
                        bpy.ops.mesh.inset(thickness=self.gp_two_inset, use_outset=True, use_edge_rail=True)   

                    if self.gp_border_bevel == True:  
                        if self.gp_two_profile < 1.00:
                            bpy.ops.mesh.select_more()
                        bpy.ops.mesh.select_more()
                        bpy.ops.mesh.region_to_loop()                  

 
            # create 2 off
            else:
      
                bpy.ops.transform.shrink_fatten(value=self.gp_shrink_fatten, use_even_offset=self.gp_shrink_even)                    

                if self.gp_round == True:
                    if self.gp_coplanar == True: 
                        bpy.ops.mesh.region_to_loop()             
                     
                    bpy.ops.mesh.bevel(offset=self.gp_rd_offset, segments=self.gp_rd_segments, profile=self.gp_rd_profile, vertex_only=False)

                    if self.gp_rd_profile < 1.00:
                        bpy.ops.mesh.inset(thickness=self.gp_rd_inset, use_outset=True, use_edge_rail=True)   

                if self.gp_border_bevel == True:  
                    if self.gp_round == True: 
                        if self.gp_rd_profile < 1.00:
                            bpy.ops.mesh.select_more()
                   
                    bpy.ops.mesh.select_more()
                    bpy.ops.mesh.region_to_loop()   



        # bevel
        if self.gp_border_bevel == True:             
            bpy.ops.mesh.bevel(offset=self.gp_border_offset, segments=self.gp_border_segments, profile=self.gp_border_profile, vertex_only=False, loop_slide=self.gp_loop_slide)   

            if self.gp_border_profile < 1.00:
                bpy.ops.mesh.inset(thickness=self.gp_border_inset, use_outset=True, use_edge_rail=True)   



        # smooth
        if self.gp_smooth == True: 
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  
            bpy.ops.mesh.faces_shade_smooth()


        # split
        if self.gp_split == True: 
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            bpy.ops.mesh.split()


        # delete custom vertex group
        ob = bpy.context.object
        for vgroup in ob.vertex_groups:
            if vgroup.name.startswith("EdgeBorder"):
                ob.vertex_groups.remove(vgroup)


        #print(self)
        #self.report({'INFO'}, "EdgeGap")  
        return {'FINISHED'}



# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 