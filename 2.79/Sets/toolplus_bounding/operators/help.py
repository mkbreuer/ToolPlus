# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# HELP OPERATOR #
class TP_BBox_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bbox'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("1.)  Object Type: plane and cubic geometry", icon = "LAYER_USED") 
        layout.label("2.)  Mesh Type: shaded > default mesh geometry", icon = "LAYER_USED") 
        layout.label("3.)  Mesh Type: shade off > transparent mesh", icon = "LAYER_USED") 
        layout.label("4.)  Mesh Type: wire only > deleted faces", icon = "LAYER_USED") 
        layout.label("5.)  Settings: stores last used adjustments", icon = "LAYER_USED") 
        layout.label("6.)  Redo Last [F6]: to change settings on the fly", icon = "LAYER_USED") 
        layout.label("7.)  Operator Presets: store or reset all to default values", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 315)



# HELP OPERATOR #
class TP_BCyl_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bcyl'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("1.)  Object Type: circle and cylindric geometry", icon = "LAYER_USED") 
        layout.label("2.)  Mesh Type: shaded > default mesh geometry", icon = "LAYER_USED") 
        layout.label("3.)  Mesh Type: shade off > transparent mesh", icon = "LAYER_USED") 
        layout.label("4.)  Mesh Type: wire only > deleted faces", icon = "LAYER_USED") 
        layout.label("5.)  Settings: stores last used adjustments", icon = "LAYER_USED") 
        layout.label("6.)  Redo Last [F6]: to change settings on the fly", icon = "LAYER_USED") 
        layout.label("7.)  Operator Presets: store or reset all to default values", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 315)
 
    

# HELP OPERATOR #
class TP_BSph_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bsph'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("1.)  Object Type: spheric geometry", icon = "LAYER_USED") 
        layout.label("2.)  Mesh Type: shaded > default mesh geometry", icon = "LAYER_USED") 
        layout.label("3.)  Mesh Type: shade off > transparent mesh", icon = "LAYER_USED") 
        layout.label("4.)  Mesh Type: wire only > deleted faces", icon = "LAYER_USED") 
        layout.label("5.)  Settings: stores last used adjustments", icon = "LAYER_USED") 
        layout.label("6.)  Redo Last [F6]: to change settings on the fly", icon = "LAYER_USED") 
        layout.label("7.)  Operator Presets: store or reset all to default values", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 315)




# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


