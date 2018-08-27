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
import addon_utils


def draw_axis_ui(self, context, layout):
    tp_props = context.window_manager.tp_props_resurface            
  
    layout.operator_context = 'INVOKE_REGION_WIN'
   
    icons = load_icons()     

    col = layout.column(align=True)

    if not tp_props.display_align: 
      
        box = col.box().column(1)
        
        row = box.row(1)   
        row.prop(tp_props, "display_align", text="", icon="TRIA_RIGHT", emboss = False)                
        row.label("Aligned")               

        button_align_x = icons.get("icon_align_x") 
        row.operator("tp_ops.align_transform", "", icon_value=button_align_x.icon_id).tp_axis='axis_x'

        button_align_y = icons.get("icon_align_y") 
        row.operator("tp_ops.align_transform", "", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

        button_align_z = icons.get("icon_align_z") 
        row.operator("tp_ops.align_transform", "", icon_value=button_align_z.icon_id).tp_axis='axis_z'
        

    else:
       
        box = col.box().column(1)
        
        row = box.row(1)  
        row.prop(tp_props, "display_align", text="", icon="TRIA_DOWN", emboss = False)            
        row.label("Aligned")  

        button_align_x = icons.get("icon_align_x") 
        row.operator("tp_ops.align_transform", "", icon_value=button_align_x.icon_id).tp_axis='axis_x'

        button_align_y = icons.get("icon_align_y") 
        row.operator("tp_ops.align_transform", "", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

        button_align_z = icons.get("icon_align_z") 
        row.operator("tp_ops.align_transform", "", icon_value=button_align_z.icon_id).tp_axis='axis_z'

        box.separator() 

        box = col.box().row()   
        
        row = box.column(1) 
        row.label("Align") 
        row.label("to..") 
        row.label("Axis") 

        row = box.column(1)

        button_align_xy = icons.get("icon_align_xy") 
        row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'

        button_align_zx = icons.get("icon_align_zx")
        row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'

        button_align_zy = icons.get("icon_align_zy") 
        row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'           

        row = box.column(1)

        button_align_x = icons.get("icon_align_x") 
        row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'

        button_align_y = icons.get("icon_align_y") 
        row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

        button_align_z = icons.get("icon_align_z") 
        row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'

        row.separator() 


        box = col.box().column(1)               
        
        row = box.row(1)   

        button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
        row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
                 
        sub = row.row(1)
        sub.scale_x = 0.3                   
        sub.operator("tp_ops.mirror1",text="X")
        sub.operator("tp_ops.mirror2",text="Y")
        sub.operator("tp_ops.mirror3",text="Z")            

        box.separator() 





def draw_align_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)

        if not tp_props.display_align: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_align", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Aligned")               

            button_align_x = icons.get("icon_align_x") 
            row.operator("tp_ops.align_transform", "", icon_value=button_align_x.icon_id).tp_axis='axis_x'

            button_align_y = icons.get("icon_align_y") 
            row.operator("tp_ops.align_transform", "", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

            button_align_z = icons.get("icon_align_z") 
            row.operator("tp_ops.align_transform", "", icon_value=button_align_z.icon_id).tp_axis='axis_z'
            

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_align", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Aligned")  

            button_align_x = icons.get("icon_align_x") 
            row.operator("tp_ops.align_transform", "", icon_value=button_align_x.icon_id).tp_axis='axis_x'

            button_align_y = icons.get("icon_align_y") 
            row.operator("tp_ops.align_transform", "", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

            button_align_z = icons.get("icon_align_z") 
            row.operator("tp_ops.align_transform", "", icon_value=button_align_z.icon_id).tp_axis='axis_z'
        
            
            if bpy.context.mode == "OBJECT":

                box = col.box().column(1)  
                        
                row = box.row(1)
                button_align_advance = icons.get("icon_align_advance")
                row.operator("tp_origin.align_tools", " ", icon_value=button_align_advance.icon_id)   
               
                button_align_x = icons.get("icon_align_x") 
                row.label(text=" ", icon_value=button_align_x.icon_id)  
      
                button_align_y = icons.get("icon_align_y") 
                row.label(text=" ", icon_value=button_align_y.icon_id)  
               
                button_align_z = icons.get("icon_align_z") 
                row.label(text=" ", icon_value=button_align_z.icon_id)  
        
                row.label(text=" ", icon='BLANK1')  
                row.label(text=" ", icon='BLANK1')  
               
                row = box.row(1)
                props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_TRANS')   
                props.tp_axis='axis_xyz'
                props.tp_transform='LOCATION'

                props = row.operator("tp_ops.align_transform",text="X")
                props.tp_axis='axis_x'
                props.tp_transform='LOCATION'

                props = row.operator("tp_ops.align_transform",text="Y")
                props.tp_axis='axis_y'
                props.tp_transform='LOCATION' 
     
                props = row.operator("tp_ops.align_transform",text="Z")
                props.tp_axis='axis_z'
                props.tp_transform='LOCATION'
           
                sub = row.row(1)
                sub.scale_x = 2.0    
                sub.operator("object.location_clear", text= " ", icon="X")
              
                props = row.operator("object.transform_apply", text=" ",icon="FILE_TICK")
                props.location= True
                props.rotation= False
                props.scale= False
                             
                row = box.row(1)

                props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_ROT') 
                props.tp_axis='axis_xyz'
                props.tp_transform='ROTATION'

                props = row.operator("tp_ops.align_transform",text="X")
                props.tp_axis='axis_x'
                props.tp_transform='ROTATION'

                props = row.operator("tp_ops.align_transform",text="Y")
                props.tp_axis='axis_y'
                props.tp_transform='ROTATION'

                props = row.operator("tp_ops.align_transform",text="Z")
                props.tp_axis='axis_z'
                props.tp_transform='ROTATION'
                
                sub = row.row(1)
                sub.scale_x = 2.0           
                sub.operator("object.rotation_clear", text=" ", icon="X")
                props = row.operator("object.transform_apply", text=" ",icon="FILE_TICK")
                props.location= False
                props.rotation= True
                props.scale= False           

                row = box.row(1)
                props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_SCALE')  
                props.tp_axis='axis_xyz'
                props.tp_transform='SCALE'

                props = row.operator("tp_ops.align_transform",text="X")
                props.tp_axis='axis_x'
                props.tp_transform='SCALE'

                props = row.operator("tp_ops.align_transform",text="Y")
                props.tp_axis='axis_y'
                props.tp_transform='SCALE'

                props = row.operator("tp_ops.align_transform",text="Z")
                props.tp_axis='axis_z'
                props.tp_transform='SCALE'
                
                sub = row.row(1)
                sub.scale_x = 2.0           
                sub.operator("object.scale_clear", text=" ", icon="X")
                
                props = row.operator("object.transform_apply", text=" ",icon="FILE_TICK")
                props.location= False
                props.rotation= False
                props.scale= True  
           
                box.separator()        
                box.separator()        

                row = box.row(1)  
                row.operator("tp_ops.xy_spread", text="Spread", icon="AXIS_TOP")  
           
                button_origin_align = icons.get("icon_origin_align") 
                row.operator("object.distribute_osc", text="Even", icon_value=button_origin_align.icon_id)           
                 
                box.separator() 
                box.separator() 
                
                row = box.row(1)                     
                row.prop(context.space_data, "transform_orientation", text="", icon='MANIPUL')
                row.operator("transform.create_orientation", text="", icon='ZOOMIN')

                if context.space_data.current_orientation:
                    box.separator() 
                    
                    row = box.row(1)
                    row.prop(context.space_data.current_orientation, "name", text="")
                    row.operator("transform.delete_orientation", text="", icon='X')

                box.separator()       
                box.separator()       
                          
                row = box.row(1)  
                button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
                row.label("Mirror", icon_value=button_align_mirror_obm.icon_id)                 

                sub = row.row(1)
                sub.scale_x = 0.3                               
                sub.operator("tp_ops.mirror1",text="X")
                sub.operator("tp_ops.mirror2",text="Y")
                sub.operator("tp_ops.mirror3",text="Z")      

                box.separator()   
                box.separator()         
                             
                row = box.row(1)             
               
                button_align_zero = icons.get("icon_align_zero") 
                row.label("ZeroTo", icon_value=button_align_zero.icon_id)  
 
                row = box.row()
                row.prop(context.scene, 'tp_switch_axis', expand=True)      

                row = box.row(1)
                row.prop(context.scene, 'tp_switch', expand=True)              
                              
                row.operator("tp_ops.zero_axis_panel", text="RUN")  

                box.separator()  


                obj = context.active_object
                if obj:
                    obj_type = obj.type
                    
                    if obj.type in {'MESH'}:


                        box = col.box().column(1)           

                        row = box.column(1)  

                        button_snap_face_to_face = icons.get("icon_snap_face_to_face") 
                        row.operator("object.align_by_faces", text="Face to Face", icon_value=button_snap_face_to_face.icon_id)  

                        button_snap_drop_down = icons.get("icon_snap_drop_down") 
                        row.operator("object.drop_on_active", text="Drop on Active", icon_value=button_snap_drop_down.icon_id) 

                        #button_snap_abc = icons.get("icon_snap_abc") 
                        #row.operator("tp_ops.np_020_point_align", text='ABC Point Align', icon_value=button_snap_abc.icon_id) 

                        box.separator()     

                        box = col.box().column(1)           
                      
                        row = box.column(1) 
                        row.label("Interpolate...")              
                      
                        row = box.column(1)    
                        row.operator("mesh.wplsmthdef_snap", text="Save Mesh State", icon ="SHAPEKEY_DATA")

                        box.separator() 

                    else:
                        pass




            if bpy.context.mode == "EDIT_MESH":


                col = layout.column(align=True)

                box = col.box().row()   
                
                row = box.column(1) 
                row.label("Align") 
                row.label("to..") 
                row.label("Axis") 

                row = box.column(1)

                button_align_xy = icons.get("icon_align_xy") 
                row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'

                button_align_zx = icons.get("icon_align_zx")
                row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'

                button_align_zy = icons.get("icon_align_zy") 
                row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'           

                row = box.column(1)

                button_align_x = icons.get("icon_align_x") 
                row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'

                button_align_y = icons.get("icon_align_y") 
                row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

                button_align_z = icons.get("icon_align_z") 
                row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'

                row.separator() 
                
                box = col.box().column(1)   
                             
                row = box.row(1)             
                button_align_mirror_edm = icons.get("icon_align_mirror_edm")              
                row.label("Mirror", icon_value=button_align_mirror_edm.icon_id) 

                sub = row.row(1)
                sub.scale_x = 0.3    
                sub.operator("tp_ops.mirror1",text="X")
                sub.operator("tp_ops.mirror2",text="Y")
                sub.operator("tp_ops.mirror3",text="Z")      

                box.separator() 

                row = box.row(1)               
                button_align_mirror_edge = icons.get("icon_align_mirror_edge")   
                row.label("Turn", icon_value=button_align_mirror_edge.icon_id)    
               
                sub = row.row(1)
                sub.scale_x = 0.9          
                sub.operator("tp_ops.mirror_over_edge", "Over Edge")

                box.separator() 
                
                box = col.box().column(1)
                
                row = box.row(1) 
                row.operator("mesh.align_operator", text = 'Store Edge').type_op = 1
                align_op = row.operator("mesh.align_operator", text = 'Align Edges').type_op = 0

                box.separator()      
     
                row = box.row(1) 
                if tp_props.display_align_help:
                    row.prop(tp_props, "display_align_help", text="", icon='INFO')
                else:
                    row.prop(tp_props, "display_align_help", text="", icon='INFO')

                row.prop(bpy.context.window_manager.paul_manager, 'align_dist_z', text = 'Superpose')
                row.prop(bpy.context.window_manager.paul_manager, 'align_lock_z', text = 'lock Z')

                if tp_props.display_align_help:

                    box.separator() 
                                  
                    row = box.column(1)         
                    row.label("This Tool need stored edge in the target:")         
                    row.label("1. go into the editmode of the target") 
                    row.label("2. select one edge as active") 
                    row.label("3. and press Store Edge") 
                   
                    row.separator()            
                    
                    row.label("Now go into editmode of the object you want to align") 
                    row.label("1. select all mesh that needs to be align") 
                    row.label("2. select on edge as active") 
                    row.label("3. and press Align Edges")
                    
                    row.separator()            
                    
                    row.label("Superpose: edge jump to edge")                  
                    row.label("lock Z: preserve the z axis")                  

                box.separator()     



                box = col.box().column(1)              
                
                row = box.column(1) 

                button_align_planar = icons.get("icon_align_planar") 
                row.operator("mesh.face_make_planar", "Planar Faces", icon_value=button_align_planar.icon_id)   
                
                button_align_con_face = icons.get("icon_align_con_face") 
                row.operator("mesh.rot_con", "Square Rotation", icon_value=button_align_con_face.icon_id)   

                button_snap_offset = icons.get("icon_snap_offset")  
                row.operator("view3d.xoffsets_main", "Xoffset & Xrotate", icon_value=button_snap_offset.icon_id)   

                box.separator()


                box = col.box().column(1)              

                row = box.column(1) 
                row.label("Interpolate...")              
              
                row = box.column(1)    
                row.operator("mesh.wplsmthdef_apply", text="Apply Smooth Deform", icon ="SHAPEKEY_DATA")

                box.separator()





        if context.mode == 'EDIT_LATTICE':
            
                       
            col = layout.column(align=True)

            box = col.box().row()   
            
            row = box.column(1) 
            row.label("Align") 
            row.label("to..") 
            row.label("Axis") 

            row = box.column(1)

            button_align_xy = icons.get("icon_align_xy") 
            row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'

            button_align_zx = icons.get("icon_align_zx")
            row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'

            button_align_zy = icons.get("icon_align_zy") 
            row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'           

            row = box.column(1)

            button_align_x = icons.get("icon_align_x") 
            row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'

            button_align_y = icons.get("icon_align_y") 
            row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

            button_align_z = icons.get("icon_align_z") 
            row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'

            row.separator() 


            box = col.box().column(1)   

            row = box.row(1)  

            button_flip_lattice = icons.get("icon_flip_lattice")              
            row.label("Flip", icon_value=button_flip_lattice.icon_id) 
                     
            sub = row.row(1)
            sub.scale_x = 0.3 
            sub.operator("lattice.flip", text="X").axis = "U"
            sub.operator("lattice.flip", text="Y").axis = "V"
            sub.operator("lattice.flip", text="Z").axis = "W"

            box.separator()

            row = box.row(1)  

            button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
            row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
                     
            sub = row.row(1)
            sub.scale_x = 0.3           
            sub.operator("tp_ops.mirror1",text="X")
            sub.operator("tp_ops.mirror2",text="Y")
            sub.operator("tp_ops.mirror3",text="Z")            
    
            box.separator()


