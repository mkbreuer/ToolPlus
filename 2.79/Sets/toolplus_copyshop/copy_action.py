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
# MKB


import bpy
import math, bmesh, mathutils,re
from bpy import*
from bpy.props import *
from bpy.types import Operator, AddonPreferences

from mathutils import Vector
from math import radians


class View3D_TP_X_Array(bpy.types.Operator):
    bl_label = 'X Array'
    bl_idname = 'tp_ops.x_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 

        for obj in selected: 

            bpy.ops.object.modifier_add(type='ARRAY')      
                    
            bpy.context.object.modifiers["Array"].name = "Array X"    
            bpy.context.object.modifiers["Array X"].count = 5
            bpy.context.object.modifiers["Array X"].relative_offset_displace[0] = 1
            bpy.context.object.modifiers["Array X"].relative_offset_displace[1] = 0
            bpy.context.object.modifiers["Array X"].relative_offset_displace[2] = 0   
                
        return {'FINISHED'}


class View3D_TP_Y_Array(bpy.types.Operator):
    bl_label = 'Y Array'
    bl_idname = 'tp_ops.y_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):        
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 

        for obj in selected: 

            bpy.ops.object.modifier_add(type='ARRAY')
                    
            bpy.context.object.modifiers["Array"].name = "Array Y"                       
            bpy.context.object.modifiers["Array Y"].count = 5
            bpy.context.object.modifiers["Array Y"].relative_offset_displace[0] = 0
            bpy.context.object.modifiers["Array Y"].relative_offset_displace[1] = 1
            bpy.context.object.modifiers["Array Y"].relative_offset_displace[2] = 0
        
        return {'FINISHED'}


class View3D_TP_Z_Array(bpy.types.Operator):
    bl_label = 'Z Array'
    bl_idname = 'tp_ops.z_array'
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 

        for obj in selected: 

            bpy.ops.object.modifier_add(type='ARRAY')
    
            bpy.context.object.modifiers["Array"].name = "Array Z" 
            bpy.context.object.modifiers["Array Z"].count = 5
            bpy.context.object.modifiers["Array Z"].relative_offset_displace[0] = 0
            bpy.context.object.modifiers["Array Z"].relative_offset_displace[1] = 0
            bpy.context.object.modifiers["Array Z"].relative_offset_displace[2] = 1   
                    
        return {'FINISHED'}





class View3D_TP_Array_Empty_Add(bpy.types.Operator):
    """place a rotated empty"""                 
    bl_idname = "tp_ops.add_empty_array"          
    bl_label = "Add Empty"                 
    bl_options = {'REGISTER', 'UNDO'}   

    tp_degress = bpy.props.EnumProperty(
        items=[("tp_00"    ,"0°"    ,""),
               ("tp_15"    ,"15°"   ,""),
               ("tp_30"    ,"30°"   ,""),
               ("tp_45"    ,"45°"   ,""),
               ("tp_60"    ,"60°"   ,""),
               ("tp_90"    ,"90°"   ,"")],
               name = "Degrees",
               default = "tp_60",    
               description = "change degrees for the empty")


    def execute(self, context):

        bpy.ops.object.empty_add(type='ARROWS')
                
        if self.tp_degress == "tp_00":
            #15
            bpy.context.object.rotation_euler[2] = 0

        if self.tp_degress == "tp_15":
            #15
            bpy.context.object.rotation_euler[2] = 0.261799
       
        if self.tp_degress == "tp_30":
            #30°
            bpy.context.object.rotation_euler[2] = 0.523599
      
        if self.tp_degress == "tp_45":
            #45°
            bpy.context.object.rotation_euler[2] = 0.785398
       
        if self.tp_degress == "tp_60":
            #60°
            bpy.context.object.rotation_euler[2] = 1.0472
       
        if self.tp_degress == "tp_90":
            #90°
            bpy.context.object.rotation_euler[2] = 1.5708
            
        bpy.context.object.name = "Empty_rotated"        

        return {'FINISHED'}  
    

