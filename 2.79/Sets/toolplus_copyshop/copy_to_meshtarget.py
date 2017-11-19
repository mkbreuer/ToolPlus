              #  ***** BEGIN GPL LICENSE BLOCK *****
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/
#  or write to the Free Software Foundation, Inc., 51 Franklin Street,
#  Fifth Floor, Boston, MA 02110-1301, USA.
#
#  ***** END GPL LICENSE BLOCK *****
"""
bl_info = {
    "name": "Copy2 vertices, edges or faces",
    "author": "Eleanor Howick (elfnor.com)",
    "version": (0, 1),
    "blender": (2,71,0),
    "location": "3D View > Object > Copy 2",
    "description": "Copy one object to the selected vertices, edges or faces of another object",
    "warning": ""
    "category": "Object",
}
"""


# LOAD CACHE #
from .caches.cache      import  (tot_settings_load)
from .caches.cache      import  (tot_settings_write)


# LOAD MODULE #

import bpy
from bpy import*
from bpy.props import *
from mathutils import Vector, Matrix


# OPERATOR #

obj_list = None

def obj_list_cb(self, context):
    VIEWD3D_Copy_To_MeshTarget.obj_list = [(obj.name, obj.name, obj.name) for obj in bpy.data.objects]   
    return VIEWD3D_Copy_To_MeshTarget.obj_list
        
def sec_axes_list_cb(self, context):
    if self.priaxes == 'X':
        sec_list = [('Y','Y','Y'), ('Z', 'Z', 'Z')]
     
    if self.priaxes == 'Y':
        sec_list = [('X','X','X'), ('Z', 'Z', 'Z')]
        
    if self.priaxes == 'Z':
        sec_list = [('X','X','X'), ('Y', 'Y', 'Y')]     
    return sec_list


class VIEWD3D_Copy_To_MeshTarget(bpy.types.Operator):
    bl_idname = "tp_ops.copy_to_meshtarget"
    bl_label = "Copy to Mesh Target"
    bl_options = {"REGISTER", "UNDO"}
    
