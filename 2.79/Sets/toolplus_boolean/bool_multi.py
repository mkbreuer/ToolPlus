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

#bl_info = {
#    "name": "Multi_Machine_v3",
#    "author": "DS",
#    "version": (0,0,1),
#    "description": "Res.Does boolean differences or unions on an target using an object (tool) in a parameter driven pattern (rotate or slide).",
#    "location": "View3D > Tool Shelf > MultiMachine",
#    "warning": "",
#    "category": "Object"}
    

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from bpy.types import WindowManager

import math
from math import radians
from mathutils import Vector, Euler
import os


# LOAD UI: PANEL #

EDIT = ["OBJECT"]
GEOM = ['MESH']

class draw_multibool_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        tp_props = context.window_manager.tp_props_multibool 

        box = layout.box().column(1) 
       
        row = box.column(1)
        row.prop_search(tp_props, "Target", bpy.data, "objects",icon="TRIA_DOWN")
        row.prop_search(tp_props, "Tool", bpy.data, "objects",icon="TRIA_DOWN")
        
        row.separator()         
       
        row.prop(tp_props, "MMAction", text="Action")      
        row.prop(tp_props, "MMMove", text="Move")      

        row.separator() 
        
        row.prop(tp_props, "MMToolXVal", text="X")
        row.prop(tp_props, "MMToolYVal", text="Y")
        row.prop(tp_props, "MMToolZVal", text="Z")
       
        row.separator() 

        row.prop(tp_props, "NumSteps", text="Num. Steps")
        row.prop(tp_props, "StartSteps", text="Start at Step")

        box.separator() 
        
        box = layout.box().column(1) 
       
        row = box.column(1)
        row.prop(tp_props, "MMPreStep", text="Pre-Move")
        
        row.separator()         
        
        row.prop(tp_props, "MMPreStepXVal", text="X")
        row.prop(tp_props, "MMPreStepYVal", text="Y")
        row.prop(tp_props, "MMPreStepZVal", text="Z")
        
        box.separator() 

        box = layout.box().column(1) 
       
        row = box.column(1)
        row.prop(tp_props, "RepeaterCnt", text="Repeat")
        row.separator() 
        row.prop(tp_props, "ReturnToLoc", text="ReturnToLoc")

        row.separator() 
        
        row = box.row(1)        
        row.operator("reset.exec", text="Reset")       
        row.operator("tool.exec", text="Execute")
      
        box.separator() 


class VIEW3D_TP_MultiBool_Panel_TOOLS(bpy.types.Panel, draw_multibool_layout):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_MultiBool_Panel_TOOLS"
    bl_label = "MultiBool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_MultiBool_Panel_UI(bpy.types.Panel, draw_multibool_layout):
    bl_idname = "VIEW3D_TP_MultiBool_Panel_UI"
    bl_label = "MultiBool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}



