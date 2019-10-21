import bpy




class View3D_TP_TP_N_Transform_Menu(bpy.types.Menu):
    """Normal Transform Menu for active Pivot Point"""
    bl_label = "Normal Transform Menu"
    bl_idname = "tp_ops.normal_transform_menu"

    def draw(self, context):
        layout = self.layout    

        layout.menu("translate.normal_menu", text="N-Translate")
        layout.menu("rotate.normal_menu", text="N-Rotate")
        layout.menu("resize.normal_menu", text="N-Scale")

        ###space###    
        if context.mode == 'EDIT_MESH':
            
            layout.separator()
            
            layout.operator('mesh.rot_con', 'Face-Rotation')



class View3D_TP_Translate_Normal_Menu(bpy.types.Menu):
    """Translate Normal Constraint for active Pivot Point"""
    bl_label = "Translate Normal Constraint"
    bl_idname = "tp_ops.translate_normal_menu"

    def draw(self, context):
        layout = self.layout         

        #layout.label("___Move___")
        
        props = layout.operator("transform.transform", text = "X-Axis")
        props.mode = 'TRANSLATION'
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.transform", text = "Y-Axis")
        props.mode = 'TRANSLATION'
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.transform", text = "Z-Axis")
        props.mode = 'TRANSLATION'
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 



class View3D_TP_Resize_Normal_Menu(bpy.types.Menu):
    """Resize Normal Constraint for active Pivot Point"""
    bl_label = "Resize Normal Constraint"
    bl_idname = "tp_ops.resize_normal_menu"

    def draw(self, context):
        layout = self.layout         
        
        #layout.label("___Scale___") 
        
        props = layout.operator("transform.resize", text = "X-Axis")
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.resize", text = "Y-Axis")
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 
        
        props = layout.operator("transform.resize", text = "Z-Axis")
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE'                  

        props = layout.operator("transform.resize", text = "XY-Axis")
        props.constraint_axis = (True, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE'



class View3D_TP_Rotate_Normal_Menu(bpy.types.Menu):
    """Rotate Normal Constraint for active Pivot Point"""
    bl_label = "Rotate Normal Constraint"
    bl_idname = "tp_ops.rotate_normal_menu"

    def draw(self, context):
        layout = self.layout         
        
        #layout.label("___Rotate___") 
        
        props = layout.operator("transform.rotate", text = "X-Axis")
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 

        props = layout.operator("transform.rotate", text = "Y-Axis")
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE' 
        
        props = layout.operator("transform.rotate", text = "Z-Axis")
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'NORMAL'
        props.snap_target = 'ACTIVE'                  


          

def Draw_View3D_TP_Transform_Normal(self,context):
    layout = self.layout
    col = layout.column(align=True)

    col.operator("transform.tosphere", text="To Sphere")
    col.operator("transform.shear", text="Shear")
    col.operator("transform.bend", text="Bend")

    col.separator() 

    #col.label("Transform with Normal Axis Constraint")
    col.menu("tp_ops.translate_normal_menu", text="N-Translate")
    col.menu("tp_ops.rotate_normal_menu", text="N-Rotate")
    col.menu("tp_ops.resize_normal_menu", text="N-Scale")
    if context.mode == 'EDIT_MESH':
        col.operator("tp_ops.align_to_normal", text="N-Align")

    col.separator()                
  


def register():
    bpy.utils.register_class(View3D_TP_Translate_Normal_Menu)
    bpy.utils.register_class(View3D_TP_Resize_Normal_Menu)
    bpy.utils.register_class(View3D_TP_Rotate_Normal_Menu)


    bpy.types.VIEW3D_PT_tools_transform.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_PT_tools_transform_mesh.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_PT_tools_transform_curve.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_PT_tools_transform_surface.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_PT_tools_mballedit.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_PT_tools_armatureedit_transform.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_PT_tools_latticeedit.append(Draw_View3D_TP_Transform_Normal)    
    bpy.types.VIEW3D_MT_transform_object.prepend(Draw_View3D_TP_Transform_Normal)  
    bpy.types.VIEW3D_MT_transform.prepend(Draw_View3D_TP_Transform_Normal)  


def unregister():

    bpy.utils.unregister_class(View3D_TP_Translate_Normal_Menu)
    bpy.utils.unregister_class(View3D_TP_Resize_Normal_Menu)
    bpy.utils.unregister_class(View3D_TP_Rotate_Normal_Menu)


    bpy.types.VIEW3D_PT_tools_transform.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_PT_tools_transform_mesh.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_PT_tools_transform_curve.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_PT_tools_transform_surface.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_PT_tools_mballedit.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_PT_tools_armatureedit_transform.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_PT_tools_latticeedit.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_MT_transform_object.remove(Draw_View3D_TP_Transform_Normal)
    bpy.types.VIEW3D_MT_transform.remove(Draw_View3D_TP_Transform_Normal)


if __name__ == "__main__":
    register()

