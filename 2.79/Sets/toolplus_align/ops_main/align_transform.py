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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****

#bl_info = {"name": "Align Vertices", "author": "MKB"}


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


def align_function(tp_transform, tp_axis, tp_pivot, tp_orient, tp_mirror, propedit, falloff, propsize):

    if bpy.context.mode == 'OBJECT':

        selected = bpy.context.selected_objects
        obj = bpy.context.active_object               
     
        for ob in selected:
            
            if tp_transform == "LOCATION":
                
                if tp_axis == "axis_x":
                    ob.location.x = obj.location.x         

                if tp_axis == "axis_y":
                    ob.location.y = obj.location.y

                if tp_axis == "axis_z":
                    ob.location.z = obj.location.z

                if tp_axis == "axis_xy":
                    ob.location.x = obj.location.x  
                    ob.location.y = obj.location.y

                if tp_axis == "axis_zy":
                    ob.location.z = obj.location.z
                    ob.location.y = obj.location.y
           
                if tp_axis == "axis_zx":
                    ob.location.z = obj.location.z
                    ob.location.x = obj.location.x

                if tp_axis == "axis_xyz":
                    ob.location = obj.location 


          
            elif tp_transform == "ROTATION":

                if tp_axis == "axis_x":
                    ob.rotation_euler.x = obj.rotation_euler.x

                if tp_axis == "axis_y":
                    ob.rotation_euler.y = obj.rotation_euler.y

                if tp_axis == "axis_z":
                    ob.rotation_euler.z = obj.rotation_euler.z

                if tp_axis == "axis_xy":
                    ob.rotation_euler.x = obj.rotation_euler.x
                    ob.rotation_euler.y = obj.rotation_euler.y

                if tp_axis == "axis_zy":
                    ob.rotation_euler.z = obj.rotation_euler.z
                    ob.rotation_euler.y = obj.rotation_euler.y

                if tp_axis == "axis_zx":
                    ob.rotation_euler.z = obj.rotation_euler.z
                    ob.rotation_euler.x = obj.rotation_euler.x

                if tp_axis == "axis_xyz":
                    ob.rotation_euler = obj.rotation_euler


            elif tp_transform == "SCALE":
                
                if tp_axis == "axis_x":
                    ob.scale.x = obj.scale.x       

                if tp_axis == "axis_y":
                    ob.scale.y = obj.scale.y

                if tp_axis == "axis_z":
                    ob.scale.z = obj.scale.z

                if tp_axis == "axis_xy":
                    ob.scale.x = obj.scale.x       
                    ob.scale.y = obj.scale.y

                if tp_axis == "axis_zy":
                    ob.scale.z = obj.scale.z      
                    ob.scale.y = obj.scale.y

                if tp_axis == "axis_zx":
                    ob.scale.z = obj.scale.z      
                    ob.scale.x = obj.scale.x

                if tp_axis == "axis_xyz":
                    ob.scale = obj.scale     


    else:

        current_pivot = bpy.context.space_data.pivot_point

        if tp_pivot == "ACTIVE_ELEMENT":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'

        if tp_pivot == "MEDIAN_POINT":
            bpy.context.space_data.pivot_point = 'MEDIAN_POINT'

        if tp_pivot == "CURSOR":
            bpy.context.space_data.pivot_point = 'CURSOR'   


        if tp_axis == "axis_x":
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

        if tp_axis == "axis_y":
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

        if tp_axis == "axis_z":
            bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)
          
        if tp_axis == "axis_xy":
            bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

        if tp_axis == "axis_zy":
            bpy.ops.transform.resize(value=(1, 0, 0), constraint_axis=(False, True, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)

        if tp_axis == "axis_zx":
            bpy.ops.transform.resize(value=(0, 1, 0), constraint_axis=(True, False, True), constraint_orientation=tp_orient, mirror=tp_mirror, proportional=propedit, proportional_edit_falloff=falloff, proportional_size=propsize)


        bpy.context.space_data.pivot_point = current_pivot



      
class VIEW3D_TP_Align_Transform(bpy.types.Operator):
    """Align Transform"""
    bl_label = "Align"
    bl_idname = "tp_ops.align_transform"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis = bpy.props.EnumProperty(
        items=[("axis_x"     ,"X"     ,""),
               ("axis_y"     ,"Y"     ,""),
               ("axis_z"     ,"Z"     ,""),
               ("axis_xy"    ,"Xy"    ,""),
               ("axis_zy"    ,"Zy"    ,""),
               ("axis_zx"    ,"Zx"    ,""),
               ("axis_xyz"   ,"XYZ"   ,"")],
               name = " ",
               default = "axis_x")

    tp_pivot = bpy.props.EnumProperty(
        items=[("ACTIVE_ELEMENT"  ,"Active Element"  ,""  ,"ROTACTIVE"    ,0),
               ("MEDIAN_POINT"    ,"Median Point"    ,""  ,"ROTATECENTER" ,1),
               ("CURSOR"          ,"3D Cursor"       ,""  ,"CURSOR"       ,2)],
               name = "Pivot", 
               default = "ACTIVE_ELEMENT")


    tp_transform = bpy.props.EnumProperty(
        items=[("LOCATION"   ,"Location"  ,""  ,"MAN_TRANS"  ,0),
               ("ROTATION"   ,"Rotation"  ,""  ,"MAN_ROT"    ,1),
               ("SCALE"      ,"Scale"     ,""  ,"MAN_SCALE"  ,2)],
               name = "Transform",
               default = "LOCATION")

    tp_orient = bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View")],
               name = "Orientation",
               default = "GLOBAL")

    propedit = bpy.props.EnumProperty(
        items=[("DISABLED"   ,"Disabled"   ,""  ,"PROP_OFF" ,0),
               ("ENABLED"    ,"Enabled"    ,""  ,"PROP_ON"  ,1),
               ("PROJECTED"  ,"Projected"  ,""  ,"PROP_ON"  ,2),
               ("CONNECTED"  ,"Connected"  ,""  ,"PROP_CON" ,3)],
               name = "Proportional Editing",
               default = "DISABLED", options={'SKIP_SAVE'})

    falloff = bpy.props.EnumProperty(
        items=[("SMOOTH"            ,"Smooth"           ,""   ,"SMOOTHCURVE"  ,0),
               ("SPHERE"            ,"Sphere"           ,""   ,"SPHERECURVE"  ,1),
               ("ROOT"              ,"Root"             ,""   ,"ROOTCURVE"    ,2),
               ("INVERSE_SQUARE"    ,"Inverse Square"   ,""   ,"ROOTCURVE"    ,3),
               ("SHARP"             ,"Sharp"            ,""   ,"SHARPCURVE"   ,4),
               ("LINEAR"            ,"Linear"           ,""   ,"LINCURVE"     ,5),
               ("CONSTANT"          ,"Constant"         ,""   ,"NOCURVE"      ,6),
               ("RANDOM"            ,"Random"           ,""   ,"RNDCURVE"     ,7)],
               name = "Proportional Falloff",
               default = "SMOOTH")

    propsize = FloatProperty(name="Size",  description= "Proportional Editing Size", min=0.001, max=100.0, default=1.0)

    tp_mirror = BoolProperty (name = "Mirror", default= False, description= "mirror over origin")

    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(1)              
            
        if bpy.context.mode == 'OBJECT':
    
            row = box.row(1) 
            row.prop(self, 'tp_transform', expand =True) 
    
            box.separator() 

            row = box.row(1) 
            row.prop(self, 'tp_axis', expand =True)
        
            box.separator() 

            row = box.row(1) 
            row.operator('tp_ops.align_transform', text="Repeat")
        
            box.separator() 

        else:
        
            row = box.row(1) 
            row.prop(self, 'tp_axis', expand =True)
        
            box.separator() 
         
            row = box.row(1) 
            row.label('Oriention:')      
            row.prop(self, 'tp_orient', text="")      

            box.separator() 

            row = box.row(1) 
            row.label('Pivot Point:')      
            row.prop(self, 'tp_pivot', text="")    

            box.separator()

            box = col.box().column(1)   

            row = box.row(1) 
            row.label("Proportional Editing")

            box.separator() 

            row = box.row() 
            row.prop(self, 'propedit', text="")
            row.prop(self, 'falloff', text="")
         
            box.separator() 
            
            row = box.row(1) 
            row.prop(self, 'propsize')
            row.prop(self, 'tp_mirror')        

            box.separator()


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        align_function(self.tp_transform, self.tp_axis, self.tp_pivot, self.tp_orient, self.tp_mirror, self.propedit, self.falloff, self.propsize)                               
        return {'FINISHED'} 




           



