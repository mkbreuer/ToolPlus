# LOAD MODUL #
import bpy 
from bpy.props import StringProperty

class VIEW3D_OT_mesh_align_help(bpy.types.Operator):
    """help information"""
    bl_idname = "tpc_ops.mesh_align_help"
    bl_label = "How To..."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #fake
        return {"FINISHED"}

    def check(self, context):
        return True

    mode : bpy.props.StringProperty(default="")     

    def draw(self, context):
        layout = self.layout

        box = layout.box().column(align=True)

        if self.mode in 'align':

            row = box.column(align=True)                                   
            row.label(text='Align X/Y/Z > axis constraint with scale 0')                                     
            row.label(text='Align Xy/Zy/Zx > douple axis constraint with scale 0')                                     
            
            row.separator()      

            row.label(text='Align to Normal > align all planar to active face')                                                                                                        
            
            row.separator()      
            
            row.label(text='Straight > align vertices to a straight line')                                                                                                        
            row.label(text='Evenly > distribute vertices evenly space')                                                                                                        
            row.label(text='Evenly Straight > align staight and distibute evenly')                                                                                                        
            
            row.separator()      

            row.label(text='Mirror over Edge > mirror selected over active edge')                                                                                                        


        if self.mode in 'flatten':                                                                     
       
            row = box.column(align=True) 
            row.label(text='Run Modal > activate than select face to')                                                                             
            row.label(text='Threshold > flatten with select linked face')                                                                                                                                                         
            
            row.separator()                  
            
            row.label(text='Flatten X/Y/Z > axis constraint with scale 0')                                        
            row.label(text='LPT Flatten > looptools-flatten with best fitting plane')                                        
            
            row.separator()             
            
            row.label(text='Region: Selection > boundary loops')                                        
            row.label(text='Region: UV Seam > add seams to boundary loops')                                        
            row.label(text='Region: Mark Sharp > mark boundary loops sharp')                                        


    def invoke(self, context, event):
        dpi_value = bpy.context.preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*4, height=300)
   

