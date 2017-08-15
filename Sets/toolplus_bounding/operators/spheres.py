
bl_info = {
"name": "T+ Bounding Extras", 
"author": "marvink.k.breuer (MKB)",
"version": (1, 0),
"blender": (2, 78, 0),
"location": "View3D > TAB Tools > Panel: Bounding",
"description": "add bounding sphere to selected objects",
"wiki_url": "https://github.com/mkbreuer/ToolPlus",
"category": "ToolPlus"}


# LOAD CACHE #
from toolplus_bounding.caches.cache      import  (settings_load)
from toolplus_bounding.caches.cache      import  (settings_write)


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# ADD GEOMETRY #
def add_sphere(bsph_seg, bsph_rig, bsph_siz, bsph_rota_x, bsph_rota_y, bsph_rota_z):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=bsph_seg, ring_count=bsph_rig, size=bsph_siz, rotation =(bsph_rota_x, bsph_rota_y, bsph_rota_z))

def add_ico(bico_div, bico_siz, bico_rota_x, bico_rota_y, bico_rota_z):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=bico_div, size=bico_siz, rotation =(bico_rota_x, bico_rota_y, bico_rota_z))


# LISTS FOR SELECTED #
name_list = []
dummy_list = []


# MAIN OPERATOR #
class VIEW3D_TP_BTube(bpy.types.Operator):
    """create a bounding geometry on selected mesh / copy local orientation"""
    bl_idname = "tp_ops.bbox_sphere"
    bl_label = "Bounding"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    tp_geom_sphere = bpy.props.EnumProperty(
        items=[("tp_add_sph"  ,"Sphere" ,"add sphere" ),
               ("tp_add_ico"  ,"Ico"    ,"add ico"    )],
               name = "ObjectType",
               default = "tp_add_sph",    
               description = "change mesh type")

    # SPHERE #
    bsph_seg = bpy.props.IntProperty(name="Segments",  description="set value", min=1, max=100, default=32) 
    bsph_rig = bpy.props.IntProperty(name="Rings",  description="set value",  min=1, max=100, default=16) 
    bsph_siz = bpy.props.FloatProperty(name="Size",  description="set value", default=1.00, min=0.01, max=100) 

    bsph_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bsph_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bsph_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # ICO #
    bico_div = bpy.props.IntProperty(name="Subdiv",  description="set value", min=1, max=5, default=2) 
    bico_siz = bpy.props.FloatProperty(name="Size",  description="set value", default=1.00, min=0.01, max=100) 

    bico_rota_x = bpy.props.FloatProperty(name="X", description="set x rotation value", default=0, min=0, max=3.60*2)
    bico_rota_y = bpy.props.FloatProperty(name="Y", description="set y rotation value", default=0, min=0, max=3.60*2)
    bico_rota_z = bpy.props.FloatProperty(name="Z", description="set z rotation value", default=0, min=0, max=3.60*2)

    # TOOLS # 
    sphere_dim = bpy.props.BoolProperty(name="Copy Scale",  description="deactivate copy scale", default=True) 
    sphere_dim_apply = bpy.props.BoolProperty(name="Apply Scale",  description="apply copied scale", default=True) 

    sphere_rota = bpy.props.BoolProperty(name="Copy Rotation",  description="deactivate copy rotation", default=True) 

    sphere_meshtype = bpy.props.EnumProperty(
        items=[("tp_00"    ,"Shaded"      ,"set shaded mesh"                    ),
               ("tp_01"    ,"Shade off"   ,"set shade off for transparent mesh" ),
               ("tp_02"    ,"Wire only"   ,"delete only faces for wired mesh"   )],
               name = "MeshType",
               default = "tp_00",    
               description = "change display type")

    sphere_origin = bpy.props.EnumProperty(
        items=[("tp_o0"    ,"None"              ,"do nothing"              ),
               ("tp_o1"    ,"Origin Center"     ,"origin to center / XYZ"  ),
               ("tp_o2"    ,"Origin Bottom"     ,"origin to bottom / -Z"   ),
               ("tp_o3"    ,"Origin Top"        ,"origin to top / +Z"      )],
               name = "Set Origin",
               default = "tp_o0",    
               description = "set origin")

    # DISPLAY #
    sphere_edges = bpy.props.BoolProperty(name="Draw Edges",  description="draw wire on edges", default=False)    
    sphere_smooth = bpy.props.BoolProperty(name="Smooth Mesh",  description="smooth mesh shading", default=False)     
    sphere_xray = bpy.props.BoolProperty(name="X-Ray",  description="bring mesh to foreground", default=False)    

    # MATERIAL #
    sph_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)    
    sph_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    sph_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    # WIDGET #
    sph_get_local = bpy.props.EnumProperty(
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
        row.prop(self, "tp_geom_sphere", text="")        

        box.separator()  

        row = box.row(1)  
        row.label("Mesh Type:") 
        row.prop(self, "sphere_meshtype", text="")
        
        box.separator()         
      
        box = layout.box().column(1) 

        row = box.row(1) 
        row.label("Copy Scale:")              
        row.prop(self, "sphere_dim", text="")           

        row.label("Apply Scale:") 
        row.prop(self, "sphere_dim_apply", text="")  

        box.separator()

        if self.tp_geom_sphere == "tp_add_sph":

            row = box.row(1) 
            row.label("Resolution:") 

            sub1 = row.column(1)
            sub1.scale_x = 1
            sub1.prop(self, "bsph_seg")
            sub1.prop(self, "bsph_rig")

            if self.sphere_dim == True:
                pass
            else:            
           
                box.separator()  

                row = box.row(1) 
                row.label("Dimension:") 

                sub1 = row.column(1)

                sub1.prop(self, "bsph_siz")

        if self.tp_geom_sphere == "tp_add_ico":

            row = box.row(1) 
            row.label("Resolution:") 

            sub0 = row.column(1)
            sub0.scale_x = 1
            sub0.prop(self, "bico_div") 

            if self.sphere_dim == True:
                pass
            else:            

                box.separator()  

                row = box.row(1) 
                row.label("Dimension:") 

                sub0 = row.column(1)
                sub0.prop(self, "bico_siz")

        box.separator()



        box = layout.box().column(1)      
        
        row = box.row(1) 
        row.label("Copy Rotation:") 
        row.prop(self, "sphere_rota", text="") 
        
        if self.tp_geom_sphere == "tp_add_sph":

            if self.sphere_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "bsph_rota_x")             
                row.prop(self, "bsph_rota_y")             
                row.prop(self, "bsph_rota_z")    
 
        else:

            if self.sphere_rota == True:
                pass
            else:
                row = box.row(1)             
                row.prop(self, "bico_rota_x")             
                row.prop(self, "bico_rota_y")             
                row.prop(self, "bico_rota_z")   

        box.separator()



        box = layout.box().column(1)   
        
        row = box.row(1)   
        row.prop(self, "sphere_origin", icon="BLANK1", text="")
        row.prop(self, "sphere_xray", icon="BLANK1")   
   
        if self.sphere_meshtype == "tp_00":

            row = box.row(1)        
            row.prop(self, "sphere_smooth", icon="BLANK1")
            row.prop(self, "sphere_edges", icon="BLANK1")                   

        box.separator()  

        box = layout.box().column(1)             

        row = box.row(1)         
        row.prop(self, "sph_mat", text ="")
        row.label(text="Color:")  
        if bpy.context.scene.render.engine == 'CYCLES':
            row.prop(self, "sph_cyclcolor", text ="")        
        else:
            row.prop(self, "sph_color", text ="")          

        box.separator()  
      
        row = box.row(1)
        row.label(text="Widget:")
        row.prop(self, "sph_get_local", expand = True, text="")        
       
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
                if self.tp_geom_sphere == "tp_add_sph":
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')                
                    add_sphere(self.bsph_seg, self.bsph_rig, self.bsph_siz, self.bsph_rota_x, self.bsph_rota_y, self.bsph_rota_z)           
                    bpy.context.object.name = obj.name + "_shaded_sphere"
                    bpy.context.object.data.name = obj.name + "_shaded_sphere"
                    
                    # add new object to dummy name list
                    new_object_name = obj.name + "_shaded_sphere"
                    dummy_list.append(new_object_name) 

                else:            
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')  
                    add_ico(self.bico_div, self.bico_siz, self.bico_rota_x, self.bico_rota_y, self.bico_rota_z)
                    bpy.context.object.name = obj.name + "_shaded_ico"
                    bpy.context.object.data.name = obj.name + "_shaded_ico"

                    # add new object to dummy name list
                    new_object_name = obj.name + "_shaded_ico"
                    dummy_list.append(new_object_name) 



                active = bpy.context.active_object             
                
                # add material with enabled object color
                for i in range(self.sph_mat):            
                    mat_name = [obj.name]
                    mat = bpy.data.materials.new(obj.name)

                    if len(active.data.materials):
                        active.data.materials[0] = mat
                    else:
                        active.data.materials.append(mat)

                    if bpy.context.scene.render.engine == 'CYCLES':
                        bpy.context.object.active_material.diffuse_color = (self.sph_cyclcolor)
                    else:
                        bpy.context.object.active_material.use_object_color = True
                        bpy.context.object.color = (self.sph_color)


                # copy data from to new object
                active.location = obj.location
                
                for i in range(self.sphere_dim):
                    active.dimensions = obj.dimensions

                    # apply scale                    
                    for i in range(self.sphere_dim_apply):
                        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

                for i in range(self.sphere_rota):
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
                if self.sphere_origin == "tp_o0":
                    pass
                
                if self.sphere_origin == "tp_o1":                                
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')                      
               
                if self.sphere_origin == "tp_o2":
                    bpy.ops.tp_ops.bbox_origin_minus_z()     
     
                if self.sphere_origin == "tp_o3":                                
                    bpy.ops.tp_ops.bbox_origin_plus_z()   
                            
                # display: xray
                for i in range(self.sphere_xray):
                    bpy.context.object.show_x_ray = True

                # display: draw all edges
                for i in range(self.sphere_edges):
                    bpy.ops.tp_ops.wire_on()
               
                # stay shaded
                if self.sphere_meshtype == "tp_00":
                    pass 
                                    
                # create shadeless
                if self.sphere_meshtype == "tp_01":
                    bpy.context.object.draw_type = 'WIRE'

                    # second rename 
                    if self.tp_geom_sphere == "tp_add_sph":          
                        bpy.context.object.name = obj.name + "_shadless_sphere"
                        bpy.context.object.data.name = obj.name + "_shadless_sphere"

                    if self.tp_geom_sphere == "tp_add_ico":              
                        bpy.context.object.name =  obj.name +"_shadless_ico"
                        bpy.context.object.data.name = obj.name + "_shadless_ico"                                
                    
                # display: smooth
                for i in range(self.sphere_smooth):
                    bpy.ops.object.shade_smooth()

                # create wired 
                if self.sphere_meshtype == "tp_02": 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.delete(type='ONLY_FACE')
                    bpy.ops.object.editmode_toggle()
          
                    # third rename 
                    if self.tp_geom_sphere == "tp_add_sph":          
                        bpy.context.object.name = obj.name + "_wire_sphere"
                        bpy.context.object.data.name = obj.name + "_wire_sphere"

                    if self.tp_geom_sphere == "tp_add_ico":              
                        bpy.context.object.name = obj.name + "_wire_ico"
                        bpy.context.object.data.name = obj.name + "_wire_ico"
                                    

        # set widget orientation
        if self.sph_get_local == "tp_w0":
            pass
        elif self.sph_get_local == "tp_w1":
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







