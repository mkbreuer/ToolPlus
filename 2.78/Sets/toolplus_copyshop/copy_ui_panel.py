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
__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



def draw_copy_panel_layout(self, context, layout):
        
        tp_props = context.window_manager.tp_collapse_copyshop_props
        
        icons = load_icons()


        display_title = context.user_preferences.addons[__package__].preferences.tab_title
        if display_title == 'on':
         
            obj = context.active_object     
            if obj:
               obj_type = obj.type
                              
               if obj_type in {'MESH'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("MESH") 
                                      
               if obj_type in {'LATTICE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("LATTICE") 

               if obj_type in {'CURVE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("CURVE")               
                   
               if obj_type in {'SURFACE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("SURFACE")                 
                   
               if obj_type in {'META'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("MBall")                 
                   
               if obj_type in {'FONT'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("FONT")  
                                                  
               if obj_type in {'ARMATURE'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("ARMATURE") 

               if obj_type in {'EMPTY'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("EMPTY") 

               if obj_type in {'CAMERA'}:
                  box = layout.box()
                  row = box.row(1)                                        
                  row.alignment = "CENTER"
                  row.label("CAMERA") 

               if obj_type in {'LAMP'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("LAMP") 

               if obj_type in {'SPEAKER'}:
                   box = layout.box()
                   row = box.row(1)                                        
                   row.alignment = "CENTER"
                   row.label("SPEAKER") 



        display_pivot = context.user_preferences.addons[__package__].preferences.tab_pivot
        if display_pivot == 'on':

            box = layout.box()
            
            row = box.row(1)  
            sub = row.row(1)
            sub.scale_x = 7

            sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
            sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
            sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
            sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
            sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")             


        if context.mode == 'OBJECT':


            display_duplicate = context.user_preferences.addons[__package__].preferences.tab_duplicate
            if display_duplicate == 'on':  
  
                box = layout.box().column(1)
                 
                row = box.row(1)
                row.operator("object.duplicate_move", text="Copy", icon="MOD_BOOLEAN")
                row.operator("object.duplicate_move_linked", text="Link-Copy", icon="CONSTRAINT_DATA")            
                          
                box.separator()  



            display_radial = context.user_preferences.addons[__package__].preferences.tab_radial
            if display_radial == 'on':  

                box = layout.box().column(1) 
                 
                row = box.row(1)
                
                display_Dynamics = context.user_preferences.addons[__package__].preferences.tab_dynamics
                if display_Dynamics == 'on':          
                    row.operator("mft.radialclone", text="", icon="FILE_REFRESH")
                else:
                    pass    
                row.operator("mft.radialclone_panel", text="Radial Z-Axis Clone", icon="BLANK1")

                row = box.row(1) 
                row.prop(context.scene, "radialClonesAngle", text="")
                row.prop(context.scene, "clonez", text="")

                box.separator()  
                        


            display_copy_to_mesh = context.user_preferences.addons[__package__].preferences.tab_copy_to_mesh
            if display_copy_to_mesh == 'on':  

                box = layout.box().column(1)
                 
                row = box.row(1)
                if tp_props.display_copy_to_faces:
                    row.prop(tp_props, "display_copy_to_faces", text="", icon='TRIA_DOWN')
                    row.operator("tp_ops.copy_to_mesh_panel", text="Copy from Source", icon='BLANK1') 
                else:
                    row.prop(tp_props, "display_copy_to_faces", text="", icon='TRIA_RIGHT')
                    row.operator("tp_ops.copy_to_mesh", text="Copy to Mesh", icon='BLANK1') 

     
                if tp_props.display_copy_to_faces:
                    scene = bpy.context.scene
                    
                    box = layout.box().column(1)
                    
                    row = box.row(1)            
                    row.label("Target:") 
     
                    sub = row.row(1)
                    sub.scale_x = 1.55               
                    sub.prop(scene, 'copytype', expand=True)
                    
                    box.separator() 
                    
                    row = box.row(1)                
                    row.label("1st Axis:")
                   
                    sub1 = row.row(1)
                    sub1.scale_x = 1                    
                    sub1.prop(scene, 'priaxes', expand=True)
                    
                    box.separator() 
                               
                    row = box.row(1)                
                    row.label("2nd Axis:") 
      
                    sub2 = row.row(1)
                    sub2.scale_x = 1     
                    sub2.prop(scene, 'secaxes', expand=True)
              
                    box.separator()     
              
                    row = box.row(1)                 
                    if scene.copytype == 'E':
                        row.prop(scene, 'edgescale')
                        
                        if scene.edgescale:
                           row = box.row(1) 
                           row.prop(scene, 'scale')           


                    if len(bpy.context.selected_objects) == 2:

                        box = layout.box().column(1)
                       
                        row = box.column(1)                                
                        row.label("! Source & Target Mesh !")                      
                     
                        box.separator() 
                                     
                        row = box.row(1)            
                        row.label("Origin to:")       
                        
                        row = box.row(1) 
                        row.prop(context.scene, "pl_set_plus_z")       
                        row.prop(context.scene, "pl_set_minus_z")  
                        
                        box.separator() 
                        
                        row = box.row(1)            
                        row.label("Relations:")

                        row = box.row(1)                                           
                        row.prop(context.scene, "pl_dupli_unlinked", text = "Unlinked")
                        row.prop(context.scene, "pl_join", text = "Join")

                        box.separator() 
                        
                        row = box.row(1)            
                        row.label("Editmode:")     
                        
                        row = box.row(1) 
                        row.prop(context.scene, "pl_set_edit_target", text = "Target")                           
                        row.prop(context.scene, "pl_set_edit_source", text = "Source")
                    
                    else:
                        pass                       
                
                box.separator()            


            display_dupli = context.user_preferences.addons[__package__].preferences.tab_dupli 
            if display_dupli == 'on':     

                obj = context.active_object     
                if obj:
                    obj_type = obj.type
                                                                          
                    if obj_type in {'MESH'}:

                        box = layout.box().column(1)
                        
                        row = box.row(1)
                        row.operator("tp_ops.dupli_set_panel", "Duplication to Active", icon = "CONSTRAINT_DATA") 

                        box.separator()
                                    
                        row = box.row(1)
                        row.prop(context.object, "dupli_type", expand=True)            

                        box.separator()
                                   
                        if context.object.dupli_type == 'FRAMES':
                            row = box.row(1)   
                            row.prop(context.object, "dupli_frames_start", text="Start")
                            row.prop(context.object, "dupli_frames_end", text="End")

                            row = box.row(1)                           
                            row.prop(context.object, "dupli_frames_on", text="On")
                            row.prop(context.object, "dupli_frames_off", text="Off")

                            row = box.row(1)   
                            row.prop(context.object, "use_dupli_frames_speed", text="Speed")

                        elif context.object.dupli_type == 'VERTS':
                            row = box.row(1)   
                            row.prop(context.object, "use_dupli_vertices_rotation", text="Rotation")

                        elif context.object.dupli_type == 'FACES':
                            row = box.row(1)                       
                            row.prop(context.object, "use_dupli_faces_scale", text="Scale")
                           
                            sub = row.row()
                            sub.active = context.object.use_dupli_faces_scale
                            sub.prop(context.object, "dupli_faces_scale", text="Inherit Scale")

                        elif context.object.dupli_type == 'GROUP':
                            row = box.row(1)
                            row.prop(context.object, "dupli_group", text="Group")

                        row = box.row(1)
                        row.prop(context.scene, "dupli_align", text="Align")
                        row.prop(context.scene, "dupli_single", text="Single")
                        
                        if context.scene.dupli_single == True:
                            
                            row = box.row(1)            
                            row.prop(context.scene, "dupli_separate", text="Separate")
                            row.prop(context.scene, "dupli_link", text="As Instance")


                box.separator()  


            display_cursor = context.user_preferences.addons[__package__].preferences.tab_cursor
            if display_cursor == 'on':  

                box = layout.box().column(1) 
                 
                row = box.row(1)                     

                display_Dynamics = context.user_preferences.addons[__package__].preferences.tab_dynamics
                if display_Dynamics == 'on':
                    row.operator("tp_ops.copy_to_cursor", text="", icon="NEXT_KEYFRAME")
                else:
                    pass    
                                         
                row.operator("tp_ops.copy_to_cursor_panel", text="Copy to Cursor", icon="BLANK1")                     
                
                row = box.row(1)  
                row.prop(context.scene, "ctc_total", text="How many?")
                                       
                box.separator() 


            display_arewo = context.user_preferences.addons[__package__].preferences.tab_arewo 
            if display_arewo == 'on':     

                box = layout.box().column(1) 
                 
                row = box.row(1)  
                row.operator("object.simplearewo", text="ARewO Replicator", icon="FRAME_NEXT")   
              
                box.separator()   


            display_array = context.user_preferences.addons[__package__].preferences.tab_array
            if display_array == 'on':

                box = layout.box().column(1) 
                 
                row = box.row(1)  
                
                if tp_props.display_array_tools:
                    row.prop(tp_props, "display_array_tools", text="Array Tools", icon='RESTRICT_VIEW_OFF')
                else:
                    row.prop(tp_props, "display_array_tools", text="Array Tools", icon='RESTRICT_VIEW_ON')  

                if tp_props.display_array_tools:
                   
                    box = layout.box().column(1) 

                    row = box.row(1) 
                    if tp_props.display_axis_array:
                        row.prop(tp_props, "display_axis_array", text="", icon='TRIA_DOWN')
                    else:
                        row.prop(tp_props, "display_axis_array", text="", icon='TRIA_RIGHT')   
                                      
                    row.operator("tp_ops.x_array", text="X Array")    
                    row.operator("tp_ops.y_array", text="Y Array")    
                    row.operator("tp_ops.z_array", text="Z Array")      

                    if tp_props.display_axis_array:
                                            
                        mod_types = []
                        append = mod_types.append

                        obj = context.active_object     
                        if obj:
                            if obj.modifiers:
                                  
                                box = layout.box().column(1)                 
                                
                                row = box.row(1)
                                row.operator("object.transform_apply", text="Applied Scale?", icon="OUTLINER_DATA_EMPTY").scale=True
                                row.operator("tp_ops.expand_mod","" ,icon = 'TRIA_DOWN')  
                                row.operator("tp_ops.collapse_mod", "" ,icon = 'TRIA_UP') 

                                row = box.row(1) 
                                row.operator("tp_ops.modifier_off","" ,icon = 'VISIBLE_IPO_OFF')  
                                row.operator("tp_ops.modifier_on", "" ,icon = 'RESTRICT_VIEW_OFF') 
                                row.operator("tp_ops.remove_mod", text="" , icon='X') 
                                row.operator("tp_ops.apply_mod", text="" , icon='FILE_TICK') 
                   
                                box.separator()
                                
                                for mod in context.active_object.modifiers:

                                    row = box.row(1)

                                    if mod.show_expanded == True:
                                        if mod.type == 'ARRAY':
                                            append(mod.type)                                       
                                            
                                            box = layout.box().column(1)
                                            
                                            row = box.row(1)                                        
                                            row.label(mod.name)
                                            
                                            if mod.fit_type == 'FIXED_COUNT':
                                                row.prop(mod, "count", text = "")                    

                                            box.separator()
                                            
                                            row = box.row(1)
                                            row.prop(mod, "relative_offset_displace", text="")

                                            box.separator()
                                            
                                            row = box.row(1)
                                            row.prop(mod, "use_merge_vertices", text="Merge")
                                            row.prop(mod, "use_merge_vertices_cap", text="First Last")
                                            
                                            row = box.row(1)
                                            row.prop(mod, "merge_threshold", text="Distance")

                                    else:
                                        box.separator()  
                            
                            else:
                                box = layout.box().column(1) 
                                
                                row = box.row(1)
                                row.operator("tp_help.axis_array", text = "! no array active !", icon ="INFO")  
                                    
                        else:
                            box = layout.box().column(1) 
                            
                            row = box.row(1)
                            row.operator("tp_help.axis_array", text = "! no array active !", icon ="INFO") 
                            ###                           

                                      
                    box.separator()
                                      
                    box = layout.box().column(1) 

                    row = box.row(1) 
                    if tp_props.display_empty:
                        row.prop(tp_props, "display_empty", text="", icon='TRIA_DOWN')
                    else:
                        row.prop(tp_props, "display_empty", text="", icon='TRIA_RIGHT')                  
                    
                    row.operator("tp_ops.add_empty_array_mods", text="Empty Plane", icon="MOD_ARRAY")
                    row.operator("tp_ops.add_empty_array", text="", icon="OUTLINER_DATA_EMPTY")

                    row = box.row(1) 
                    if tp_props.display_empty:
                        row.prop(tp_props, "display_empty", text="", icon='TRIA_DOWN')
                    else:
                        row.prop(tp_props, "display_empty", text="", icon='TRIA_RIGHT')                  
                    
                    row.operator("tp_ops.add_empty_curve_mods", text="Empty Array", icon="MOD_ARRAY")
                    row.operator("tp_ops.add_empty_curve", text="", icon="OUTLINER_DATA_CURVE")
                    

                    if tp_props.display_empty:  

                        mod_types = []
                        append = mod_types.append
                                              
                        obj = context.active_object       
                        if obj:

                            if obj.modifiers:
                        
                                box = layout.box().column(1)                 
                                
                                row = box.row(1)
                                row.operator("object.transform_apply", text="Applied Scale?", icon="OUTLINER_DATA_EMPTY").scale=True
                                row.operator("tp_ops.expand_mod","" ,icon = 'TRIA_DOWN')  
                                row.operator("tp_ops.collapse_mod", "" ,icon = 'TRIA_UP') 

                                row = box.row(1) 
                                row.operator("tp_ops.modifier_off","off" ,icon = 'VISIBLE_IPO_OFF')  
                                row.operator("tp_ops.modifier_on", "on" ,icon = 'RESTRICT_VIEW_OFF') 
                                row.operator("tp_ops.remove_mod", text="del." , icon='X') 
                                row.operator("tp_ops.apply_mod", text="set" , icon='FILE_TICK') 

                                box.separator()

                                for mod in context.active_object.modifiers:
                                      
                                    if mod.show_expanded == True:
                                        if mod.type == 'ARRAY':
                                            append(mod.type)
                                            
                                            box = layout.box().column(1) 
                                            
                                            if mod.fit_type == 'FIXED_COUNT':
                                                
                                                row = box.row(1)                                        
                                                row.label("Mesh Array")
                                                
                                                if mod.fit_type == 'FIXED_COUNT':
                                                    row.prop(mod, "count", text = "")                    

                                                box.separator()
                                                
                                                row = box.row(1)
                                                row.prop(mod, "relative_offset_displace", text="")

                                                box.separator()
                                                
                                                row = box.row(1)
                                                row.prop(mod, "use_merge_vertices", text="Merge")
                                                row.prop(mod, "use_merge_vertices_cap", text="First Last")
                                                
                                                row = box.row(1)
                                                row.prop(mod, "merge_threshold", text="Distance")

                                                box.separator()   
                                                
                                                row = box.column(1)
                                                row.prop(mod, "offset_object", text="")   
                                                
                                                box.separator()

                                            elif mod.fit_type == 'FIT_CURVE':
                                               
                                                box.separator()
                                            
                                                row = box.row(1)
                                                row.label(text="Mesh Offset")                                                                                      
                                               
                                                row = box.row(1)
                                                row.prop(mod, "relative_offset_displace", text = "")

                                                box.separator()
                                                
                                                row = box.row(1)
                                                row.prop(mod, "use_merge_vertices", text="Merge")
                                                row.prop(mod, "use_merge_vertices_cap", text="First Last")
                                                
                                                row = box.row(1)
                                                row.prop(mod, "merge_threshold", text="Distance")
                                                
                                                box.separator()   
                                                
                                                row = box.row(1)                                          
                                                row.prop(mod, "curve", text = "")    

                                                box.separator()                      
                                       
                                        elif mod.type == 'CURVE':
                                            append(mod.type)                         
                                            
                                            box = layout.box().column(1) 
                                            
                                            row = box.column(1)
                                            row.label(text="Curve Deformation Axis")
                                            
                                            row = box.column(1)                                        
                                            row.row().prop(mod, "deform_axis", expand=True)
                                            
                                            box.separator()
                                            
                                            row = box.column(1) 
                                            row.prop(mod, "object", text="")
                                                                                    
                                            box.separator()
                                
                                    else:
                                        box.separator()  
                            
                            else:
                                box = layout.box().column(1) 
                                
                                row = box.row(1)
                                row.operator("tp_help.empty_array", text = "! nothing selected !", icon ="INFO")   
                            
                                box = layout.box().column(1) 
                                    
                        else:
                            box = layout.box().column(1) 
                            
                            row = box.row(1)
                            row.operator("tp_help.empty_array", text = "! nothing selected !", icon ="INFO")             
                            
                            box = layout.box().column(1) 
                          
                          
                    box.separator() 

                    row = box.row(1) 
                    if tp_props.display_array:
                        row.prop(tp_props, "display_array", text="", icon='TRIA_DOWN')
                    else:
                        row.prop(tp_props, "display_array", text="", icon='TRIA_RIGHT')                  

                    row.operator("tp_ops.add_curve_array_mods", text="Curve Array", icon="MOD_ARRAY")     
                    row.operator("tp_ops.add_curve_array", text="", icon="CURVE_BEZCURVE")    
                          
                    row = box.row(1) 
                    if tp_props.display_array:
                        row.prop(tp_props, "display_array", text="", icon='TRIA_DOWN')
                    else:
                        row.prop(tp_props, "display_array", text="", icon='TRIA_RIGHT')                           

                    row.operator("tp_ops.add_circle_array_mods", text="Circle Array", icon="MOD_ARRAY")
                    row.operator("tp_ops.add_circle_array", text="", icon="CURVE_BEZCIRCLE")
                    
                    if tp_props.display_array:

                        mod_types = []
                        append = mod_types.append
                        
                        obj = context.active_object       
                        if obj:

                            if obj.modifiers:
                         
                                box = layout.box().column(1)                 
                                
                                row = box.row(1)
                                row.operator("object.transform_apply", text="Applied Scale?", icon="OUTLINER_DATA_EMPTY").scale=True
                                row.operator("tp_ops.expand_mod","" ,icon = 'TRIA_DOWN')  
                                row.operator("tp_ops.collapse_mod", "" ,icon = 'TRIA_UP') 

                                row = box.row(1) 
                                row.operator("tp_ops.modifier_off","off" ,icon = 'VISIBLE_IPO_OFF')  
                                row.operator("tp_ops.modifier_on", "on" ,icon = 'RESTRICT_VIEW_OFF') 
                                row.operator("tp_ops.remove_mod", text="del." , icon='X') 
                                row.operator("tp_ops.apply_mod", text="set" , icon='FILE_TICK') 

                                box.separator() 
                        
                                for mod in context.active_object.modifiers:
                                      
                                    if mod.show_expanded == True:
                                        if mod.type == 'ARRAY':
                                            append(mod.type)
                                            
                                            box = layout.box().column(1) 
                                            
                                            if mod.fit_type == 'FIXED_COUNT':
                                                
                                                row = box.row(1)                                        
                                                row.label("Mesh Array")
                                                
                                                if mod.fit_type == 'FIXED_COUNT':
                                                    row.prop(mod, "count", text = "")                    

                                                box.separator()
                                                
                                                row = box.row(1)
                                                row.prop(mod, "relative_offset_displace", text="")

                                                box.separator()
                                                
                                                row = box.row(1)
                                                row.prop(mod, "use_merge_vertices", text="Merge")
                                                row.prop(mod, "use_merge_vertices_cap", text="First Last")
                                                
                                                row = box.row(1)
                                                row.prop(mod, "merge_threshold", text="Distance")

                                                box.separator()   
                                                
                                                row = box.column(1)
                                                row.prop(mod, "offset_object", text="")   
                                                
                                                box.separator()

                                            elif mod.fit_type == 'FIT_CURVE':
                                               
                                                box.separator()
                                            
                                                row = box.row(1)
                                                row.label(text="Mesh Offset")                                                                                      
                                               
                                                row = box.row(1)
                                                row.prop(mod, "relative_offset_displace", text = "")

                                                box.separator()
                                                
                                                row = box.row(1)
                                                row.prop(mod, "use_merge_vertices", text="Merge")
                                                row.prop(mod, "use_merge_vertices_cap", text="First Last")
                                                
                                                row = box.row(1)
                                                row.prop(mod, "merge_threshold", text="Distance")
                                                
                                                box.separator()   
                                                
                                                row = box.row(1)                                          
                                                row.prop(mod, "curve", text = "")    

                                                box.separator()                      
                                       
                                        elif mod.type == 'CURVE':
                                            append(mod.type)                         
                                            
                                            box = layout.box().column(1) 
                                            
                                            row = box.column(1)
                                            row.label(text="Curve Deformation Axis")
                                            
                                            row = box.column(1)                                        
                                            row.row().prop(mod, "deform_axis", expand=True)
                                            
                                            box.separator()
                                            
                                            row = box.column(1) 
                                            row.prop(mod, "object", text="")
                                                                                    
                                            box.separator()
                                
                                    else:
                                        box.separator()  
                            
                            else:
                                box = layout.box().column(1) 
                                
                                row = box.row(1)
                                row.operator("tp_help.curve_array", text = "! nothing selected !", icon ="INFO")   
                            
                                box = layout.box().column(1) 
                                    
                        else:
                            box = layout.box().column(1) 
                            
                            row = box.row(1)
                            row.operator("tp_help.curve_array", text = "! nothing selected !", icon ="INFO")             
                            
                            box = layout.box().column(1) 
                          
                      
                    box.separator()                        
                     
                    row = box.row(1) 
                    if tp_props.display_pfath:
                        row.prop(tp_props, "display_pfath", text="", icon='TRIA_DOWN')
                    else:
                        row.prop(tp_props, "display_pfath", text="", icon='TRIA_RIGHT')            

                    display_Dynamics = context.user_preferences.addons[__package__].preferences.tab_dynamics
                    if display_Dynamics == 'on':     
                        row.operator("object.fpath_array", text="", icon ="ALIGN")                              
                    else:
                        pass
                    
                    row.operator("tp_ops.add_fpath_con", text="Add Follow Path", icon="CONSTRAINT_DATA")          
                    row.operator("tp_ops.add_fpath_curve", text="", icon="CURVE_BEZCIRCLE")
                   
                    box.separator() 
                    
                    if tp_props.display_pfath:
                        
                        con_types = []
                        append = con_types.append
                        
                        obj = context.active_object     
                        if obj:                                            
                            if obj.constraints:
                                                                                            
                                for con in context.active_object.constraints:

                                    box = layout.box().column(1)
                            
                                    row = box.row(1)
                                    row.operator("object.fpath_array_panel", text="Set FPath Array", icon ="MOD_ARRAY")  
                                    
                                    box.separator()
                                    
                                    row = box.row(1)
                                    row.prop(context.scene, "type", )    
                                    
                                    row = box.row(1)                            
                                    row.prop(context.scene, "count")

                                                                     
                                    box.separator() 

                                    row = box.row(1)
                                    layout.operator_context = 'INVOKE_REGION_WIN'                    
                                    row.prop(context.scene, "frame_current", text="Frame")
                                    row.operator("object.select_grouped", text="Select Group").type='GROUP'
                                        
                                    row = box.row(1)      
                                    row.operator("tp_ops.linked_fpath",text="Set Linked")                  
                                    row.operator("tp_ops.single_fpath",text="Set Unlinked")  

                                    box.separator() 
                                    
                                    box = layout.box().column(1)                 
                                    
                                    row = box.row(1)
                                      
                                    row.operator("object.transform_apply", text="Applied Scale?", icon="OUTLINER_DATA_EMPTY").scale=True
                                    row.operator("tp_ops.expand_con","" ,icon = 'TRIA_DOWN')  
                                    row.operator("tp_ops.collapse_con", "" ,icon = 'TRIA_UP') 

                                    row = box.row(1) 
                                    row.operator("tp_ops.constraint_off","off" ,icon = 'VISIBLE_IPO_OFF')  
                                    row.operator("tp_ops.constraint_on", "on" ,icon = 'RESTRICT_VIEW_OFF') 
                                    row.operator("object.constraints_clear", text="clear" , icon='X') 

                                    box.separator()                                     

                                    if con.show_expanded == True:  
                                                                                
                                        box = layout.box().column(1) 
                                
                                        row = box.row(1)  
                                        
                                        if con.type == 'FOLLOW_PATH':
                                           
                                            append(con.type)

                                            box.label(con.name)
                                            
                                            box.prop(con, "target")

                                            box.separator() 
                                            
                                            row = box.column(1)                                                      
                                            row.operator("constraint.followpath_path_animate", text="Animate Path", icon='ANIM_DATA')
                                            row.label("!need activation in properties!")  
                                            
                                            box.separator()
                                            
                                            if context.scene.type == "OFFSET":
                                                row.prop(context.scene,"offset")
                                       
                                            elif context.scene.type == "FIXED_POSITION":
                                                row.prop(context.scene,"factor", "Offset")
                                                                                         
                                            box.separator() 
                                            
                                            row.prop(con, "use_curve_follow")
                                            
                                            row = box.row(1)
                                            row.label("Axis")
                                            row.prop(con, "forward_axis", expand=True)

                                            box.separator() 
                                            
                                            row = box.row(1)                            
                                            row.prop(con, "up_axis", text="Up")
                                            row.label()

                                            ###
                                            box.separator()   
                                    
                            else:
                                box = layout.box().column(1) 
                                
                                row = box.row(1)
                                row.operator("tp_help.follow_path", text ="! no constraint active !", icon ="INFO")  
                                    
                        else:
                            box = layout.box().column(1) 
                            
                            row = box.row(1)
                            row.operator("tp_help.follow_path", text = "! nothing selected !", icon ="INFO")             


                box.separator() 
             

            display_advance = context.user_preferences.addons[__package__].preferences.tab_advance
            if display_advance == 'on':


                box = layout.box().column(1) 
                 
                row = box.row(1)
                
                if tp_props.display_toall:
                    row.prop(tp_props, "display_toall", text="", icon='TRIA_DOWN')
                else:
                    row.prop(tp_props, "display_toall", text="", icon='TRIA_RIGHT')

                row.menu("VIEW3D_MT_copypopup", text="Advance Copy", icon = "DISCLOSURE_TRI_RIGHT") 
             
                if tp_props.display_toall:
                    scene = context.scene
                    
                    box = layout.box().column(1)
                        
                    row = box.row(1) 
                    row.alignment = 'CENTER'                
                    row.label("Material", icon='MATERIAL') 

                    row = box.row(1) 
                    row.label("copy to:") 
                                      
                    row = box.row(1)   
                    row.operator("scene.to_all", text="Selected").mode = "material, selected"
                    row.operator("scene.to_all", text="Children").mode = "material, children"

                    box.separator()
                                    
                    row = box.row(1) 
                    row.label("append to:") 
                                      
                    row = box.row(1)   
                    row.operator("scene.to_all", text="Selected").mode = "material, selected, append"
                    row.operator("scene.to_all", text="Children").mode = "material, children, append"

                    box.separator()

                    box = layout.box().column(1)
                        
                    row = box.row(1) 
                    row.alignment = 'CENTER'                
                    row.label("Modifier", icon='MODIFIER') 
     
                    row = box.row(1) 
                    row.label("copy to:") 
                                      
                    row = box.row(1)   
                    row.operator("scene.to_all", text="Selected").mode = "modifier, selected"
                    row.operator("scene.to_all", text="Children").mode = "modifier, children"

                    box.separator()                

                    row = box.row(1) 
                    row.label("append to:") 
                                      
                    row = box.row(1)   
                    row.operator("scene.to_all", text="Selected").mode = "modifier, selected, append"
                    row.operator("scene.to_all", text="Children").mode = "modifier, children, append"
                    
                    box.separator()  

                    row = box.row(1)
                    row.prop(context.scene, "excludeMod")              
                    


            display_instances = context.user_preferences.addons[__package__].preferences.tab_instances
            if display_instances == 'on':
                
                box.separator()      

                box = layout.box().column(1) 
                 
                row = box.column(1)
                row.label("Linked Instances", icon = "CONSTRAINT_DATA")
                
                box.separator() 
                                 
                row = box.row(1)     
                row.operator("object.make_links_data","Set", icon="LINKED").type='OBDATA'
                row.operator("tp_ops.make_single","Clear", icon="UNLINKED")
               
                box.separator() 
               
                row = box.row(1)                 
                row.operator("object.select_linked", text="Linked", icon="RESTRICT_SELECT_OFF")   
                row.operator("object.join", text="Join", icon="AUTOMERGE_ON")             

                box.separator() 
               
                row = box.row(1)  

                row.operator_menu_enum("object.make_links_data", "type","links",  icon="CONSTRAINT")
                
                sub = row.row(1)
                sub.scale_x = 0.3333            
                sub.operator("tp_ops.origin_plus_z", text="T", icon="LAYER_USED")  
                props = sub.operator("object.origin_set", text="M", icon="LAYER_USED")
                props.type = 'ORIGIN_GEOMETRY'
                props.center = 'BOUNDS'
                sub.operator("tp_ops.origin_minus_z", text="B", icon="LAYER_USED")

                box.separator()




        if context.mode == 'EDIT_MESH':

            box = layout.box().column(1)
             
            row = box.column(1)
            row.operator("mesh.duplicate_move", text="Duplicate", icon="MOD_BOOLEAN")
            
            box = layout.box().column(1) 
             
            row = box.column(1)  
            row.operator("tp_ops.copy_to_cursor_panel", text="Copy to Cursor", icon="NEXT_KEYFRAME")                      
            row.prop(context.scene, "ctc_total", text="How many?")

            box.separator()   


        display_transform = context.user_preferences.addons[__package__].preferences.tab_transform
        if display_transform == 'on':
            
            if context.mode == 'OBJECT':  
                
                box = layout.box().column(1)
                
                row = box.row(1)
                if tp_props.display_apply:            
                    row.prop(tp_props, "display_apply", text="", icon="MANIPUL")
                else:
                    row.prop(tp_props, "display_apply", text="", icon="MANIPUL")
                             
                row.label("Apply")  

                sub = row.row(1)
                sub.scale_x = 0.3           
                sub.operator("object.transform_apply", text=" ", icon ="MAN_TRANS").location=True
                sub.operator("object.transform_apply", text=" ", icon ="MAN_ROT").rotation=True                
                sub.operator("object.transform_apply", text=" ", icon ="MAN_SCALE").scale=True                             
                
                if tp_props.display_apply: 
                   
                    box = layout.box().column(1)
                    
                    row = box.column_flow(2)
                    row.label("Transforms to Deltas")  
                    row.operator("object.transforms_to_deltas", text="Location").mode='LOC'
                    row.operator("object.transforms_to_deltas", text="Rotation").mode='ROT' 
                    row.operator("object.transforms_to_deltas", text="All").mode='ALL'
                    row.operator("object.transforms_to_deltas", text="Scale").mode='SCALE'                    
                    row.operator("object.anim_transforms_to_deltas", text="Animated")
                    
                    box.separator() 
                   
                    row = box.column(1)
                    row.operator("object.visual_transform_apply")
                    row.operator("object.duplicates_make_real")
                                                  
                box.separator()                     


        display_shade = context.user_preferences.addons[__package__].preferences.tab_shade
        if display_shade == 'on':                                         

            box = layout.box().column(1)
            
            row = box.row(1)
            if tp_props.display_display:            
                row.prop(tp_props, "display_display", text="", icon="WORLD")
                row.label("Display")
            else:
                row.prop(tp_props, "display_display", text="", icon="WORLD")
                row.label("OSD")

                obj = context.active_object
                if obj:               
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text="", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="", icon='GHOST_ENABLED')        
                else:
                    row.label("", icon="BLANK1")  


                obj = context.active_object
                if obj:
                    active_wire = obj.show_wire 
                    if active_wire == True:
                        row.operator("tp_ops.wire_off", "", icon = 'MESH_PLANE')              
                    else:                       
                        row.operator("tp_ops.wire_on", "", icon = 'MESH_GRID')
                else:
                    row.label("", icon="BLANK1")  

                
                if context.mode == 'EDIT_MESH':          

                    row.operator("mesh.faces_shade_flat", text="", icon="MESH_CIRCLE") 
                    row.operator("mesh.faces_shade_smooth", text="", icon="SMOOTH")  
                    row.operator("mesh.normals_make_consistent", text="", icon="SNAP_NORMAL")  
                
                if context.mode == 'OBJECT':             
      
                    row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
                    row.operator("object.shade_smooth", text="", icon="SMOOTH")  
                    row.operator("tp_ops.rec_normals", text="", icon="SNAP_NORMAL") 

            
            if tp_props.display_display: 
            
                box.separator()
                
                row = box.row(1)                                                          
                row.operator("tp_ops.wire_all", text="Wire all", icon='WIRE')
                
                obj = context.active_object
                if obj:
                    active_wire = obj.show_wire 
                    if active_wire == True:
                        row.operator("tp_ops.wire_off", "Wire Select", icon = 'MESH_PLANE')              
                    else:                       
                        row.operator("tp_ops.wire_on", "Wire Select", icon = 'MESH_GRID')
                else:
                    row.label("", icon="BLANK1")            
               
                row = box.row(1)
                
                obj = context.active_object
                if obj:               
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text="Solid Shade", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text="Wire Shade", icon='GHOST_ENABLED')        
                else:
                    row.label("", icon="BLANK1")  
 
                ob = context.object
                if ob: 
                    row.prop(ob, "draw_type", text="")
                    
                    row = box.row(1)
                    row.prop(ob, "show_bounds", text="ShowBounds", icon='STICKY_UVS_LOC') 
                    row.prop(ob, "draw_bounds_type", text="")    
               
                else:
                    row.label("", icon="BLANK1") 

                
                if context.mode == 'EDIT_MESH':          
                    
                    box.separator() 
                    
                    row = box.row(1)  
                    row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
                    row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 
                    
                    row = box.row(1)  
                    row.operator("mesh.normals_make_consistent", text="Consistent Normals", icon="SNAP_NORMAL")  
                
                else:            
                    
                    box.separator() 
                    
                    if context.mode == 'OBJECT': 
                        
                        row = box.row(1)  
                        row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
                        row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
                   
                    row = box.row(1)  
                    row.operator("tp_ops.rec_normals", text="Consistent Normals", icon="SNAP_NORMAL")  

                box.separator() 






        display_history = context.user_preferences.addons[__package__].preferences.tab_history 
        if display_history == 'on':
            
            box = layout.box().column(1)  

            row = box.row(1)        
            row.operator("view3d.ruler", text="Ruler")   
             
            row.operator("ed.undo_history", text="History")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS") 
           
            box.separator()   

        else:
            pass     
  
  
        

class VIEW3D_TP_Copy_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Tools"
    bl_idname = "VIEW3D_TP_Copy_Panel_TOOLS"
    bl_label = "T+ Copy"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_context = 'objectmode'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)   
        return isModelingMode 


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_copy_panel_layout(self, context, layout) 
        


class VIEW3D_TP_Copy_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Copy_Panel_UI"
    bl_label = "T+ Copy"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_context = 'objectmode'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object) 
        return isModelingMode 


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
                              
        draw_copy_panel_layout(self, context, layout) 




class VIEW3D_TP_Copy_Panel_PROPS(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Copy_Panel_PROPS"
    bl_label = "T+ Copy"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object" #TAB
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object) 
        return isModelingMode 


    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
                              
        draw_copy_panel_layout(self, context, layout) 