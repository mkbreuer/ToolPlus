# LOAD MODUL #    
import bpy, bmesh
from bpy import *
from bpy.props import *
#from . icons.icons import load_icons   


def func_align_mesh(self):

    view_layer = bpy.context.view_layer        
    selected = bpy.context.selected_objects
    active = view_layer.objects.active 

    current_pivot = bpy.context.scene.tool_settings.transform_pivot_point
    current_select_mode = bpy.context.tool_settings.mesh_select_mode[0]
    current_select_mode = bpy.context.tool_settings.mesh_select_mode[1]
    current_select_mode = bpy.context.tool_settings.mesh_select_mode[2]

    #me = bpy.context.object.data
    #bm = bmesh.from_edit_mesh(me)
    #current_select_mode = bm.select_mode[0]
    #current_select_mode = bm.select_mode[1]
    #current_select_mode = bm.select_mode[2]

    if self.set_pivot == "ACTIVE_ELEMENT":
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

    if self.set_pivot == "MEDIAN_POINT":
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

    if self.set_pivot == "BOUNDING_BOX_CENTER":
        bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'       

    if self.set_pivot == "CURSOR":
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR' 


    if self.use_align_axis == "axis_n":
      
        value_x = 1
        value_y = 1
        value_z = 0            
        axis_x = False
        axis_y = False
        axis_z = True
        
        #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type="FACE")
        #bpy.context.tool_settings.mesh_select_mode = (False, False, True)

        me = bpy.context.object.data
        bm = bmesh.from_edit_mesh(me)
        #bm.select_mode = {'VERT', 'EDGE', 'FACE'}      
        #selected_verts = [v.select for v in bm.verts]
        #selected_edges = [e.select for e in bm.edges]
        selected_faces = [f.select for f in bm.faces]
        if selected_faces:
            self.report({'INFO'},"%d faces selected" % len(selected_faces))

            bpy.ops.transform.resize(value=(value_x, value_y, value_z), orient_type=self.set_orient_type_normal, 
                                     constraint_axis=(axis_x, axis_y, axis_z), mirror=self.use_mirror, 
                                     use_proportional_edit=self.use_prop_edit, proportional_edit_falloff=self.use_prop_falloff, proportional_size=self.use_prop_size, 
                                     use_proportional_connected=self.use_prop_connected, use_proportional_projected=self.use_prop_projected)
        else:
            self.report({'WARNING'},"No active face selected")
        
    else:            

        if self.use_align_axis == "axis_x":
            value_x = 0
            value_y = 1
            value_z = 1
            axis_x = True
            axis_y = False
            axis_z = False

        if self.use_align_axis == "axis_y":
            value_x = 1
            value_y = 0
            value_z = 1
            axis_x = False
            axis_y = True
            axis_z = False
    
        if self.use_align_axis == "axis_z":
            value_x = 1
            value_y = 1
            value_z = 0            
            axis_x = False
            axis_y = False
            axis_z = True

        if self.use_align_axis == "axis_xy":
            value_x = 0
            value_y = 0
            value_z = 1
            axis_x = True
            axis_y = True
            axis_z = False

        if self.use_align_axis == "axis_zx":
            value_x = 0
            value_y = 1
            value_z = 0
            axis_x = True
            axis_y = False
            axis_z = True

        if self.use_align_axis == "axis_zy":
            value_x = 1
            value_y = 0
            value_z = 0
            axis_x = False
            axis_y = True
            axis_z = True
    
        if self.use_align_axis == "axis_xyz":
            value_x = 0
            value_y = 0
            value_z = 0            
            axis_x = True
            axis_y = True
            axis_z = True

        bpy.ops.transform.resize(value=(value_x, value_y, value_z), orient_type=self.set_orient_type, 
                                 constraint_axis=(axis_x, axis_y, axis_z), mirror=self.use_mirror, 
                                 use_proportional_edit=self.use_prop_edit, proportional_edit_falloff=self.use_prop_falloff, proportional_size=self.use_prop_size, 
                                 use_proportional_connected=self.use_prop_connected, use_proportional_projected=self.use_prop_projected)

        #bm.select_mode = current_select_mode[0]
        #bm.select_mode = current_select_mode[1]
        #bm.select_mode = current_select_mode[2]
        bpy.context.tool_settings.mesh_select_mode[0] = current_select_mode
        bpy.context.tool_settings.mesh_select_mode[1] = current_select_mode
        bpy.context.tool_settings.mesh_select_mode[2] = current_select_mode
        bpy.context.scene.tool_settings.transform_pivot_point = current_pivot   





      
