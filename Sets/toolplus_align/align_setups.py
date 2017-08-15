import bpy
from bpy import*
from bpy.props import *
from bpy.types import WindowManager



class View3D_TP_SnapSet(bpy.types.Operator):
    """Setups for Snapping"""
    bl_idname = "tp_ops.snap_set"
    bl_label = "SnapSet"
    bl_options = {'REGISTER', 'UNDO'}


    bpy.types.Scene.tp_snap_type = bpy.props.EnumProperty(
        items=[("snap_3D"           ,"3d"           ,"3D Cursor jump to median of selected or active (default)"),
               ("snap_vert"         ,"Vert"         ,"Snap permanent to next Vertices"),
               ("snap_grid"         ,"Grid"         ,"Snap permanent to the Grid"), 
               ("snap_place"        ,"Place"        ,"Snap and rotate with CTRL to next surface"),
               ("snap_retopo"       ,"Retopo"       ,"Snap permanent to sub-selected surface > editmode")],
               name = "TP SnapSet",
               default = "snap_3D",    
               description = "change manipulator axis")

    active = bpy.props.BoolProperty(name="Jump to Active", description ="Jump to Active" , default = True)
    selected = bpy.props.BoolProperty(name="Jump to Selected <> Active", description ="Jump to Active" , default = False)

    def execute(self, context):

        if context.scene.tp_snap_type == "snap_vert":       
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   

        if context.scene.tp_snap_type == "snap_place":   
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = True
            bpy.context.scene.tool_settings.use_snap_project = True

        if context.scene.tp_snap_type == "snap_retopo":      
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
                        
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False

        if context.scene.tp_snap_type == "snap_grid":   
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
            bpy.context.scene.tool_settings.use_snap_grid_absolute = True
            bpy.context.scene.tool_settings.use_snap_align_rotation = False    

        if context.scene.tp_snap_type == "snap_3D":   
            bpy.context.space_data.pivot_point = 'CURSOR'  

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   
            
            for i in range(self.active):
                bpy.ops.view3d.snap_cursor_to_active()

            for i in range(self.selected):
                bpy.ops.view3d.snap_cursor_to_selected()


        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.row(1)
        row.alignment = 'CENTER'        
        row.prop(context.scene, 'tp_snap_type',text=" ", expand =True)                                            
                                         
        if bpy.context.space_data.pivot_point == 'CURSOR':
            row = box.column(1) 

            if self.active == True:
                row.prop(self, 'selected')
            else:
                row.prop(self, 'active')

    #def invoke(self, context, event):
        #return context.window_manager.invoke_props_dialog(self, width = 125)  





class View3D_TP_Snap_Setup_Menu(bpy.types.Operator):
    """Setups for Snapping"""
    bl_idname = "tp_ops.snap_setup_menu"
    bl_label = "Snap Sets :)"
    bl_options = {'REGISTER', 'UNDO'}


    tp_snap = bpy.props.EnumProperty(
                             items=[("tp_retopo"        ,"Mesh Retopo"          ,"Mesh Retopo"        ,"" , 1),                                     
                                    ("tp_place"         ,"Place Object"         ,"Place Object"       ,"" , 2),
                                    ("tp_grid"          ,"Absolute Grid"        ,"Absolute Grid"      ,"" , 3),                                    
                                    ("tp_active_vert"   ,"Active Vertex"        ,"Active Vertex"      ,"" , 4),
                                    ("tp_closest"       ,"Closest Vertex"       ,"Closest Vertex"     ,"" , 5),
                                    ("tp_active_3d"     ,"3d Cursor Active"     ,"3d CursorActive"    ,"" , 6),
                                    ("tp_selected_3d"   ,"3d Cursor Selected"   ,"3d CursorSelected"  ,"" , 7)],
                                    name = "SnapSets", 
                                    default = "tp_grid")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.row(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_snap',text=" ", expand =True)                                            


    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*1.75, height=300)


    def execute(self, context):
  
        if self.tp_snap == "tp_grid":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
            bpy.context.scene.tool_settings.use_snap_grid_absolute = True
            bpy.context.scene.tool_settings.use_snap_align_rotation = False            
            
        elif self.tp_snap == "tp_place":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = True
            bpy.context.scene.tool_settings.use_snap_project = True
                        
        elif self.tp_snap == "tp_retopo":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
                        
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False
            
            
        elif self.tp_snap == "tp_active_vert":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False       
  
        elif self.tp_snap == "tp_closest":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False    


        elif self.tp_snap == "tp_active_3d":
            bpy.context.space_data.pivot_point = 'CURSOR'            

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   
            bpy.ops.view3d.snap_cursor_to_active()
                        
            
        elif self.tp_snap == "tp_selected_3d":
            bpy.context.space_data.pivot_point = 'CURSOR'  

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   

            bpy.ops.view3d.snap_cursor_to_selected()
                
        return {'FINISHED'}





class View3D_TP_Display_All_Manipulator(bpy.types.Operator):
    """Show all Manipulator"""
    bl_idname = "tp_ops.manipulator_all"
    bl_label = "Show all Manipulator"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
   
        bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE', 'SCALE'}       

        return {'FINISHED'}



class View3D_TP_Display_Move_Manipulator(bpy.types.Operator):
    """Show Move Manipulator"""
    bl_idname = "tp_ops.manipulator_move"
    bl_label = "Show Move Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.context.space_data.transform_manipulators = {'TRANSLATE'}       

        return {'FINISHED'}


class View3D_TP_Display_Rotate_Manipulator(bpy.types.Operator):
    """Show Rotate Manipulator"""
    bl_idname = "tp_ops.manipulator_rota"
    bl_label = "Show Rotate Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.context.space_data.transform_manipulators = {'ROTATE'}       

        return {'FINISHED'}



class View3D_TP_Display_Scale_Manipulator(bpy.types.Operator):
    """Show Scale Manipulator"""
    bl_idname = "tp_ops.manipulator_scale"
    bl_label = "Show Scale Manipulator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.context.space_data.transform_manipulators = {'SCALE'}       

        return {'FINISHED'}




def register():
    
    bpy.utils.register_module(__name__)

def unregister():
   
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
    
 
