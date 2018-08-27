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


# DRAW SYMDIM #
def draw_symdim_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        

        icons = load_icons()
  
        scene = context.scene
       
        col = layout.column(align=True)

        if not tp_props.display_symdim:  
            
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_symdim", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("AutoSym") 
            
            if scene.tp_sym_default == True:
                row.prop(scene, "tp_sym_default", text="", icon ="PAUSE")              
            else:           
                if context.mode == 'SCULPT':
                    row.prop(scene, "tp_sym_default", text="", icon ="PAUSE")  
                else:
                    row.prop(scene, "tp_mirror", text="", icon ="MOD_MIRROR")   
                    if scene.tp_mirror == True:
                        row.prop(scene, "tp_apply", text="", icon ="FILE_TICK")                     
                    else:
                        pass                        

            if context.mode == 'SCULPT':
                row.prop(scene, "tp_sculpt", text="", icon ="SCULPTMODE_HLT")   
            else:
                row.prop(scene, "tp_edit", text="", icon ="EDIT") 
            row.operator("tp_ops.mods_positiv_x_symcut", text="", icon ="MOD_WIREFRAME")

        else:  
           
            box = col.box().column(1)
            
            row = box.row(1)                        
            row.prop(tp_props, "display_symdim", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("AutoSym") 
                                   
            if scene.tp_sym_default == True:
                row.prop(scene, "tp_sym_default", text="", icon ="PAUSE")              
            else:             
                row.prop(scene, "tp_mirror", text="", icon ="MOD_MIRROR")   
                if scene.tp_mirror == True:
                    row.prop(scene, "tp_apply", text="", icon ="FILE_TICK")                     
                else:
                    pass
           
            if context.mode == 'SCULPT':
                row.prop(scene, "tp_sculpt", text="", icon ="SCULPTMODE_HLT")   
            else:
                row.prop(scene, "tp_edit", text="", icon ="EDIT")                  
            row.operator("tp_ops.mods_positiv_x_symcut", text="", icon ="MOD_WIREFRAME")


            box = col.box().column(1)                
                               
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
            row.operator("tp_ops.mods_negativ_xyz_symcut", text="+XYZ")          
            row.operator("tp_ops.mods_positiv_xyz_symcut", text="-XYZ")
            
            if context.mode == 'EDIT_MESH':
                row.operator("tp_ops.normal_symcut", text="Normal")
           

            box.separator()  
      
            row = box.row(1) 
            row.prop(scene, "tp_sym_default", text="use symmetize", icon ="PAUSE")  

            row = box.row(1) 
            sub = row.row(1)
            sub.scale_x = 0.5           
            sub.prop(scene, "tp_sculpt", text="Sculpt", icon ="SCULPTMODE_HLT")   
            sub.prop(scene, "tp_edit", text="Edit", icon ="EDIT")    

            box.separator() 

            is_mirror = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'MIRROR' :
                    is_mirror = True
            
            if is_mirror == True:

                row = box.row()  
                row.alignment = 'CENTER'              
                row.prop(bpy.context.active_object.modifiers["Mirror"], "show_viewport", text="")                                                                     
                
                obj = context.active_object
                if obj.mode in {'EDIT'}:                
                    row.operator("tp_ops.mods_edit","", icon='EDITMODE_HLT')                                                    
                    row.operator("tp_ops.mods_cage","", icon='OUTLINER_OB_MESH')                 

                row.operator("tp_ops.remove_mods_mirror", text="", icon='X') 
                row.operator("tp_ops.apply_mods_mirror", text="", icon='FILE_TICK')

                box.separator()      

                for mode in bpy.context.object.modifiers :
                    if mode.type == 'MIRROR' :              
                        if mode.use_mirror_merge is True:                              
                            row = box.row()  
                            row.alignment = 'CENTER'              
                            row.prop(bpy.context.active_object.modifiers["Mirror"], "merge_threshold", text="Merge")           
                            box.separator()  
