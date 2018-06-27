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

# LOAD CACHE #
from .caches.cache      import  (toc_settings_load)
from .caches.cache      import  (toc_settings_write)

# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import *


# OPERATOR # 
def draw_operator(self, context):
    scene = context.scene
    cursor = scene.cursor_location
    obj = scene.objects.active

    # check for 3d editor
    view = context.space_data
    if view.type == 'VIEW_3D':
        rv3d = view.region_3d
        # store cursor position        
        current_pos = view.cursor_location.xyz

        if self.transform_cursor == True:
            view.cursor_location[0] = self.cursor_x
            view.cursor_location[1] = self.cursor_y
            view.cursor_location[2] = self.cursor_z
        else:
            # reload cursor position  
            view.cursor_location.xyz = current_pos       


    if context.mode =='OBJECT':

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

    else:

        if context.mode == 'EDIT_MESH':
            bpy.ops.mesh.separate(type='SELECTED')  

        if context.mode == 'EDIT_CURVE':
            bpy.ops.curve.separate()
   
        if context.mode == 'EDIT_SURFACE':
            bpy.ops.curve.separate()

        bpy.ops.object.editmode_toggle()

        first_obj = bpy.context.active_object
        obj_a, obj_b = context.selected_objects
        second_obj = obj_a if obj_b == first_obj else obj_b  
       
        # active: second
        bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
        bpy.data.objects[second_obj.name].select=True  
        
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        obj = scene.objects.active
        for i in range(self.total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            # custom transform        
            if self.transform_copies == True:

                obj.delta_location[0] += self.distance[0]
                obj.delta_location[1] += self.distance[1]
                obj.delta_location[2] += self.distance[2]
                
                obj.delta_rotation_euler.x += self.rotation[0]
                obj.delta_rotation_euler.y += self.rotation[1]
                obj.delta_rotation_euler.z += self.rotation[2]
                
                obj.delta_scale[0] += self.scale[0]
                obj.delta_scale[1] += self.scale[1]
                obj.delta_scale[2] += self.scale[2]

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        bpy.ops.object.select_linked(type='OBDATA') 
        bpy.ops.object.join()

        # active: first                
        bpy.context.scene.objects.active = bpy.data.objects[first_obj.name] 
        bpy.data.objects[first_obj.name].select = True    
        bpy.data.objects[second_obj.name].select=True      

        bpy.ops.object.join()

        bpy.ops.object.editmode_toggle()

    return {'FINISHED'}

    
# DRAW PROPS [F6] # 
def draw_props(self, context):
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

    box.separator()      

    row = box.row(1)
    row.prop(self, "transform_cursor")         
       
    if self.transform_cursor == True:

        row = box.column(1)        
        row.prop(self, "cursor_x") 
        row.prop(self, "cursor_y")               
        row.prop(self, "cursor_z") 

    box.separator()   

    row = box.row(1)
    row.prop(self, "transform_copies")         
       
    if self.transform_copies == True:

        row = box.column(1)        
        row.prop(self, "distance") 
        
        row = box.column(1)  
        row.prop(self, "rotation")               
        
        row = box.column(1)  
        row.prop(self, "scale") 

    box.separator()   



class View3D_TP_Copy2Cursor(bpy.types.Operator):
    """Copy selected object to cursor direction"""
    bl_idname = "tp_ops.copy_to_cursor"
    bl_label = "Copy 2 Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)

    # TRANSFORM CURSOR #
    transform_cursor = bpy.props.BoolProperty(name="Use Cursor Transform", description ="!destructive: loss of first cursor position" , default = False)

    cursor_x = bpy.props.FloatProperty(name="Cursor X",  description=" ", default=0.0, min=-1000, max=1000)
    cursor_y = bpy.props.FloatProperty(name="Cursor Y",  description=" ", default=0.0, min=-1000, max=1000)
    cursor_z = bpy.props.FloatProperty(name="Cursor Z",  description=" ", default=0.0, min=-1000, max=1000)

    # TRANSFORM COPIES #
    transform_copies = bpy.props.BoolProperty(name="Use Copy Transform", description ="" , default = False)

    distance = bpy.props.FloatVectorProperty(name="Distance", description="Distance between the elements in BUs", default = (0.0, 0.0, 0.0))    
    rotation = bpy.props.FloatVectorProperty(name="Rotation", description="Delta rotation of the elements in radians", default = (0.0, 0.0, 0.0))
    scale = bpy.props.FloatVectorProperty(name="Scale", description="Delta scale of the elements in BUs", default = (0.0, 0.0, 0.0))


    # DRAW PROPS [F6] # 
    def draw(self, context):
        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        toc_settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        toc_settings_write(self)
        
        draw_operator(self, context)
            
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)   



