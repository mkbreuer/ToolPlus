# BEGIN GPL LICENSE BLOCK #####
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
# END GPL LICENSE BLOCK #####

#bl_info = {
#    "name": "Mifth CloneTools",
#    "author": "Paul Geraskin",
#    "version": (0, 1, 0),
#    "blender": (2, 78, 0),
#    "location": "3D Viewport",
#    "description": "Mifth Tools",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "T+"}


# LOAD CACHE #
from .caches.cache      import  (settings_load)
from .caches.cache      import  (settings_write)

# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *
from bpy_extras import view3d_utils

import math
import mathutils
import random
from mathutils import *


#class MFTPanelCloning(bpy.types.Panel):
#    bl_label = "Cloning"
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'TOOLS'
#    bl_context = "objectmode"
#    bl_category = 'Mifth'
#    # bl_options = {'DEFAULT_CLOSED'}

#    def draw(self, context):
#        layout = self.layout
#        mft_props = context.window_manager.mifth_clone_props    

#        layout.label(text="Radial Clone:")
#        row = layout.row(1)        
#        row.operator("tp_ops.mft_radialclone", text="Radial Clone")
#        row.prop(mft_props, "mft_clonez", text='')       
#       
#        row = layout.row(1)
#        row.prop(mft_props, "mft_radialClonesAxis", text='')
#        row.prop(mft_props, "mft_radialClonesAxisType", text='')
#       
#        layout.separator()

# adjusted by MKB

# OPERATOR # 
def draw_operator(self, context):
    
    if context.mode == "EDIT_MESH":
        pass
    else:  
        if len(bpy.context.selected_objects) > 0:
            activeObj = bpy.context.scene.objects.active
            selObjects = bpy.context.selected_objects

            activeObjMatrix = activeObj.matrix_world


            bpy.ops.view3d.snap_cursor_to_active()      

     
            clones_count = self.mft_clonez
            if self.mft_create_last_clone is False:
                clones_count = self.mft_clonez - 1

            for i in range(clones_count):
                bpy.ops.object.duplicate(linked=True, mode='DUMMY')
                theAxis = None

                if self.mft_radialClonesAxis == 'X':
                    if self.mft_radialClonesAxisType == 'Local':
                        theAxis = (
                            activeObjMatrix[0][0], activeObjMatrix[1][0], activeObjMatrix[2][0])
                    else:
                        theAxis = (1, 0, 0)

                elif self.mft_radialClonesAxis == 'Y':
                    if self.mft_radialClonesAxisType == 'Local':
                        theAxis = (
                            activeObjMatrix[0][1], activeObjMatrix[1][1], activeObjMatrix[2][1])
                    else:
                        theAxis = (0, 1, 0)

                elif self.mft_radialClonesAxis == 'Z':
                    if self.mft_radialClonesAxisType == 'Local':
                        theAxis = (
                            activeObjMatrix[0][2], activeObjMatrix[1][2], activeObjMatrix[2][2])
                    else:
                        theAxis = (0, 0, 1)

                rotateValue = (math.radians(self.mft_radialClonesAngle) / float(self.mft_clonez))
                bpy.ops.transform.rotate(value=rotateValue, axis=theAxis)


            bpy.ops.object.select_all(action='DESELECT')

            for obj in selObjects:
                obj.select = True
            selObjects = None
            bpy.context.scene.objects.active = activeObj
        else:
            self.report({'INFO'}, "Select Objects!")




    # custom transform        
    if self.copy_transform_use == True:

        bpy.ops.object.duplicate_move()


        view = context.space_data
        rv3d = view.region_3d
        current_cloc = view.cursor_location.xyz   

        # location 
        bpy.ops.transform.translate(value=(self.copy_location_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
        bpy.ops.transform.translate(value=(0, self.copy_location_y, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
        bpy.ops.transform.translate(value=(0, 0, self.copy_location_z), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

        # rotate 
        bpy.ops.transform.rotate(value=self.copy_rotate_x, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
        bpy.ops.transform.rotate(value=self.copy_rotate_y, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
        bpy.ops.transform.rotate(value=self.copy_rotate_z, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

        # scale 
        bpy.ops.transform.resize(value=(self.copy_scale_x, 0, 0), constraint_axis=(True, False, False), constraint_orientation='NORMAL')
        bpy.ops.transform.resize(value=(0, self.copy_scale_y, 0), constraint_axis=(False, True, False), constraint_orientation='NORMAL')
        bpy.ops.transform.resize(value=(0, 0, self.copy_scale_z), constraint_axis=(False, False, True), constraint_orientation='NORMAL')

        view.cursor_location = current_cloc       
        for i in range(self.mft_origin):            

            bpy.ops.object.origin_set(type='ORIGIN_CURSOR') 


    for i in range(self.mft_single):
        bpy.ops.object.select_linked(type='OBDATA')
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

    for i in range(self.mft_join):
        bpy.ops.object.select_linked(type='OBDATA')
        bpy.ops.object.join()
        
    for i in range(self.mft_edit):       
        bpy.ops.object.editmode_toggle()





# DRAW PROPS [F6] # 
def draw_props(self, context):
    layout = self.layout
    box = layout.box().column(1)     
    
    row = box.row(1)
    row.prop(self, "mft_radialClonesAxisType", text='')
    row.prop(self, "mft_radialClonesAxis", text='')

    row = box.row(1)            
    row.operator("tp_ops.mft_radialclone", text="Repeat")
    row.prop(self, "mft_clonez", text='Amount')        

    row = box.row(1)         
    row.prop(self, "mft_create_last_clone", text='CloneLast')       
    row.prop(self, "mft_single")        
    
    row = box.row(1)         
    row.prop(self, "mft_join")
    row.prop(self, "mft_edit")


    box = layout.box().column(1)   

    row = box.row(1)
    row.prop(self, "copy_transform_use")         
    
    if self.copy_transform_use == True:

        row.prop(self, "mft_origin")

        row = box.row(1)
        row.label("Location") 
        
        row = box.row(1)        
        row.prop(self, "copy_location_x") 
        row.prop(self, "copy_location_y")               
        row.prop(self, "copy_location_z") 
 
        box.separator()

        row = box.row(1)
        row.label("Rotation") 
        
        row = box.row(1)
        row.prop(self, "copy_rotate_x") 
        row.prop(self, "copy_rotate_y")               
        row.prop(self, "copy_rotate_z") 
 
        box.separator()

        row = box.row(1)
        row.label("Scale") 
        
        row = box.row(1)
        row.prop(self, "copy_scale_x") 
        row.prop(self, "copy_scale_y")               
        row.prop(self, "copy_scale_z") 

    box.separator()



class MFTRadialClone_PopUp(bpy.types.Operator):
    bl_idname = "tp_ops.mft_radialclone_popup"
    bl_label = "Radial Clone"
    bl_description = "Radial Clone"
    bl_options = {'REGISTER', 'UNDO'}

    # RADIAL CLONE #
    mft_create_last_clone = BoolProperty(name="Create Last Clone",description="create last clone...",default=False)
    mft_radialClonesAngle = FloatProperty(default=360.0, min=-360.0,max=360.0)
    mft_clonez = IntProperty(default=8,min=2, max=300)
    mft_radialClonesAxis = EnumProperty(items=(('X', 'X', ''),('Y', 'Y', ''),('Z', 'Z', '')),default = 'Z')
    mft_radialClonesAxisType = EnumProperty(items=(('Global', 'Global', ''),('Local', 'Local', '')),default = 'Global')

    # RELATIONS #    
    mft_single = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)    
    mft_join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)    
    mft_edit = bpy.props.BoolProperty(name="Edit",  description="Editmode", default=False)    

    # TRANSFORM #
    copy_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  
    mft_origin = bpy.props.BoolProperty(name="Set Origin back",  description="set origin back to previuos postion", default=False)  

    # TRANSFORM LOCATION #
    copy_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})

    # TRANSFORM ROTATE #
    copy_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})

    # TRANSFORM SCALE #
    copy_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})

    # DRAW PROPS [F6] # 
    def draw(self, context):
        
        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        settings_write(self)
        
        draw_operator(self, context)
            
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)    




