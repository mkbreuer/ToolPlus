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
        
        layout.scale_y = 1.3

        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        Display_Add = context.user_preferences.addons[__package__].preferences.tab_add_menu 
        if Display_Add == True: 

            layout.operator_menu_enum("object.modifier_add", "type", text="New", icon='MODIFIER')            

        layout.menu("tp_menu.modifier_visual", text="Visual", icon='RESTRICT_VIEW_OFF')


        Display_Modi_Menus = context.user_preferences.addons[__package__].preferences.tab_modifier_menus 
        if Display_Modi_Menus == True:

            if context.mode =='SCULPT':            
                   
                    layout.separator()
                   
                    layout.menu("tp_menu.modifier_subsurf", text="MultiRes", icon='MOD_MULTIRES')

            else:

                layout.separator()
                
                layout.menu("tp_menu.modifier_subsurf", text="SubSurf", icon='MOD_SUBSURF')
                layout.menu("tp_menu.modifier_array", text="Array", icon='MOD_ARRAY')
                layout.menu("tp_menu.modifier_mirror", text="Mirror", icon='MOD_MIRROR')


        Display_AutoSym = context.user_preferences.addons[__package__].preferences.tab_autosym_menu 
        if Display_AutoSym == True:   

            layout.separator()

            layout.menu("tp_menu.modifier_autosym", text="AutoSym", icon='MOD_WIREFRAME')
            layout.menu("tp_menu.modifier_autosym_opt", text="Options", icon='SCRIPTWIN')
            
            
        Display_ModCopy = context.user_preferences.addons[__package__].preferences.tab_modcopy_menu
        if Display_ModCopy == True:
            
            if context.mode == 'OBJECT':  
               
                layout.separator()        

                layout.menu("tp_menu.modcopy", text="CopyTo", icon = 'PASTEFLIPDOWN')  


        Display_ModStack = context.user_preferences.addons[__package__].preferences.tab_modstack_menu 
        if Display_ModStack == True:

            layout.separator()

            layout.operator("tp_batch.modifier_stack", text="Modifier Stack", icon = 'COLLAPSEMENU')  


        Display_Apply = context.user_preferences.addons[__package__].preferences.tab_clear_menu 
        if Display_Apply == True:
            
            layout.separator()            
           
            layout.operator("tp_ops.remove_mod", icon = 'X', text="Delete all")
            layout.operator("tp_ops.apply_mod", icon = 'FILE_TICK', text="Apply all")
        

        Display_Hover = context.user_preferences.addons[__package__].preferences.tab_hover_menu 
        if Display_Hover == True:
            
            layout.separator()

            layout.operator("wm.toggle_all_show_expanded", icon = 'FULLSCREEN_ENTER', text="Expand Toggle")  

        
         
class VIEW3D_TP_Display_ModCopy(bpy.types.Menu):
    bl_label = "ModCopy"
    bl_idname = "tp_menu.modcopy"
    
    def draw(self, context):
        layout = self.layout
 
        icons = load_icons()

        split = layout.split()

        col = split.column()

        col.scale_y = 1.2
       
        button_mods_append = icons.get("icon_mods_append") 
        col.label("Append to", icon_value=button_mods_append.icon_id)  
        
        col.operator("tp_ops.to_all", text="Childs").mode = "modifier, children, append"    
        col.operator("tp_ops.to_all", text="Selected").mode = "modifier, selected, append"
       
        col.separator()   
     
        col.label(text="Select Type:")

        col = split.column()
            
        col.scale_y = 1.2
        
        button_mods_copy = icons.get("icon_mods_copy")        
        col.label("Copy to", icon_value=button_mods_copy.icon_id)  

        col.operator("tp_ops.to_all", text="Childs").mode = "modifier, children"    
        col.operator("tp_ops.to_all", text="Selected").mode = "modifier, selected"
       
        col.separator()   

        col.operator("object.copy_selected_modifiers", text="Copy")



class VIEW3D_TP_Display_Modifier_SubSurf(bpy.types.Menu):
    bl_label = "Subsurf / MultiRes"
    bl_idname = "tp_menu.modifier_subsurf"
    
    def draw(self, context):
        layout = self.layout
 
        icons = load_icons()

        split = layout.split()

        col = split.column()

        col.scale_y = 1.2

        if context.mode =='SCULPT':            
            col.operator("tp_ops.multires_add", text="Add", icon="DISCLOSURE_TRI_RIGHT")   
        else:
            col.label("View", icon="MOD_SUBSURF")      
                          
        col.separator() 
 
        col.operator("tp_ops.subsurf_1")
        col.operator("tp_ops.subsurf_2")            
        col.operator("tp_ops.subsurf_3")
       
        col.separator()        
       
        if context.mode =='SCULPT':   
            col.operator("tp_ops.remove_mods_multires", text="Rem." , icon='PANEL_CLOSE')  
        else:       
            col.operator("tp_ops.remove_mods_subsurf", text="Rem." , icon='PANEL_CLOSE')   

        col = split.column()
            
        col.scale_y = 1.2
       
        col.operator("tp_ops.subsurf_0")          
                  
        col.separator()

        col.operator("tp_ops.subsurf_4")
        col.operator("tp_ops.subsurf_5")
        col.operator("tp_ops.subsurf_6")

        col.separator()

        button_apply = icons.get("icon_apply")                              

        if context.mode =='SCULPT':   
            col.operator("tp_ops.apply_mods_multires", text="Apply", icon_value=button_apply.icon_id)             
        else:
            col.operator("tp_ops.apply_mods_subsurf", text="Apply", icon_value=button_apply.icon_id)     




