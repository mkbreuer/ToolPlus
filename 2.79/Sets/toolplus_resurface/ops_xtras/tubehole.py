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
    "name": "TubeHole",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] > Xtras Panel",
    "description": "create a hole or a tube to selectd face or vertex",
    "warning": "to fix uneven hole or tube > use inset or cut a square into an ngon",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD MATERIALS # 
from toolplus_rebound.ops_xtras.materials import (remove_material_slots)
from toolplus_rebound.ops_xtras.materials import (tbhl_create_material_0)
from toolplus_rebound.ops_xtras.materials import (tbhl_create_material_1)
from toolplus_rebound.ops_xtras.materials import (tbhl_create_material_2)
from toolplus_rebound.ops_xtras.materials import (tbhl_create_material_3)
from toolplus_rebound.ops_xtras.materials import (tbhl_create_material_4)




# LOAD MODULE #
import bpy
import bmesh, os, random
from bpy import*
from bpy.props import *
from bpy.types import WindowManager


def create_vertex_groups_1(self, context):
     
    groupName = 'RoundBorder'
     
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
    
    

    
class VIEW3D_TP_TubeHole(bpy.types.Operator):                  
    """create a hole or a tube to selectd face or vertex"""                   
    bl_idname = "tp_ops.tubehole"                     
    bl_label = "TubeHole"   
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}     

    @classmethod                                     
    def poll(cls, context):                         
        return context.mode == "EDIT_MESH" and context.object is not None


    # VERT ONLY #
    vthl_vert_div = bpy.props.IntProperty(name="Div",  description="set value", min=0, soft_max=10, default=0)    
    vthl_vert_offset = bpy.props.FloatProperty(name="Scale",  description="set value", default=10, min=0, max=100)    
    vthl_vert_profil = bpy.props.FloatProperty(name="Bow",  description="set value", default=0.00, min=0.01, max=1.00)    

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # IN/OUT SWITCH #
    fchl_cutturn_use = bpy.props.BoolProperty(name="DivType", description="enabel switch cuttype", default=True)
    fchl_inout_use = bpy.props.BoolProperty(name="In / Out", description="enabel switch inside or border face", default=True)

    # SUBDIV #
    fchl_divide = bpy.props.IntProperty(name="Subdiv",  description="set value", min=0, max=10, default=1)    
    fchl_div_quadri = bpy.props.BoolProperty(name="Quad/Tri",  description="switch quad or tri tp prevent ngons", default=False)    
    fchl_div_smooth = bpy.props.FloatProperty(name="Smooth",  description="set value", default=0.00, min=0.01, max=1.00)    

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # TRANSFORM #
    fchl_scale = bpy.props.FloatProperty(name="Scale", description="set x rotation value", default=0.50, min=-100, max=100)
    fchl_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  

    # TRANSFORM LOCATION #
    fchl_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100)
    fchl_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100)
    fchl_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100)

    # TRANSFORM ROTATE #
    fchl_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    fchl_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    fchl_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60)

    # TRANSFORM SCALE #
    fchl_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100)
    fchl_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100)
    fchl_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # GAP # 
    fchl_gap_use = bpy.props.BoolProperty(name="Gap", description="enabel gabp around hole", default=False)
    fchl_gap_inset_height = bpy.props.FloatProperty(name="Bevel 1", description="scale gap size", default=0.2, min=0.05, max=100)
    fchl_gap_inset_out = bpy.props.FloatProperty(name="Bevel 2", description="set bevel size on gap", default=0.2, min=0.00, max=10)
    fchl_gap_depth = bpy.props.FloatProperty(name="Depth", description="set depth size", default=0.5, min=0.00, max=100)
    fchl_gap_scale_in = bpy.props.FloatProperty(name="Scale", description="scale gap size", default=0.2, min=0.05, max=100)
    
    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # CLOSE HOLE #
    fchl_close = bpy.props.BoolProperty(name="Fill Ngon",  description="close or open Hole", default=True)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # TUBE #
    fchl_tube = bpy.props.BoolProperty(name="Tube",  description="enable tube extrusion", default=False)
    fchl_tube_scale = bpy.props.FloatProperty(name="Scale", description="set scale value", default=1.00, min=0.00, max=100)
    fchl_extrude = bpy.props.FloatProperty(name="Height", description="set extrude value", default=3.00, min=-100, max=100)

    # BEVEL 1: BOTTOM #
    fchl_bvl1_use = bpy.props.BoolProperty(name="Bevel 1",  description="activate bevel", default=False) 
    fchl_bvl1_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    fchl_bvl1_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1.00, min=0.00, max=1.00)
    fchl_bvl1_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0.01, max=100)
    fchl_bvl1_loopslide_use = bpy.props.BoolProperty(name="LoopSlide",  description="deactivate loopslide", default=False) 

    # BEVEL 2: TOP #
    fchl_bvl2_use = bpy.props.BoolProperty(name="Bevel 2",  description="activate bevel", default=False) 
    fchl_bvl2_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    fchl_bvl2_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1.00, min=0.00, max=1.00)
    fchl_bvl2_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0.01, max=100)
    fchl_bvl2_loopslide_use = bpy.props.BoolProperty(name="Even",  description="deactivate loopslide", default=False) 

    # BEVEL INSET #
    fchl_bvl_inset_use = bpy.props.BoolProperty(name="Inset", description="enabel bevel inset", default=False)
    fchl_bvl_inset_switch = bpy.props.BoolProperty(name="in/out", description="set in or out value", default=False)

    fchl_bvl_inset_out_thick = bpy.props.FloatProperty(name="Thick", description="set thickness value", default=0.02, min=0.00, max=1.00)
    fchl_bvl_inset_out_depth = bpy.props.FloatProperty(name="Depth", description="set depth value", default=0.02, min=0.00, max=1.00)

    fchl_bvl_inset_in_thick = bpy.props.FloatProperty(name="Thick", description="set thickness value", default=0.02, min=0.00, max=1.00)
    fchl_bvl_inset_in_depth = bpy.props.FloatProperty(name="Depth", description="set depth value", default=-0.02, min=-1.00, max=0.00)

    fchl_bvl_inset_fin_use = bpy.props.BoolProperty(name="BowInset", description="enabel bow bevel inset", default=False)
    fchl_bvl_inset_fin = bpy.props.FloatProperty(name="Inset", description="set scale value", default=0.02, min=0.00, max=1.00)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # PIPE #
    fchl_pipe_use = bpy.props.BoolProperty(name="Pipe", description="enabel pipe inset", default=False)
    fchl_pipe_scale = bpy.props.FloatProperty(name="Scale", description="set scale value", default=0.5, min=0.01, max=100)
    fchl_pipe_depth = bpy.props.FloatProperty(name="Depth", description="set depth value", default=0.3, min=0.01, max=100)

    fchl_bvl_pipe_use = bpy.props.BoolProperty(name="Bevel", description="enabel pipe bevel", default=False)
    fchl_bvl_pipe_loopslide_use = bpy.props.BoolProperty(name="Even",  description="deactivate loopslide", default=False) 
    fchl_pipe_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    fchl_pipe_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1.00, min=0.00, max=1.00)
    fchl_pipe_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0.01, max=10)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # GRID #
    fchl_dissolve = bpy.props.BoolProperty(name="Fill Grid",  description="enable grid at tube end", default=True) 
    fchl_fix_use = bpy.props.BoolProperty(name="FixGrid",  description="enable grid at tube end", default=False) 
    fchl_fix = bpy.props.FloatProperty(name="Scale", description="fix grid when subdiv more then 5", default=1.00, min=0.00, max=1.00)

    # BOW #
    fchl_bow_use = bpy.props.BoolProperty(name="Bow", description="enable bow at tube end", default=False)
    fchl_bow_height = bpy.props.FloatProperty(name="Height", description="set lenght value", default=0.3, min=-100, max=100)

    # BOW BEVEL #
    fchl_bow_inset_use = bpy.props.BoolProperty(name="BowInset", description="enabel bow bevel inset", default=False)
    fchl_bow_inset = bpy.props.FloatProperty(name="Inset", description="set scale value", default=0.15, min=0.05, max=100)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # POKE #
    fchl_poke = bpy.props.BoolProperty(name="Poke",  description="enable poke triangulation", default=False) 
    fchl_poke_offset = bpy.props.FloatProperty(name="Offset", description="move poke triangulation", default=0.00, min=-100, max=100)

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # ROUND #
    fchl_sphere_use = bpy.props.BoolProperty(name="Round",  description="enable round first border egde", default=False) 
    fchl_sphere = bpy.props.FloatProperty(name="R", description="round first border egde", default=1.00, min=0.00, max=1.00)

    # BEVEL: ROUND #
    fchl_bvl4_use = bpy.props.BoolProperty(name="Bevel 4",  description="activate bevel", default=False) 
    fchl_bvl4_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    fchl_bvl4_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1.00, min=0.00, max=1.00)
    fchl_bvl4_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0.01, max=100)
    fchl_bvl4_loopslide_use = bpy.props.BoolProperty(name="Even",  description="deactivate loopslide", default=False) 

    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # SMOOTH #
    fchl_smooth = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    

    # SPLIT #
    fchl_split = bpy.props.BoolProperty(name="Split",  description="split created hole or tube", default=False)    

    tbh_meshcheck = bpy.props.BoolProperty(name="MeshCheck",  description="enable mesh analyse: intersect", default=False)       
    
    #-------------###-------------###-------------###-------------###-------------###-------------###-------------###-------------#

    # MATERIAL #
    fchl_mat = bpy.props.BoolProperty(name="Color Check",  description="add material to the mesh", default=False)    
    my_swatch = FloatVectorProperty(name = "Color", default=[0.0,1.0,1.0], min = 0, max = 1,  subtype='COLOR')
    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0) 

 

    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        col = layout.column(align = True)

        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):
            
            box = col.box().column(1) 
            row = box.row(1)
            row.label("Verts")
            row.prop(self, "vthl_vert_offset")        

            row = box.row(1)
            row.label(" ")    
            row.prop(self, "vthl_vert_div")    
            
            row = box.row(1)
            row.label(" ")  
            row.prop(self, "vthl_vert_profil")    

            box.separator()


        box = col.box().column(1)   

        row = box.row(1)
        row.prop(self, "fchl_inout_use") 

        if self.fchl_inout_use == True:
            row.prop(self, "fchl_cutturn_use")               

        row = box.row(1)
        row.prop(self, "fchl_div_quadri")        
        row.prop(self, "fchl_close")          

        box.separator()

        row = box.row(1)
        row.prop(self, "fchl_scale")   
        row.prop(self, "fchl_divide") 
     
        box.separator()

        box = col.box().column(1)   

        row = box.row(1)
        row.prop(self, "fchl_transform_use")         
        
        if self.fchl_transform_use == True:

            row = box.row(1)
            row.label("Location") 
            
            row = box.row(1)        
            row.prop(self, "fchl_location_x") 
            row.prop(self, "fchl_location_y")               
            row.prop(self, "fchl_location_z") 
     
            box.separator()

            row = box.row(1)
            row.label("Rotation") 
            
            row = box.row(1)
            row.prop(self, "fchl_rotate_x") 
            row.prop(self, "fchl_rotate_y")               
            row.prop(self, "fchl_rotate_z") 
     
            box.separator()

            row = box.row(1)
            row.label("Scale") 
            
            row = box.row(1)
            row.prop(self, "fchl_scale_x") 
            row.prop(self, "fchl_scale_y")               
            row.prop(self, "fchl_scale_z") 


        box.separator()

        
        if self.fchl_close == False:
            
            box = col.box().column(1)  

            row = box.row(1)
            row.prop(self, "fchl_gap_use")
            
            if self.fchl_gap_use == True: 
                                   
                row.prop(self, "fchl_gap_depth")   

                row = box.row(1) 
                row.label("")
                row.prop(self, "fchl_gap_inset_out")   

                row = box.row(1)

                if self.fchl_location_z > -0 and self.fchl_location_z > 0: 
                    row.prop(self, "fchl_gap_inset_height")  
                else:
                    row.label("")
     
                row.prop(self, "fchl_gap_scale_in")   

            box.separator() 


            box = col.box().column(1)  

            row = box.row(1)
            row.prop(self, "fchl_tube")


            if self.fchl_tube == True:


                row.prop(self, "fchl_extrude")   

                row = box.row(1)
                row.label("")
                row.prop(self, "fchl_tube_scale")   

                box.separator() 

                row = box.row(1) 
                row.prop(self, "fchl_bvl1_use")
                row.prop(self, "fchl_bvl1_offset") 
                    
                row = box.row(1) 
                row.prop(self, "fchl_bvl1_loopslide_use")
                row.prop(self, "fchl_bvl1_profile")

                row = box.row(1)
                row.label(" ")    
                row.prop(self, "fchl_bvl1_segment") 

                box.separator() 
                    
                row = box.row(1) 
                row.prop(self, "fchl_bvl2_use")
                row.prop(self, "fchl_bvl2_offset") 
                    
                row = box.row(1) 
                row.prop(self, "fchl_bvl2_loopslide_use")
                row.prop(self, "fchl_bvl2_profile")

                row = box.row(1)
                row.label(" ")    
                row.prop(self, "fchl_bvl2_segment") 
                
                box.separator() 
 
                box = col.box().column(1)  

                if self.fchl_dissolve == True:
                    if self.fchl_bvl2_use == True:

                        box.separator()    
                        
                        row = box.row(1) 
                        row.prop(self, "fchl_pipe_use")
                        row.prop(self, "fchl_pipe_scale")                      
                     
                        row = box.row(1)                           
                        row.label(" ")      
                        row.prop(self, "fchl_pipe_depth")
                                                     
                        box.separator()  
                        
                        row = box.row(1) 
                        row.prop(self, "fchl_bvl_pipe_use")                        
                        row.prop(self, "fchl_pipe_offset") 
                        
                        row = box.row(1)                         
                        row.prop(self, "fchl_bvl_pipe_loopslide_use")
                        row.prop(self, "fchl_pipe_profile")
                        
                        row = box.row(1)                           
                        row.label(" ")                          
                        row.prop(self, "fchl_pipe_segment")            

                        box.separator()
                        

            box = col.box().column(1)  

            row = box.column(1)
            row.prop(self, "fchl_dissolve")        

            box.separator()  
                
            if self.fchl_dissolve == False:
 
                if self.fchl_divide > 1:
                 
                    row = box.row(1)              
                    row.prop(self, "fchl_bow_use")  
                    row.prop(self, "fchl_bow_height")  
                    
                    if self.fchl_bvl2_use == False:   
                       
                        box.separator()

                        row = box.row(1)
                        row.prop(self, "fchl_bow_inset_use") 
                        row.prop(self, "fchl_bow_inset") 

                    box.separator()

                    row = box.row(1) 
                    row.prop(self, "fchl_fix_use") 
                    row.prop(self, "fchl_fix") 

                    box.separator()
                else:
                    pass


        if self.fchl_close == False:


            box = col.box().column(1)  
            
            row = box.row(1) 
            row.prop(self, "fchl_poke")   
            row.prop(self, "fchl_poke_offset")    

            if self.fchl_mat == False: 

                box.separator()

                row = box.row(1)
                row.prop(self, "fchl_sphere_use")   
                row.prop(self, "fchl_sphere")   

            box.separator()

            if self.fchl_location_z > -0 and self.fchl_location_z > 0:

                if self.fchl_sphere_use == True:

                    row = box.row(1) 
                    row.prop(self, "fchl_bvl4_use")
                    row.prop(self, "fchl_bvl4_offset") 
                        
                    row = box.row(1) 
                    row.prop(self, "fchl_bvl4_loopslide_use")
                    row.prop(self, "fchl_bvl4_profile")

                    row = box.row(1)
                    row.label(" ")    
                    row.prop(self, "fchl_bvl4_segment") 

                    box.separator()



            box = col.box().column(1)             
            
            if self.fchl_mat == False: 
                
                row = box.row(1)         
                row.prop(self, "fchl_smooth", text ="Smooth")        
                row.prop(self, "fchl_split", text =" Split")   

                box.separator()  

            row = box.row(1)         
            row.prop(self, "fchl_mat")
            
            if self.fchl_mat == True: 
                row = box.row(1) 
                row.prop(self, "index_count")  
                row.prop(self, "my_swatch", text="")     
                box.separator() 

            if self.fchl_close == False:                            
                row = box.row()
                row.prop(context.space_data, "use_occlude_geometry", text="Occlude", icon='ORTHO') 
                row.prop(self, 'tbh_meshcheck', icon ="ORTHO")            

            box.separator()  


        box = col.box().column(1)   

        row = box.row(1)
        row.operator('tp_ops.tubehole', text='Repeat')
        row.operator("wm.operator_defaults", text="Reset")  

        box.separator()




    # EXECUTE MAIN OPERATOR #       
    def execute(self, context):                     

        #check for mesh selections
        object = context.object
        object.update_from_editmode()

        mesh_bm = bmesh.from_edit_mesh(object.data)

        selected_faces = [f for f in mesh_bm.faces if f.select]
        #selected_edges = [e for e in mesh_bm.edges if e.select]
        selected_verts = [v for v in mesh_bm.verts if v.select]


        # check wich select mode is active        
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False): 
                                    
            # check verts selection value  
            if len(selected_verts) > 1:
                self.report({'WARNING'}, "Select only 1 Vertex")
                return {'CANCELLED'}

            # to be sure that only verts are selectable
            bpy.ops.mesh.select_mode(type="VERT")    
            
            # bevel vertex     
            bpy.ops.mesh.bevel(offset=self.vthl_vert_offset, segments=self.vthl_vert_div, profile=self.vthl_vert_profil, vertex_only=True, loop_slide=True)

            print(self)
            self.report({'INFO'}, "VertTube") 


        else:                

            # check face selection value                 
            if len(selected_faces) > 1:
                bpy.ops.mesh.dissolve_faces()
                
            # need selectable faces 
            bpy.ops.mesh.select_mode(type="FACE") 

        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

        # create vertex group
        bpy.ops.object.editmode_toggle()
        create_vertex_groups_1(self, context)
        bpy.ops.object.editmode_toggle()

        # assign a material
        if self.fchl_mat == True:


            # delete materials
            remove_material_slots()

            obj = bpy.context.object 
            
