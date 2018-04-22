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
     

class VIEW3D_TP_Modifier_Menu(bpy.types.Menu):
    bl_label = "Modifier"
    bl_idname = "VIEW3D_TP_Modifier_Menu"  
    bl_space_type = 'VIEW_3D'
    
    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        #button_origin_center_view = icons.get("icon_origin_center_view")
        #layout.operator("tp_ops.origin_set_center", text="Center", icon_value=button_origin_center_view.icon_id)
        
        layout.scale_y = 1.3

        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        Display_Add = context.user_preferences.addons[__package__].preferences.tab_add_menu 
        if Display_Add == True: 

            layout.operator_menu_enum("object.modifier_add", "type", text="New", icon='MODIFIER')            



        layout.menu("tp_menu.modifier_visual", text="Visual", icon='RESTRICT_VIEW_OFF')

 
        Display_Modi_Menus = context.user_preferences.addons[__package__].preferences.tab_modifier_menus 
        if Display_Modi_Menus == True: 

            layout.separator()

            layout.menu("tp_menu.modifier_subsurf", text="Subsurf", icon='MOD_SUBSURF')
            layout.menu("tp_menu.modifier_array", text="ArrayAxis", icon='MOD_ARRAY')
            layout.menu("tp_menu.modifier_mirror", text="MirrorAxis", icon='MOD_MIRROR')
        

        Display_ATM = context.user_preferences.addons[__package__].preferences.tab_automirror_menu 
        if Display_ATM == True:   

            layout.separator()

            layout.menu("tp_menu.modifier_autosym", text="AutoSym", icon='MOD_WIREFRAME')
            layout.menu("tp_menu.modifier_autosym_opt", text="Options", icon='SCRIPTWIN')
            

        Display_ModStack = context.user_preferences.addons[__package__].preferences.tab_modstack_menu 
        if Display_ModStack == True:

            layout.separator()

            layout.operator("tp_batch.modifier_stack", text="Modifier Stack", icon = 'COLLAPSEMENU')  


        Display_Apply = context.user_preferences.addons[__package__].preferences.tab_clear_menu 
        if Display_Apply == True:
            
            layout.separator()            
           
            layout.operator("tp_ops.remove_mod", icon = 'X', text="Delete all")

            obj = context.object      
            if obj.mode == 'OBJECT':
                layout.operator("tp_ops.apply_mod", icon = 'FILE_TICK', text="Apply all")
                   
            if obj.mode == 'EDIT':
                layout.operator("tp_ops.apply_mod", icon = 'FILE_TICK', text="Apply all")                


        Display_Hover = context.user_preferences.addons[__package__].preferences.tab_hover_menu 
        if Display_Hover == True:
            
            layout.separator()

            layout.operator("tp_ops.collapse_mod", icon = 'TRIA_RIGHT', text="HoverCollapse")  
            layout.operator("tp_ops.expand_mod", icon = 'TRIA_DOWN', text="HoverExpand")
        
         


class VIEW3D_TP_Display_Modifier_SubSurf(bpy.types.Menu):
    bl_label = "Mirror Subsurf"
    bl_idname = "tp_menu.modifier_subsurf"
    
    def draw(self, context):
        layout = self.layout
       
        layout.operator("tp_ops.subsurf_0")
        layout.operator("tp_ops.subsurf_1")
        layout.operator("tp_ops.subsurf_2")            
        layout.operator("tp_ops.subsurf_3")
        layout.operator("tp_ops.subsurf_4")
        layout.operator("tp_ops.subsurf_5")
        layout.operator("tp_ops.subsurf_6")




class VIEW3D_TP_Display_Modifier_Mirror(bpy.types.Menu):
    bl_label = "Mirror Modifier"
    bl_idname = "tp_menu.modifier_mirror"
    
    def draw(self, context):
        layout = self.layout
       
        split = layout.split()
        col = split.column()
        col.operator("tp_ops.mod_mirror_x", text="X Axis")
        col.operator("tp_ops.mod_mirror_y", text="Y Axis")
        col.operator("tp_ops.mod_mirror_z", text="Z Axis")

        col.separator()
        col.label(text="")   

       
        col = split.column()
        col.operator("tp_ops.mod_mirror_xy", text="XY Axis")
        col.operator("tp_ops.mod_mirror_yz", text="XZ Axis")
        col.operator("tp_ops.mod_mirror_xz", text="YZ Axis")

        col.separator()
        
        col.operator("tp_ops.mod_mirror_xyz", text="XYZ Axis")        




