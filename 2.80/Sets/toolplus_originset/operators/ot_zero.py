# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
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
#

# LOAD MODUL #
import bpy
import mathutils
from bpy import *
from bpy.props import (BoolProperty, EnumProperty, FloatVectorProperty)
from mathutils import Vector, Matrix


# OPERATOR AS POP UP MENU #
class VIEW3D_OT_zero_to_global_axis_menu(bpy.types.Operator):
    """align origin, object or cursor to global axis"""                 
    bl_idname = "tpc_ops.zero_axis_menu"          
    bl_label = "Zero to XYZ Axis"                 
    bl_options = {'REGISTER', 'UNDO'}   

    tp_switch : bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_org",    
               description = "zero object or cursor")

    align_x : BoolProperty (name = "X", default= False, description= "enable X axis alignment")
    align_y : BoolProperty (name = "Y", default= False, description= "enable Y axis alignment")                               
    align_z : BoolProperty (name = "Z", default= False, description= "enable Z axis alignment")

    lock_x : BoolProperty (name = "X Lock", default= False, description= "lock transform on x axis")
    lock_y : BoolProperty (name = "Y Lock", default= False, description= "lock transform on y axis")                               
    lock_z : BoolProperty (name = "Z Lock", default= False, description= "lock transform on z axis")

    tp_origin_offset : FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)
    tp_align_offset : FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)

    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(align=True)

        row = box.row()
        row.prop(self, 'tp_switch', expand=True)
      
        box.separator()

        row = box.row()
        row.prop(self, 'align_x')
        row.prop(self, 'align_y')
        row.prop(self, 'align_z')
                
        box.separator()
       
        if self.tp_switch == 'tp_obj':

            if self.lock_x == True:
                ico_x = 'LOCKED'
            else:
                ico_x = 'UNLOCKED'       

            if self.lock_y == True:
                ico_y = 'LOCKED'
            else:
                ico_y = 'UNLOCKED'       
          
            if self.lock_z == True:
                ico_z = 'LOCKED'
            else:
                ico_z = 'UNLOCKED'       

            row = box.row(align=False)
            row.prop(self, "lock_x", text="X", icon=ico_x)       
            row.prop(self, "lock_y", text="Y", icon=ico_y) 
            row.prop(self, "lock_z", text="Z", icon=ico_z) 
            
            box.separator()

        if self.tp_switch == 'tp_org':
       
            row = box.row(align=True)      
            row.prop(self, "tp_origin_offset", text="")
          
            box.separator()

        if self.tp_switch == 'tp_obj':
       
            row = box.row(align=True)      
            row.prop(self, "tp_align_offset", text="")
          
            box.separator()


    def execute(self, context):

        bpy.ops.tpc_ops.zero_axis(tp_switch = self.tp_switch, 
                                 align_x   = self.align_x, 
                                 align_y   = self.align_y, 
                                 align_z   = self.align_z, 
                                 lock_x   = self.lock_x, 
                                 lock_y   = self.lock_y, 
                                 lock_z   = self.lock_z, 
                                 tp_origin_offset = self.tp_origin_offset, 
                                 tp_align_offset  = self.tp_align_offset)

        return {'FINISHED'} 

    def invoke(self, context, event):
        dpi_value = bpy.context.preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)




# Snippet from Advanced Align Tools
# "author": "Lell, Anfeo"
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
            
            nm = obj_mtx.inverted() @ Matrix.Translation(-move_pivot) @ obj_mtx

            # move mesh 
            me.transform(nm) 
            
        if loc_x: 
            movement(offset_x)
       
        if loc_y:
            movement(offset_y)   
       
        if loc_z:
            movement(offset_z)


    ref_co = bpy.context.scene.cursor.location  
    move_pivot(act_obj)
   
    for obj in sel_obj:   
        move_pivot(obj)           


                    

class VIEW3D_OT_origin_cursor_align(bpy.types.Operator):
    """align origin to cursor"""
    bl_idname = "tpc_ops.origin_cursor_align"
    bl_label = "origin align"
    bl_description = "Origin Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    loc_x : BoolProperty (name = "Align to X axis", default= False, description= "Enable X axis alignment")
    loc_y : BoolProperty (name = "Align to Y axis", default= False, description= "Enable Y axis alignment")                               
    loc_z : BoolProperty (name = "Align to Z axis", default= False, description= "Enable Z axis alignment")

    loc_offset : FloatVectorProperty(name="Location Offset", description="Offset for location align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)       

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(align=True)              
        box.separator()      
        
        row = box.row()
        row.prop(self, 'active_too')    

        box.separator()      
     
        row = box.row(align=True)
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
    

