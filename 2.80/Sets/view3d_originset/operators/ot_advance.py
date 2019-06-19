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
# original advanced align tools by authors: Lell, Anfeo
# original distribute objects by authors: Oscurart and CodemanX



# LOAD MODUL #
import bpy, mathutils
from mathutils import Vector, Matrix
from bpy.props import EnumProperty, BoolProperty, IntProperty, FloatVectorProperty
#from ..icons.icons import load_icons

# used_subject 0 for object, 1 for pivot and 2 for cursor
def align_function(used_subject, active_too, use_consistent, use_self_or_active, 
                   ref1, ref2, use_invert, use_invert2, show_boundbox, show_boundbox_type,
                   location_x_axis, location_y_axis, location_z_axis, location_offset, 
                   rotation_x, rotation_y, rotation_z, rotation_offset, 
                   scale_x, scale_y, scale_z, scale_offset, 
                   fit_x, fit_y, fit_z,
                   lock_location_x, lock_location_y, lock_location_z,
                   lock_rotation_x,lock_rotation_y, lock_rotation_z,
                   lock_scale_x, lock_scale_y, lock_scale_z,
                   cycle_through, viewport_display, show_display_name, show_display_axis,
                   show_display_wire, show_display_edges, show_display_space, show_display_shadow,
                   show_display_front, show_display_type, show_obj_color):

    view_layer = bpy.context.view_layer        
   
    for i in range(cycle_through): 
        bpy.ops.tpc_ops.cycle_through()

    sel_obj = bpy.context.selected_objects
    act_obj = view_layer.objects.active
    
    global sel_max
    global sel_min
    global sel_center
    global ref2_co
       
    def get_reference_points(obj, space):
        
        me = obj.data
        co_list = []
        #get all the points coordinates
        if space == "global":
            ok = False
            obj_mtx = obj.matrix_world                                                           
            if obj.type == 'MESH' and len(me.vertices) > 0:                    
                ok = True                
                for p in me.vertices:
                    co_list.append((obj_mtx @ p.co))    

            elif obj.type == 'SURFACE' and len(me.splines) > 0:
                ok = True                
                for s in me.splines:
                    for p in s.points:
                        co_list.append((obj_mtx @ p.co))
            elif obj.type == 'FONT' and len(me.splines) > 0:
                ok = True                
                for s in me.splines:
                    for p in s.bezier_points:
                        co_list.append((obj_mtx @ p.co))
         
        elif space == "local":            
            ok = False                                                           
            if obj.type == 'MESH' and len(me.vertices) > 0:                    
                ok = True                
                for p in me.vertices:
                    co_list.append(p.co)    

            elif o.type == 'SURFACE' and len(me.splines) > 0:
                ok = True                
                for s in me.splines:
                    for p in s.points:
                        co_list.append(p.co)
            elif o.type == 'FONT' and len(o.data.splines) > 0:
                ok = True                
                for s in me.splines:
                    for p in s.bezier_points:
                        co_list.append(p.co)                 
        
        # if a valid point has been found
        # proceed to calculate the extremes
        if ok:            
            
            max_x = co_list[0][0] #x.co.x
            min_x = co_list[0][0] #x.co.x
           
            max_y = co_list[0][1] #x.co.y
            min_y = co_list[0][1] #x.co.y

            max_z = co_list[0][2] #x.co.z
            min_z = co_list[0][2] #x.co.z
                
            for v in co_list:                                
                
                # comparison of the coorders of the list 
                # to find the minor and major ones for each axis

                act_x = v[0] #a
                act_y = v[1] #b
                act_z = v[2] #c                                             
                
           
                if use_invert == False:
                    
                    # plus x                    
                    if location_x_axis == True:                    
                        if act_x > max_x:    max_x = act_x
                        if act_x > min_x:    min_x = act_x
                    
                    if use_invert2 == False:

                        # plus y
                        if location_y_axis == True:                    
                            if act_y > max_y:    max_y = act_y
                            if act_y > min_y:    min_y = act_y

                    else:
                            
                        # minus y
                        if location_y_axis == True:                    
                            if act_y < max_y:    max_y = act_y
                            if act_y < min_y:    min_y = act_y
                                                                                              
                else:                                                     
      
                    # minus x
                    if location_x_axis == True:                    
                        if act_x < max_x:    max_x = act_x
                        if act_x < min_x:    min_x = act_x
                                      
                    if use_invert2 == False: 
                                     
                        # minus y
                        if location_y_axis == True:                    
                            if act_y < max_y:    max_y = act_y
                            if act_y < min_y:    min_y = act_y
                  
                    else:
                  
                        # minus y
                        if location_y_axis == True:                    
                            if act_y > max_y:    max_y = act_y
                            if act_y > min_y:    min_y = act_y

              
                if location_z_axis == True:   

                    # max = plus z
                    if act_z > max_z:    max_z = act_z             
              
                    # min = plus z                
                    if act_z < min_z:    min_z = act_z                
                        

        else:
            # use the object pivot
            a = obj.location  
            min_x = a[0]
            max_x = a[0] 
            min_y = a[1]
            max_y = a[1]                                
            min_z = a[2]
            max_z = a[2]


        center_x = min_x + ((max_x - min_x) / 2)
        center_y = min_y + ((max_y - min_y) / 2)
        center_z = min_z + ((max_z - min_z) / 2)               
                      
        reference_points = [min_x, center_x, max_x, min_y, center_y, max_y, min_z, center_z, max_z]    
       
        return reference_points

    
    
    # look for the extreme points of the selection    
    def get_sel_ref(ref_co, sel_obj):
        
        sel_min = ref_co.copy()
        sel_max = ref_co.copy() 
        
        for obj in sel_obj:
            if obj != act_obj or (active_too and obj == act_obj):
                
                ref_points = get_reference_points(obj, "global")

                ref_min = Vector([ref_points[0], ref_points[3], ref_points[6]])
                ref_max = Vector([ref_points[2], ref_points[5], ref_points[8]])            
                   
                if ref_min[0] < sel_min[0]:              
                    sel_min[0] = ref_min[0]
              
                if ref_max[0] > sel_max[0]:
                    sel_max[0] = ref_max[0]
               
                if ref_min[1] < sel_min[1]:
                    sel_min[1] = ref_min[1]
               
                if ref_max[1] > sel_max[1]:
                    sel_max[1] = ref_max[1]
               
                if ref_min[2] < sel_min[2]:
                    sel_min[2] = ref_min[2]
               
                if ref_max[2] > sel_max[2]:
                    sel_max[2] = ref_max[2]

        return sel_min, sel_max;
                    
                    
   
    def find_ref2_co(act_obj):
        
        # contains the coordinates of the reference point for positioning
        if ref2 == "set_min":        
            ref_points = get_reference_points(act_obj, "global")
            ref2_co = [ref_points[0], ref_points[3], ref_points[6]]           
            ref2_co = Vector(ref2_co)
       
        elif ref2 == "set_center":
            ref_points = get_reference_points(act_obj, "global")
            ref2_co = [ref_points[1], ref_points[4], ref_points[7]]     
            ref2_co = Vector(ref2_co)
       
        elif ref2 == "set_origin":
            ref2_co = act_obj.location
            ref2_co = Vector(ref2_co)
      
        elif ref2 == "set_max":    
            ref_points = get_reference_points(act_obj, "global")
            ref2_co = [ref_points[2], ref_points[5], ref_points[8]]        
            ref2_co = Vector(ref2_co)
       
        elif ref2 == "set_cursor":
            ref2_co = bpy.context.scene.cursor.location                    
       
        elif ref2 == "set_zero":
            ref2_co = act_obj.location
            ref2_co = Vector(ref2_co)

        elif ref2 == "set_distribute":
            ref2_co = act_obj.location
            ref2_co = Vector(ref2_co)
      
        return ref2_co


    
    def find_zero_coord(obj):
        
        bpy.context.scene.cursor.location = bpy.context.object.location  
 
        if location_x_axis == True: 
            bpy.context.scene.cursor.location[0] = 0 + location_offset[0] 
            bpy.context.object.location[0] = 0 + location_offset[0]                    
            for obj in sel_obj:                  
                obj.location[0] = act_obj.location[0] + location_offset[0]

        if location_y_axis == True:
            bpy.context.scene.cursor.location[1] = 0 + location_offset[1] 
            if used_subject == "use_object":        
                bpy.context.object.location[1] = 0 + location_offset[1]  
                for obj in sel_obj:                  
                    obj.location[1] = act_obj.location[1] + location_offset[1]
      
        if location_z_axis == True:               
            bpy.context.scene.cursor.location[2] = 0 + location_offset[2]   
            bpy.context.object.location[2] = 0 + location_offset[2]  
            for obj in sel_obj:                  
                obj.location[2] = act_obj.location[2] + location_offset[2]           
        
        
    def find_new_coord(obj):

        ref_points = get_reference_points(obj, "global") 

        if location_x_axis == True:
           
            if ref1 == "set_min":                           
                min_x = ref_points[0]
                new_x = ref2_co[0] + (obj.location[0] - min_x) + location_offset[0]
           
            elif ref1 == "set_center":
                center_x = ref_points[1]
                new_x = ref2_co[0] + (obj.location[0] - center_x) + location_offset[0]
           
            elif ref1 == "set_origin":
                new_x = ref2_co[0] + location_offset[0]
           
            elif ref1 == "set_max":                
                max_x = ref_points[2]   
                new_x = ref2_co[0] - (max_x - obj.location[0]) + location_offset[0] 

            obj.location[0] = new_x
         
 
        if location_y_axis == True:
           
            if ref1 == "set_min":            
                min_y = ref_points[3]
                new_y = ref2_co[1] + (obj.location[1] - min_y) + location_offset[1]
            
            elif ref1 == "set_center":
                center_y = ref_points[4]
                new_y = ref2_co[1] + (obj.location[1] - center_y) + location_offset[1]
           
            elif ref1 == "set_origin":
                new_y = ref2_co[1] + location_offset[1]
           
            elif ref1 == "set_max":                
                max_y = ref_points[5]   
                new_y = ref2_co[1] - (max_y - obj.location[1]) + location_offset[1]        
         
            obj.location[1] = new_y
       

        if location_z_axis == True:
            
            if ref1 == "set_min":           
                min_z = ref_points[6]
                new_z = ref2_co[2] + (obj.location[2] - min_z) + location_offset[2]
            
            elif ref1 == "set_center":
                center_z = ref_points[7]
                new_z = ref2_co[2] + (obj.location[2] - center_z) + location_offset[2]
           
            elif ref1 == "set_origin":
                new_z = ref2_co[2] + location_offset[2]
           
            elif ref1 == "set_max":                
                max_z = ref_points[8]
                new_z = ref2_co[2] - (max_z - obj.location[2]) + location_offset[2]

            obj.location[2] = new_z
    
   
    def find_new_rotation(obj):
      
        if rotation_x == True:
            obj.rotation_euler[0] = act_obj.rotation_euler[0] + rotation_offset[0]
      
        if rotation_y == True:    
            obj.rotation_euler[1] = act_obj.rotation_euler[1] + rotation_offset[1]
      
        if rotation_z == True:    
            obj.rotation_euler[2] = act_obj.rotation_euler[2] + rotation_offset[2]
    
  
    def find_new_scale(obj):
       
        if scale_x == True:
            obj.scale[0] = act_obj.scale[0] + scale_offset[0]
       
        if scale_y == True:    
            obj.scale[1] = act_obj.scale[1] + scale_offset[1]
       
        if scale_z == True:    
            obj.scale[2] = act_obj.scale[2] + scale_offset[2]
                    
  
    def find_new_dimensions(obj, ref_dim):
       
        ref_points = get_reference_points(obj, "local")
       
        if fit_x:
            dim = ref_points[2] - ref_points[0]
            obj.scale[0] = (ref_dim[0] / dim) * act_obj.scale[0] 
       
        if fit_y:
            dim = ref_points[5] - ref_points[3]
            obj.scale[1] = (ref_dim[1] / dim) * act_obj.scale[1] 
      
        if fit_z:
            dim = ref_points[8] - ref_points[6]
            obj.scale[2] = (ref_dim[2] / dim) * act_obj.scale[2]         
            
        
    def move_pivot(obj):
        me = obj.data                
        vec_ref2_co = Vector(ref2_co)       
        offset = vec_ref2_co - obj.location  

        offset_x = [offset[0] + location_offset[0], 0, 0]
        offset_y = [0, offset[1] + location_offset[1], 0]
        offset_z = [0, 0, offset[2] + location_offset[2]]   
        
        def movement(vec):
            obj_mtx = obj.matrix_world.copy()
            # find pivot displacement vector
            move_pivot = Vector(vec)
             
            # move the pivot point = object location
            pivot = obj.location
            pivot += move_pivot 
    
             
            nm = obj_mtx.inverted() @ Matrix.Translation(-move_pivot) @ obj_mtx

            # move mesh
            me.transform(nm) 
            
        if location_x_axis: 
            movement(offset_x)

        if location_y_axis:
            movement(offset_y)   
       
        if location_z_axis:
            movement(offset_z)



    def point_in_selection(act_obj, sel_obj):
     
        ok = False
        for o in sel_obj:
            if o != act_obj:
                ref_ob = o
                obj_mtx = o.matrix_world                   
               
                if o.type == 'MESH' and len(o.data.vertices) > 0:
                    ref_co = o.data.vertices[0].co.copy()
                    ref_co = obj_mtx @ ref_co
                    ok = True                        
                    break
                
                elif o.type == 'CURVE' and len(o.data.splines) > 0:
                    ref_co = o.data.splines[0].bezier_point[0].co.copy()
                    ref_co = obj_mtx @ ref_co
                    ok = True
                    break
             
                elif o.type == 'SURFACE' and len(o.data.splines) > 0:
                    ref_co = o.data.splines[0].points[0].co.copy()
                    ref_co = obj_mtx @ ref_co
                    ok = True
                    break
               
                elif o.type == 'FONT' and len(o.data.splines) > 0:
                    ref_co = o.data.splines[0].bezier_points[0].co.copy()
                    ref_co = obj_mtx @ ref_co
                    ok = True
                    break                   
      
        # if no object had data: use of position of an object that is not the active one
        # as the internal point of the selection    
        if ok == False:
            for o in sel_obj:
                if o != act_obj:
                    ref_ob = o 
                    ref_co = ref_ob.location
        
        return ref_co    
  

    

    # USE OBJECT #                 
    if used_subject == "use_object":

        if act_obj.type == 'MESH' or act_obj.type == 'FONT' or act_obj.type == 'SURFACE': #or act_obj.type == 'CURVE' 
            ref2_co = find_ref2_co(act_obj)            
        
        else:
          
            if ref2 == "set_cursor":
                ref2_co = bpy.context.scene.cursor.location
           
            else:    
                ref2_co = act_obj.location
   
       
        # in the case of consistent selection
        if use_consistent: 

            for o in sel_obj:
                if o != act_obj:
                    ref_ob = o 
                    ref_co = ref_ob.location
            
                    # looking for a point that is in the selection space          
                    ref_co = point_in_selection(act_obj, sel_obj)                                

                    sel_min, sel_max = get_sel_ref(ref_co, sel_obj)
                            
                    sel_center = sel_min + ((sel_max - sel_min) / 2)        
                    
                    translate = [0, 0, 0]

                    # calculation of how much to move the selection
                    if ref1 == "set_min":                                               
                        translate = ref2_co - sel_min + location_offset
                  
                    elif ref1 == "set_center":
                        translate = ref2_co - sel_center + location_offset                              
                 
                    elif ref1 == "set_max": 
                        translate = ref2_co - sel_max + location_offset                                           

                    # move the various objects   
                    for obj in sel_obj:
                        
                        if obj != act_obj or (active_too and obj == act_obj):

                            if location_x_axis:                             
                                obj.location[0] += translate[0]

                            if location_y_axis:                              
                                obj.location[1] += translate[1]   

                            if location_z_axis:                                    
                                obj.location[2] += translate[2]
     

        else:  
           
            for obj in sel_obj:
              
                if obj != act_obj:
                   
                    if rotation_x or rotation_y or rotation_z:
                        find_new_rotation(obj)
                
                    if fit_x or fit_y or fit_z:
                        dim = [0, 0, 0]
                        ref_points = get_reference_points(act_obj, "local")                    
                        dim[0] = ref_points[2]-ref_points[0]
                        dim[1] = ref_points[5]-ref_points[3]
                        dim[2] = ref_points[8]-ref_points[6]
                        find_new_dimensions(obj, dim)
                    
                    if scale_x or scale_y or scale_z:
                        find_new_scale(obj)    
                       
                    if location_x_axis or location_y_axis or location_z_axis:                          
                        
                        if ref2 != "set_zero":                                
                            find_new_coord(obj)
                        else:
                            find_zero_coord(obj)
                                                    
                                                              
            if active_too == True:
               
                if location_x_axis or location_y_axis or location_z_axis:
                    find_new_coord(act_obj)
                    if ref2 != "set_zero":                                
                        find_new_coord(act_obj)
                    else:
                        find_zero_coord(act_obj)

              
                if rotation_x or rotation_y or rotation_z:
                    find_new_rotation(act_obj)
              
                if scale_x or scale_y or scale_z:
                    find_new_scale(act_obj)
                                





    # USE ORIGIN #    
    elif used_subject == "use_origin":   
           
        if ref2 == "set_zero":            

            ref2_co = bpy.context.scene.cursor.location  
            
            bpy.context.scene.cursor.location = bpy.context.object.location   

            if location_x_axis == True: 
                bpy.context.scene.cursor.location[0] = 0 + location_offset[0] 
            
                if bpy.context.mode == 'OBJECT':
                    for obj in sel_obj:
                        if active_too == True:
                            move_pivot(obj)  
                        else:  
                            if obj != act_obj:
                                move_pivot(obj)                                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    for obj in sel_obj:
                        if active_too == True:
                            move_pivot(obj)  
                        else:  
                            if obj != act_obj:
                                move_pivot(obj)     
                    bpy.ops.object.editmode_toggle() 

            if location_y_axis == True:    
                bpy.context.scene.cursor.location[1] = 0 + location_offset[1] 
            
                if bpy.context.mode == 'OBJECT':            
                    for obj in sel_obj:
                        if active_too == True:
                            move_pivot(obj)  
                        else:  
                            if obj != act_obj:
                                move_pivot(obj)  
                else:   
                    bpy.ops.object.editmode_toggle()
                    for obj in sel_obj:
                        if active_too == True:
                            move_pivot(obj)  
                        else:  
                            if obj != act_obj:
                                move_pivot(obj)  
                    bpy.ops.object.editmode_toggle() 

            if location_z_axis == True:      
                bpy.context.scene.cursor.location[2] = 0 + location_offset[2]    
        
                if bpy.context.mode == 'OBJECT':
                    for obj in sel_obj:
                        if active_too == True:
                            move_pivot(obj)  
                        else:  
                            if obj != act_obj:
                                move_pivot(obj)                 
                else:   
                    bpy.ops.object.editmode_toggle()
                    for obj in sel_obj:
                        if active_too == True:
                            move_pivot(obj)  
                        else:  
                            if obj != act_obj:
                                move_pivot(obj)   
                    bpy.ops.object.editmode_toggle() 

       
        else:
            
            if use_self_or_active == "use_active":
                if act_obj.type == 'MESH':
                    ref2_co = find_ref2_co(act_obj)
           
            for obj in sel_obj:
               
                if use_self_or_active == "use_self":
                    ref2_co = find_ref2_co(obj)
               
                if location_x_axis or location_y_axis or location_z_axis:
                    if obj != act_obj and obj.type == 'MESH':
                        move_pivot(obj)
            
            if active_too == True:
                if act_obj.type == 'MESH':
                    if location_x_axis or location_y_axis or location_z_axis:
                        if use_self_or_active == "use_self":
                            ref2_co = find_ref2_co(act_obj)
                        move_pivot(act_obj)





    # USE CURSOR #    
    elif used_subject == "use_cursor":
       
        if use_self_or_active == "use_active":
           
            if act_obj.type == 'MESH' or act_obj.type == 'FONT' or act_obj.type == 'SURFACE': #or act_obj.type == 'CURVE' 
                ref2_co = find_ref2_co(act_obj)
                ref_points = get_reference_points(act_obj, "global")
           
            else: 
                ref2_co = act_obj.location
                ref_points = [act_obj.location[0], act_obj.location[0], act_obj.location[0], 
                              act_obj.location[1], act_obj.location[1], act_obj.location[1], 
                              act_obj.location[2], act_obj.location[2], act_obj.location[2]]        
            
           
            if ref2 == "set_min":            
               
                if location_x_axis == True:
                    bpy.context.scene.cursor.location[0] = ref_points[0] + location_offset[0]
               
                if location_y_axis == True:
                    bpy.context.scene.cursor.location[1] = ref_points[3] + location_offset[1]
              
                if location_z_axis == True:
                    bpy.context.scene.cursor.location[2] = ref_points[6] + location_offset[2]
           
            elif ref2 == "set_center":
                
                if location_x_axis == True:
                    bpy.context.scene.cursor.location[0] = ref_points[1] + location_offset[0]
               
                if location_y_axis == True:
                    bpy.context.scene.cursor.location[1] = ref_points[4] + location_offset[1]
               
                if location_z_axis == True:
                    bpy.context.scene.cursor.location[2] = ref_points[7] + location_offset[2]
            
            elif ref2 == "set_origin":
               
                if location_x_axis == True: bpy.context.scene.cursor.location[0] = act_obj.location[0] + location_offset[0]
               
                if location_y_axis == True: bpy.context.scene.cursor.location[1] = act_obj.location[1] + location_offset[1]
               
                if location_z_axis == True: bpy.context.scene.cursor.location[2] = act_obj.location[2] + location_offset[2]
           
            elif ref2 == "set_max":
                
                if location_x_axis == True:
                    bpy.context.scene.cursor.location[0] = ref_points[2] + location_offset[0]
                
                if location_y_axis == True:
                    bpy.context.scene.cursor.location[1] = ref_points[5] + location_offset[1]
               
                if location_z_axis == True:
                    bpy.context.scene.cursor.location[2] = ref_points[8] + location_offset[2]

           
            elif ref2 == "set_zero": 
                if location_x_axis == True: 
                    bpy.context.scene.cursor.location[0] = 0 + location_offset[0] 
                
                if location_y_axis == True:    
                    bpy.context.scene.cursor.location[1] = 0 + location_offset[1] 

                if location_z_axis == True:      
                    bpy.context.scene.cursor.location[2] = 0 + location_offset[2]   

      
        elif use_self_or_active == "use_selection":
            ref_co = point_in_selection(act_obj, sel_obj)
            
            sel_min, sel_max = get_sel_ref(ref_co, sel_obj)
            sel_center = sel_min + ((sel_max - sel_min) / 2)
            
            if ref2 == "set_min":            
                
                if location_x_axis == True:
                    bpy.context.scene.cursor.location[0] = sel_min[0] + location_offset[0]
               
                if location_y_axis == True:
                    bpy.context.scene.cursor.location[1] = sel_min[1] + location_offset[1]
               
                if location_z_axis == True:
                    bpy.context.scene.cursor.location[2] = sel_min[2] + location_offset[2]
           
            elif ref2 == "set_center":
               
                if location_x_axis == True:
                    bpy.context.scene.cursor.location[0] = sel_center[0] + location_offset[0]
              
                if location_y_axis == True:
                    bpy.context.scene.cursor.location[1] = sel_center[1] + location_offset[1]
               
                if location_z_axis == True:
                    bpy.context.scene.cursor.location[2] = sel_center[2] + location_offset[2]
          
            elif ref2 == "set_max":
                
                if location_x_axis == True:
                    bpy.context.scene.cursor.location[0] = sel_max[0] + location_offset[0]
                
                if location_y_axis == True:
                    bpy.context.scene.cursor.location[1] = sel_max[1] + location_offset[1]
               
                if location_z_axis == True:
                    bpy.context.scene.cursor.location[2] = sel_max[2] + location_offset[2]

     
            elif ref2 == "set_zero": 
                if location_x_axis == True: 
                    bpy.context.scene.cursor.location[0] = 0 + location_offset[0] 
                
                if location_y_axis == True:    
                    bpy.context.scene.cursor.location[1] = 0 + location_offset[1] 

                if location_z_axis == True:      
                    bpy.context.scene.cursor.location[2] = 0 + location_offset[2]   



        # USE DISTRIBUTE #    
        if ref2 == "set_distribute":
            
            if len(bpy.context.selected_objects) <= 1:
            
                print(self)
                self.report({'INFO'}, "Select more!")  

            else:
                #ref2_co = bpy.context.scene.cursor.location

                axis_x = 0
                axis_y = 0
                axis_z = 0     
                  
                if use_invert == False: 

                    dif = sel_obj[-1].location - sel_obj[0].location + location_offset

                    global_axis = dif/(len(sel_obj[:])-1)
                        
                    new_location = sel_obj[0].location

                else:
                    dif = sel_obj[0].location - sel_obj[-1].location + location_offset
                             
                    global_axis = dif/(len(sel_obj[:])-1)

                    new_location = sel_obj[-1].location      
                
                for obj in sel_obj:    
                          
                    if location_x_axis == True:  
                        obj.location[0]  = new_location[0] + axis_x 
                   
                    if location_y_axis == True: 
                        obj.location[1] = new_location[1] + axis_y
                    
                    if location_z_axis == True:
                        obj.location[2]  = new_location[2] + axis_z
                            
                    axis_x += global_axis[0] 
                    axis_y += global_axis[1]
                    axis_z += global_axis[2]


    # LOCK TRANSFORM # 
    for obj in sel_obj: 

        if lock_location_x == True:
            obj.lock_location[0] = True
        else:
            obj.lock_location[0] = False
       
        if lock_location_y == True:
            obj.lock_location[1] = True
        else:
            obj.lock_location[1] = False
        
        if lock_location_z == True:
            obj.lock_location[2] = True
        else:
            obj.lock_location[2] = False

        if lock_rotation_x == True:
            obj.lock_rotation[0] = True
        else:
            obj.lock_rotation[0] = False
       
        if lock_rotation_y == True:
            obj.lock_rotation[1] = True
        else:
            obj.lock_rotation[1] = False
       
        if lock_rotation_z == True:
            obj.lock_rotation[2] = True
        else:
            obj.lock_rotation[2] = False
       
        if lock_scale_x == True:
            obj.lock_scale[0] = True
        else:
            obj.lock_scale[0] = False
       
        if lock_scale_y == True:
            obj.lock_scale[1] = True
        else:
            obj.lock_scale[1] = False
       
        if lock_scale_z == True:
            obj.lock_scale[2] = True
        else:
            obj.lock_scale[2] = False

        if show_boundbox == False:            
            obj.show_bounds = False
        else:
            obj.show_bounds = True
            obj.display_bounds_type = show_boundbox_type


        if show_display_name == False:
            obj.show_name = False
        else:
            obj.show_name = True
 
        if show_display_axis == False:
            obj.show_axis = False
        else:
            obj.show_axis = True

        if show_display_wire == False:
            obj.show_wire = False
        else:
            obj.show_wire = True

        if show_display_edges == False:
            obj.show_all_edges = False
        else:
            obj.show_all_edges = True

        if show_display_space == False:
            obj.show_texture_space = False
        else:
            obj.show_texture_space = True

        if show_display_shadow == False:
            obj.display.show_shadows = False
        else:
            obj.display.show_shadows = True

        if show_display_front == False:
            obj.show_in_front = False
        else:
            obj.show_in_front = True

        obj.display_type = show_display_type
        obj.color = (show_obj_color)


    # RELOAD ACTIVE #     
    view_layer.objects.active = act_obj

    return {'FINISHED'} 



