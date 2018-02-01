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


class VIEW3D_TP_Deform_Menu(bpy.types.Operator):
    """Deform Menu"""
    bl_idname = "tp_menu.batch_deform"
    bl_label = "Deform"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):      
        return {'FINISHED'}
           
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.scene and context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)

    def draw(self, context):
        
        tpw = context.window_manager.tp_props_defom_window
        
        layout = self.layout
        wm = bpy.context.window_manager    
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()   

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
                    row.label("Easy Lattice Mesh Deform")
                   
                    box.separator()   
                    
                    row = box.row(1)                           
                    row.operator("tp_ops.easy_lattice_panel", text="Create", icon ="OUTLINER_DATA_LATTICE")  
                    row.operator("tp_ops.lattice_apply", text = "Apply", icon="MOD_LATTICE")                    
                        
                    box.separator()   
                    
                    row = box.row(1) 
                    row.prop(context.scene, "lat_u", text="X")
                    row.prop(context.scene, "lat_w", text="Y")
                    row.prop(context.scene, "lat_m", text="Z")
                    
                    box.separator()           
                    
                    row = box.row(1)
                    row.prop(context.scene, "lat_type", text = "Type")

                    box.separator()                    



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
            
            row = box.row(1)                           
            row.operator("tp_ops.easy_lattice", text="Create", icon ="OUTLINER_DATA_LATTICE")  
            #row.operator("tp_ops.lattice_apply", text = "Apply", icon="MOD_LATTICE")                               
                      
            ###
            box.separator()     

           
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
                
                box.separator()  
                
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
        

    def check(self, context):
        return True


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
