# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****


#bl_info = {
#    "name": "Mifth Tools",
#    "author": "Paul Geraskin",
#    "version": (0, 1, 0),
#    "blender": (2, 71, 0),
#    "location": "3D Viewport",
#    "description": "Mifth Tools",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Tools"}


import bpy
from bpy.props import *
from bpy.types import Operator, AddonPreferences

import math



class RadialClone(bpy.types.Operator):
    """Radial Clone"""
    bl_idname = "mft.radialclone"
    bl_label = "Radial Clone"
    bl_description = "Radial Clone"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    radialClonesAngle = FloatProperty(default = 360.0, min = -360.0, max = 360.0)
    clonez = IntProperty(default = 8, min = 2, max = 300)
    single = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)    
    join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)    
    edit = bpy.props.BoolProperty(name="Edit",  description="Editmode", default=False)    

    def draw(self, context):
        layout = self.layout
        box = layout.box().column(1)   

        row = box.column(1) 
        row.prop(self, "radialClonesAngle")
        row.prop(self, "clonez")
        
        row = box.row(1)         
        row.prop(self, "single")
        row.prop(self, "join")
        row.prop(self, "edit")

    def execute(self, context):

        if len(bpy.context.selected_objects) > 0:
            activeObj = bpy.context.scene.objects.active
            selObjects = bpy.context.selected_objects
            mifthTools = bpy.context.scene.mifthTools
            activeObjMatrix = activeObj.matrix_world

            for i in range(self.clonez - 1):
                bpy.ops.object.duplicate(linked=True, mode='DUMMY')
                theAxis = None

                if mifthTools.radialClonesAxis == 'X':
                    if mifthTools.radialClonesAxisType == 'Local':
                        theAxis = (activeObjMatrix[0][0], activeObjMatrix[1][0], activeObjMatrix[2][0])
                    else:
                        theAxis = (1, 0, 0)

                elif mifthTools.radialClonesAxis == 'Y':
                    if mifthTools.radialClonesAxisType == 'Local':
                        theAxis = (activeObjMatrix[0][1], activeObjMatrix[1][1], activeObjMatrix[2][1])
                    else:
                        theAxis = (0, 1, 0)

                elif mifthTools.radialClonesAxis == 'Z':
                    if mifthTools.radialClonesAxisType == 'Local':
                        theAxis = (activeObjMatrix[0][2], activeObjMatrix[1][2], activeObjMatrix[2][2])
                    else:
                        theAxis = (0, 0, 1)
                
                rotateValue = (math.radians(self.radialClonesAngle)/float(self.clonez))
                bpy.ops.transform.rotate(value=rotateValue, axis=theAxis)

            bpy.ops.object.select_all(action='DESELECT')

            for obj in selObjects:
                obj.select = True
            selObjects = None
            bpy.context.scene.objects.active = activeObj
        else:
            self.report({'INFO'}, "Select Objects!")

        for i in range(self.single):
            bpy.ops.object.select_linked(type='OBDATA')
            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

        for i in range(self.join):
            bpy.ops.object.select_linked(type='OBDATA')
            bpy.ops.object.join()
            
        for i in range(self.edit):
            bpy.ops.object.editmode_toggle()
               
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)


class RadialClone_Panel(bpy.types.Operator):
    """Radial Clone"""
    bl_idname = "mft.radialclone_panel"
    bl_label = "Radial Clone"
    bl_description = "Radial Clone"
    bl_options = {'REGISTER', 'UNDO'}

    bpy.types.Scene.radialClonesAngle = FloatProperty(default = 360.0, min = -360.0, max = 360.0)
    bpy.types.Scene.clonez = IntProperty(default = 2, min = 2, max = 300)

    rz_unlink = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)  
    rz_join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)       
  

    def draw(self, context):
        layout = self.layout.column(1)

        box = layout.box().column(1)
        
        row = box.column(1)        
        row.prop(self, 'rz_join', text="Join")
        row.label("or")
        row.prop(self, 'rz_unlink', text="Unlink")
        

    def execute(self, context):
        scene = context.scene

        if len(bpy.context.selected_objects) > 0:
            activeObj = bpy.context.scene.objects.active
            selObjects = bpy.context.selected_objects
            mifthTools = bpy.context.scene.mifthTools
            activeObjMatrix = activeObj.matrix_world

            for i in range(scene.clonez - 1):
                bpy.ops.object.duplicate(linked=True, mode='DUMMY')
                theAxis = None

                if mifthTools.radialClonesAxis == 'X':
                    if mifthTools.radialClonesAxisType == 'Local':
                        theAxis = (activeObjMatrix[0][0], activeObjMatrix[1][0], activeObjMatrix[2][0])
                    else:
                        theAxis = (1, 0, 0)

                elif mifthTools.radialClonesAxis == 'Y':
                    if mifthTools.radialClonesAxisType == 'Local':
                        theAxis = (activeObjMatrix[0][1], activeObjMatrix[1][1], activeObjMatrix[2][1])
                    else:
                        theAxis = (0, 1, 0)

                elif mifthTools.radialClonesAxis == 'Z':
                    if mifthTools.radialClonesAxisType == 'Local':
                        theAxis = (activeObjMatrix[0][2], activeObjMatrix[1][2], activeObjMatrix[2][2])
                    else:
                        theAxis = (0, 0, 1)
                
                rotateValue = (math.radians(scene.radialClonesAngle)/float(scene.clonez))
                bpy.ops.transform.rotate(value=rotateValue, axis=theAxis)

            bpy.ops.object.select_all(action='DESELECT')

            for obj in selObjects:
                obj.select = True
            selObjects = None
            bpy.context.scene.objects.active = activeObj
        else:
            self.report({'INFO'}, "Select Objects!")

        for i in range(self.rz_unlink):
            bpy.ops.object.select_linked(type='OBDATA')
            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

        for i in range(self.rz_join):
            bpy.ops.object.select_linked(type='OBDATA')
            bpy.ops.object.join()

               
        return {'FINISHED'}



class MFTProperties(bpy.types.PropertyGroup):

    radialClonesAxis = EnumProperty(items = (('X', 'X', ''), ('Y', 'Y', ''), ('Z', 'Z', '')), default = 'Z')

    radialClonesAxisType = EnumProperty(items = (('Global', 'Global', ''),('Local', 'Local', '')), default = 'Global')

    mft_radialClonesAngle = FloatProperty(default = 360.0, min = -360.0, max = 360.0)
    mft_clonez = IntProperty(default = 8, min = 2, max = 300)
 


