# ##### BEGIN GPL LICENSE BLOCK #####
#
# by Marvin K. Breuer, Oktober 2017
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


bl_info = {
    "name": "Curve: Copy",
    "description": "create copies from curve",
    "category": "T+",
    "author": "MKB",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
}


# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import *


class VIEW3D_TP_Curve_Copies(bpy.types.Operator):
    """Curve Copies"""
    bl_idname = "tp_ops.curve_copies"
    bl_label = "Curve Copy"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.type == 'CURVE')


    # MAIN PROPS #
    copies = bpy.props.IntProperty(name="Copies", description="How many?", default=1, min=1, soft_max=1000, step=1)
    outline = bpy.props.FloatProperty(name="Amount", default=0.1, min=-100, max=100)

    # TRANSFORM #
    cv_transform_use = bpy.props.BoolProperty(name="Individual Transform",  description="enable transform tools", default=False)  

    # TRANSFORM LOCATION #
    cv_location = bpy.props.FloatProperty(name="Local Z", description="set location value", default=0.00, min=-100, max=100)
    cv_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100)
    cv_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100)
    cv_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100)

    # TRANSFORM ROTATE #
    cv_rotate = bpy.props.FloatProperty(name="Rotate Z", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    cv_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    cv_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60)
    cv_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60)

    # TRANSFORM SCALE #
    cv_scale = bpy.props.FloatProperty(name="Scale XY", description="set xy scale value", default=1.00, min=0, max=100)
    cv_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100)
    cv_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100)
    cv_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100)

    # RELATIONS #
    link = bpy.props.BoolProperty(name="Link Data", description="add copies", default=True)  
    join = bpy.props.BoolProperty(name="Join Copies", description="join all copies", default=True)  


    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        col = layout.column(align = True)

        box = col.box().column(1)  

        row = box.row(1)
        row.prop(self, "copies")                 

        box.separator()
                
        box = col.box().column(1)   

        row = box.row(1)
        row.prop(self, "cv_transform_use")         
        
        if self.cv_transform_use == True:

            row = box.row(1)
            row.label("Location") 
            
            row = box.row(1)        
            row.prop(self, "cv_location_x") 
            row.prop(self, "cv_location_y")               
            row.prop(self, "cv_location_z") 
     
            box.separator()

            row = box.row(1)
            row.label("Rotation") 
            
            row = box.row(1)
            row.prop(self, "cv_rotate_x") 
            row.prop(self, "cv_rotate_y")               
            row.prop(self, "cv_rotate_z") 
     
            box.separator()

            row = box.row(1)
            row.label("Scale") 
            
            row = box.row(1)
            row.prop(self, "cv_scale_x") 
            row.prop(self, "cv_scale_y")               
            row.prop(self, "cv_scale_z") 

        else:

            row = box.column(1)
            row.prop(self, "cv_location") 
            row.prop(self, "cv_rotate") 
            row.prop(self, "cv_scale") 


        box.separator()
        
        if context.mode == 'OBJECT':
            
            box = col.box().column(1)  
                    
            row = box.row(1)
            row.prop(self, "link")
            if self.link == True:
                row.prop(self, "join")
            else:
                pass


    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()

        ### store 3d cursor location
        c3d = context.space_data
        if c3d.type == 'VIEW_3D':
            rc3d = c3d.region_3d
            current_cloc = c3d.cursor_location.xyz 

        
        # create copies
        for i in range(self.copies):
            
            # check mode
            if context.mode == 'OBJECT':            
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
                bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":self.link})

            else:
                bpy.ops.curve.duplicate_move()
                           
            # individual transform        
            if self.cv_transform_use == True:

                # location 
                bpy.ops.transform.translate(value=(self.cv_location_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='LOCAL')
                bpy.ops.transform.translate(value=(0, self.cv_location_y, 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL')
                bpy.ops.transform.translate(value=(0, 0, self.cv_location_z), constraint_axis=(False, False, True), constraint_orientation='LOCAL')

                # rotate 
                bpy.ops.transform.rotate(value=self.cv_rotate_x, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='LOCAL')
                bpy.ops.transform.rotate(value=self.cv_rotate_y, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL')
                bpy.ops.transform.rotate(value=self.cv_rotate_z, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='LOCAL')

                # scale 
                bpy.ops.transform.resize(value=(self.cv_scale_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='LOCAL')
                bpy.ops.transform.resize(value=(0, self.cv_scale_y, 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL')
                bpy.ops.transform.resize(value=(0, 0, self.cv_scale_z), constraint_axis=(False, False, True), constraint_orientation='LOCAL')

            else:
                # simple transform
                bpy.ops.transform.translate(value=(0, 0, self.cv_location), constraint_axis=(False, False, True), constraint_orientation='LOCAL')
                bpy.ops.transform.rotate(value=self.cv_rotate, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='LOCAL')
                bpy.ops.transform.resize(value=(self.cv_scale, self.cv_scale, 0), constraint_axis=(True, True, False), constraint_orientation='LOCAL')

            
            # check mode
            if context.mode == 'OBJECT':
                if self.link == True:
                    for i in range(self.join):
                        bpy.ops.object.select_linked(type='OBDATA')
                        bpy.ops.object.join()

                ### set origin to previous location
                c3d.cursor_location = current_cloc 
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            else:
                pass


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
    
 