def align_function_image(tp_axis, tp_pivot2):

        if tp_pivot2 == "CENTER":
            bpy.context.space_data.pivot_point = 'CENTER'

        if tp_pivot2 == "MEDIAN":
            bpy.context.space_data.pivot_point = 'MEDIAN'

        if tp_pivot2 == "CURSOR":
            bpy.context.space_data.pivot_point = 'CURSOR'   

        if tp_axis == "axis_x":
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        if tp_axis == "axis_y":
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        if tp_axis == "axis_xy":
            bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


      
class VIEW3D_TP_Align_UV_Image(bpy.types.Operator):
    """Align UV Image"""
    bl_label = "Align"
    bl_idname = "tp_ops.align_uv_image"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis = bpy.props.EnumProperty(
        items=[("axis_x"    ,"X"    ,""),
               ("axis_y"    ,"Y"    ,""),
               ("axis_xy"   ,"XY"   ,"")],
               name = " ",
               default = "axis_x")

    bpy.types.Scene.tp_pivot2 = bpy.props.EnumProperty(
        items=[("CENTER"  ,"Box Center"   ,""  ,"ROTATE"       ,0),
               ("MEDIAN"  ,"Median Point" ,""  ,"ROTATECENTER" ,1),
               ("CURSOR"  ,"2D Cursor"    ,""  ,"CURSOR"       ,2)],
               name = "Pivot", 
               default = "CENTER")

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        align_function_image(self.tp_axis, bpy.context.scene.tp_pivot2)                               
        return {'FINISHED'} 