class View3D_TP_Array_Empty_Add_Mods(bpy.types.Operator):
    """place a Array & Curve modifier to selected object"""                 
    bl_idname = "tp_ops.add_empty_array_mods"          
    bl_label = "Empty Curve & Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    plane = bpy.props.BoolProperty(name="6 Side Plane", description="add plane for a 6 side array", default=True) 

    def execute(self, context):

        for i in range(self.plane):
            bpy.ops.object.select_pattern(pattern="Empty_rotated")
            bpy.ops.view3d.snap_cursor_to_selected()               
            bpy.ops.mesh.primitive_plane_add()
            bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
            bpy.ops.transform.translate(value=(0.866025, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            bpy.context.object.scale[1] = 0.5
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)


        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].name = "Empty Array"
        bpy.context.object.modifiers["Empty Array"].fit_type = 'FIXED_COUNT'
        bpy.context.object.modifiers["Empty Array"].count = 6
        bpy.context.object.modifiers["Empty Array"].use_relative_offset = False        
        bpy.context.object.modifiers["Empty Array"].use_object_offset = True
        bpy.context.object.modifiers["Empty Array"].offset_object = bpy.data.objects["Empty_rotated"]

     
        return {'FINISHED'}   
       


class View3D_TP_Array_Empty_Curve_Add(bpy.types.Operator):
    """place a curve for array"""                 
    bl_idname = "tp_ops.add_empty_curve"          
    bl_label = "Add Empty Curve"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        obj = context.active_object     
        if obj:
            bpy.ops.view3d.snap_cursor_to_selected()
        
        bpy.ops.curve.primitive_bezier_circle_add(radius=10)
        bpy.context.object.name = "Empty_Curve"

        return {'FINISHED'}  


class View3D_TP_Array_Empty_Curve_Add_Mods(bpy.types.Operator):
    """place a Array & Curve modifier to selected object"""                 
    bl_idname = "tp_ops.add_empty_curve_mods"          
    bl_label = "Empty Curve & Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].name = "Empty Curve Array"
        bpy.context.object.modifiers["Empty Curve Array"].fit_type = 'FIT_CURVE'
        bpy.context.object.modifiers["Empty Curve Array"].curve = bpy.data.objects["Empty_Curve"]
        bpy.context.object.modifiers["Empty Curve Array"].use_relative_offset = True
        bpy.context.object.modifiers["Empty Curve Array"].relative_offset_displace[0] = 0
        bpy.context.object.modifiers["Empty Curve Array"].relative_offset_displace[2] = 1
        bpy.context.object.modifiers["Empty Curve Array"].use_merge_vertices = True
        bpy.context.object.modifiers["Empty Curve Array"].use_merge_vertices_cap = True

        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers["Curve"].object = bpy.data.objects["Empty_Curve"]           
        bpy.context.object.modifiers["Curve"].deform_axis = 'POS_Z'
     
        return {'FINISHED'}   


class View3D_TP_Array_Circle_Add(bpy.types.Operator):
    """place a circle curve"""                 
    bl_idname = "tp_ops.add_circle_array"          
    bl_label = "Circle Curve"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        obj = context.active_object     
        if obj:
            bpy.ops.view3d.snap_cursor_to_selected()
       
        bpy.ops.curve.primitive_bezier_circle_add(radius=10)
        bpy.context.object.name = "Circle_Curve"

        return {'FINISHED'}  
    

class View3D_TP_Array_Circle_Add_Mods(bpy.types.Operator):
    """place a Array & Curve modifier to selected object"""                 
    bl_idname = "tp_ops.add_circle_array_mods"          
    bl_label = "Circle Curve & Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].name = "Circle Array"        
        bpy.context.object.modifiers["Circle Array"].fit_type = 'FIXED_COUNT'
        bpy.context.object.modifiers["Circle Array"].count = 12
        bpy.context.object.modifiers["Circle Array"].curve = bpy.data.objects["Circle_Curve"]     
        bpy.context.object.modifiers["Circle Array"].relative_offset_displace[0] = 2.61638

        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers["Curve"].object = bpy.data.objects["Circle_Curve"]        

        return {'FINISHED'}   
       

class View3D_TP_Array_Curve_Add(bpy.types.Operator):
    """place a path curve"""                 
    bl_idname = "tp_ops.add_curve_array"          
    bl_label = "Path Curve & Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        obj = context.active_object     
        if obj:
            bpy.ops.view3d.snap_cursor_to_selected()

        bpy.ops.curve.primitive_bezier_curve_add(radius=10)
        bpy.context.object.name = "Curve_Array" 
       
        return {'FINISHED'}
    

