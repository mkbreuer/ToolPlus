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
# Snippet from Advanced Align Tools
# "author": "Lell, Anfeo"


# LOAD MODUL #
import bpy, mathutils
from mathutils import Vector, Matrix
from bpy.props import EnumProperty, BoolProperty, FloatVectorProperty 


def origin_cursor_function(loc_x, loc_y, loc_z, loc_offset):
               
    sel_obj = bpy.context.selected_objects
    act_obj = bpy.context.active_object
    
    global ref_co

    def move_pivot(obj):
        me = obj.data                
        vec_ref_co = Vector(ref_co)       
       
        offset = vec_ref_co - obj.location  
       
        offset_x = [offset[0] + loc_offset[0], 0, 0]
        offset_y = [0, offset[1] + loc_offset[1], 0]
        offset_z = [0, 0, offset[2] + loc_offset[2]]   
        
        def movement(vec):
            obj_mtx = obj.matrix_world.copy()
            # find pivot displacement vector
            move_pivot = Vector(vec)
             
            # move pivot point = object location
            pivot = obj.location
            pivot += move_pivot         
            
            nm = obj_mtx.inverted() * Matrix.Translation(-move_pivot) * obj_mtx

            # move mesh 
            me.transform(nm) 
            
        if loc_x: 
            movement(offset_x)
       
        if loc_y:
            movement(offset_y)   
       
        if loc_z:
            movement(offset_z)


    ref_co = bpy.context.scene.cursor_location  
    move_pivot(act_obj)
   
    for obj in sel_obj:   
        move_pivot(obj)           



class VIEW3D_OT_Origin_Cursor_Align(bpy.types.Operator):
    """align origin to cursor"""
    bl_idname = "tpc_ot.origin_cursor_align"
    bl_label = "origin align"
    bl_description = "Origin Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    loc_x = BoolProperty (name = "Align to X axis", default= False, description= "Enable X axis alignment")
    loc_y = BoolProperty (name = "Align to Y axis", default= False, description= "Enable Y axis alignment")                               
    loc_z = BoolProperty (name = "Align to Z axis", default= False, description= "Enable Z axis alignment")

    loc_offset = FloatVectorProperty(name="Location Offset", description="Offset for location align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)       

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(1)              
        box.separator()      
        
        row = box.row()
        row.prop(self, 'active_too')    

        box.separator()      
     
        row = box.row(1)
        row.prop(self, "loc_x", text="X")       
        row.prop(self, "loc_y", text="Y") 
        row.prop(self, "loc_z", text="Z")
       
        box.separator()              
        
        row = box.row()   
        row.prop(self, 'loc_offset', text='')     
       
        box.separator()    

    def execute(self, context):
        origin_cursor_function(self.loc_x, self.loc_y, self.loc_z, self.loc_offset) 
                               
        return {'FINISHED'} 
    


