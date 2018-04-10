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
from .. icons.icons import load_icons    


class View3D_TP_Origin_Batch(bpy.types.Operator):
    """Origin"""
    bl_label = "Origin"
    bl_idname = "tp_batch.origin_batch"               
    bl_options = {'REGISTER', 'UNDO'}  
        
    def draw(self, context):
        layout = self.layout
        
        tp_props = context.window_manager.tp_props_origin     
          
        icons = load_icons()

        col = layout.column(1)   

        if context.mode == 'OBJECT':

            box = col.box().column(1)                         
            
            row = box.column(1)
            
            button_origin_center_view = icons.get("icon_origin_center_view")
            row.operator("object.transform_apply", text="Center", icon_value=button_origin_center_view.icon_id).location=True

            button_origin_cursor = icons.get("icon_origin_cursor")
            row.operator("tp_ops.origin_set_cursor", text="Cursor", icon_value=button_origin_cursor.icon_id)

            row.separator()
            
            button_origin_tomesh = icons.get("icon_origin_tomesh")
            row.operator("tp_ops.origin_tomesh", text="Origin to Geom", icon_value=button_origin_tomesh.icon_id)

            button_origin_meshto = icons.get("icon_origin_meshto")
            row.operator("tp_ops.origin_meshto", text="Geom to Origin", icon_value=button_origin_meshto.icon_id)

            selected = bpy.context.selected_objects
            n = len(selected)                         
            if n == 1:

                button_origin_tosnap = icons.get("icon_origin_tosnap")         
                row.operator("tp_ops.origin_modal", text="Snap to Geom", icon_value=button_origin_tosnap.icon_id)

            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_tools
            if display_advanced == 'on':
                pass
            else:  

                n = len(selected)            
                if n == 2:

                    if tp_props.display_origin_active:                     
                        
                        button_origin_copy = icons.get("icon_origin_copy")           
                        row.prop(tp_props, "display_origin_active", text="Align to Active", icon_value=button_origin_copy.icon_id)                      

                    else:
                       
                        button_origin_toactive = icons.get("icon_origin_toactive")               
                        row.prop(tp_props, "display_origin_active", text="Align to Active", icon_value=button_origin_toactive.icon_id)                        

                    if tp_props.display_origin_active: 
               
                        box.separator()
                        
                        row = box.row(1)                        
                        
                        row = box.row()
                        row.prop(tp_props, 'tp_axis_active', expand=True)
                        
                        box.separator() 
     
                        row = box.row()                        
                        row.prop(tp_props, 'tp_distance_active', expand=True)                                              
                        row.operator("tp_ops.origin_to_active", text="RUN")                
                     
                        box.separator() 
                        
                        row = box.row(1)
                        
                        if tp_props.active_too == True:
                            row.prop(tp_props, 'active_too', text="Active Origin too!", icon="LAYER_ACTIVE")
                        else:
                            row.prop(tp_props, 'active_too', text="Not Active Origin!", icon="LAYER_USED")
                                            
                        box.separator()
                        box = col.box().column(1)     


            row.separator()

            button_origin_mass = icons.get("icon_origin_mass")           
            row.operator("tp_ops.origin_set_mass", text="Center of Mass", icon_value=button_origin_mass.icon_id)

            box.separator()


            row = box.row(1)
            
            if tp_props.display_origin_bbox:                     
                
                button_origin_bbox = icons.get("icon_origin_bbox")            
                row.prop(tp_props, "display_origin_bbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)                     
               
                row.operator("object.bbox_origin_modal_ops", text="1-BBox")
          
            else:
               
                button_origin_bbox = icons.get("icon_origin_bbox")                
                row.prop(tp_props, "display_origin_bbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)
                
                row.operator("object.bbox_origin_modal_ops", text="1-BBox")
                            
            if bpy.context.object.type == 'MESH':
                
                
                if tp_props.display_origin_bbox: 
                 
                    box.separator()                   
                     
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
                    box.separator()

                    row = box.row(1)
                    row.prop(context.object, "show_bounds", text="Show Bounds") 
                    row.prop(context.object, "draw_bounds_type", text="") 

                    box.separator()
                    box = col.box().column(1) 



            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_tools
            if display_advanced == 'on':  

                box.separator()          
               
                row = box.column(1)

                button_origin_distribute = icons.get("icon_origin_distribute")  
                row.operator("object.distribute_osc", "Distribute", icon_value=button_origin_distribute.icon_id)

                button_origin_align = icons.get("icon_origin_align")                
                row.operator("tp_origin.align_tools", "Advanced", icon_value=button_origin_align.icon_id)    
      


            box.separator()  
             
            row = box.row(1)
            
            if tp_props.display_origin_zero:                     
                button_align_zero = icons.get("icon_align_zero")          
                row.prop(tp_props, "display_origin_zero", text="Zero to Axis", icon_value=button_align_zero.icon_id)                             
           
            else:
                button_align_zero = icons.get("icon_align_zero")              
                row.prop(tp_props, "display_origin_zero", text="Zero to Axis", icon_value=button_align_zero.icon_id)               

            if tp_props.display_origin_zero: 

                box.separator()   

                row = box.row(1)
                row.prop(context.scene, 'tp_switch_axis', expand=True)

                box.separator() 
                
                row = box.row()
                row.prop(context.scene, 'tp_switch', expand=True)

                sub = row.row(1)
                sub.scale_x = 0.95         
                button_origin_apply = icons.get("icon_origin_apply")  
                sub.operator("tp_ops.zero_axis_panel", "RUN")#, icon_value=button_origin_apply.icon_id)  


            box.separator()    


                           

        else:

            box = col.box().column(1) 
            
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
                
                row = box.row(1)
                
                if tp_props.display_origin_editbox:                     
                    button_origin_bbox = icons.get("icon_origin_bbox")            
                    row.prop(tp_props, "display_origin_editbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)                     
                else:
                    button_origin_bbox = icons.get("icon_origin_bbox")                
                    row.prop(tp_props, "display_origin_editbox", text="X-BBox", icon_value=button_origin_bbox.icon_id)
                    
                if tp_props.display_origin_editbox:        

                    box.separator()    
                    
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
                    box = col.box().column(1) 
                    box.separator()  

            else:
                box.separator()                 



            display_advanced = context.user_preferences.addons[__package__].preferences.tab_display_tools
            if display_advanced == 'on':  

                box.separator()          
               
                row = box.column(1)
                button_origin_mesh = icons.get("icon_origin_mesh")                
                row.operator("tp_ops.origin_transform", "Advanced", icon_value=button_origin_mesh.icon_id)    
      
        
            box.separator()  
            
            row = box.row(1)         

            if tp_props.display_origin_zero_edm:                     
                button_align_zero = icons.get("icon_align_zero")          
                row.prop(tp_props, "display_origin_zero_edm", text="ZeroAxis", icon_value=button_align_zero.icon_id)                             

            else:
                button_align_zero = icons.get("icon_align_zero")              
                row.prop(tp_props, "display_origin_zero_edm", text="ZeroAxis", icon_value=button_align_zero.icon_id)               
                                   
            if tp_props.display_origin_zero_edm: 

                box.separator()   

                row = box.row(1)
                row.prop(context.scene, 'tp_switch_axis', expand=True)       
            
                box.separator() 

                row = box.row()
                row.prop(context.scene, 'tp_switch', expand=True)
                
                sub = row.row(1)
                sub.scale_x = 0.95         
                button_origin_apply = icons.get("icon_origin_apply")  
                sub.operator("tp_ops.zero_axis_panel", "RUN")#, icon_value=button_origin_apply.icon_id)  

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