class View3D_TP_Array_Curve_Add_Mods(bpy.types.Operator):
    """place a Array & Curve modifier to selected object"""                 
    bl_idname = "tp_ops.add_curve_array_mods"          
    bl_label = "Path Curve Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].name = "Curve Array"           
        bpy.context.object.modifiers["Curve Array"].fit_type = 'FIT_CURVE'
        bpy.context.object.modifiers["Curve Array"].curve = bpy.data.objects["Curve_Array"]     
        bpy.context.object.modifiers["Curve Array"].relative_offset_displace[0] = 1
       
        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers["Curve"].object = bpy.data.objects["Curve_Array"]  

        return {'FINISHED'}         
        

class View3D_TP_FPath_Curve_Add(bpy.types.Operator):
    """place a curve for follow path"""                 
    bl_idname = "tp_ops.add_fpath_curve"          
    bl_label = "Follow Path Curve"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        obj = context.active_object     
        if obj:
            bpy.ops.view3d.snap_cursor_to_selected()
                        
        bpy.ops.curve.primitive_bezier_circle_add(radius=10)
        bpy.context.object.name = "Follow_Path_Curve"

        return {'FINISHED'}  
         

class View3D_TP_FPath_Add_Con(bpy.types.Operator):
    """place a follow path constraint"""                 
    bl_idname = "tp_ops.add_fpath_con"          
    bl_label = "Follow Path Constraint"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
     
        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
        bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["Follow_Path_Curve"]
        bpy.context.object.constraints["Follow Path"].use_curve_follow = True
        bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_X'

        return {'FINISHED'}                      

    
class View3D_TP_FPath_Linked(bpy.types.Operator):
    """linked object from constraint"""                 
    bl_idname = "tp_ops.linked_fpath"          
    bl_label = "linked object from constraint"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.object.select_linked(type='OBDATA')     
        bpy.ops.object.visual_transform_apply()
        bpy.ops.object.constraints_clear()

        return {'FINISHED'}  


class View3D_TP_FPath_Unlinked(bpy.types.Operator):
    """single objects & data from constraint"""                 
    bl_idname = "tp_ops.single_fpath"          
    bl_label = "single objects & data from constraint"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.object.select_linked(type='OBDATA')     
        bpy.ops.object.visual_transform_apply()
        bpy.ops.object.constraints_clear()
        bpy.ops.object.make_single_user(type='ALL', object=True, obdata=True)

        return {'FINISHED'}  



class View3D_TP_Copy2Cursor(bpy.types.Operator):
    """Copy selected object to cursor direction"""
    bl_idname = "tp_ops.copy_to_cursor"
    bl_label = "Copy 2 Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)


    def draw(self, context):
        layout = self.layout.column(1)
       

        box = layout.box().column(1)
        
        row = box.column(1)        
        row.prop(self, 'total', text="Steps")
        
        if context.mode == 'OBJECT':

            obj = context.active_object     
            if obj:
               obj_type = obj.type
                              
               if obj_type in {'MESH'}:            
                    row = box.row(1) 
                    row.prop(self, 'join', text="Join")
                    row.label("or")
                    row.prop(self, 'unlink', text="Unlink")


    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        for i in range(self.total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        if self.join == True:
            bpy.ops.object.select_linked(type='OBDATA') 
            bpy.ops.object.join()

        if self.unlink == True: 
            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)



