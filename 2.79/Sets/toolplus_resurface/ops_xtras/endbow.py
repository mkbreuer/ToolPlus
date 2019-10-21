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
    "name": "T+ EndBow",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] > Xtras Panel",
    "description": "create grid with a bow on a hole or a bow with selected mesh",
    "warning": "grid fill works best with a regular count of vertices",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD MODULE #
import bpy
import bmesh
from bpy import*
from bpy.props import *


# VERTEX GROUP #
def create_vertex_groups_endbow(self, context):
     
    groupName = 'EndBow'
     
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
    


# MAIN OPERATOR #
class VIEW3D_TP_EndBow(bpy.types.Operator):
    """create grid with a bow on a hole or a bow with selected mesh"""
    bl_idname = "tp_ops.endbow"
    bl_label = "EndBow"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

                       
    # GRID FILL #
    fill_grid_use = bpy.props.BoolProperty(name="Grid Fill", description="enabel bevel inset", default=False, options={'SKIP_SAVE'})
    grid_simple = bpy.props.BoolProperty(name="Smooth", description="simple blending", default=False)
    grid_span = bpy.props.IntProperty(name="Span",  description="number of loops", default=2, min=0, max=20, step=1) 
    grid_offset = bpy.props.IntProperty(name="Offset",  description="rotation of loops", default=0, min=0, max=20, step=1) 

    # SUBDIV # 
    ebb_subdiv_use = bpy.props.BoolProperty(name="SubDiv", description="enabel subdivide", default=False)
    subdiv_cuts = bpy.props.IntProperty(name="Cuts",  description="change subdivide cuts", default=1, min=0, max=20, step=1) 
    subdiv_quadtri = bpy.props.BoolProperty(name="QuadTri", description="change subdivide connection", default=False)    
    subdiv_quadcorner = bpy.props.EnumProperty(
                          items = [("FAN",          "Fan",          "", 1),
                                   ("PATH",         "Path",         "", 2),
                                   ("STRAIGHT_CUT", "Straight Cut", "", 3), 
                                   ("INNERVERT",    "Inner Vert",   "", 4)], 
                                   description="Quad Cornaer Type")


    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # GRID #
    ebb_fix_use = bpy.props.BoolProperty(name="Grid Fix",  description="enable grid at tube end", default=False) 
    ebb_fix = bpy.props.FloatProperty(name="Scale", description="fix grid when subdiv more then 5", default=1.00, min=0.01, max=10.00)

    # BOW #
    ebb_bow_use = bpy.props.BoolProperty(name="Bow", description="enabel bow bevel inset", default=False)
    ebb_bow_height = bpy.props.FloatProperty(name="Height", description="set lenght value", default=0.3, min=-100, max=100)
    ebb_bow_factor = bpy.props.FloatProperty(name="Factor", description="set lenght value", default=1, min=0, max=1)
    ebb_bow_repeat = bpy.props.IntProperty(name="Repeat", description="set lenght value", default=1, min=0, max=10)
    ebb_bow_inset = bpy.props.FloatProperty(name="Width", description="set scale value", default=0.02, min=0.00, max=1.00)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # TRANSFORM #
    ebb_scale = bpy.props.FloatProperty(name="Scale", description="set x rotation value", default=0.50, min=-100, max=100)
    ebb_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  
    ebb_link_use = bpy.props.BoolProperty(name="Link",  description="enable select link ", default=False)  

    # TRANSFORM LOCATION #
    ebb_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100)
    ebb_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100)
    ebb_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100)

    # TRANSFORM ROTATE #
    ebb_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    ebb_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    ebb_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60)

    # TRANSFORM SCALE #
    ebb_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100)
    ebb_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100)
    ebb_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # BEVEL TOP #
    ebb_bvl_use = bpy.props.BoolProperty(name="Bevel",  description="activate bevel", default=False) 
    ebb_bvl_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    ebb_bvl_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1.00, min=0.00, max=1.00)
    ebb_bvl_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0.01, max=100)
    ebb_bvl_loopslide_use = bpy.props.BoolProperty(name="Even",  description="enable loopslide", default=True) 

    # BEVEL INSET #
    ebb_bvl_inset_use = bpy.props.BoolProperty(name="Inset", description="enabel bevel inset", default=False)
    ebb_bvl_inset_switch = bpy.props.BoolProperty(name="in/out", description="set in or out value", default=False)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # SMOOTH #
    ebb_smooth = bpy.props.BoolProperty(name="M-Smooth",  description="smooth mesh", default=False)    

    # SPLIT #
    ebb_split = bpy.props.BoolProperty(name="M-Split",  description="split mesh", default=False)    



    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        col = layout.column(align = True)

        box = col.box().column(1)  

        row = box.row(1)
        row.prop(self, "fill_grid_use") 

        if self.fill_grid_use == True:   

            row.prop(self, "grid_span") 

            row = box.row(1)
            row.prop(self, "grid_simple") 
            row.prop(self, "grid_offset") 
       
            box.separator()
            
        box.separator()

        row = box.row(1)
        row.prop(self, "ebb_subdiv_use") 

        if self.ebb_subdiv_use == True:   

            row.prop(self, "subdiv_cuts") 

            row = box.row(1)
            row.prop(self, "subdiv_quadtri") 
            row.prop(self, "subdiv_quadcorner", text="") 

        box.separator()
       
        box = col.box().column(1) 

        row = box.row(1)
        row.prop(self, "ebb_bow_use") 
        row.prop(self, "ebb_bow_height") 

        row = box.row(1)
        row.label("") 
        row.prop(self, "ebb_bow_repeat") 

        row = box.row(1)
        row.label("") 
        row.prop(self, "ebb_bow_factor") 

        box.separator()

        row = box.row(1) 
        row.prop(self, "ebb_fix_use") 
        row.prop(self, "ebb_fix") 
 
        box.separator()



        box = col.box().column(1)   

        row = box.row(1)
        row.prop(self, "ebb_transform_use")         
       
        
        if self.ebb_transform_use == True:

            row.prop(self, "ebb_link_use")  

            row = box.row(1)
            row.label("Location") 
            
            row = box.row(1)        
            row.prop(self, "ebb_location_x") 
            row.prop(self, "ebb_location_y")               
            row.prop(self, "ebb_location_z") 
     
            box.separator()

            row = box.row(1)
            row.label("Rotation") 
            
            row = box.row(1)
            row.prop(self, "ebb_rotate_x") 
            row.prop(self, "ebb_rotate_y")               
            row.prop(self, "ebb_rotate_z") 
     
            box.separator()

            row = box.row(1)
            row.label("Scale") 
            
            row = box.row(1)
            row.prop(self, "ebb_scale_x") 
            row.prop(self, "ebb_scale_y")               
            row.prop(self, "ebb_scale_z") 

            box.separator()
            
        box = col.box().column(1)  
            
        row = box.row(1) 
        row.prop(self, "ebb_bvl_use")


        if self.ebb_bvl_use == True:

            row.prop(self, "ebb_bvl_loopslide_use", text="Even")
            
            row = box.row(1) 
            row.prop(self, "ebb_bow_inset") 
            row.prop(self, "ebb_bvl_offset") 

            row = box.row(1)
            row.prop(self, "ebb_bvl_profile")
            row.prop(self, "ebb_bvl_segment")                     

        box.separator()


        box = col.box().column(1)             

        row = box.row(1)         
        row.prop(self, "ebb_smooth")        
        row.prop(self, "ebb_split")  


        box = col.box().column(1)   

        row = box.row(1)
        row.operator("wm.operator_defaults", text="Reset")  

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


        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'


            
        # check wich select mode is active        
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True): 
            pass
        else:

            verts_len = len(selected_verts)
            if (verts_len%2) > 0:              
                print(self)
                self.report({'INFO'}, 'Need even number of vertices')  
            else:            
                if self.fill_grid_use == True:
                    bpy.ops.mesh.fill_grid(span=self.grid_span, offset=self.grid_offset, use_interp_simple=self.grid_simple)


        if self.ebb_subdiv_use == True:
            bpy.ops.mesh.subdivide(number_cuts=self.subdiv_cuts, smoothness=0, quadtri=self.subdiv_quadtri, quadcorner=self.subdiv_quadcorner)


        # create bow              
        if self.ebb_bow_use == True:                       
            bpy.ops.mesh.select_less()
            bpy.ops.transform.translate(value=(0, 0, self.ebb_bow_height), constraint_axis=(False, False, True), constraint_orientation='NORMAL')
            bpy.ops.mesh.vertices_smooth(factor=self.ebb_bow_factor, repeat=self.ebb_bow_repeat)
            bpy.ops.mesh.select_more()


        bpy.ops.object.editmode_toggle()
        create_vertex_groups_endbow(self, context)
        bpy.ops.object.editmode_toggle()


        # custom transform        
        if self.ebb_transform_use == True:

            if self.ebb_link_use == True:
                bpy.ops.mesh.select_linked(delimit={'SEAM'})

            # location 
            bpy.ops.transform.translate(value=(self.ebb_location_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
            bpy.ops.transform.translate(value=(0, self.ebb_location_y, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
            bpy.ops.transform.translate(value=(0, 0, self.ebb_location_z), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

            # rotate 
            bpy.ops.transform.rotate(value=self.ebb_rotate_x, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
            bpy.ops.transform.rotate(value=self.ebb_rotate_y, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
            bpy.ops.transform.rotate(value=self.ebb_rotate_z, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

            # scale 
            bpy.ops.transform.resize(value=(self.ebb_scale_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
            bpy.ops.transform.resize(value=(0, self.ebb_scale_y, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
            bpy.ops.transform.resize(value=(0, 0, self.ebb_scale_z), constraint_axis=(False, False, True), constraint_orientation='NORMAL')



        # add bevel to the border
        if self.ebb_bvl_use == True:                                 
           
            # apply scale in objectmode
            bpy.ops.object.editmode_toggle()           
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            bpy.ops.object.editmode_toggle()                  
            
            
            #if self.ebb_bvl_profile < 1.00:
            bpy.ops.mesh.inset(use_edge_rail=True, thickness=self.ebb_bow_inset+self.ebb_bvl_offset+0.02, use_outset=True)
            bpy.ops.mesh.inset(use_edge_rail=True, thickness=self.ebb_bow_inset+self.ebb_bvl_offset+0.02, use_outset=False)

            bpy.ops.mesh.select_more()

            # select edgeborder
            bpy.ops.mesh.region_to_loop()   
                        
            # bevel top
            bpy.ops.mesh.bevel(offset=self.ebb_bvl_offset, segments=self.ebb_bvl_segment, profile=self.ebb_bvl_profile, loop_slide=self.ebb_bvl_loopslide_use)                      

            bpy.ops.mesh.select_mode(type="FACE")   


        if self.ebb_fix_use == True:
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            if self.ebb_bvl_use == True:    

                n = self.ebb_bvl_segment+1                      
                for i in range(n):
                    bpy.ops.mesh.select_less()                             

                if self.ebb_bvl_profile < 1.00:
                    bpy.ops.mesh.select_less()   
                    bpy.ops.mesh.select_less()   
 
            else:  
                bpy.ops.mesh.select_less()

            bpy.ops.mesh.vertices_smooth(factor=self.ebb_fix, repeat=1) 
            bpy.ops.transform.resize(value=(self.ebb_fix, self.ebb_fix, self.ebb_fix), constraint_axis=(True, True, True), constraint_orientation='NORMAL')

            bpy.ops.mesh.select_more()


        if self.ebb_smooth == True: 
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            bpy.ops.mesh.faces_shade_smooth()

        if self.ebb_split == True: 
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            bpy.ops.mesh.split()

        # delete custom vertex group
        ob = bpy.context.object
        for vgroup in ob.vertex_groups:
            if vgroup.name.startswith("EndBow"):
                ob.vertex_groups.remove(vgroup)


        #print(self)
        #self.report({'INFO'}, "EndBow")  
        return {'FINISHED'}


# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():  
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 
