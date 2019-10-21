# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

#bl_info = { 'name': "KTools", 'author': "Kjartan Tysdal",
#        'wiki_url': 'http://www.kjartantysdal.com/scripts',
#}

# LOAD MODUL #   
import bpy, bmesh 
from bpy import *
from bpy.props import *


#Adds Autotubes to the Addon     
class autotubes(bpy.types.Operator):
        """Creates a spline tube based on selected edges""" 
        bl_idname = "tp_ops.edgetubes"                
        bl_label = "Auto Tubes"             
        bl_options = {'REGISTER', 'UNDO'} 

        bevel = FloatProperty(name="Tube Width", description="Change width of the tube.", default=0.1, min = 0)
        res = IntProperty(name="Tube Resolution", description="Change resolution of the tube.", default=2, min = 0, max = 20)
        

        def execute(self, context):
                
                mode = bpy.context.active_object.mode
                type = bpy.context.active_object.type
                bevel = self.bevel  
                res = self.res
                

                if mode == 'EDIT' and type == 'MESH':
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        bpy.ops.object.duplicate()
                        
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.select_all(action='INVERT')
                        bpy.ops.mesh.delete(type='EDGE')
                        
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        bpy.ops.object.subdivision_set(level=0)
                        bpy.ops.object.convert(target='CURVE')
                        bpy.context.object.data.fill_mode = 'FULL'
                        bpy.context.object.data.bevel_depth = 0.1
                        bpy.context.object.data.splines[0].use_smooth = True
                        bpy.context.object.data.bevel_resolution = 2
                        bpy.ops.object.shade_smooth()
                        
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.curve.spline_type_set(type='BEZIER')
                        
                        bpy.context.object.data.bevel_depth = bevel
                        bpy.context.object.data.bevel_resolution = res
                        
                        #bpy.ops.transform.transform(('INVOKE_DEFAULT'), mode='CURVE_SHRINKFATTEN')
                        
                        
                        
                elif type == 'CURVE':
                        
                        bpy.context.object.data.bevel_depth = bevel
                        bpy.context.object.data.bevel_resolution = res
                        
                elif mode != 'EDIT' and type == 'MESH':
                        self.report({'ERROR'}, "This one only works in Edit mode")
                        return {'CANCELLED'}


                return {'FINISHED'} 

# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()










 
