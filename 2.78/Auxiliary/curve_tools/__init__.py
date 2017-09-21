bl_info = {
    "name": "Curve Tools 2",
    "description": "Adds some functionality for bezier/nurbs curve/surface modeling",
    "author": "Mackraken, guy lateur, Meta-Androcto, MKB",
    "version": (0, 2, 0),
    "blender": (2, 71, 0),
    "location": "View3D > Tool Shelf > Addons Tab",
    "warning": "WIP",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Curve/Curve_Tools",
    "tracker_url": "https://developer.blender.org/maniphest/task/edit/form/2/",
    "category": "Add Curve"}




import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'curve_tools'))

if "bpy" in locals():
    
    import importlib    

    importlib.reload(Properties)
    importlib.reload(Operators)
    importlib.reload(auto_loft)
    importlib.reload(curve_outline)
    importlib.reload(curve_normalize)
    importlib.reload(curve_remove_doubles)
    importlib.reload(add_simple_curve)
    importlib.reload(curve_extend)
    importlib.reload(curve_first_points)
    importlib.reload(curve_simplify)
    importlib.reload(curve_split)
    importlib.reload(curve_trim)

    print("Reloaded multifiles")

else:

    from . import Properties
    from . import Operators
    from . import auto_loft
    from . import curve_outline
    from . import curve_normalize
    from . import curve_remove_doubles
    from . import add_simple_curve
    from . import curve_extend
    from . import curve_first_points
    from . import curve_simplify
    from . import curve_split
    from . import curve_trim

    print("Imported multifiles")



import bpy
from bpy.props import*
from bpy.types import AddonPreferences, PropertyGroup


def UpdateDummy(object, context):
    scene = context.scene
    SINGLEDROP = scene.UTSingleDrop
    DOUBLEDROP = scene.UTDoubleDrop
    LOFTDROP = scene.UTLoftDrop
    TRIPLEDROP = scene.UTTripleDrop
    UTILSDROP = scene.UTUtilsDrop



class CurveTools2Settings(PropertyGroup):
    # selection
    SelectedObjects = CollectionProperty(
                        type=Properties.CurveTools2SelectedObject
                        )
    NrSelectedObjects = IntProperty(
                        name="NrSelectedObjects",
                        default=0,
                        description="Number of selected objects",
                        update=UpdateDummy
                        )
    # NrSelectedObjects = IntProperty(name="NrSelectedObjects", default=0, description="Number of selected objects")

    # curve
    CurveLength = FloatProperty(
                        name="CurveLength",
                        default=0.0,
                        precision=6
                        )
    # splines
    SplineResolution = IntProperty(
                        name="SplineResolution",
                        default=64,
                        min=2, max=1024,
                        soft_min=2,
                        description="Spline resolution will be set to this value"
                        )
    SplineRemoveLength = FloatProperty(
                        name="SplineRemoveLength",
                        default=0.001,
                        precision=6,
                        description="Splines shorter than this threshold length will be removed"
                        )
    SplineJoinDistance = FloatProperty(
                        name="SplineJoinDistance",
                        default=0.001,
                        precision=6,
                        description="Splines with starting/ending points closer to each other "
                                    "than this threshold distance will be joined"
                        )
    SplineJoinStartEnd = BoolProperty(
                        name="SplineJoinStartEnd",
                        default=False,
                        description="Only join splines at the starting point of one and the ending point of the other"
                        )
    splineJoinModeItems = (
                        ('At midpoint', 'At midpoint', 'Join splines at midpoint of neighbouring points'),
                        ('Insert segment', 'Insert segment', 'Insert segment between neighbouring points')
                        )
    SplineJoinMode = EnumProperty(
                        items=splineJoinModeItems,
                        name="SplineJoinMode",
                        default='At midpoint',
                        description="Determines how the splines will be joined"
                        )
    # curve intersection
    LimitDistance = FloatProperty(
                        name="LimitDistance",
                        default=0.0001,
                        precision=6,
                        description="Displays the result of the curve length calculation"
                        )

    intAlgorithmItems = (
                        ('3D', '3D', 'Detect where curves intersect in 3D'),
                        ('From View', 'From View', 'Detect where curves intersect in the RegionView3D')
                        )
    IntersectCurvesAlgorithm = EnumProperty(
                        items=intAlgorithmItems,
                        name="IntersectCurvesAlgorithm",
                        description="Determines how the intersection points will be detected",
                        default='3D'
                        )
    intModeItems = (
                    ('Insert', 'Insert', 'Insert points into the existing spline(s)'),
                    ('Split', 'Split', 'Split the existing spline(s) into 2'),
                    ('Empty', 'Empty', 'Add empty at intersections')
                    )
    IntersectCurvesMode = EnumProperty(
                    items=intModeItems,
                    name="IntersectCurvesMode",
                    description="Determines what happens at the intersection points",
                    default='Split'
                    )
    intAffectItems = (
                    ('Both', 'Both', 'Insert points into both curves'),
                    ('Active', 'Active', 'Insert points into active curve only'),
                    ('Other', 'Other', 'Insert points into other curve only')
                    )
    IntersectCurvesAffect = EnumProperty(
                    items=intAffectItems,
                    name="IntersectCurvesAffect",
                    description="Determines which of the selected curves will be affected by the operation",
                    default='Both'
                    )





