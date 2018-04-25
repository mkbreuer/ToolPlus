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


# PROPERTIES: TAB MODIFIER #
def submenu_func_modifier(self, context):
    if (context.active_object):
        if (len(context.active_object.modifiers)):

            col = self.layout.column(1)

            Display_RemoveType = context.user_preferences.addons[__package__].preferences.tab_remove_type    
            Display_toall = context.user_preferences.addons[__package__].preferences.tab_toall

            if Display_RemoveType == True or Display_toall == True:

                obj = context.active_object
                if obj:
                    mod_list = obj.modifiers
                    if mod_list:
                        
                        box = col.box().column(1)  
                        
                        row = box.row(1)
                                     
                        if Display_RemoveType == True:

                            row = box.row(1)
                            row.prop(context.scene, "tp_mods_type", text="")
                            row.operator("tp_ops.mods_by_type", text="Remove Type")                           

                        if Display_toall == True:         
                            if context.mode == 'OBJECT':

                                row = box.row(1)
                                row.operator("scene.to_all", text="2-Childs", icon='LINKED').mode = "modifier, children"    
                                row.operator("scene.to_all", text="2-Selected", icon='RESTRICT_SELECT_OFF').mode = "modifier, selected"

            else:
                pass
            
            row = col.row(1)
            row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF')                                                                       
            row.operator("object.toggle_apply_modifiers_view", text=" ", icon='RESTRICT_VIEW_OFF') 
            row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
            row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  
            
            if context.mode == 'OBJECT':
                row.operator("object.apply_all_modifiers", text=" ", icon='FILE_TICK') 
            else:
                row.operator("tp_ops.apply_mod", text=" ", icon='FILE_TICK') 
               
            row.operator("object.delete_all_modifiers", text=" ", icon='X')   
            row.operator("wm.toggle_all_show_expanded", text=" ", icon='FULLSCREEN_ENTER') 
      
            col.separator()



# UI: SUB MENU # 
def update_submenu_modifier(self, context):

    try:                
        bpy.types.DATA_PT_modifiers.remove(submenu_func_modifier)                   
    except:
        pass

    if context.user_preferences.addons[__package__].preferences.tab_submenu_modifier == 'win':
        bpy.types.DATA_PT_modifiers.prepend(submenu_func_modifier)

    if context.user_preferences.addons[__package__].preferences.tab_submenu_modifier == 'off':
        pass

