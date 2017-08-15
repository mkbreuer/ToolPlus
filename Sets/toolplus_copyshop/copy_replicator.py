# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****
  
import bpy
import math

# bl_info is a dictionary containing addon meta-data such as the title, version and author to be displayed in the user preferences addon list.
#bl_info = {
 #   "name": "ARewO",
  #  "author": "Frederik Steinmetz & Gottfried Hofmann",
   # "version": (0, 3),
    #"blender": (2, 66, 0),
    #"location": "SpaceBar Search -> ARewO",
    #"description": "Animation replicator with offset",
    #"category": "",}


# time_start = time.time()
# offset_extra = 0
# replicat = bpy.context.active_object


class SimpleARewO(bpy.types.Operator):
    """replicator with optionsetting"""     
    bl_idname = "object.simplearewo"        
    bl_label = "ARewO"         
    bl_options = {'REGISTER', 'UNDO'}  
    

    loops = bpy.props.IntProperty(name="Replications", description="How many?", default=1, min=1, soft_max=1000, step=1)
    
    offset = bpy.props.FloatProperty(name="Offset", description="Offset of the animations in frames", default = 10.0, soft_max=1000.0, soft_min=-1000.0, step=1.0)
    
    distance = bpy.props.FloatVectorProperty(name="Distance", description="Distance between the elements in BUs", default = (0.1, 0.0, 0.0))
    
    rotation = bpy.props.FloatVectorProperty(name="Rotation", description="Delta rotation of the elements in radians", default = (0.0, 0.0, 0.0))

    scale = bpy.props.FloatVectorProperty(name="Scale", description="Delta scale of the elements in BUs", default = (0.0, 0.0, 0.0))

    def execute(self, context):
        
        #the actual script
        for i in range(self.loops):
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False})
            obj = bpy.context.active_object
            
            obj.delta_location[0] += self.distance[0]
            obj.delta_location[1] += self.distance[1]
            obj.delta_location[2] += self.distance[2]
            
            obj.delta_rotation_euler.x += self.rotation[0]
            obj.delta_rotation_euler.y += self.rotation[1]
            obj.delta_rotation_euler.z += self.rotation[2]
            
            obj.delta_scale[0] += self.scale[0]
            obj.delta_scale[1] += self.scale[1]
            obj.delta_scale[2] += self.scale[2]
            

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)     


