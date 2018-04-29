# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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


# LOAD UI #i
from .layouts.ui_pivot      import draw_pivot_ui
from .layouts.ui_insert     import draw_insert_ui
from .layouts.ui_draw       import draw_draw_ui
from .layouts.ui_bevel      import draw_bevel_ui
from .layouts.ui_convert    import draw_convert_ui
from .layouts.ui_custom     import draw_custom_ui
from .layouts.ui_edit       import draw_edit_ui
from .layouts.ui_info       import draw_info_ui
from .layouts.ui_insert     import draw_insert_ui
from .layouts.ui_custom     import draw_custom_ui
from .layouts.ui_set        import draw_set_ui
from .layouts.ui_select     import draw_select_ui
from .layouts.ui_taper      import draw_taper_ui
from .layouts.ui_type       import draw_type_ui
from .layouts.ui_utils      import draw_utils_ui
from .layouts.ui_history    import draw_history_ui


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    


EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_PARTICLE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT']


class draw_curve_ui:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM:
        return isModelingMode and context.mode in EDIT

    icons = load_icons()

    types_expand = [("cuv_00"  ,""   ,"insert"    ,'EXPORT'                 ,0),
                    ("cuv_01"  ,""   ,"draw"     ,'BRUSH_DATA'             ,1), 
                    ("cuv_02"  ,""   ,"info"     ,'INFO'                   ,2), 
                    ("cuv_03"  ,""   ,"type"     ,'IPO_BEZIER'             ,3), 
                    ("cuv_04"  ,""   ,"edit"     ,'OUTLINER_DATA_CURVE'    ,4),
                    ("cuv_05"  ,""   ,"bevel"    ,'MOD_WARP'               ,5),                   
                    ("cuv_06"  ,""   ,"taper"    ,'STYLUS_PRESSURE'        ,6),                   
                    ("cuv_07"  ,""   ,"utils"    ,'PANEL_CLOSE'            ,7),                   
                    ("cuv_08"  ,""   ,"settings" ,'SCRIPTWIN'              ,8)]                  
                    #("cuv_09"  ,""   ,"custom"   ,'LAMP'   ,9)]                  

 
    types_dropdown = [("cuv_00"  ,"insert"   ,"insert"   ,''   ,0),
                      ("cuv_01"  ,"draw"     ,"draw"     ,''   ,1), 
                      ("cuv_02"  ,"info"     ,"info"     ,''   ,2), 
                      ("cuv_03"  ,"type"     ,"type"     ,''   ,3), 
                      ("cuv_04"  ,"edit"     ,"edit"     ,''   ,4),
                      ("cuv_05"  ,"bevel"    ,"bevel"    ,''   ,5),                   
                      ("cuv_06"  ,"taper"    ,"taper"    ,''   ,6),                   
                      ("cuv_07"  ,"utils"    ,"utils"    ,''   ,7),                   
                      ("cuv_08"  ,"settings" ,"settings" ,''   ,8),                  
                      ("cuv_09"  ,"custom"   ,"custom"   ,''   ,9)]                  

                     #("cuv_00"    ,"0"   ,"inserts"   ,icons["icon_boolean_rebool_brush"].icon_id    ,0), 
    
    bpy.types.Scene.panel_layout_dropdown = bpy.props.EnumProperty(name = " ", default = "cuv_00", items = types_dropdown)
    bpy.types.Scene.panel_layout_expand = bpy.props.EnumProperty(name = " ", default = "cuv_00", items = types_expand)

    def draw(self, context):
        layout = self.layout.column(1)   
        layout.operator_context = 'INVOKE_REGION_WIN'
                
        icons = load_icons()
       
        scene = context.scene
         
        draw_pivot_ui(self, context, layout)  

        if context.user_preferences.addons[__package__].preferences.tab_panel_layout_type == 'type_two':  

            col = layout.column(1)

            box = col.box().column(1) 
            row = box.row(1)  
            row.scale_y = 1.2 
            
            if context.user_preferences.addons[__package__].preferences.tab_panel_layout_expand == 'type_expand':
                row.alignment = 'CENTER' 
                row.prop(scene, 'panel_layout_expand', emboss = False, expand = True) 

                if scene.panel_layout_expand == "cuv_00":
                    draw_insert_ui(self, context, layout)  
            
                if scene.panel_layout_expand == "cuv_01":               
                    draw_draw_ui(self, context, layout)    

                obj = context.active_object
                if obj:
                    obj_type = obj.type                
                    if obj.type in {'CURVE', 'NURBS', 'SURFACE','TEXT','MBALL'}: 
      
                        if scene.panel_layout_expand == "cuv_02":
                           
                            draw_info_ui(self, context, layout)  

                        if scene.panel_layout_expand == "cuv_03": 
                          
                            draw_type_ui(self, context, layout)  
             
                        if scene.panel_layout_expand == "cuv_04":       
                            draw_edit_ui(self, context, layout)        

                        if scene.panel_layout_expand == "cuv_05":   
                                  
                            draw_bevel_ui(self, context, layout)               

                        if scene.panel_layout_expand == "cuv_06": 
                      
                            draw_taper_ui(self, context, layout) 

                        if scene.panel_layout_expand == "cuv_07": 
                           
                            draw_utils_ui(self, context, layout) 

                        if scene.panel_layout_expand == "cuv_08": 
                           
                            draw_set_ui(self, context, layout) 

                #if scene.panel_layout_expand == "cuv_09": 
                   
                    #draw_custom_ui(self, context, layout)             

            else:
                row.prop(scene, 'panel_layout_dropdown', text="Layout") 

                if scene.panel_layout_dropdown == "cuv_00":
                    draw_insert_ui(self, context, layout)  
            
                if scene.panel_layout_dropdown == "cuv_01":               
                    draw_draw_ui(self, context, layout)    

                obj = context.active_object
                if obj:
                    obj_type = obj.type                
                    if obj.type in {'CURVE', 'NURBS', 'SURFACE','TEXT','MBALL'}: 
      
                        if scene.panel_layout_dropdown == "cuv_02":
                           
                            draw_info_ui(self, context, layout)  

                        if scene.panel_layout_dropdown == "cuv_03": 
                          
                            draw_type_ui(self, context, layout)  
             
                        if scene.panel_layout_dropdown == "cuv_04":       
                            draw_edit_ui(self, context, layout)        

                        if scene.panel_layout_dropdown == "cuv_05":   
                                  
                            draw_bevel_ui(self, context, layout)               

                        if scene.panel_layout_dropdown == "cuv_06": 
                      
                            draw_taper_ui(self, context, layout) 

                        if scene.panel_layout_dropdown == "cuv_07": 
                           
                            draw_utils_ui(self, context, layout) 

                        if scene.panel_layout_dropdown == "cuv_08": 
                           
                            draw_set_ui(self, context, layout) 

                if scene.panel_layout_dropdown == "cuv_09": 
                   
                    draw_custom_ui(self, context, layout)             

                  
        else:

            tp_props = context.window_manager.tp_props_curve        
           
            col = layout.column(align=True)                
            if not tp_props.display_curve_insert: 
              
                box = col.box().column(1)
                
                row = box.row(1)   
                row.prop(tp_props, "display_curve_insert", text="", icon="TRIA_RIGHT", emboss = False)                
                row.label("Insert")

            else:
               
                box = col.box().column(1)
                
                row = box.row(1)  
                row.prop(tp_props, "display_curve_insert", text="", icon="TRIA_DOWN", emboss = False)            
                sub = row.row()
                sub.alignment = "CENTER"  
                sub.label("INSERT")  
                row.label("", icon="TRIA_DOWN")  

                draw_insert_ui(self, context, layout) 


            if context.mode == "OBJECT" or context.mode == "EDIT_CURVE":
            
                col = layout.column(align=True)                
                if not tp_props.display_curve_draw: 
                  
                    box = col.box().column(1)
                    
                    row = box.row(1)   
                    row.prop(tp_props, "display_curve_draw", text="", icon="TRIA_RIGHT", emboss = False)                
                    row.label("Draw")

                else:
                   
                    box = col.box().column(1)
                    
                    row = box.row(1)  
                    row.prop(tp_props, "display_curve_draw", text="", icon="TRIA_DOWN", emboss = False)            
                    sub = row.row()
                    sub.alignment = "CENTER" 
                    sub.label("DRAW")  
                    row.label("", icon="TRIA_DOWN")  
             
                    draw_draw_ui(self, context, layout) 


            obj = context.active_object
            if obj:
                obj_type = obj.type                
                if obj.type in {'CURVE', 'NURBS', 'SURFACE','TEXT','MBALL'}: 


                    col = layout.column(align=True)                
                    if not tp_props.display_curve_info: 
                      
                        box = col.box().column(1)
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_info", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Info")

                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_info", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("INFO")    
                        row.label("", icon="TRIA_DOWN")  
                                                
                        draw_info_ui(self, context, layout)  



                    if context.mode == "EDIT_CURVE" or context.mode == "EDIT_SURFACE":
                    
                        col = layout.column(align=True)                
                        if not tp_props.display_curve_select: 
                          
                            box = col.box().column(1)
                            
                            row = box.row(1)   
                            row.prop(tp_props, "display_curve_select", text="", icon="TRIA_RIGHT", emboss = False)                
                            row.label("Select")

                        else:
                           
                            box = col.box().column(1)
                            
                            row = box.row(1)  
                            row.prop(tp_props, "display_curve_select", text="", icon="TRIA_DOWN", emboss = False)            
                            sub = row.row()
                            sub.alignment = "CENTER" 
                            sub.label("SELECT")     
                            row.label("", icon="TRIA_DOWN")  
                          
                            draw_select_ui(self, context, layout)               



                    col = layout.column(align=True)                
                    if not tp_props.display_curve_type: 
                      
                        box = col.box().column(1)
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_type", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Type")

                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_type", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("TYPE")    
                        row.label("", icon="TRIA_DOWN")  
                                    
                        draw_type_ui(self, context, layout) 



                    col = layout.column(align=True)                
                    if not tp_props.display_curve_edit: 
                      
                        box = col.box().column(1)
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_edit", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Edit")                                                                                

                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_edit", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("EDIT")              
                        row.label("", icon="TRIA_DOWN")  
                          
                        draw_edit_ui(self, context, layout) 



                    col = layout.column(align=True)                
                    if not tp_props.display_curve_bevel: 
                      
                        box = col.box().column(1)
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_bevel", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Bevel")

                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_bevel", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("BEVEL")  
                        row.label("", icon="TRIA_DOWN")  
                          
                        draw_bevel_ui(self, context, layout) 



                    col = layout.column(align=True)                
                    if not tp_props.display_curve_taper: 
                      
                        box = col.box().column(1)
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_taper", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Taper")
                                
                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_taper", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("TAPER")  
                        row.label("", icon="TRIA_DOWN")  
                          
                        draw_taper_ui(self, context, layout) 



                    col = layout.column(align=True)        
                    if not tp_props.display_curve_utility: 
                      
                        box = col.box().column(1)  
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_utility", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Utility")

                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_utility", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("UTILITY") 
                        row.label("", icon="TRIA_DOWN")  
                          
                        draw_utils_ui(self, context, layout) 
                       


                    col = layout.column(align=True)        
                    if not tp_props.display_curve_setting: 
                      
                        box = col.box().column(1)  
                        
                        row = box.row(1)   
                        row.prop(tp_props, "display_curve_setting", text="", icon="TRIA_RIGHT", emboss = False)                
                        row.label("Settings")

                    else:
                       
                        box = col.box().column(1)
                        
                        row = box.row(1)  
                        row.prop(tp_props, "display_curve_setting", text="", icon="TRIA_DOWN", emboss = False)            
                        sub = row.row()
                        sub.alignment = "CENTER" 
                        sub.label("SETTINGS")  
                        row.label("", icon="TRIA_DOWN")  
                                                        
                        draw_set_ui(self, context, layout) 


            if context.user_preferences.addons[__package__].preferences.tab_panel_layout_custom == 'add':  

 
                col = layout.column(align=True)        
                if not tp_props.display_curve_custom: 
                  
                    box = col.box().column(1)  
                    
                    row = box.row(1)   
                    row.prop(tp_props, "display_curve_custom", text="", icon="TRIA_RIGHT", emboss = False)                
                    row.label("Custom")

                else:
                   
                    box = col.box().column(1)
                    
                    row = box.row(1)  
                    row.prop(tp_props, "display_curve_custom", text="", icon="TRIA_DOWN", emboss = False)            
                    sub = row.row()
                    sub.alignment = "CENTER" 
                    sub.label("CUSTOM")  
                    row.label("", icon="TRIA_DOWN")  
                                                    
                    draw_custom_ui(self, context, layout) 



        if context.mode == "OBJECT":
            draw_convert_ui(self, context, layout) 
      
        draw_history_ui(self, context, layout)        




# LOAD UI #

class VIEW3D_TP_Curve_Compact_TOOLS(bpy.types.Panel, draw_curve_ui):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Curve_Compact_TOOLS"
    bl_label = "Curve"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_Curve_Compact_UI(bpy.types.Panel, draw_curve_ui):
    bl_idname = "VIEW3D_TP_Curve_Compact_UI"
    bl_label = "Curve"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

