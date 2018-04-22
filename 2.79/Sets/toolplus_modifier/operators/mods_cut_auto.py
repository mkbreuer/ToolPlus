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
from mathutils import Vector

bpy.types.Scene.AutoCut_axis = bpy.props.EnumProperty(items = [("x",   "X",   "", 1), ("y",   "Y",   "", 2), ("z",   "Z",   "", 3)], description="Axis used by the mirror modifier")
bpy.types.Scene.AutoCut_orientation = bpy.props.EnumProperty(items = [("positive", "Positive", "", 1),("negative", "Negative", "", 2)], description="Choose the side along the axis of the editable part (+/- coordinates)")
bpy.types.Scene.AutoCut_cut = bpy.props.BoolProperty(default= True, description="If enabeled, cut the mesh in two parts and mirror it. If not, just make a loopcut")
bpy.types.Scene.tp_edit = bpy.props.BoolProperty(name="Switch Mode", description="Switch Mode", default=False)     
 
class View3D_TP_Align_Vertices(bpy.types.Operator):
    """Align Vertices on 1 Axis"""
    bl_idname = "tp_ops.align_vertices"
    bl_label = "Align Vertices on 1 Axis"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        x1,y1,z1 = bpy.context.scene.cursor_location
        bpy.ops.view3d.snap_cursor_to_selected()

        x2,y2,z2 = bpy.context.scene.cursor_location

        bpy.context.scene.cursor_location[0],bpy.context.scene.cursor_location[1],bpy.context.scene.cursor_location[2]  = 0,0,0

        #Vertices coordinate to 0 (local coordinate, so on the origin)
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if bpy.context.scene.AutoCut_axis == 'x':
                    axis = 0
                elif bpy.context.scene.AutoCut_axis == 'y':
                    axis = 1
                elif bpy.context.scene.AutoCut_axis == 'z':
                    axis = 2
                vert.co[axis] = 0
        
        bpy.context.scene.cursor_location = x2,y2,z2

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        bpy.context.scene.cursor_location = x1,y1,z1

        return {'FINISHED'}


   
class View3D_TP_AutoCut(bpy.types.Operator):
    """ Automatically cut an object along an axis """
    bl_idname = "tp_ops.autocut"
    bl_label = "AutoCut"
    bl_options = {'REGISTER'} # 'UNDO' ?

    @classmethod
    def poll(cls, context):
        return True
            
    def get_local_axis_vector(self, context, X, Y, Z, orientation):
        loc = context.object.location
        bpy.ops.object.mode_set(mode="OBJECT") # Needed to avoid to translate vertices
        
        v1 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(X*orientation, Y*orientation, Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        v2 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(-X*orientation, -Y*orientation, -Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        
        bpy.ops.object.mode_set(mode="EDIT")
        return v2-v1
    
    def execute(self, context):
        X,Y,Z = 0,0,0
        if bpy.context.scene.AutoCut_axis == 'x':
            X = 1
        elif bpy.context.scene.AutoCut_axis == 'y':
            Y = 1
        elif bpy.context.scene.AutoCut_axis == 'z':
            Z = 1
            
        bpy.ops.object.mode_set(mode="EDIT") # Go to edit mode
        
        bpy.ops.mesh.select_all(action='SELECT') # Select all the vertices
        
        if bpy.context.scene.AutoCut_orientation == 'positive':
            orientation = 1
        else:
            orientation = -1
            
        cut_normal = self.get_local_axis_vector(context, X, Y, Z, orientation)
            
        bpy.ops.mesh.bisect(plane_co=(bpy.context.object.location[0], bpy.context.object.location[1], bpy.context.object.location[2]), plane_no=cut_normal, use_fill= False, clear_inner= bpy.context.scene.AutoCut_cut, clear_outer= 0) # Cut the mesh
        
        bpy.ops.tp_ops.align_vertices() # Use to align the vertices on the origin

        return {'FINISHED'}

   


class VIEW3D_TP_Negativ_X_cut_obm(bpy.types.Operator):
    """cut object and delete negative X"""
    bl_idname = "tp_ops.mods_negativ_x_cut_obm"
    bl_label = "Cut -X"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


class VIEW3D_TP_Positiv_X_cut_obm(bpy.types.Operator):
    """cut object and delete positiv X"""
    bl_idname = "tp_ops.mods_positiv_x_cut_obm"
    bl_label = "Cut +X"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


class VIEW3D_TP_Negativ_Y_cut_obm(bpy.types.Operator):
    """cut object and delete negative Y"""
    bl_idname = "tp_ops.mods_negativ_y_cut_obm"
    bl_label = "Cut -Y"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


class VIEW3D_TP_Positiv_Y_cut_obm(bpy.types.Operator):
    """cut object and delete positiv Y"""
    bl_idname = "tp_ops.mods_positiv_y_cut_obm"
    bl_label = "Cut +Y"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


class VIEW3D_TP_Negativ_Z_cut_obm(bpy.types.Operator):
    """cut object and delete negative Z"""
    bl_idname = "tp_ops.mods_negativ_z_cut_obm"
    bl_label = "Cut -Z"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


class VIEW3D_TP_Positiv_Z_cut_obm(bpy.types.Operator):
    """cut object and delete positiv Z"""
    bl_idname = "tp_ops.mods_positiv_z_cut_obm"
    bl_label = "Cut +Z"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}



class VIEW3D_TP_Negativ_X_cut_obm(bpy.types.Operator):
    """cut object and delete negative X"""
    bl_idname = "tp_ops.mods_negativ_x_cut_obm"
    bl_label = "Cut -X"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
          
        return {'FINISHED'}


class VIEW3D_TP_Positiv_X_Cut_obm(bpy.types.Operator):
    """cut object on the positiv X-Ais"""
    bl_idname = "tp_ops.mods_positiv_x_cut_obm"
    bl_label = "Cut +X"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
        
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()                
                 
        return {'FINISHED'}


class VIEW3D_TP_Negativ_Y_Cut_obm(bpy.types.Operator):
    """cut object and delete negative Y"""
    bl_idname = "tp_ops.mods_negativ_y_cut_obm"
    bl_label = "Cut -Y"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
                  
        return {'FINISHED'}


class VIEW3D_TP_Positiv_Y_Cut_obm(bpy.types.Operator):
    """cut object and delete positiv Y"""
    bl_idname = "tp_ops.mods_positiv_y_cut_obm"
    bl_label = "Cut +Y"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')
    
    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
         
        return {'FINISHED'}


class VIEW3D_TP_Negativ_Z_Cut_obm(bpy.types.Operator):
    """cut object and delete positive Z"""
    bl_idname = "tp_ops.mods_negativ_z_cut_obm"
    bl_label = "Cut -Z"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()
        bpy.ops.object.modifier_remove(modifier="Mirror")

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


class VIEW3D_TP_PositivZ_Cut_obm(bpy.types.Operator):
    """cut object and delete positive Z  """
    bl_idname = "tp_ops.mods_positiv_z_cut_obm"
    bl_label = "Cut +Z"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()
        bpy.ops.object.modifier_remove(modifier="Mirror")  

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}




