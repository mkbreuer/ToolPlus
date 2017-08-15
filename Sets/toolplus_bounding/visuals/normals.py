import bpy
from bpy import*
from bpy.props import *





class VIEW3D_TP_Normals(bpy.types.Operator):
    """Recalculate Normals for all selected Objects in Objectmode"""
    bl_idname = "tp_ops.rec_normals"
    bl_label = "Recalculate Normals"     

    def execute(self, context):
        #print(self)
        #self.report({'INFO'}, "Recalculate Normals")                   
        for obj in bpy.context.selected_objects:
            bpy.context.scene.objects.active = obj 
                
            if obj:
                obj_type = obj.type

                if obj_type in {'MESH'}:                 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent()
                    bpy.ops.object.editmode_toggle()            

        return {'FINISHED'}          





def register():    
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

