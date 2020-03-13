# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

# base snippet from copy attributes addon 
# by bassam kurdali, fabian fricke, adam wiseman
def generic_copy(source, target, string=""):
    """copy attributes from source to target"""
    for attr in dir(source):
        if attr.find(string) > -1:
            try:
                setattr(target, attr, getattr(source, attr))
            except:
                pass
    return


class VIEW3D_OT_modifier_copy(bpy.types.Operator):
    """copy modifier from active to selected"""
    bl_idname = "tpc_ot.modifier_copy"
    bl_label = "Copy Modifier from Active:"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll_func(cls, context):
        return(len(context.selected_objects) > 1)

    selected_type : EnumProperty( 
      items = [("selection", "All Selected",   "",  "BLANK1", 1), 
               ("children",  "Childs of Active", "",  "BLANK1", 2)], 
               name = "Type",
               default = "selection",
               description="modifier properties")

    mody_list : BoolVectorProperty(size=32, options={'SKIP_SAVE'})

    def draw(self, context):
        layout = self.layout.column_flow(columns=2, align=False)
        for idx, const in enumerate(bpy.context.active_object.modifiers):
            layout.prop(self, 'mody_list', index=idx, text=const.name, toggle=True)

        layout = self.layout.column(align=True)      
        layout.label(text='Copy to:')
        
        layout = self.layout.row(align=False)
        layout.prop(self, 'selected_type', expand=True)

    def execute(self, context):
        view_layer = bpy.context.view_layer        
        active = view_layer.objects.active   

        if self.selected_type == 'selection':
            selected = bpy.context.selected_objects[:]
            selected.remove(active)             
       
        else:
            selected = active.children
      
        for obj in selected:           
            if obj != active:               
                for index, flag in enumerate(self.mody_list):
                    if flag:
                        active = bpy.context.active_object
                        old_modifier = active.modifiers[index]
                        new_modifier = obj.modifiers.new(
                            type=active.modifiers[index].type, 
                            name=active.modifiers[index].name)
                        generic_copy(old_modifier, new_modifier)

        return{'FINISHED'}

    def invoke(self, context, event):
        dpi_value = bpy.context.preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=350)


# REGISTER #
classes = (
    VIEW3D_OT_modifier_copy,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()