def align_function_graph(tp_axis, tp_pivot3):

        if tp_pivot3 == "BOUNDING_BOX_CENTER":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

        if tp_pivot3 == "INDIVIDUAL_ORIGINS":
            bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'

        if tp_pivot3 == "CURSOR":
            bpy.context.space_data.pivot_point = 'CURSOR'   


        if tp_axis == "axis_x":
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        if tp_axis == "axis_y":
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        if tp_axis == "axis_xy":
            bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


      
class VIEW3D_TP_Align_Graph(bpy.types.Operator):
    """Align Graph"""
    bl_label = "Align"
    bl_idname = "tp_ops.align_graph"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis = bpy.props.EnumProperty(
        items=[("axis_x"    ,"X"    ,""),
               ("axis_y"    ,"Y"    ,""),
               ("axis_xy"   ,"XY"   ,"")],
               name = " ",
               default = "axis_x")

    bpy.types.Scene.tp_pivot3 = bpy.props.EnumProperty(
        items=[("BOUNDING_BOX_CENTER"  ,"Box Center"   ,""  ,"ROTATE"           ,0),
               ("INDIVIDUAL_ORIGINS"   ,"Individuals"  ,""  ,"ROTATECOLLECTION" ,1),
               ("CURSOR"               ,"2D Cursor"    ,""  ,"CURSOR"           ,2)],
               name = "Pivot", 
               default = "BOUNDING_BOX_CENTER") 

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        align_function_graph(self.tp_axis, bpy.context.scene.tp_pivot3)                               
        return {'FINISHED'} 





def align_function_node(tp_axis):

        if tp_axis == "axis_x":
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        if tp_axis == "axis_y":
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

      
class VIEW3D_TP_Align_Node(bpy.types.Operator):
    """Align Node"""
    bl_label = "Align"
    bl_idname = "tp_ops.align_node"
    bl_options = {'REGISTER', 'UNDO'}
    
    tp_axis = bpy.props.EnumProperty(
        items=[("axis_x"   ,"X"   ,""),
               ("axis_y"   ,"Y"   ,"")],
               name = " ",
               default = "axis_x")

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        align_function_node(self.tp_axis)                               
        return {'FINISHED'} 

class VIEW3D_TP_Clear_Location(bpy.types.Operator):
    """Clear Location"""
    bl_label = "Clear Location"
    bl_idname = "tp_ops.location_clear"
    bl_options = {'REGISTER', 'UNDO'}

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        bpy.ops.object.location_clear()                       
        return {'FINISHED'} 

class VIEW3D_TP_Clear_Rotation(bpy.types.Operator):
    """Clear Rotation"""
    bl_label = "Clear Rotation"
    bl_idname = "tp_ops.rotation_clear"
    bl_options = {'REGISTER', 'UNDO'}

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        bpy.ops.object.rotation_clear()                  
        return {'FINISHED'} 

class VIEW3D_TP_Clear_Scale(bpy.types.Operator):
    """Clear Scale"""
    bl_label = "Clear Scale"
    bl_idname = "tp_ops.scale_clear"
    bl_options = {'REGISTER', 'UNDO'}

    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        bpy.ops.object.scale_clear()                    
        return {'FINISHED'} 





# REGISTER #
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()