class VIEW3D_OT_advanced_align_tools(bpy.types.Operator):
    """Align Object, Origins and Cursor / Distribute Origins / Zero to XYZ Axis / Align to Bounding Box (use Self)"""
    bl_idname = "tpc_ops.advanced_align_tools"
    bl_label = "Advanced Align"
    bl_description = "Advanced Align"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    # ADVANCED #         
    open_location : BoolProperty (name = "Align Location", default=True, description= "move the selected")    
    open_rotation : BoolProperty (name = "Align Rotation", default=True, description= "rotate the selected")    
    open_scale : BoolProperty (name = "Align Scale", default=True, description= "scale the selected")    
    open_dimension : BoolProperty (name = "Align Dimension", default=True, description= "set dimension on selected")    

    active_too : BoolProperty (name = "Active too", default=True, description= "move the active object, too")    
    active_too : BoolProperty (name = "Active too", default=True, description= "move the active object, too")    
    active_too : BoolProperty (name = "Active too", default=True, description= "move the active object, too")    
    show_advanced : BoolProperty (name = "Advanced", default =False, description = "show all advanced options")    
    use_consistent : BoolProperty (name = "Consistent", default = False, description = "use consistent selection")
   
    used_subject : EnumProperty (items=(("use_object", "Object", "align objects"), 
                                        ("use_origin", "Origin", "align objects origin"), 
                                        ("use_cursor", "Cursor", "align cursor to active")), 
                                        name = "Align to...", 
                                        description = "choose element to align")   

    # OPTION FOR SELECTED #
    ref1 : EnumProperty (items=(("set_max",     "Max",      "align the maximum point"), 
                                ("set_center",  "Center",   "align the center point"), 
                                ("set_origin",  "Origin",   "align the origin"), 
                                ("set_min",     "Min",      "align the minimum point")),
                                name = "Selection reference", 
                                description = "moved objects reference point")   

    # OPTION FOR ACTIVE #
    ref2 : EnumProperty (items=(("set_max",        "Max",        "align to the maximum point"), 
                                ("set_center",     "Center",     "align to the center point"),
                                ("set_origin",     "Origin",     "align to the origin"),
                                ("set_min",        "Min",        "align to the minimum point"), 
                                ("set_cursor",     "Cursor",     "align to cursor"),
                                ("set_zero",       "Axis",       "align to global axis"),
                                ("set_bbox",       "BBox",       "align origin to bounding box"),
                                ("set_distribute", "Distribute", "distribute between the origin")),
                                name = "Active reference", 
                                description = "destination point")
    
    # RELATION #
    use_self_or_active : EnumProperty (items = (("use_self",        "Self",         "in relation of itself"), 
                                                ("use_active",      "Active",       "in relation of the active object"), 
                                                ("use_selection",   "Selection",    "in relation of the entire selection")), 
                                                name = "Relation", 
                                                default = "use_active", 
                                                description = "align origin to...")


    # ALIGN LOCATION #
    location_x_axis : BoolProperty (name = "Align to X axis", default=False, description= "enable X axis location alignment")
    location_y_axis : BoolProperty (name = "Align to Y axis", default=False, description= "enable Y axis location alignment")                               
    location_z_axis : BoolProperty (name = "Align to Z axis", default=False, description= "enable Z axis location alignment")
    
    apply_loc : BoolProperty (name = "Apply Location", default=False, description= "apply location transform")
    
    lock_location_x : BoolProperty (name = "Lock X Location", default=False, description= "lock location transform on x axis")
    lock_location_y : BoolProperty (name = "Lock Y Location", default=False, description= "lock location transform on y axis")                               
    lock_location_z : BoolProperty (name = "Lock Z Location", default=False, description= "lock location transform on z axis")

    # ALIGN ROTATION #
    rotation_x : BoolProperty (name = "Align Rotation to X axis", default=False, description= "enable X axis rotation alignment")
    rotation_y : BoolProperty (name = "Align Rotation to Y axis", default=False, description= "enable Y axis rotation alignment")
    rotation_z : BoolProperty (name = "Align Rotation to Z axis", default=False, description= "enable Z axis rotation alignment")
    
    apply_rot : BoolProperty (name = "Apply Rotation", default=False, description= "apply rotation transform")
    
    lock_rotation_x : BoolProperty (name = "Lock X Rotation", default=False, description= "lock rotation transform on x axis")
    lock_rotation_y : BoolProperty (name = "Lock Y Rotation", default=False, description= "lock rotation transform on y axis")                               
    lock_rotation_z : BoolProperty (name = "Lock Z Rotation", default=False, description= "lock rotation transform on z axis")
   
    # MATCH SCALE #
    scale_x : BoolProperty (name = "Match Scale to X axis", default=False, description= "enable X axis scale alignment")
    scale_y : BoolProperty (name = "Match Scale to Y axis", default=False, description= "enable Y axis scale alignment")
    scale_z : BoolProperty (name = "match Scale to Z axis", default=False, description= "enable Z axis scale alignment")
    
    apply_scale : BoolProperty (name = "Apply Scale", default=False, description= "apply scale transform")  
    
    lock_scale_x : BoolProperty (name = "Lock X Scale", default=False, description= "lock scale transform on x axis")
    lock_scale_y : BoolProperty (name = "Lock Y Scale", default=False, description= "lock scale transform on y axis")                               
    lock_scale_z : BoolProperty (name = "Lock Z Scale", default=False, description= "lock scale transform on z axis")

    # FIT DIMENSION #
    fit_x : BoolProperty (name = "Fit Dimension to X axis", default=False, description= "enable X axis dimension alignment")
    fit_y : BoolProperty (name = "Fit Dimension to Y axis", default=False, description= "enable Y axis dimension alignment")
    fit_z : BoolProperty (name = "Fit Dimension to Z axis", default=False, description= "enable Z axis dimension alignment")
    
    apply_dim : BoolProperty (name = "Apply  Dimension", default=False, description= "apply dimension transform")

    # TRANSFORM OFFSET #
    location_offset : FloatVectorProperty(name="Location Offset", description="offset for location align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)
    rotation_offset : FloatVectorProperty(name="Rotation Offset", description="offset for rotation alignment", default=(0.0, 0.0, 0.0), subtype='EULER', size=3) 
    scale_offset : FloatVectorProperty(name="Scale Offset", description="offset for scale match", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)                                                               
    
    use_invert : BoolProperty(name="Invert1", default=False)
    use_invert2 : BoolProperty(name="Invert2", default=False)

    # ACTIVE CYCLE  #
    cycle_through : IntProperty(name="cycle active",  description="cycle through all selected to make it active", min=0, max=100, default=0, subtype = 'DISTANCE', options={'SKIP_SAVE'}) 
   
    # DISPLAY # 
    show_boundbox : BoolProperty(name="Show Bounds: Box", default=False) 
    show_boundbox_type : EnumProperty (items = (("BOX",       "Box",        "display bounds as box"), 
                                                ("SPHERE",    "Sphere",     "display bounds as sphere"), 
                                                ("CYLINDER",  "Cylinder",   "display bounds as cylinder"), 
                                                ("CONE",      "Cone",       "display bounds as cone"),  
                                                ("CAPSULE",   "Capsule",    "display bounds as capsule")), 
                                                name = "Display Bounds Type", 
                                                default = "BOX", 
                                                description = "display Bounds type")

    viewport_display : BoolProperty(name="Display", default=False)
    show_display_name : BoolProperty(name="Name", default=False)
    show_display_axis : BoolProperty(name="Axis", default=False)
    show_display_wire : BoolProperty(name="Wire", default=False)
    show_display_edges : BoolProperty(name="All Edges", default=False)
    show_display_space : BoolProperty(name="Texture Space", default=False)
    show_display_shadow : BoolProperty(name="Shadow", default=True)
    show_display_front : BoolProperty(name="In Front", default=False)
    show_obj_color : FloatVectorProperty(name='', description='Object Color', default=(1.0, 1.0, 1.0, 1.0), min=0, max=1, step=1, precision=4, subtype='COLOR_GAMMA', size=4)
    show_display_type : EnumProperty (items = (("BOUNDS",   "Bounds",   "display as bounds"), 
                                               ("WIRE",     "Wire",     "display as wire"), 
                                               ("SOLID",    "Solid",    "display as solid"), 
                                               ("TEXTURED", "Textured", "display as textured")), 
                                                name = "Display Type", 
                                                default = "SOLID", 
                                                description = "display type")



    def draw(self, context):
        layout = self.layout
        
        #icons = load_icons()
        layout.scale_y = 1.05    
  
        view_layer = bpy.context.view_layer    

        if bpy.context.mode == 'OBJECT':

            row = layout.row(align=True)

            row.prop(self,'active_too')
            row.prop(self, 'show_advanced')

            if self.show_advanced:
                row = layout.row(align=True)            
         
            row.prop(self, 'viewport_display')

            if self.show_advanced:
                row.prop(self, 'use_consistent')
            

            layout = self.layout
           
            col = layout.column(align=True)
         
            box = col.box().column(align=True) 
         
            row = box.row(align=True)
            row.prop(self, 'cycle_through', text="cycle active", icon="NEXT_KEYFRAME")
            
            box = col.box().column(align=True) 
            
            box.separator()
          
            # USED ELEMENT TO ALIGN #
            row = box.row(align=True)
            row.prop(self, 'used_subject', expand =True)

            # OPTIONS ACTIVE OBJECT: nSELECTED #
            box.separator()       
            box.separator()   
        
            act = view_layer.objects.active        
            if self.show_advanced == True:
                if act:
                    row = box.row(align=True)          
                    row.label(text="Active: "+act.name, icon ='RESTRICT_SELECT_OFF')
           
            
            row = box.row(align=True)
            #row.prop (self, 'ref2', expand=True)
            row.prop_enum(self, "ref2", 'set_max', text="max")
            row.prop_enum(self, "ref2", 'set_center', text="center")
            row.prop_enum(self, "ref2", 'set_origin', text="origin")
            row.prop_enum(self, "ref2", 'set_min', text="min")
            
            row = box.row(align=True)            
            row.prop_enum(self, "ref2", 'set_cursor', text="cursor")
            row.prop_enum(self, "ref2", 'set_zero', text="axis")

            sub1 = row.row(align=True) 
            sub1.enabled = (self.used_subject == 'use_cursor')
            sub1.prop_enum(self, "ref2", 'set_distribute', text="distribute")
     
            # OPTIONS SELECTION #
            box.separator()       
            box.separator()      
                                    
            #Selection Options
            if self.show_advanced == True:
                sel = bpy.context.selected_objects
                sel_obs = len(sel)
            
                if sel_obs != 0:
                    row = box.row(align=True)
                    row.label(text="nSelected: "+str(sel_obs)+" Objects", icon ='VIS_SEL_11')
          
            if self.ref2 != 'set_zero' and self.ref2 != 'set_distribute':
                if self.used_subject == "use_origin" or self.used_subject == "use_cursor":
                    row = box.row(align=True)
                    row.prop(self, 'use_self_or_active', expand = True)
                else:                   
                    row = box.row(align=True)
                    row.prop(self, 'ref1', expand=True)


            box.separator()       
            box = col.box().column(align=True) 
            box.separator()       

           
            # LOACATION #
            row = box.row(align=True)
            row.prop(self, 'open_location', text='', icon='ORIENTATION_VIEW')
            row.label(text="Align Location:")

            sub = row.row(align=True)
            sub.alignment = 'RIGHT'                 
            if self.used_subject == 'use_object' or self.ref2 == 'set_distribute':
                sub.prop(self, 'use_invert', text='', icon = 'ARROW_LEFTRIGHT')


            if self.used_subject == 'use_origin':
               
                if self.location_x_axis == True or self.location_y_axis == True:
                    sub.prop(self, 'use_invert', text='', icon = 'ARROW_LEFTRIGHT')
                
                if self.location_x_axis == True and self.location_y_axis == True:           
                    sub.prop(self, 'use_invert2', text='', icon = 'FILE_REFRESH')

            sub.label(text="Apply")
            sub.prop(self, 'apply_loc', text='')

         
            if self.open_location == True:                 
               
                box.separator()  
               
                if self.lock_location_x == True:
                    ico_x = 'LOCKED'
                else:
                    ico_x = 'UNLOCKED'       

                if self.lock_location_y == True:
                    ico_y = 'LOCKED'
                else:
                    ico_y = 'UNLOCKED'       
              
                if self.lock_location_z == True:
                    ico_z = 'LOCKED'
                else:
                    ico_z = 'UNLOCKED'       

                row = box.row(align=True)
                row.prop(self, "lock_location_x", text="", icon=ico_x) 
                row.prop(self, "location_x_axis", text="X")       

                row.prop(self, "lock_location_y", text="", icon=ico_y) 
                row.prop(self, "location_y_axis", text="Y") 

                row.prop(self, "lock_location_z", text="", icon=ico_z) 
                row.prop(self, "location_z_axis", text="Z")


                box.separator()  

                # OFFSET #                
                if self.show_advanced == True:
                    row = box.row(align=True)
                    row.prop(self, 'location_offset', text='')     
                                                          
   
            if self.ref2 != 'set_zero' and self.ref2 != 'set_distribute' and self.used_subject == "use_object":

                # ROTATION #
                box.separator()   
                box = col.box().column(align=True) 
                box.separator()   

                row = box.row(align=True)
                row.prop(self, 'open_rotation', text='', icon='ORIENTATION_GIMBAL')       
                row.label(text='Align Rotation:')       
             
                sub = row.row(align=True)
                sub.alignment = 'RIGHT'      
                sub.label(text="Apply")
                sub.prop(self, 'apply_rot', text='')
               
                box.separator()    

                if self.open_rotation == True: 
      
                    if self.lock_rotation_x == True and self.lock_rotation_y == True and self.lock_rotation_z == True:
                        ico_value = 'LOCKED'
                    else:
                        ico_value = 'UNLOCKED'

                    row = box.row(align=True)
                    row.prop(self, "lock_rotation_x", text="", icon=ico_value)  
                    row.prop(self, 'rotation_x', text='X')
                   
                    row.prop(self, "lock_rotation_y", text="", icon=ico_value)           
                    row.prop(self, 'rotation_y', text='Y')

                    row.prop(self, "lock_rotation_z", text="", icon=ico_value) 
                    row.prop(self, 'rotation_z', text='Z')

                    box.separator()  
                
                    if self.show_advanced == True:
                        row = box.row(align=True)
                        row.prop (self, 'rotation_offset', text = '')
               

                # SCALE #
                box.separator()   
                box = col.box().column(align=True) 
                box.separator()   

                row = box.row(align=True)
                row.prop(self, 'open_scale', text='', icon='ORIENTATION_LOCAL') 
                row.label(text='Match Scale:')
                
                sub = row.row(align=True)
                sub.alignment = 'RIGHT'        
                sub.label(text="Apply")
                sub.prop(self, 'apply_scale', text='')           

                box.separator()  

                if self.open_scale == True: 

                    if self.lock_scale_x == True and self.lock_scale_y == True and self.lock_scale_z == True:
                        ico_value = 'LOCKED'
                    else:
                        ico_value = 'UNLOCKED'

                    row = box.row(align=True)
                    row.prop(self, "lock_scale_x", text="", icon=ico_value)  
                    row.prop(self, 'scale_x', text='X')
          
                    row.prop(self, "lock_scale_y", text="", icon=ico_value)        
                    row.prop(self, 'scale_y', text='Y')
          
                    row.prop(self, "lock_scale_z", text="", icon=ico_value)          
                    row.prop(self, 'scale_z', text='Z')   
                      
                    box.separator()  

                    if self.show_advanced == True:
                        row = box.row(align=True)
                        row.prop (self, 'scale_offset', text = '')
                
               
                # DIMENSION #
                box.separator()   
                box = col.box().column(align=True) 
                box.separator()   

                row = box.row(align=True)
                row.prop(self, 'open_dimension', text='', icon='ORIENTATION_LOCAL')
                row.label(text='Fit Dimensions:')
                
                if self.open_dimension == True: 
                
                    sub = row.row(align=True)
                    sub.alignment = 'RIGHT'              
                    sub.label(text="Apply")
                    sub.prop (self, 'apply_dim', text='')
                   
                    box.separator()  

                    row = box.row(align=True)
                    row.prop (self, 'fit_x', text='X')
                    row.prop (self, 'fit_y', text='Y')
                    row.prop (self, 'fit_z', text='Z')

                box.separator()   
 

           
            if self.viewport_display == True:
                     
                box = layout.box().column(align=True) 
                 
                row = box.row(align=True)
                row.prop (self, 'show_display_name')
                row.prop (self, 'show_display_axis')
             
                box.separator()   
                
                row = box.row(align=True)
                row.prop (self, 'show_display_wire')
                row.prop (self, 'show_display_edges')
              
                box.separator()   
               
                row = box.row(align=True)
                row.prop (self, 'show_display_space')
                row.prop (self, 'show_display_shadow')
             
                box.separator()   
              
                row = box.row(align=True)
                row.prop (self, 'show_display_front')
                row.label (text=' ')
               
                box.separator()   
               
                row = box.row(align=False)
                row.prop (self, 'show_boundbox', text="Show Bounds", icon='STICKY_UVS_LOC')
                row.prop (self, "show_obj_color")               
                
                box.separator()             
               
                row = box.row(align=False)               
                row.prop (self, 'show_boundbox_type', text="")
                row.prop (self, 'show_display_type', text="")  

                box.separator()   
                
            
    def execute(self, context):
        align_function(self.used_subject, self.active_too, self.use_consistent, self.use_self_or_active, 
                       self.ref1, self.ref2,self.use_invert, self.use_invert2, self.show_boundbox, self.show_boundbox_type,
                       self.location_x_axis, self.location_y_axis, self.location_z_axis, self.location_offset,
                       self.rotation_x, self.rotation_y, self.rotation_z, self.rotation_offset, 
                       self.scale_x, self.scale_y, self.scale_z, self.scale_offset, 
                       self.fit_x, self.fit_y, self.fit_z, 
                       self.lock_location_x, self.lock_location_y, self.lock_location_z,
                       self.lock_rotation_x, self.lock_rotation_y, self.lock_rotation_z,
                       self.lock_scale_x, self.lock_scale_y, self.lock_scale_z, 
                       self.cycle_through, self.viewport_display, self.show_display_name, self.show_display_axis,
                       self.show_display_wire, self.show_display_edges, self.show_display_space, self.show_display_shadow,
                       self.show_display_front, self.show_display_type, self.show_obj_color)

                               
        return {'FINISHED'} 
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)  





# cycle through selected objects by 
class VIEW3D_OT_cycle_through(bpy.types.Operator):
    """cycle through selected objects"""
    bl_idname = "tpc_ops.cycle_through"
    bl_label = "cycle through"
    bl_options = {'INTERNAL'}

    def execute(self, context):

        view_layer = bpy.context.view_layer        
         
        selection = bpy.context.selected_objects

        if not view_layer.objects.active:
            if len(selection):
                view_layer.objects.active = selection[0]
        else:
            for i, o in enumerate(selection):
                if o == view_layer.objects.active :
                    view_layer.objects.active = selection[(i+1) % len(selection)]
                    break
        
        return {'FINISHED'}



def register():
    bpy.utils.register_class(VIEW3D_OT_cycle_through)
    bpy.utils.register_class(VIEW3D_OT_advanced_align_tools)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_cycle_through)
    bpy.utils.unregister_class(VIEW3D_OT_advanced_align_tools)

if __name__ == "__main__":
    register()