#    obj_list = None
#  
#    def obj_list_cb(self, context):
#        return VIEWD3D_Copy_To_MeshTarget.obj_list
#            
#    def sec_axes_list_cb(self, context):
#        if self.priaxes == 'X':
#            sec_list = [('Y','Y','Y'), ('Z', 'Z', 'Z')]
#         
#        if self.priaxes == 'Y':
#            sec_list = [('X','X','X'), ('Z', 'Z', 'Z')]
#            
#        if self.priaxes == 'Z':
#            sec_list = [('X','X','X'), ('Y', 'Y', 'Y')]     
#        return sec_list
    

    copytype = bpy.props.EnumProperty(items=(('V','','paste to vertices','VERTEXSEL',0),
                                             ('E','','paste to edges','EDGESEL',1),
                                             ('F','','paste to faces','FACESEL',2)),
                                      description='where to paste to')
                                                    
    copyfromobject = bpy.props.EnumProperty(items=obj_list_cb, name='Copy from:')
                                                                                      
    priaxes = bpy.props.EnumProperty(items=(('X', 'X', 'along X'),
                                            ('Y', 'Y', 'along Y'),
                                            ('Z', 'Z', 'along Z')),
                                            )
                                             
    edgescale = bpy.props.BoolProperty(name='Scale to fill edge?')
                                                
    secaxes = bpy.props.EnumProperty(items=sec_axes_list_cb, name='Secondary Axis')
    
    scale = bpy.props.FloatProperty(default=1.0, min=0.0, name='Scale')

           
    set_plus_z = bpy.props.BoolProperty(name="Top",  description="set origin to top", default = False)       
    set_center_z = bpy.props.BoolProperty(name="Center",  description="set origin to center", default = False)   
    set_minus_z = bpy.props.BoolProperty(name="Bottom",  description="set origin to bottom", default = False)       

    join = bpy.props.BoolProperty(name="Join Copies",  description="join copies with source", default = False)       
    dupli_unlinked = bpy.props.BoolProperty(name="Unlink Copies",  description="unlink copies", default = False)      

    set_edit_target = bpy.props.BoolProperty(name="Edit Target",  description="jump to target editmode", default = False)   
    set_edit_source = bpy.props.BoolProperty(name="Edit Source",  description="jump to source editmode", default = False)   


    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        box = layout.box().column(1)
            
        row = box.row(1)            
        row.label("Source:")                    
        row.prop(self, "copyfromobject", text="")  
        
        box.separator() 
        
        row = box.row(1)            
        row.label("Target:") 
 
        sub = row.row(1)
        sub.scale_x = 1.55               
        sub.prop(self, 'copytype', expand=True)
        
        box.separator() 
        
        row = box.row(1)                
        row.label("1st Axis:") 
        row.prop(self, 'priaxes', expand=True)
        
        box.separator() 
                   
        row = box.row(1)                
        row.label("2nd Axis:") 
        row.prop(self, 'secaxes', expand=True)
  
        box.separator()     
  
        row = box.row(1)                 
        if self.copytype == 'E':
            row.prop(self, 'edgescale')
            
            if self.edgescale:
               row = box.row(1) 
               row.prop(self, 'scale')             


        if len(bpy.context.selected_objects) == 1:   
            box = layout.box().column(1)

            row = box.row(1)  
            row.label("! more options: select a source & a target mesh !", icon ="INFO")              

        else:

            obj = context.active_object
            if obj:
                if obj.type in {'MESH'}:        
                    box = layout.box().column(1)
                                                     
                    row = box.row(1)        
                    row.label("Relations:")              
                    row.prop(self, 'dupli_unlinked', text="Unlinked") 
                    row.prop(self, 'join', text="Join")   
                    
                    row = box.row(1)        
                    row.label("Editmode:")                   
                    row.prop(self, 'set_edit_source', text="Source")
                    row.prop(self, 'set_edit_target', text="Target")
                     
                    box.separator()   

                    row = box.row(1)        
                    row.label("Origin:")                 
                    row.prop(self, 'set_plus_z', text="Top")                 
                    row.prop(self, 'set_center_z', text="Center")                 
                    row.prop(self, 'set_minus_z', text="Bottom")   

                    box.separator()   
                       
            else:
                pass

        return

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):               
        tot_settings_load(self)
        return self.execute(context)
        

    def execute(self, context):

        tot_settings_write(self)
        

        obj = context.active_object
   
        if len(bpy.context.selected_objects) == 2:
           
            bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'

            bpy.ops.object.mode_set(mode='OBJECT')

            if obj:
                if obj.type in {'MESH'}:

                    first_obj = bpy.context.active_object

                    obj_a, obj_b = context.selected_objects

                    second_obj = obj_a if obj_b == first_obj else obj_b  
                        
                    ### origin to top
                    for i in range(self.set_plus_z):
                        
                        # active: second
                        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                        bpy.data.objects[second_obj.name].select=True                
                        
                        bpy.ops.tp_ops.origin_plus_z()  
                       
                        # active: first                
                        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name] 
                        bpy.data.objects[first_obj.name].select = True         
                

                    ### origin to center
                    for i in range(self.set_center_z):
                        
                        # active: second
                        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                        bpy.data.objects[second_obj.name].select=True                

                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY') 
                       
                        # active: first                    
                        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name] 
                        bpy.data.objects[first_obj.name].select = True 


                    ### origin to bottom
                    for i in range(self.set_minus_z):
                        
                        # active: second
                        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                        bpy.data.objects[second_obj.name].select=True                

                        bpy.ops.tp_ops.origin_minus_z()  
                       
                        # active: first                    
                        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name] 
                        bpy.data.objects[first_obj.name].select = True 


                    # active: first   
                    bpy.data.objects[second_obj.name].select=False                

                    if context.mode == 'EDIT_MESH': 

                        print(self)
                        self.report({'INFO'}, "! need source & target !")  
                


                    copytoobject = context.active_object.name
                    axes = self.priaxes + self.secaxes
                    copy_list = copy_to_from(context.scene, 
                                             bpy.data.objects[copytoobject],
                                             bpy.data.objects[self.copyfromobject],
                                             self.copytype, 
                                             axes,
                                             self.edgescale,
                                             self.scale)



                    for i in range(self.join):                    
                        # active: first
                        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]
                        bpy.data.objects[first_obj.name].select=True    
                        
                        bpy.ops.object.join()
                        
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.mesh.normals_make_consistent()
                        bpy.ops.object.editmode_toggle()


                    for i in range(self.dupli_unlinked):                                     

                        # active: second
                        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]                
                        bpy.data.objects[second_obj.name].select=True 
                        
                        bpy.ops.object.select_linked(type='OBDATA')
                        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)



                    for i in range(self.set_edit_source):
                        
                        # active: second
                        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]                
                        bpy.data.objects[second_obj.name].select=True
                                            
                        bpy.ops.object.mode_set(mode='EDIT')   

                    for i in range(self.set_edit_target):

                        # active: first
                        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]
                        bpy.data.objects[first_obj.name].select=True                    
                        
                        bpy.ops.object.mode_set(mode='EDIT')        
                        
                        print(self)
                        self.report({'INFO'}, "Editmode")      





                else:
                    print(self)
                    self.report({'INFO'}, "! need source & target !")    
    

        else:
            
            copytoobject = context.active_object.name
            axes = self.priaxes + self.secaxes
            copy_list = copy_to_from(context.scene, 
                                     bpy.data.objects[copytoobject],
                                     bpy.data.objects[self.copyfromobject],
                                     self.copytype, 
                                     axes,
                                     self.edgescale,
                                     self.scale)

        return {"FINISHED"}

    
    def invoke(self, context, event):
        VIEWD3D_Copy_To_MeshTarget.obj_list = [(obj.name, obj.name, obj.name) for obj in bpy.data.objects]
        return context.window_manager.invoke_props_popup(self, event)    
    







