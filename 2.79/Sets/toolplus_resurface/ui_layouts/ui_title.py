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


def draw_title_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        
        icons = load_icons()

        col = layout.column(align=True)

        box = col.box().column(1) 

        row = box.row(1)         

        obj = context.active_object     
        if obj:
           obj_type = obj.type
                                                         

           if obj_type in {'MESH'}:
                 
               if obj.mode in {'EDIT'}:
                   #a="Toggle to Object mode"
                   ico="OUTLINER_DATA_MESH"
               else:
                   #a="Toggle to Edit mode"
                   ico="OUTLINER_OB_MESH"
           
               if context.mode == "SCULPT":   

                   row = box.row(1)         

                   if tp_props.display_title:                       
                        row.prop(tp_props, "display_title", text="", icon = "VIEWZOOM", emboss = False)                           
                   else:            
                        row.prop(tp_props, "display_title", text="", icon = "VIEWZOOM", emboss = False)   
                        
                   row.prop(context.object , "name", text="")

               else:
                   
                   row = box.row(1)         
                   row.alignment = "CENTER"  
                   
                   if tp_props.display_title:                       
                        row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
                   else:            
                        row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                      
                   
                   row.label("MESH") 


        
           row = box.row(1)                    
           row.alignment = "CENTER" 
           
           if obj_type in {'LATTICE'}:
            
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_LATTICE"
               else:
                   ico="OUTLINER_OB_LATTICE"                

               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)    
           
               row.label("LATTICE") 


           if obj_type in {'CURVE'}:
             
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_CURVE"
               else:
                   ico="OUTLINER_OB_CURVE"                     
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)    
           
               row.label("CURVE")               

               
           if obj_type in {'SURFACE'}:
              
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_SURFACE"
               else:
                   ico="OUTLINER_OB_SURFACE"                    
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)    
           
               row.label("SURFACE")                 
               

           if obj_type in {'META'}:
            
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_META"
               else:
                   ico="OUTLINER_OB_META"                    
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("META")                 

               
           if obj_type in {'FONT'}:
              
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_FONT"
               else:
                   ico="OUTLINER_OB_FONT"                     
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("FONT")  
                                              

           if obj_type in {'ARMATURE'}:
               
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_ARMATURE"
               else:
                   ico="OUTLINER_OB_ARMATURE"                     
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("ARMATURE") 


           if obj_type in {'EMPTY'}:

               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_EMPTY"
               else:
                   ico="OUTLINER_OB_EMPTY"                       
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("EMPTY") 


           if obj_type in {'CAMERA'}:
           
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_CAMERA"
               else:
                   ico="OUTLINER_OB_CAMERA"                   
              
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("CAMERA") 


           if obj_type in {'LAMP'}:
              
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_LAMP"
               else:
                   ico="OUTLINER_OB_LAMP"                     
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("LAMP") 


           if obj_type in {'SPEAKER'}:
              
               if obj.mode in {'EDIT'}:
                   ico="OUTLINER_DATA_SPEAKER"
               else:
                   ico="OUTLINER_OB_SPEAKER"                    
               
               if tp_props.display_title:                       
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False)                           
               else:            
                    row.prop(tp_props, "display_title", text="", icon = ico, emboss = False) 

               row.label("SPEAKER") 


        else:
            row.alignment = "CENTER"              
            row.label("???") 
                





        if tp_props.display_title:   
           
            box = col.box().column(1)       

            row = box.row(1)                 
            row.prop(context.object , "name", text="Name", icon = "COPY_ID") 
            row.operator("tp_ops.copy_name_to_meshdata", text= "", icon ="PASTEDOWN")

            row = box.row(1)      
            row.prop(context.object.data , "name", text="Data", icon = "OUTLINER_DATA_MESH") 
            row.operator("tp_ops.copy_data_name_to_object", text= "", icon ="COPYDOWN")


        
