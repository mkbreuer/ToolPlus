# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    

EDIT = ["EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

class draw_layout_smooth:

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type not in GEOM:
                return isModelingMode and context.mode not in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        icons = load_icons()
      
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 

        if context.mode == 'OBJECT':
            
           box = layout.box().column(1) 
            
           row = box.column(1)
           row.operator("object.shade_flat", text="Shade Flat", icon="MESH_CIRCLE")
           row.operator("object.shade_smooth", text="Shade Smooth", icon="SMOOTH")   
                  
           obj = context.active_object     
           if obj:
               obj_type = obj.type
                              
               if obj_type in {'MESH'}:
               
                    box.separator() 
                   
                    row = box.row(1) 

                    if context.active_object.data.show_double_sided == False:  
                        row.prop(context.active_object.data, "show_double_sided",icon="GHOST")        
                    else:  
                        row.prop(context.active_object.data, "show_double_sided",icon="GHOST")                    
                   
                    if context.active_object.data.use_auto_smooth == False:              
                        row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                    else:  
                        row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
                
                    row = box.row(1)
                    row.active = context.active_object.data.use_auto_smooth
                    row.prop(context.active_object.data, "auto_smooth_angle", text="AutoSmooth Angle") 
                   
                    box.separator() 
 

               else:
                   pass

           box.separator()  


        if context.mode == 'EDIT_MESH':


            box = layout.box().column(1)                   

            row = box.column(1)
            row.operator("mesh.faces_shade_flat", icon="MESH_CIRCLE") 
            row.operator("mesh.faces_shade_smooth", icon="SMOOTH") 
            
            box.separator() 
            
            row = box.row(1) 
            
            row = box.row(1) 
            if context.active_object.data.show_double_sided == False:  
                row.prop(context.active_object.data, "show_double_sided",icon="GHOST")        
            else:  
                row.prop(context.active_object.data, "show_double_sided",icon="GHOST")    
           
            if context.active_object.data.use_auto_smooth == False:              
                row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
            else:  
                row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
        
            row = box.row(1)
            row.active = context.active_object.data.use_auto_smooth
            row.prop(context.active_object.data, "auto_smooth_angle", text="AutoSmooth Angle")     

            box.separator() 


        if context.mode == 'EDIT_CURVE':
                                            
            row = box.row(1)                                
            row.operator("tp_ops.curve_shade", text="Flat", icon="MESH_CIRCLE").shade_mode='flat'
            row.operator("tp_ops.curve_shade", text="Smooth", icon="SMOOTH").shade_mode='smooth'  
            
            box.separator()
            
            row = box.row(1)  
            row.operator("curve.normals_make_consistent",text="Recalculate Normals", icon='SNAP_NORMAL')     

            box.separator() 
                                        


class VIEW3D_TP_Smooth_Panel_TOOLS(bpy.types.Panel, draw_layout_smooth):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Smooth_Panel_TOOLS"
    bl_label = "Smooth"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_Smooth_Panel_UI(bpy.types.Panel, draw_layout_smooth):
    bl_idname = "VIEW3D_TP_Smooth_Panel_UI"
    bl_label = "Smooth"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

