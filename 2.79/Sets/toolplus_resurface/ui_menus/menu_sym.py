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


class VIEW3D_TP_SymDim_Menu(bpy.types.Menu):
    bl_label = "SymDim"
    bl_idname = "VIEW3D_TP_SymDim_Menu"   

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'        

        icons = load_icons()


        display_vertical = context.user_preferences.addons[__package__].preferences.tab_vertical_menu
        if display_vertical == 'on':
            

            split = layout.split()

            col = split.column()      
            col.operator("tp_ops.mods_positiv_x_symcut", text="+X")
            col.operator("tp_ops.mods_positiv_y_symcut", text="+Y")
            col.operator("tp_ops.mods_positiv_z_symcut", text="+Z")

            col.operator("tp_ops.mods_negativ_xy_symcut", text="+Xy")
            col.operator("tp_ops.mods_negativ_xz_symcut", text="+Xz")
            col.operator("tp_ops.mods_negativ_yz_symcut", text="+Yz")

            col.operator("tp_ops.mods_positiv_xyz_symcut", text="+XYZ")          
           
            if context.mode == 'EDIT_MESH':
                col.label(text="Direction:")

            is_mirror = False            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'MIRROR' :
                    is_mirror = True            
            if is_mirror == True:
              
                col.separator()       
                col.operator("tp_ops.remove_mod_mirror", text="Remove", icon='X') 

       
            col.separator()     
            col.prop(context.scene, "tp_edit", text="Edit", icon ="EDIT")   
            col.prop(context.scene, "tp_sculpt", text="Sculpt", icon ="SCULPTMODE_HLT")   

            col.separator()  
            button_remove = icons.get("icon_remove")
            col.operator("tp_ops.remove_doubles", text="Del.Doubles",icon_value=button_remove.icon_id)                 
          

            col = split.column()             
            col.operator("tp_ops.mods_negativ_x_symcut", text="-- X")
            col.operator("tp_ops.mods_negativ_y_symcut", text="-- Y")
            col.operator("tp_ops.mods_negativ_z_symcut", text="-- Z")
           
            col.operator("tp_ops.mods_positiv_xy_symcut", text="-- Xy")
            col.operator("tp_ops.mods_positiv_xz_symcut", text="-- Xz")
            col.operator("tp_ops.mods_positiv_yz_symcut", text="-- Yz")
  
            col.operator("tp_ops.mods_negativ_xyz_symcut", text="-XYZ")

            if context.mode == 'EDIT_MESH':
                col.operator("tp_ops.normal_symcut", text="Normal")

                     
            is_mirror = False            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'MIRROR' :
                    is_mirror = True
            
            if is_mirror == True:
                
                col.separator()   
                col.operator("tp_ops.apply_mod_mirror", text="Apply", icon='FILE_TICK')      

            
            col.separator()              
            col.prop(context.scene, "tp_mirror", text="Mirror", icon ="MOD_MIRROR")   
            col.prop(context.scene, "tp_apply", text="Apply", icon ="FILE_TICK")   
                            
            col.separator()  
            button_recalc = icons.get("icon_recalc")                 
            col.operator("mesh.normals_make_consistent", text="Recalc.",icon_value=button_recalc.icon_id)   

            
        else:                


            split = layout.split()

            col = split.column()      
            col.operator("tp_ops.mods_positiv_x_symcut", text="+X")
            col.operator("tp_ops.mods_positiv_y_symcut", text="+Y")
            col.operator("tp_ops.mods_positiv_z_symcut", text="+Z")

            col = split.column()             
            col.operator("tp_ops.mods_negativ_x_symcut", text="-- X")
            col.operator("tp_ops.mods_negativ_y_symcut", text="-- Y")
            col.operator("tp_ops.mods_negativ_z_symcut", text="-- Z")
            
     
            col = layout.column(1)

            col = split.column()            
            col.operator("tp_ops.mods_negativ_xy_symcut", text="+Xy")
            col.operator("tp_ops.mods_negativ_xz_symcut", text="+Xz")
            col.operator("tp_ops.mods_negativ_yz_symcut", text="+Yz")

            col = split.column()            
            col.operator("tp_ops.mods_positiv_xy_symcut", text="-- Xy")
            col.operator("tp_ops.mods_positiv_xz_symcut", text="-- Xz")
            col.operator("tp_ops.mods_positiv_yz_symcut", text="-- Yz")


            col = layout.column(1)

            col = split.column()             
            col.operator("tp_ops.mods_positiv_xyz_symcut", text="+XYZ")          
           
            if context.mode == 'EDIT_MESH':
                col.label(text="Direction:")

            col = split.column()  
            col.operator("tp_ops.mods_negativ_xyz_symcut", text="-XYZ")

            if context.mode == 'EDIT_MESH':
                col.operator("tp_ops.normal_symcut", text="Normal")

                     
            is_mirror = False
            
            for mode in bpy.context.object.modifiers :
                if mode.type == 'MIRROR' :
                    is_mirror = True
            
            if is_mirror == True:
                
                col = layout.row(1)

                col = split.column()    
                col.operator("tp_ops.remove_mod_mirror", text="Remove", icon='X') 
                col.operator("tp_ops.apply_mod_mirror", text="Apply", icon='FILE_TICK')
                

