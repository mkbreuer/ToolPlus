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

#    based on Bevel Curve Tools from Yusuf Umar
#    MKB Version 1



# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

from bpy_extras.object_utils import AddObjectHelper, object_data_add

import math
from mathutils import Vector, Quaternion

from toolplus_resurface.ops_curve.add_taper_bevel import *


EDIT = ["EDIT_CURVE", "EDIT_SURFACE"]


def radius_falloff(points, power = 1.0, tip = 'ONE'):
    total_points = len(points)
    for i, point in enumerate(points):
        dist = i/(total_points-1)
        if tip == 'ONE':
            radius_weight = 1.0 - pow(dist, power)
        elif tip == 'DUAL':
            if dist >= 0.5:
                dist = (dist - 0.5) * 2.0
                radius_weight = 1.0 - pow(dist, power)
            else:
                dist = dist * 2.0
                radius_weight = pow(dist, 1/power)
        elif tip == 'NO':
            radius_weight = 1.0
        #print(dist, radius_weight)
        point.radius = radius_weight


def get_spline_points(spline):
    # Points for griffindor
    if spline.type == 'POLY':
        points = spline.points
    else:
        points = spline.bezier_points

    return points


def get_point_position(curve_obj, index=0, spline_index=0):
    curve_mat = curve_obj.matrix_world
    curve = curve_obj.data
    points = get_spline_points(curve.splines[spline_index])
    return curve_mat * points[index].co.xyz


def check_bevel_used_by_other_objects(scene, curve_obj):

    bevel_used = False

    for o in scene.objects:
        if (o.type == 'CURVE' and
            o != curve_obj and
            o.data.bevel_object == curve_obj.data.bevel_object):
            bevel_used = True

    return bevel_used



def get_point_rotation(scene, curve_obj, index=0, spline_index=0):

    # get curve attributes
    curve_mat = curve_obj.matrix_world
    curve = curve_obj.data
    points = get_spline_points(curve.splines[spline_index])

    # new temp object to detect local x-axis and y-axis of first handle
    # temp bevel object for temp curve
    temp_bevel_curve = bpy.data.curves.new('__temp_bevel', 'CURVE')
    temp_spline = temp_bevel_curve.splines.new('POLY')
    temp_spline.points.add(2)
    temp_spline.points[0].co = Vector((1.0, 0.0, 0.0, 1.0))
    temp_spline.points[1].co = Vector((0.0, 1.0, 0.0, 1.0))
    temp_bevel_obj = bpy.data.objects.new('__temp_bevel', temp_bevel_curve)
    scene.objects.link(temp_bevel_obj)

    # Temp Curve
    curve_copy = curve_obj.data.copy()
    curve_copy.use_fill_caps = False
    curve_copy.bevel_object = temp_bevel_obj
    temp_obj = bpy.data.objects.new('__temp', curve_copy)
    scene.objects.link(temp_obj)
    temp_obj.location = curve_obj.location
    temp_obj.rotation_mode = curve_obj.rotation_mode
    temp_obj.rotation_quaternion = curve_obj.rotation_quaternion
    temp_obj.rotation_euler = curve_obj.rotation_euler

    # convert temp curve to mesh
    bpy.ops.object.select_all(action='DESELECT') 
    scene.objects.active = temp_obj
    temp_obj.select = True
    bpy.ops.object.convert(target='MESH')

    offset = 0
    micro_offset = 0

    # cyclic check
    for i, spline in enumerate(curve.splines):
        if i > spline_index:
            break

        if i > 0:
            ps_count = len(get_spline_points(curve.splines[i-1]))
            offset += ps_count-1
        if spline.use_cyclic_u:
            offset += 1
        elif i > 0:
            micro_offset += 1

    # get x-axis and y-axis of the first handle
    handle_x = temp_obj.data.vertices[curve.resolution_u * (index + offset) * 3 + micro_offset * 3].co
    handle_y = temp_obj.data.vertices[curve.resolution_u * (index + offset) * 3 + 1 + micro_offset * 3].co

    target_x = handle_x - points[index].co.xyz
    target_y = handle_y - points[index].co.xyz
    target_x.normalize()
    target_y.normalize()

    # delete temp objects
    temp_bevel_obj.select = True
    bpy.ops.object.delete()
    
    # match bevel x-axis to handle x-axis
    bevel_x = Vector((1.0, 0.0, 0.0))
    target_x = curve_mat.to_3x3() * target_x
    rot_1 = bevel_x.rotation_difference(target_x)

    # match bevel y-axis to handle y-axis
    bevel_y = rot_1.to_matrix() * Vector((0.0, 1.0, 0.0))
    target_y = curve_mat.to_3x3() * target_y
    rot_2 = bevel_y.rotation_difference(target_y)

    # select curve object again
    scene.objects.active = curve_obj
    curve_obj.select = True

    return rot_2 * rot_1



