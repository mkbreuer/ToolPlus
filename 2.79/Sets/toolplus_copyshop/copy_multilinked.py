#bl_info = {
#    "name": "Duplicate Multiple Linked",
#    "description": "Copies the selected object into multiple linked duplicates, optionally parented under an empty.",
#    "author": "This script is public domain",
#    "version": (0,2),
#    "blender": (2, 6, 3),
#    "api": 46461,
#    "location": "View3D > Object",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Object"}

import bpy

def duplicateObject(context, numCopies, transVec, doParent):
    activeObj = context.active_object
    dupCopies = []
    dupCopies.append(activeObj)
    while numCopies > 0:
        bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":transVec, "release_confirm":False})
        dupCopies.append(context.active_object)
        numCopies -= 1
    if doParent:
        groupName = activeObj.name + "_Copies"
        bpy.ops.object.add(type='EMPTY')
        groupEmpty = context.active_object
        groupEmpty.name = groupName
        for i in dupCopies:
            bpy.data.objects[i.name].select = True

            bpy.data.objects[groupEmpty.name].select = True
        bpy.ops.object.parent_set(type="OBJECT")
    else:
        for i in dupCopies:
            #updated 
            bpy.ops.object.select_pattern(pattern=i.name, extend=True)

class multiDuplicate(bpy.types.Operator):
    """ create multi copies and parented them under an empty """
    bl_idname = "object.multi_duplicate"
    bl_label = "Duplicate Multiple Linked"
    bl_options = {"REGISTER", "UNDO"}
    
    my_int = bpy.props.IntProperty(name="Number of Copies:", default=True, description="Number of copies", min=1, max=5000, subtype="NONE")
    my_floatvec = bpy.props.FloatVectorProperty(name="XYZ Offset:", default=(0.0,0.0,0.0), min=-1000, max=1000, description="XYZ Offset")
    my_bool = bpy.props.BoolProperty(name="Parent under Empty", default=True)
 
    @classmethod
    def poll(cls, context):
        ob = context.object
        if ob == None:
            return False
        elif ob.select:
            return True
        return False

    def execute(self, context):
        duplicateObject(context, self.my_int, self.my_floatvec, self.my_bool)
        return {'FINISHED'}
    
    def invoke(self, context, event):
       return self.execute(context)

#def menu_draw(self, context):
#   self.layout.operator_context = 'INVOKE_REGION_WIN'
#   self.layout.operator(multiDuplicate.bl_idname, "Duplicate Multiple Linked")
 
def register():
    bpy.utils.register_module(__name__)
#   bpy.types.VIEW3D_MT_object.append(menu_draw)
 
def unregister():
#   bpy.types.VIEW3D_MT_object.remove(menu_draw)
    bpy.utils.unregister_module(__name__)
 
if __name__ == '__main__':
    register()