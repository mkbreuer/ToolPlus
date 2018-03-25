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


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


# LISTS FOR SELECTED & DUPLICATIONS #
first_list = []
second_list = []


# only available when align advance is disabled
# How to run this for multi objects in a simple way?

# create empty to repair apply transform
def create_empty_object(context, self):
        
    c3d = context.space_data
    active = bpy.context.active_object  
    selected = bpy.context.selected_objects

    for obj in selected:  
 
        if self.tp_axis_active == "tp_x":  
            
            # SET CURSOR #                   
            
            if self.tp_distance_active == "tp_min":              
                
                x_axis = active.location.x - active.dimensions.x/4                  

            if self.tp_distance_active == "tp_mid":   
                x_axis = active.location.x
  
            if self.tp_distance_active == "tp_max":                
                x_axis = active.location.x + active.dimensions.x/4

            y_axis = obj.location.y 
            z_axis = obj.location.z 
          
            c3d.cursor_location = (x_axis, y_axis, z_axis)
        
          
            # SET ORIGIN #
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')


        if self.tp_axis_active == "tp_y":  

            # SET CURSOR #                   
            
            if self.tp_distance_active == "tp_min": 
                y_axis = active.location.y - active.dimensions.y/4                  
            
            if self.tp_distance_active == "tp_mid": 
                y_axis = active.location.y
            
            if self.tp_distance_active == "tp_max": 
                y_axis = active.location.y + active.dimensions.y/4

            x_axis = obj.location.x 
            z_axis = obj.location.z 
          
            c3d.cursor_location = (x_axis, y_axis, z_axis)                  
          
            # SET ORIGIN #

            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
              

        if self.tp_axis_active == "tp_z":  
                     
            # SET CURSOR #                   
            
            if self.tp_distance_active == "tp_min": 
                z_axis = active.location.z - active.dimensions.z/4                  
            
            if self.tp_distance_active == "tp_mid": 
                z_axis = active.location.z
            
            if self.tp_distance_active == "tp_max": 
                z_axis = active.location.z + active.dimensions.z/4

            x_axis = obj.location.x 
            y_axis = obj.location.y 
          
            c3d.cursor_location = (x_axis, y_axis, z_axis)                  
          
            # SET ORIGIN #

            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')


        if self.tp_axis_active == "tp_a": 
                     
            # SET CURSOR #       
            x_axis = active.location.x 
            y_axis = active.location.y 
            z_axis = active.location.z 

            c3d.cursor_location = (x_axis, y_axis, z_axis)
          
            # SET ORIGIN #
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    return self    



class View3D_TP_Zero_Origin_to_Active(bpy.types.Operator):
    """align origin to active object"""                 
    bl_idname = "tp_ops.origin_to_active"          
    bl_label = "Origin to Active"                 
    bl_options = {'REGISTER', 'UNDO'}   


    tp_axis_active = bpy.props.EnumProperty(
        items=[("tp_x"    ,"X"    ,"01"),
               ("tp_y"    ,"Y"    ,"02"),
               ("tp_z"    ,"Z"    ,"03"),
               ("tp_a"    ,"XYZ"  ,"04")],
               name = "Align to Active",
               default = "tp_x",    
               description = "zero target to choosen axis")

    tp_distance_active = bpy.props.EnumProperty(
        items=[("tp_min"    ,"Min"    ,"01"),
               ("tp_mid"    ,"Mid"    ,"02"),
               ("tp_max"    ,"Max"    ,"03")],
               name = "Align Distance",
               default = "tp_mid",    
               description = "align distance for origin")


    active_too = bpy.props.BoolProperty(name="Active too!",  description="align origin to active object", default=False, options={'SKIP_SAVE'})    


    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        box.separator()

        row = box.row(1)
        row.prop(self, 'tp_axis_active', expand=True)
    
        box.separator()
     
        row = box.row(1)
        
        if self.active_too == True:
            row.prop(self, 'active_too', text="Act", icon="LAYER_ACTIVE")
        else:
            row.prop(self, 'active_too', text="Act", icon="LAYER_USED")
 
        row.prop(self, 'tp_distance_active', expand=True)
        
        box.separator()
        


    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)


    def execute(self, context):

        settings_write(self) 

        selected = bpy.context.selected_objects
        n = len(selected)
        if n == 2:
        #if n > 0:

            c3d = context.space_data
            if c3d.type == 'VIEW_3D':

                bpy.ops.view3d.snap_cursor_to_active()

                rc3d = c3d.region_3d
                current_cloc = c3d.cursor_location.xyz # store cursor

                first_obj = bpy.context.active_object
                
                # switch only between two selected objects
                obj_a, obj_b = context.selected_objects                 
                second_obj = obj_a if obj_b == first_obj else obj_b 

                # align origin to selected active axis
                create_empty_object(context, self)             

                #for i in range(self.active_too):
                if self.active_too == True:
                    pass
                else:                 
                    # select objects in lists and set origin of active back
                    c3d.cursor_location = current_cloc # reload cursor
                    bpy.ops.object.select_all(action='DESELECT')
                                             
                    # set active: first_obj                
                    bpy.context.scene.objects.active = bpy.data.objects[first_obj.name] 
                    bpy.data.objects[first_obj.name].select = True                     
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')   
              


                bpy.ops.object.select_all(action='DESELECT')
     
                # set active: second_obj
                bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                bpy.data.objects[second_obj.name].select=True   
                bpy.ops.view3d.snap_cursor_to_active()

        else:
            self.report({'INFO'}, "Select 2!")

        
        return {'FINISHED'}


#    def invoke(self, context, event):
#        dpi_value = bpy.context.user_preferences.system.dpi        
#        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)

        

# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    tp = bpy.context.window_manager.tp_props_origin
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp, key))



# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    tp = bpy.context.window_manager.tp_props_origin
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp, key, getattr(self, key))
 
          
              
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()