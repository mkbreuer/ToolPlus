# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you may redistribute it, and/or
# modify it, under the terms of the GNU General Public License
# as published by the Free Software Foundation - either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, write to:
#
#   the Free Software Foundation Inc.
#   51 Franklin Street, Fifth Floor
#   Boston, MA 02110-1301, USA
#
# or go online at: http://www.gnu.org/licenses/ to view license options.
#
# ***** END GPL LICENCE BLOCK *****


#bl_info = {
#    "name": "Tube Tool",
#    "author": "Dealga McArdle",
#    "version": (0, 0, 4),
#    "blender": (2, 7, 4),
#    "location": "specials menu (key W)",
#    "description": "Adds curve with endpoints on two arbitrary polygons",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Mesh"}

# expanded: MKB

import bpy
import bmesh
import random
from mathutils import Vector

from bpy.props import *
name_list = []
new_object_list = []

class TubeCallbackOps(bpy.types.Operator):

    bl_idname = "object.tube_callback"
    bl_label = "Tube Callback"
    bl_options = {"INTERNAL"}

    current_name = StringProperty(default='')
    fn = StringProperty(default='')
    default = FloatProperty()

    def dispatch(self, context, type_op):
        wm = context.window_manager
        operators = wm.operators

        # only do this part if also current_name is passed in
        if self.current_name:

            cls = None
            for k in operators:
                if k.bl_idname == 'tp_ops.2facetube':
                    if k.generated_name == self.current_name:
                        cls = k

            if not cls:
                ''' all callback functions require a valid class reference '''
                return

            if type_op == "Reset radii":
                print('attempt reset:', cls.generated_name)
                cls.main_scale = 1.0
                cls.point1_scale = 1.0
                cls.point2_scale = 1.0

            elif type_op == "To Mesh":
                cls.make_real()

            elif type_op == 'Join':

                # # gets current name, but could be stored earlier..
                # base_obj = bpy.context.edit_object
                # base_obj_name = base_obj.name

                # new_obj = cls.make_real()
                # print(' made', new_obj.name)

                # # let's use ops to add verts+faces to base_obj
                # bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                # bpy.ops.object.select_all(action='DESELECT')

                # new_obj.select = True
                # print('base obj name', base_obj_name)
                # base_obj = bpy.data.objects[base_obj_name]
                # base_obj.select = True
                # bpy.context.scene.objects.active = base_obj

                # # join and return back to edit mode.
                # # bpy.ops.object.join()
                # # bpy.ops.object.mode_set(mode='EDIT')

                # # don't overwrite with existing mesh.
                # cls.joined = True
                ...

            else:
                # would prefer to be implicit.. but self.default is OK for now.
                # ideally, the value is derived from the prop default
                # of cls.type_op. but for now it is passed explicitely.
                # Barf. Dryheave.
                setattr(cls, type_op, self.default)
                cls.execute(context)

    def execute(self, context):
        self.dispatch(context, self.fn)
        return {'FINISHED'}


def median(face):
    med = Vector()
    for vert in face.verts:
        vec = vert.co
        med = med + vec
    return med / len(face.verts)


