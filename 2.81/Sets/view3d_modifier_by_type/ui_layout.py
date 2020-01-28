# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2020 MKB
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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


def get_addon_props():
    addon_global_props = bpy.context.window_manager.global_props_modbytype
    return (addon_global_props)


# DRAW UI LAYOUT #
def draw_modifier_by_type_ui(self, context, layout):
  
    addon_prefs = context.preferences.addons[__package__].preferences         
    global_props = get_addon_props()         
   
    layout.scale_y = addon_prefs.ui_scale_y   
 
    box = layout.box().column(align=True) 

    view_layer = bpy.context.view_layer
    selected = bpy.context.selected_objects
    for obj in selected:
        if obj:                
            mod_list = obj.modifiers
            if mod_list:
                
                contx = bpy.context.copy()
                contx['object'] = obj    
                
                for mod in mod_list: 
                    contx['modifier'] = mod
                    name = contx['modifier'].name    
               
                mod = mod_list[name]

                if mod.show_render == True:
                    ico_render = 'RESTRICT_RENDER_OFF'
                else:
                    ico_render = 'RESTRICT_RENDER_ON' 
          
                if mod.show_viewport == True:
                    ico_viewport = 'RESTRICT_VIEW_OFF'
                else:
                    ico_viewport = 'RESTRICT_VIEW_ON'

                if mod.show_viewport == True:
                    ico_viewport = 'RESTRICT_VIEW_OFF'
                else:
                    ico_viewport = 'RESTRICT_VIEW_ON'  

                if mod.show_in_editmode == True:
                    ico_editmode = 'EDITMODE_HLT'
                else:
                    ico_editmode = 'EDITMODE_HLT'

                if mod.show_on_cage == True:
                    ico_cage = 'MESH_DATA'
                else:
                    ico_cage = 'MESH_DATA'    


                if addon_prefs.toggle_display_name == False:         
                    txt_unhide  = " "
                    txt_edit    = " "
                    txt_cage    = " "
                    txt_up      = " "
                    txt_down    = " "
                    txt_stack   = " "
                    txt_render  = " "
                    txt_remove  = " "
                    txt_apply   = " "
                
                else: 
                    txt_unhide  = "(Un)Hide"
                    txt_edit    = "Edit"
                    txt_cage    = "Cage"
                    txt_up      = "Up"
                    txt_down    = "Down"
                    txt_stack   = "Expanded"
                    txt_render  = "Render"
                    txt_remove  = "Remove"
                    txt_apply   = "Apply"
     
     
                if addon_prefs.toggle_display_custom1 == True:
                    box.separator()
         
                    row = box.row(align=True)        
                    if addon_prefs.toggle_display_name == True:
                        row.label(text="Custom:")   
                    row.prop(global_props, "mod_string", text="")
                
                box.separator()
     
                row = box.row(align=True)        
                if addon_prefs.toggle_display_name == True:
                    row.label(text="Modifier:")   
                row.prop(global_props, "mod_list", text="")

                box.separator()

                if addon_prefs.toggle_layout_type == 'type_a':
                
                    row = box.row(align=True)
                    if addon_prefs.toggle_display_name == True:
                        row.label(text="Process:") 
                    row.prop(global_props, "mod_processing", text="")

                    box.separator()

                    row = box.row(align=True)
                    if addon_prefs.toggle_display_name == True:
                        row.label(text="Execute:") 
                    row.operator("tpc_ot.modifier_by_type", text="Run", icon='FRAME_NEXT')       


                if addon_prefs.toggle_layout_type == 'type_b':
                
                    row = box.row(align=True)               
                    row.prop_enum(global_props, "mod_processing", "UNHIDE", text=txt_unhide, icon=ico_viewport)         
                    row.prop_enum(global_props, "mod_processing", "EDIT", text=txt_edit, icon=ico_editmode)       
                    row.prop_enum(global_props, "mod_processing", "CAGE", text=txt_cage, icon=ico_cage)       
     
                    row = box.row(align=True)      
                    row.prop_enum(global_props, "mod_processing", "UP", text=txt_up, icon='TRIA_UP')       
                    row.prop_enum(global_props, "mod_processing", "DOWN", text=txt_down, icon='TRIA_DOWN')                        
                    row.prop_enum(global_props, "mod_processing", "STACK", text=txt_stack, icon='FULLSCREEN_ENTER')       

                    row = box.row(align=True) 
                    row.prop_enum(global_props, "mod_processing", "RENDER", text=txt_render, icon=ico_render)          
                    row.prop_enum(global_props, "mod_processing", "REMOVE", text=txt_remove, icon='PANEL_CLOSE')       
                    row.prop_enum(global_props, "mod_processing", "APPLY", text=txt_apply, icon='CHECKMARK')       

                    box.separator()

                    row = box.row(align=True)
                    row.operator("tpc_ot.modifier_by_type", text="Run", icon='FRAME_NEXT')  


                if addon_prefs.toggle_layout_type == 'type_c':

                    row = box.row(align=True)
                   
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_unhide, icon=ico_viewport)       
                    props.mod_processing='UNHIDE'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_edit, icon=ico_editmode)       
                    props.mod_processing='EDIT'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_cage, icon=ico_cage)       
                    props.mod_processing='CAGE'
                    props.mod_list=global_props.mod_list

                    row = box.row(align=True) 
         
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_up, icon='TRIA_UP')       
                    props.mod_processing='UP'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_down, icon='TRIA_DOWN')       
                    props.mod_processing='DOWN'
                    props.mod_list=global_props.mod_list         
                 
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_stack, icon='FULLSCREEN_ENTER')       
                    props.mod_processing='STACK'
                    props.mod_list=global_props.mod_list

                    row = box.row(align=True) 

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_render, icon=ico_render)          
                    props.mod_processing='RENDER'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_remove, icon='PANEL_CLOSE')       
                    props.mod_processing='REMOVE'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_apply, icon='CHECKMARK')       
                    props.mod_processing='APPLY'
                    props.mod_list=global_props.mod_list


                if addon_prefs.toggle_layout_type == 'type_d':

                    row = box.column(align=True)
                 
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_stack, icon='FULLSCREEN_ENTER')       
                    props.mod_processing='STACK'
                    props.mod_list=global_props.mod_list

                    row.separator() 
                   
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_render, icon=ico_render)          
                    props.mod_processing='RENDER'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_unhide, icon=ico_viewport)       
                    props.mod_processing='UNHIDE'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_edit, icon=ico_editmode)       
                    props.mod_processing='EDIT'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_cage, icon=ico_cage)       
                    props.mod_processing='CAGE'
                    props.mod_list=global_props.mod_list

                    row.separator() 

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_up, icon='TRIA_UP')       
                    props.mod_processing='UP'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_down, icon='TRIA_DOWN')       
                    props.mod_processing='DOWN'
                    props.mod_list=global_props.mod_list         

                    row.separator() 

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_remove, icon='PANEL_CLOSE')       
                    props.mod_processing='REMOVE'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_apply, icon='CHECKMARK')       
                    props.mod_processing='APPLY'
                    props.mod_list=global_props.mod_list
                
     
                if addon_prefs.toggle_layout_type == 'type_e':

                    row = box.row(align=True)
                   
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_stack, icon='FULLSCREEN_ENTER')       
                    props.mod_processing='STACK'
                    props.mod_list=global_props.mod_list

                    row.separator()            
                
                    props = row.operator("tpc_ot.modifier_by_type", text=txt_render, icon=ico_render)          
                    props.mod_processing='RENDER'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_unhide, icon=ico_viewport)       
                    props.mod_processing='UNHIDE'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_edit, icon=ico_editmode)       
                    props.mod_processing='EDIT'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_cage, icon=ico_cage)       
                    props.mod_processing='CAGE'
                    props.mod_list=global_props.mod_list

                    row.separator()   

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_up, icon='TRIA_UP')       
                    props.mod_processing='UP'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_down, icon='TRIA_DOWN')       
                    props.mod_processing='DOWN'
                    props.mod_list=global_props.mod_list         
                 

                    row.separator()   

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_remove, icon='PANEL_CLOSE')       
                    props.mod_processing='REMOVE'
                    props.mod_list=global_props.mod_list

                    props = row.operator("tpc_ot.modifier_by_type", text=txt_apply, icon='CHECKMARK')       
                    props.mod_processing='APPLY'
                    props.mod_list=global_props.mod_list



                box.separator()
            else:
                row = box.row(align=True)        
                row.label(text="No modifier found!")

    
    col = layout.row(align=True)
    col.scale_y = 0.60 
    col.operator("preferences.addon_show", text=" ", icon="LAYER_USED").module="view3d_modifier_by_type"
    #layout.popover(panel="VIEW3D_OT_modifier_by_type_panel_ui", text="Menu Panel")  

