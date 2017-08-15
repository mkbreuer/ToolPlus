import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons

    
    
class tp_ops_OriginObm(bpy.types.Operator):
    """set origin to selected / stay in objectmode"""                 
    bl_idname = "tp_ops.origin_obm"          
    bl_label = "origin to selected / in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
    

class tp_ops_OriginEdm(bpy.types.Operator):
    """set origin to selected / stay in editmode"""                 
    bl_idname = "tp_ops.origin_edm"          
    bl_label = "origin to selected in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class tp_ops_Origin_Edm_Cursor(bpy.types.Operator):
    """set origin to cursor / stay in editmode"""                 
    bl_idname = "tp_ops.origin_cursor_edm"          
    bl_label = "origin to cursor in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class tp_ops_Origin_Obm_Cursor(bpy.types.Operator):
    """set origin to cursor / stay in objectmode"""                 
    bl_idname = "tp_ops.origin_cursor_obm"          
    bl_label = "origin to cursor in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}   



class PlaceOrigin(bpy.types.Operator):
    '''Set Origin'''
    bl_idname = "place.origin"
    bl_label = "Set Origin"
    bl_options = {"REGISTER", 'UNDO'}   

    geoto = bpy.props.BoolProperty(name="Geometry to Origin",  description="Place Origin", default = False)   
    orito = bpy.props.BoolProperty(name="Origin to Geometry",  description="Place Origin", default = False)   
    cursor = bpy.props.BoolProperty(name="Origin to 3D Cursor",  description="Place Origin", default = False)   
    mass = bpy.props.BoolProperty(name="Origin to MassCenter",  description="Place Origin", default = False)   
    mode_obm = bpy.props.BoolProperty(name="Switch Mode",  description="Switch the Mode", default = False)   
    cursor_edm = bpy.props.BoolProperty(name="Set to Cursor",  description="Set to Cursor", default = True)   
    mode = bpy.props.BoolProperty(name="Switch Mode",  description="Switch the Mode", default = False)   

    def draw(self, context):
        layout = self.layout.column(1)
        box = layout.box().column(1)

        row = box.column(1)         
        if context.mode == 'OBJECT':   
            row.prop(self, 'geoto')
            row.prop(self, 'orito')
            row.prop(self, 'cursor')
            row.prop(self, 'mass')
            row.prop(self, 'mode_obm')
        else:             
            row.prop(self, 'cursor_edm')
            row.prop(self, 'mode')

        #row.operator('wm.operator_defaults', text="Reset", icon ="RECOVER_AUTO")    

    def execute(self, context):
        

        if bpy.context.mode == 'OBJECT':
            
            for i in range(self.geoto):
                bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
            
            for i in range(self.orito):               
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for i in range(self.cursor):
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            
            for i in range(self.mass):
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        
            for i in range(self.mode_obm):
                bpy.ops.object.editmode_toggle()

        if bpy.context.mode == 'EDIT_MESH':
            
            for i in range(self.cursor_edm):            
                bpy.ops.view3d.snap_cursor_to_selected()
           
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            bpy.ops.object.editmode_toggle()
            
            for i in range(self.mode):
                bpy.ops.object.editmode_toggle()
        
        return{'FINISHED'}
 
    def invoke(self, context, event):
        self.geoto
        self.orito
        self.cursor
        self.mass
        self.mode_obm
        self.mode
        return context.window_manager.invoke_props_dialog(self, width = 150)    

 



