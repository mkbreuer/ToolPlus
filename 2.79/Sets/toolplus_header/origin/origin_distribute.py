# ##### BEGIN GPL LICENSE BLOCK #####
#
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
# https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation
# based on distribute objects by Oscurart and CodemanX


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from mathutils import Vector


class VIEW3D_TP_Distribute_Objects(bpy.types.Operator):
    """Space Objects between there Origins"""
    bl_idname = "tp_ops.distribute_objects"
    bl_label = "Distribute Objects"       
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}   

    Boolx = bpy.props.BoolProperty(name="X")
    Booly = bpy.props.BoolProperty(name="Y")
    Boolz = bpy.props.BoolProperty(name="Z")
    Invert = bpy.props.BoolProperty(name="I", default =False)

    use_axis = bpy.props.EnumProperty(
        items=[("axis_x"   ,"X"   ,"distribute X axis"),
               ("axis_y"   ,"Y"   ,"distribute Y axis"),
               ("axis_z"   ,"Z"   ,"distribute Z axis"),
               ("axis_xy"  ,"XY"  ,"distribute XY axis"),
               ("axis_yz"  ,"YZ"  ,"distribute YZ axis"),
               ("axis_xz"  ,"XZ"  ,"distribute XZ axis"),
               ("axis_xyz" ,"XYZ" ,"distribute XYZ axis")],
               name = "Axis",
               default = "axis_x")
    
    tp_offset = FloatVectorProperty(name="Offset", description="offset", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)


    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(1)              
        box.separator() 
        
        row = box.row(1) 
        row.prop(self, 'Boolx') 
        row.prop(self, 'Booly') 
        row.prop(self, 'Boolz') 
        row.prop(self, 'Invert', text="", icon="FILE_REFRESH") 

        box.separator() 
        
        row = box.row(1) 
        row.prop(self, 'tp_offset', text="") 

        box.separator()


    def execute(self, context):

        if len(bpy.context.selected_objects) <= 1:
        
            print(self)
            self.report({'INFO'}, "Select more!")  

        else:

            #bpy.context.selected_objects     # = all selected object
            #bpy.context.selected_objects[:]  # = [:] every selected object 
            #bpy.context.selected_objects[0]  # = first selected object
            #bpy.context.selected_objects[1]  # = second selected object
            #bpy.context.selected_objects[-1] # = last selected object
            
            if self.Invert == False: 

                dif = bpy.context.selected_objects[-1].location - bpy.context.selected_objects[0].location + self.tp_offset

                chunk_global = dif/(len(bpy.context.selected_objects[:])-1)
                
                chunk_x = 0
                chunk_y = 0
                chunk_z = 0
                
                delta_fst = bpy.context.selected_objects[0].location


            else:
                dif = bpy.context.selected_objects[0].location - bpy.context.selected_objects[-1].location + self.tp_offset*-1
                         
                chunk_global = dif/(len(bpy.context.selected_objects[:])-1)
                
                chunk_x = 0
                chunk_y = 0
                chunk_z = 0
                
                delta_fst = bpy.context.selected_objects[-1].location      
                            
            for obj in bpy.context.selected_objects:    
                      
                if self.use_axis == 'axis_x' or self.Boolx == True:  
                    obj.location.x  = delta_fst[0] + chunk_x 
               
                if self.use_axis == 'axis_y' or self.Booly == True: 
                    obj.location[1] = delta_fst[1] + chunk_y
                
                if self.use_axis == 'axis_z' or self.Boolz == True:
                    obj.location.z  = delta_fst[2] + chunk_z
     
                if self.use_axis == 'axis_xy':  
                    obj.location.x  = delta_fst[0] + chunk_x
                    obj.location[1] = delta_fst[1] + chunk_y           
         
                if self.use_axis == 'axis_yz': 
                    obj.location[1] = delta_fst[1] + chunk_y
                    obj.location.z  = delta_fst[2] + chunk_z               
                
                if self.use_axis == 'axis_xz':
                    obj.location.x  = delta_fst[0] + chunk_x
                    obj.location.z  = delta_fst[2] + chunk_z 
     
                if self.use_axis == 'axis_xyz':
                    obj.location.x  = delta_fst[0] + chunk_x
                    obj.location[1] = delta_fst[1] + chunk_y  
                    obj.location.z  = delta_fst[2] + chunk_z            
              
                chunk_x += chunk_global[0] 
                chunk_y += chunk_global[1]
                chunk_z += chunk_global[2]

        return {'FINISHED'}




class VIEW3D_TP_Distribute_Objects_Menu(bpy.types.Operator):
    """Space Objects between there Origins"""
    bl_idname = "tp_ops.distribute_objects_menu"
    bl_label = "Distribute Objects"       
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}   

    Boolx = bpy.props.BoolProperty(name="X", default =False)
    Booly = bpy.props.BoolProperty(name="Y", default =False)
    Boolz = bpy.props.BoolProperty(name="Z", default =False)
    Invert = bpy.props.BoolProperty(name="I", default =False)

    use_axis = bpy.props.EnumProperty(
        items=[("axis_x"   ,"X"   ,"distribute X axis"),
               ("axis_y"   ,"Y"   ,"distribute Y axis"),
               ("axis_z"   ,"Z"   ,"distribute Z axis"),
               ("axis_xy"  ,"XY"  ,"distribute XY axis"),
               ("axis_yz"  ,"YZ"  ,"distribute YZ axis"),
               ("axis_xz"  ,"XZ"  ,"distribute XZ axis"),
               ("axis_xyz" ,"XYZ" ,"distribute XYZ axis")],
               name = "Axis",
               default = "axis_x")
    
    tp_offset = FloatVectorProperty(name="Offset", description="offset", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)


    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(1)              
        box.separator() 
        
        row = box.row(1) 
        row.prop(self, 'Boolx') 
        row.prop(self, 'Booly') 
        row.prop(self, 'Boolz') 
        row.prop(self, 'Invert', text="", icon="FILE_REFRESH") 

        box.separator() 
        
        row = box.row(1) 
        row.prop(self, 'tp_offset', text="") 

        box.separator()


    def execute(self, context):

        bpy.ops.tp_ops.distribute_objects(Boolx=self.Boolx, Booly=self.Booly, Boolz=self.Boolz, Invert=self.Invert, tp_offset=self.tp_offset)

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