class VIEW3D_TP_Positiv_XY_Cut_obm(bpy.types.Operator):
    """cut object and delete positive XY  """
    bl_idname = "tp_ops.mods_positiv_xy_cut_obm"
    bl_label = "Cut +XY"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()            

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}



class VIEW3D_TP_Positiv_XZ_Cut_obm(bpy.types.Operator):
    """cut object and delete positive XZ  """
    bl_idname = "tp_ops.mods_positiv_xz_cut_obm"
    bl_label = "Cut +XZ"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()     
        
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}


    


class VIEW3D_TP_Positiv_YZ_Cut_obm(bpy.types.Operator):
    """cut object and delete positive YZ  """
    bl_idname = "tp_ops.mods_positiv_yz_cut_obm"
    bl_label = "Cut +YZ"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 

        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()            
        
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()         

        return {'FINISHED'}



class VIEW3D_TP_Positiv_XYZ_Cut_obm(bpy.types.Operator):
    """cut object and delete positive XYZ  """
    bl_idname = "tp_ops.mods_positiv_xyz_cut_obm"
    bl_label = "Cut +XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()            
        
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'negative'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        

        return {'FINISHED'}



class VIEW3D_TP_Negativ_XY_Cut_obm(bpy.types.Operator):
    """cut object and delete negativ XY"""
    bl_idname = "tp_ops.mods_negativ_xy_cut_obm"
    bl_label = "Cut -XY"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()            

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
                  
        return {'FINISHED'}




class VIEW3D_TP_Negativ_XZ_Cut_obm(bpy.types.Operator):
    """cut object and delete negativ XZ"""
    bl_idname = "tp_ops.mods_negativ_xz_cut_obm"
    bl_label = "Cut -XZ"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()


        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
                  
        return {'FINISHED'}




class VIEW3D_TP_Negativ_YZ_Cut_obm(bpy.types.Operator):
    """cut object and delete negativ YZ"""
    bl_idname = "tp_ops.mods_negativ_yz_cut_obm"
    bl_label = "Cut -YZ"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 

        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()            
        
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
                  
        return {'FINISHED'}