class VIEW3D_OT_align_mesh(bpy.types.Operator):
    """Align mesh in editmode / e.g.: scale xyzn = 0"""
    bl_label = "Align Mesh"
    bl_idname = "tpc_ot.align_mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    set_pivot : bpy.props.EnumProperty(
        items=[("ACTIVE_ELEMENT"        ,"Active Element"   ,""  ,"PIVOT_ACTIVE"    ,0),
               ("MEDIAN_POINT"          ,"Median Point"     ,""  ,"PIVOT_MEDIAN"    ,1),
               ("BOUNDING_BOX_CENTER"   ,"Bound Box Center" ,""  ,"PIVOT_BOUNDBOX"  ,2),
               ("CURSOR"                ,"3D Cursor"        ,""  ,"PIVOT_CURSOR"    ,3)],
               name = "Pivot", 
               default = "ACTIVE_ELEMENT",
               options={'SKIP_SAVE'})

    set_orient_type : bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View"),
               ("CURSOR"    ,"Cursor"     ,"Cursor")],
               name = "Orientation",
               default = "GLOBAL",    
               description = "change manipulator axis")

    set_orient_type_normal : bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View"),
               ("CURSOR"    ,"Cursor"     ,"Cursor")],
               name = "Orientation",
               default = "NORMAL",    
               description = "change manipulator axis",
               options={'SKIP_SAVE'})


    use_align_axis : bpy.props.EnumProperty(
        items=[("axis_x"   ,"X"   ,""),
               ("axis_y"   ,"Y"   ,""),
               ("axis_z"   ,"Z"   ,""),
               ("axis_xy"  ,"Xy"  ,""),
               ("axis_zy"  ,"Zy"  ,""),
               ("axis_zx"  ,"Zx"  ,""),
               ("axis_xyz" ,"XYZ" ,""),
               ("axis_n"   ,"N"   ,"")],
               name = " ",
               default = "axis_x",
               options={'SKIP_SAVE'})

    use_mirror : BoolProperty (name = "Mirror", default= False, description= "mirror over origin")
    
    # PROPORTIONAL EDITING #
    use_prop_edit : BoolProperty (name = "Proportional Editing", default= False, description= "")

    use_prop_falloff : bpy.props.EnumProperty(
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

    use_prop_size : FloatProperty(name="Size",  description= "Proportional Editing Size", min=0.001, max=100.0, default=1.0)
    use_prop_connected : BoolProperty (name = "Connected", default= False, description= "")
    use_prop_projected : BoolProperty (name = "Projected", default= False, description= "")
    
    set_orient_axis : bpy.props.EnumProperty(
        items=[("X"   ,"X"  ,"orient axis"),
               ("Y"   ,"Y"  ,"orient axis"),
               ("Z"   ,"Z"  ,"Cursor")],
               name = "orient axis",
               default = "Z",    
               description = "change orient axis")

    set_align : bpy.props.EnumProperty(
      items = [("WORLD",  "World",  ""),
               ("VIEW",   "View",   ""),                       
               ("CURSOR", "Cursor", "")], 
               name = "Align",
               default = "WORLD",
               description="")


    use_transform : bpy.props.EnumProperty(
        items=[("LOCATION"   ,"Location"  ,""),
               ("ROTATION"   ,"Rotation"  ,""),
               ("SCALE"      ,"Scale"     ,"")],
               name = "Transform",
               default = "LOCATION")


    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(align=True)              
        
        row = box.row(align=True) 
        #row.prop(self, 'use_align_axis', expand =True)
    
        row.prop_enum(self, "use_align_axis", 'axis_x',   text="X") 
        row.prop_enum(self, "use_align_axis", 'axis_y',   text="Y") 
        row.prop_enum(self, "use_align_axis", 'axis_z',   text="Z") 
        row.prop_enum(self, "use_align_axis", 'axis_xy',  text="Xy") 
        row.prop_enum(self, "use_align_axis", 'axis_zy',  text="Zy") 
        row.prop_enum(self, "use_align_axis", 'axis_zx',  text="Zx") 
        row.prop_enum(self, "use_align_axis", 'axis_xyz', text="XYZ") 
        row.prop_enum(self, "use_align_axis", 'axis_n',   text="N") 


        box.separator() 
     
        row = box.row(align=True) 
        row.label(text='Oriention:')      
        if self.use_align_axis == 'axis_n':
            row.prop(self, 'set_orient_type_normal', text="")      
        else:
            row.prop(self, 'set_orient_type', text="")      

        box.separator() 

        row = box.row(align=True) 
        row.label(text='Pivot Point:')      
        row.prop(self, 'set_pivot', text="")    
 
        box.separator()

        box = col.box().column(align=True)   

        row = box.row(align=True) 
        row.prop(self, 'use_prop_edit', text="")
        row.label(text="Proportional Editing")
        
        if self.use_prop_edit == True:
            box.separator() 

            row = box.row() 
            row.prop(self, 'use_prop_falloff', text="")
            row.prop(self, 'use_prop_size')             
       
            box.separator() 
            
            #row = box.row(align=True) 
            #row.prop(self, 'use_mirror')        
          
            row = box.row(align=True) 
            row.prop(self, 'use_prop_connected')
            row.prop(self, 'use_prop_projected') 


    # EXECUTE MAIN OPERATOR #
    def execute(self, context):                                 
        func_align_mesh(self)                               
        return {'FINISHED'} 