def draw_curve_panel_layout(self, context, layout):
    
        scene = context.scene
        SINGLEDROP = scene.UTSingleDrop
        DOUBLEDROP = scene.UTDoubleDrop
        LOFTDROP = scene.UTLoftDrop
        TRIPLEDROP = scene.UTTripleDrop
        UTILSDROP = scene.UTUtilsDrop
        layout = self.layout
        
        if context.mode == "OBJECT":
            layout.menu("INFO_MT_simple_menu", text="Simple 2D Curves", icon="MOD_CURVE")


        # Z. selection
        boxSelection = self.layout.box()
        row = boxSelection.row(align=True)
        row.operator("curvetools2.operatorselectioninfo", text="Selection Info")
        row.prop(context.scene.curvetools, "NrSelectedObjects", text="")

        # Single Curve options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTSingleDrop", icon="TRIA_DOWN")
        if SINGLEDROP:
            # A. 1 curve
            row = col.row(align=True)
            row.label(text="Single Curve:")
            row = col.row(align=True)

            # A.1 curve info/length
            row.operator("curvetools2.operatorcurveinfo", text="Curve info")
            row = col.row(align=True)
            row.operator("curvetools2.operatorcurvelength", text="Calc Length")
            row.prop(context.scene.curvetools, "CurveLength", text="")

            # A.2 splines info
            row = col.row(align=True)
            row.operator("curvetools2.operatorsplinesinfo", text="Curve splines info")

            # A.3 segments info
            row = col.row(align=True)
            row.operator("curvetools2.operatorsegmentsinfo", text="Curve segments info")

            # A.4 origin to spline0start
            #row = col.row(align=True)
            #row.operator("curvetools2.operatororigintospline0start", text="Set origin to spline start")

        # Double Curve options
        box2 = self.layout.box()
        col = box2.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTDoubleDrop", icon="TRIA_DOWN")

        if DOUBLEDROP:
            # B. 2 curves
            row = col.row(align=True)
            row.label(text="2 curves:")

            # B.1 curve intersections
            row = col.row(align=True)
            row.operator("curvetools2.operatorintersectcurves", text="Intersect curves")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "LimitDistance", text="LimitDistance")
            # row.active = (context.scene.curvetools.IntersectCurvesAlgorithm == '3D')

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "IntersectCurvesAlgorithm", text="Algorithm")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "IntersectCurvesMode", text="Mode")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "IntersectCurvesAffect", text="Affect")

        # Loft options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTLoftDrop", icon="TRIA_DOWN")

        if LOFTDROP:
            # B.2 surface generation
            wm = context.window_manager
            scene = context.scene
            row = col.row(align=True)
            row.operator("curvetools2.create_auto_loft")
            
            col = box1.column(align=True)
            row = col.column_flow(2)              
            lofters = [o for o in scene.objects if "autoloft" in o.keys()]
            for o in lofters:             
                row.label(o.name)
           
            col = box1.column(align=True)
            row = col.row(align=True)
            row.prop(wm, "auto_loft", toggle=True)

        # Advanced options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTTripleDrop", icon="TRIA_DOWN")
        if TRIPLEDROP:
            # C. 3 curves
            row = col.column(align=True)        
            row.operator("object._curve_outline", text="Curve Outline")
           
            if context.mode == "OBJECT":
                row.operator("object.sep_outline", text="Separate Outline")                
                row.operator("curve.simplify", text="Simplify")
                row.operator("curvetools2.operatorbirail", text="Birail")
                row.operator("curvetools2.operatororigintospline0start", text="FirstPoint")
  
            elif context.mode == "EDIT_CURVE":

                vertex = []
                selected = []
                n = 0
                obj = context.active_object
                if obj is not None:
                    if obj.type == 'CURVE':
                        for i in obj.data.splines:
                            for j in i.bezier_points:
                                n += 1
                                if j.select_control_point:
                                    selected.append(n)
                                    vertex.append(obj.matrix_world * j.co)

                    if len(vertex) > 0 and n > 2:
                        simple_edit = row.operator("curve.bezier_points_fillet", text='Fillet')
                  
                    if len(vertex) == 2 and abs(selected[0] - selected[1]) == 1:
                        simple_divide = row.operator("curve.bezier_spline_divide", text='Divide')


                row.operator("bpt.bezier_curve_split", text="Split")
                row.operator("curve.trim_tool", text="Trim")
                row.operator("curve.extend_tool", text="Extend")
                
                row.operator("curve.surfsk_first_points", text="FirstPoints")
                row.operator("curve.remove_doubles")
                
                

        # Utils Curve options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTUtilsDrop", icon="TRIA_DOWN")

        if UTILSDROP:
           
            # D.1 set spline resolution
            row = col.row(align=True)
            row.operator("dynamic.normalize", text="", icon='KEYTYPE_JITTER_VEC')  
            row.prop(context.object.data, "resolution_u", text=" Set Resolution")
            #row.operator("curvetools2.operatorsplinessetresolution", text="Set resolution")
            #row.prop(context.scene.curvetools, "SplineResolution", text="")
            active_wire = bpy.context.object.show_wire 
            if active_wire == True:
                row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
            else:                       
                row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID')  
      
            # D.2 remove splines
            row = col.row(align=True)
            row.operator("curvetools2.operatorsplinesremovezerosegment", text="Remove 0-segments splines")

            row = col.row(align=True)
            row.operator("curvetools2.operatorsplinesremoveshort", text="Remove short splines")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "SplineRemoveLength", text="Threshold remove")

            # D.3 join splines
            row = col.row(align=True)
            row.operator("curvetools2.operatorsplinesjoinneighbouring", text="Join neighbouring splines")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinDistance", text="Threshold join")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinStartEnd", text="Only at start & end")

            row = col.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinMode", text="Join mode")




