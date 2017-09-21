import bpy
from bpy import*
from bpy.props import *



class VIEW3D_TP_Batch_Automirror(bpy.types.Operator):
    """T+ AutoMirror """
    bl_idname = "tp_batch.automirror"
    bl_label = "T+ AutoMirror"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):      
        return {'FINISHED'}
           
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)

    def draw(self, context):
        tp_props = context.window_manager.tp_collapse_menu_modifier   
        layout = self.layout
        wm = bpy.context.window_manager
        layout.operator_context = 'INVOKE_DEFAULT'     
        layout.operator_context = 'INVOKE_REGION_WIN'

        if bpy.context.object.type == 'MESH':
            
            box = layout.box().column(1)
            
            row = box.row(1)
            if tp_props.display_automirror:            
                row.prop(tp_props, "display_automirror", text="", icon="MOD_WIREFRAME")
            else:
                row.prop(tp_props, "display_automirror", text="", icon="MOD_WIREFRAME")
   
            row.label("AutoMirror")


            box.separator() 
            
            row = box.row(1)
            row.prop(context.scene, "AutoMirror_orientation", text="")                                     
            sub1 = row.row(1)
            sub1.scale_x = 0.5
            sub1.prop(context.scene, "AutoMirror_axis", text="")  
            row.operator("object.automirror", text="Execute")                 
          
            box.separator()                      
           
            row = box.row(1)
            row.prop(context.scene, "AutoMirror_threshold", text="Thresh")             
            row.operator("tp_ops.remove_mods_mirror", text="Remove" , icon='X')             
            if context.mode == 'EDIT_MESH': 
                row.operator("tp_ops.apply_mods_mirror_edm", text="Apply", icon='FILE_TICK')                                                                                                                                               
            else:
                row.operator("tp_ops.apply_mods_mirror", text="Apply", icon='FILE_TICK') 


            box.separator() 

            if tp_props.display_automirror: 
                                  
                box = layout.box().column(1) 
                row = box.row(1)
                row.prop(context.scene, "AutoMirror_toggle_edit", text="Editmode")
                row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
                
                row = box.row(1)
                row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")            

                box.separator() 

 
        else:
            
            box = layout.box().column(1)  
            
            row = box.row(1)              
            row.label(icon="ERROR", text="Only for Mesh!")
           

    def check(self, context):
        return True