class View3D_TP_Copy2Cursor_panel(bpy.types.Operator):
    """Copy selected object to cursor direction"""
    bl_idname = "tp_ops.copy_to_cursor_panel"
    bl_label = "Copy 2 Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    bpy.types.Scene.ctc_total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

    ctc_unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    ctc_join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)

    def draw(self, context):
        layout = self.layout.column(1)

        box = layout.box().column(1)
        
        row = box.column(1)        
        row.prop(self, 'ctc_join', text="Join")
        row.label("or")
        row.prop(self, 'ctc_unlink', text="Unlink")


    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        for i in range(context.scene.ctc_total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            factor = i / scene.ctc_total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        if self.ctc_join == True:
            bpy.ops.object.select_linked(type='OBDATA') 
            bpy.ops.object.join()

        if self.ctc_unlink == True: 
            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

        return {'FINISHED'}



class View3D_TP_Dupli_Set_Panel(bpy.types.Operator):
    """Duplication on active Object"""
    bl_idname = "tp_ops.dupli_set_panel"
    bl_label = "Duplication Set :)"
    bl_options = {'REGISTER', 'UNDO'}
    
    bpy.types.Scene.dupli_align = bpy.props.BoolProperty(name="Align Source",  description="Align Object Location", default=False)       
    bpy.types.Scene.dupli_single = bpy.props.BoolProperty(name="Make Real",  description="Single Dupli-Instances", default=False)    
    bpy.types.Scene.dupli_separate = bpy.props.BoolProperty(name="Separate all",  description="Separate Objects", default=False)    
    bpy.types.Scene.dupli_link = bpy.props.BoolProperty(name="Link separted",  description="Link separated Objects", default=False)    

    def draw(self, context):
        layout = self.layout.column(1)
        
        if len(bpy.context.selected_objects) == 2:   

            box = layout.box().column(1)

            row = box.row(1)         
            row.prop(context.object, "dupli_type", expand=True)

            box.separator()
            
            row = box.row(1)   
            row.prop(context.scene, 'dupli_align')       
            row.prop(context.scene, 'dupli_single')

            row = box.row(1)   
            row.prop(context.scene, 'dupli_separate')        
            row.prop(context.scene, 'dupli_link')
            
            box.separator()

            row = box.row(1)          
            box.separator()
            row.scale_x = 0.5        
            row.operator('wm.operator_defaults', text="Reset", icon ="RECOVER_AUTO")

        else:
            box = layout.box().column(1)

            row = box.row(1)  
            row.label("need a source and a target", icon ="INFO")  
            

    def execute(self, context):

        if len(bpy.context.selected_objects) == 2:

            first_obj = bpy.context.active_object

            obj_a, obj_b = context.selected_objects

            second_obj = obj_a if obj_b == first_obj else obj_b  

            for i in range(context.scene.dupli_align):             

                #copy dimensions to it
                active = bpy.context.active_object
                selected = bpy.context.selected_objects

                for obj in selected:                                        
                    obj.location = active.location
          
            bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]            
            bpy.data.objects[first_obj.name].select=True  
           
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)              

            for i in range(context.scene.dupli_single):   
                bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]            
                bpy.data.objects[first_obj.name].select=True  
               
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

                bpy.ops.object.duplicates_make_real()
                bpy.ops.object.parent_clear(type='CLEAR')

                bpy.data.objects[first_obj.name].select=False                  
                
                bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                bpy.data.objects[second_obj.name].select=True  
               
                bpy.ops.object.select_linked(type='OBDATA')
                bpy.ops.object.join()                
                
                for i in range(context.scene.dupli_separate):                
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.separate(type='LOOSE')
                    bpy.ops.object.editmode_toggle()

                    for i in range(context.scene.dupli_link):
                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY') 
                        bpy.ops.object.make_links_data(type='OBDATA')                   
        else:
            print(self)
            self.report({'INFO'}, "need a source and a target")  

        return {'FINISHED'}



