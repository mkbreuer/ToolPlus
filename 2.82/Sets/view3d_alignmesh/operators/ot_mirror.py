# LOAD MODULE #
import bpy
from bpy import*


class VIEW3D_OT_mirror_over_edge(bpy.types.Operator):
    """mirror selected mesh over active edge / normal Y axis"""                 
    bl_idname = "tpc_ot.mirror_over_edge"          
    bl_label = "Edge Mirror"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        
        store_pivot = bpy.context.scene.tool_settings.transform_pivot_point

        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'  

        bpy.ops.transform.mirror(orient_type='NORMAL', constraint_axis=(False, True, False), 
                                 use_proportional_edit=False, proportional_edit_falloff='SMOOTH', 
                                 proportional_size=1, use_proportional_connected=False, 
                                 use_proportional_projected=False)

        bpy.ops.mesh.normals_make_consistent(inside=False)
       
        bpy.context.scene.tool_settings.transform_pivot_point = store_pivot

        return {'FINISHED'}
