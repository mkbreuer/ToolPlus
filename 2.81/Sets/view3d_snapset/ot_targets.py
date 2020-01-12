# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


class VIEW3D_OT_pivot_target(bpy.types.Operator):
    """set pivot point"""
    bl_idname = "tpc_ot.set_pivot"
    bl_label = "Set Pivot"
    bl_options = {'REGISTER', 'UNDO'}

    tpc_pivot : bpy.props.EnumProperty(
                 items=[("BOUNDING_BOX_CENTER"  ," "    ,""   ,"ROTATE"            , 1),
                        ("CURSOR"               ," "    ,""   ,"CURSOR"            , 2),
                        ("INDIVIDUAL_ORIGINS"   ," "    ,""   ,"ROTATECOLLECTION"  , 3),
                        ("MEDIAN_POINT"         ," "    ,""   ,"ROTATECENTER"      , 4),
                        ("ACTIVE_ELEMENT"       ," "    ,""   ,"ROTACTIVE"         , 5)],
                        name = "Pivot", 
                        default = "BOUNDING_BOX_CENTER")


    tpc_align : BoolProperty(name="Only Origins",description="manipulate center points", default=False)

    def draw(self, context):
        layout = self.layout.column(align = True)  

        box = layout.box().column(align = True)  
        
        row = box.column(align = True)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_pivot',text=" ", expand =True)                                            
     
        box.separator()
        
        row = box.column(align = True)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_align',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):

        if self.tpc_pivot == "BOUNDING_BOX_CENTER":
            bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'          

        elif self.tpc_pivot == "CURSOR":
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR' 

        elif self.tpc_pivot == "INDIVIDUAL_ORIGINS":
            bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'           

        elif self.tpc_pivot == "MEDIAN_POINT":
            bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'                        

        elif self.tpc_pivot == "ACTIVE_ELEMENT":
            bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
        
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = self.tpc_align

        # header info
        #context.area.header_text_set("SnapSet: %s" % (self.tpc_pivot))   
        return {'FINISHED'}
    
    
               
class VIEW3D_OT_orient_axis(bpy.types.Operator):
    """set transform axis orientation"""
    bl_idname = "tpc_ot.orient_axis"
    bl_label = "Transform Axis Orientation"
    bl_options = {'REGISTER', 'UNDO'}

    tpc_axis : bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View"),
               ("CURSOR"    ,"Cursor"   ,"Cursor")],
               name = "Orientation",
               default = "GLOBAL",    
               description = "change manipulator axis")

    def draw(self, context):
        layout = self.layout.column(align = True)  

        box = layout.box().column(align = True)  
        
        row = box.column(align = True)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_axis',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):
        
        if self.tpc_axis == "GLOBAL":
            bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'                           
       
        elif self.tpc_axis == "LOCAL":
            bpy.context.scene.transform_orientation_slots[0].type = 'LOCAL' 
       
        elif self.tpc_axis == "NORMAL":
            bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'            
       
        elif self.tpc_axis == "GIMBAL":
             bpy.context.scene.transform_orientation_slots[0].type = 'GIMBAL'            
       
        elif self.tpc_axis == "VIEW":
            bpy.context.scene.transform_orientation_slots[0].type = 'VIEW'      
        
        elif self.tpc_axis == "CURSOR":
            bpy.context.scene.transform_orientation_slots[0].type = 'CURSOR'

        # header info
        #context.area.header_text_set("SnapSet: %s" % (self.tpc_axis))  
        return {'FINISHED'}



class VIEW3D_OT_set_orientation(bpy.types.Operator):
    """creates custom transform orientation and overwrite"""
    bl_idname = "tpc_ot.set_orientation"
    bl_label = "Custom Orientation"
    bl_options = {'REGISTER', 'UNDO'}

    set_orientation_name : StringProperty(name="User Input", default="Custom", description="")
    use_view : BoolProperty(name="Use View",description="", default=False)
    use : BoolProperty(name="Use after creation",description="", default=True)
    overwrite : BoolProperty(name="Overwrite Previous",description="", default=True)

    def execute(self, context):
        snap_global = context.window_manager.snap_global_props     
        bpy.ops.transform.create_orientation(name=snap_global.set_orientation_name, use_view=self.use_view, use=self.use, overwrite=self.overwrite)
        return {"FINISHED"}



