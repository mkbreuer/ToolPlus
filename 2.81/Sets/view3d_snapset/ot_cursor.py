# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from bpy.app.handlers import persistent

def func_cursor(self, context):
    bpy.context.space_data.overlay.show_cursor = True

    bpy.ops.wm.tool_set_by_id(name="builtin.cursor")
    
    #https://docs.blender.org/api/current/bpy.ops.view3d.html    
    bpy.ops.view3d.cursor3d(use_depth=self.depth, orientation=self.orient)

    bpy.context.preferences.edit.object_align=self.object_align




class VIEW3D_OT_3d_cursor_align(bpy.types.Operator):
    """switch to use 3d cursor tool to align new objects to rotated cursor"""
    bl_idname = "tpc_ot.cursor_object_align"
    bl_label = "Cursor Align"
    bl_options = {"REGISTER", 'UNDO'}

    depth : BoolProperty(name="Surface Project", description="project onto the surface", default=True)

    orient : bpy.props.EnumProperty(
      items = [("NONE",   "None",      "leave orientation unchanged"             ,1),
               ("VIEW",   "View",      "orient to the viewport"                  ,2),
               ("XFORM",  "Transform", "orient to the current transform setting" ,3), 
               ("GEOM",   "Geometry",   "match the surface normal"               ,4)], 
               name = "Orientation",
               default = "GEOM",
               description="Preset viewpoint to use")

    object_align : bpy.props.EnumProperty(
      items = [("WORLD",   "World",    "align new objects to world cooridnate system"  ,1),
               ("VIEW",   "View",      "align new objects to active 3D view"           ,2),
               ("CURSOR",  "3D Cursor",  "align new objects to 3D cursors rotation"    ,3)], 
               name = "Align to",
               default = "CURSOR",
               description="")
        

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_AREA'
        layout.operator_context = "INVOKE_DEFAULT"       

        box = layout.box().column(align=True) 

        row = box.row(align=True)         
        row.label(text="Surface Project")
        row.prop(self, "depth", text='')

        box.separator()       
       
        row = box.row(align=True)  
        row.label(text="Orientation")       
        row.prop(self, "orient", text='')
     
        box.separator()

        row = box.row(align=True)  
        row.label(text="Align to")
        row.prop(self, "object_align", text='')


    def execute(self, context):
        func_cursor(self, context)
        return {'FINISHED'}  



    #??? >> ERROR (wm.operator): c:\b\win64_cmake_vs2017\win64_cmake_vs2017\blender.git\source\blender\windowmanager\intern\wm_event_system.
    #                            c:1462 wm_operator_invoke: invalid operator call 'VIEW3D_OT_cursor3d'

    # https://developer.blender.org/T59744

## REGISTER #
#classes = (
#    VIEW3D_OT_3d_cursor_align,
#)

#def register():
#    for cls in classes:
#        bpy.utils.register_class(cls)

#def unregister():
#    for cls in reversed(classes):
#        bpy.utils.unregister_class(cls)


#if __name__ == "__main__":
#    register()



