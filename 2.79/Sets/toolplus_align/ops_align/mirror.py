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


import bpy
from bpy import*



class View3D_TP_Mirror_over_Edge(bpy.types.Operator):
    """mirror over active edge / normal Y axis"""                 
    bl_idname = "tp_ops.mirror_over_edge"          
    bl_label = "mirror over active edge"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        bpy.context.space_data.transform_orientation = 'NORMAL'
        bpy.ops.transform.mirror(constraint_axis=(False, True, False))
        bpy.context.space_data.transform_orientation = 'GLOBAL'
        #bpy.ops.view3d.pivot_bounding_box()
        bpy.ops.mesh.normals_make_consistent()
       
        return {'FINISHED'}

       
#####  Mirror XYZ Local  ##########

class View3D_TP_Mirror4(bpy.types.Operator):
    """mirror over X axis / local"""                 
    bl_idname = "tp_ops.mirror4"          
    bl_label = "mirror selected on X axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='LOCAL')
       
        return {'FINISHED'}
        

class View3D_TP_Mirror5(bpy.types.Operator):
    """mirror over Y axis / local"""                
    bl_idname = "tp_ops.mirror5"         
    bl_label = "mirror selected on Y axis > local"                 
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, True, False), constraint_orientation='LOCAL')
        
        return {'FINISHED'}        


class View3D_TP_Mirror6(bpy.types.Operator):
    """mirror over Z axis / local"""                 
    bl_idname = "tp_ops.mirror6"        
    bl_label = "mirror selected on Z axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, False, True), constraint_orientation='LOCAL')
        
        return {'FINISHED'}



#####  Mirror XYZ Global  #########

class View3D_TP_Mirror1(bpy.types.Operator):
    """mirror over X axis / global"""                 
    bl_idname = "tp_ops.mirror1"          
    bl_label = "mirror selected on X axis"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(True, False, False))
       
        return {'FINISHED'}


class View3D_TP_Mirror2(bpy.types.Operator):
    """mirror over Y axis / global"""                
    bl_idname = "tp_ops.mirror2"         
    bl_label = "mirror selected on Y axis"                 
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(False, True, False))
        
        return {'FINISHED'}
       

class View3D_TP_Mirror3(bpy.types.Operator):
    """mirror over Z axis / global"""                 
    bl_idname = "tp_ops.mirror3"        
    bl_label = "mirror selected on Z axis"                  
    bl_options = {'REGISTER', 'UNDO'}  
        
    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(False, False, True))
        
        return {'FINISHED'}
    



def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__) 

if __name__ == "__main__":
    register()
