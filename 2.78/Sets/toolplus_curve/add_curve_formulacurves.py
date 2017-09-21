bl_info = {
    "name": "FormulaCurves",
    "description": "Make FormulaCurves",
    "author": "Peter de Reuver",
    "version": (1, 0),
    "blender": (2, 72, 0),
    "location": "View3D > Add > Curve",
    "warning": "",  # used for warning icon and text in addons panel
    #   "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.4/Py/"
    #               "Scripts/Object/Spirals",
    "category": "Add Curve",
}

import bpy
import time
from bpy.props import *
from math import sin, cos, pi, exp
from bpy_extras.object_utils import AddObjectHelper, object_data_add


# make Curve
#-----------------------------------------------------------------------------
def make_Lorenz(props, context):
    verts = []
    verts.extend([1, 0, 0, 1])
    x = 1
    y = 0
    z = 0
    step = props.length / (props.number_points * 100)
    for i in range(1, props.number_points * 100 - 1):
        px = x + (props.constA * (y - x)) * step
        py = y + (x * (props.constB - z) - y) * step
        pz = z + (x * y - props.constC * z) * step
        x = px
        y = py
        z = pz
        verts.extend([px, py, pz, 1])
    return verts


def make_Rossler(props, context):
    verts = []
    verts.extend([1, 0, 0, 1])
    x = 1
    y = 0
    z = 0
    step = props.length / (props.number_points * 100)
    for i in range(1, props.number_points * 100 - 1):
        px = x - (y + z) * step
        py = y + (x + props.constA * y) * step
        pz = z + (props.constB + z * (x - props.constC)) * step
        x = px
        y = py
        z = pz
        verts.extend([px, py, pz, 1])
    return verts


def make_Tinkerbell(props, context):
    verts = []
    verts.extend([1, 0, 0, 1])
    x = 1
    y = 0
    z = 0
    # dt=props.step
    step = props.length / (props.number_points * 100)
    dt = step
    for i in range(1, props.number_points * 100 - 1):
        px = (x + dt) * (x + dt) - y * y + props.constA * (x + dt) + props.constB * y
        py = 2 * (x + dt) * y - props.constC * (x + dt) + props.constD * y
        pz = z + 0.0001
        x = px
        y = py
        z = pz
        verts.extend([px, py, pz, 1])
    return verts


def make_PickOver(props, context):
    verts = []
    verts.extend([1, 1, 0, 1])
    x = 1
    y = 1
    z = 0
    step = props.length / (props.number_points * 100)
    for i in range(1, props.number_points * 100 - 1):
        px = x * cos(props.constA) - (y - x**x) * sin(props.constA)
        py = x * sin(props.constA) - (y - x**x) * cos(props.constA)
        pz = z + 0.0001  # props.constB
        # px=sin(props.constA*y)-z*cos(props.constB*x)
        # py=z*sin(props.ConstC*x)-cos(props.constD*x)
        # pz=x*sin(props.constAa)

        # px=x*x-y*y+props.constA*x+props.constB*y
        # py=2*x*y-2*x+0.5*y
        # pz=z
        x = px
        y = py
        z = pz
        verts.extend([px, py, pz, 1])
    return verts

#-----------------------------------------------------------------------------


def draw_curve(props, context):

    bpy.ops.object.select_all(action='DESELECT')

    # if props.spiral_type == 1:
    if props.formulaType == 'Lorenz':
        verts = make_Lorenz(props, context)
    # if props.spiral_type == 2:
    elif props.formulaType == 'Rossler':
        verts = make_Rossler(props, context)
    # if props.spiral_type == 3:
    elif props.formulaType == 'Tinkerbell':
        verts = make_Tinkerbell(props, context)
    elif props.formulaType == 'PickOver':
        verts = make_Roskenn(props, context)

    curve_data = bpy.data.curves.new(name='FormulaCurve', type='CURVE')
    curve_data.dimensions = '3D'
    curve_data.fill_mode = 'FULL'
    curve_data.resolution_u = 3
    curve_data.bevel_depth = props.bevel
    curve_data.extrude = props.extrude
    curve_data.bevel_resolution = 3

    # if props.curve_type == 0:
    if props.outputType == 'POLY':
        spline = curve_data.splines.new(type='POLY')
    # elif props.curve_type == 1:
    elif props.outputType == 'NURBS':
        spline = curve_data.splines.new(type='NURBS')

    spline.points.add(len(verts) * 0.25 - 1)  # Add only one quarter of points as elements in verts, because verts looks like: "x,y,z,?,x,y,z,?,x,..."
    spline.points.foreach_set('co', verts)
    new_obj = object_data_add(context, curve_data)
    bpy.ops.object.shade_smooth()
    # print(curve_data.name)
    # big=max(bpy.data.objects[curve_data.name].dimensions.x,bpy.data.objects[curve_data.name].dimensions.y,bpy.data.objects[curve_data.name].dimensions.z)
    scaleXX = min(1, props.scaleX / bpy.data.objects[curve_data.name].dimensions.x)
    scaleYY = min(1, props.scaleY / bpy.data.objects[curve_data.name].dimensions.y)
    scaleZZ = min(1, props.scaleZ / bpy.data.objects[curve_data.name].dimensions.z)
    # print(scale2)
    # scale2=2/max(new_obj.dimensions.x,new_obj.dimensions.y,new_obj.dimensions.z)
    #bpy.ops.transform.resize(value=(props.scale,props.scale, props.scale), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='LINEAR', proportional_size=1.8052)
    bpy.ops.transform.resize(value=(scaleXX, scaleYY, scaleZZ), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='LINEAR', proportional_size=1.8052)


