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


class View3D_TP_Copy_Origin(bpy.types.Operator):
    '''Set Origin to the Origin Location of the selected Object(s)'''
    bl_idname = "tp_ops.copy_origin"
    bl_label = "Copy Origin"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):
        
        current_pivot = bpy.context.space_data.pivot_point

        if context.mode == 'OBJECT':
            bpy.ops.view3d.snap_cursor_to_active()
            bpy.context.space_data.pivot_point = 'CURSOR'
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        else:        
            bpy.ops.object.editmode_toggle()         
            bpy.ops.view3d.snap_cursor_to_active()
            bpy.context.space_data.pivot_point = 'CURSOR'
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')      
            bpy.ops.object.editmode_toggle()          
        
        bpy.context.space_data.pivot_point = current_pivot      
        return{'FINISHED'}  


class View3D_TP_Origin_EditCenter(bpy.types.Operator):
    '''Set Origin to Center / Editmode'''
    bl_idname = "tp_ops.origin_set_editcenter"
    bl_label = "Set Origin to Center / Editmode"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.mesh.select_all(action='SELECT') 
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')               
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='DESELECT') 
        
        return{'FINISHED'}  
    

class View3D_TP_OriginObm(bpy.types.Operator):
    """set origin to selected / stay in objectmode"""                 
    bl_idname = "tp_ops.origin_obm"          
    bl_label = "origin to selected / in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
    

class View3D_TP_OriginEdm(bpy.types.Operator):
    """set origin to selected / stay in editmode"""                 
    bl_idname = "tp_ops.origin_edm"          
    bl_label = "origin to selected in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class View3D_TP_Origin_Edm_Cursor(bpy.types.Operator):
    """set origin to cursor / stay in editmode"""                 
    bl_idname = "tp_ops.origin_cursor_edm"          
    bl_label = "origin to cursor in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class View3D_TP_Origin_Obm_Cursor(bpy.types.Operator):
    """set origin to cursor / stay in objectmode"""                 
    bl_idname = "tp_ops.origin_cursor_obm"          
    bl_label = "origin to cursor in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}   



class View3D_TP_Origin_Center(bpy.types.Operator):
    '''Set Origin to Center'''
    bl_idname = "tp_ops.origin_set_center"
    bl_label = "Origin to Center"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        if context.mode == 'OBJECT':

            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)                 

        else:   
            bpy.ops.object.editmode_toggle()
            
            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
            
            bpy.ops.object.editmode_toggle()

        return{'FINISHED'}


class View3D_TP_Origin_Cursor(bpy.types.Operator):
    '''Set Origin to Cursor'''
    bl_idname = "tp_ops.origin_set_cursor"
    bl_label = "Origin to Cursor"
    bl_options = {"REGISTER", 'UNDO'}   

    set_cursor = bpy.props.BoolProperty(name="Set 3D Cursor",  description="set pivot to 3d cursor", default = False)   
    
    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        
        for i in range(self.set_cursor):
        
            bpy.context.space_data.pivot_point = 'CURSOR'

        return{'FINISHED'}

 

class VIEW3D_TP_Origin_Mass(bpy.types.Operator):
    '''Set Origin to Center of Mass: (Surface) or (Volume)'''
    bl_idname = "tp_ops.origin_set_mass"
    bl_label = "Center of Mass"
    bl_options = {"REGISTER", 'UNDO'}   

    set_mass = bpy.props.EnumProperty(
      items = [("tp_ms",   "Mass (Surface)",  "Mass (Surface)",  "BLANK1", 1),
               ("tp_mv",   "Mass (Volume)",   "Mass (Volume)",   "BLANK1", 2)], 
               name = " ",
               default = "tp_ms",
               description="Set Origin to Center of Mass: (Surface) or (Volume)")
                                      

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align=True)

        box = col.box().column(1)             

        row = box.row(1)  
        row.prop(self, 'set_mass', text=" ", expand=True)

        box.separator()


    def execute(self, context):
        
        if self.set_mass == "tp_ms":
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')        
        else:        
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')

        return{'FINISHED'}



class View3D_TP_Origin_toMesh(bpy.types.Operator):
    '''Set Origin to Mesh'''
    bl_idname = "tp_ops.origin_tomesh"
    bl_label = "Origin to Mesh"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        return{'FINISHED'}    
    
    
class View3D_TP_Origin_Meshto(bpy.types.Operator):
    '''Set Mesh to Origin'''
    bl_idname = "tp_ops.origin_meshto"
    bl_label = "Mesh to Origin"
    bl_options = {"REGISTER", 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        
        return{'FINISHED'}  




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()