class VIEW3D_TP_Display_Modifier_Mirror(bpy.types.Menu):
    bl_label = "Mirror Modifier"
    bl_idname = "tp_menu.modifier_mirror"
    
    def draw(self, context):
        layout = self.layout

        icons = load_icons()
       
        split = layout.split()
        
        col = split.column()

        col.scale_y = 1.2
        
        col.label("1-Axis", icon="MANIPUL")       
       
        col.operator("tp_ops.mod_mirror_x", text="X")
        col.operator("tp_ops.mod_mirror_y", text="Y")
        col.operator("tp_ops.mod_mirror_z", text="Z")

        col.separator()
        
        col.label("3-Axis", icon="MANIPUL")        

        col.separator()

        col.operator("tp_ops.remove_mods_mirror", text="Rem." , icon='PANEL_CLOSE')        


        col = split.column()

        col.scale_y = 1.2
       
        col.label("2-Axis", icon="MANIPUL")      
        
        col.operator("tp_ops.mod_mirror_xy", text="XY")
        col.operator("tp_ops.mod_mirror_yz", text="XZ")
        col.operator("tp_ops.mod_mirror_xz", text="YZ")

        col.separator()
        
        col.operator("tp_ops.mod_mirror_xyz", text="XYZ")        
    
        col.separator()
       
        button_apply = icons.get("icon_apply")   
        if context.mode == 'EDIT_MESH': 
            col.operator("tp_ops.apply_mods_mirror_edm", text="Apply", icon_value=button_apply.icon_id)                                                                                                                                               
        else:
            col.operator("tp_ops.apply_mods_mirror", text="Apply", icon_value=button_apply.icon_id)                                                                                                                                               




class VIEW3D_TP_Display_Modifier_Array(bpy.types.Menu):
    bl_label = "Array Modifier"
    bl_idname = "tp_menu.modifier_array"
    
    def draw(self, context):
        layout = self.layout

        icons = load_icons()

        split = layout.split()

        col = split.column()

        col.scale_y = 1.2

        col.label("1-Axis", icon="MANIPUL")
       
        col.operator("tp_ops.x_array", "X")
        col.operator("tp_ops.y_array", "Y")
        col.operator("tp_ops.z_array", "Z")

        col.separator()
       
        col.label("3-Axis", icon="MANIPUL")
       
        col.separator()     
      
        col.operator("tp_ops.remove_mods_array", text="Rem." , icon='PANEL_CLOSE')      

        col = split.column()

        col.scale_y = 1.2

        col.label("2-Axis", icon="MANIPUL")
       
        col.operator("tp_ops.xy_array", "XY")
        col.operator("tp_ops.xz_array", "XZ")
        col.operator("tp_ops.yz_array", "YZ")

        col.separator()

        col.operator("tp_ops.xyz_array", "XYZ")

        col.separator()
       
        button_apply = icons.get("icon_apply")                                                                                                                                                   
        col.operator("tp_ops.apply_mods_array", text="Apply", icon_value=button_apply.icon_id)     



class VIEW3D_TP_Display_Modifier_AutoSym_Menu(bpy.types.Menu):
    bl_label = "AutoSym"
    bl_idname = "tp_menu.modifier_autosym"
    
    def draw(self, context):
        layout = self.layout

        split = layout.split()
        col = split.column()
       
        col.scale_y = 1.2
       
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
     
        col.scale_y = 1.2        
    
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

        layout.scale_y = 1.2

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences    
                   
        layout.prop(panel_prefs, "autosym_mirror", text="add modifier", icon ="MOD_MIRROR")   
        layout.prop(panel_prefs, "autosym_apply", text="apply modifier", icon ="FILE_TICK")                        
        layout.prop(panel_prefs, "autosym_edit", text="stay in editmode", icon ="EDIT")    

        layout.separator() 

        layout.prop(panel_prefs, "autosym_symmetrize", text="use symmetrize", icon ="PAUSE")  
        layout.prop(panel_prefs, "autosym_sculpt", text="stay in sculptmode", icon ="SCULPTMODE_HLT")   
       
        layout.separator()  
        wm = context.window_manager    
        layout.operator("wm.save_userpref", icon='FILE_TICK')  



class VIEW3D_TP_Display_Modifier_Visual(bpy.types.Menu):
    bl_label = "Visual Modifier"
    bl_idname = "tp_menu.modifier_visual"
    
    def draw(self, context):
        layout = self.layout                         
    
        layout.scale_y = 1.2

        layout.operator("tp_ops.mods_view","View", icon = 'RESTRICT_VIEW_OFF')                                                                       
        layout.operator("tp_ops.mods_edit","Edit", icon='EDITMODE_HLT')                                                    
        layout.operator("tp_ops.mods_cage","Cage", icon='OUTLINER_OB_MESH')      
        layout.operator("tp_ops.mods_render","Render", icon = 'RESTRICT_RENDER_OFF') 










