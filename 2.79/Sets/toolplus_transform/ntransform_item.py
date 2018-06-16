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

def transform_pivot_draw(self,context):
    panel_prefs = context.user_preferences.addons[__package__].preferences
    icons = load_icons()
    
    layout = self.layout.column(align=True)

    col = layout.column(align=True)

    if panel_prefs.tab_pivot == True:   
        
        row = col.row(align=True)
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


def transform_tools_draw(self,context):
    panel_prefs = context.user_preferences.addons[__package__].preferences
    icons = load_icons()
    
    layout = self.layout.column(align=True)

    col = layout.column(align=True)

    if panel_prefs.tab_transform == True: 

        col.operator("transform.tosphere", text="To Sphere")
        col.operator("transform.shear", text="Shear")
        col.operator("transform.bend", text="Bend")

        col.separator()            

    if panel_prefs.tab_normal == True:
         
        if panel_prefs.tab_use_menu == True: 

            col.menu("VIEW3D_TP_Move_Normal_Menu", text="N-Translate")
            col.menu("VIEW3D_TP_Rotate_Normal_Menu", text="N-Rotate")
            col.menu("VIEW3D_TP_Resize_Normal_Menu", text="N-Scale")

        else:
            
            row = col.row(align=True)  
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

            row = col.row(align=True)
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
     
            row = col.row(align=True)
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
            

        col.separator()    

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

            col = layout.column(align=True)      
                                   
            if panel_prefs.tn_align_to == "location":                  

                row = col.row()
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

                row = col.row()
                row.scale_y = 1.3   
                
                row.operator("object.location_clear", text= " ", icon="PANEL_CLOSE")
                                    
                props = row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id)
                props.tp_axis='axis_y'
                props.tp_transform='LOCATION' 
             
                button_align_zy = icons.get("icon_align_zy") 
                props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
                props.tp_axis= 'axis_zy'         
                props.tp_transform= 'LOCATION'    

                row = col.row()
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

                row = col.row()
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

                row = col.row()
                row.scale_y = 1.3   

                row.operator("object.rotation_clear", text=" ", icon="PANEL_CLOSE")
                
                props = row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id)
                props.tp_axis='axis_y'
                props.tp_transform='ROTATION'

                button_align_zy = icons.get("icon_align_zy") 
                props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
                props.tp_axis= 'axis_zy'         
                props.tp_transform= 'ROTATION'     

                row = col.row()
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
                
                row = col.row()
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

                row = col.row()
                row.scale_y = 1.3   

                row.operator("object.scale_clear", text=" ", icon="PANEL_CLOSE")
                
                props = row.operator("tp_ops.align_transform",text="Y", icon_value=button_align_y.icon_id)
                props.tp_axis='axis_y'
                props.tp_transform='SCALE'

                button_align_zy = icons.get("icon_align_zy") 
                props = row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id)
                props.tp_axis= 'axis_zy'         
                props.tp_transform= 'SCALE'   

                row = col.row()
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


            col.separator()  
            
            row = col.row(align=True)
            row.scale_y = 1.3                                                 
            row.prop(panel_prefs, 'tn_align_to', text="") 
           
            col.separator()        


         else:

            col = layout.column(align=True)                   
            
            row = col.row()
            row.scale_y = 1.3          
            row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'            
            row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'
            
            row = col.row()
            row.scale_y = 1.3              
            row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'    
            row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           
            
            row = col.row()
            row.scale_y = 1.3  
            row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'            
            row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'

            col.separator()    
           
            # MESH #     
            if context.mode == 'EDIT_MESH':   
                              
                row = col.row()
                row.scale_y = 1.3  
            
                props = row.operator("tp_ops.align_transform", "Normal", icon_value=button_align_to_normal.icon_id)                
                props.tp_axis='axis_z'
                props.tp_orient='NORMAL'

                col.separator()    




# UI: TRANSFORM SUB MENU # 
def update_submenu_ntransform(self, context):

    try:                
        bpy.types.VIEW3D_PT_tools_transform.remove(transform_pivot_draw)
        bpy.types.VIEW3D_PT_tools_transform_mesh.remove(transform_pivot_draw)
        bpy.types.VIEW3D_PT_tools_transform_curve.remove(transform_pivot_draw)
        bpy.types.VIEW3D_PT_tools_transform_surface.remove(transform_pivot_draw)
        bpy.types.VIEW3D_PT_tools_mballedit.remove(transform_pivot_draw)
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.remove(transform_pivot_draw)
        bpy.types.VIEW3D_PT_tools_latticeedit.remove(transform_pivot_draw)
        bpy.types.VIEW3D_MT_transform.remove(transform_pivot_draw)                

        bpy.types.VIEW3D_PT_tools_transform.remove(transform_tools_draw)
        bpy.types.VIEW3D_PT_tools_transform_mesh.remove(transform_tools_draw)
        bpy.types.VIEW3D_PT_tools_transform_curve.remove(transform_tools_draw)
        bpy.types.VIEW3D_PT_tools_transform_surface.remove(transform_tools_draw)
        bpy.types.VIEW3D_PT_tools_mballedit.remove(transform_tools_draw)
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.remove(transform_tools_draw)
        bpy.types.VIEW3D_PT_tools_latticeedit.remove(transform_tools_draw)
        bpy.types.VIEW3D_MT_transform.remove(transform_tools_draw) 

    except:
        pass

    if context.user_preferences.addons[__package__].preferences.tab_submenu_ntransform == 'insert':

        bpy.types.VIEW3D_PT_tools_transform.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_PT_tools_transform_mesh.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_PT_tools_transform_curve.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_PT_tools_transform_surface.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_PT_tools_mballedit.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_PT_tools_latticeedit.prepend(transform_pivot_draw)    
        bpy.types.VIEW3D_MT_transform.prepend(transform_pivot_draw)  


        bpy.types.VIEW3D_PT_tools_transform.append(transform_tools_draw)    
        bpy.types.VIEW3D_PT_tools_transform_mesh.append(transform_tools_draw)    
        bpy.types.VIEW3D_PT_tools_transform_curve.append(transform_tools_draw)    
        bpy.types.VIEW3D_PT_tools_transform_surface.append(transform_tools_draw)    
        bpy.types.VIEW3D_PT_tools_mballedit.append(transform_tools_draw)    
        bpy.types.VIEW3D_PT_tools_armatureedit_transform.append(transform_tools_draw)    
        bpy.types.VIEW3D_PT_tools_latticeedit.append(transform_tools_draw)    
        bpy.types.VIEW3D_MT_transform.prepend(transform_tools_draw)  

    if context.user_preferences.addons[__package__].preferences.tab_submenu_ntransform == 'remove':
        pass



## PROPERTIES: TAB OBJECT #
#def submenu_func_object(self, context):


