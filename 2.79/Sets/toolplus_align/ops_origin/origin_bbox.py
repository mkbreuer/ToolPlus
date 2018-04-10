# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons


class VIEW3D_TP_BBox_Origin_Back(bpy.types.Operator):
    """BBox Origin"""
    bl_label = "BBox Origin"
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
        
        row = box.row(1)                                     
        row.alignment ='CENTER'         
        row.label(" +Y Axis")
        row.separator() 
        row.label("   xY Axis")
        row.separator()   
        row.label("--Y Axis")

        #####                  
        row = box.row(1)                                     
        row.alignment ='CENTER'
         
        button_origin_left_top = icons.get("icon_origin_left_top")   
        row.operator('tp_ops.cubeback_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
       
        button_origin_top = icons.get("icon_origin_top")  
        row.operator('tp_ops.cubeback_edgetop_minus_y', text="", icon_value=button_origin_top.icon_id)
        
        button_origin_right_top = icons.get("icon_origin_right_top")
        row.operator('tp_ops.cubeback_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)

        row.separator()
        
        button_origin_left_top = icons.get("icon_origin_left_top")   
        row.operator('tp_ops.cubefront_edgetop_minus_x', text="", icon_value=button_origin_left_top.icon_id)
        
        button_origin_top = icons.get("icon_origin_top")  
        row.operator('tp_ops.cubefront_side_plus_z', text="", icon_value=button_origin_top.icon_id)
        
        button_origin_right_top = icons.get("icon_origin_right_top")
        row.operator('tp_ops.cubefront_edgetop_plus_x', text="", icon_value=button_origin_right_top.icon_id)

        row.separator()
        
        button_origin_left_top = icons.get("icon_origin_left_top")   
        row.operator('tp_ops.cubefront_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
        
        button_origin_top = icons.get("icon_origin_top")  
        row.operator('tp_ops.cubeback_edgetop_plus_y', text="", icon_value=button_origin_top.icon_id)
        
        button_origin_right_top = icons.get("icon_origin_right_top")
        row.operator('tp_ops.cubefront_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)
        
        #####

        row = box.row(1)                          
        row.alignment ='CENTER' 
        
        button_origin_left = icons.get("icon_origin_left")
        row.operator('tp_ops.cubefront_edgemiddle_minus_x', text="", icon_value=button_origin_left.icon_id)
       
        button_origin_cross = icons.get("icon_origin_cross")
        row.operator('tp_ops.cubefront_side_plus_y', text="", icon_value=button_origin_cross.icon_id)
        
        button_origin_right = icons.get("icon_origin_right")
        row.operator('tp_ops.cubefront_edgemiddle_plus_x', text="", icon_value=button_origin_right.icon_id)

        row.separator()

        button_origin_left = icons.get("icon_origin_left")
        row.operator('tp_ops.cubefront_side_minus_x', text="", icon_value=button_origin_left.icon_id)
       
        if context.mode == 'OBJECT':
            button_origin_diagonal = icons.get("icon_origin_diagonal")
            row.operator('object.origin_set', text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'
        else:
            button_origin_diagonal = icons.get("icon_origin_diagonal")
            row.operator('tp_ops.origin_set_editcenter', text="", icon_value=button_origin_diagonal.icon_id)
        
        button_origin_right = icons.get("icon_origin_right")
        row.operator('tp_ops.cubefront_side_plus_x', text="", icon_value=button_origin_right.icon_id)

        row.separator()
        
        button_origin_left = icons.get("icon_origin_left")
        row.operator('tp_ops.cubefront_edgemiddle_minus_y', text="", icon_value=button_origin_left.icon_id)
        
        button_origin_cross = icons.get("icon_origin_cross")
        row.operator('tp_ops.cubefront_side_minus_y', text="", icon_value=button_origin_cross.icon_id)
        
        button_origin_right = icons.get("icon_origin_right")
        row.operator('tp_ops.cubefront_edgemiddle_plus_y', text="", icon_value=button_origin_right.icon_id)

        #####

        row = box.row(1)
        row.alignment ='CENTER' 
        
        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
        row.operator('tp_ops.cubeback_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
        
        button_origin_bottom = icons.get("icon_origin_bottom")
        row.operator('tp_ops.cubefront_edgebottom_plus_y', text="", icon_value=button_origin_bottom.icon_id)
        
        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
        row.operator('tp_ops.cubeback_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

        row.separator()
        
        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
        row.operator('tp_ops.cubefront_edgebottom_minus_x', text="", icon_value=button_origin_left_bottom.icon_id)
        
        button_origin_bottom = icons.get("icon_origin_bottom")
        row.operator('tp_ops.cubefront_side_minus_z', text="", icon_value=button_origin_bottom.icon_id)
        
        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
        row.operator('tp_ops.cubefront_edgebottom_plus_x', text="", icon_value=button_origin_right_bottom.icon_id)    

        row.separator()

        button_origin_left_bottom = icons.get("icon_origin_left_bottom")
        row.operator('tp_ops.cubefront_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
        
        button_origin_bottom = icons.get("icon_origin_bottom")
        row.operator('tp_ops.cubefront_edgebottom_minus_y', text="", icon_value=button_origin_bottom.icon_id)
        
        button_origin_right_bottom = icons.get("icon_origin_right_bottom")
        row.operator('tp_ops.cubefront_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

        box.separator()


        #####


        box = layout.box().column(1) 
         
        row = box.row(1)
        row.prop(context.object, "show_bounds", text="Show Bounds", icon='STICKY_UVS_LOC') 
        row.prop(context.object, "draw_bounds_type", text="") 


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





















