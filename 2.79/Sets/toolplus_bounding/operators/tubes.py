# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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


#bl_info = {
#"name": "T+ Bounding Cylinder", 
#"author": "marvink.k.breuer (MKB)",
#"version": (1, 1),
#"blender": (2, 78, 0),
#"location": "View3D > TAB Tools > Panel: Bounding",
#"description": "add bounding cylinder or cone to selected objects",
#"wiki_url": "https://github.com/mkbreuer/ToolPlus",
#"category": "ToolPlus"}


# LOAD CACHE #
from toolplus_bounding.caches.cache      import  (settings_load)
from toolplus_bounding.caches.cache      import  (settings_write)


# LOAD MODULE #
import bpy, bmesh
from bpy import *
from bpy.props import *


# ADD GEOMETRY #
def add_circ(bcirc_res, bcirc_rad, tube_fill, bcirc_rota_x, bcirc_rota_y, bcirc_rota_z):
    bpy.ops.mesh.primitive_circle_add(vertices=bcirc_res, radius=bcirc_rad, fill_type=tube_fill, rotation=(bcirc_rota_x, bcirc_rota_y, bcirc_rota_z))

def add_cyl(bcyl_res, bcyl_rad, bcyl_dep, tube_fill, bcyl_rota_x, bcyl_rota_y, bcyl_rota_z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=bcyl_res, radius=bcyl_rad, depth=bcyl_dep, end_fill_type=tube_fill, rotation=(bcyl_rota_x, bcyl_rota_y, bcyl_rota_z))    

def add_cone(bcon_res, bcon_res1, bcon_res2, bcon_depth, tube_fill, bcon_rota_x, bcon_rota_y, bcon_rota_z):
    bpy.ops.mesh.primitive_cone_add(vertices=bcon_res, radius1=bcon_res1, radius2=bcon_res2, depth=bcon_depth, end_fill_type=tube_fill, rotation=(bcon_rota_x, bcon_rota_y, bcon_rota_z))

def add_torus(btor_seg1, btor_seg2, btor_siz1, btor_siz2, btor_rota_x, btor_rota_y, btor_rota_z):
    bpy.ops.mesh.primitive_torus_add(rotation=(btor_rota_x, btor_rota_y, btor_rota_z), major_segments=btor_seg1, minor_segments=btor_seg2, mode="MAJOR_MINOR" , major_radius=btor_siz1, minor_radius=btor_siz2)#, abso_major_rad=btor_rad1, abso_minor_rad=btor_rad2)


# EXTRUSION #
def func_extrude(bvl_extrude_offset):
    # store current mode
    current_mode = bpy.context.mode
    bpy.ops.object.mode_set(mode='EDIT')
    
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type="FACE")   
    bpy.context.tool_settings.mesh_select_mode=(False, False, True)   

    bpy.ops.mesh.select_face_by_sides(number=4, type='EQUAL')      
    bpy.ops.mesh.select_all(action='INVERT')         

    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    for face in bm.faces:
        if face.select:          

            scale = bvl_extrude_offset  
            bpy.ops.transform.shrink_fatten(value=scale, use_even_offset=False, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    # reload previous mode
    bpy.ops.object.mode_set(mode=current_mode)  
    bpy.ops.tp_ops.rec_normals()      


# BEVEL #
def func_bevel(bvl_offset, bvl_segment, bvl_profile, bvl_select_all, bvl_verts_use):
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # store current mode
    current_mode = bpy.context.mode
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type="FACE")   
    bpy.context.tool_settings.mesh_select_mode=(False, False, True)  

    bpy.ops.mesh.select_face_by_sides(number=4, type='EQUAL')      
    bpy.ops.mesh.select_all(action='INVERT')         

    # select all edges
    if bvl_select_all == True:
        bpy.ops.mesh.select_all(action='SELECT')
    
    bpy.ops.mesh.bevel(offset=bvl_offset, segments=bvl_segment, profile=bvl_profile, vertex_only=bvl_verts_use)          

    # reload previous mode
    bpy.ops.object.mode_set(mode=current_mode)  
    bpy.ops.tp_ops.rec_normals()    


# PIPE #
def func_pipe(bvl_pipe_offset):
    # store current mode
    current_mode = bpy.context.mode
    bpy.ops.object.mode_set(mode='EDIT')
 
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type="FACE")   
    bpy.context.tool_settings.mesh_select_mode=(False, False, True)  

    bpy.ops.mesh.select_face_by_sides(number=4, type='EQUAL')      
    bpy.ops.mesh.select_all(action='INVERT')
    
    bpy.ops.mesh.inset(thickness=bvl_pipe_offset)
    
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    for face in bm.faces:
        if face.select:
            bpy.ops.mesh.bridge_edge_loops()

    # reload previous mode
    bpy.ops.object.mode_set(mode=current_mode)  
    bpy.ops.tp_ops.rec_normals()    


