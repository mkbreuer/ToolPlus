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

from toolplus_transform.ntransform_menu import VIEW3D_TP_Move_Normal_Menu
from toolplus_transform.ntransform_menu import VIEW3D_TP_Resize_Normal_Menu
from toolplus_transform.ntransform_menu import VIEW3D_TP_Rotate_Normal_Menu

EDIT = ["OBJECT", "SCULPT", "EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']

class draw_ntransform_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)

#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:
#                return isModelingMode and context.mode in EDIT

        return isModelingMode

    def draw(self, context):
        tp_props = context.window_manager.tp_collapse_ntransform        
        panel_prefs = context.user_preferences.addons[__package__].preferences
 
        layout = self.layout.column(align=True)    

        icons = load_icons()
        
        col = layout.row(align=True)
   
        col = layout.row(align=True)  
        col.label("Settings")
  
        if tp_props.display_settings:            
            col.prop(tp_props, "display_settings", text="", icon="SCRIPTWIN")
        else:
            col.prop(tp_props, "display_settings", text="", icon="SCRIPTWIN")                     
      
        layout.separator() 
        
        col = layout.column(align=True)  

        if panel_prefs.tab_pivot == True:  

            box = col.box().column(align=True)  
            box.separator()               
            
            row = box.row(align=True)
            sub = row.row(align=True)
            sub.scale_x = 7
            sub.scale_y = 1.3
            sub.alignment ='CENTER'  

            sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
            sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
            sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
            sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
            sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")      
            button_snap_place = icons.get("icon_snap_place")
            sub.menu("VIEW3D_TP_SnapSet_Menu", text="", icon_value=button_snap_place.icon_id) 
            
            box.separator()   
        

         
        if panel_prefs.tab_normal == True:  

 
            if panel_prefs.tab_use_menu == True: 

                box = col.box().column(align=True)      
                box.separator()     
                              
                row = box.column(align=True) 
                row.scale_y = 1.3              
                row.menu("VIEW3D_TP_Move_Normal_Menu", text="N-Translate")
                row.menu("VIEW3D_TP_Rotate_Normal_Menu", text="N-Rotate")
                row.menu("VIEW3D_TP_Resize_Normal_Menu", text="N-Scale")
                
                if context.mode == 'EDIT_MESH':
                    row.operator("mesh.align_normal", text="N-Align")

            else:
                box = col.box().column(align=True)      
                box.separator()     
                                
                row = box.row(align=True)              
                row.scale_y = 1.3  
                row.label(text=" ", icon='MAN_TRANS')   

                props = row.operator("transform.transform", text = "X")
                props.mode = 'TRANSLATION'
                props.constraint_axis = (True, False, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 

                props = row.operator("transform.transform", text = "Y")
                props.mode = 'TRANSLATION'
                props.constraint_axis = (False, True, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 

                props = row.operator("transform.transform", text = "Z")
                props.mode = 'TRANSLATION'
                props.constraint_axis = (False, False, True)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 

                props = row.operator("transform.transform", text = "XY")
                props.constraint_axis = (True, True, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE'

                row = box.row(align=True)              
                row.scale_y = 1.3  
                row.label(text=" ", icon='MAN_ROT') 

                props = row.operator("transform.rotate", text = "X")
                props.constraint_axis = (True, False, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 

                props = row.operator("transform.rotate", text = "Y")
                props.constraint_axis = (False, True, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 
                
                props = row.operator("transform.rotate", text = "Z")
                props.constraint_axis = (False, False, True)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE'       
           
                props = row.operator("transform.rotate", text = "XY")
                props.constraint_axis = (True, True, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE'

                row = box.row(align=True)              
                row.scale_y = 1.3  
                row.label(text=" ", icon='MAN_SCALE')  

                props = row.operator("transform.resize", text = "X")
                props.constraint_axis = (True, False, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 

                props = row.operator("transform.resize", text = "Y")
                props.constraint_axis = (False, True, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE' 
                
                props = row.operator("transform.resize", text = "Z")
                props.constraint_axis = (False, False, True)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE'                  

                props = row.operator("transform.resize", text = "XY")
                props.constraint_axis = (True, True, False)
                props.constraint_orientation = 'NORMAL'
                props.snap_target = 'ACTIVE'
                            
            box.separator()    



        # ALIGN TO #
        if panel_prefs.tab_align == True:  

             button_align_x = icons.get("icon_align_x") 
             button_align_y = icons.get("icon_align_y")                     
             button_align_z = icons.get("icon_align_z")                  
             button_align_xy = icons.get("icon_align_xy") 
             button_align_zx = icons.get("icon_align_zx")
             button_align_zy = icons.get("icon_align_zy")                   
             button_align_to_normal = icons.get("icon_align_to_normal")  
             button_apply = icons.get("icon_apply") 


             # OBJECT #     
             if context.mode == 'OBJECT':

                box = col.box().column(align=True)      
                box.separator()  

                if panel_prefs.tn_align_to == "location":                  

                    row = box.row()
                    row.scale_y = 1.3   

                    props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_TRANS')   
                    props.tp_axis='axis_xyz'
                    props.tp_transform='LOCATION' 
                                             
                    props = row.operator("tp_ops.align_transform",text="X", icon_value=button_align_x.icon_id)
                    props.tp_axis='axis_x'
                    props.tp_transform='LOCATION'

                    button_align_xy = icons.get("icon_align_xy") 
                    props = row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
                    props.tp_axis= 'axis_xy'         
                    props.tp_transform= 'LOCATION'       

                    row = box.row()
                    row.scale_y = 1.3   
                    
                    row.operator("object.location_clear", text= " ", icon="PANEL_CLOSE")
                                        
                    props = row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id)
                    props.tp_axis='axis_y'
                    props.tp_transform='LOCATION' 
                 
                    button_align_zy = icons.get("icon_align_zy") 
                    props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
                    props.tp_axis= 'axis_zy'         
                    props.tp_transform= 'LOCATION'    

                    row = box.row()
                    row.scale_y = 1.3   
                    
                    props = row.operator("object.transform_apply", text=" ", icon_value=button_apply.icon_id)
                    props.location= True
                    props.rotation= False
                    props.scale= False
                    
                    props = row.operator("tp_ops.align_transform",text="Z", icon_value=button_align_z.icon_id)
                    props.tp_axis='axis_z'
                    props.tp_transform='LOCATION'

                    button_align_zx = icons.get("icon_align_zx")
                    props = row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
                    props.tp_axis= 'axis_zx'         
                    props.tp_transform= 'LOCATION'    
                   

                if panel_prefs.tn_align_to == "rotation": 

                    row = box.row()
                    row.scale_y = 1.3   

                    props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_ROT') 
                    props.tp_axis='axis_xyz'
                    props.tp_transform='ROTATION'
                    
                    props = row.operator("tp_ops.align_transform",text="X", icon_value=button_align_x.icon_id)
                    props.tp_axis='axis_x'
                    props.tp_transform='ROTATION'

                    button_align_xy = icons.get("icon_align_xy") 
                    props = row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
                    props.tp_axis= 'axis_xy'         
                    props.tp_transform= 'ROTATION'    

                    row = box.row()
                    row.scale_y = 1.3   

                    row.operator("object.rotation_clear", text=" ", icon="PANEL_CLOSE")
                    
                    props = row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id)
                    props.tp_axis='axis_y'
                    props.tp_transform='ROTATION'

                    button_align_zy = icons.get("icon_align_zy") 
                    props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
                    props.tp_axis= 'axis_zy'         
                    props.tp_transform= 'ROTATION'     

                    row = box.row()
                    row.scale_y = 1.3   

                    props = row.operator("object.transform_apply", text=" ", icon_value=button_apply.icon_id)
                    props.location= False
                    props.rotation= True
                    props.scale= False     
                    
                    props = row.operator("tp_ops.align_transform",text="Z", icon_value=button_align_z.icon_id)
                    props.tp_axis='axis_z'
                    props.tp_transform='ROTATION'

                    button_align_zx = icons.get("icon_align_zx")
                    props = row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
                    props.tp_axis= 'axis_zx'         
                    props.tp_transform= 'ROTATION'    
                    


                if panel_prefs.tn_align_to == "scale": 
                    
                    row = box.row()
                    row.scale_y = 1.3   
               
                    props = row.operator("tp_ops.align_transform",text=" ", icon='MAN_SCALE')  
                    props.tp_axis='axis_xyz'
                    props.tp_transform='SCALE'

                    props = row.operator("tp_ops.align_transform",text="X", icon_value=button_align_x.icon_id)
                    props.tp_axis='axis_x'
                    props.tp_transform='SCALE'

                    button_align_xy = icons.get("icon_align_xy") 
                    props = row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id)
                    props.tp_axis= 'axis_xy'         
                    props.tp_transform= 'SCALE'  

                    row = box.row()
                    row.scale_y = 1.3   

                    row.operator("object.scale_clear", text=" ", icon="PANEL_CLOSE")
                    
                    props = row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id)
                    props.tp_axis='axis_y'
                    props.tp_transform='SCALE'

                    button_align_zy = icons.get("icon_align_zy") 
                    props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
                    props.tp_axis= 'axis_zy'         
                    props.tp_transform= 'SCALE'   

                    row = box.row()
                    row.scale_y = 1.3   

                    props = row.operator("object.transform_apply", text=" ", icon_value=button_apply.icon_id)
                    props.location= False
                    props.rotation= False
                    props.scale= True  
                        
                    props = row.operator("tp_ops.align_transform",text="Z", icon_value=button_align_z.icon_id)
                    props.tp_axis='axis_z'
                    props.tp_transform='SCALE'

                    button_align_zx = icons.get("icon_align_zx")
                    props = row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id)
                    props.tp_axis= 'axis_zx'         
                    props.tp_transform= 'SCALE'    


                box.separator()  
                
                row = box.row(align=True)
                row.scale_y = 1.3                                                 
                row.prop(panel_prefs, 'tn_align_to', text="") 
               
                box.separator()        


             else:
    
                box = col.box().column(align=True)      
                box.separator()                            
                
                row = box.row()
                row.scale_y = 1.3          
                row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'            
                row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'
                
                row = box.row()
                row.scale_y = 1.3              
                row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'    
                row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           
                
                row = box.row()
                row.scale_y = 1.3  
                row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'            
                row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'        


                box.separator()    
               
                # MESH #     
                if context.mode == 'EDIT_MESH':   
                                  
                    row = box.row(align=True)
                    row.scale_y = 1.3  
                
                    props = row.operator("tp_ops.align_transform", "Normal", icon_value=button_align_to_normal.icon_id)                
                    props.tp_axis='axis_z'
                    props.tp_orient='NORMAL'

                    box.separator()    




        if tp_props.display_settings:  

            box = col.box().column(align=True)
             
            box.separator() 

            row = box.row(align=True) 
            row.label( text="Panel Layout", icon ="COLLAPSEMENU")    
            row.operator("tp_ops.help_curve_prefs", text="", icon='INFO')  
            
            box.separator()            
            
            row = box.column(align=True)
            row.prop(panel_prefs, 'tab_location', expand=True)

            box.separator()

            row = box.row(align=True)            
            if panel_prefs.tab_location == 'tools':              
                row.prop(panel_prefs, "tools_category")
                  
            box.separator()            
          
            row = box.row(align=True)             
            row.prop(panel_prefs, 'tab_pivot')
            row.prop(panel_prefs, 'tab_transform')

            row = box.row(align=True)       
            row.prop(panel_prefs, 'tab_align')

            row = box.row(align=True)   
            row.prop(panel_prefs, 'tab_normal')           
            if panel_prefs.tab_normal == True:            
                row.prop(panel_prefs, 'tab_use_menu')

           
            box.separator()        
            box = col.box().column(align=True)                       
            box.separator() 
           
            row = box.row(align=True) 
            row.label("Append to Transform Panel", icon ="COLLAPSEMENU")
            
            row = box.row(align=True)
            row.prop(panel_prefs, 'tab_submenu_ntransform', expand=True)

            box.separator()        
            box = col.box().column(align=True)                       
            box.separator() 
             
            row = box.row(1)  
            row.label("Menu [CTRL+SHIFT+X]", icon ="COLLAPSEMENU") 
           
            row = box.row(1)           
            row.prop(panel_prefs, 'tab_menu_ntransform', expand=True)

            box.separator() 
             
            row = box.row(1)            
            row.operator("tp_ops.keymap_ntransform", text = 'Open KeyMap')
            row.operator('wm.url_open', text = 'Type of Events').url = "https://lh3.googleusercontent.com/zfNKbUKpnvLTPADu4btQI_adXhkR9iPiSyy31ZvP89YNK6YSiLf4iVC3lpzN76DTdEdHHIZqZK6qM2OYRSAeFRlIof5xHC0wLQtOaCwYEKi43A6W9KGkGAwnlNGqUugQdleEHTMLZnL67u4m6kU1KTKlFASfyDuFCCvdyGGaa5-gZ9kib1AiJ_2exgWvRh1yM86PehsJH65Zp0r6x5zhqZpLI1IS9K-zlyvaKg_WgYuVMzvsd3JrB2BAo-BIZGX9MFA8t-CC3qVtTLXH8WAkHo9IyA1u7GnlCM5p9wffwpu1NhCsZTuQwPnn0BGmOCD0tPCm_LJSJSDyCtkfBXvK_hdsQ3XM0Jcttl1oHJKYqbPoIjHMaLl7pNGmwMhcjlgPqXMq01Eln0wm6NHbJyTe5WMBN7FaB0WEaot7V9TsFxACRJzD2dJu-zP7xJ_vw6sMlYcXLf962SkzRShIMTJiBzSxui5sRJ1uKPCehcdP4E3pEc1tIFO1dQZTSwrLf9luz1S79zCflUCgJFWa8GfN4KGWG09mO4jUBJIdtobsDeM_NPyvraz6Lq4OTz90zgQQ1cxTzQ49MzYcIesnrw7TE2Ilr7UTkOpuoxL4rPw=w696-h1278-no"            

            box.separator() 

            row = box.row(align=True)   
            row.prop(panel_prefs, 'tab_normal_menu')   
            
            box.separator()        
            box = col.box().column(align=True)                       
            box.separator() 
             
            row = box.row(align=True)        
            wm = context.window_manager    
            row.operator("wm.save_userpref", icon='FILE_TICK')  

            box.separator()   



class VIEW3D_TP_Transform_Panel_TOOLS(bpy.types.Panel, draw_ntransform_panel_layout):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Transform_Panel_TOOLS"
    bl_label = "Transform+"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_Transform_Panel_UI(bpy.types.Panel, draw_ntransform_panel_layout):
    bl_idname = "VIEW3D_TP_Transform_Panel_UI"
    bl_label = "Transform+"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
