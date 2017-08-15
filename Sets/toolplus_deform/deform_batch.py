__status__ = "toolplus custom version"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2016"


import bpy
from bpy import*
from bpy.props import *
from . icons.icons import load_icons


class View3D_TP_Deform_Batch(bpy.types.Operator):
    """Batch Deform"""
    bl_idname = "tp_batch.batch_deform"
    bl_label = "Deform :)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):      
        return {'FINISHED'}
           
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.scene and context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)

    def draw(self, context):
        
        tpw = context.window_manager.tpw_defom_window
        
        layout = self.layout
      
        icons = load_icons()

        wm = bpy.context.window_manager    
        layout.operator_context = 'INVOKE_REGION_WIN'
        

        if context.mode == 'EDIT_LATTICE':
            
            box = layout.box().column(1)                    

            row = box.row(1)

            row.prop(context.object.data, "use_outside")
            row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

            box.separator()                       

            row = box.row(1)
            row.prop(context.object.data, "points_u", text="X")
            row.prop(context.object.data, "points_v", text="Y")
            row.prop(context.object.data, "points_w", text="Z")
         
            row = box.row(1)
            row.prop(context.object.data, "interpolation_type_u", text="")
            row.prop(context.object.data, "interpolation_type_v", text="")
            row.prop(context.object.data, "interpolation_type_w", text="")  

            box.separator()                       

            row = box.row(1)
            row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")
             
            ###
            box.separator()   


        if context.mode == 'OBJECT':


            obj = context.active_object     
            if obj:
               obj_type = obj.type

               if obj_type in {'LATTICE'}:
                    box = layout.box().column(1)                    

                    row = box.row(1)

                    row.prop(context.object.data, "use_outside")
                    row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

                    box.separator()                       

                    row = box.row(1)
                    row.prop(context.object.data, "points_u", text="X")
                    row.prop(context.object.data, "points_v", text="Y")
                    row.prop(context.object.data, "points_w", text="Z")
                 
                    row = box.row(1)
                    row.prop(context.object.data, "interpolation_type_u", text="")
                    row.prop(context.object.data, "interpolation_type_v", text="")
                    row.prop(context.object.data, "interpolation_type_w", text="")  

                    box.separator()                       

                    row = box.column(1)
                    row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")
                    row.operator("tp_ops.zero_rotation", "Set zero rotation", icon ="MAN_ROT")
                    
                    box.separator()   


               else:
                    box = layout.box().column(1)   

                    row = box.row(1)
                    row.alignment = 'CENTER'
                    row.label("Easy Lattice")
                   
                    box.separator()   
                    
                    row = box.row(1)        
                                       
                    button_lattice_create = icons.get("icon_lattice_create")                                                               
                    row.operator("object.easy_lattice_panel", text="Create", icon_value=button_lattice_create.icon_id)  

                    button_lattice_apply = icons.get("icon_lattice_apply")    
                    row.operator("tp_ops.lattice_apply", text = "Apply", icon_value=button_lattice_apply.icon_id)                     
                        
                    box.separator()   
                    
                    row = box.row(1) 
                    row.prop(context.scene, "lat_u", text="X")
                    row.prop(context.scene, "lat_w", text="Y")
                    row.prop(context.scene, "lat_m", text="Z")
                    
                    box.separator()           
                    
                    row = box.row(1)
                    row.prop(context.scene, "lat_type", text = "Type")

                    box.separator()                    


            Display_MeshCage = context.user_preferences.addons[__package__].preferences.tab_meshcage_menu 
            if Display_MeshCage == 'on':   
                
                box = layout.box().column(1)   

                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("MeshCage Deform")
               
                box.separator()   
                
                row = box.row(1)         
                row.operator("tp_ops.add_bound_meshcage", "MeshCageBox", icon ="MOD_MESHDEFORM")            

                if context.object.draw_type == 'WIRE':
                    row.operator("tp_ops.draw_solid", text="", icon='GHOST_DISABLED')     
                else:
                    row.operator("tp_ops.draw_wire", text="", icon='GHOST_ENABLED') 
              
                row = box.row(1)  
                obj = context.object
                if obj:
                    
                    MID = "MDeformer"
                    if obj.modifiers.get(MID, None):
                        row.operator("mesh.deformer_clear", "", icon ="PANEL_CLOSE")
                    else:
                        row.operator("mesh.deformer_set", "Set Deformer", icon ="CONSTRAINT_DATA")

                box.separator()  

            else:
                pass

           
            Display_Project = context.user_preferences.addons[__package__].preferences.tab_project_menu 
            if Display_Project == 'on':   
 
                box = layout.box().column(1)   

                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("Project to active Surface")
               
                box.separator()   
                
                row = box.column(1)                           
                row.operator("mesh.project_onto_uvmapped_mesh", text="to UVs", icon ="MOD_LATTICE")  
                row.operator("mesh.project_onto_selected_mesh", text = "to Mesh", icon="MOD_SHRINKWRAP")    
                row.operator("mesh.mirror_mesh_along_mirrormesh_normals", text = "Normals Mirror", icon="MOD_MIRROR")    

                ###
                box.separator()                                     
            else:
                pass



            Display_VertexGroups = context.user_preferences.addons[__package__].preferences.tab_vertgrp_menu 
            if Display_VertexGroups == 'on':   
                     
                box = layout.box().column(1)   

                row = box.row(1)              
                row.alignment = 'CENTER'
                row.label("VertexGroups", icon='STICKY_UVS_LOC')     
                
                box.separator()                                       
                
                row = box.row()
                row.template_list("MESH_UL_vgroups", "", context.object, "vertex_groups", context.object.vertex_groups, "active_index", rows=4)           

                col = row.column()
                sub = col.column(1)
                sub.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                sub.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                sub.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                sub.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                sub.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                
                
                ###
                box.separator()    


            Display_Hook = context.user_preferences.addons[__package__].preferences.tab_hook_menu
            if Display_Hook == 'on':   
                
                obj = context.active_object
                if obj:
                    for mo in obj.modifiers:
                        if mo.type == 'HOOK':
                         
                            row = box.row()
                            if tpw.display_mod_hook:
                                row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')            
                            else:                
                                row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')

                            if tpw.display_mod_hook: 

                                row = box.column(1)                                 
                                mo_types = []
                                append = mo_types.append

                                for mo in context.active_object.modifiers:
                                    if mo.type == 'HOOK':
                                        
                                        append(mo.type)

                                        box = layout.box().column(1)  

                                        row = box.column(1)                                  
                                        row.label(mo.name)

                                        row = box.column(1)
                                        row.prop(mo, "object", text="")
                                        row.prop_search(mo, "vertex_group", context.object, "vertex_groups", text="")

                                        box.separator()

                                        row = box.column(1)
                                        row.prop(mo, "falloff_radius")
                                        row.prop(mo, "strength", slider=True)
                                        
                                        box.separator()
                                        
                                        row = box.column(1)
                                        row.prop(mo, "use_falloff_uniform")
                                        row.prop(mo, "falloff_type", text="")                                                        

                                        ###
                                        box.separator()   

            else:
                pass


        if context.mode == 'EDIT_MESH':

            box = layout.box().column(1)   

            row = box.row(1)
            row.alignment = 'CENTER'
            row.label("Easy Lattice")
          
            box.separator()                 
          
            row = box.row(1)      
                                 
            button_lattice_create = icons.get("icon_lattice_create")                                                               
            row.operator("object.easy_lattice_panel", text="Create", icon_value=button_lattice_create.icon_id)  

            button_lattice_apply = icons.get("icon_lattice_apply")    
            row.operator("tp_ops.lattice_apply", text = "Apply", icon_value=button_lattice_apply.icon_id)                                                   
                      
            box.separator()   
            
            row = box.row(1) 
            row.prop(context.scene, "lat_u", text="X")
            row.prop(context.scene, "lat_w", text="Y")
            row.prop(context.scene, "lat_m", text="Z")
            
            box.separator()           
            
            row = box.row(1)
            row.prop(context.scene, "lat_type", text = "Type")

            ###
            box.separator()     


            Display_Project = context.user_preferences.addons[__package__].preferences.tab_project_menu 
            if Display_Project == 'on':   

                box = layout.box().column(1)   

                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("MeshCage Deform")
               
                box.separator()   
                
                row = box.column(1)

                if context.object:
                    objects = assigned_objects(context.object)
                    
                    if len(objects) > 0:
                        info = "%d associated objects"  % len(objects)
                        
                        row.label(text=info)

                        if is_bound(context.object):
                            
                            row.operator("mesh.deformer_bind", text = "Unbind objects") 
                            
                            box.separator() 
                            
                            row = box.row(1)
                            row.operator("mesh.deformer_clear", text= "Remove").apply=False
                            row.operator("mesh.deformer_clear", text= "Apply").apply=True
                       
                        else:   
                            row.operator("mesh.deformer_bind", text = "Bind objects")
                            
                            row = box.row()
                            row.operator("mesh.deformer_clear", text= "Remove").apply=False

                    else: 
                        row.label(text="no associated objects", icon = "INFO")                   
                        
                ###
                box.separator()                                     
            else:
                pass


            Display_VertexGroups = context.user_preferences.addons[__package__].preferences.tab_vertgrp_menu 
            if Display_VertexGroups == 'on':   
 
                box = layout.box().column(1)   

                row = box.row(1)              
                row.alignment = 'CENTER'
                row.label("VertexGroups", icon='STICKY_UVS_LOC')     
                
                box.separator()                                       
                
                row = box.row()
                row.template_list("MESH_UL_vgroups", "", context.object, "vertex_groups", context.object.vertex_groups, "active_index", rows=4)           

                col = row.column()
                sub = col.column(1)
                sub.operator("object.vertex_group_add", icon='ZOOMIN', text="")
                sub.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
                sub.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
                sub.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                sub.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'                                

                row = box.row(1)
                row.operator("object.vertex_group_assign", text="Assign", icon="ZOOMIN") 
                row.operator("object.vertex_group_remove_from", text="Remove", icon="ZOOMOUT") 

                row = box.row(1)                    
                row.operator("object.vertex_group_select", text="Select", icon="RESTRICT_SELECT_OFF")
                row.operator("object.vertex_group_deselect", text="Deselect", icon="RESTRICT_SELECT_ON")
                
                row = box.row(1)
                row.prop(context.tool_settings, "vertex_group_weight", text="Weight")
            
                ###
                box.separator()    
            else:
                pass

           
            Display_Hook = context.user_preferences.addons[__package__].preferences.tab_hook_menu 
            if Display_Hook == 'on':   
                
                box = layout.box().column(1)   

                row = box.row(1)              
                row.alignment = 'CENTER'
                row.label("HOOK", icon='HOOK')     
                
                box.separator()
                      
                row = box.row(1)   
                row.operator_context = 'EXEC_AREA'
                row.operator("object.hook_add_newob", text="to New")
                row.operator("object.hook_add_selob", text="to Selected").use_bone = False
                    
                row = box.row(1)
                row.operator("object.hook_add_selob", text="to Selected Object Bone").use_bone = True

                box.separator()

                for mo in context.active_object.modifiers:
                    
                    if mo.type == 'HOOK':
                        
                        row = box.row(1)
                        row.operator_menu_enum("object.hook_assign", "modifier", text="Assign")
                        row.operator_menu_enum("object.hook_remove", "modifier", text="Remove")
                            
                        row = box.row(1)
                        row.operator_menu_enum("object.hook_select", "modifier", text="Select")
                        row.operator_menu_enum("object.hook_reset", "modifier", text="Reset")
                        
                        row = box.row(1)
                        row.operator_menu_enum("object.hook_recenter", "modifier", text="Recenter")                            

                        box.separator()  
                   
                        row = box.column(1) 

                        if tpw.display_mod_hook:
                            row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')            
                        else:                
                            row.prop(tpw, "display_mod_hook", text="Hook Mod", icon='HOOK')

                        if tpw.display_mod_hook: 

                            row = box.column(1)                                 
                            mo_types = []
                            append = mo_types.append

                            obj = context.active_object
                            if obj:
                                for mo in obj.modifiers:
                                    if mo.type == 'HOOK':
                                        
                                        append(mo.type)

                                        box = layout.box().column(1)  

                                        row = box.column(1)                                  
                                        row.label(mo.name)

                                        row = box.column(1)
                                        row.prop(mo, "object", text="")
                                        row.prop_search(mo, "vertex_group", context.object, "vertex_groups", text="")

                                        box.separator()

                                        row = box.column(1)
                                        row.prop(mo, "falloff_radius")
                                        row.prop(mo, "strength", slider=True)
                                        
                                        box.separator()
                                        
                                        row = box.column(1)
                                        row.prop(mo, "use_falloff_uniform")
                                        row.prop(mo, "falloff_type", text="")                                                        

                                        ###
                                        box.separator()   
            else:
                pass


        obj = context.active_object
        if obj:
            if obj.modifiers:  
                                      
                box = layout.box().column(1)  

                row = box.row(1)  
                row.operator("tp_ops.remove_mod", text="Clear All", icon='X') 
                row.operator("tp_ops.apply_mod", text="Apply All", icon='FILE_TICK')  
                
                row = box.row(1)
                row.operator("tp_ops.modifier_on", "View on",icon = 'RESTRICT_VIEW_OFF')     
                row.operator("tp_ops.modifier_off","View off",icon = 'VISIBLE_IPO_OFF')  
          
                box.separator() 
                   
            else:
                pass
        

        Display_History = context.user_preferences.addons[__package__].preferences.tab_history_menu 
        if Display_History == 'on':

            box = layout.box().column(1)    
                          
            row = box.row(1)         
            row.operator("ed.undo", text=" ", icon="LOOP_BACK")
            row.operator("ed.redo", text=" ", icon="LOOP_FORWARDS") 
                    
        else:
            pass

    def check(self, context):
        return True


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


