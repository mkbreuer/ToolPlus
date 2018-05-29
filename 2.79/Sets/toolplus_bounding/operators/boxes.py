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
#"name": "T+ Bounding Box", 
#"author": "marvink.k.breuer (MKB)",
#"version": (1, 1),
#"blender": (2, 78, 0),
#"location": "View3D > TAB Tools > Panel: Bounding",
#"description": "add bounding box to selected objects",
#"wiki_url": "https://github.com/mkbreuer/ToolPlus",
#"category": "ToolPlus"}


# LOAD CACHE #
from toolplus_bounding.caches.cache      import  (settings_load)
from toolplus_bounding.caches.cache      import  (settings_write)


# LOAD MODULE #
import bpy
import bmesh
from bpy import *
from bpy.props import *

import mathutils, math, re
from mathutils.geometry import intersect_line_plane
from mathutils import Vector
from math import radians
from math import pi

# ADD GEOMETRY #
def build_grid(subX, subY, subR, bgrid_rota_x, bgrid_rota_y, bgrid_rota_z):
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=subX, y_subdivisions=subY, radius=subR, rotation=(bgrid_rota_x, bgrid_rota_y, bgrid_rota_z))

def build_cube(bcube_rad, bcube_rota_x, bcube_rota_y, bcube_rota_z):
    bpy.ops.mesh.primitive_cube_add(radius=bcube_rad, rotation=(bcube_rota_x, bcube_rota_y, bcube_rota_z))

def build_box(self, context):
    width = self.scale.x
    height = self.scale.y
    depth = self.scale.z

                
    verts = [(+1.0 * width, +1.0 * height, -1.0 * depth),
             (+1.0 * width, -1.0 * height, -1.0 * depth),
             (-1.0 * width, -1.0 * height, -1.0 * depth),
             (-1.0 * width, +1.0 * height, -1.0 * depth),
             (+1.0 * width, +1.0 * height, +1.0 * depth),
             (+1.0 * width, -1.0 * height, +1.0 * depth),
             (-1.0 * width, -1.0 * height, +1.0 * depth),
             (-1.0 * width, +1.0 * height, +1.0 * depth),
             ]
    edges = []
    faces = [(0, 1, 2, 3),
             (4, 7, 6, 5),
             (0, 4, 5, 1),
             (1, 5, 6, 2),
             (2, 6, 7, 3),
             (4, 0, 3, 7),
            ]


    mesh = bpy.data.meshes.new(name="_bbox")
    mesh.from_pydata(verts, edges, faces)

    # add the mesh as an object into the scene with this utility module
    from bpy_extras import object_utils
    object_utils.object_data_add(context, mesh, operator=self)



# BEVEL #
def func_bevel_cube(box_offset, box_segment, box_profile, box_verts_use):
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="EDGE")   
    bpy.context.tool_settings.mesh_select_mode=(False, True, False)   
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent()       
    bpy.ops.mesh.bevel(offset=box_offset, segments=box_segment, profile=box_profile, vertex_only=box_verts_use)          
    bpy.ops.object.editmode_toggle()


# SPHERE #
def func_sphere_cube(box_sphere):
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.context.tool_settings.mesh_select_mode=(True, True, True)   
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent()       
    bpy.ops.transform.tosphere(value=box_sphere)       
    bpy.ops.object.editmode_toggle()


# SUBDIVIDE #
def func_subdivide(box_subdiv, box_subdiv_smooth):
    bpy.ops.object.editmode_toggle()              
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent()                                                                           
    bpy.ops.mesh.subdivide(number_cuts=box_subdiv, smoothness=box_subdiv_smooth)             
    bpy.ops.object.editmode_toggle()   


# LISTS FOR SELECTED #
name_list = []
dummy_list = []

