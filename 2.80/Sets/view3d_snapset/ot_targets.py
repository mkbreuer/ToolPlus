# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


class VIEW3D_OT_PIVOT_TARGET(bpy.types.Operator):
    """Set Pivot"""
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
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_pivot',text=" ", expand =True)                                            
     
        box.separator()
        
        row = box.column(1)
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
    
    
               
class VIEW3D_OT_ORIENT_AXIS(bpy.types.Operator):
    """Transform Axis Orientation"""
    bl_idname = "tpc_ot.orient_axis"
    bl_label = "Transform Axis Orientation"
    bl_options = {'REGISTER', 'UNDO'}

    tpc_axis : bpy.props.EnumProperty(
        items=[("GLOBAL"    ,"Global"   ,"Global"),
               ("LOCAL"     ,"Local"    ,"Local"),
               ("NORMAL"    ,"Normal"   ,"Normal"),
               ("GIMBAL"    ,"Gimbal"   ,"Gimbal"),
               ("VIEW"      ,"View"     ,"View"),
               ("CURSOR"    ,"Cursor"     ,"Cursor")],
               name = "Orientation",
               default = "GLOBAL",    
               description = "change manipulator axis")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
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




class VIEW3D_OT_SNAP_TARGET(bpy.types.Operator):
    """Snap Target"""
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
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
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




class VIEW3D_OT_SNAP_ELEMENT(bpy.types.Operator):
    """Snap Element"""
    bl_idname = "tpc_ot.snap_element"
    bl_label = "Snap Element"
    bl_options = {'REGISTER', 'UNDO'}

    tpc_snape : bpy.props.EnumProperty(
                 items=[("INCREMENT" ,"Increment"   ,""   ,"SNAP_INCREMENT" , 1),
                        ("VERTEX"    ,"Vertex"      ,""   ,"SNAP_VERTEX"    , 2),
                        ("EDGE"      ,"Edge"        ,""   ,"SNAP_EDGE"      , 3),
                        ("FACE"      ,"Face"        ,""   ,"SNAP_FACE"      , 4),
                        ("VOLUME"    ,"Volume"      ,""   ,"SNAP_VOLUME"    , 5)],
                        name = "Snap Element", 
                        default = "INCREMENT")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tpc_snape',text=" ", expand =True)                                            
     
        box.separator()

    def execute(self, context):

        if self.tpc_snape == "INCREMENT":
            bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}

        elif self.tpc_snape == "VERTEX":
            bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}   

        elif self.tpc_snape == "EDGE":
            bpy.context.scene.tool_settings.snap_elements = {'EDGE'}    

        elif self.tpc_snape == "FACE":
            bpy.context.scene.tool_settings.snap_elements = {'FACE'}                      

        elif self.tpc_snape == "VOLUME":
            bpy.context.scene.tool_settings.snap_elements = {'VOLUME'}   

        # header info
        #context.area.header_text_set("SnapSet: %s" % (self.tpc_snape)) 
        return {'FINISHED'}



class VIEW3D_OT_SNAP_USE(bpy.types.Operator):
    """Snap Toggle"""
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