class View3D_TP_DupliSet(bpy.types.Operator):
    """Duplication on active Object"""
    bl_idname = "tp_ops.dupli_set"
    bl_label = "Duplication Set :)"
    bl_options = {'REGISTER', 'UNDO'}
    
    align = bpy.props.BoolProperty(name="Align Source",  description="align selected to active location", default=False)       
    single = bpy.props.BoolProperty(name="Make Real",  description="single > remove parenting", default=False)    
    separate = bpy.props.BoolProperty(name="Separate all",  description="separate to single objects", default=False)    
    link = bpy.props.BoolProperty(name="Link separted",  description="link separated objects", default=False)    

    def draw(self, context):
        layout = self.layout.column(1)
        
        if len(bpy.context.selected_objects) == 2:   
                 
            box = layout.box().column(1)

            row = box.row(1)         
            row.prop(context.object, "dupli_type", expand=True)

            box.separator()
            
            row = box.row(1)   
            row.prop(self, 'align')       
            row.prop(self, 'single')

            row = box.row(1)   
            row.prop(self, 'separate')        
            row.prop(self, 'link')
            
            box.separator()

            row = box.row(1)          
            box.separator()
            row.scale_x = 0.5        
            row.operator('wm.operator_defaults', text="Reset", icon ="RECOVER_AUTO")

        else:
            box = layout.box().column(1)

            row = box.row(1)  
            row.label("need a source and a target", icon ="INFO")  
            

    def execute(self, context):

        if len(bpy.context.selected_objects) == 2:

            first_obj = bpy.context.active_object

            obj_a, obj_b = context.selected_objects

            second_obj = obj_a if obj_b == first_obj else obj_b  

            for i in range(self.align):  
                           
                #copy dimensions to it
                active = bpy.context.active_object
                selected = bpy.context.selected_objects

                for obj in selected:                    
                    obj.location = active.location

            bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]            
            bpy.data.objects[first_obj.name].select=True  
           
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
              

            for i in range(self.single):   
                bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]            
                bpy.data.objects[first_obj.name].select=True  
               
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

                bpy.ops.object.duplicates_make_real()
                bpy.ops.object.parent_clear(type='CLEAR')

                bpy.data.objects[first_obj.name].select=False                  
                
                bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                bpy.data.objects[second_obj.name].select=True  
               
                bpy.ops.object.select_linked(type='OBDATA')
                bpy.ops.object.join()                

                for i in range(self.separate):                
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.separate(type='LOOSE')
                    bpy.ops.object.editmode_toggle()

                    for i in range(self.link):
                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY') 
                        bpy.ops.object.make_links_data(type='OBDATA')   
                
        else:
            print(self)
            self.report({'INFO'}, "need a source and a target")  

        return {'FINISHED'}
 
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)



class View3D_TP_MakeSingle(bpy.types.Operator):
    """Make Single User for all Linked (Object Data)"""
    bl_idname = "tp_ops.make_single"
    bl_label = "Make Single"

    def execute(self, context):
        bpy.ops.object.select_linked(type='OBDATA')
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)
        return {'FINISHED'}


class View3D_TP_Help_Axis_Array(bpy.types.Operator):
	bl_idname = 'tp_help.axis_array'
	bl_label = ''

	def draw(self, context):
		layout = self.layout
		layout.label('1. Add or select a Source Object')
		layout.label('2. Press any Axis Array Button')
		layout.label('3. Open properties to make changes (Arrow Icon)')
	
	def execute(self, context):
		return {'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width = 300)  


class View3D_TP_Help_Empty_Array(bpy.types.Operator):
	bl_idname = 'tp_help.empty_array'
	bl_label = ''

	def draw(self, context):
		layout = self.layout
		layout.label('1. Add Empty Object (Icon Button)')
		layout.label('2. Add Empty Plane Object (Icon Button)')
		layout.label('3. Add the Curve (Icon Button)')
		layout.label('4. Select Empty Plane Object')
		layout.label('4. Press the Empty Array Button')
		layout.label('5. Open properties to make changes (Arrow Icon)')
	
	def execute(self, context):
		return {'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width = 300)  


class View3D_TP_Help_Curve_Array(bpy.types.Operator):
	bl_idname = 'tp_help.curve_array'
	bl_label = ''

	def draw(self, context):
		layout = self.layout
		layout.label('1. Add or select a Source Object')
		layout.label('2. Add the Curve (Icon Button)')
		layout.label('3. Select Source Object again')
		layout.label('4. Press the Array Button')
		layout.label('5. Open properties to make changes (Arrow Icon)')
	
	def execute(self, context):
		return {'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width = 300)  


class View3D_TP_Help_Follow_Path(bpy.types.Operator):
	bl_idname = 'tp_help.follow_path'
	bl_label = ''

	def draw(self, context):
		layout = self.layout
		layout.label('1. Add or select a Source Object')
		layout.label('2. Add the Curve (Icon Button)')
		layout.label('3. Select Source Object again')
		layout.label('4. Press Follow Path Button')
		layout.label('5. Move the Source to the Parent Start Point')
		layout.label('6. Activate Animate Path in the Constraint Property')
		layout.label('7. Open properties to make changes (Arrow Icon)')
		layout.label('8. It is activated when it move by scrolling the frame')
		layout.label('9. Choose Type and Count for Array > Evenly Spaced, etc.')
		layout.label('10. Press: Set FPath Array')
	
	def execute(self, context):
		return {'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width = 300)      
	
	

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()