class VIEW3D_OT_snap_target(bpy.types.Operator):
    """set snap target"""
    bl_idname = "tpc_ot.snap_target"
    bl_label = "Snap Target"
    bl_options = {'REGISTER', 'UNDO'}

    tpc_snapt : bpy.props.EnumProperty(
                 items=[("CLOSEST"   ,"Closest"  ,"Closest"  ,"" , 1),
                        ("CENTER"    ,"Center"   ,"Center"   ,"" , 2),
                        ("MEDIAN"    ,"Median"   ,"Median"   ,"" , 3),
                        ("ACTIVE"    ,"Active"   ,"Active"   ,"" , 4)],
                        name = "Snap Target", 
                        default = "CLOSEST")

    def draw(self, context):
        layout = self.layout.column(align = True)  

        box = layout.box().column(align = True)  
        
        row = box.column(align = True)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_snapt',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):
  
        if self.tpc_snapt == "CLOSEST":
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'         
     
        elif self.tpc_snapt == "CENTER":
            bpy.context.scene.tool_settings.snap_target = 'CENTER'
     
        elif self.tpc_snapt == "MEDIAN":
            bpy.context.scene.tool_settings.snap_target = 'MEDIAN'        
     
        elif self.tpc_snapt == "ACTIVE":
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
    
        # header info
        #context.area.header_text_set("SnapSet: %s" % (self.tpc_snapt)) 
        return {'FINISHED'}




class VIEW3D_OT_snap_element(bpy.types.Operator):
    """set snap elements"""
    bl_idname = "tpc_ot.snap_element"
    bl_label = "Snap Element"
    bl_options = {'REGISTER', 'UNDO'}

    tpc_snape : EnumProperty(
         items=[("INCREMENT"          ,"Increment"   ,"" ,"SNAP_INCREMENT"     , 1),
                ("VERTEX"             ,"Vertex"      ,"" ,"SNAP_VERTEX"        , 2),
                ("EDGE"               ,"Edge"        ,"" ,"SNAP_EDGE"          , 3),
                ("FACE"               ,"Face"        ,"" ,"SNAP_FACE"          , 4),
                ("VOLUME"             ,"Volume"      ,"" ,"SNAP_VOLUME"        , 5),
                ("EDGE_MIDPOINT"      ,"MidPoint"    ,"" ,"SNAP_MIDPOINT"      , 6),
                ("EDGE_PERPENDICULAR" ,"Perpendic"   ,"" ,"SNAP_PERPENDICULAR" , 7)],
                name = "Snap Element", 
                default = "INCREMENT")

    def draw(self, context):
        layout = self.layout.column(align = True)  

        box = layout.box().column(align = True)  
        
        row = box.column(align = True)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_snape',text=" ", expand=True)                                            
  
        box.separator()


    def execute(self, context):
        
        # seven_elements = [self.tpc_increment, self.tpc_vertex, self.tpc_edge, self.tpc_face, self.tpc_volume, self.tpc_midpoint, self.tpc_perpendic]                                                            
        # if seven_elements == True:   
        #    bpy.context.scene.tool_settings.snap_elements = {'INCREMENT', 'VERTEX', 'EDGE', 'FACE', 'VOLUME', 'EDGE_MIDPOINT', 'EDGE_PERPENDICULAR'}

        if self.tpc_snape == "INCREMENT":                        
            bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}

        if self.tpc_snape == "VERTEX":
            bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}   
  
        if self.tpc_snape == "EDGE":
            bpy.context.scene.tool_settings.snap_elements = {'EDGE'}    
    
        if self.tpc_snape == "FACE":
            bpy.context.scene.tool_settings.snap_elements = {'FACE'}                      
    
        if self.tpc_snape == "VOLUME":
            bpy.context.scene.tool_settings.snap_elements = {'VOLUME'}   
   
        if self.tpc_snape == "EDGE_MIDPOINT":
            bpy.context.scene.tool_settings.snap_elements = {'EDGE_MIDPOINT'}

        if self.tpc_snape == "EDGE_PERPENDICULAR":
            bpy.context.scene.tool_settings.snap_elements = {'EDGE_PERPENDICULAR'}          

        # header info
        # context.area.header_text_set("SnapSet: %s" % (self.tpc_snape)) 

        return {'FINISHED'}




class VIEW3D_OT_snap_use(bpy.types.Operator):
    """toggle use snap on/off"""
    bl_idname = "tpc_ot.snap_use"
    bl_label = "Use Snap"
    bl_options = {'REGISTER', 'UNDO'}

    mode : bpy.props.StringProperty(default="")

    def execute(self, context):

        if self.mode == "use_snap":
            bpy.context.scene.tool_settings.use_snap = True
        
        if self.mode == "unuse_snap":
            bpy.context.scene.tool_settings.use_snap = False
       
        # header info
        #context.area.header_text_set("SnapSet: %s" % (self.mode)) 
        return {'FINISHED'}
    


# REGISTER #
classes = (
    VIEW3D_OT_pivot_target,
    VIEW3D_OT_orient_axis,
    VIEW3D_OT_set_orientation,
    VIEW3D_OT_snap_target,
    VIEW3D_OT_snap_element,
    VIEW3D_OT_snap_use,
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()    
    