# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright (C) 2017  Marvin.K.Breuer (MKB)]
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# LOCAL ORIENTATION #
import mathutils
def local_rotate(mesh, mat):
    for v in mesh.vertices:
        vec = mat * v.co
        v.co = vec
        
# OPERATOR #
class VIEW3D_TP_Copy_Transform_Local(bpy.types.Operator):
    """copy location, rotation & scale and local orientation"""
    bl_idname = "tp_ops.copy_local_transform"
    bl_label = "ReMove / ReScale"
    bl_options = {'REGISTER', 'UNDO'}

    # TRANSFORM #
    copy_loc = bpy.props.BoolProperty(name="XYZ",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_loc_x = bpy.props.BoolProperty(name="X",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_loc_y = bpy.props.BoolProperty(name="Y",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_loc_z = bpy.props.BoolProperty(name="Z",  description="set on or off", default=False, options={'SKIP_SAVE'}) 

    copy_rot = bpy.props.BoolProperty(name="XYZ",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_rot_x = bpy.props.BoolProperty(name="X",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_rot_y = bpy.props.BoolProperty(name="Y",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_rot_z = bpy.props.BoolProperty(name="Z",  description="set on or off", default=False, options={'SKIP_SAVE'}) 

    copy_scl = bpy.props.BoolProperty(name="XYZ",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_scl_x = bpy.props.BoolProperty(name="X",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_scl_y = bpy.props.BoolProperty(name="Y",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    copy_scl_z = bpy.props.BoolProperty(name="Z",  description="set on or off", default=False, options={'SKIP_SAVE'}) 

    adapt_x = bpy.props.BoolProperty(name="X",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_y = bpy.props.BoolProperty(name="Y",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_z = bpy.props.BoolProperty(name="Z",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_xy = bpy.props.BoolProperty(name="Xy",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_xz = bpy.props.BoolProperty(name="Xz",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_yx = bpy.props.BoolProperty(name="Yx",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_yz = bpy.props.BoolProperty(name="Yz",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_zx = bpy.props.BoolProperty(name="Zx",  description="set on or off", default=False, options={'SKIP_SAVE'}) 
    adapt_zy = bpy.props.BoolProperty(name="Zy",  description="set on or off", default=False, options={'SKIP_SAVE'}) 


    # ORIENTATION #
    copy_ort = bpy.props.BoolProperty(name="Local Orientation",  description="set on or off", default=False) 

    # WIDGET #
    set_widget = bpy.props.EnumProperty(
        items=[("tp_w0"    ,"None"      ,"None"   ),
               ("tp_w1"    ,"Local"     ,"Local"  ),
               ("tp_w2"    ,"Global"    ,"Global" )],
               name = "Set Widget",
               default = "tp_w0",    
               description = "widget orientation")


    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        box = layout.box().column(1)   

        if len(bpy.context.selected_objects) > 1: 

            row = box.row(1)
            row.label("Location:") 

            sub1 = row.column(1)
            display_loc = not self.copy_loc      
            sub1.prop(self, "copy_loc")        

            row = box.row(1)
            row.label(" ") 

            sub1a = row.row(1)
            sub1a.active = display_loc  
            sub1a.scale_x = 0.33
            sub1a.prop(self, "copy_loc_x")    
            sub1a.prop(self, "copy_loc_y")    
            sub1a.prop(self, "copy_loc_z")    

            box.separator() 
            box.separator() 

            row = box.row(1)
            row.label("Rotation:") 

            sub2 = row.column(1)
            display_rota = not self.copy_rot  
            sub2.prop(self, "copy_rot")        
          
            row = box.row(1)
            row.label(" ") 

            sub2a = row.row(1)
            sub2a.active = display_rota  
            sub2a.scale_x = 0.33
            sub2a.prop(self, "copy_rot_x")        
            sub2a.prop(self, "copy_rot_y")        
            sub2a.prop(self, "copy_rot_z")        

            box.separator() 
            box.separator() 

            row = box.row(1)
            row.label("Dimension:") 


            sub3 = row.column(1)
            display_scale = not self.copy_scl  
            sub3.prop(self, "copy_scl")        
     
            row = box.row(1)
            row.label(" ") 

            sub3a = row.row(1) 
            sub3a.active = display_scale  
            sub3a.scale_x = 0.33
            sub3a.prop(self, "copy_scl_x")        
            sub3a.prop(self, "copy_scl_y")        
            sub3a.prop(self, "copy_scl_z")        
     
            box.separator() 


            box = layout.box().column(1)   

            row = box.row(1)
            row.label("Orientation:") 
            row.prop(self, "copy_ort")        
        
            box.separator()  
            box.separator()  
          
            row = box.row(1)
            row.label(text="Widget:")
            row.prop(self, "set_widget", expand = True)        
           
            box.separator() 


        else:        

            row = box.row(1)
            row.label("Adapt")      
        
            row.label(" ") 

            row.prop(self, "adapt_x")  
            row.prop(self, "adapt_y")  
            row.prop(self, "adapt_z")  
         
            row = box.row(1)
            row.label("Axis") 

            sub3a = row.row(1) 
            sub3a.scale_x = 0.5
            sub3a.prop(self, "adapt_xy")        
            sub3a.prop(self, "adapt_yx")        
            sub3a.prop(self, "adapt_zx")        
            
            row = box.row(1)
            row.label(" ") 

            sub3a = row.row(1)  
            sub3a.scale_x = 0.5
            sub3a.prop(self, "adapt_xz")        
            sub3a.prop(self, "adapt_yz")        
            sub3a.prop(self, "adapt_zy")        
            
            box.separator() 



  


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        active = bpy.context.active_object
        selected = bpy.context.selected_objects

        mat_active = active.rotation_euler.to_matrix()
        mat_active.invert()  

        for obj in selected:

            # Location         
            for i in range(self.copy_loc):                                         
                obj.location = active.location            

            for i in range(self.copy_loc_x):                 
                obj.location.x = active.location.x

            for i in range(self.copy_loc_y):                 
                obj.location.y = active.location.y

            for i in range(self.copy_loc_z):                 
                obj.location.z = active.location.z                
                
           
            # Rotation
            for i in range(self.copy_rot):
                obj.rotation_euler = active.rotation_euler                

            for i in range(self.copy_rot_x):
                obj.rotation_euler.x = active.rotation_euler.x     

            for i in range(self.copy_rot_y):
                obj.rotation_euler.y = active.rotation_euler.y     
                            
            for i in range(self.copy_rot_z):
                obj.rotation_euler.z = active.rotation_euler.z     


            # Dimension
            for i in range(self.copy_scl):            
                obj.dimensions = active.dimensions

            for i in range(self.copy_scl_x):            
                obj.dimensions.x = active.dimensions.x

            for i in range(self.copy_scl_y):            
                obj.dimensions.y = active.dimensions.y
       
            for i in range(self.copy_scl_z):            
                obj.dimensions.z = active.dimensions.z

    

            # Local 
            for i in range(self.copy_ort):  
                if obj != active:
                    mat_ob = obj.rotation_euler.to_matrix()
                    if obj.type == 'MESH':                    
                        mat = mat_active * mat_ob
                        local_rotate(obj.data, mat)
                        obj.rotation_euler = active.rotation_euler 



            # Adapt Axis 0=X / 1=Y / 2=Z

            for i in range(self.adapt_x):            
                obj.dimensions[1] = active.dimensions[0]                
                bpy.ops.tp_ops.copy_local_transform(adapt_xz=True)

            for i in range(self.adapt_y):            
                obj.dimensions[0] = active.dimensions[1]                
                bpy.ops.tp_ops.copy_local_transform(adapt_yz=True)

            for i in range(self.adapt_z):            
                obj.dimensions[0] = active.dimensions[2]                
                bpy.ops.tp_ops.copy_local_transform(adapt_zy=True)


            #x-axis to y-axis  
            for i in range(self.adapt_xy):            
                obj.dimensions[1] = active.dimensions[0]
           
            #x-axis to z-axis            
            for i in range(self.adapt_xz):  
                obj.dimensions[2] = active.dimensions[0]

            #y-axis to x-axis
            for i in range(self.adapt_yx):                                
                obj.dimensions[0] = active.dimensions[1]

            #y-axis to z-axis            
            for i in range(self.adapt_yz): 
                obj.dimensions[2] = active.dimensions[1]       

            #z-axis to x-axis  
            for i in range(self.adapt_zx):            
                obj.dimensions[0] = active.dimensions[2]
                        
            #z-axis to y-axis            
            for i in range(self.adapt_zy):  
                obj.dimensions[1] = active.dimensions[2]




        # Widget
        if self.set_widget == "tp_w0":
            pass
        elif self.set_widget == "tp_w1":
            bpy.context.space_data.transform_orientation = 'LOCAL'              
        else:
            bpy.context.space_data.transform_orientation = 'GLOBAL'  

        return {'FINISHED'}

        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)




# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()