# FUNCTIONS #

def copy_to_from(scene, to_obj, from_obj, copymode, axes, edgescale, scale):
    if copymode == 'V':
        copy_list = vertex_copy(scene, to_obj, from_obj, axes)
    if copymode == 'E':
        copy_list = edge_copy(scene, to_obj, from_obj, axes, edgescale, scale)
    if copymode == 'F':
        copy_list = face_copy(scene, to_obj, from_obj,axes)
    return copy_list
  
axes_dict = {'XY': (1,2,0), 
             'XZ': (2,1,0),
             'YX': (0,2,1),
             'YZ': (2,0,1),
             'ZX': (0,1,2),
             'ZY': (1,0,2)}  
    
def copyto(scene, source_obj, pos, xdir, zdir, axes, scale=None):  
     """ 
     copy the source_obj to pos, so its primary axis points in zdir and its 
     secondary axis points in xdir       
     """  
     copy_obj = source_obj.copy()
     scene.objects.link(copy_obj)     
       
     xdir = xdir.normalized()  
     zdir = zdir.normalized()  
     #rotation first  
     z_axis = zdir  
     x_axis = xdir      
     y_axis = z_axis.cross(x_axis)  
     #use axes_dict to assign the axis as chosen in panel 
     A, B, C = axes_dict[axes]
     rot_mat = Matrix()  
     rot_mat[A].xyz = x_axis  
     rot_mat[B].xyz = y_axis  
     rot_mat[C].xyz = z_axis  
     rot_mat.transpose()  
     
     #rotate object 
     copy_obj.matrix_world = rot_mat   
            
     #move object into position    
     copy_obj.location = pos  
     
     #scale object
     if  scale != None:
         copy_obj.scale = scale
     
     return copy_obj  
      
def vertex_copy(scene, obj, source_obj, axes):    
    #vertex select mode  
    sel_verts = [] 
    copy_list = []
    for v in obj.data.vertices:  
        if v.select == True:  
            sel_verts.append(v)  
  
    #make a set for each vertex. The set contains all the connected vertices  
    #use sets so the list is unique  
    vert_con = [set() for i in range(len(obj.data.vertices))]  
    for e in obj.data.edges:  
        vert_con[e.vertices[0]].add(e.vertices[1])  
        vert_con[e.vertices[1]].add(e.vertices[0])  
      
    for v in sel_verts:  
        pos = v.co * obj.matrix_world.transposed()  
        xco = obj.data.vertices[list(vert_con[v.index])[0]].co * obj.matrix_world.transposed()  
         
        zdir = (v.co + v.normal) * obj.matrix_world.transposed() - pos  
        zdir = zdir.normalized()  
          
        edir = pos - xco  
          
        #edir is nor perpendicular to z dir  
        #want xdir to be projection of edir onto plane through pos with direction zdir  
        xdir = edir - edir.dot(zdir) * zdir  
        xdir = -xdir.normalized()  
          
        copy = copyto(scene, source_obj, pos, xdir, zdir, axes)  
        copy_list.append(copy)  
    #select all copied objects  
    for copy in copy_list:  
        copy.select = True 
    obj.select = False    
    return copy_list

  