class VIEW3D_CurvePanel_TOOLS(bpy.types.Panel):
    bl_category = "Tools"
    bl_idname = "VIEW3D_CurvePanel_TOOLS"
    bl_label = "Curve Tools 2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        #need for complete empty 3d view 
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE'

    def draw(self, context):
         layout = self.layout
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_curve_panel_layout(self, context, layout)         


class VIEW3D_CurvePanel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_CurvePanel_UI"
    bl_label = "Curve Tools 2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        #need for complete empty 3d view 
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE'

    def draw(self, context):
         layout = self.layout 
         layout.operator_context = 'INVOKE_REGION_WIN'

         draw_curve_panel_layout(self, context, layout) 



# Addons Preferences Update Panel
def update_panel(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_CurvePanel_UI)        
        bpy.utils.unregister_class(VIEW3D_CurvePanel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_CurvePanel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':

        VIEW3D_CurvePanel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.category

        bpy.utils.register_class(VIEW3D_CurvePanel_TOOLS)

    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_CurvePanel_UI)

  



class CurveAddonPreferences(AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    category = bpy.props.StringProperty(name="Category", description="Choose a name for the category of the panel", default="Tools", update=update_panel)

    tab_location = bpy.props.EnumProperty(
        name = 'Shelf Location',
        description = 'Choose shelf location for the panel',
        items=(('tools', 'Tool Shelf [T]', 'place panel in the 3d view tool shelf [T] / left side'),
               ('ui', 'Property Shelf [N]', 'place panel in the  3d view property shelf [N] / right side')),
               default='tools', update = update_panel)

    def draw(self, context):

        layout = self.layout
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(self, 'tab_location', expand=True)

        if self.tab_location == 'tools':
            row = col.row(align=True)
            row.label(text="Category:")
            row.prop(self, "category", text="")            



# AutoLoft 
def run_auto_loft(self, context):
    if self.auto_loft:
        bpy.ops.wm.auto_loft_curve()
    return None



# Registration
import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.Scene.UTSingleDrop = BoolProperty(
                                    name="Single Curve",
                                    default=False,
                                    description="Single Curve"
                                    )
    bpy.types.Scene.UTDoubleDrop = BoolProperty(
                                    name="Two Curves",
                                    default=False,
                                    description="Two Curves"
                                    )
    bpy.types.Scene.UTLoftDrop = BoolProperty(
                                    name="Two Curves Loft",
                                    default=False,
                                    description="Two Curves Loft"
                                    )
    bpy.types.Scene.UTTripleDrop = BoolProperty(
                                    name="Advanced",
                                    default=False,
                                    description="Advanced"
                                    )
    bpy.types.Scene.UTUtilsDrop = BoolProperty(
                                    name="Curves Utils",
                                    default=False,
                                    description="Curves Utils"
                                    )

    bpy.types.Scene.curvetools = bpy.props.PointerProperty(type=CurveTools2Settings)
    bpy.types.WindowManager.auto_loft = BoolProperty(default=False, name="Auto Loft", update=run_auto_loft)



def unregister():
    
    del bpy.types.Scene.UTSingleDrop
    del bpy.types.Scene.UTDoubleDrop
    del bpy.types.Scene.UTLoftDrop
    del bpy.types.Scene.UTTripleDrop
    del bpy.types.Scene.UTUtilsDrop

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
if __name__ == "__main__":
    register()
