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
    
EDIT = ["EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE", "POSE"]
GEOM = ['META', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'FORCE', 'SPEAKER']

class draw_layout_modifier:

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
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

        tp = context.window_manager.tp_props_display    
        icons = load_icons()
  
        ob = context.object  
        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene 

        box = layout.box().column(1)  
            
        row = box.row(1) 
        row.operator_menu_enum("object.modifier_add", "type","Add Modifier", icon="MODIFIER")          

        obj = context.active_object
        if obj:
            mod_list = obj.modifiers
            if mod_list:

                if context.mode == 'OBJECT':
                
                    row.operator("tp_ops.mods_render","", icon = 'RESTRICT_RENDER_OFF') 
                    row.operator("tp_ops.mods_view","", icon = 'RESTRICT_VIEW_OFF')                                                                       
                
                if context.active_object.mode == 'EDIT':
                
                    row.operator("tp_ops.mods_edit","", icon='EDITMODE_HLT')                                                    
                    row.operator("tp_ops.mods_cage","", icon='OUTLINER_OB_MESH')                  
                
                row.operator("tp_ops.remove_mod", text="", icon='X') 
                row.operator("tp_ops.apply_mod", text="", icon='FILE_TICK')          

        else:
            pass
  
        box.separator() 

        obj = context.active_object
        if obj:
            mod_list = obj.modifiers
            if mod_list:

                row = box.row(1)

                row.prop(context.scene, "tp_mods_type", text="")
                row.operator("tp_ops.remove_mods_type", text="Remove by Type")                           
 

                if context.mode == 'OBJECT':

                    row = box.row(1)
                    row.operator("scene.to_all", text="To Childs", icon='LINKED').mode = "modifier, children"    
                    row.operator("scene.to_all", text="To Selected", icon='FRAME_NEXT').mode = "modifier, selected"

                box.separator() 

        else:
            pass


        box = layout.box().column(1)
        
        row = box.row(1)
        if tp.display_subsurf:            
            row.prop(tp, "display_subsurf", text="", icon="MOD_SUBSURF")
        else:
            row.prop(tp, "display_subsurf", text="", icon="MOD_SUBSURF")
            
        row.label("SubSurf")
       
        if len(context.selected_objects) == 1:
            
            is_subsurf = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'SUBSURF' :
                    is_subsurf = True
            
            if is_subsurf == True:
             
                if context.mode == 'EDIT_MESH':
                    row.operator("transform.edge_crease", text="", icon='IPO_EASE_IN_OUT')   

                row.operator("tp_ops.remove_mods_subsurf", text="" , icon='X')             
                row.operator("tp_ops.apply_mods_subsurf", text="", icon='FILE_TICK')                                                                                                                                             
   
        else: 
            pass 
      

        box.separator()  
        
        row = box.row(1)
        row.scale_x = 0.6             
        row.operator("tp_ops.subsurf_0")
        row.operator("tp_ops.subsurf_1")
        row.operator("tp_ops.subsurf_2")            
        row.operator("tp_ops.subsurf_3")
        row.operator("tp_ops.subsurf_4")
        row.operator("tp_ops.subsurf_5")
        #row.operator("tp_ops.subsurf_6")


        
        box.separator() 
        
        if tp.display_subsurf: 
                            
            obj = context.active_object
            if obj:
 
                mo_types = []
                append = mo_types.append

                for mo in obj.modifiers:
                    if mo.type == 'SUBSURF':
                        append(mo.type)

                        #box.label(mo.name)

                        row = box.row(1)
                        row.prop(mo, "use_subsurf_uv",text="UVs")
                        row.prop(mo, "show_only_control_edges",text="Optimal")                    
                        #row.prop(mo, "use_opensubdiv",text="OPSubdiv")                    
                        #row.prop(system, "opensubdiv_compute_type", text="")

                        box.separator() 

            else:
                pass
            

        obj = context.active_object     
        if obj:
            obj_type = obj.type
                                                                  
            if obj_type in {'MESH'}:

                box = layout.box().column(1)
                
                row = box.row(1)

                if tp.display_dim:            
                    row.prop(tp, "display_dim", text="", icon="MAN_SCALE")            
                    row.label("CopyDim") 
                
                else:
                    row.prop(tp, "display_dim", text="", icon="MOD_WIREFRAME")                
                    row.label("MirrorCut") 
                                       
                    row.prop(context.scene, "tp_mirror", text="", icon ="MOD_MIRROR")   
                    if bpy.context.scene.tp_mirror == True:
                        row.prop(context.scene, "tp_apply", text="", icon ="FILE_TICK")                     
                    else:
                        pass
                    row.prop(context.scene, "tp_sculpt", text="", icon ="SCULPTMODE_HLT")   
                    row.prop(context.scene, "tp_edit", text="", icon ="EDIT")            
                                

                if tp.display_dim:  
                
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

                        row.operator("tp_ops.remove_mod_mirror", text="", icon='X') 
                        row.operator("tp_ops.apply_mod_mirror", text="", icon='FILE_TICK')

            else:
                pass

        else:
            pass                
 
        

class VIEW3D_TP_Modifier_Panel_TOOLS(bpy.types.Panel, draw_layout_modifier):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Modifier_Panel_TOOLS"
    bl_label = "Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_Modifier_Panel_UI(bpy.types.Panel, draw_layout_modifier):
    bl_idname = "VIEW3D_TP_Modifier_Panel_UI"
    bl_label = "Modifier"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}









