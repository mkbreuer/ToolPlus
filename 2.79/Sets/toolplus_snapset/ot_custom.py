# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*


class VIEW3D_OT_Snapset_Button_A(bpy.types.Operator):
    """Snap to Button A Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_a"
    bl_label = "Snap Button A..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        prefs = context.user_preferences.addons[__package__].preferences

        bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
        
        bpy.context.space_data.pivot_point = prefs.prop_bta_pivot     
        bpy.context.space_data.use_pivot_point_align = prefs.prop_bta_use_pivot 
        bpy.context.scene.tool_settings.snap_element = prefs.prop_bta_elements
        bpy.context.scene.tool_settings.snap_target = prefs.prop_bta_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = prefs.prop_bta_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = prefs.prop_bta_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = prefs.prop_bta_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = prefs.prop_bta_project
        bpy.context.scene.tool_settings.use_snap_peel_object = prefs.prop_bta_peel_object
        
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_B(bpy.types.Operator):
    """Snap to Button B Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_b"
    bl_label = "Snap Button B..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        prefs = context.user_preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
        
        bpy.context.space_data.pivot_point = prefs.prop_btb_pivot     
        bpy.context.space_data.use_pivot_point_align = prefs.prop_btb_use_pivot 
        bpy.context.scene.tool_settings.snap_element = prefs.prop_btb_elements
        bpy.context.scene.tool_settings.snap_target = prefs.prop_btb_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = prefs.prop_btb_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = prefs.prop_btb_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = prefs.prop_btb_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = prefs.prop_btb_project
        bpy.context.scene.tool_settings.use_snap_peel_object = prefs.prop_btb_peel_object
        
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_C(bpy.types.Operator):
    """Snap to Button C Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_c"
    bl_label = "Snap Button C..."
    bl_options = {'REGISTER', 'UNDO'}

    prop_btc_cursor=bpy.props.EnumProperty(
        name = "3d Cursor to...", 
        items=[("tpc_active" ,"Active"   ,"Active"   ,"" , 1),                                     
               ("tpc_select" ,"Selected" ,"Selected" ,"" , 2)],
        default = "tpc_active")

    def draw(self, layout):
        layout = self.layout
        
        box = layout.box().column(1)  
        
        row = box.column(1)     
        row.label(text="3d Cursor to...")   
        row.prop(self, 'prop_btc_cursor',text=" ", expand =True)   
        

    def execute(self, context):            

        prefs = context.user_preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
        
        bpy.context.space_data.pivot_point = prefs.prop_btc_pivot     
        bpy.context.space_data.use_pivot_point_align = prefs.prop_btc_use_pivot 
        bpy.context.scene.tool_settings.snap_element = prefs.prop_btc_elements
        bpy.context.scene.tool_settings.snap_target = prefs.prop_btc_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = prefs.prop_btc_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = prefs.prop_btc_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = prefs.prop_btc_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = prefs.prop_btc_project
        bpy.context.scene.tool_settings.use_snap_peel_object = prefs.prop_btc_peel_object        
        
        if self.prop_btc_cursor == 'tpc_active':
            bpy.ops.view3d.snap_cursor_to_active()
            
        if self.prop_btc_cursor == 'tpc_select':
            bpy.ops.view3d.snap_cursor_to_selected()
             
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_D(bpy.types.Operator):
    """Snap to Button D Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_d"
    bl_label = "Snap Button D..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        prefs = context.user_preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
        
        bpy.context.space_data.pivot_point = prefs.prop_btd_pivot     
        bpy.context.space_data.use_pivot_point_align = prefs.prop_btd_use_pivot 
        bpy.context.scene.tool_settings.snap_element = prefs.prop_btd_elements
        bpy.context.scene.tool_settings.snap_target = prefs.prop_btd_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = prefs.prop_btd_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = prefs.prop_btd_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = prefs.prop_btd_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = prefs.prop_btd_project
        bpy.context.scene.tool_settings.use_snap_peel_object = prefs.prop_btd_peel_object

        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_E(bpy.types.Operator):
    """Snap to Button E Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_e"
    bl_label = "Snap Button E..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        prefs = context.user_preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
        
        bpy.context.space_data.pivot_point = prefs.prop_bte_pivot     
        bpy.context.space_data.use_pivot_point_align = prefs.prop_bte_use_pivot 
        bpy.context.scene.tool_settings.snap_element = prefs.prop_bte_elements
        bpy.context.scene.tool_settings.snap_target = prefs.prop_bte_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = prefs.prop_bte_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = prefs.prop_bte_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = prefs.prop_bte_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = prefs.prop_bte_project
        bpy.context.scene.tool_settings.use_snap_peel_object = prefs.prop_bte_peel_object

        return {'FINISHED'}



class VIEW3D_OT_Snapset_Button_F(bpy.types.Operator):
    """Snap to Button F Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_f"
    bl_label = "Snap Button F..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        prefs = context.user_preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
        
        bpy.context.space_data.pivot_point = prefs.prop_btf_pivot     
        bpy.context.space_data.use_pivot_point_align = prefs.prop_btf_use_pivot 
        bpy.context.scene.tool_settings.snap_element = prefs.prop_btf_elements
        bpy.context.scene.tool_settings.snap_target = prefs.prop_btf_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = prefs.prop_btf_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = prefs.prop_btf_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = prefs.prop_btf_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = prefs.prop_btf_project
        bpy.context.scene.tool_settings.use_snap_peel_object = prefs.prop_btf_peel_object

        return {'FINISHED'}