class VIEW3D_TP_Display_Modifier_Array(bpy.types.Menu):
    bl_label = "Array Modifier"
    bl_idname = "tp_menu.modifier_array"
    
    def draw(self, context):
        layout = self.layout

        split = layout.split()
        col = split.column()
        col.operator("tp_ops.x_array", "X Array")
        col.operator("tp_ops.y_array", "Y Array")
        col.operator("tp_ops.z_array", "Z Array")

        col.separator()
       
        col.label(text="")   
      
        col = split.column()
        col.operator("tp_ops.xy_array", "XY Array")
        col.operator("tp_ops.xz_array", "XZ Array")
        col.operator("tp_ops.yz_array", "YZ Array")

        col.separator()

        col.operator("tp_ops.xyz_array", "XYZ Array")



class VIEW3D_TP_Display_Modifier_AutoSym_Menu(bpy.types.Menu):
    bl_label = "AutoSym"
    bl_idname = "tp_menu.modifier_autosym"
    
    def draw(self, context):
        layout = self.layout
        
        split = layout.split()
        col = split.column()

        col.label("Positiv", icon="MOD_WIREFRAME")

        col.operator("tp_ops.mods_positiv_x_symcut", "+X")
        col.operator("tp_ops.mods_positiv_y_symcut", "+Y")
        col.operator("tp_ops.mods_positiv_z_symcut", "+Z")        

        col.separator()

        col.operator("tp_ops.mods_positiv_xy_symcut", "+XY")
        col.operator("tp_ops.mods_positiv_xz_symcut", "+XZ")
        col.operator("tp_ops.mods_positiv_yz_symcut", "+YZ")

        col.separator() 

        col.operator("tp_ops.mods_positiv_xyz_symcut", "+XYZ")


        col = split.column()
        
        col.label("Negative", icon="MOD_WIREFRAME")
                
        col.operator("tp_ops.mods_negativ_x_symcut", "-- X")
        col.operator("tp_ops.mods_negativ_y_symcut", "-- Y")    
        col.operator("tp_ops.mods_negativ_z_symcut", "-- Z")

        col.separator()    

        col.operator("tp_ops.mods_negativ_xy_symcut", "-- XY")
        col.operator("tp_ops.mods_negativ_xz_symcut", "-- XZ")
        col.operator("tp_ops.mods_negativ_yz_symcut", "-- YZ")

        col.separator() 

        col.operator("tp_ops.mods_negativ_xyz_symcut", "-- XYZ")

class VIEW3D_TP_Display_Modifier_AutoSymOpt_Menu(bpy.types.Menu):
    bl_label = "Options"
    bl_idname = "tp_menu.modifier_autosym_opt"
    
    def draw(self, context):
        layout = self.layout
        
        scene = context.scene       
                   
        layout.prop(scene, "tp_mirror", text="add modifier", icon ="MOD_MIRROR")   
        layout.prop(scene, "tp_apply", text="apply modifier", icon ="FILE_TICK")                        
        layout.prop(scene, "tp_edit", text="stay in editmode", icon ="EDIT")    

        layout.separator() 

        layout.prop(scene, "tp_sym_default", text="use symmetrize", icon ="PAUSE")  
        layout.prop(scene, "tp_sculpt", text="stay in sculptmode", icon ="SCULPTMODE_HLT")   
 



class VIEW3D_TP_Display_Modifier_Visual(bpy.types.Menu):
    bl_label = "Visual Modifier"
    bl_idname = "tp_menu.modifier_visual"
    
    def draw(self, context):
        layout = self.layout                         
    
        layout.operator("tp_ops.mods_view","View", icon = 'RESTRICT_VIEW_OFF')                                                                       
        layout.operator("tp_ops.mods_edit","Edit", icon='EDITMODE_HLT')                                                    
        layout.operator("tp_ops.mods_cage","Cage", icon='OUTLINER_OB_MESH')      
        layout.operator("tp_ops.mods_render","Render", icon = 'RESTRICT_RENDER_OFF') 










