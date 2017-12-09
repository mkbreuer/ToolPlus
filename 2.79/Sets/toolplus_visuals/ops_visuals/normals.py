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
#

# LOAD MODUL #
import bpy
from bpy import*
from bpy.props import *



class VIEW3D_TP_Visual_Normals(bpy.types.Operator):
    """Recalculate Normals for all selected Objects in Objectmode"""
    bl_idname = "tp_ops.rec_normals"
    bl_label = "Recalculate Normals"     

    def execute(self, context):
                
        for obj in bpy.context.selected_objects:
            bpy.context.scene.objects.active = obj 
                
            if obj:
                obj_type = obj.type

                if obj_type in {'MESH'}:                 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent()
                    bpy.ops.object.editmode_toggle()            

                    print(self)
                    self.report({'INFO'}, "Done!")      
                else:
                    print(self)
                    self.report({'INFO'}, "Not possible!")   

        return {'FINISHED'}          



class VIEW3D_TP_Visual_Curve_Shade(bpy.types.Operator):
    """Curve Shading"""
    bl_idname = "tp_ops.curve_shade"
    bl_label = "Curve Shade"     
   
    shade_mode = bpy.props.StringProperty(default="")                
      
    def execute(self, context):

        if "smooth" in self.shade_mode:  
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.shade_smooth()
            bpy.ops.object.editmode_toggle()

        if "flat" in self.shade_mode:  
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.shade_flat()
            bpy.ops.object.editmode_toggle()

        return {'FINISHED'}      


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