def get_proper_index_bevel_placement(curve_obj):
    """ Returns (spline index, point index) """
    idx = (0, 0)
    found = False

    for i, spline in enumerate(curve_obj.data.splines):
        points = get_spline_points(spline)
        # Prioritising radius of 1.0
        for j, point in enumerate(points):
            if point.radius == 1.0:
                idx = (i, j)
                found = True
                break
        if found:
            break

    # If still not found do another loop
    if not found:
        for i, spline in enumerate(curve_obj.data.splines):
            points = get_spline_points(spline)
            for j, point in enumerate(points):
                if point.radius <= 1.0 and point.radius >= 0.3:
                    temp_ps = get_spline_points(curve_obj.data.splines[idx[0]])
                    old_radius = temp_ps[idx[1]].radius
                    # get the biggest radius under 1.0
                    if point.radius > old_radius or old_radius > 1.0:
                        idx = (i, j)
    return idx



class VIEW3D_TP_Convert_to_Mesh(bpy.types.Operator):
    """Join, isolate or union curve / convert to meshes"""
    bl_idname = "tp_ops.convert_to_merged_mesh"
    bl_label = "Convert To Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # check if curve is selected
        obj = bpy.context.active_object
        return context.mode == 'OBJECT' and obj and obj.type == 'CURVE'
    

    mode = bpy.props.StringProperty(default="")

    bpy.types.Scene.tp_curve_convert_toogle = bpy.props.BoolProperty(name="Convert Toggle", description="convert to mesh or keep curves", default=True)  

    bpy.types.Scene.tp_try_dissolve_toogle = bpy.props.BoolProperty(name="Try Dissolve",  description="try to dissolve the vertices inside the boundary", default=True)

    def execute(self, context):

        scene = context.scene

        # Listing selected curve objects
        selected_objs = [obj for obj in scene.objects if obj.select == True and obj.type == 'CURVE'] # and o.data.bevel_object]


        if "SEPARATE" in self.mode: 

            for obj in selected_objs:

                splines = obj.data.splines
                spline_len = len(splines)

                # if spline is more than one, do separation
                if spline_len > 1:

                    scene.objects.active = obj
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.curve.select_all(action='DESELECT')

                    # do reversed loop to separate
                    for i in reversed(range(1, spline_len)):
                        for bp in splines[i].bezier_points:
                            bp.select_control_point = True
                        bpy.ops.curve.separate()

                    bpy.ops.object.editmode_toggle()  
  
 
        # toggle convert curve to mesh
        scene = bpy.context.scene            
        for i in range(scene.tp_curve_convert_toogle):
                       
            bpy.ops.object.convert(target='MESH')
            
            # remove vertex duplication on selected objects
            for obj in selected_objs:
                scene.objects.active = obj
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.remove_doubles()
                bpy.ops.object.editmode_toggle()
                obj.select = True

       
        if "MERGED" in self.mode: 
            bpy.ops.object.join()

        if "UNION" in self.mode:# and len(selected_objs) > 1:
            
            bpy.ops.object.join() 
            bpy.ops.object.editmode_toggle()            
            bpy.ops.mesh.select_all(action='SELECT')             
     
            bpy.ops.mesh.dissolve_limited()
           
            bpy.ops.mesh.select_all(action='SELECT')  
           
            bpy.ops.mesh.select_mode(type="EDGE")              
            bpy.ops.bpt.boolean_2d_union()

            scene = bpy.context.scene            
            for i in range(scene.tp_try_dissolve_toogle):
                                          
                bpy.ops.mesh.select_all(action='SELECT')
                
                bpy.ops.mesh.region_to_loop()
                bpy.ops.mesh.select_all(action='INVERT')
                bpy.ops.mesh.dissolve_mode(use_verts=True)


            bpy.ops.mesh.select_mode(type="VERT")               
            bpy.ops.object.editmode_toggle()  


        # smooth shade object
        bpy.ops.object.shade_smooth()



        return {'FINISHED'}



bpy.types.Scene.tp_finish_taper = bpy.props.BoolProperty(name="To Editmode of main object", description="back to editmode", default=False)  