#            obj.vertex_groups.new('VerGrp_0')
#            bpy.ops.object.vertex_group_assign()
#            bpy.ops.object.vertex_group_set_active(group='VerGrp_0')

            # create material and assign
            bpy.ops.object.material_slot_add()           
            obj.material_slots[obj.material_slots.__len__() - 1].material = tbhl_create_material_0()       

#            bpy.ops.mesh.select_all(action='DESELECT')
#            bpy.ops.object.vertex_group_select()
#            bpy.context.object.active_material_index = 0
#            bpy.ops.object.material_slot_assign()   


        else:
            # delete materials
            remove_material_slots()             




        # enable mesh analyse
        if self.tbh_meshcheck == True: 
            bpy.context.object.data.show_statvis = True
            bpy.context.scene.tool_settings.statvis.type = 'INTERSECT'   
        else:
            bpy.context.object.data.show_statvis = False

        # turn cut            
        if self.fchl_cutturn_use == True: 
        
            if self.fchl_divide == 0:
                pass
            else:
                # subdivie hole
                bpy.ops.mesh.subdivide(number_cuts=self.fchl_divide, smoothness=self.fchl_div_smooth, quadtri = self.fchl_div_quadri)     

            # extrude zero move
            for i in range(self.fchl_inout_use):
                bpy.ops.mesh.inset(thickness=0.001, use_outset =True)


        else:
            for i in range(self.fchl_inout_use):
                bpy.ops.mesh.inset(thickness=0.001)

            if self.fchl_divide == 0:
                pass
            else:
                # subdivie hole
                bpy.ops.mesh.subdivide(number_cuts=self.fchl_divide, smoothness=self.fchl_div_smooth, quadtri = self.fchl_div_quadri)     



        # scale hole
        bpy.ops.transform.resize(value=(self.fchl_scale, self.fchl_scale, self.fchl_scale))

        # make circle with looptools circle
        bpy.ops.tp_mesh.lt_circle()
        
        # alternative: to sphere (used for round border edges)
        #bpy.ops.transform.tosphere(value=1, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

  
        # custom transform        
        if self.fchl_transform_use == True:

            # location 
            bpy.ops.transform.translate(value=(self.fchl_location_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
            bpy.ops.transform.translate(value=(0, self.fchl_location_y, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
            bpy.ops.transform.translate(value=(0, 0, self.fchl_location_z), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

            # rotate 
            bpy.ops.transform.rotate(value=self.fchl_rotate_x, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
            bpy.ops.transform.rotate(value=self.fchl_rotate_y, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
            bpy.ops.transform.rotate(value=self.fchl_rotate_z, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

            # scale 
            bpy.ops.transform.resize(value=(self.fchl_scale_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
            bpy.ops.transform.resize(value=(0, self.fchl_scale_y, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
            bpy.ops.transform.resize(value=(0, 0, self.fchl_scale_z), constraint_axis=(False, False, True), constraint_orientation='NORMAL')


        # delete face for hole
        if self.fchl_close == True:
            bpy.ops.mesh.delete(type='FACE')
       
  
        # go further when face close
        if self.fchl_close == True:
            pass

        else:
            
            # create gap inset 
            for i in range(self.fchl_gap_use):
                
                if self.fchl_location_z > -0 and self.fchl_location_z > 0:  
                    bpy.ops.mesh.inset(use_edge_rail=True, thickness=self.fchl_gap_inset_height, depth=0, use_outset=True)

               
                # assign a material to the last slot
                if self.fchl_mat == True:
                                 
                    obj = bpy.context.object 
                    
                    obj.vertex_groups.new('VerGrp_1')
                    bpy.ops.object.vertex_group_assign()
                    bpy.ops.object.vertex_group_set_active(group='VerGrp_1')
                         
                    # create material and assign
                    bpy.ops.object.material_slot_add()           
                    obj.material_slots[obj.material_slots.__len__() - 1].material = tbhl_create_material_1() 

                    bpy.ops.mesh.select_all(action='DESELECT')
                    bpy.ops.object.vertex_group_select()
                    #bpy.context.object.active_material_index = 1
                    bpy.ops.object.material_slot_assign()          
                    

                # inset out
                bpy.ops.mesh.inset(thickness=self.fchl_gap_inset_out*2, depth=0)
                bpy.ops.mesh.inset(thickness=0, depth=self.fchl_gap_inset_out*-2)

                # depth
                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, self.fchl_gap_depth*-1), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL'})
                
                # inset in
                bpy.ops.mesh.inset(thickness=0, depth=self.fchl_gap_inset_out*-1)
                bpy.ops.mesh.inset(thickness=self.fchl_gap_inset_out, depth=0)
                
                # scale
                bpy.ops.mesh.inset(thickness=self.fchl_gap_scale_in, depth=0)



            # create an ngon
            for i in range(self.fchl_dissolve):                        
                bpy.ops.mesh.dissolve_faces()
                
                
            # bow with grid
            if self.fchl_dissolve == False:
                if self.fchl_divide > 1:                                            
                    for i in range(self.fchl_bow_use):                       
                        bpy.ops.mesh.select_less()
                        bpy.ops.transform.translate(value=(0, 0, self.fchl_bow_height), constraint_axis=(False, False, True), constraint_orientation='NORMAL')
                        bpy.ops.mesh.vertices_smooth(factor=1, repeat=0)
                        bpy.ops.mesh.select_more()
                

            # create triangulated faces
            if self.fchl_bvl2_use == False: 
                for i in range(self.fchl_poke):            
                    bpy.ops.mesh.poke(offset=self.fchl_poke_offset)
              

            # extrude tube 1
            for i in range(self.fchl_tube):
                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, self.fchl_extrude), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL'})
                bpy.ops.transform.resize(value=(self.fchl_tube_scale, self.fchl_tube_scale, 0), constraint_axis=(True, True, False), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

                # add bevel 1 to tube start
                for i in range(self.fchl_bvl1_use):                                 
                  
                    # apply scale in objectmode
                    bpy.ops.object.editmode_toggle()           
                    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
                    bpy.ops.object.editmode_toggle()

                    # select edgeborder
                    bpy.ops.mesh.select_more()                    
                    bpy.ops.mesh.region_to_loop()                        
                                     
                    # bevel bottom                        
                    bpy.ops.mesh.bevel(offset=self.fchl_bvl1_offset, segments=self.fchl_bvl1_segment, profile=self.fchl_bvl1_profile, loop_slide=self.fchl_bvl1_loopslide_use)          

                    # assign a material to pipe
                    if self.fchl_mat == True:
                        
                        obj = bpy.context.object 
                        
                        obj.vertex_groups.new('VerGrp_2')
                        bpy.ops.object.vertex_group_assign()
                        bpy.ops.object.vertex_group_set_active(group='VerGrp_2')
                        
                        # create material and assign
                        bpy.ops.object.material_slot_add()           
                        obj.material_slots[obj.material_slots.__len__() - 1].material = tbhl_create_material_2() 

                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.vertex_group_select()
                        #bpy.context.object.active_material_index = 2
                        bpy.ops.object.material_slot_assign()
                        

                    # border edge               
                    if self.fchl_bvl1_profile < 1.00:
                        bpy.ops.mesh.inset(thickness=self.fchl_bvl1_offset/2, use_outset=True, use_edge_rail=True)   

                    # selection without grid
                    if self.fchl_dissolve == True:  
                    
                        # count and count and ... 
                        bpy.ops.mesh.select_more()

                        if self.fchl_bvl1_profile < 1.00:
                            bpy.ops.mesh.select_more()
                               
                        if self.fchl_bvl1_segment < 3:                                                        
                                    
                            if self.fchl_bvl1_segment < 2:  
                                n = 3                      
                                for i in range(n):
                                    bpy.ops.mesh.select_less()   

                                if self.fchl_bvl1_profile < 1.00: 
                                    bpy.ops.mesh.select_less() 
                                    bpy.ops.mesh.select_less() 

                            else:                            
                                n = 4                      
                                for i in range(n):
                                    bpy.ops.mesh.select_less()                              
                            
                                if self.fchl_bvl1_profile < 1.00: 
                                    
                                    if self.fchl_bvl1_segment == 2:                                                             
                                        n = 2                                            
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()                              
                                   
                                    else:                            
                                        n = 6                                             
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()   

                        else:
    
                            n = self.fchl_bvl1_segment+2                      
                            for i in range(n):
                                bpy.ops.mesh.select_less()                             

                            if self.fchl_bvl1_profile < 1.00:
                                bpy.ops.mesh.select_less()   
                                bpy.ops.mesh.select_less()   
  

                    # selection with grid
                    else:                    
                       
                        # select edgeborder
                        # count and count and ... 
                        bpy.ops.mesh.select_more()                      
                        bpy.ops.mesh.select_more() 

                        if self.fchl_divide > 2:
                            n = +1
                            for i in range(n):
                                bpy.ops.mesh.select_more()  

                            if self.fchl_divide > 4:
                                n = +1
                                for i in range(n):
                                    bpy.ops.mesh.select_more()  

                                if self.fchl_divide > 6:
                                    n = +1
                                    for i in range(n):
                                        bpy.ops.mesh.select_more()  

                                    if self.fchl_divide > 8:
                                        n = +1
                                        for i in range(n):
                                            bpy.ops.mesh.select_more()  


                        if self.fchl_bvl1_profile < 1.00:
                            bpy.ops.mesh.select_more()                    

                        if self.fchl_bvl1_segment < 3:                                                        
                                    
                            if self.fchl_bvl1_segment < 2:  
                                n = 4                      
                                for i in range(n):
                                    bpy.ops.mesh.select_less()   

                                if self.fchl_bvl1_profile < 1.00: 
                                    bpy.ops.mesh.select_less() 
                                    bpy.ops.mesh.select_less() 

                            else:                            
                                n = 5                      
                                for i in range(n):
                                    bpy.ops.mesh.select_less()                              
                            
                                if self.fchl_bvl1_profile < 1.00: 
                                
                                    if self.fchl_bvl1_segment == 2:                            
                                        n = 2                                            
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()                              
                                   
                                    else:                            
                                        n = 6                                             
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()   
                        
                        else:                  
                            n = self.fchl_bvl1_segment+3                      
                            for i in range(n):
                                bpy.ops.mesh.select_less()                             

                            if self.fchl_bvl1_profile < 1.00:
                                bpy.ops.mesh.select_less()   
                                bpy.ops.mesh.select_less()   



                        if self.fchl_divide > 2:
                            n = +1
                            for i in range(n):
                                bpy.ops.mesh.select_less()                             

                            if self.fchl_divide > 4:
                                n = +1
                                for i in range(n):
                                    bpy.ops.mesh.select_less()   

                                if self.fchl_divide > 6:
                                    n = +1
                                    for i in range(n):
                                        bpy.ops.mesh.select_less()   

                                    if self.fchl_divide > 8:
                                        n = +1
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()   


                    bpy.ops.mesh.select_mode(type="FACE")  



            # fix grid when subdiv is to high
            if self.fchl_dissolve == False:  
                if self.fchl_fix_use == True:
                    bpy.ops.mesh.select_less()
                    
                    if self.fchl_bow_use == True:
                        bpy.ops.mesh.vertices_smooth(factor=self.fchl_fix, repeat=10) 
                        bpy.ops.transform.resize(value=(self.fchl_fix, self.fchl_fix, self.fchl_fix), constraint_axis=(True, True, True), constraint_orientation='NORMAL')

                    else:
                        bpy.ops.mesh.vertices_smooth(factor=1, repeat=100) 
                        bpy.ops.transform.resize(value=(self.fchl_fix, self.fchl_fix, self.fchl_fix), constraint_axis=(True, True, True), constraint_orientation='NORMAL')
                    bpy.ops.mesh.select_more()



            # when used bow: add inset as bevel for even tube finish
            if self.fchl_dissolve == False:  
               
                # add bow inset
                if self.fchl_bvl2_use == False:                
                    for i in range(self.fchl_bow_inset_use):                  
                        bpy.ops.mesh.inset(thickness=self.fchl_bow_inset, use_outset=True)
                        bpy.ops.mesh.inset(thickness=self.fchl_bow_inset, use_outset=False)


            # add bevel 2 to tube top
            for i in range(self.fchl_bvl2_use):                                 
               
                # apply scale in objectmode
                bpy.ops.object.editmode_toggle()           
                bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
                bpy.ops.object.editmode_toggle()
                

                # select edgeborder
                bpy.ops.mesh.region_to_loop()                         

                # bevel top
                bpy.ops.mesh.bevel(offset=self.fchl_bvl2_offset, segments=self.fchl_bvl2_segment, profile=self.fchl_bvl2_profile, loop_slide=self.fchl_bvl2_loopslide_use)          
             
                # border edge
                if self.fchl_bvl2_profile < 1.00:
                  bpy.ops.mesh.inset(thickness=self.fchl_bvl2_offset/2, use_outset=True, use_edge_rail=True)

                bpy.ops.mesh.select_mode(type="FACE")   

                         
                # create pipe
                if self.fchl_bvl2_use == True: 

                   # assign a material to pipe
                    if self.fchl_mat == True:
                        
                        obj = bpy.context.object 
                        
                        obj.vertex_groups.new('VerGrp_3')
                        bpy.ops.object.vertex_group_assign()
                        bpy.ops.object.vertex_group_set_active(group='VerGrp_3')
                        
                        # create material and assign
                        bpy.ops.object.material_slot_add()           
                        obj.material_slots[obj.material_slots.__len__() - 1].material = tbhl_create_material_3()                                                               
                                                           
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.vertex_group_select()                        
                        bpy.ops.object.material_slot_assign()


                   
                    # count and count and ... 
                    if self.fchl_pipe_use == True or self.fchl_poke == True:  

                        bpy.ops.mesh.select_more()

                        if self.fchl_bvl2_profile < 1.00:
                            bpy.ops.mesh.select_more()
   
                        if self.fchl_bvl2_segment < 3:                                                                                                                         
                            
                            if self.fchl_bvl2_segment < 2:  
                                n = 2                     
                                for i in range(n):
                                    bpy.ops.mesh.select_less()   

                                if self.fchl_bvl2_profile < 1.00: 
                                    bpy.ops.mesh.select_less() 
                                    bpy.ops.mesh.select_less() 

                            else:                                                                                                                        
                                n = 3                     
                                for i in range(n):
                                    bpy.ops.mesh.select_less()  

                                if self.fchl_bvl2_profile < 1.00: 
                                    bpy.ops.mesh.select_less() 
                                    bpy.ops.mesh.select_less()


                        else:
                            if self.fchl_bvl2_profile < 1.00: 
                                bpy.ops.mesh.select_less() 
                                bpy.ops.mesh.select_less() 

                            n = self.fchl_bvl2_segment+1                       
                            for i in range(n):
                                bpy.ops.mesh.select_less() 

          
                        # add pipe hole
                        if self.fchl_pipe_use == True: 

                            bpy.ops.mesh.inset(thickness=self.fchl_pipe_scale+self.fchl_bvl2_offset/2, use_outset=False)                                                  

                            # assign a material to pipe
                            if self.fchl_mat == True:
                                
                                obj = bpy.context.object 
                                
                                obj.vertex_groups.new('VerGrp_4')
                                bpy.ops.object.vertex_group_assign()
                                bpy.ops.object.vertex_group_set_active(group='VerGrp_4')
                                
                                # create material and assign
                                bpy.ops.object.material_slot_add()           
                                obj.material_slots[obj.material_slots.__len__() - 1].material = tbhl_create_material_4()   

                                bpy.ops.mesh.select_all(action='DESELECT')
                                bpy.ops.object.vertex_group_select()

                                #bpy.context.object.active_material_index = 4
                                bpy.ops.object.material_slot_assign()

                           
                            bpy.ops.mesh.inset(thickness=0, depth=self.fchl_pipe_depth*-1+self.fchl_pipe_offset*-1, use_outset=False)  

                           
                            if self.fchl_bvl_pipe_use == True:    
                                                        
                                bpy.ops.mesh.select_more()
                                bpy.ops.mesh.loop_to_region()
                                bpy.ops.mesh.region_to_loop()

                                bpy.ops.mesh.bevel(offset=self.fchl_pipe_offset, segments=self.fchl_pipe_segment, profile=self.fchl_pipe_profile, loop_slide = self.fchl_bvl_pipe_loopslide_use)         

                                # border edge
                                if self.fchl_pipe_profile < 1.00:
                                    bpy.ops.mesh.inset(thickness=self.fchl_pipe_offset/2, use_outset=True)



                        # add poke
                        if self.fchl_poke == True:                       
                   
                            # count and count and ... 
                            if self.fchl_pipe_use == True: 
                                bpy.ops.mesh.select_more()
                            
                                if self.fchl_pipe_profile < 1.00:
                                    bpy.ops.mesh.select_more()
           
                                if self.fchl_pipe_segment < 3:                                                                                                                         
                                    
                                    if self.fchl_pipe_segment < 2:  
                                        n = 4                     
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()   

                                        if self.fchl_pipe_profile < 1.00: 
                                            n = 4                     
                                            for i in range(n):
                                                bpy.ops.mesh.select_less()  

                                    else:                                                                                                                        
                                        n = 6                     
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()  

                                        if self.fchl_pipe_profile < 1.00: 
                                            n = 4                     
                                            for i in range(n):
                                                bpy.ops.mesh.select_less()  

                                else:
                                    if self.fchl_pipe_profile < 1.00: 
                                        n = 4                     
                                        for i in range(n):
                                            bpy.ops.mesh.select_less()  

                                    n = self.fchl_pipe_segment+1                     
                                    for i in range(n):
                                        
                                        if self.fchl_pipe_segment == 3:                                             
                                            n = 2                   
                                            for i in range(n):
                                                bpy.ops.mesh.select_less()                                              
                                        else:                                            
                                            n = 1+1                     
                                            for i in range(n):
                                                bpy.ops.mesh.select_less()  
                           
                            # triangulate with poke
                            bpy.ops.mesh.poke(offset=self.fchl_poke_offset)


            # use inset instead of bevel
            if self.fchl_tube == False: 
                for i in range(self.fchl_bvl_inset_fin_use):                  
                    bpy.ops.mesh.inset(thickness=self.fchl_bvl_inset_fin, use_outset=False)


        # back to select mode? 
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):            
            bpy.ops.mesh.select_mode(type="VERT")         
        else:
            bpy.ops.mesh.select_mode(type="FACE") 
        
        # shift to selected
        bpy.ops.view3d.snap_cursor_to_selected()




        # smooth shading
        if self.fchl_smooth == True: 
            
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            # smooth
            bpy.ops.mesh.faces_shade_smooth()


        # roundness
        if self.fchl_sphere_use == True: 
            
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            #round borderedge
            bpy.ops.mesh.region_to_loop()
            bpy.ops.transform.tosphere(value=self.fchl_sphere)

            # bevel
            if self.fchl_bvl4_use == True: 
                bpy.ops.mesh.bevel(offset=self.fchl_bvl4_offset, segments=self.fchl_bvl4_segment, profile=self.fchl_bvl4_profile, loop_slide=self.fchl_bvl4_loopslide_use)          
               
                if self.fchl_bvl4_profile < 1.00:
                    bpy.ops.mesh.inset(thickness=self.fchl_bvl4_offset/2, use_outset=True)


        if self.fchl_split == True: 
            # get custom vertex group
            bpy.ops.mesh.select_all(action='DESELECT')
            sel_id = bpy.context.object.vertex_groups.active_index
            bpy.ops.object.vertex_group_select(sel_id)  

            # split
            bpy.ops.mesh.split()


        # material check with mat-id and color picker type
        if len(context.object.material_slots) > 0:
            ob = bpy.context.object
            try:
               mat = ob.data.materials[self.index_count]
            except IndexError:
                print(self)
                self.report({'INFO'}, "No further Material!")  
                pass
            else:        
                if bpy.context.scene.render.engine == 'BLENDER_RENDER':                   
                    words = self.my_swatch
                    color = (float(words[0]), float(words[1]), float(words[2]))            
                    mat.diffuse_color = color

                else:
                    node=mat.node_tree.nodes['Diffuse BSDF']         
                    words = self.my_swatch
                    RGB = (float(words[0]), float(words[1]), float(words[2]),1) 
                    node.inputs['Color'].default_value = RGB
        else:
            pass


        # delete all custom vertex group    
        ob = bpy.context.object
        for vgroup in ob.vertex_groups:
            #if vgroup.name.startswith("VerGrp_1"):
            ob.vertex_groups.remove(vgroup)


        #print(self)
        #self.report({'INFO'}, "FaceTube")  
        return {'FINISHED'}


# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 