class BBox_Origin_Back(bpy.types.Operator):
    """BBox Origin Set :)"""
    bl_label = "BBox Origin Set :)"
    bl_idname = "tp_ops.bbox_origin_set"               
    bl_options = {'REGISTER', 'UNDO'}  
        
    #####
    Back_Left_Top = bpy.props.BoolProperty(name="Back-Left-Top",  description="Back-Left-Top", default=False)     
    Back_Top = bpy.props.BoolProperty(name="Back-Top",  description="Back-Top", default=False)     
    Back_Right_Top = bpy.props.BoolProperty(name="Back-Right-Top",  description="Back-Right-Top", default=False)     

    Back_Left = bpy.props.BoolProperty(name="Back-Left-Top",  description="Back-Left-Top", default=False)     
    Back = bpy.props.BoolProperty(name="Back-Top",  description="Back-Top", default=False)     
    Back_Right = bpy.props.BoolProperty(name="Back-Right-Top",  description="Back-Right-Top", default=False)  

    Back_Left_Bottom = bpy.props.BoolProperty(name="Back-Left-Bottom",  description="Back-Left-Bottom", default=False)     
    Back_Bottom = bpy.props.BoolProperty(name="Back-Bottom",  description="Back-Bottom", default=False)     
    Back_Right_Bottom = bpy.props.BoolProperty(name="Back-Right-Bottom",  description="Back-Right-Bottom", default=False)  

    #####
    Middle_Left_Top = bpy.props.BoolProperty(name="Middle-Left-Top",  description="Middle-Left-Top", default=False)     
    Top = bpy.props.BoolProperty(name="Top",  description="Top", default=False)     
    Middle_Right_Top = bpy.props.BoolProperty(name="Middle-Right-Top",  description="Middle-Right-Top", default=False)     

    Left = bpy.props.BoolProperty(name="Middle-Left-Top",  description="Middle-Left-Top", default=False)     
    Middle = bpy.props.BoolProperty(name="Middle",  description="Middle", default=False)        
    Right = bpy.props.BoolProperty(name="Middle-Right-Top",  description="Middle-Right-Top", default=False)  

    Middle_Left_Bottom = bpy.props.BoolProperty(name="Middle-Left-Bottom",  description="Middle-Left-Bottom", default=False)     
    Bottom = bpy.props.BoolProperty(name="Middle-Bottom",  description="Middle-Bottom", default=False)     
    Middle_Right_Bottom = bpy.props.BoolProperty(name="Middle-Right-Bottom",  description="Middle-Right-Bottom", default=False)  

    #####
    Front_Left_Top = bpy.props.BoolProperty(name="Front-Left-Top",  description="Front-Left-Top", default=False)     
    Front_Top = bpy.props.BoolProperty(name="Front-Top",  description="Front-Top", default=False)     
    Front_Right_Top = bpy.props.BoolProperty(name="Front-Right-Top",  description="Front-Right-Top", default=False)     

    Front_Left = bpy.props.BoolProperty(name="Front-Left-Top",  description="Front-Left-Top", default=False)     
    Front = bpy.props.BoolProperty(name="Front-Top",  description="Front-Top", default=False)     
    Front_Right = bpy.props.BoolProperty(name="Front-Right-Top",  description="Front-Right-Top", default=False)  

    Front_Left_Bottom = bpy.props.BoolProperty(name="Front-Left-Bottom",  description="Front-Left-Bottom", default=False)     
    Front_Bottom = bpy.props.BoolProperty(name="Front-Bottom",  description="Front-Bottom", default=False)     
    Front_Right_Bottom = bpy.props.BoolProperty(name="Front-Right-Bottom",  description="Front-Right-Bottom", default=False)  


    def draw(self, context):
        layout = self.layout
       
        icons = load_icons()
     
        box = layout.box().column(1)     
        box.scale_x = 0.1


        #####  
        
        row = box.row(1)                                     
        sub1 = row.row(1)

        sub1.alignment ='LEFT'         
        sub1.label(" +Y Axis")

        sub2 = row.row(1)
        sub2.alignment ='CENTER'         
        sub2.label("   xY Axis")

        sub3 = row.row(1)
        sub3.alignment ='RIGHT'         
        sub3.label("--Y Axis")



        #####  
        
        row = box.row(1)                                     
        sub1 = row.row(1)

        sub1.alignment ='LEFT' 

        button_origin_left_top = icons.get("icon_origin_left_top")           
        sub1.prop(self, 'Back_Left_Top', text="", icon_value=button_origin_left_top.icon_id)

        button_origin_top = icons.get("icon_origin_top")     
        sub1.prop(self, 'Back_Top', text="", icon_value=button_origin_top.icon_id)

        button_origin_right_top = icons.get("icon_origin_right_top")   
        sub1.prop(self, 'Back_Right_Top', text="", icon_value=button_origin_right_top.icon_id)

        sub2 = row.row(1)
        sub2.alignment ='CENTER' 
        
        button_origin_left_top = icons.get("icon_origin_left_top")                   
        sub2.prop(self, 'Middle_Left_Top', text="", icon_value=button_origin_left_top.icon_id)

        button_origin_top = icons.get("icon_origin_top")         
        sub2.prop(self, 'Top', text="", icon_value=button_origin_top.icon_id)

        button_origin_right_top = icons.get("icon_origin_right_top")   
        sub2.prop(self, 'Middle_Right_Top', text="", icon_value=button_origin_right_top.icon_id)

        sub3 = row.row(1)
        sub3.alignment ='RIGHT' 
        
        button_origin_left_top = icons.get("icon_origin_left_top")         
        sub3.prop(self, 'Front_Left_Top', text="", icon_value=button_origin_left_top.icon_id)

        button_origin_top = icons.get("icon_origin_top") 
        sub3.prop(self, 'Front_Top', text="", icon_value=button_origin_top.icon_id)
        
        button_origin_right_top = icons.get("icon_origin_right_top")           
        sub3.prop(self, 'Front_Right_Top', text="", icon_value=button_origin_right_top.icon_id)
        

        #####

        row = box.row(1) 
         
        sub1 = row.row(1)
        sub1.alignment ='LEFT' 
        
        button_origin_left = icons.get("icon_origin_left")        
        sub1.prop(self, 'Back_Left', text="", icon_value=button_origin_left.icon_id)
        
        button_origin_diagonal = icons.get("icon_origin_diagonal")        
        sub1.prop(self, 'Back', text="", icon_value=button_origin_diagonal.icon_id)

        button_origin_right = icons.get("icon_origin_right")
        sub1.prop(self, 'Back_Right', text="", icon_value=button_origin_right.icon_id)

        sub2 = row.row(1)
        sub2.alignment ='CENTER' 

        button_origin_left = icons.get("icon_origin_left")  
        sub2.prop(self, 'Left', text="", icon_value=button_origin_left.icon_id)

        button_origin_cross = icons.get("icon_origin_cross")
        sub2.prop(self, 'Middle', text="", icon_value=button_origin_cross.icon_id)

        button_origin_right = icons.get("icon_origin_right")
        sub2.prop(self, 'Right', text="", icon_value=button_origin_right.icon_id)

        sub3 = row.row(1)
        sub3.alignment ='RIGHT' 
        
        button_origin_left = icons.get("icon_origin_left")  
        sub3.prop(self, 'Front_Left', text="", icon_value=button_origin_left.icon_id)

        button_origin_diagonal = icons.get("icon_origin_diagonal")  
        sub3.prop(self, 'Front', text="", icon_value=button_origin_diagonal.icon_id)
        
        button_origin_right = icons.get("icon_origin_right")
        sub3.prop(self, 'Front_Right', text="", icon_value=button_origin_right.icon_id)


        #####

        row = box.row(1)
          
        sub1 = row.row(1)
        sub1.alignment ='LEFT' 
        
        button_origin_left_bottom = icons.get("icon_origin_left_bottom")        
        sub1.prop(self, 'Back_Left_Bottom', text="", icon_value=button_origin_left_bottom.icon_id)

        button_origin_bottom = icons.get("icon_origin_bottom")
        sub1.prop(self, 'Back_Bottom', text="", icon_value=button_origin_bottom.icon_id)
        
        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
        sub1.prop(self, 'Back_Right_Bottom', text="", icon_value=button_origin_right_bottom.icon_id)

        sub2 = row.row(1)
        sub2.alignment ='CENTER' 

        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
        sub2.prop(self, 'Middle_Left_Bottom', text="", icon_value=button_origin_left_bottom.icon_id)

        button_origin_bottom = icons.get("icon_origin_bottom")
        sub2.prop(self, 'Bottom', text="", icon_value=button_origin_bottom.icon_id)

        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
        sub2.prop(self, 'Middle_Right_Bottom', text="", icon_value=button_origin_right_bottom.icon_id)    

        sub3 = row.row(1)
        sub3.alignment ='RIGHT' 
        
        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
        sub3.prop(self, 'Front_Left_Bottom', text="",icon_value=button_origin_left_bottom.icon_id)
        
        button_origin_bottom = icons.get("icon_origin_bottom")
        sub3.prop(self, 'Front_Bottom', text="", icon_value=button_origin_bottom.icon_id)

        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
        sub3.prop(self, 'Front_Right_Bottom', text="", icon_value=button_origin_right_bottom.icon_id)

        #####

        box = layout.box().column(1) 
         
        row = box.row(1)
        row.prop(context.object, "show_bounds", text="Show Bounds", icon='STICKY_UVS_LOC') 

        sub = row.row(1)
        sub.scale_x = 0.5  
        sub.prop(context.object, "draw_bounds_type", text="") 


    def execute(self, context):

        #Top         
        for i in range(self.Back_Left_Top):        
            bpy.ops.tp_ops.cubeback_cornertop_minus_xy()
        
        for i in range(self.Back_Top):   
            bpy.ops.tp_ops.cubeback_edgetop_minus_y()
        
        for i in range(self.Back_Right_Top):            
            bpy.ops.tp_ops.cubeback_cornertop_plus_xy()
             
        #Middle          
        for i in range(self.Back_Left):        
            bpy.ops.tp_ops.cubefront_edgemiddle_minus_x()
        
        for i in range(self.Back):            
            bpy.ops.tp_ops.cubefront_side_plus_y() 
        
        for i in range(self.Back_Right):            
            bpy.ops.tp_ops.cubefront_edgemiddle_plus_x()   
         
        #Bottom       
        for i in range(self.Back_Left_Bottom):        
            bpy.ops.tp_ops.cubeback_cornerbottom_minus_xy()
        
        for i in range(self.Back_Bottom):            
            bpy.ops.tp_ops.cubefront_edgebottom_plus_y() 
       
        for i in range(self.Back_Right_Bottom):            
            bpy.ops.tp_ops.cubeback_cornerbottom_plus_xy()  
                   

        #####

        #Top
        for i in range(self.Middle_Left_Top):
            bpy.ops.tp_ops.cubefront_edgetop_minus_x()

        for i in range(self.Top):
            bpy.ops.tp_ops.cubefront_side_plus_z()

        for i in range(self.Middle_Right_Top):
            bpy.ops.tp_ops.cubefront_edgetop_plus_x()              
         
        #Middle
        for i in range(self.Left):                   
            bpy.ops.tp_ops.cubefront_side_minus_x()
        
        for i in range(self.Middle):        
            if context.mode == "EDIT_MESH":
                bpy.ops.mesh.select_all(action='SELECT') 
                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.editmode_toggle() 
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                bpy.ops.object.editmode_toggle()
            else:
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
              
        for i in range(self.Right):                         
            bpy.ops.tp_ops.cubefront_side_plus_x()              
    
        #Bottom
        for i in range(self.Middle_Left_Bottom):
            bpy.ops.tp_ops.cubefront_edgebottom_minus_x()

        for i in range(self.Bottom):           
            bpy.ops.tp_ops.cubefront_side_minus_z()             

        for i in range(self.Middle_Right_Bottom):           
            bpy.ops.tp_ops.cubefront_edgebottom_plus_x()  


        #####

        #Top                    
        for i in range(self.Front_Left_Top):
            bpy.ops.tp_ops.cubefront_cornertop_minus_xy()

        for i in range(self.Front_Top):
            bpy.ops.tp_ops.cubeback_edgetop_plus_y()

        for i in range(self.Front_Right_Top):
            bpy.ops.tp_ops.cubefront_cornertop_plus_xy()
                        

        #Middle                      
        for i in range(self.Front_Left):
            bpy.ops.tp_ops.cubefront_edgemiddle_minus_y()     

        for i in range(self.Front):
            bpy.ops.tp_ops.cubefront_side_minus_y()       

        for i in range(self.Front_Right):
            bpy.ops.tp_ops.cubefront_edgemiddle_plus_y()          


        #Bottom
        for i in range(self.Front_Left_Bottom):
            bpy.ops.tp_ops.cubefront_cornerbottom_minus_xy()             
       
        for i in range(self.Front_Bottom):
            bpy.ops.tp_ops.cubefront_edgebottom_minus_y()

        for i in range(self.Front_Right_Bottom):
            bpy.ops.tp_ops.cubefront_cornerbottom_plus_xy()
             
        return {'FINISHED'}

    def check(self, context):
        return True

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)



    
# REGISTER
  
def register():

    bpy.utils.register_module(__name__)
 
    
def unregister():

    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()




