class VIEW3D_TP_Finish_Edit_Bevel(bpy.types.Operator):
    """finish editing bevel object"""
    bl_idname = "curve.finish_edit_bevel"
    bl_label = "Finish Edit Bevel"
    bl_description = "Finish edit bevel object"
    bl_options = {'REGISTER', 'UNDO'}

    #bpy.types.Scene.tp_finish_taper = bpy.props.BoolProperty(name="To Editmode of main object", description="back to editmode", default=False)  

    def execute(self, context):
        
        bpy.ops.object.editmode_toggle()
     
        bevel_obj = context.active_object       

        # add bevel object to layer 19
        bevel_obj.layers[19] = True
        for i in range(19):
            bevel_obj.layers[i] = False
        bevel_obj.hide = True

        # select source
        for obj in context.scene.objects:
            if obj.type == 'CURVE' and obj.data.bevel_object and obj.data.bevel_object == bevel_obj:
                obj.select = True
                context.scene.objects.active = obj

        # toggle to source editmode
        scene = bpy.context.scene            
        for i in range(scene.tp_finish_taper):
            bpy.ops.object.editmode_toggle()

        return {'FINISHED'}




class VIEW3D_TP_Hide_Bevel_Objects(bpy.types.Operator):
    """Nice Useful Tooltip"""
    bl_idname = "curve.hide_bevel_objects"
    bl_label = "Hide Bevel Objects"
    bl_description = "Hide all bevel objects in the scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        scn = context.scene

        bevel_objs = list()

        for obj in scn.objects:
            if obj.type == 'CURVE' and obj.data.bevel_object and obj.data.bevel_object not in bevel_objs:
                bevel_objs.append(obj.data.bevel_object)
            if '_bevel_obj' in obj.name and  obj not in bevel_objs:
                bevel_objs.append(obj)
        
        for obj in bevel_objs:
            # Change object's layer to only layer 19
            obj.layers[19] = True
            for i in range(19):
                obj.layers[i] = False
            # Hide objects
            obj.hide = True
        
        return {'FINISHED'}



class VIEW3D_TP_Edit_Bevel_Curve(bpy.types.Operator):
    """Nice Useful Tooltip"""
    bl_idname = "curve.edit_bevel_curve"
    bl_label = "Edit Bevel"
    bl_description = "Edit bevel shape of curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        scn = context.scene
        obj = context.active_object
        curve = obj.data
        bevel_obj = curve.bevel_object

        if context.mode in EDIT:
            bpy.ops.object.mode_set(mode = 'OBJECT')  

        # hide all bevel objects around first
        bpy.ops.curve.hide_bevel_objects()

        # duplicate bevel object if it's used by other object
        bevel_used = check_bevel_used_by_other_objects(scn, obj)
        if bevel_used:
            bevel_obj = bpy.data.objects.new(obj.name + '_bevel_obj', bevel_obj.data.copy())
            scn.objects.link(bevel_obj)
            curve.bevel_object = bevel_obj

        idx = get_proper_index_bevel_placement(obj)
        bevel_rotation = get_point_rotation(scn, obj, index=idx[1], spline_index=idx[0])
        bevel_position = get_point_position(obj, index=idx[1], spline_index=idx[0])

        # Set object rotation and location
        bevel_obj.rotation_mode = 'QUATERNION'
        bevel_obj.rotation_quaternion = bevel_rotation
        bevel_obj.location = bevel_position

        # Show bevel object on active layer
        for i in range(20):
            bevel_obj.layers[i] = scn.layers[i]

        # Show object if hidden
        bevel_obj.hide = False

        bpy.ops.object.select_all(action='DESELECT')
        scn.objects.active = bevel_obj
        bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}





# LISTS FOR SELECTED #
name_list = []
dummy_list = []

# CURVE GEOMETRY #
def add_curve(radius):
    bpy.ops.curve.primitive_bezier_curve_add(radius = radius)