class MFTRadialClone(bpy.types.Operator):
    bl_idname = "tp_ops.mft_radialclone"
    bl_label = "Radial Clone"
    bl_description = "Radial Clone"
    bl_options = {'REGISTER', 'UNDO'}

    # RADIAL CLONE #
    mft_create_last_clone = BoolProperty(name="Create Last Clone",description="create last clone...",default=False)
    mft_radialClonesAngle = FloatProperty(default=360.0, min=-360.0,max=360.0)
    mft_clonez = IntProperty(default=8,min=2, max=300)
    mft_radialClonesAxis = EnumProperty(items=(('X', 'X', ''),('Y', 'Y', ''),('Z', 'Z', '')),default = 'Z')
    mft_radialClonesAxisType = EnumProperty(items=(('Global', 'Global', ''),('Local', 'Local', '')),default = 'Global')

    # RELATIONS #    
    mft_single = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)    
    mft_join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)    
    mft_edit = bpy.props.BoolProperty(name="Edit",  description="Editmode", default=False)    

    # TRANSFORM #
    copy_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  
    mft_origin = bpy.props.BoolProperty(name="Set Origin back",  description="set origin back to previuos postion", default=False)  

    # TRANSFORM LOCATION #
    copy_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})

    # TRANSFORM ROTATE #
    copy_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})

    # TRANSFORM SCALE #
    copy_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})


    # DRAW PROPS [F6] # 
    def draw(self, context):

        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        settings_write(self)
        
        draw_operator(self, context)
               
        return {'FINISHED'}


class MFTCloneProperties(bpy.types.PropertyGroup):

    # RADIAL CLONE #
    mft_create_last_clone = BoolProperty(name="Create Last Clone",description="create last clone...",default=False)
    mft_radialClonesAngle = FloatProperty(default=360.0, min=-360.0,max=360.0)
    mft_clonez = IntProperty(default=8,min=2, max=300)
    mft_radialClonesAxis = EnumProperty(items=(('X', 'X', ''),('Y', 'Y', ''),('Z', 'Z', '')),default = 'Z')
    mft_radialClonesAxisType = EnumProperty(items=(('Global', 'Global', ''),('Local', 'Local', '')),default = 'Global')

    # RELATIONS #    
    mft_single = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)    
    mft_join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)    
    mft_edit = bpy.props.BoolProperty(name="Edit",  description="Editmode", default=False)    

    # TRANSFORM #
    copy_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  
    mft_origin = bpy.props.BoolProperty(name="Set Origin back",  description="set origin back to previuos postion", default=False)  

    # TRANSFORM LOCATION #
    copy_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})

    # TRANSFORM ROTATE #
    copy_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})

    # TRANSFORM SCALE #
    copy_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

    bpy.types.WindowManager.mft_clone_props = PointerProperty(name="Mifth Cloning Variables",type=MFTCloneProperties, description="Mifth Cloning Properties")

def unregister():

    del bpy.types.WindowManager.mft_clone_props

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
