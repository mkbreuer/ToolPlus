__author__ = "mkbreuer"
__status__ = "toolplus"
__version__ = "1.0"
__date__ = "2016"


import bpy
from bpy import*
from bpy.props import*


###Mr. Stan_Pancake
class VIEW3D_TP_ThroughSelected(bpy.types.Operator):
    """cursor cycle through selected objects"""
    bl_idname = "tp_ops.throughselected"
    bl_label = "Cycle through Selected"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        selection = bpy.context.selected_objects


        if not bpy.context.active_object.select:
            if len(selection):
                bpy.context.scene.objects.active = selection[0]
                bpy.ops.view3d.snap_cursor_to_active() 
        else:
            for i, o in enumerate(selection):
                if o == bpy.context.active_object:
                    bpy.context.scene.objects.active = selection[(i+1) % len(selection)]
                    
                    bpy.ops.view3d.snap_cursor_to_active() 
                    break
        
        return {'FINISHED'}


class VIEW3D_TP_Snapset_Custom(bpy.types.Operator):
    """Snap with Active Verts or Closest Median > setting pivot & snap"""
    bl_idname = "tp_ops.snapset_custom"
    bl_label = "Custom..."
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, layout):
        layout = self.layout
        
        box = layout.box().column(1)  
        
        row = box.column(1)
        row.label("Placeholder...")
        row.label("align_snap_set.py")
    

    def execute(self, context):            

        return {'FINISHED'}

    def invoke(self, context, event):        
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2, height=300)

    #def invoke(self, context, event):
        #return context.window_manager.invoke_props_popup(self, event)    



#### Snap Set ####

class VIEW3D_TP_Snapset_Grid(bpy.types.Operator):
    """Absolute Grid > setting pivot & snap grid snapping"""
    bl_idname = "tp_ops.grid"
    bl_label = "Absolute Grid"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
        bpy.context.scene.tool_settings.use_snap_grid_absolute = True
        bpy.context.scene.tool_settings.use_snap_align_rotation = False            

        return {'FINISHED'}


class VIEW3D_TP_Snapset_Place(bpy.types.Operator):
    """Place Objects > setting pivot & snap for normal rotate"""
    bl_idname = "tp_ops.place"
    bl_label = "Place Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'FACE'
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        bpy.context.scene.tool_settings.use_snap_align_rotation = True
        bpy.context.scene.tool_settings.use_snap_project = True
                        
        return {'FINISHED'}


class VIEW3D_TP_Snapset_Retopo(bpy.types.Operator):
    """Mesh Retopo > setting pivot & snap for surface snapping"""
    bl_idname = "tp_ops.retopo"
    bl_label = "Mesh Retopo"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):            

        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
                    
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'FACE'
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        bpy.context.scene.tool_settings.use_snap_align_rotation = False
                    
        return {'FINISHED'}


class VIEW3D_TP_Snapset_Active_Vert(bpy.types.Operator):
    """Snap with Active Verts or Closest Median > setting pivot & snap"""
    bl_idname = "tp_ops.active_vert"
    bl_label = "Snap Verts..."
    bl_options = {'REGISTER', 'UNDO'}

    tp_verts = bpy.props.EnumProperty(
                             items=[("tp_active"        ,"Active"     ,"Active"      ,"" , 1),                                     
                                    ("tp_closest"       ,"Closest"    ,"Closest"     ,"" , 2)],
                                    name = "Snap Verts...", 
                                    default = "tp_active")

    def draw(self, layout):
        layout = self.layout
        
        box = layout.box().column(1)  
        
        row = box.row(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_verts',text=" ", expand =True)   

    def execute(self, context):            
                
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'VERTEX'

        if self.tp_verts == "tp_active": 
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'    
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
     
        if self.tp_verts == "tp_closest":         

            bpy.context.space_data.pivot_point = 'MEDIAN_POINT'                 
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        
        bpy.context.scene.tool_settings.use_snap_align_rotation = False       
 
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)      




class VIEW3D_TP_Snapset_Active_3d(bpy.types.Operator):
    """Set 3D Cursor to active or selected"""
    bl_idname = "tp_ops.active_3d"
    bl_label = "3d Cursor to..."
    bl_options = {'REGISTER', 'UNDO'}

    tp_3dc = bpy.props.EnumProperty(
                             items=[("tp_active"        ,"Active"      ,"Active"      ,"" , 1),                                     
                                    ("tp_select"        ,"Selected"    ,"Selected"    ,"" , 2)],
                                    name = "3d Cursor to...", 
                                    default = "tp_active")

    def draw(self, layout):
        layout = self.layout
        
        box = layout.box().column(1)  
        
        row = box.row(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_3dc',text=" ", expand =True)   

    def execute(self, context):            

        bpy.context.space_data.pivot_point = 'CURSOR'            

        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'VERTEX'
        bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
        bpy.context.scene.tool_settings.use_snap_align_rotation = False   
                        
        if self.tp_3dc == "tp_active": 
            bpy.ops.view3d.snap_cursor_to_active()   

        if self.tp_3dc == "tp_select": 
            bpy.ops.view3d.snap_cursor_to_selected()            

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)      





class VIEW3D_TP_Snap_Setup(bpy.types.Operator):
    """SnapSet :)"""
    bl_idname = "tp_align.snap_setup"
    bl_label = "Snap Sets :)"
    bl_options = {'REGISTER', 'UNDO'}


    tp_snap = bpy.props.EnumProperty(
                             items=[("tp_retopo"        ,"Mesh Retopo"          ,"Mesh Retopo"        ,"" , 1),                                     
                                    ("tp_place"         ,"Place Object"         ,"Place Object"       ,"" , 2),
                                    ("tp_grid"          ,"Absolute Grid"        ,"Absolute Grid"      ,"" , 3),                                    
                                    ("tp_active_vert"   ,"Active Vertex"        ,"Active Vertex"      ,"" , 4),
                                    ("tp_closest"       ,"Closest Vertex"       ,"Closest Vertex"     ,"" , 5),
                                    ("tp_active_3d"     ,"3d Cursor Active"     ,"3d CursorActive"    ,"" , 6),
                                    ("tp_selected_3d"   ,"3d Cursor Selected"   ,"3d CursorSelected"  ,"" , 7)],
                                    name = "SnapSets", 
                                    default = "tp_grid")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_snap',text=" ", expand =True)                                            
                                         
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*1.75, height=300)


    def execute(self, context):
  
        if self.tp_snap == "tp_grid":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
            bpy.context.scene.tool_settings.use_snap_grid_absolute = True
            bpy.context.scene.tool_settings.use_snap_align_rotation = False            
            
        elif self.tp_snap == "tp_place":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = True
            bpy.context.scene.tool_settings.use_snap_project = True
                        
        elif self.tp_snap == "tp_retopo":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
                        
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False            
            
        elif self.tp_snap == "tp_active_vert":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False       
  
        elif self.tp_snap == "tp_closest":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False    

        elif self.tp_snap == "tp_active_3d":
            bpy.context.space_data.pivot_point = 'CURSOR'            

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   
            bpy.ops.view3d.snap_cursor_to_active()
                                    
        elif self.tp_snap == "tp_selected_3d":
            bpy.context.space_data.pivot_point = 'CURSOR'  

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   

            bpy.ops.view3d.snap_cursor_to_selected()

        return {'FINISHED'}


# Register

def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()




