def add_circle(radius_circle, rotation_circle, rotation_tilt, self):
    bpy.ops.curve.primitive_bezier_circle_add(radius = radius_circle)#, rotation = rotation_circle)

    bpy.ops.object.editmode_toggle()     
    bpy.ops.curve.select_all(action='SELECT')
   
    if self.shape == 'CIRCLE':            
        pass
  
    elif self.shape == 'OCTAGON':
        
        bpy.ops.curve.spline_type_set(type='POLY', use_handles=True)
        bpy.ops.curve.spline_type_set(type='BEZIER')


    elif self.shape == 'RHOMBUS':

        bpy.ops.curve.handle_type_set(type='FREE_ALIGN')
        bpy.ops.curve.spline_type_set(type='POLY', use_handles=False)
        bpy.ops.curve.spline_type_set(type='BEZIER')
    
    
    elif self.shape == 'SQUARE':

        bpy.ops.curve.handle_type_set(type='FREE_ALIGN')
        bpy.ops.curve.spline_type_set(type='POLY', use_handles=False)
        bpy.ops.curve.spline_type_set(type='BEZIER')

        bpy.ops.transform.rotate(value=0.785398, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='NORMAL')


    elif self.shape == 'TRIANGLE':
    
        bpy.ops.curve.de_select_last()
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.dissolve_verts()
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.handle_type_set(type='VECTOR')


    elif self.shape == 'SEGMENT':

        bpy.ops.curve.de_select_last()
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.delete(type='VERT')
        bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.de_select_first()
        bpy.ops.curve.de_select_last()
        bpy.ops.curve.select_all(action='INVERT')
        bpy.ops.curve.handle_type_set(type='VECTOR')
         


    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.transform.tilt(value=rotation_tilt, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    bpy.ops.object.editmode_toggle()     





class VIEW3D_TP_CurveGuide_for_Bevel(bpy.types.Operator):
    """add curve as guide bevel on target curve"""
    bl_idname = "tp_ops.curve_guide_bevel"
    bl_label = "Bevel Guide"
    bl_options = {'REGISTER', 'UNDO'}

    shape = EnumProperty(name = "Shape",
            items=(('SQUARE',       "Square",       ""),
                   ('SEGMENT',      "Segment",      ""),
                   ('TRIANGLE',     "Triangle",     ""), 
                   ('OCTAGON',      "Octagon",      ""), 
                   ('RHOMBUS',      "Rhombus",      ""), 
                   ('CIRCLE',       "Circle",       "")),                   
                   default='CIRCLE',
                   description="Use predefined shape of bevel")

    #radius = FloatProperty(name="Size (Curve)", description="Size of the curve", min=0.1, max=100.0, default=10.0, step=0.3, precision=3)    

    radius_circle = FloatProperty(name="Size Bevel Object)", description="Size of the curve", min=0.1, max=100.0, default=10.0, step=0.3, precision=3)
    rotation_tilt = FloatProperty(name="Rotate", description="Tilt rotation", unit='ROTATION', min=0.0, max=math.pi*2.0, default=0.0)
    rotation_circle = FloatProperty(name="Rotate (Bevel Object)", description="rotation", unit='ROTATION', min=0.0, max=math.pi*2.0, default=0.0)

    type = IntProperty(name='Type', description='Type of bevel curve', default=1, min=1, max=5)
    scale_x = FloatProperty(name="scale x", description="scale on x axis", default=5.0)
    scale_y = FloatProperty(name="scale y", description="scale on y axis", default=5.0)
    link = BoolProperty(name='link xy', default=True)

    def execute(self, context):

        curve_obj = context.active_object
        curve = curve_obj.data
     
        selected = bpy.context.selected_objects
        
        #add_curve(self.radius) 

        if context.mode in EDIT:
            bpy.ops.object.mode_set(mode = 'OBJECT')   


#        obj = context.active_object     
#        if obj:
#           obj_type = obj.type
#           if obj_type in {'CURVE'}:    
#        

 
        for obj in selected:

            # add source to name list
            name_list.append(obj.name)   

            # add bevel object
            #add_circle(self.radius_circle, self.rotation_circle, self.rotation_tilt, self)


            bpy.context.object.name = obj.name + "_bevel_obj"
            bpy.context.object.data.name = obj.name + "_bevel_obj"

            # add new object to dummy name list
            new_object_name = obj.name + "_bevel_obj"
            dummy_list.append(new_object_name) 

            # deselect source
            bpy.data.objects[obj.name].select = False   

            # select objects in lists             
            bpy.data.objects[new_object_name].select = True                                  
            new_object_name = bpy.context.active_object  
             
            # add bevel to curve
            curve.bevel_object = new_object_name
            curve.use_fill_caps = True

            # Send bevel object to layer 20
            new_object_name.layers[19] = True
            for i in range(19):
                new_object_name.layers[i] = False
                # Hide objects
            new_object_name.hide = True


            # select source
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[obj.name].select = True             
            bpy.context.scene.objects.active = selected[0]

        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()