# OPERATOR #
class mmtoolButton(bpy.types.Operator):
    """Make Multi Diff or Union""" 
    bl_idname = "tool.exec"
    bl_label = "Make Diff or Union"
    bl_options = {'REGISTER', 'UNDO'} 

    bpSP = bpy.props.StringProperty()    
    Target = bpy.props.StringProperty()
    Tool = bpy.props.StringProperty()
    
    MMAction = EnumProperty(items=(('None', "None", "No tooling"),
                        ('Diff', "Diff", "Do Boolean Difference"),
                        ('Union', "Union", "Do Boolean Union")),                        
                    name="MMAction",
                    default = 'Diff',
                    description="Action for the Multi Machine.")
    MMMove = EnumProperty(items=(('Slide', "Slide", "Slide the target on the axis"),
                        ('Rotate', "Rotate", "Rotate the target on the axis")),
                    name="MMMove",
                    default = 'Rotate',
                    description="What action should happen in the machining sequence.")
    MMToolXVal = FloatProperty(name='MMToolXVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on X axis.")
    MMToolYVal = FloatProperty(name='MMToolYVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Y axis.")
    MMToolZVal = FloatProperty(name='MMToolZVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Z axis.")
    NumSteps = IntProperty(name='NumSteps', min=1, max=10000, description="Number tooling steps to take.")
    StartSteps = IntProperty(name='StartSteps', min=0, max=10000, description="The step at which to start tooling (current location is zero).")
    MMPreStep = EnumProperty(items=(('None', "None", "No Pre-step"),
                        ('Slide', "Slide", "Slide the target on the axis"),
                        ('Rotate', "Rotate", "Rotate the target on the axis")),
                    name="MMPreStep",
                    default = 'None',
                    description="Movement for the Pre-step (done once before each tooling sequence).")
    MMPreStepXVal = FloatProperty(name='MMPreStepXVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on X axis in pre-step.")
    MMPreStepYVal = FloatProperty(name='MMPreStepYVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Y axis in pre-step..")
    MMPreStepZVal = FloatProperty(name='MMPreStepZVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Z axis in pre-step..")
    RepeaterCnt = IntProperty(name='RepeaterCnt', min=1, max=1000, description="Number of times to repeat the pre-step and tooling sequence.", default = 1)
   
    ReturnToLoc = BoolProperty(name='ReturnToLoc', default = True)

    # DRAW REDO LAST PROPS [F6] # 
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(1) 
       
        row = box.column(1)
        row.prop_search(self, "Target", bpy.data, "objects",icon="TRIA_DOWN")
        row.prop_search(self, "Tool", bpy.data, "objects",icon="TRIA_DOWN")
        
        row.separator()         
       
        row.prop(self, "MMAction", text="Action")      
        row.prop(self, "MMMove", text="Move")      

        row.separator() 
        
        row.prop(self, "MMToolXVal", text="X")
        row.prop(self, "MMToolYVal", text="Y")
        row.prop(self, "MMToolZVal", text="Z")
       
        row.separator() 

        row.prop(self, "NumSteps", text="Num. Steps")
        row.prop(self, "StartSteps", text="Start at Step")

        box.separator() 
        
        box = layout.box().column(1) 
       
        row = box.column(1)
        row.prop(self, "MMPreStep", text="Pre-Move")
        
        row.separator()         
        
        row.prop(self, "MMPreStepXVal", text="X")
        row.prop(self, "MMPreStepYVal", text="Y")
        row.prop(self, "MMPreStepZVal", text="Z")
        
        box.separator() 

        box = layout.box().column(1) 
       
        row = box.column()
        row.prop(self, "RepeaterCnt", text="Repeat")
        row.prop(self, "ReturnToLoc", text="ReturnToLoc")
      
        box.separator() 



    # load panel settings #
    def invoke(self, context, event):        
        settings_load(self)
        return self.execute(context)

    def execute(self, context):
        # write panel settings #
        settings_write(self) 
  
        os.system("cls")
        vars = self
        #vars = context.scene
        target = bpy.data.objects[vars.Target]
        tool = bpy.data.objects[vars.Tool]
        orig_Euler = target.rotation_euler
        orig_Location = target.location
        print('RTL: ', vars.ReturnToLoc)
        print(orig_Euler)
        print(orig_Location)
        return2_eul = rot_eul = [orig_Euler[0],orig_Euler[1],orig_Euler[2]]
        return2_loc = slide_loc = [orig_Location[0],orig_Location[1],orig_Location[2]]
        toolRotRads = [radians(vars.MMToolXVal),radians(vars.MMToolYVal),radians(vars.MMToolZVal)]
        toolSlideUnits = [vars.MMToolXVal,vars.MMToolYVal,vars.MMToolZVal]
        prestepRotRads = [radians(vars.MMPreStepXVal),radians(vars.MMPreStepYVal),radians(vars.MMPreStepZVal)]
        prestepSlideUnits = [vars.MMPreStepXVal,vars.MMPreStepYVal,vars.MMPreStepZVal]

        # print('orig: ',orig_Euler,orig_Location)
        # print('rot and slide: ',rot_eul,slide_loc)
        # print('tool: ',toolRotRads,toolSlideUnits)
        # print('pre: ',prestepRotRads,prestepSlideUnits)
        
        for r in range(vars.RepeaterCnt):
            # print ('rep_cnt: ',r)
            if (vars.MMPreStep =='Rotate'):
                rot_eul = Euler([sum(e) for e in zip(rot_eul, prestepRotRads)], "XYZ")
                target.rotation_euler = rot_eul
            elif (vars.MMPreStep =='Slide'):
                slide_loc = Vector([sum(v) for v in zip(slide_loc, prestepSlideUnits)])
                target.location = slide_loc
            
            # print('rot slide: ',rot_eul,slide_loc)
            
            for i in range(vars.NumSteps+1):
                # print('step: ',i)
                if (i > 0 ):
                    if (vars.MMMove == 'Rotate'):
                        rot_eul = Euler([sum(z) for z in zip(rot_eul, toolRotRads)], "XYZ")
                    else: # Assumes 'Slide'
                        slide_loc = Vector([sum(z) for z in zip(slide_loc, toolSlideUnits)])

                # At step 0 these are the original euler\location (or location after pre-step), else the eul\loc just set
                target.rotation_euler = rot_eul 
                target.location = slide_loc
                bpy.ops.object.select_all(action='DESELECT')
                target.select = True
                bpy.context.scene.objects.active = target
                
                if (i >= vars.StartSteps): # Execute tool action at this step
                    bpy.ops.object.modifier_add(type='BOOLEAN')
                    mod = target.modifiers
                    mod[0].name = "MMTool"
                    if (vars.MMAction == 'Diff'):
                        # print('diff: ',rot_eul, slide_loc)
                        mod[0].operation = 'DIFFERENCE'
                    else: # Assumes 'Union'
                        # print('union: ',rot_eul, slide_loc)
                        mod[0].operation = 'UNION'
                    if (vars.MMAction != 'None'):
                        mod[0].object = tool
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod[0].name)
                    
                i += 1
            r += 1
            
        if (vars.ReturnToLoc == True):
            print('Return!!!: ', return2_eul, return2_loc)
            target.rotation_euler = return2_eul
            target.location = return2_loc
            
        if self.bpSP == '':
            print('Done')
        else:
            print("Don't Make Cuts from %s!" % self.bpSP)
        return {"FINISHED"}


# RESET #
class mmtoolReset(bpy.types.Operator):
    bl_idname = "reset.exec"
    bl_label = "Reset values"
    bl_options = {'REGISTER', 'UNDO'}
 
    bpSPRS = bpy.props.StringProperty()

    def execute(self, context):

        tp_props = context.window_manager.tp_props_multibool         
        resetVars = tp_props

        resetVars.Target = ""
        resetVars.Tool = ""
        resetVars.MMAction = "None"
        resetVars.MMPreStep = "None"
        resetVars.MMToolXVal = 0
        resetVars.MMToolYVal = 0
        resetVars.MMToolZVal = 0
        resetVars.NumSteps = 0
        resetVars.StartSteps = 0
        resetVars.MMPreStepXVal = 0
        resetVars.MMPreStepYVal = 0
        resetVars.MMPreStepZVal = 0
        resetVars.RepeaterCnt = 0
        resetVars.ReturnToLoc = True
            
        if self.bpSPRS == '':
            print('Done')
        else:
            print("Don't Make Cuts from %s!" % self.bpSPRS)
        return {"FINISHED"}



# MULTIBOOL #
class VIEW3D_TP_Multi_Bool_Props(bpy.types.PropertyGroup):
    
    bpSPRS = bpy.props.StringProperty()

    bpSP = bpy.props.StringProperty()   
    Target = bpy.props.StringProperty()
    Tool = bpy.props.StringProperty()
    
    MMAction = EnumProperty(items=(('None', "None", "No tooling"),
                        ('Diff', "Diff", "Do Boolean Difference"),
                        ('Union', "Union", "Do Boolean Union")),                        
                    name="MMAction",
                    default = 'Diff',
                    description="Action for the Multi Machine.")

    MMMove = EnumProperty(items=(('Slide', "Slide", "Slide the target on the axis"),
                        ('Rotate', "Rotate", "Rotate the target on the axis")),
                    name="MMMove",
                    default = 'Rotate',
                    description="What action should happen in the machining sequence.")

    MMToolXVal = FloatProperty(name='MMToolXVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on X axis.")
    MMToolYVal = FloatProperty(name='MMToolYVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Y axis.")
    MMToolZVal = FloatProperty(name='MMToolZVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Z axis.")

    NumSteps = IntProperty(name='NumSteps', min=1, max=10000, description="Number tooling steps to take.")
    StartSteps = IntProperty(name='StartSteps', min=0, max=10000, description="The step at which to start tooling (current location is zero).")

    MMPreStep = EnumProperty(items=(('None', "None", "No Pre-step"),
                        ('Slide', "Slide", "Slide the target on the axis"),
                        ('Rotate', "Rotate", "Rotate the target on the axis")),
                    name="MMPreStep",
                    default = 'None',
                    description="Movement for the Pre-step (done once before each tooling sequence).")

    MMPreStepXVal = FloatProperty(name='MMPreStepXVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on X axis in pre-step.")
    MMPreStepYVal = FloatProperty(name='MMPreStepYVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Y axis in pre-step..")
    MMPreStepZVal = FloatProperty(name='MMPreStepZVal', default = 0, min=-100000, max=100000, precision=5, description="Number of degrees or units to move target on Z axis in pre-step..")

    RepeaterCnt = IntProperty(name='RepeaterCnt', min=1, max=1000, description="Number of times to repeat the pre-step and tooling sequence.", default = 1)
    ReturnToLoc = BoolProperty(name='ReturnToLoc', default = True)




# LOAD PANEL SETTINGS (LPT: Bart Crouch) #
def settings_load(self):
    tp_props = bpy.context.window_manager.tp_props_multibool
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(self, key, getattr(tp_props, key))

# STORE PANEL SETTINGS  (LPT: Bart Crouch) #
def settings_write(self):
    tp_props = bpy.context.window_manager.tp_props_multibool
    tool = self.name.split()[0].lower()
    keys = self.as_keywords().keys()
    for key in keys:
        setattr(tp_props, key, getattr(self, key))
 


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