def edge_copy(scene, obj, source_obj, axes, es, scale): 
    #edge select mode  
    sel_edges = []
    copy_list = []
    for e in obj.data.edges:  
        if e.select == True:  
            sel_edges.append(e)  
    for e in sel_edges:  
        #pos is average of two edge vertexs  
        v0 = obj.data.vertices[e.vertices[0]].co * obj.matrix_world.transposed()  
        v1 = obj.data.vertices[e.vertices[1]].co * obj.matrix_world.transposed()  
        pos = (v0 + v1)/2  
        #xdir is along edge  
        xdir = v0-v1  
        xlen = xdir.magnitude
        xdir = xdir.normalized()  
        #project each edge vertex normal onto plane normal to xdir  
        vn0 = (obj.data.vertices[e.vertices[0]].co * obj.matrix_world.transposed()   
              + obj.data.vertices[e.vertices[0]].normal) - v0  
        vn1 = (obj.data.vertices[e.vertices[1]].co  * obj.matrix_world.transposed()  
              + obj.data.vertices[e.vertices[1]].normal) - v1  
        vn0p = vn0 - vn0.dot(xdir)*xdir  
        vn1p = vn1 - vn1.dot(xdir)*xdir  
        #the mean of the two projected normals is the zdir  
        zdir = vn0p + vn1p  
        zdir = zdir.normalized()  
        escale = None
        if es:
            escale = Vector([1.0, 1.0, 1.0])
            i = list('XYZ').index(axes[1])
            escale[i] = scale*xlen/source_obj.dimensions[i] 
      
        copy = copyto(scene, source_obj, pos, xdir, zdir, axes, scale=escale)  
        copy_list.append(copy)  
    #select all copied objects  
    for copy in copy_list:  
        copy.select = True  
    obj.select = False 
    return copy_list
  



def face_copy(scene, obj, source_obj, axes):  

    #face select mode  
    sel_faces = []
    copy_list = []

    for f in obj.data.polygons:  
        if f.select == True:  
            sel_faces.append(f)  

    for f in sel_faces:                     
          fco = f.center * obj.matrix_world.transposed()    

          #get first vertex corner of transformed object    
          vco = obj.data.vertices[f.vertices[0]].co * obj.matrix_world.transposed()    

          #get face normal of transformed object    
          fn = (f.center + f.normal) * obj.matrix_world.transposed()  - fco    
          fn = fn.normalized()    
        
          copy = copyto(scene, source_obj, fco, vco - fco, fn, axes)    
          copy_list.append(copy)   

    #select all copied objects  
    for copy in copy_list:  
        copy.select = True  
    obj.select = False     

    return copy_list
        





# PROPERTY GROUP: COPY TO TARGET #
class ToTarget_Properties(bpy.types.PropertyGroup):
    

    copytype = bpy.props.EnumProperty(items=(('V','','paste to vertices','VERTEXSEL',0),
                                             ('E','','paste to edges','EDGESEL',1),
                                             ('F','','paste to faces','FACESEL',2)),
                                      description='where to paste to')
                                                    
    copyfromobject = bpy.props.EnumProperty(items=obj_list_cb, name='Copy from:')
                                                                                      
    priaxes = bpy.props.EnumProperty(items=(('X', 'X', 'along X'),
                                            ('Y', 'Y', 'along Y'),
                                            ('Z', 'Z', 'along Z')),
                                            )
                                             
    edgescale = bpy.props.BoolProperty(name='Scale to fill edge?')
                                                
    secaxes = bpy.props.EnumProperty(items=sec_axes_list_cb, name='Secondary Axis')
    
    scale = bpy.props.FloatProperty(default=1.0, min=0.0, name='Scale')

           
    set_plus_z = bpy.props.BoolProperty(name="Top",  description="set origin to top", default = False)       
    set_center_z = bpy.props.BoolProperty(name="Center",  description="set origin to center", default = False)   
    set_minus_z = bpy.props.BoolProperty(name="Bottom",  description="set origin to bottom", default = False)       

    join = bpy.props.BoolProperty(name="Join Copies",  description="join copies with source", default = False)       
    dupli_unlinked = bpy.props.BoolProperty(name="Unlink Copies",  description="unlink copies", default = False)      

    set_edit_target = bpy.props.BoolProperty(name="Edit Target",  description="jump to target editmode", default = False)   
    set_edit_source = bpy.props.BoolProperty(name="Edit Source",  description="jump to source editmode", default = False) 



# REGISTRY #

def register():
    bpy.utils.register_module(__name__)

    # PROPS COPY TO TARGET # 
    bpy.types.WindowManager.totarget_props = PointerProperty(type = ToTarget_Properties)

def unregister():
    bpy.utils.unregister_module(__name__)

    # PROPS COPY TO TARGET # 
    del bpy.types.WindowManager.totarget_props 

if __name__ == "__main__":
    register()
        
        