class formulacurves(bpy.types.Operator):
    bl_idname = "curve.formulacurves"
    bl_label = "FormulaCurves"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}  # UNDO needed for operator redo and therefore also to let the addobjecthelp appear!!!
    bl_description = "adds different types of formula curves"
    # oldT='PickOver'

    FormulaTypes = [
        ('Lorenz', 'Lorenz', 'Lorenz'),
        ('Rossler', 'Rossler', 'Rossler')]  # ,
    #   ('Tinkerbell', 'Tinkerbell', 'Tinkerbell'),
    #  ('PickOver', 'Pickover', 'PickOver')]
    formulaType = EnumProperty(name="Type",
                               description="Form of Curve to create",
                               items=FormulaTypes)

    SplineTypes = [
        ('POLY', 'Poly', 'POLY'),
        ('NURBS', 'Nurbs', 'NURBS')]
    #,('BEZIER', 'Bezier', 'BEZIER')]
    outputType = EnumProperty(name="Output splines",
                              description="Type of splines to output",
                              items=SplineTypes)
    oldT = EnumProperty(name="Type",
                        description="Form of Curve to create",
                        items=FormulaTypes)

    number_points = IntProperty(default=25, min=10, max=100, description="Resolution")
    length = IntProperty(default=50, min=10, max=500, description="Length")

    scaleX = FloatProperty(default=2, min=0.1, max=10, description="Scale x")
    scaleY = FloatProperty(default=2, min=0.1, max=10, description="Scale y")
    scaleZ = FloatProperty(default=2, min=0.1, max=10, description="Scale z")

    extrude = FloatProperty(default=0, min=0, max=10, description="Extrude")
    bevel = FloatProperty(default=0.15, min=0.01, max=10, description="Bevel")

    constA = FloatProperty(default=10.0, min=-100.00, max=100.00, description="constant A")
    constB = FloatProperty(default=28.0, min=-100.00, max=100.00, description="constant B")
    constC = FloatProperty(default=8 / 7, min=-100.00, max=100.00, description="constant C")
    constD = FloatProperty(default=-2.43, min=-100.00, max=100.00, description="constant D")

    #touch = BoolProperty(default=False, description="No empty spaces between cycles")

    def draw(self, context):  # Function used by Blender to draw the menu
        if not(self.formulaType == self.oldT):
            if self.formulaType == 'Lorenz':
                self.constA = 10
                self.constB = 28
                self.constC = 8 / 3

            if self.formulaType == 'Rossler':
                self.constA = 0.2
                self.constB = 0.2
                self.constC = 5.7

            if self.formulaType == 'Tinkerbell':
                self.constA = 0.9
                self.constB = 0.6
                self.constC = 2.0
                self.constD = 0.5

            if self.formulaType == 'PickOver':
                self.constA = 2.24
                self.constB = 0.43
                self.constC = -0.65
                self.constD = -2.43
            self.oldT = self.formulaType
        layout = self.layout
        col = layout.column()
        col.prop(self, 'formulaType')

        col = layout.column()
        layout.label(text="Bcurve Generate W:")
        #col.row().prop(self, 'outputType', expand=True)
        layout.prop(self, 'outputType', expand=True)
        #layout.prop(self, 'curve_type', text="Curve Type")
        layout.prop(self, 'number_points', text="# points (*100)")
        #layout.prop(self, 'step', text = "Step")
        layout.prop(self, 'scaleX', text="Scale x")
        layout.prop(self, 'scaleY', text="Scale y")
        layout.prop(self, 'scaleZ', text="Scale z")
        layout.label(text="Curve appearance:")
        layout.prop(self, 'extrude', text="Extrude")
        layout.prop(self, 'bevel', text="Bevel")
        layout.label(text=self.formulaType + " Options:")
        box = layout.box()
        box.prop(self, 'length', text="length of curve")
        box.prop(self, 'constA', text="Constant A")
        box.prop(self, 'constB', text="Constant B")
        box.prop(self, 'constC', text="Constant C")
        if self.formulaType == 'Tinkerbell':
            box.prop(self, 'constD', text="Constant D")
        if self.formulaType == 'PickOver':
            box.prop(self, 'constD', text="Constant D")

            #    box2 = box.box()
            #    box2.prop(self, 'dif_z', text = "Height per Cycle")
            #    box2.prop(self, 'touch', text = "Make Snail")

    @classmethod
    def poll(cls, context):  # method called by blender to check if the operator can be run
        return context.scene != None

    def execute(self, context):
        # turn off undo
        undo = bpy.context.user_preferences.edit.use_global_undo
        bpy.context.user_preferences.edit.use_global_undo = False

        time_start = time.time()
        draw_curve(self, context)
        print("Drawing FormulaCurve Finished: %.4f sec", time.time() - time_start)
        # restore pre operator undo state
        bpy.context.user_preferences.edit.use_global_undo = undo
        return {'FINISHED'}


# Registration

def formulacurve_button(self, context):
    self.layout.operator(
        formulacurves.bl_idname,
        text="Add FormulaCurve",
        icon='PLUGIN'
    )


def register():
    bpy.utils.register_class(formulacurves)
    bpy.types.VIEW3D_MT_object.append(formulacurve_button)
    bpy.types.INFO_MT_curve_add.append(formulacurve_button)


def unregister():
    bpy.utils.unregister_class(formulacurves)
    bpy.types.INFO_MT_curve_add.remove(formulacurve_button)
    bpy.types.VIEW3D_MT_object.remove(formulacurve_button)

if __name__ == "__main__":
    register()
