# !!! NOT IN USE !!! #
# ALTERNATIV: BOUNDING BOX GEOMETRY WITH COPIED LOCAL ORIENTATION ON ONE TARGET #

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

def Rotate(myMesh, mat):
    for v in myMesh.vertices:
        vec = mat * v.co
        v.co = vec

class VIEW3D_TP_BBox_Source(bpy.types.Operator):
    """Make bound boxes for selected objects"""      
    bl_idname = "tp_ops.bounding_box_source"
    bl_label = "Bounding Box"
    bl_options = {'REGISTER', 'UNDO'}

    geom = bpy.props.EnumProperty(
        items=[("tp_bb1"    ,"Plane"   ,"add single plane (ngone)"  ),
               ("tp_bb2"    ,"Cube"     ,"add a cube"               )],
               name = "",
               default = "tp_bb1",    
               description = "choose geometry for bounding")
               
    scale = FloatVectorProperty(name="Scale",  default=(1.0, 1.0, 1.0), subtype='TRANSLATION', description="scaling")

    # build bound geometry
    def build(self, i, obj):
        box = bpy.context.selected_objects[i].bound_box
        ob_old = bpy.context.selected_objects[i].matrix_world
        
        name = ('_bbox_source') # object name
        mesh = bpy.data.meshes.new(name) # data name 
        
        # object name: copy source name and add suffix
        #name = (bpy.context.selected_objects[i].name + '_BBox')    

        # data name
        mesh = bpy.data.meshes.new(name) 

        # create new object associated with the mesh
        ob_new = bpy.data.objects.new(name, mesh)
        
        # copy data from old to new object
        ob_new.location = ob_old.translation
        ob_new.scale = ob_old.to_scale()
        ob_new.rotation_euler = ob_old.to_euler()
        #ob_new.show_name = False
       
        # link to scene and select new object        
        bpy.context.scene.objects.link(ob_new)
       
        # scale props
        scale_x = self.scale.x
        scale_y = self.scale.y
        scale_z = self.scale.z

        # add geometry: plane
        if self.geom == "tp_bb1":

            verts = [Vector((+1 * scale_x, -1 * scale_y, 0)),
                     Vector((-1 * scale_x, -1 * scale_y, 0)),
                     Vector((-1 * scale_x, +1 * scale_y, 0)),
                     Vector((+1 * scale_x, +1 * scale_y, 0)),
                    ]
            edges = []
            faces = [[3, 2, 1, 0]]

            mesh.from_pydata(verts, edges, faces)
            mesh.update(calc_edges=True)


        # add geometry: cube
        else:# self.geom == "tp_bb2":
           
            verts = [Vector((+1 * scale_x, +1 * scale_y, -1 * scale_z)),
                     Vector((+1 * scale_x, -1 * scale_y, -1 * scale_z)),
                     Vector((-1 * scale_x, -1 * scale_y, -1 * scale_z)),
                     Vector((-1 * scale_x, +1 * scale_y, -1 * scale_z)),
                     
                     Vector((+1 * scale_x, +1 * scale_y, +1 * scale_z)),
                     Vector((+1 * scale_x, -1 * scale_y, +1 * scale_z)),
                     Vector((-1 * scale_x, -1 * scale_y, +1 * scale_z)),
                     Vector((-1 * scale_x, +1 * scale_y, +1 * scale_z)),
                     ]

            edges = []

            faces = [(0, 1, 2, 3),
                     (4, 7, 6, 5),
                     (0, 4, 5, 1),
                     (1, 5, 6, 2),
                     (2, 6, 7, 3),
                     (4, 0, 3, 7),
                    ]

            mesh.from_pydata(verts, edges, faces)
            mesh.update(calc_edges=True)

        # make it active
        bpy.context.scene.objects.active = ob_new
        
        # store current mode
        current_mode = bpy.context.mode        
        bpy.ops.object.mode_set(mode='EDIT')
       
        # recalulate normals
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent()            

        # reload previous mode
        bpy.ops.object.mode_set(mode=current_mode)      
        
        return ob_new

    # run operator
    def execute(self, context):
        active = bpy.context.active_object
        selected = bpy.context.selected_objects
        
        mat_active = active.rotation_euler.to_matrix()
        mat_active.invert()

        i = 0
        for ob in selected:
            self.build(i, ob)
            i += 1                 

            # copy local orientation
            mat_ob = ob.rotation_euler.to_matrix()
            mat = mat_active * mat_ob
            Rotate(ob.data, mat)
            active.rotation_euler = ob.rotation_euler



        return {'FINISHED'}




# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()
