class VIEW3D_TP_Negativ_XYZ_Cut_obm(bpy.types.Operator):
    """cut object and delete negativ XYZ"""
    bl_idname = "tp_ops.mods_negativ_xyz_cut_obm"
    bl_label = "Cut -XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    edit = bpy.props.BoolProperty(name="Switch Mode",  description="Switch Mode", default=True) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'edit')

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.AutoCut_axis = 'x'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()

        bpy.context.scene.AutoCut_axis = 'y'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()            
        
        bpy.context.scene.AutoCut_axis = 'z'
        bpy.context.scene.AutoCut_orientation = 'positive'
        bpy.ops.tp_ops.autocut()
        
        obj = bpy.context.active_object
        obj.modifiers.clear()

        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()        
                  
        return {'FINISHED'}


    
class VIEW3D_TP_Boolean_Normal_Cut(bpy.types.Operator):
    """cut object at seleted normal"""
    bl_idname = "tp_ops.normal_cut"
    bl_label = "Normal Cut"
    bl_options = {'REGISTER', 'UNDO'}

    flip = bpy.props.BoolProperty(name="Flip Normals",  description="Flip Normals", default=False) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'flip')

    def execute(self, context):
        
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1})
        for i in range(self.flip):
            bpy.ops.mesh.flip_normals()
        bpy.ops.transform.resize(value=(1000, 1000, 0), constraint_axis=(True, True, False))
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 1000), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        
        bpy.ops.mesh.select_linked(delimit={'SEAM'})
        bpy.ops.mesh.intersect_boolean(operation='DIFFERENCE')
                         
        return {'FINISHED'}




class VIEW3D_TP_AutoCut(bpy.types.Operator):
    """cut and delete choosen sides"""
    bl_idname = "tp_ops.mods_autocut_obm"
    bl_label = "AutoCuts"
    bl_options = {'REGISTER', 'UNDO'}

    bpy.types.Scene.tp_axis = bpy.props.EnumProperty(
                          items = [("positiv",  "Positiv", "", 1),
                                   ("negativ",  "Negativ", "", 2)], 
                                   name = "Side for Remove",
                                   description="side for remove")
                                   

    bpy.types.Scene.tp_axis_cut = bpy.props.EnumProperty(
                          items = [("x",   "X",   "", 1),
                                   ("y",   "Y",   "", 2),
                                   ("z",   "Z",   "", 3), 
                                   ("xy",  "XY",  "", 4), 
                                   ("xz",  "XZ",  "", 5), 
                                   ("yz",  "YZ",  "", 6), 
                                   ("xyz", "XYZ", "", 7), 
                                   ("normal", "Normal", "", 8)],
                                   name = "Axis for Remove", 
                                   description="axis for remove")

  
    def execute(self, context):
        scene = context.scene
        
        if scene.tp_axis == "positiv":
             
            if scene.tp_axis_cut == "x":
                bpy.ops.tp_ops.mods_positiv_x_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "y":            
                bpy.ops.tp_ops.mods_positiv_y_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "z":  
                bpy.ops.tp_ops.mods_positiv_z_cut_obm()       
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "xy":  
                bpy.ops.tp_ops.mods_positiv_xy_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "xy":  
                bpy.ops.tp_ops.mods_positiv_xz_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "yz":  
                bpy.ops.tp_ops.mods_positiv_yz_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "xyz":            
                bpy.ops.tp_ops.mods_positiv_xyz_cut_obm()
                bpy.ops.object.editmode_toggle()             
            if context.mode == 'EDIT_MESH':
                if scene.tp_axis_cut == "normal":            
                    bpy.ops.tp_ops.normal_cut()


        if scene.tp_axis == "negativ":

            if scene.tp_axis_cut == "x":  
                bpy.ops.tp_ops.mods_negativ_x_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "y":            
                bpy.ops.tp_ops.mods_negativ_y_cut_obm()   
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "z":             
                bpy.ops.tp_ops.mods_negativ_z_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "xy":  
                bpy.ops.tp_ops.mods_negativ_xy_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "xz":            
                bpy.ops.tp_ops.mods_negativ_xz_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "yz":             
                bpy.ops.tp_ops.mods_negativ_yz_cut_obm()
                bpy.ops.object.editmode_toggle() 
            if scene.tp_axis_cut == "xyz":             
                bpy.ops.tp_ops.mods_negativ_xyz_cut_obm()
                bpy.ops.object.editmode_toggle()  
            if context.mode == 'EDIT_MESH':
                if scene.tp_axis_cut == "normal":            
                    bpy.ops.tp_ops.normal_cut(flip=True)
                      

        if bpy.context.scene.tp_edit == True:
            
            if context.mode == 'EDIT_MESH': 
                bpy.ops.object.editmode_toggle()

            bpy.ops.object.editmode_toggle() 

        else:
            pass
        

        return {'FINISHED'}



    
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


