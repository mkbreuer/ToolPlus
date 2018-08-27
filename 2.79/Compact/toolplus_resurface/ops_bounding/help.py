# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *



# HELP OPERATOR #
class VIEW3D_TP_BBox_Settings_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bounding_settings'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("  Object Type: different geometry to bounding selected", icon = "LAYER_USED") 
        layout.label("  Mesh Types: kind of geometry display in the scene", icon = "LAYER_USED") 
        layout.label("  -> shaded: geometry with solid faces", icon = "LAYER_USED") 
        layout.label("  -> shade off: geometry with transparent faces", icon = "LAYER_USED") 
        layout.label("  -> wire only: only vertices and edges geoemtry / non faces", icon = "LAYER_USED") 
        layout.label("  Settings: stores last used adjustments for faster use", icon = "LAYER_USED") 
        layout.label("  Reset: use operator presets to restore to defaults", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 330)



# HELP OPERATOR #
class VIEW3D_TP_BBox_ReName_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bounding_rename'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("Type 1:  prefix / name from selected objects / suffix", icon = "LAYER_USED") 
        layout.label("Type 2:  prefix / use custom instead of object names / suffix", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 330)



# HELP OPERATOR #
class VIEW3D_TP_BBox_Select_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bounding_select'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("Type 1: select default suffix > object type + mesh type", icon = "LAYER_USED") 
        layout.label("Type 2: select custom pattern > when suffix use not default names", icon = "LAYER_USED") 
        layout.label("unix style wildcards > *everything / starting* / *contains*", icon = "LAYER_USED") 
        layout.label("unix style wildcards > ?singel / [just-abc] / [!not-abc]", icon = "LAYER_USED") 
        layout.label("Setting Extend: add selected to selection additivly", icon = "LAYER_USED") 
        layout.label("Setting Linked: link selected to active as instances", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 375)




# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


