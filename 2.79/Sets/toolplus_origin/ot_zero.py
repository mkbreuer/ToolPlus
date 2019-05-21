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
import mathutils
from bpy import *
from bpy.props import *
from mathutils import Vector, Matrix


# LOAD CUSTOM TOOL SETTINGS #
def settings_load(self):
    panel_prefs = context.user_preferences.addons[__package__].preferences
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(panel_prefs, key))


# STORE CUSTOM TOOL SETTINGS #
def settings_write(self):
    panel_prefs = context.user_preferences.addons[__package__].preferences
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(panel_prefs, key, getattr(self, key))


class VIEW3D_OT_Zero_to_Global_Axis(bpy.types.Operator):
    """align origin, object or cursor to global axis"""                 
    bl_idname = "tpc_ot.zero_axis"          
    bl_label = "ZeroAxis"                 
    bl_options = {'REGISTER', 'UNDO'}   

    tp_switch = bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_org",    
               description = "zero object or cursor")

    align_x = BoolProperty (name = "X", default= False, description= "enable X axis alignment")
    align_y = BoolProperty (name = "Y", default= False, description= "enable Y axis alignment")                               
    align_z = BoolProperty (name = "Z", default= False, description= "enable Z axis alignment")

    tp_origin_offset = FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)
    tp_align_offset = FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)

    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        row = box.row()
        row.prop(self, 'tp_switch', expand=True)
      
        box.separator()

        row = box.row()
        row.prop(self, 'align_x')
        row.prop(self, 'align_y')
        row.prop(self, 'align_z')
        
        box.separator()

        if self.tp_switch == 'tp_org':
       
            row = box.row(1)      
            row.prop(self, "tp_origin_offset", text="")
          
            box.separator()

        if self.tp_switch == 'tp_obj':
       
            row = box.row(1)      
            row.prop(self, "tp_align_offset", text="")
          
            box.separator()
        

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):
        
        # WRITE CUSTOM SETTTINGS #
        settings_write(self) 
              
        selected = bpy.context.selected_objects
        obj = bpy.context.active_object    

        # STORE ACTIVE # 
        target = bpy.context.scene.objects.active    
      
        bpy.context.space_data.cursor_location = bpy.context.object.location  

        # X AXIS #
        if self.align_x == True:  
            
            if self.tp_switch == "tp_obj":        
                bpy.context.object.location[0] = 0                    
                for ob in selected:                  
                    ob.location[0] = obj.location[0] + self.tp_align_offset[0]

            if self.tp_switch == "tp_crs" or self.tp_switch == "tp_org":
       
                bpy.context.space_data.cursor_location[0] = 0 

            if self.tp_switch == "tp_org":                
                
                if context.mode == 'OBJECT':
                    bpy.ops.tpc_ot.origin_cursor_align(loc_x=True, loc_offset=self.tp_origin_offset)                 
                else:   
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.tpc_ot.origin_cursor_align(loc_x=True, loc_offset=self.tp_origin_offset)
                    bpy.ops.object.editmode_toggle()



        # Y AXIS #
        if self.align_y == True:  

            if self.tp_switch == "tp_obj":        
                bpy.context.object.location[1] = 0  
                for ob in selected:                  
                    ob.location[1] = obj.location[1] + self.tp_align_offset[1]
 
            if self.tp_switch == "tp_crs" or self.tp_switch == "tp_org":            
                bpy.context.space_data.cursor_location[1] = 0 

            if self.tp_switch == "tp_org":
                
                if context.mode == 'OBJECT':
                    bpy.ops.tpc_ot.origin_cursor_align(loc_y=True, loc_offset=self.tp_origin_offset)                  
                else:   
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.tpc_ot.origin_cursor_align(loc_y=True, loc_offset=self.tp_origin_offset)
                    bpy.ops.object.editmode_toggle()



        # Z AXIS #
        if self.align_z == True:  

            if self.tp_switch == "tp_obj":     
                bpy.context.object.location[2] = 0  
                for ob in selected:                  
                    ob.location[2] = obj.location[2] + self.tp_align_offset[2]

            if self.tp_switch == "tp_crs" or self.tp_switch == "tp_org":      
                bpy.context.space_data.cursor_location[2] = 0 

            if self.tp_switch == "tp_org":        
                
                if context.mode == 'OBJECT':
                    bpy.ops.tpc_ot.origin_cursor_align(loc_z=True, loc_offset=self.tp_origin_offset)                    
                else:   
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.tpc_ot.origin_cursor_align(loc_z=True, loc_offset=self.tp_origin_offset)  
                    bpy.ops.object.editmode_toggle()


        # RELOAD ACTIVE #     
        bpy.context.scene.objects.active = target

        return {'FINISHED'} 





class VIEW3D_OT_Zero_to_Global_Axis_Menu(bpy.types.Operator):
    """align origin, object or cursor to global axis"""                 
    bl_idname = "tpc_ot.zero_axis_menu"          
    bl_label = "ZeroAxis"                 
    bl_options = {'REGISTER', 'UNDO'}   

    tp_switch = bpy.props.EnumProperty(
        items=[("tp_obj"    ,"Object"    ,"01"),
               ("tp_org"    ,"Origin"    ,"02"),
               ("tp_crs"    ,"Cursor"    ,"03")],
               name = "ZeroFor",
               default = "tp_org",    
               description = "zero object or cursor")

    align_x = BoolProperty (name = "X", default= False, description= "enable X axis alignment")
    align_y = BoolProperty (name = "Y", default= False, description= "enable Y axis alignment")                               
    align_z = BoolProperty (name = "Z", default= False, description= "enable Z axis alignment")

    tp_origin_offset = FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)
    tp_align_offset = FloatVectorProperty(name="Offset", description="offset align position", default=(0.0, 0.0, 0.0), subtype='XYZ', size=3)

    def draw(self, context):
        layout = self.layout
        
        box = layout.box().column(1)

        row = box.row()
        row.prop(self, 'tp_switch', expand=True)
      
        box.separator()

        row = box.row()
        row.prop(self, 'align_x')
        row.prop(self, 'align_y')
        row.prop(self, 'align_z')
        
        box.separator()

        if self.tp_switch == 'tp_org':
       
            row = box.row(1)      
            row.prop(self, "tp_origin_offset", text="")
          
            box.separator()

        if self.tp_switch == 'tp_obj':
       
            row = box.row(1)      
            row.prop(self, "tp_align_offset", text="")
          
            box.separator()


    def execute(self, context):

        bpy.ops.tpc_ot.zero_axis(tp_switch = self.tp_switch, 
                                 align_x   = self.align_x, 
                                 align_y   = self.align_y, 
                                 align_z   = self.align_z, 
                                 tp_origin_offset = self.tp_origin_offset, 
                                 tp_align_offset  = self.tp_align_offset)

        return {'FINISHED'} 

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)





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


                    

# Snippet from Advanced Align Tools
# "author": "Lell, Anfeo"
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
    