# LISTS FOR SELECTED #
name_list = []
dummy_list = []

# MAIN OPERATOR #
class VIEW3D_TP_BTube(bpy.types.Operator):
    """create a bounding geometry on selected mesh / copy local orientation"""
    bl_idname = "tp_ops.bbox_cylinder"
    bl_label = "Bounding"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    tp_geom_tube = bpy.props.EnumProperty(
        items=[("tp_add_cyl"   ,"Tube"   ,"add cylinder" ,1),
               ("tp_add_cone"  ,"Cone"   ,"add cone"     ,2),
               ("tp_add_circ"  ,"Circle" ,"add circle"   ,3),
               ("tp_add_tor"   ,"Torus"  ,"add torus"    ,4)],
               name = "ObjectType",
               default = "tp_add_cyl",    
               description = "change mesh type")

    tube_fill = bpy.props.EnumProperty(
        items=[("NOTHING"   ,"Nothing"  ,""   ),
               ("NGON"      ,"Ngon"     ,""   ),
               ("TRIFAN"    ,"Triangle" ,""   )],
               name = "FillType",
               default = "NGON",    
               description = "change fill type")

    # CIRCLE #
    bcirc_res = bpy.props.IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bcirc_rad = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)

    bcirc_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcirc_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcirc_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CYLINDER #
    bcyl_res = bpy.props.IntProperty(name="Verts", description="set vertices value",  min=3, max=80, default=12)
    bcyl_rad = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)
    bcyl_dep = bpy.props.FloatProperty(name="Depth", description="set depth value", default=1.0, min=0.01, max=100)

    bcyl_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcyl_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcyl_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CONE #
    bcon_res = bpy.props.IntProperty(name="Verts", description="vertices value",  min=3, max=80, default=12)
    bcon_res1 = bpy.props.FloatProperty(name="Bottom", description="set bottom value",  min=0.01, max=100, default=2.5)
    bcon_res2 = bpy.props.FloatProperty(name="Top", description="set top value",  min=0.01, max=100, default=1.0)
    bcon_depth = bpy.props.FloatProperty(name="Depth", description="set depth value",  min=1, max=100, default=2)

    bcon_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcon_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcon_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TORUS #
    btor_seg1 = bpy.props.IntProperty(name="Major Segments", description="set value",  min=1, max=100, default=51) 
    btor_seg2 = bpy.props.IntProperty(name="Minor Segments", description="set value",  min=1, max=100, default=15)
    btor_siz1 = bpy.props.FloatProperty(name="Major Radius", description="set value", default=1.13, min=0.01, max=1000)
    btor_siz2 = bpy.props.FloatProperty(name="Minor Radius", description="set value", default=0.78, min=0.01, max=1000)

    btor_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    btor_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    btor_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TOOLS #
    bvl_pipe_use = bpy.props.BoolProperty(name="Use Pipe",  description="activate pipe", default=False) 
    bvl_pipe_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0.01, max=100)

    bvl_bevel_use = bpy.props.BoolProperty(name="Use Bevel",  description="activate bevel", default=False) 
    bvl_select_all = bpy.props.BoolProperty(name="All",  description="use bevel on each edge", default=False) 
    bvl_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    bvl_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1, min=0, max=1)
    bvl_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0, max=10) 
    bvl_verts_use = bpy.props.BoolProperty(name="Vertices",  description="activate vertex extrusion", default=False) 

    bvl_extrude_use = bpy.props.BoolProperty(name="Use Extrude",  description="activate extrusion", default=False) 
    bvl_extrude_offset = bpy.props.FloatProperty(name="Extrude",  description="extrude on local z axis", default=1, min=0, max=100) 


    # TUBE # 
    tube_dim = bpy.props.BoolProperty(name="Copy Scale",  description="deactivate copy scale", default=True) 
    tube_dim_apply = bpy.props.BoolProperty(name="Apply Scale",  description="apply copied scale", default=True) 

    tube_rota = bpy.props.BoolProperty(name="Rotation",  description="deactivate copy rotation", default=True) 

    tube_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "MeshType",
               default = "tp_00",    
               description = "change display type")

    tube_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    tube_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    tube_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    tube_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)    

    # MATERIAL #
    tube_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    tube_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    tube_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    tube_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Set Widget",
               default = "tp_w0",    
               description = "widget orientation")
               
               
    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(1)   

        row = box.row(1)
        row.label("Object Type:") 
        row.prop(self, "tp_geom_tube", text="")        

        box.separator()  

        row = box.row(1)  
        row.label("Mesh Type:") 
        row.prop(self, "tube_meshtype", text="")
        
        if self.tp_geom_tube == "tp_add_tor":
            pass
        else:
            box.separator() 
         
            row = box.row(1) 
            row.label("Fill Type:") 
            row.prop(self, "tube_fill", text="")
        
        box.separator()         


        box = layout.box().column(1)  

        row = box.row(1) 
        row.label("Copy Scale:")              
        row.prop(self, "tube_dim", text="")           

        row.label("Apply Scale:") 
        row.prop(self, "tube_dim_apply", text="")   

        box.separator()                

        if self.tp_geom_tube == "tp_add_cyl":

            box.separator() 

            row = box.row(1) 
            row.label("Resolution:") 

            sub1 = row.column(1)
            sub1.scale_x = 1
            sub1.prop(self, "bcyl_res")

            if self.tube_dim == True:
                pass
            else:            

                box.separator()  

                row = box.row(1) 
                row.label("Dimension:") 

                sub1 = row.column(1)

                sub1.prop(self, "bcyl_rad")
                sub1.prop(self, "bcyl_dep")

        if self.tp_geom_tube == "tp_add_cone":
            
            box.separator() 

            row = box.row(1) 
            row.label("Resolution:") 

            sub0 = row.column(1)
            sub0.scale_x = 1
            sub0.prop(self, "bcon_res")

            box.separator()  

            row = box.row(1) 
            row.label("Dimension:") 

            sub0 = row.column(1)
            sub0.prop(self, "bcon_res2")
            sub0.prop(self, "bcon_res1")  

            if self.tube_dim == True:
                pass
            else:            
                sub0.prop(self, "bcon_depth")

        if self.tp_geom_tube == "tp_add_circ":

            box.separator() 

            row = box.row(1) 
            row.label("Resolution:") 

            sub1 = row.column(1)
            sub1.scale_x = 1
            sub1.prop(self, "bcirc_res")

            if self.tube_dim == True:
                pass
            else:            
                box.separator()  

                row = box.row(1) 
                row.label("Dimension:") 

                sub1 = row.column(1)

                sub1.prop(self, "bcirc_rad")


        if self.tp_geom_tube == "tp_add_tor":
                
            box.separator() 

            row = box.row(1) 
            row.label("Resolution:") 

            row = box.column(1) 
            row.prop(self, "btor_seg1")
            row.prop(self, "btor_seg2")

            if self.tube_dim == True:
                pass
            else:            
                
                box.separator() 

                row = box.row(1) 
                row.label("Dimension:") 

                row = box.column(1)         
                row.prop(self, "btor_siz1")
                row.prop(self, "btor_siz2")


        box.separator()
        
        box = layout.box().column(1)      
        
        row = box.row(1) 
        row.label("Copy Rotation:") 
        row.prop(self, "tube_rota", text="") 
        
        if self.tp_geom_tube == "tp_add_cyl":

            if self.tube_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "bcyl_rota_x")             
                row.prop(self, "bcyl_rota_y")             
                row.prop(self, "bcyl_rota_z")    

 
        if self.tp_geom_tube == "tp_add_cone":

            if self.tube_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "bcon_rota_x")             
                row.prop(self, "bcon_rota_y")             
                row.prop(self, "bcon_rota_z")   
 

        if self.tp_geom_tube == "tp_add_circ":

            if self.tube_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "bcirc_rota_x")             
                row.prop(self, "bcirc_rota_y")             
                row.prop(self, "bcirc_rota_z")  


        if self.tp_geom_tube == "tp_add_tor":

            if self.tube_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "btor_rota_x")             
                row.prop(self, "btor_rota_y")             
                row.prop(self, "btor_rota_z") 



        box.separator()
        
        box = layout.box().column(1)  

        row = box.row(1)   
        row.prop(self, "tube_origin", icon="BLANK1", text="")
        row.prop(self, "tube_xray", icon="BLANK1")   

        row = box.row(1)        
        row.prop(self, "tube_smooth", icon="BLANK1")
        row.prop(self, "tube_edges", icon="BLANK1")               

        box.separator()

        box = layout.box().column(1)  

        if self.tp_geom_tube == "tp_add_cyl" or self.tp_geom_tube == "tp_add_cone":

            if self.tube_fill == "NGON": 

                row = box.row(1) 
                row.prop(self, "bvl_extrude_use")

                row = box.row(1) 
                row.prop(self, "bvl_extrude_offset")

                box.separator()
                box.separator()
             
                row = box.row(1) 
                row.prop(self, "bvl_pipe_use")
                row.prop(self, "bvl_pipe_offset")
     
                box.separator()
                box.separator()

                row = box.row(1) 

                row.prop(self, "bvl_bevel_use")
                row.prop(self, "bvl_select_all")                
                row.prop(self, "bvl_verts_use")
                
                row = box.column(1) 
                row.prop(self, "bvl_segment")         
                row.prop(self, "bvl_offset")           
                row.prop(self, "bvl_profile")

        box.separator()  

        box = layout.box().column(1)             

        row = box.row(1)         
        row.prop(self, "tube_mat", text ="")
        row.label(text="Color:")  
        if bpy.context.scene.render.engine == 'CYCLES':
            row.prop(self, "tube_cyclcolor", text ="")        
        else:
            row.prop(self, "tube_color", text ="")     

        box.separator()  
        box.separator()  
      
        row = box.row(1)
        row.label(text="Widget:")
        row.prop(self, "tube_get_local", expand = True)        
       
        box.separator()   

    
    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)
       
        # return context.window_manager.invoke_props_popup(self, event) 
        # panel unutilized with popup invoke  


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        settings_write(self) # custom props
        
        selected = bpy.context.selected_objects
        
        # set 3d cursor
        bpy.ops.view3d.snap_cursor_to_selected() 
        
        # store 3d cursor
        v3d = context.space_data
        if v3d.type == 'VIEW_3D':
                        
            rv3d = v3d.region_3d
            current_cloc = v3d.cursor_location.xyz         
            #v3d.cursor_location = ()
        
            for obj in selected:
                # add source to name list
                name_list.append(obj.name) 
                                      
                # add geometry and first rename 
                if self.tp_geom_tube == "tp_add_cyl":
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')                
                    add_cyl(self.bcyl_res, self.bcyl_rad, self.bcyl_dep, self.tube_fill, self.bcyl_rota_x, self.bcyl_rota_y, self.bcyl_rota_z)            
                    bpy.context.object.name = obj.name + "_shaded_tube"
                    bpy.context.object.data.name = obj.name + "_shaded_tube"
                
                    # add new object to dummy name list
                    new_object_name = obj.name + "_shaded_tube"
                    dummy_list.append(new_object_name) 

                if self.tp_geom_tube == "tp_add_cone":              
                    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                    add_cone(self.bcon_res, self.bcon_res1, self.bcon_res2, self.bcon_depth, self.tube_fill, self.bcon_rota_x, self.bcon_rota_y, self.bcon_rota_z)
                    bpy.context.object.name = obj.name + "_shaded_cone"
                    bpy.context.object.data.name = obj.name + "_shaded_cone"

                    # add new object to dummy name list
                    new_object_name = obj.name + "_shaded_cone"
                    dummy_list.append(new_object_name) 

                if self.tp_geom_tube == "tp_add_circ":   
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')                
                    add_circ(self.bcirc_res, self.bcirc_rad, self.tube_fill, self.bcirc_rota_x, self.bcirc_rota_y, self.bcirc_rota_z)
                    bpy.context.object.name = obj.name + "_shaded_circle"
                    bpy.context.object.data.name = obj.name + "_shaded_circle"
                
                    # add new object to dummy name list
                    new_object_name = obj.name + "_shaded_circle"
                    dummy_list.append(new_object_name) 

                if self.tp_geom_tube == "tp_add_tor":
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')  
                    add_torus(self.btor_seg1, self.btor_seg2, self.btor_siz1, self.btor_siz2, self.btor_rota_x, self.btor_rota_y, self.btor_rota_z)
                    bpy.context.object.name = obj.name + "_shaded_torus"
                    bpy.context.object.data.name = obj.name + "_shaded_torus"

                    # add new object to dummy name list
                    new_object_name = obj.name + "_shaded_torus"
                    dummy_list.append(new_object_name) 
                


                active = bpy.context.active_object             
                
                # add material with enabled object color
                for i in range(self.tube_mat):            
                    mat_name = [obj.name]
                    mat = bpy.data.materials.new(obj.name)

                    if len(active.data.materials):
                        active.data.materials[0] = mat
                    else:
                        active.data.materials.append(mat)

                    if bpy.context.scene.render.engine == 'CYCLES':
                        bpy.context.object.active_material.diffuse_color = (self.tube_cyclcolor)
                    else:
                        bpy.context.object.active_material.use_object_color = True
                        bpy.context.object.color = (self.tube_color)


                # copy data from to new object                
                for i in range(self.tube_dim):                    
                    active.dimensions = obj.dimensions

                    # apply scale
                    for i in range(self.tube_dim_apply):
                        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

                active.location = obj.location

                for i in range(self.tube_rota):   
                    active.rotation_euler = obj.rotation_euler
                                                 
                # reload 3d cursor
                v3d.cursor_location = current_cloc 
                
                # select objects in lists
                bpy.data.objects[obj.name].select = True                  
                bpy.data.objects[new_object_name].select = True                                  

                # place origin
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

                # deselect source
                bpy.data.objects[obj.name].select = False    

                # set origin 
                if self.tube_origin == "tp_o0":
                    pass
                
                if self.tube_origin == "tp_o1":                                
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')                      
               
                if self.tube_origin == "tp_o2":
                    bpy.ops.tp_ops.bbox_origin_minus_z()     
     
                if self.tube_origin == "tp_o3":                                
                    bpy.ops.tp_ops.bbox_origin_plus_z()   
                            
                # display: xray
                for i in range(self.tube_xray):
                    bpy.context.object.show_x_ray = True

                # display: draw all edges
                for i in range(self.tube_edges):
                    bpy.context.object.show_wire = True
                    bpy.context.object.show_all_edges = True     
               
                # stay shaded
                if self.tube_meshtype == "tp_00":
                    pass 
                                    
                # create shadeless
                if self.tube_meshtype == "tp_01":
                    bpy.context.object.draw_type = 'WIRE'

                    # second rename
                    if self.tp_geom_tube == "tp_add_cyl":
                        bpy.context.object.name = obj.name + "_shadless_tube"
                        bpy.context.object.data.name = obj.name + "_shadless_tube"
                    
                    if self.tp_geom_tube == "tp_add_cone":              
                        bpy.context.object.name = obj.name + "_shadless_cone"
                        bpy.context.object.data.name = obj.name + "_shadless_cone"

                    if self.tp_geom_tube == "tp_add_circ": 
                        bpy.context.object.name = obj.name + "_shadless_circle"
                        bpy.context.object.data.name = obj.name + "_shadless_circle"

                    if self.tp_geom_tube == "tp_add_torus":
                        bpy.context.object.name = obj.name + "_shadless_torus"
                        bpy.context.object.data.name = obj.name + "_shadless_torus"


                # display: smooth
                for i in range(self.tube_smooth):
                    bpy.ops.object.shade_smooth()

                # create extrusion
                for i in range(self.bvl_extrude_use):                                                    
                    func_extrude(self.bvl_extrude_offset)
                            
                # create pipe                     
                if self.tp_geom_tube == "tp_add_cyl" or self.tp_geom_tube == "tp_add_cone":
                    if self.tube_fill == "NGON": 
                        for i in range(self.bvl_pipe_use): 
                            func_pipe(self.bvl_pipe_offset)
                                                                                  
                # create bevel            
                for i in range(self.bvl_bevel_use):                                    
                    func_bevel(self.bvl_offset, self.bvl_segment, self.bvl_profile, self.bvl_select_all, self.bvl_verts_use)                  
                                         
                # create wired 
                if self.tube_meshtype == "tp_02": 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.delete(type='ONLY_FACE')
                    bpy.ops.object.editmode_toggle()
          
                    # third rename
                    if self.tp_geom_tube == "tp_add_cyl":
                        bpy.context.object.name = obj.name + "_wire_tube"
                        bpy.context.object.data.name = obj.name + "_wire_tube"
                    
                    if self.tp_geom_tube == "tp_add_cone":              
                        bpy.context.object.name = obj.name + "_wire_cone"
                        bpy.context.object.data.name = obj.name + "_wire_cone"

                    if self.tp_geom_tube == "tp_add_circ": 
                        bpy.context.object.name = obj.name + "_wire_circle"
                        bpy.context.object.data.name = obj.name + "_wire_circle"

                    if self.tp_geom_tube == "tp_add_torus":
                        bpy.context.object.name = obj.name + "_wire_torus"
                        bpy.context.object.data.name = obj.name + "_wire_torus"

        # set widget orientation
        if self.tube_get_local == "tp_w0":
            pass
        elif self.tube_get_local == "tp_w1":
            bpy.ops.tp_ops.space_local()               
        else:
            bpy.ops.tp_ops.space_global()   
            
        return {'FINISHED'}
            
            


# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()







