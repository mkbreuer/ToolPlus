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



def draw_mods_history_layout(self, context, layout):
    tp_props = context.window_manager.tp_collapse_menu_modifier     

    icons = load_icons()

    col = layout.column(align=True)        
    
    Display_RemoveType = context.user_preferences.addons[__package__].preferences.tab_remove_type    

    if Display_RemoveType == True:

        obj = context.active_object
        if obj:
            mod_list = obj.modifiers
            if mod_list:
                
                box = col.box().column(1)  
               
                box.separator()    
               
                row = box.row(1)
                row.prop(context.scene, "tp_mods_type", text="")
                row.operator("tp_ops.mods_by_type", text="Remove Type")                           
               
                box.separator()   
    else:
        pass

    box = col.box().column(1)  
    
    row = box.row(1)
    if tp_props.display_options:            
        row.prop(tp_props, "display_options", text="", icon="SCRIPTWIN")
    else:
        row.prop(tp_props, "display_options", text="", icon="SCRIPTWIN")                     

    button_ruler = icons.get("icon_ruler") 
    row.operator("view3d.ruler", text="Ruler", icon_value=button_ruler.icon_id)  
 
    row.operator("ed.undo", text="", icon="FRAME_PREV")            
    row.operator("ed.undo_history", text="", icon ="COLLAPSEMENU")
    row.operator("ed.redo", text="", icon="FRAME_NEXT") 
   
    if tp_props.display_options: 

        panel_prefs = context.user_preferences.addons[__package__].preferences

        box = col.box().column(1)  
        box.separator()                 

        row = box.column(1)
        row.label( text="Location: Main Panel")      

        row = box.row()
        row.prop(panel_prefs, 'tab_location', expand = True)                

        row = box.row()
        row.prop(panel_prefs, 'tools_category', text="")                       
     
        box.separator()  
       
        display_icon_type = context.user_preferences.addons[__package__].preferences.tab_location_icons        
        if display_icon_type == 'icons':
          
            row = box.row()
            row.prop(panel_prefs, 'tab_location_icons', expand = True)      

        else:
            
            row = box.row(1)
            if tp_props.display_options_panel:            
                row.prop(tp_props, "display_options_panel", text="", icon="SCRIPTWIN")
            else:
                row.prop(tp_props, "display_options_panel", text="", icon="SCRIPTWIN")   

            row.prop(panel_prefs, 'tab_location_icons', expand = True)      
                
            if tp_props.display_options_panel:               
                box.separator()   

                row = box.row(1)
                row.label("Tools in Panel")

                row = box.column_flow(2)
                row.prop(panel_prefs, 'tab_title', text="Title")
                row.prop(panel_prefs, 'tab_pivot', text="Pivot")
                row.prop(panel_prefs, 'tab_autosym', text="AutoSym")
                row.prop(panel_prefs, 'tab_mirror', text="Mirror")
                row.prop(panel_prefs, 'tab_bevel', text="Bevel")
                row.prop(panel_prefs, 'tab_subsurf', text="SubSurf")
                row.prop(panel_prefs, 'tab_solidify', text="Solidify")
                row.prop(panel_prefs, 'tab_simple', text="Deform")
                row.prop(panel_prefs, 'tab_cast', text="Cast")
                row.prop(panel_prefs, 'tab_screw', text="Screw")
                row.prop(panel_prefs, 'tab_lattice', text="Lattice")
                row.prop(panel_prefs, 'tab_multires', text="MultiRes")
                row.prop(panel_prefs, 'tab_decimate', text="Decimate")
                row.prop(panel_prefs, 'tab_remesh', text="Remesh")
                row.prop(panel_prefs, 'tab_smooth', text="Smooth")
                row.prop(panel_prefs, 'tab_array', text="Array")
                row.prop(panel_prefs, 'tab_transform', text="Transform")
                row.prop(panel_prefs, 'tab_shade', text="Shading")
                row.prop(panel_prefs, 'tab_modcopy', text="Copy")
                row.prop(panel_prefs, 'tab_remove_type', text="Remove")


        box.separator()                 
        box.separator()                 

        row = box.column(1)
        row.label( text="Location: Modifier Stack")      
        
        row = box.row()            
        if tp_props.display_options_stack:            
            row.prop(tp_props, "display_options_stack", text="", icon="SCRIPTWIN")
        else:
            row.prop(tp_props, "display_options_stack", text="", icon="SCRIPTWIN")   
        
        row.prop(panel_prefs, 'tab_location_stack', expand = True)                

        row = box.row()

        row.prop(panel_prefs, 'tools_category_stack', text="")   
          
        if tp_props.display_options_stack: 
            
            row = box.row()
            row.prop(panel_prefs, 'tab_stack_copy', text="CopyTo")
            row.prop(panel_prefs, 'tab_stack_remove', text="Remove Type")       
       
       
        box.separator()                 
        box.separator()    


        row = box.row(1)
        row.label("Location: Modifier Properties")
     
        row = box.row(1)
        if tp_props.display_options_submenu:            
            row.prop(tp_props, "display_options_submenu", text="", icon="SCRIPTWIN")
        else:
            row.prop(tp_props, "display_options_submenu", text="", icon="SCRIPTWIN")   

        row.prop(panel_prefs, 'tab_submenu_modifier', expand = True)                

        if tp_props.display_options_submenu:  
            
            row = box.row()
            row.prop(panel_prefs, 'tab_props_copy', text="CopyTo")
            row.prop(panel_prefs, 'tab_props_remove', text="Remove Type")

 
        box.separator()                   
        box.separator()                   

        row = box.row(1)
        row.label("Tools in Menu [SHIFT+V]")
     
        row = box.row(1)
        if tp_props.display_options_menu:            
            row.prop(tp_props, "display_options_menu", text="", icon="SCRIPTWIN")
        else:
            row.prop(tp_props, "display_options_menu", text="", icon="SCRIPTWIN")                     

        row.prop(panel_prefs, 'tab_menu_modifier', expand = True)                
                
        if tp_props.display_options_menu:  
            
            row = box.column_flow(2)
            row.prop(panel_prefs, 'tab_add_menu', text="Add")
            row.prop(panel_prefs, 'tab_modifier_menus', text="Modifier")
            row.prop(panel_prefs, 'tab_modcopy_menu', text="Copy")                
            row.prop(panel_prefs, 'tab_autosym_menu', text="AutoSym")                
            row.prop(panel_prefs, 'tab_modstack_menu', text="Stack")
            row.prop(panel_prefs, 'tab_clear_menu', text="Clear")
            row.prop(panel_prefs, 'tab_hover_menu', text="Hover")         
     
        box.separator()                             
        box.separator()                             

        row = box.row(1)    
        wm = context.window_manager    
        row.operator("wm.save_userpref", icon='FILE_TICK')  

        box.separator()   


