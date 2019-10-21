# ##### BEGIN GPL LICENSE BLOCK #####
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

from .. ops_curve.curve_convert import *


def draw_convert_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        

        icons = load_icons()
        
        layout.operator_context = 'INVOKE_REGION_WIN'

        obj = context.active_object     
        if obj:
           obj_type = obj.type

           if obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}:  

                col = layout.column(align=True)


                icons = load_icons()
                         
                if context.mode in {"OBJECT"}:

                    obj = context.active_object     
                    if obj:
                       obj_type = obj.type
                           
                       box = col.box().column(1)                    
                        
                       row = box.row(1)
                       if tp_props.display_convert:  
                            row.prop(tp_props, "display_convert", text="", icon="TRIA_DOWN", emboss = False)                
                       else:
                            row.prop(tp_props, "display_convert", text="", icon="TRIA_RIGHT", emboss = False)            

                       if obj_type in {'MESH'}:
                                   
                           row.label("Convert Curve:")    

                           #button_convert_to_curve = icons.get("icon_convert_to_curve") 
                           #row.operator("object.convert",text="", icon_value=button_convert_to_curve.icon_id).target="CURVE"   
                           row.operator("object.convert",text="", icon="MOD_CURVE").target='CURVE'             
                     
                       if obj_type in {'CURVE', 'SURFACE', 'META', 'FONT'}:                                       
                                   
                           row.label("Convert Mesh:")

                           obj = context.active_object     
                           if obj and bpy.context.object.data.dimensions == '2D':                   
                                row.operator("tp_ops.convert_mesh",text="", icon = "MOD_REMESH")
                           else:
                                pass       
                           
                           #button_convert_to_mesh = icons.get("icon_convert_to_mesh") 
                           #row.operator("object.convert",text="", icon_value=button_convert_to_mesh.icon_id).target="MESH"                              
                           row.operator("object.convert",text="", icon = "MOD_SOLIDIFY").target="MESH"     


                       if tp_props.display_convert:  

                                                      
                           if obj_type in {'CURVE'}: 
                               
                               box.separator() 
                               box.separator() 

                               row = box.row(1)             
                               
                               active_convert = bpy.context.scene.tp_curve_convert_toogle  
                               if active_convert == True:                           
                                    row.prop(context.scene, "tp_curve_convert_toogle", text="", icon ="MESH_DATA")
                               else:        
                                    row.prop(context.scene, "tp_curve_convert_toogle", text="", icon ="OUTLINER_DATA_CURVE")        
                               
                               row.operator("tp_ops.convert_to_merged_mesh", text="Merge").mode ='MERGED'
                               row.operator("tp_ops.convert_to_merged_mesh", text="Isolate").mode ='SEPARATE'

                               if active_convert == True:

                                   box.separator() 

                                   row = box.row(1)   
 
                                   try_dissolve = bpy.context.scene.tp_try_dissolve_toogle  
                                   if try_dissolve == True:                           
                                        row.prop(context.scene, "tp_try_dissolve_toogle", text="", icon ="PROP_CON")
                                   else:        
                                        row.prop(context.scene, "tp_try_dissolve_toogle", text="", icon ="PROP_ON")     

                                   row.operator("tp_ops.convert_to_merged_mesh", text="Union").mode ='UNION'
                                   row.label(" ")

                               box.separator() 
                               box.separator() 



                           box = col.box().column(1)
                          
                           row = box.row(1)                    
                           row.label("Convert-Non-Destructive") 

                           box.separator() 
                          
                           row = box.row(1)                            
                           row.label("CurveName:")
                           
                           if "," in obj.names:
                                li = obj.names.split(",")
                                del li[len(li) - 1]
                                for i in li:
                                    row.label(i)
                           else:
                                row.prop_search(obj, "names", context.scene, "objects")
                               
                                row = box.row(1)
                                row.prop(obj, "rscale", "Copy Scale")

                           sub = row.row(1)
                           sub.scale_x = 1.1             
                           sub.operator("mesh.curve_convert_update", icon="FILE_REFRESH")
                       
                           box.separator() 


                           if obj_type in {'CURVE'}: 
                                
                               if len(context.selected_objects) > 1:
                                                       
                                    row = box.row(1) 
                                    row.operator("mesh.curve_convert_add_multiple", icon="GROUP")

                                    box.separator() 
                                
                               else:                         
                                    row = box.row(1) 
                                    row.operator("mesh.curve_convert_add", icon="MESH_CUBE")                               
                                    
                                    box.separator() 



                       
                       
                       
                       
                       

        if context.mode in {"EDIT_CURVE"}:

            col = layout.column(align=True)

            box = col.box().column(1) 
         
            row = box.column(1) 
            
            if len(context.selected_objects) > 1:
                pass
            else:
                row.operator("mesh.curve_convert_add", icon="MESH_CUBE")    
            
            row.operator("mesh.curve_convert_update_all", icon="FILE_REFRESH")

            box.separator() 