def update_simple_tube(oper, context):

    generated_name = oper.generated_name

    obj_main = bpy.context.edit_object

    if not obj_main:
        return

    mw = obj_main.matrix_world
    me = obj_main.data
    bm = bmesh.from_edit_mesh(me)

    # get active face indices
    medians = []
    normals = []

    if not oper.flip_u:
        faces = [f for f in bm.faces if f.select]
    else:
        faces = list(reversed([f for f in bm.faces if f.select]))

    for f in faces:
        if len(medians) > 2:
            # dont select more than 2 faces.
            break
        normals.append(f.normal)
        medians.append(median(f))

    # This will automatically scale the bezierpoint radii as a
    # function of the size of the polygons
    bevel_depth = (medians[0] - (faces[0].verts[0].co)).length
    scale2 = (medians[1] - (faces[1].verts[0].co)).length
    op2_scale = scale2 / bevel_depth


    def modify_curve(medians, normals, curvename):
        print('this happens')
        obj = bpy.data.objects[generated_name]
        curvedata = obj.data
        polyline = curvedata.splines[0]

        polyline.use_smooth = oper.show_smooth
        obj.data.fill_mode = oper.fill_mode
        obj.data.bevel_depth = bevel_depth
        obj.data.bevel_resolution = oper.subdiv
        obj.show_wire = oper.show_wire
        obj.data.extrude = oper.extrude
        obj.data.offset = oper.offset
        pointA, pointB = [0, -1] if not oper.flip_v else [-1, 0]

        ''' the radii stuff must be tidier before merge to master. '''

        # Point 0
        ''' default scale or radius point1 == 1 '''
        point1 = polyline.bezier_points[pointA]
        co = medians[0]
        if oper.equal_radii:
            point1.radius = 1 * oper.main_scale
        else:
            point1.radius = 1 * oper.main_scale * oper.point1_scale

        point1.co = co
        point1.handle_left = (co - (normals[0] * oper.handle_ext_1))
        point1.handle_right = (co + (normals[0] * oper.handle_ext_1))

        # Point 1
        point2 = polyline.bezier_points[pointB]
        if oper.equal_radii:
            point2.radius = 1 * oper.main_scale
        else:
            point2.radius = 1 * op2_scale * oper.main_scale * oper.point2_scale

        co = medians[1]
        point2.co = co
        point2.handle_right = (co - (normals[1] * oper.handle_ext_2))
        point2.handle_left = (co + (normals[1] * oper.handle_ext_2))

        polyline.resolution_u = oper.tube_resolution_u

    print('generated name:', generated_name)
    modify_curve(medians, normals, generated_name)


    # add material with enabled object color
    for i in range(oper.add_mat):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        bpy.ops.object.select_pattern(pattern=generated_name)

        first_obj = bpy.context.active_object
        obj_a, obj_b = context.selected_objects
        second_obj = obj_a if obj_b == first_obj else obj_b  
            
        # active: second                          
        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
        bpy.data.objects[second_obj.name].select=True     

        active = bpy.context.active_object
        # Get material
        mat = bpy.data.materials.get("Mat_FaceTube")
        if mat is None:
            # create material
            mat = bpy.data.materials.new(name="Mat_FaceTube")
        else:
            bpy.ops.object.material_slot_remove()
            mat = bpy.data.materials.new(name="Mat_FaceTube")
                 
        # Assign it to object
        if len(active.data.materials):
            # assign to 1st material slot
            active.data.materials[0] = mat
        else:
            # no slots
            active.data.materials.append(mat)
                
        # toggle random
        if oper.add_random == False:            
                            
            # toggle color target
            if oper.add_objmat == False: 
                
                # object color
                if bpy.context.scene.render.engine == 'CYCLES':
                    mat.diffuse_color = (oper.add_cyclcolor)                        
                else:
                    mat.use_object_color = True
                    bpy.context.object.color = (oper.add_color)
            else:                                      
                # regular material
                pass                       
        else:                 
            # toggle color target
            if oper.add_objmat == False:   
                
                # object color
                if bpy.context.scene.render.engine == 'CYCLES':
                    for i in range(3):
                        RGB = (random.random(),random.random(),random.random(),1)
                        mat.diffuse_color = RGB                       
                else:
                    mat.use_object_color = True
                    for i in range(3):
                        RGB = (random.random(),random.random(),random.random(),1)
                        bpy.context.object.color = RGB
           
            else:        
                # regular material    
                if bpy.context.scene.render.engine == 'CYCLES':
                    node=mat.node_tree.nodes['Diffuse BSDF']
                    for i in range(3):
                        node.inputs['Color'].default_value[i] *= random.random()             
                else:
                    for i in range(3):
                        mat.diffuse_color[i] *= random.random()   
  
        
        bpy.ops.object.select_all(action='DESELECT')
           
        # active: first                
        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name] 
        bpy.data.objects[first_obj.name].select = True

        bpy.ops.object.editmode_toggle()


