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

# LOAD UI #
from .ui_layouts.ui_title                  import draw_title_ui
from .ui_layouts.ui_snaphot                import draw_snapshot_ui
from .ui_layouts.ui_symdim                 import draw_symdim_ui
from .ui_layouts.ui_visual                 import draw_visual_ui
from .ui_layouts.ui_custom                 import draw_custom_ui
from .ui_layouts.ui_sculpt                 import draw_sculpt_ui
from .ui_layouts.ui_sculpt                 import draw_sculpt_edit_ui
from .ui_layouts.ui_sculpt                 import draw_sculpt_mask_ui
from .ui_layouts.ui_sculpt_brush           import draw_sculpt_brush_ui
from .ui_layouts.ui_modifier_sculpt        import draw_modifier_sculpt_ui

# LOAD BRUSHES # 
def mkb_exist():
    mkb_brush_exist = False  
    for item in bpy.data.brushes:
        if item.name.endswith("IK"):
            mkb_brush_exist = True
    return mkb_brush_exist  


# LOAD PANEL #
EDIT = ["SCULPT"]
GEOM = ['MESH']

class draw_layout_resculpt:
    
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
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        tp_props = context.window_manager.tp_props_resurface

        icons = load_icons()    
        
        # LOADED LAYOUTS ---------------------------------------------------------------------
 
        
        # TITLE # 
        draw_title = context.user_preferences.addons[__package__].preferences.tab_title_ui
        if draw_title == 'on':  

            draw_title_ui(self, context, layout) 


        # SCULPT BRUSH #
        draw_brush = context.user_preferences.addons[__package__].preferences.tab_brush_ui
        if draw_brush == 'on': 
                     
            draw_sculpt_brush_ui(self, context, layout)

   
        # SCULPT #
        draw_sculpt_ui(self, context, layout)
 

        # EDITING #
        display_sculpt_edit = context.user_preferences.addons[__package__].preferences.tab_sculpt_edit
        if display_sculpt_edit == 'on': 

            draw_sculpt_edit_ui(self, context, layout)


        # MASK #
        display_sculpt_mask = context.user_preferences.addons[__package__].preferences.tab_sculpt_mask
        if display_sculpt_mask == 'on': 

            draw_sculpt_mask_ui(self, context, layout)


        # SYMDIM #
        display_symdim = context.user_preferences.addons[__package__].preferences.tab_symdim_ui
        if display_symdim == 'on':   
            
            draw_symdim_ui(self, context, layout)  


        # SNAPSHOT #
        display_snapshot = context.user_preferences.addons[__package__].preferences.tab_snapshot_ui
        if display_snapshot == 'on': 

            draw_snapshot_ui(self, context, layout)


        # CUSTOM #
        display_custom = context.user_preferences.addons[__package__].preferences.tab_custom_sculpt_ui
        if display_custom == 'on': 
            
            draw_custom_ui(self, context, layout)   


        # MODIFIER #
        display_modifier = context.user_preferences.addons[__package__].preferences.tab_modsculpt_ui
        if display_modifier == 'on':                                         
        
            draw_modifier_sculpt_ui(self, context, layout)   


        # VISUALS #    
        display_visual = context.user_preferences.addons[__package__].preferences.tab_visual_ui
        if display_visual == 'on':

            draw_visual_ui(self, context, layout)       



        # MAIN PANEL ------------------------------------------------------------------------------


        # HISTORY #  
        display_history = context.user_preferences.addons[__package__].preferences.tab_history_ui
        if display_history == 'on':

            
            box = layout.box().column(1)                     

            row = box.row(1) 
            row.operator('tp_ops.load_single_brush', text='Image', icon ="ASSET_MANAGER")
            row.operator('tp_ops.load_brushes', text='Folder', icon ="IMASEL")

            #row.operator("wm.append", text='Append', icon = 'TPAINT_HLT')

            row = box.row(1)         
            if mkb_exist() == False:
                row.operator("tp_ops.load_brushes", text='Load Brushes', icon = 'BRUSH_DATA')
                
            if mkb_exist():
                row.operator("tp_ops.load_brushes", text = 'Remove Brushes', icon = 'BRUSH_DATA')
                
            row.operator("tp_ops.reload_brushes", icon = 'FILE_REFRESH')


            box.separator()            

            row = box.row(1)        
            if tp_props.display_docu:
                row.prop(tp_props, "display_docu", text="", icon='SCRIPTWIN')
            else:
                row.prop(tp_props, "display_docu", text="", icon='SCRIPTWIN')     

            row.operator("view3d.ruler", text="Ruler")            
            row.operator("ed.undo", text="", icon="FRAME_PREV")
            row.operator("ed.undo_history", text="", icon="COLLAPSEMENU")
            row.operator("ed.redo", text="", icon="FRAME_NEXT") 
           
            box.separator()   

            if tp_props.display_docu:                
                
                col = layout.column(align=True)                
               
                box = col.box().column(1)             

                row = box.row(1)
                #row.prop(tp_props, "display_help", text="View Help", icon='INFO')    
                row.operator("wm.url_open", text="Open Wiki", icon='QUESTION').url = "https://github.com/mkbreuer/ToolPlus/wiki" 
              
                box.separator() 
               
                row = box.row(1)              
                wm = context.window_manager    
                row.operator("wm.save_userpref", icon='FILE_TICK')   
                row.operator("wm.restart_blender", text="", icon='LOAD_FACTORY') 
               
                panel_prefs = context.user_preferences.addons[__package__].preferences
                expand = panel_prefs.expand_panel_tools

                box.separator() 
         
                row = box.row(1)                  
                row.prop(panel_prefs, "tools_category", text="Category")   
                
                box.separator()  

                panel_prefs = context.user_preferences.addons[__package__].preferences
                expand = panel_prefs.expand_panel_tools

                row = box.row(1)
                row.prop(panel_prefs, 'tab_location_sculpt', expand=True)   
                
                box.separator()  

                row = box.row(1)
                row.prop(panel_prefs, 'tab_brush_ui', expand=True)   
                
                box.separator()  

                row = box.row(1)
                row.prop(panel_prefs, 'tab_brush_quickset', expand=True)   
                
                row = box.row(1)
                row.alignment = 'CENTER'
                row.label("> quickbrush need a restart <")             
              
                box.separator()                
              
                row = box.column_flow(2)
                                      
                row.prop(panel_prefs, 'tab_title_ui', expand=True)                                       
                row.prop(panel_prefs, 'tab_sculpt_mask', expand=True)
                row.prop(panel_prefs, 'tab_snapshot_ui', expand=True) 
                row.prop(panel_prefs, 'tab_visual_ui', expand=True)        

                row.prop(panel_prefs, 'tab_sculpt_edit', expand=True)                
                row.prop(panel_prefs, 'tab_symdim_ui', expand=True)
                row.prop(panel_prefs, 'tab_modsculpt_ui', expand=True)               
                row.prop(panel_prefs, 'tab_history_ui', expand=True)                
                row.prop(panel_prefs, 'tab_custom_sculpt_ui', expand=True) 
                
                box.separator() 
                box.separator() 
             
            row = box.row(1)             
            row.label( text="", icon = "LAYER_USED")                                  
            row.operator("object.editmode_toggle", text="Edit", icon = "EDIT")                            
            row.operator("paint.weight_paint_toggle", text="Weight", icon = "WPAINT_HLT") 
            row.label( text="", icon = "LAYER_USED")

            box.separator()

 
# LOAD PANEL #  

class VIEW3D_TP_ReSculpt_Panel_TOOLS(bpy.types.Panel, draw_layout_resculpt):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_ReSculpt_Panel_TOOLS"
    bl_label = "ReSculpt"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'   
    bl_options = {'DEFAULT_CLOSED'}


class VIEW3D_TP_ReSculpt_Panel_UI(bpy.types.Panel, draw_layout_resculpt):
    bl_idname = "VIEW3D_TP_ReSculpt_Panel_UI"
    bl_label = "ReSculpt"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  
    bl_options = {'DEFAULT_CLOSED'}

