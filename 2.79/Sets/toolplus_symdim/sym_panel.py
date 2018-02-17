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


def draw_symmetry_panel_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_menu_symmetry        
        
        icons = load_icons()
  
        col = layout.column(1)

        box = col.box().column(1)
        
        row = box.row(1)

        if tp_props.display_dim:            
            row.prop(tp_props, "display_dim", text="", icon="MAN_SCALE")            
            row.label("CopyDim") 
        
        else:
            row.prop(tp_props, "display_dim", text="", icon="MOD_WIREFRAME")                
            row.label("MirrorCut") 
                               
            row.prop(context.scene, "tp_mirror", text="", icon ="MOD_MIRROR")   
            if bpy.context.scene.tp_mirror == True:
                row.prop(context.scene, "tp_apply", text="", icon ="FILE_TICK")                     
            else:
                pass
            row.prop(context.scene, "tp_sculpt", text="", icon ="SCULPTMODE_HLT")   
            row.prop(context.scene, "tp_edit", text="", icon ="EDIT")            
                        

        if tp_props.display_dim:  
        
            box.separator()  
           
            row = box.row(1)
            row.operator("tp_ops.copy_dimension_axis", text = "x > y").tp_axis='tp_x_y'
            row.operator("tp_ops.copy_dimension_axis", text = "y > x").tp_axis='tp_y_x'
            row.operator("tp_ops.copy_dimension_axis", text = "z > x").tp_axis='tp_z_x'            

            row = box.row(1)           
            row.operator("tp_ops.copy_dimension_axis", text = "x > z").tp_axis='tp_x_z'
            row.operator("tp_ops.copy_dimension_axis", text = "y > z").tp_axis='tp_y_z'
            row.operator("tp_ops.copy_dimension_axis", text = "z > y").tp_axis='tp_z_y'

            box.separator()                 

        else:
            
            box.separator()                    
                               
            row = box.row(1)         
            row.operator("tp_ops.mods_positiv_x_symcut", text="+X")
            row.operator("tp_ops.mods_positiv_y_symcut", text="+Y")
            row.operator("tp_ops.mods_positiv_z_symcut", text="+Z")

            row = box.row(1)             
            row.operator("tp_ops.mods_negativ_x_symcut", text="-- X")
            row.operator("tp_ops.mods_negativ_y_symcut", text="-- Y")
            row.operator("tp_ops.mods_negativ_z_symcut", text="-- Z")
         
            box.separator() 

            row = box.row(1)             
            row.operator("tp_ops.mods_negativ_xy_symcut", text="+Xy")
            row.operator("tp_ops.mods_negativ_xz_symcut", text="+Xz")
            row.operator("tp_ops.mods_negativ_yz_symcut", text="+Yz")

            row = box.row(1)             
            row.operator("tp_ops.mods_positiv_xy_symcut", text="-- Xy")
            row.operator("tp_ops.mods_positiv_xz_symcut", text="-- Xz")
            row.operator("tp_ops.mods_positiv_yz_symcut", text="-- Yz")
     
            box.separator()  
      
            row = box.row(1)             
            row.operator("tp_ops.mods_positiv_xyz_symcut", text="+XYZ")          
            row.operator("tp_ops.mods_negativ_xyz_symcut", text="-XYZ")
            
            if context.mode == 'EDIT_MESH':
                row.operator("tp_ops.normal_symcut", text="Normal")
                
                box.separator()            
                
                box = col.box().column(1)
 
                row = box.row(1)
                button_remove = icons.get("icon_remove")
                row.operator("tp_ops.remove_doubles", text="Del.",icon_value=button_remove.icon_id)                 
             
                button_flip = icons.get("icon_flip")                
                row.operator("mesh.flip_normals", text="Flip",icon_value=button_flip.icon_id) 

                button_recalc = icons.get("icon_recalc")                 
                row.operator("mesh.normals_make_consistent", text="Recalc.",icon_value=button_recalc.icon_id)   

            box.separator() 

                 

 
        obj = context.object
        if obj:
            if obj.type in {'MESH'}:

                is_mirror = False
                
                for mode in bpy.context.object.modifiers :
                    if mode.type == 'MIRROR' :
                        is_mirror = True
                
                if is_mirror == True:
                    
                    box = col.box().column(1)   

                    row = box.row(1)
                    row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF') 
                    row.operator("tp_ops.mods_view"," ", icon = 'RESTRICT_VIEW_OFF')               

                    if context.active_object.mode == 'EDIT':                                                                    
                        row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
                        row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  

                    row.operator("tp_ops.remove_mod_mirror", text=" ", icon='X') 
                  
                    button_apply = icons.get("icon_apply")
                    row.operator("tp_ops.apply_mod_mirror", text=" ",icon_value=button_apply.icon_id)
                    
                    box.separator()                                                                                                                                                                                                                                                                                            

                else:
                    pass
    
                obj = context.active_object
                if obj:
     
                    mo_types = []            
                    append = mo_types.append

                    for mo in context.active_object.modifiers:
                                                      
                        if mo.type == 'MIRROR':
                            append(mo.type)
                            #box.label(mo.name)

                            row = box.row(1)
                            row.prop(mo, "use_x")
                            row.prop(mo, "use_y")
                            row.prop(mo, "use_z")
                            
                            row = box.row(1)
                            row.prop(mo, "use_mirror_merge", text="Merge")
                            row.prop(mo, "use_clip", text="Clipping")
             
                            box.separator() 
                else:
                    pass

        else:
            pass                
 
        

        


class VIEW3D_TP_SymDim_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_SymDim_Panel_TOOLS"
    bl_label = "SymDim"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_symmetry_panel_layout(self, context, layout) 



class VIEW3D_TP_SymDim_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_SymDim_Panel_UI"
    bl_label = "SymDim"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'  

        draw_symmetry_panel_layout(self, context, layout) 


