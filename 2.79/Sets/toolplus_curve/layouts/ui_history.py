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


# DRAW UI LAYOUT #
def draw_history_ui(self, context, layout):

    layout.operator_context = 'INVOKE_REGION_WIN'                                  
    
    tp_props = context.window_manager.tp_props_curve        
   
    icons = load_icons()

    col = layout.column(1)  
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
 
        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences

        box.separator()  

        row = box.row(1)
        row.prop(panel_prefs, 'tab_location_option_switch', expand = True)          

        box.separator()                
        
        box = col.box().column(1) 

        box.separator()   

        if context.user_preferences.addons[addon_key].preferences.tab_location_option_switch == 'panels':

            row = box.row(1)
            row.label( text="Panel Layout", icon="RIGHTARROW_THIN")    
            row.operator("tp_ops.help_curve_prefs", text="", icon='INFO')  

            box.separator()  

            row = box.row(1) 
            row.prop(panel_prefs, 'tab_panel_layout', expand = True)   

            if context.user_preferences.addons[addon_key].preferences.tab_panel_layout == 'compact':
         
                box.separator()  
                
                row = box.row(1) 
                row.prop(panel_prefs, 'tab_panel_layout_type', expand = True)   
                
               
                if context.user_preferences.addons[addon_key].preferences.tab_panel_layout_type == 'type_two':
                
                    box.separator()  
                   
                    row = box.row(1) 
                    row.prop(panel_prefs, 'tab_panel_layout_expand', expand = True)   
                
                else:                   
                    box.separator()                      
                   
                    row = box.row(1) 
                    row.prop(panel_prefs, 'tab_panel_layout_custom', expand = True)   


            box.separator()                 

            row = box.column(1)
            row.label( text="Panel Location", icon="ARROW_LEFTRIGHT")      

            box.separator()  

            row = box.row(1)
            row.prop(panel_prefs, 'tab_panel_location', expand = True)          

            box.separator()   

            row = box.row(1)
            row.prop(panel_prefs, 'tools_category_location', text="TAB")                       
           
            box.separator()                 

            box.separator()                 

            row = box.row(1)
            row.label( text="Panel Custom", icon="ARROW_LEFTRIGHT")      
            row.operator("tp_ops.help_curve_custom", text="", icon='INFO')  
          
            box.separator()  

            row = box.row(1)
            row.prop(panel_prefs, 'tab_location_custom', expand = True)          

            box.separator()   
            
            row = box.row(1)
            row.prop(panel_prefs, 'tools_category_custom', text="TAB")                       
            row.operator("tp_ops.keymap_curve_custom", text="", icon="SCRIPT")     
           
            box.separator()    

       
        if context.user_preferences.addons[addon_key].preferences.tab_location_option_switch == 'menus':
            
            row = box.row(1)
            row.label( text="Shortcut Menu", icon="RIGHTARROW_THIN")    
            row.operator("tp_ops.help_curve_prefs", text="", icon='INFO')  
            
            box.separator()   
            
            row = box.row(1)                   
            row.prop(panel_prefs, 'tab_menu_curve', expand=True)

            box.separator() 
            box.separator() 
            box.separator() 

            row = box.row(1)
            row.label( text="Append Extra Menus", icon="RIGHTARROW_THIN")    
            row.operator("tp_ops.help_curve_append", text="", icon='INFO')  
            
            box.separator()   
            
            row = box.row(1)            
            row.prop(panel_prefs, 'tab_menu_append', expand=True)
           
            box.separator()
                       
            row = box.column_flow(2)          
            row.prop(panel_prefs, 'tab_append_add')
            #row.prop(panel_prefs, 'tab_append_special')
            row.prop(panel_prefs, 'tab_append_delete')
            row.prop(panel_prefs, 'tab_append_import')
            row.prop(panel_prefs, 'tab_append_editors')

            box.separator()    
  

        if context.user_preferences.addons[addon_key].preferences.tab_location_option_switch == 'tools':
 
            box.separator()
            
            row = box.row(1)
            row.label(text="Panel", icon="RIGHTARROW_THIN")
            row.operator("tp_ops.help_curve_prefs", text="", icon='INFO')                              
           
            row = box.row()       
            row.prop(panel_prefs, 'curve_primitiv')
            
            box.separator()  
            box.separator()  

            row = box.row(1)
            row.label( text="Menu", icon="RIGHTARROW_THIN")     
            row.operator("tp_ops.help_curve_prefs", text="", icon='INFO')    
          
            row = box.column()       
            row.prop(panel_prefs, 'tab_showhide')
            
            box.separator()  


        box.separator()    

        box = col.box().column(1) 

        box.separator()    
                       
        row = box.row(1)  
        row.scale_y = 1.3
        wm = context.window_manager 
        row.operator("wm.restart_blender", text="Restart", icon='RECOVER_AUTO')  
        row.operator("wm.save_userpref", text="Save", icon='FILE_TICK')          

        box.separator()  




class VIEW3D_TP_Curve_History_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Curve"
    bl_idname = "VIEW3D_TP_Curve_History_Panel_TOOLS"
    bl_label = "History"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
         
        draw_history_ui(self, context, layout)


         
class VIEW3D_TP_Curve_History_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Curve_History_Panel_UI"
    bl_label = "History"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        if len(context.selected_objects) > 0:
            obj = context.active_object
            return obj != None and obj.type == 'CURVE' and isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
         
        draw_history_ui(self, context, layout)                              

