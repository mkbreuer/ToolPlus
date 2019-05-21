# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

class VIEW3D_OT_Set_Origin_To(bpy.types.Operator):
    '''set origin to selected...'''
    bl_idname = "tpc_ot.set_origin_to"
    bl_label = "Set Origin"
    bl_options = {"REGISTER", 'UNDO'}   
  
    set_cursor = bpy.props.BoolProperty(name="Set 3D Cursor",  description="set pivot to 3d cursor", default = False)   
    mode = bpy.props.StringProperty(default="")    

#    place_origin = bpy.props.EnumProperty(
#      items = [("ORIGIN_GEOMETRY",          "Origin to Geometry",     "Origin to Geometry",      1),
#               ("GEOMETRY_ORIGIN",          "Geometry to Origin",     "Geometry to Origin",      2),
#               ("ORIGIN_CURSOR",            "Origin to 3D Cursor",    "Origin to 3D Cursor",     3), 
#               ("ORIGIN_CENTER_OF_MASS",    "Center of Mass/Surface", "Center of Mass/Surface",  4), 
#               ("ORIGIN_CENTER_OF_VOLUME",  "Center of Mass/Volume",  "Center of Mass/Volume",   5)], 
#               name = "Origin to...",
#               default = "ORIGIN_GEOMETRY",
#               description=" ")

    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
       
        col = layout.column(align=True)

        box = col.box().column(1)              
            
        row = box.column(1) 
        row.prop(self, 'mode')
        
        row.separator()

        row.prop(self, 'set_cursor')

        if "LINKED_FACE" in self.mode: 
    
            row.separator()

            row.prop(self, 'set_value')
    
        box.separator()


    def execute(self, context):
            
        oldmode = bpy.context.object.mode

        if context.mode =='EDIT_MESH':
                        
            if "LINKED_MESH" in self.mode:          
                bpy.ops.mesh.select_linked(delimit=set())
                bpy.ops.view3d.snap_cursor_to_selected() 
       
            if "SELECTED_MESH" in self.mode:          
                bpy.ops.view3d.snap_cursor_to_selected() 

            if "ORIGIN_CURSOR" in self.mode:
                pass
            else:
                bpy.ops.view3d.snap_cursor_to_selected() 
       
        bpy.ops.object.mode_set(mode='OBJECT')  

        if "COPY_ORIGIN" in self.mode:
            current_pivot = bpy.context.space_data.pivot_point     
            bpy.ops.view3d.snap_cursor_to_active() 
 
        if "ORIGIN_CENTER" in self.mode:
            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
     
        if "ORIGIN_GEOMETRY" in self.mode:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        if "GEOMETRY_ORIGIN" in self.mode:
            bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
       
        if "ORIGIN_CURSOR" in self.mode:
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        if "ORIGIN_CENTER_OF_MASS" in self.mode:       
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')   
        
        if "ORIGIN_CENTER_OF_VOLUME" in self.mode:              
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')

    
        if "COPY_ORIGIN" in self.mode:                    
            bpy.context.space_data.pivot_point = current_pivot   

        if self.set_cursor == True:        
            bpy.context.space_data.pivot_point = 'CURSOR'                   
        
        bpy.ops.object.mode_set(mode=oldmode)
        return{'FINISHED'}  



def register():
    bpy.utils.register_class(VIEW3D_OT_Set_Origin_To)


def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_Set_Origin_To)


if __name__ == "__main__":
    register()

    








