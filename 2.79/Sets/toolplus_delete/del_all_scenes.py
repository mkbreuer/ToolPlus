import bpy

#bl_info = {
#    "name": "Delete From All Scenes",
#    "description": "This will delete an object from all scenes rather than just from the current one.",
#    "author": "Abel Groenewolt",
#    "version": (0,1),
#    "blender": (2, 5, 9),
#    "api": 40791,
#    "location": "Object Tools > Delete From All Scenes panel > Delete from all scenes",
#    "warning": "", # used for warning icon and text in addons panel
#    "category": "Object"}

## interface ##

"""
class DeleteFromAllScenesPanel(bpy.types.Panel) :
    #bl_space_type = "VIEW_3D"
    #bl_region_type = "TOOLS"
    #bl_context = "objectmode"
    bl_label = "Delete From All Scenes"

    def draw(self, context) :
        TheCol = self.layout.column(align = True)
        TheCol.operator("object.delete_from_all_scenes", text = "Delete From All Scenes")
# end interface class
"""


## operator ##

class DeleteFromAllScenes(bpy.types.Operator):
    bl_idname = "object.delete_from_all_scenes"
    bl_label = "Delete Object From All Scenes"
    bl_options = {"UNDO"}
    
    ## actual function ## 
    def invoke(self, context, event):
        for i in range (0,len(bpy.context.selected_objects)):
            current_object = bpy.context.selected_objects[0]
            # unlink object from all scenes
            for sce in bpy.data.scenes:
                try:    sce.objects.unlink(current_object)
                except:    pass
        return {"FINISHED"}
    # end invoke
# end operator class

def register():
	bpy.utils.register_class(DeleteFromAllScenes)
	#bpy.utils.register_class(DeleteFromAllScenesPanel)
def unregister():
	bpy.utils.register_class(DeleteFromAllScenes)
	#bpy.utils.register_class(DeleteFromAllScenesPanel)

if __name__ == "__main__":
    register()


