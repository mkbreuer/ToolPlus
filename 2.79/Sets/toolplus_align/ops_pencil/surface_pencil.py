# LOAD MODULE #
import bpy
import bmesh
from bpy import*
from bpy.props import *


bpy.types.Scene.obj1 = bpy.props.StringProperty()

# Create GP Line
class VIEW3D_TP_Surface_Pen(bpy.types.Operator):
    bl_idname = "tp_ops.surface_pencil"
    bl_label = "Surface Pen"
    bl_description = "Draw grease pencil lines with surface placement"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
       
        WM = context.window_manager

        bpy.context.scene.tool_settings.grease_pencil_source = 'OBJECT'
        bpy.context.scene.tool_settings.gpencil_stroke_placement_view3d = 'SURFACE'
        
        bpy.ops.gpencil.draw('INVOKE_DEFAULT')
                
        return {"FINISHED"}



class VIEW3D_TP_RemoveGP(bpy.types.Operator):
    bl_idname = "tp_ops.remove_gp"
    bl_label = "Remove GP"
    bl_description = "Remove all Grease Pencil Strokes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.gpencil_data is not None:
            bpy.ops.gpencil.data_unlink()
        else:
            self.report({'INFO'}, "No Grease Pencil data to Unlink")
            return {'CANCELLED'}

        return{'FINISHED'}


# REGISTRY #
def register():    
    bpy.utils.register_module(__name__)

def unregister():  
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
 
    