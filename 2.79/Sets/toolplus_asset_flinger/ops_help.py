# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# OPEN KEYMAP #
from os.path import dirname
from toolplus_asset_flinger import ui_keymap

class View3D_TP_KeyMap_AssetFlinger(bpy.types.Operator):
    bl_idname = "tp_ops.keymap_assetflinger"
    bl_label = "Open KeyMap (Text Editor)"
    bl_description = "open keymap file in the text editor"

    def execute(self, context):
        path = ui_keymap.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}





# HELP OPERATOR #
class VIEW3D_TP_Help_Path_Settings(bpy.types.Operator):
    bl_idname = 'tp_ops.help_path_settings'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        
        layout.label("", icon = "TRIA_DOWN")   
        layout.label("Open Libraries:")            
        layout.label("click on text to insert as obj or from blend file", icon="LAYER_USED")               
        layout.label("- append (editable): add data completely into the scene", icon="LAYER_USED")   
        layout.label("- link (not editable): linked as a referenced object to the scene", icon="LAYER_USED")     
        layout.label("- linked: Make Local [L] makes the data local to the file", icon="LAYER_USED")        
        layout.label("", icon = "TRIA_UP")           
      
        layout.label("", icon = "TRIA_DOWN")             
        layout.label("Save to Libraries:")    
        layout.label("the export save autom. a obj and an blend file", icon="LAYER_USED")   
        layout.label("- obj: objects are only meshes", icon="LAYER_USED")   
        layout.label("- blend file: save non destructiv with all created properties", icon="LAYER_USED")   
        layout.label("thumbnails will be rendering automatically", icon="LAYER_USED")   
        layout.label("previous can be overstored with new objects and preview", icon="LAYER_USED")   
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 350)





# HELP OPERATOR #
class VIEW3D_TP_Help_Path_Project(bpy.types.Operator):
    bl_idname = 'tp_ops.help_path_project'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("path to the project folder location", icon="LAYER_USED")   
        layout.label("each folder is a category in the insert preview", icon="LAYER_USED")           
        layout.label("new categories can be added in the save window", icon="LAYER_USED")       
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 275)


# HELP OPERATOR #
class VIEW3D_TP_Help_Path_Asset(bpy.types.Operator):
    bl_idname = 'tp_ops.help_path_asset'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("path to the main asset location", icon="LAYER_USED")   
        layout.label("each folder is a category in the insert preview", icon="LAYER_USED")            
        layout.label("new categories can be added in the save window", icon="LAYER_USED")       
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 275)



# HELP OPERATOR #
class VIEW3D_TP_Help_Color(bpy.types.Operator):
    bl_idname = 'tp_ops.help_color'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("Original - beige solid look", icon="LAYER_USED")
        layout.label("Gray - gray solid look ", icon="LAYER_USED")
        layout.label("Silver - silver metal look", icon="LAYER_USED")
        layout.label("Wire - dark wire on light grey", icon="LAYER_USED")
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 170)


# HELP OPERATOR #
class VIEW3D_TP_Help_Size(bpy.types.Operator):
    bl_idname = 'tp_ops.help_size'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("64x64 - very small, less details", icon="LAYER_USED")
        layout.label("128x128 - optimal size, middle details" , icon="LAYER_USED")
        layout.label("256x256 - slow to render, much details", icon="LAYER_USED")
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 235)


# HELP OPERATOR #
class VIEW3D_TP_Help_Location(bpy.types.Operator):
    bl_idname = 'tp_ops.help_location'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("Tool Shelf [T]:  right 3d view shelf", icon = "LAYER_USED") 
        layout.label("Property Shelf [N]:  left 3d view shelf", icon = "LAYER_USED") 
        layout.label("TAB: insert the Panel to named Catergory", icon = "LAYER_USED") 
        layout.label("TAB: new Name = new Tab Catergory", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 250)



# HELP OPERATOR #
class VIEW3D_TP_Help_Input(bpy.types.Operator):
    bl_idname = 'tp_ops.help_input'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
       
        layout.label("", icon = "TRIA_DOWN")         
        layout.label("Open Project: [SHIFT+ALT+E]", icon = "LAYER_USED") 
        layout.label("Save to Project: [SHIFT+ALT+W]", icon = "LAYER_USED")       
        layout.label("turn off need a restart", icon = "LAYER_USED")       

        layout.label("", icon = "SPACE3")            
      
        layout.label("Open Asset Library: [CTRL+SHIFT+ALT+E]", icon = "LAYER_USED") 
        layout.label("Save to Asset Library: [CTRL+SHIFT+ALT+A]", icon = "LAYER_USED") 
        layout.label("turn off need a restart", icon = "LAYER_USED") 

        layout.label("", icon = "SPACE3")    
     
        layout.label("Popup Menu: [CTRL+SHIFT+ALT+W]", icon = "LAYER_USED") 
  
        layout.label("", icon = "SPACE3")  
          
        layout.label("Header: Add 2 / 2 Icon Buttons", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  

    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 275)




# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


