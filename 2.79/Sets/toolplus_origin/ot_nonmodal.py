# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

class VIEW3D_OT_Set_Origin_To(bpy.types.Operator):
    '''set origin to selected...'''
    bl_idname = "tpc_ot.set_origin_to"
    bl_label = "Set Origin"
    bl_options = {"REGISTER", 'UNDO'}   
  
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
        #row.prop(self, 'toggle_snap_cursor')

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





class VIEW3D_OT_Origin_to_Edit(bpy.types.Operator):
    """set origin to selected or active / stay in edit or objectmode"""                 
    bl_idname = "tpc_ot.origin_to_edit_selected"          
    bl_label = "Origin to Edit Selected"                 
    bl_options = {'REGISTER', 'UNDO'}   
  
    mode = bpy.props.StringProperty(default="", options={'SKIP_SAVE'})   
    #toggle_snap_cursor = bpy.props.BoolProperty(name="to selected or active",  description="change cursor snap", default = False)   

# ???
#    set_cursor=bpy.props.EnumProperty(
#        name = "3d Cursor to...", 
#        items=[("tpc_active" ,"Active"   ,"Active"   ,"" , 1),                                     
#               ("tpc_select" ,"Selected" ,"Selected" ,"" , 2)],
#        default = "tpc_active")

#    def draw(self, layout):
#        layout = self.layout
#        
#        box = layout.box().column(1)  
#        
#        row = box.column(1)     
#        row.label(text="3d Cursor to...")   
#        row.prop(self, 'set_cursor',text=" ", expand =True)   
  
    def execute(self, context):
       
        #oldmode = bpy.context.object.mode
      
        if self.set_cursor == 'tpc_active':
            bpy.ops.view3d.snap_cursor_to_active()
                        
        if self.set_cursor == 'tpc_select':
     
     
        bpy.ops.view3d.snap_cursor_to_selected()     

        bpy.ops.object.mode_set(mode='OBJECT')  
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')


        #if "SET_EDIT" in self.mode:   
        #bpy.context.object.mode = oldmode
        bpy.ops.object.editmode_toggle()


        if "SET_OBJECT" in self.mode:   
            bpy.ops.object.editmode_toggle()
   
        return {'FINISHED'}


