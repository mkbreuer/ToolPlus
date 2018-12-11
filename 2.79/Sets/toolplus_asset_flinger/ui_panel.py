# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2018 MKB
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
from . icons.buttons.icons import load_icons


# LOAD KEYMAP #
import rna_keymap_ui
def get_keymap_item(km, kmi_name, kmi_value):
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_name:
            if km.keymap_items[i].properties.name == kmi_value:
                return km_item
    return None

def draw_keymap_item(km, kmi, kc, layout):
    if kmi:
        layout.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, layout, 0)
        
        
# DRAW UI LAYOUT #
class draw_flinger_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return isModelingMode

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()  

        tp_props = context.window_manager.tp_props_assetflinger    

        addon_key = __package__.split(".")[0]    
        panel_prefs = context.user_preferences.addons[addon_key].preferences

        col = layout.column(1)   

        if panel_prefs.tap_display_project: 

            box = col.box().column(1)                         

            box.separator()           
          
            row = box.column(1)

            button_open_project = icons.get("icon_open_project")
            row.operator("view3d.asset_flinger_project", text="Open Project", icon_value=button_open_project.icon_id)               
          
            button_save_project = icons.get("icon_save_project")
            row.operator("export.asset_flinger_project", text="Save to Project", icon_value=button_save_project.icon_id)
            
            box.separator()    
            box.separator()    

        box = col.box().column(1)                         

        box.separator()           
      
        row = box.column(1)
      
        button_open_library = icons.get("icon_open_library")
        row.operator("view3d.asset_flinger", text="Open Library", icon_value=button_open_library.icon_id)
     
        button_save_library = icons.get("icon_save_library")
        row.operator("export.asset_flinger", text="Save to Library", icon_value=button_save_library.icon_id)
        
        box.separator()    
        box.separator()   

        box = col.box().column(1)                         

        box.separator()   

        row = box.row(1)                      
        

        if tp_props.display_settings:   
            row.prop(tp_props, "display_settings", text="Settings", icon="SCRIPTWIN")                 
        else:
            row.prop(tp_props, "display_settings", text="Settings", icon="SCRIPTWIN")     

        row.operator("tp_ops.help_path_settings", text="", icon='INFO')  
       
        box.separator()    
 
        if tp_props.display_settings: 


            box.separator()  

            row = box.row(1)
            row.prop(tp_props, 'display_preferences', expand = True)     

            box.separator()   

            box.separator()             
            box = col.box().column(1)                         
            box.separator()   

            if tp_props.display_preferences =='path': 

                row = box.row(1)
                row.label( text="Project Library Path", icon="FILE_FOLDER")      
                if panel_prefs.tap_display_project:   
                    row.prop(panel_prefs, "tap_display_project", text="", icon="RESTRICT_VIEW_OFF")                 
                else:
                    row.prop(panel_prefs, "tap_display_project", text="", icon="RESTRICT_VIEW_ON")      
                row.operator("tp_ops.help_path_project", text="", icon='INFO')  
                
                box.separator()  

                row = box.row(1)
                row.prop(panel_prefs, 'custom_library_path_project', text="")                              
              
               
                box.separator()   
                box.separator()             
                box.separator() 


                row = box.row(1)
                row.label( text="Asset Library Path", icon="FILE_FOLDER")      
                row.operator("tp_ops.help_path_asset", text="", icon='INFO')  
                
                box.separator()  

                row = box.row(1)
                row.prop(panel_prefs, 'custom_library_path', text="")                              
               
                box.separator()   
                box.separator()             



            if tp_props.display_preferences =='preview': 


                row = box.row(1)
                row.label( text="Thumbnail Color", icon="FILE_IMAGE")    
                row.operator("tp_ops.help_color", text="", icon='INFO')  
                
                box.separator()   
                
                row = box.row(1)                   
                row.prop(panel_prefs, 'render_scene', text="")

                box.separator() 
                box.separator() 
                box.separator() 

                row = box.row(1)
                row.label( text="Thumbnail Size", icon="ZOOM_ALL")    
                row.operator("tp_ops.help_size", text="", icon='INFO')  
                
                box.separator()  
                row = box.row(1)                   
                row.prop(panel_prefs, 'thumbnail_render_size', text="")

                box.separator() 
                box.separator() 



            if tp_props.display_preferences =='ui': 


                row = box.row(1)
                row.label( text="Panel Location", icon="ARROW_LEFTRIGHT")      
                row.operator("tp_ops.help_location", text="", icon='INFO')  
                
                box.separator()  

                row = box.row(1)
                row.prop(panel_prefs, 'tab_location_asset', expand = True)          
      
                if panel_prefs.tab_location_asset == 'tools':

                    box.separator()   
                    
                    row = box.row(1)                     
                    row.prop(panel_prefs, "tools_category_asset", text="TAB")
              
                       
                box.separator()   
                box = col.box().column(1)           
                box.separator()   
                
                box.separator()   
                
                row = box.row(1)
                row.label( text="Input", icon="HAND")    
                row.operator("tp_ops.help_input", text="", icon='INFO')  
                
                box.separator()   
                box.separator()   
                
                row = box.column(1)                                 
                row.prop(panel_prefs, 'tab_keymap_project', text="Keys: Project")                
                row.prop(panel_prefs, 'tab_keymap_asset', text="Keys: Library")                

                box.separator()

                row = box.row(1)
                row.prop(panel_prefs, 'tab_popup_menu', text="Popup Menu")          

                box.separator()

                row = box.row(1)
                row.prop(panel_prefs, 'tab_menu_append', text="Append to Add Menu")
                             
                box.separator()
                
                row = box.column(1)
                row.prop(panel_prefs, 'tab_header_project', text="Header Buttons: Project")
                row.prop(panel_prefs, 'tab_header_library', text="Header Buttons: Library")
                             
                box.separator()                                
                box.separator()



            box.separator()    
            box = col.box().column(1) 
            box.separator()    
                           
            row = box.row(1)  
            row.scale_y = 1.3
            wm = context.window_manager
            row.operator("screen.userpref_show", text="Preferences", icon='PREFERENCES')   
            #row.operator("wm.restart_blender", text="Restart", icon='RECOVER_AUTO')  
            row.operator("wm.save_userpref", text="Save", icon='SAVE_PREFS')          

            box.separator()  




# LOAD UI: PANEL #
class VIEW3D_TP_AssetFlinger_Panel_TOOLS(bpy.types.Panel, draw_flinger_panel_layout):
    bl_category = "Create"
    bl_idname = "VIEW3D_TP_AssetFlinger_Panel_TOOLS"
    bl_label = "Asset Library"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_AssetFlinger_Panel_UI(bpy.types.Panel, draw_flinger_panel_layout):
    bl_idname = "VIEW3D_TP_AssetFlinger_Panel_UI"
    bl_label = "Asset Library"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