class VIEW_3D_TP_Add_2_Face_Tube(bpy.types.Operator):
    """Add curve between to selected faces"""
    bl_idname = "tp_ops.2facetube"
    bl_label = "Face Tube"
    bl_options = {'REGISTER', 'UNDO'}

    base_name = StringProperty(default='TT_tube')
    generated_name = StringProperty(default='')

    subdiv = IntProperty(
        name="Profile Subdivision",
        description="subdivision level for the profile (circumference)",
        default=4, min=0, max=16)

    tube_resolution_u = IntProperty(
        min=0, default=12, max=30,
        description="subdivision level for the length of the initial curve")

    handle_ext_1 = FloatProperty(min=-200.0, default=20.0, max=200.0)
    handle_ext_2 = FloatProperty(min=-200.0, default=20.0, max=200.0)

    show_smooth = BoolProperty(default=False)
    show_wire = BoolProperty(default=False)
    keep_operator_alive = BoolProperty(default=True)

    main_scale = FloatProperty(min=0.0001, default=1.0, max=50.0)
    point1_scale = FloatProperty(min=0.0001, default=1.0, max=50.0)
    point2_scale = FloatProperty(min=0.0001, default=1.0, max=50.0)

    flip_v = BoolProperty()
    flip_u = BoolProperty()

    equal_radii = BoolProperty(default=0)
    # joined = BoolProperty(default=0)

    do_not_process = BoolProperty(default=False)

    fill_mode = EnumProperty(name = "Fill Type",
            items=(('FULL',  "Full",  ""),                                                    
                   ('BACK',  "Back",  ""),                   
                   ('FRONT', "Front", ""),                   
                   ('HALF',  "Half",  "")),                   
                   default='FULL',
                   description="change fill type of spline")   
    
    offset = bpy.props.FloatProperty(name="Offset",  description=" ", default=0, min=0.00, max=1000)
    extrude = bpy.props.FloatProperty(name="Height",  description=" ", default=0, min=0.00, max=1000)

    # MATERIAL #
    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)        
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random material", default=False, options={'SKIP_SAVE'})    
    add_objmat = bpy.props.BoolProperty(name="Add Material",  description="add material", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    def draw(self, context):
        layout = self.layout
        callback = "object.tube_callback"
        col = layout.column(align=True)

        box = col.box().column(1)  
       
        row = box.row(1) 
        row.prop(self, "subdiv", text="Loop")
        row.prop(self, "tube_resolution_u", text="Ring")

        row = box.row(1) 
        row.prop(self, "offset", text="Offset")          
        row.prop(self, "extrude", text="Height")
       
        box.separator()
       
        row = box.row() 
        row.prop(self, "equal_radii", text="equal radii")
        row.prop(self, "main_scale", text="Radius")

        box.separator()

        def prop_n_reset(split, pname, pstr, default, enabled=True):
            ''' I draw a slider and an operator to reset the slider '''
            pid = split.row(align=True)
            pid.enabled = enabled
            pid.prop(self, pname, text=pstr)
            a = pid.operator(callback, text="", icon="LINK")
            a.fn = pname
            a.current_name = self.generated_name
            a.default = default

        er = not self.equal_radii
        # ROW 1
        row = box.row(); split = row.split(percentage=0.5)
        prop_n_reset(split, "handle_ext_1", "handle 1", 2.0)  # left
        prop_n_reset(split, "point1_scale", "radius_1", 1.0, er)  # right

        # ROW 2
        row = box.row(); split = row.split()
        prop_n_reset(split, "handle_ext_2", "handle 2", 2.0)  # left
        prop_n_reset(split, "point2_scale", "radius_2", 1.0, er)  # right

        # next row
        row = box.row()
        split = row.split(percentage=0.5)
        col_left = split.column()

        col_left.label("display")
        left_row = col_left.row()
        left_row.prop(self, "show_smooth", text="smooth", toggle=True)
        left_row.prop(self, "show_wire", text="wire", toggle=True)

        col_right = split.column()
        col_right.label("flip over")
        right_row = col_right.row()
        right_row.prop(self, "flip_u", text='Direction', toggle=True)
        right_row.prop(self, "flip_v", text='Normal', toggle=True)

        box.separator()
       
        row = box.row() 
        row.prop(self, "fill_mode", text="") 
        
#        k = col.operator(callback, text="Reset radii")
#        k.fn = "Reset radii"
#        k.current_name = self.generated_name

#        k = col.operator(callback, text="To Mesh")
#        k.fn = 'To Mesh'
#        k.current_name = self.generated_name

#         k = col.operator(callback, text="Join")
#         k.fn = 'Join'
#         k.current_name = self.generated_name

        box.separator()  
             
        row = box.row(1) 
        row.prop(self, "add_mat", text ="")                    
        row.label(text="Color:") 
     
        #row.prop(self, "add_objmat", text ="", icon="GROUP_VCOL")
        if self.add_random == False:                   
            if self.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(self, "add_cyclcolor", text ="")        
                else:
                    row.prop(self, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")  
        else:            
            if self.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(self, "add_cyclcolor", text ="")        
                else:
                    row.prop(self, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")              

        row.prop(self, "add_random", text ="", icon="FILE_REFRESH")
       
        box.separator()


    def __init__(self):

        '''
        - create curve
        - assign default values
        - add to scene
        - record given name
        '''


        scn = bpy.context.scene
        obj_main = bpy.context.edit_object

        if not (obj_main.data.total_face_sel == 2):
            self.do_not_process = True
            self.report({'WARNING'}, 'select two faces only')
            return

        mw = obj_main.matrix_world

        curvedata = bpy.data.curves.new(name=self.base_name, type='CURVE')     
        new_object_list.append(self.base_name)        

        curvedata.dimensions = '3D'

        obj = bpy.data.objects.new('Obj_' + curvedata.name, curvedata)
        obj.location = (0, 0, 0)  # object origin
        bpy.context.scene.objects.link(obj)
        self.generated_name = obj.name

        obj.matrix_world = mw.copy()

        polyline = curvedata.splines.new('BEZIER')
        polyline.bezier_points.add(1)
        polyline.use_smooth = False
        obj.data.fill_mode = self.fill_mode        
        obj.data.extrude = self.extrude
        obj.data.offset = self.offset

        update_simple_tube(self, bpy.context)
        

    def __del__(self):
        print("End")

    @classmethod
    def poll(self, context):
        return self.do_not_process

    def make_real(self):
        objects = bpy.data.objects
        obj = objects[self.generated_name]  # this curve object

        scene = bpy.context.scene
        settings = 'PREVIEW'
        modifiers = True
        obj_data = obj.to_mesh(scene, modifiers, settings)

        obj_n = objects.new('MESHED_' + obj.name, obj_data)
        obj_n.location = (0, 0, 0)
        obj_n.matrix_world = obj.matrix_world.copy()
        bpy.context.scene.objects.link(obj_n)
        obj.hide_render = True
        obj.hide = True
        # return obj_n

    def execute(self, context):
        if self.do_not_process:
            return {'CANCELLED'}
        else: 
            selected = bpy.context.selected_objects
            for obj in selected:
                name_list.append(obj.name)                 
                update_simple_tube(self, context)  

            del name_list[:]
            del new_object_list[:]   
            return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()