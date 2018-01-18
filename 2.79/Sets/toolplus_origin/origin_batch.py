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


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    


class View3D_TP_Origin_Batch(bpy.types.Operator):
    """Origin"""
    bl_label = "Origin"
    bl_idname = "tp_batch.origin_batch"               
    bl_options = {'REGISTER', 'UNDO'}  
        
    def draw(self, context):
        layout = self.layout
        
        tp_props = context.window_manager.bbox_origin_window     
          
        icons = load_icons()

        if context.mode == 'OBJECT':

            box = layout.box().column(1)                         
            
            row = box.column(1)
            
            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_set_cursor", text="Cursor", icon_value=button_origin_cursor.icon_id)

            row.separator()
            
            button_origin_tomesh = icons.get("icon_origin_tomesh")
            row.operator("tp_ops.origin_tomesh", text="Origin to Mesh", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            row.operator("tp_ops.origin_meshto", text="Mesh to Origin", icon_value=button_origin_meshto.icon_id)

            row.separator()
            
            button_origin_mass = icons.get("icon_origin_mass")           
            row.operator("tp_ops.origin_set_mass", text="Center of Mass", icon_value=button_origin_mass.icon_id)


            box = layout.box().column(1)
            row = box.row(1)
            
            if tp_props.display_origin_bbox:                     
                
                button_origin_bbox = icons.get("icon_origin_bbox")            
                row.prop(tp_props, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)                     
               
                row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
          
            else:
               
                button_origin_bbox = icons.get("icon_origin_bbox")                
                row.prop(tp_props, "display_origin_bbox", text="", icon_value=button_origin_bbox.icon_id)
                
                row.operator("object.bbox_origin_modal_ops", text="   BBoxOrigin")
                            

            obj = context.active_object
            if obj:
                obj_type = obj.type
                
                if obj.type in {'MESH'}:

                    if tp_props.display_origin_bbox: 
                 

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


            box = layout.box().column(1) 
             
            row = box.row(1)
            
            if tp_props.display_origin_zero:                     
                button_align_zero = icons.get("icon_align_zero")          
                row.prop(tp_props, "display_origin_zero", text="", icon_value=button_align_zero.icon_id)                             
               
                row.operator("tp_ops.zero_axis_panel", "   ZeroAxis")  
           
            else:
                button_align_zero = icons.get("icon_align_zero")              
                row.prop(tp_props, "display_origin_zero", text="", icon_value=button_align_zero.icon_id)               
               
                row.operator("tp_ops.zero_axis_panel", "   ZeroAxis")  
                    
            if tp_props.display_origin_zero: 

                box.separator()   
                
                row = box.row(1)
                row.prop(context.scene, 'tp_switch', expand=True)

                row = box.row()
                row.prop(context.scene, 'tp_switch_axis', expand=True)
                
            box.separator()    


            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_advanced
            if display_advanced == 'on':  

                box = layout.box().column(1) 
                
                row = box.column(1)

                button_origin_distribute = icons.get("icon_origin_distribute")  
                row.operator("object.distribute_osc", "Distribute", icon_value=button_origin_distribute.icon_id)

                button_origin_align = icons.get("icon_origin_align")                
                row.operator("tp_origin.align_tools", "Advanced", icon_value=button_origin_align.icon_id)    
      

                box.separator()                                     


        else:   

            box = layout.box().column(1) 
            
            row = box.column(1) 

            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_cursor_edm", text="Cursor", icon_value=button_origin_cursor.icon_id)            

            row.separator()

            button_origin_edm = icons.get("icon_origin_edm")            
            row.operator("tp_ops.origin_edm","Edm-Select", icon_value=button_origin_edm.icon_id)       

            button_origin_obj = icons.get("icon_origin_obj")   
            row.operator("tp_ops.origin_obm","Obm-Select", icon_value=button_origin_obj.icon_id)             

            if context.mode == 'EDIT_MESH':
            
                row.separator()
         
                button_origin_ccc = icons.get("icon_origin_ccc")            
                row.operator("tp_ops.origin_ccc","3P-Center", icon_value=button_origin_ccc.icon_id)    

                box.separator() 
 
                box = layout.box().column(1)     
                box.scale_x = 0.1
                
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
                sub1.operator('tp_ops.cubeback_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
               
                button_origin_top = icons.get("icon_origin_top")  
                sub1.operator('tp_ops.cubeback_edgetop_minus_y', text="", icon_value=button_origin_top.icon_id)
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                sub1.operator('tp_ops.cubeback_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)

                sub2 = row.row(1)
                sub2.alignment ='CENTER' 
                
                button_origin_left_top = icons.get("icon_origin_left_top")   
                sub2.operator('tp_ops.cubefront_edgetop_minus_x', text="", icon_value=button_origin_left_top.icon_id)
                
                button_origin_top = icons.get("icon_origin_top")  
                sub2.operator('tp_ops.cubefront_side_plus_z', text="", icon_value=button_origin_top.icon_id)
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                sub2.operator('tp_ops.cubefront_edgetop_plus_x', text="", icon_value=button_origin_right_top.icon_id)

                sub3 = row.row(1)
                sub3.alignment ='RIGHT' 
                
                button_origin_left_top = icons.get("icon_origin_left_top")   
                sub3.operator('tp_ops.cubefront_cornertop_minus_xy', text="", icon_value=button_origin_left_top.icon_id)
                
                button_origin_top = icons.get("icon_origin_top")  
                sub3.operator('tp_ops.cubeback_edgetop_plus_y', text="", icon_value=button_origin_top.icon_id)
                
                button_origin_right_top = icons.get("icon_origin_right_top")
                sub3.operator('tp_ops.cubefront_cornertop_plus_xy', text="", icon_value=button_origin_right_top.icon_id)
                
                #####

                row = box.row(1) 
                 
                sub1 = row.row(1)
                sub1.alignment ='LEFT' 
                
                button_origin_left = icons.get("icon_origin_left")
                sub1.operator('tp_ops.cubefront_edgemiddle_minus_x', text="", icon_value=button_origin_left.icon_id)
               
                button_origin_cross = icons.get("icon_origin_cross")
                sub1.operator('tp_ops.cubefront_side_plus_y', text="", icon_value=button_origin_cross.icon_id)
                
                button_origin_right = icons.get("icon_origin_right")
                sub1.operator('tp_ops.cubefront_edgemiddle_plus_x', text="", icon_value=button_origin_right.icon_id)

                sub2 = row.row(1)
                sub2.alignment ='CENTER' 

                button_origin_left = icons.get("icon_origin_left")
                sub2.operator('tp_ops.cubefront_side_minus_x', text="", icon_value=button_origin_left.icon_id)
               
                if context.mode == 'OBJECT':
                    button_origin_diagonal = icons.get("icon_origin_diagonal")
                    sub2.operator('object.origin_set', text="", icon_value=button_origin_diagonal.icon_id).type='ORIGIN_GEOMETRY'
                else:
                    button_origin_diagonal = icons.get("icon_origin_diagonal")
                    sub2.operator('tp_ops.origin_set_editcenter', text="", icon_value=button_origin_diagonal.icon_id)
                
                button_origin_right = icons.get("icon_origin_right")
                sub2.operator('tp_ops.cubefront_side_plus_x', text="", icon_value=button_origin_right.icon_id)

                sub3 = row.row(1)
                sub3.alignment ='RIGHT' 
                
                button_origin_left = icons.get("icon_origin_left")
                sub3.operator('tp_ops.cubefront_edgemiddle_minus_y', text="", icon_value=button_origin_left.icon_id)
                
                button_origin_cross = icons.get("icon_origin_cross")
                sub3.operator('tp_ops.cubefront_side_minus_y', text="", icon_value=button_origin_cross.icon_id)
                
                button_origin_right = icons.get("icon_origin_right")
                sub3.operator('tp_ops.cubefront_edgemiddle_plus_y', text="", icon_value=button_origin_right.icon_id)

                #####

                row = box.row(1)
                  
                sub1 = row.row(1)
                sub1.alignment ='LEFT' 
                
                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                sub1.operator('tp_ops.cubeback_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                sub1.operator('tp_ops.cubefront_edgebottom_plus_y', text="", icon_value=button_origin_bottom.icon_id)
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                sub1.operator('tp_ops.cubeback_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                sub2 = row.row(1)
                sub2.alignment ='CENTER' 

                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                sub2.operator('tp_ops.cubefront_edgebottom_minus_x', text="", icon_value=button_origin_left_bottom.icon_id)
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                sub2.operator('tp_ops.cubefront_side_minus_z', text="", icon_value=button_origin_bottom.icon_id)
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                sub2.operator('tp_ops.cubefront_edgebottom_plus_x', text="", icon_value=button_origin_right_bottom.icon_id)    

                sub3 = row.row(1)                
                sub3.alignment ='RIGHT' 

                button_origin_left_bottom = icons.get("icon_origin_left_bottom")
                sub3.operator('tp_ops.cubefront_cornerbottom_minus_xy', text="", icon_value=button_origin_left_bottom.icon_id)
                
                button_origin_bottom = icons.get("icon_origin_bottom")
                sub3.operator('tp_ops.cubefront_edgebottom_minus_y', text="", icon_value=button_origin_bottom.icon_id)
                
                button_origin_right_bottom = icons.get("icon_origin_right_bottom")
                sub3.operator('tp_ops.cubefront_cornerbottom_plus_xy', text="", icon_value=button_origin_right_bottom.icon_id)

                box.separator()                        
                    
            else:
                box.separator()                 
                                   


        box = layout.box().column(1)  
        
        row = box.row(1)
        row.operator("ed.undo", text=" ", icon="LOOP_BACK")
        row.operator("ed.redo", text=" ", icon="LOOP_FORWARDS") 
       
        box.separator()   


    def execute(self, context):
   
        return {'FINISHED'}

    def check(self, context):
        return True

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()