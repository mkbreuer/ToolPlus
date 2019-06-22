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

        addon_prefs = context.preferences.addons[__package__].preferences

        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap
        
        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_bta_pivot     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_bta_use_pivot 
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_bta_elements}
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_bta_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_bta_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_bta_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_bta_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_bta_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_bta_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_bta_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_bta_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_bta_scale

        # header info
        #context.area.header_text_set("SnapSet: %s" % (addon_prefs.name_bta))           
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_B(bpy.types.Operator):
    """Snap to Button B Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_b"
    bl_label = "Snap Button B..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        addon_prefs = context.preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap
        
        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_btb_pivot     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_btb_use_pivot 
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_btb_elements}
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_btb_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_btb_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_btb_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_btb_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_btb_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_btb_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_btb_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_btb_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_btb_scale
    
        # header info
        #context.area.header_text_set("SnapSet: %s" % (addon_prefs.name_btb))          
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_C(bpy.types.Operator):
    """Snap to Button C Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_c"
    bl_label = "Snap Button C..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        addon_prefs = context.preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap
        
        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_btc_pivot     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_btc_use_pivot 
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_btc_elements}
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_btc_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_btc_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_btc_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_btc_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_btc_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_btc_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_btc_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_btc_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_btc_scale
        
        # header info
        #context.area.header_text_set("SnapSet: %s" % (addon_prefs.name_btc))          
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_D(bpy.types.Operator):
    """Snap to Button D Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_d"
    bl_label = "Snap Button D..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        addon_prefs = context.preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap
        
        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_btd_pivot     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_btd_use_pivot 
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_btd_elements}
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_btd_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_btd_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_btd_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_btd_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_btd_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_btd_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_btd_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_btd_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_btd_scale
        
        # header info
        #context.area.header_text_set("SnapSet: %s" % (addon_prefs.name_btd))          
        return {'FINISHED'}


class VIEW3D_OT_Snapset_Button_E(bpy.types.Operator):
    """Snap to Button E Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_e"
    bl_label = "Snap Button E..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        addon_prefs = context.preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap
        
        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_bte_pivot     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_bte_use_pivot 
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_bte_elements}
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_bte_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_bte_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_bte_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_bte_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_bte_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_bte_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_bte_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_bte_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_bte_scale
        
        # header info
        #context.area.header_text_set("SnapSet: %s" % (addon_prefs.name_bte))          
        return {'FINISHED'}



class VIEW3D_OT_Snapset_Button_F(bpy.types.Operator):
    """Snap to Button F Snap Settings"""
    bl_idname = "tpc_ot.snapset_button_f"
    bl_label = "Snap Button F..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        addon_prefs = context.preferences.addons[__package__].preferences
        
        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap
        
        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_btf_pivot     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_btf_use_pivot 
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_btf_elements}
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_btf_target
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_btf_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_btf_snap_self
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_btf_align_rotation       
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_btf_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_btf_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_btf_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_btf_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_btf_scale
        
        # header info
        #context.area.header_text_set("SnapSet: %s" % (addon_prefs.name_btf))          
        return {'FINISHED'}


