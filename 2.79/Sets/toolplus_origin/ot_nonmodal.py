# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

class VIEW3D_OT_Set_Origin_To(bpy.types.Operator):
    '''set origin to selected...'''
    bl_idname = "tpc_ops.set_origin_to"
    bl_label = "Set Origin"
    bl_options = {"REGISTER", 'UNDO'}   
  
    mode = bpy.props.StringProperty(default="")    

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

        bpy.ops.object.mode_set(mode=oldmode)
        return{'FINISHED'}  





class VIEW3D_OT_Origin_to_Edit(bpy.types.Operator):
    """set origin to selected or active / stay in edit or objectmode"""                 
    bl_idname = "tpc_ops.origin_to_edit_selected"          
    bl_label = "Origin to Edit Selected"                 
    bl_options = {'REGISTER', 'UNDO'}   
  
    mode = bpy.props.StringProperty(default="", options={'SKIP_SAVE'})   

    def execute(self, context):
       
        bpy.ops.view3d.snap_cursor_to_selected()     

        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        if "SET_EDIT" in self.mode:   
            bpy.ops.object.editmode_toggle()

        if "SET_OBJECT" in self.mode:   
            bpy.ops.object.editmode_toggle()
   
        return {'FINISHED'}