# MAIN OPERATOR #
class VIEW3D_TP_BBox_Cube(bpy.types.Operator):
    """create bounding boxes for selected objects / copy local orientation"""      
    bl_idname = "tp_ops.bbox_cube"
    bl_label = "Bounding"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    tp_geom_box = bpy.props.EnumProperty(
        items=[("tp_bb1"    ,"Grid"   ,"add grid plane"  ),
               ("tp_bb2"    ,"Cube"   ,"add a cube"      )],
               name = "",
               default = "tp_bb2",    
               description = "choose geometry for bounding")

    # NAME #
    tp_rename_boxes = BoolProperty(name="ReName", default=False, description="uncheckt: use name from active / checkt: use custom name")

    box_prefix = bpy.props.StringProperty(name="Name", default="")
    grid_prefix = bpy.props.StringProperty(name="Name", default="")

    box_name = bpy.props.StringProperty(name="Name", default="_custom")
    grid_name = bpy.props.StringProperty(name="Name", default="_custom")

    box_shaded_suffix = bpy.props.StringProperty(name="Name", default="_box_shaded")
    box_shadeless_suffix = bpy.props.StringProperty(name="Name", default="_box_shadeless")
    box_wired_suffix = bpy.props.StringProperty(name="Name", default="_box_wired")

    grid_shaded_suffix = bpy.props.StringProperty(name="Name", default="_grid_shaded")
    grid_shadeless_suffix = bpy.props.StringProperty(name="Name", default="_grid_shadeless")
    grid_wired_suffix = bpy.props.StringProperty(name="Name", default="_grid_wired")


    # GRID #
    subX = bpy.props.IntProperty(name="X Subdiv", description="set vertices value",  min=2, max=100, default=0, step=1)
    subY = bpy.props.IntProperty(name="Y Subdiv", description="set vertices value",  min=2, max=100, default=0, step=1)
    subR = bpy.props.FloatProperty(name="Radius", description="set vertices value", default=1.0, min=0.01, max=100)            

    bgrid_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bgrid_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bgrid_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # CUBE #

    scale = FloatVectorProperty(name="Scale", default=(1.0, 1.0, 1.0), subtype='TRANSLATION', description="scaling" )
    rotation = FloatVectorProperty(name="Rotation", subtype='EULER')

    bcube_rad = FloatProperty(name="Radius",  default=1.0, min=0.01, max=100, description="xyz scaling")

    bcube_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bcube_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bcube_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # generic transform props
    view_align = BoolProperty(name="Align to View", default=False)
    location = FloatVectorProperty(name="Location", subtype='TRANSLATION')
    rotation = FloatVectorProperty(name="Rotation",subtype='EULER')
    layers = BoolVectorProperty(name="Layers", size=20, subtype='LAYER', options={'HIDDEN', 'SKIP_SAVE'}) 
            
    # TOOLS #
    box_subdiv_use = bpy.props.BoolProperty(name="Subdivide",  description="activate subdivide", default=False) 
    box_subdiv = bpy.props.IntProperty(name="Loops", description="How many?", default=1, min=0, max=20, step=1)                   
    box_subdiv_smooth = bpy.props.FloatProperty(name="Smooth",  description="smooth subdivide", default=0.0, min=0.0, max=1.0)                    

    box_sphere_use = bpy.props.BoolProperty(name="Use Sphere",  description="activate to sphere", default=False) 
    box_sphere = bpy.props.FloatProperty(name="Sphere",  description="transform to sphere", default=1, min=0, max=1) 

    box_bevel_use = bpy.props.BoolProperty(name="Use Bevel",  description="activate bevel", default=False) 
    box_segment = bpy.props.IntProperty(name="Segments",  description="set segment", default=2, min=0, max=20, step=1) 
    box_profile = bpy.props.FloatProperty(name="Profile",  description="set profile", default=1, min=0, max=1)
    box_offset = bpy.props.FloatProperty(name="Offset",  description="set offset", default=0.2, min=0, max=10)
    box_verts_use = bpy.props.BoolProperty(name="Use Vertices",  description="activate vertex extrusion", default=False) 

    # BOX # 
    box_dim = bpy.props.BoolProperty(name="Copy Scale",  description="deactivate copy scale", default=True) 
    box_dim_apply = bpy.props.BoolProperty(name="Apply Scale",  description="apply copied scale", default=True) 

    box_rota = bpy.props.BoolProperty(name="Copy Rotation",  description="deactivate copy rotation", default=True) 

    box_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "",
               default = "tp_00",    
               description = "change meshtype")

    box_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    box_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    box_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    box_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)    

    # MATERIAL #
    box_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    box_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    box_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    box_get_local = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"" ),
               ("tp_w1"    ,"Local"     ,"" ),
               ("tp_w2"    ,"Global"    ,"" )],
               name = "Set Local Widget",
               default = "tp_w0",    
               description = "widget orientation")

 
    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(1)         
        
        row = box.column(1) 
        row.label("Object Name:")               

        if self.tp_geom_box == "tp_bb2":
            row.prop(self, "box_prefix", text="prefix")
            row.prop(self, "box_name", text="custom")

            if self.box_meshtype == "tp_00":    
                row.prop(self, "box_shaded_suffix", text="suffix")

            if self.box_meshtype == "tp_01":    
                row.prop(self, "box_shadeless_suffix", text="suffix")

            if self.box_meshtype == "tp_02":    
                row.prop(self, "box_wired_suffix", text="suffix")

        else:
            row.prop(self, "grid_prefix", text="prefix")
            row.prop(self, "grid_name", text="custom")
            
            if self.box_meshtype == "tp_00":            
                row.prop(self, "grid_shaded_suffix", text="suffix")
            
            if self.box_meshtype == "tp_01":
                row.prop(self, "grid_shadeless_suffix", text="suffix")
            
            if self.box_meshtype == "tp_02":
                row.prop(self, "grid_wired_suffix", text="suffix")

        box.separator()   

        box = layout.box().column(1)         
           
        row = box.row(1) 
        row.label("Object Type:")               
        row.prop(self, "tp_geom_box", text="")

        box.separator()   

        row = box.row(1) 
        row.label("Mesh Type:")               
        row.prop(self, "box_meshtype", text="")

        box.separator()                 

        box = layout.box().column(1)   
       
        row = box.row(1) 
        row.prop(self, "box_dim", text="") 
        row.label("Copy Scale")              
                       
        row.separator()
        
        row.prop(self, "box_dim_apply", text="")     
        row.label("Apply Scale") 
  
        box.separator()

        if self.tp_geom_box == "tp_bb2":

            box.separator()

            row = box.row(1) 
            row.prop(self, "box_subdiv_use", text="")
            row.label("Subdivide:") 

            sub = row.row(1)
            sub.scale_x = 1.175
            sub.prop(self, "box_subdiv")
     
            row = box.row(1)        
            row.label("", icon ="BLANK1") 
            row.label(" ") 
            
            sub = row.row(1)
            sub.scale_x = 1.175         
            sub.prop(self, "box_subdiv_smooth")


        if self.tp_geom_box == "tp_bb1": 

            box.separator()
          
            row = box.row(1) 
            row.label("Resolution:") 
            
            sub0 = row.column(1)
            sub0.scale_x = 1

            sub0.prop(self, "subX")
            sub0.prop(self, "subY")           
            if self.box_dim == False:  

                box.separator()  

                row = box.row(1) 
                row.label("Dimension:") 
              
                sub0 = row.column(1)
                sub0.prop(self, "subR")

        else:
            if self.box_dim == False:

                box.separator()

                row = box.row(1) 
                row.label("Dimension:") 
                
                sub0 = row.column(1)
                sub0.scale_x = 1

                if context.space_data.local_view is not None:                
                    sub0.prop(self, "bcube_rad", text="")
                else:                
                    sub0.prop(self, "scale", text="")

        box.separator()

        
        row = box.row(1) 
        row.label("Copy Rotation:") 
        row.prop(self, "box_rota", text="") 
            

        if self.tp_geom_box == "tp_bb1":

            if self.box_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "bgrid_rota_x")             
                row.prop(self, "bgrid_rota_y")             
                row.prop(self, "bgrid_rota_z")    
     
        else:

            if self.box_rota == True:
                pass
            else:

                if context.space_data.local_view is not None:
                    #bpy.ops.view3d.localview()
                    row = box.row(1)             
                    row.prop(self, "bcube_rota_x")             
                    row.prop(self, "bcube_rota_y")             
                    row.prop(self, "bcube_rota_z")   

                else:
                    row = box.row(1)             
                    row.prop(self, "rotation", text="")  

            box.separator()


        box = layout.box().column(1)           
        
        row = box.row(1)   
        row.prop(self, "box_origin", icon="BLANK1")
        row.prop(self, "box_xray", icon="BLANK1")   

        row = box.row(1)        
        row.prop(self, "box_smooth", icon="BLANK1")
        row.prop(self, "box_edges", icon="BLANK1")     

        box.separator() 
        



        box = layout.box().column(1)   

        if self.tp_geom_box == "tp_bb1":

            row = box.row(1) 
            row.prop(self, "box_sphere_use")

            row = box.row(1) 
            row.prop(self, "box_sphere")

            box.separator()
            box.separator()


        row = box.row(1) 
        row.prop(self, "box_bevel_use")
        row.prop(self, "box_verts_use")
            
        row = box.row(1) 
        row.prop(self, "box_segment")
        
        row = box.row(1)           
        row.prop(self, "box_offset")
        
        row = box.row(1)            
        row.prop(self, "box_profile")

        box.separator()


        box = layout.box().column(1)             

        row = box.row(1)         
        row.prop(self, "box_mat", text ="")
        row.label(text="Color:")  
        if bpy.context.scene.render.engine == 'CYCLES':
            row.prop(self, "box_cyclcolor", text ="")        
        else:
            row.prop(self, "box_color", text ="")        
                              
        box.separator() 
        box.separator()  
      
        row = box.row(1)
        row.label(text="Widget:")
        row.prop(self, "box_get_local", expand = True)        
       
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
        
        #grid_name = "_grid"     
        #box_name = "_box"         
       
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

                # add geometry
                if self.tp_geom_box == "tp_bb1":
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')                
                    build_grid(self.subX, self.subY, self.subR, self.bgrid_rota_x, self.bgrid_rota_y, self.bgrid_rota_z)                                              

                    if self.tp_rename_boxes == False:

                        bpy.context.object.name = self.grid_prefix + obj.name + self.grid_shaded_suffix
                        bpy.context.object.data.name = self.grid_prefix + obj.name + self.grid_shaded_suffix  
                        
                        # add new object to dummy name list
                        new_object_name = self.grid_prefix + obj.name + self.grid_shaded_suffix
                        dummy_list.append(new_object_name) 
                      
                    else:

                        bpy.context.object.name = self.grid_prefix + self.grid_name + self.grid_shaded_suffix
                        bpy.context.object.data.name = self.grid_prefix + self.grid_name + self.grid_shaded_suffix  
                        
                        # add new object to dummy name list
                        new_object_name = self.grid_prefix + self.grid_name + self.grid_shaded_suffix
                        dummy_list.append(new_object_name) 


                else:
                    
                    # check if local view
                    if context.space_data.local_view is not None:
                        
                        # jump out from local view
                        #bpy.ops.view3d.localview()

                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')                                                   
                       
                        # add default cube primitiv
                        build_cube(self.bcube_rad, self.bcube_rota_x, self.bcube_rota_y, self.bcube_rota_z)

                    else:
                                        
                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')    
                        
                        # add defined mesh cube 
                        build_box(self, context)
                     
   
                    if self.tp_rename_boxes == False:
 
                        bpy.context.object.name = self.box_prefix + obj.name + self.box_shaded_suffix
                        bpy.context.object.data.name = self.box_prefix + obj.name + self.box_shaded_suffix
 
                        # add new object to dummy name list
                        new_object_name = self.box_prefix + obj.name + self.box_shaded_suffix
                        dummy_list.append(new_object_name) 

                    else:

                        bpy.context.object.name = self.box_prefix + self.box_name + self.box_shaded_suffix
                        bpy.context.object.data.name = self.box_prefix + self.box_name + self.box_shaded_suffix

                        # add new object to dummy name list
                        new_object_name = self.box_prefix + self.box_name + self.box_shaded_suffix
                        dummy_list.append(new_object_name) 
                        

                active = bpy.context.active_object             
                
                # add material with enabled object color
                for i in range(self.box_mat):            
                    mat_name = [obj.name]
                    mat = bpy.data.materials.new(obj.name)

                    if len(active.data.materials):
                        active.data.materials[0] = mat
                    else:
                        active.data.materials.append(mat)

                    if bpy.context.scene.render.engine == 'CYCLES':
                        bpy.context.object.active_material.diffuse_color = (self.box_cyclcolor)
                    else:
                        bpy.context.object.active_material.use_object_color = True
                        bpy.context.object.color = (self.box_color)


                # copy data from to new object
                active.location = obj.location

                for i in range(self.box_dim):
                    active.dimensions = obj.dimensions
                
                    # apply scale                    
                    for i in range(self.box_dim_apply):
                        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

                for i in range(self.box_rota):
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
                if self.box_origin == "tp_o0":
                    pass
                
                if self.box_origin == "tp_o1":                                                
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')                      
               
                if self.box_origin == "tp_o2":
                    bpy.ops.tp_ops.bbox_origin_minus_z()     
     
                if self.box_origin == "tp_o3":                                
                    bpy.ops.tp_ops.bbox_origin_plus_z()   

             
                if self.tp_geom_box == "tp_bb2":

                    # subdivide
                    for i in range(self.box_subdiv_use): 
                        func_subdivide(self.box_subdiv, self.box_subdiv_smooth)  
     
                if self.tp_geom_box == "tp_bb1":

                    # to sphere
                    for i in range(self.box_sphere_use): 
                        func_sphere_cube(self.box_sphere)   
 
                # display: xray
                for i in range(self.box_xray):
                    bpy.context.object.show_x_ray = True
          
                # display: draw all edges
                for i in range(self.box_edges):
                    bpy.context.object.show_wire = True
                    bpy.context.object.show_all_edges = True                                   

                # stay shaded
                if self.box_meshtype == "tp_00":
                    pass

                # SHADLESS MESH
                if self.box_meshtype == "tp_01":
                    bpy.context.object.draw_type = 'WIRE'

                    # second rename
                    if self.tp_rename_boxes == False:
 
                        if self.tp_geom_box == "tp_bb1":               
                            bpy.context.object.name = self.grid_prefix + obj.name + self.grid_shadeless_suffix
                            bpy.context.object.data.name = self.grid_prefix + obj.name + self.grid_shadeless_suffix            
                        else:          
                            bpy.context.object.name = self.box_prefix + obj.name + self.box_shadeless_suffix
                            bpy.context.object.data.name = self.box_prefix + obj.name + self.box_shadeless_suffix 

                    else:
                        
                        if self.tp_geom_box == "tp_bb1":               
                            bpy.context.object.name = self.grid_prefix + self.grid_name + self.grid_shadeless_suffix
                            bpy.context.object.data.name = self.grid_prefix + self.grid_name + self.grid_shadeless_suffix             
                        else:          
                            bpy.context.object.name = self.box_prefix + self.box_name + self.box_shadeless_suffix
                            bpy.context.object.data.name = self.box_prefix + self.box_name + self.box_shadeless_suffix  



                # display: smooth
                for i in range(self.box_smooth):                 
                    bpy.ops.object.shade_smooth()
                
                # create bevel
                for i in range(self.box_bevel_use):                                   
                    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
                    func_bevel_cube(self.box_offset, self.box_segment, self.box_profile, self.box_verts_use)
                    
                # WIRED MESH
                if self.box_meshtype == "tp_02":            
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.delete(type='ONLY_FACE')
                    bpy.ops.object.editmode_toggle()
     
                    # third rename
                    if self.tp_rename_boxes == False:

                        if self.tp_geom_box == "tp_bb1":                
                            bpy.context.object.name = self.grid_prefix + obj.name + self.grid_wired_suffix  
                            bpy.context.object.data.name = self.grid_prefix + obj.name + self.grid_wired_suffix            
                        else:            
                            bpy.context.object.name = self.box_prefix + obj.name + self.box_wired_suffix
                            bpy.context.object.data.name = self.box_prefix + obj.name + self.box_wired_suffix 
                        
                    else:

                        if self.tp_geom_box == "tp_bb1":                
                            bpy.context.object.name = self.grid_prefix + self.grid_name + self.grid_wired_suffix
                            bpy.context.object.data.name = self.grid_prefix + self.grid_name + self.grid_wired_suffix            
                        else:            
                            bpy.context.object.name = self.box_prefix + self.box_name + self.box_wired_suffix
                            bpy.context.object.data.name = self.box_prefix + self.box_name + self.box_wired_suffix

         
                # fix normals
                bpy.ops.tp_ops.rec_normals()



        # set widget orientation
        if self.box_get_local == "tp_w0":
            pass
        elif self.box_get_local == "tp_w1":
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



