class View3D_TP_Copy2Cursor_panel(bpy.types.Operator):
    """Copy selected object to cursor direction"""
    bl_idname = "tp_ops.copy_to_cursor_panel"
    bl_label = "Copy 2 Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)

    # TRANSFORM CURSOR #
    transform_cursor = bpy.props.BoolProperty(name="Use Cursor Transform", description ="!destructive: loss of first cursor position" , default = False)

    cursor_x = bpy.props.FloatProperty(name="Cursor X",  description=" ", default=0.0, min=-1000, max=1000)
    cursor_y = bpy.props.FloatProperty(name="Cursor Y",  description=" ", default=0.0, min=-1000, max=1000)
    cursor_z = bpy.props.FloatProperty(name="Cursor Z",  description=" ", default=0.0, min=-1000, max=1000)

    # TRANSFORM COPIES #
    transform_copies = bpy.props.BoolProperty(name="Use Copy Transform", description ="" , default = False)

    distance = bpy.props.FloatVectorProperty(name="Distance", description="Distance between the elements in BUs", default = (0.0, 0.0, 0.0))    
    rotation = bpy.props.FloatVectorProperty(name="Rotation", description="Delta rotation of the elements in radians", default = (0.0, 0.0, 0.0))
    scale = bpy.props.FloatVectorProperty(name="Scale", description="Delta scale of the elements in BUs", default = (0.0, 0.0, 0.0))


    # DRAW PROPS [F6] # 
    def draw(self, context):
        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        toc_settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        toc_settings_write(self)
        
        draw_operator(self, context)
            
        return {'FINISHED'}




# PROPERTY GROUP: COPY TO CURSOR #
class ToCursor_Properties(bpy.types.PropertyGroup):
    
    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)

    # TRANSFORM CURSOR #
    transform_cursor = bpy.props.BoolProperty(name="Use Cursor Transform", description ="!destructive: loss of first cursor position" , default = False)

    cursor_x = bpy.props.FloatProperty(name="Cursor X",  description=" ", default=0.0, min=-1000, max=1000)
    cursor_y = bpy.props.FloatProperty(name="Cursor Y",  description=" ", default=0.0, min=-1000, max=1000)
    cursor_z = bpy.props.FloatProperty(name="Cursor Z",  description=" ", default=0.0, min=-1000, max=1000)

    # TRANSFORM COPIES #
    transform_copies = bpy.props.BoolProperty(name="Use Copy Transform", description ="" , default = False)

    distance = bpy.props.FloatVectorProperty(name="Distance", description="Distance between the elements in BUs", default = (0.0, 0.0, 0.0))    
    rotation = bpy.props.FloatVectorProperty(name="Rotation", description="Delta rotation of the elements in radians", default = (0.0, 0.0, 0.0))
    scale = bpy.props.FloatVectorProperty(name="Scale", description="Delta scale of the elements in BUs", default = (0.0, 0.0, 0.0))


# REGISTRY #
def register():
    bpy.utils.register_module(__name__)
 
    # PROPS TO CURSOR # 
    bpy.types.WindowManager.tocursor_props = PointerProperty(type = ToCursor_Properties)

def unregister():
    bpy.utils.unregister_module(__name__)

    # PROPS TO CURSOR # 
    del bpy.types.WindowManager.tocursor_props

if __name__ == "__main__":
    register()
        
        
