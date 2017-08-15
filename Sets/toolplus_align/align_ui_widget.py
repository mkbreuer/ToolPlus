# ##### BEGIN GPL LICENSE BLOCK #####
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



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons



def draw_align_widget_tools_panel_layout(self, context, layout):
     
        icons = load_icons()    
     
        box = layout.box().column(1) 
        
        row = box.row(1)  
        sub = row.row(1)
        sub.scale_x = 7

        sub.operator("tp_ops.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("tp_ops.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("tp_ops.pivot_active", "", icon="ROTACTIVE")
        sub.operator("tp_ops.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("tp_ops.pivot_median", "", icon="ROTATECENTER")     


        Display_Snap = context.user_preferences.addons[__package__].preferences.tab_snap 
        if Display_Snap == 'on':

            box = layout.box().column(1)           

            row = box.row(1)               
            row.operator("wm.context_toggle", text=" ", icon='MANIPUL').data_path = "space_data.show_manipulator" 
            row.operator("tp_ops.manipulator_all", " ", icon = 'NDOF_DOM')
            row.operator("tp_ops.manipulator_move", " ", icon = 'MAN_TRANS')                    
            row.operator("tp_ops.manipulator_rota", " ", icon = 'MAN_ROT')                    
            row.operator("tp_ops.manipulator_scale", " ", icon = 'MAN_SCALE')              

            row = box.row(1)
            if bpy.context.space_data.transform_orientation == 'GLOBAL':         
                row.operator("tp_ops.space_global", "Gobal", emboss = False)        
            else:        
                row.operator("tp_ops.space_global", "Gobal")        

            if bpy.context.space_data.transform_orientation == 'LOCAL':   
                row.operator("tp_ops.space_local", "Local", emboss = False)
            else:
                row.operator("tp_ops.space_local", "Local")

            if bpy.context.space_data.transform_orientation == 'NORMAL':   
                row.operator("tp_ops.space_normal", "Normal", emboss = False)
            else:    
                row.operator("tp_ops.space_normal", "Normal")

            if bpy.context.space_data.transform_orientation == 'GIMBAL':   
                row.operator("tp_ops.space_gimbal", "Gimbal", emboss = False)
            else:    
                row.operator("tp_ops.space_gimbal", "Gimbal")                 

            if bpy.context.space_data.transform_orientation == 'VIEW':   
                row.operator("tp_ops.space_view", "View", emboss = False)
            else:    
                row.operator("tp_ops.space_view", "View")    
            
            box.separator()
            box.separator()
                                       
            row = box.row(1)
            row.prop(context.tool_settings, "use_snap", text=" ")           

            if bpy.context.scene.tool_settings.snap_target == 'CLOSEST':         
                row.operator("tp_ops.snap_closest", "Closest", emboss = False)        
            else:        
                row.operator("tp_ops.snap_closest", "Closest")        

            if bpy.context.scene.tool_settings.snap_target == 'CENTER':
                row.operator("tp_ops.snap_center", "Center", emboss = False)
            else:
                row.operator("tp_ops.snap_center", "Center")

            if bpy.context.scene.tool_settings.snap_target == 'MEDIAN':
                row.operator("tp_ops.snap_median", "Median", emboss = False)
            else:    
                row.operator("tp_ops.snap_median", "Median")

            if bpy.context.scene.tool_settings.snap_target == 'ACTIVE':
                row.operator("tp_ops.snap_active", "Active", emboss = False)
            else:    
                row.operator("tp_ops.snap_active", "Active")


            row = box.row(1)
            
            if bpy.context.scene.tool_settings.snap_element == 'INCREMENT':                                    
                row.operator("tp_ops.snape_increment", " ", icon = "SNAP_INCREMENT", emboss = False)        
            else:
                row.operator("tp_ops.snape_increment", " ", icon = "SNAP_INCREMENT")        

            if bpy.context.scene.tool_settings.snap_element == 'VERTEX':            
                row.operator("tp_ops.snape_vertex", " ", icon = "SNAP_VERTEX", emboss = False)        
            else:
                row.operator("tp_ops.snape_vertex", " ", icon = "SNAP_VERTEX")        

            if bpy.context.scene.tool_settings.snap_element == 'EDGE':
                row.operator("tp_ops.snape_edge", " ", icon = "SNAP_EDGE", emboss = False)        
            else:
                row.operator("tp_ops.snape_edge", " ", icon = "SNAP_EDGE")        

            if bpy.context.scene.tool_settings.snap_element == 'FACE':
                row.operator("tp_ops.snape_face", " ", icon = "SNAP_FACE", emboss = False)
            else:
                row.operator("tp_ops.snape_face", " ", icon = "SNAP_FACE")

            if bpy.context.scene.tool_settings.snap_element == 'VOLUME':
                row.operator("tp_ops.snape_volume", " ", icon = "SNAP_VOLUME", emboss = False) 
            else:
                row.operator("tp_ops.snape_volume", " ", icon = "SNAP_VOLUME") 
            
            box.separator()
            box.separator()
            
            row = box.row(1) 
            row.alignment = 'CENTER' 
            
            if bpy.context.scene.tool_settings.snap_element == 'INCREMENT':          
                row.prop(context.tool_settings, "use_snap_grid_absolute", text="Snap Grid = Absolute", icon="SNAP_GRID")           

            if bpy.context.scene.tool_settings.snap_element in {'VERTEX', 'EDGE'}:  
                row.prop(context.tool_settings, "use_snap_align_rotation", text="Snap Vertex & Edge = Normal", icon="SNAP_NORMAL")           
                        
            if bpy.context.scene.tool_settings.snap_element in {'FACE'}: 
                row.prop(context.tool_settings, "use_snap_project", text="Snap Face = Project", icon="RETOPO")

            if bpy.context.scene.tool_settings.snap_element == 'VOLUME': 
                row.prop(context.tool_settings, "use_snap_peel_object", text="Snap Volume = Peel Object", icon="SNAP_PEEL_OBJECT")

            box.separator()
            

       
        Display_SnapSet = context.user_preferences.addons[__package__].preferences.tab_snapset
        if Display_SnapSet == 'on':

            box = layout.box().column(1)  

            Display_Title = context.user_preferences.addons[__package__].preferences.tab_title
            if Display_Title == 'on':   
            
                row = box.row(1)           
                row.label("Snap Set...")  

            row = box.row(1) 
            
            button_snap_grid = icons.get("icon_snap_grid")
            row.operator("tp_ops.grid", text=" ", icon_value=button_snap_grid.icon_id)

            if context.mode == 'OBJECT':

                button_snap_place = icons.get("icon_snap_place")
                row.operator("tp_ops.place", text=" ", icon_value=button_snap_place.icon_id)

            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                row.operator("tp_ops.retopo", text=" ", icon_value=button_snap_retopo.icon_id)

            button_snap_cursor = icons.get("icon_snap_cursor")           
            row.operator("tp_ops.active_3d", text=" ", icon_value=button_snap_cursor.icon_id) 
 
            button_snap_active = icons.get("icon_snap_active")
            row.operator("tp_ops.active_vert", text=" ", icon_value=button_snap_active.icon_id)

            box.separator() 
    
    

        Display_Normals = context.user_preferences.addons[__package__].preferences.tab_normals
        if Display_Normals == 'on':

            box = layout.box().column(1) 

            Display_Title = context.user_preferences.addons[__package__].preferences.tab_title
            if Display_Title == 'on': 
                      
                row = box.row(1)  
                row.label("Normal Axis") 
                        
            row = box.row(1)              
            row.menu("tp_ops.translate_normal_menu", text="Move")
            row.menu("tp_ops.rotate_normal_menu", text="Rotate")
            row.menu("tp_ops.resize_normal_menu", text="Scale")           

            box.separator() 



        Display_PropEdit = context.user_preferences.addons[__package__].preferences.tab_propedit 
        if Display_PropEdit == 'on':

            box = layout.box().column(1)           

            row = box.row(1)                   
            row.prop(context.tool_settings , "use_proportional_edit_objects","Proportional Edit", icon_only=True)
            
            sub = row.row(1)
            sub.scale_x = 0.5
            sub.prop(context.tool_settings , "proportional_edit_falloff", icon_only=True) 

            box.separator()           
              

        Display_Orientation = context.user_preferences.addons[__package__].preferences.tab_orientation
        if Display_Orientation == 'on':
            
            box = layout.box().column(1)  

            Display_Title = context.user_preferences.addons[__package__].preferences.tab_title
            if Display_Title == 'on': 

                row = box.row(1)         
                row.label(text="Transform Orientation")

            row = box.row(1)         
            
            row.prop(context.space_data, "transform_orientation", text="", icon='MANIPUL')
            row.operator("transform.create_orientation", text="", icon='ZOOMIN')

            if context.space_data.current_orientation:
                box.separator() 
                
                row = box.row(1)
                row.prop(context.space_data.current_orientation, "name", text="")
                row.operator("transform.delete_orientation", text="", icon='X')

            box.separator() 
        

        Display_Cursor = context.user_preferences.addons[__package__].preferences.tab_cursor
        if Display_Cursor == 'on':

            box = layout.box().column(1)  
           
            row = box.row(1)
            row.column().prop(context.space_data, "cursor_location", text="3D Cursor Location")

            box.separator() 



class VIEW3D_TP_Align_Widget_Panel_TOOLS(bpy.types.Panel):
    bl_category = "Align"
    bl_idname = "VIEW3D_TP_Align_Widget_Panel_TOOLS"
    bl_label = "Widget"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_align_widget_tools_panel_layout(self, context, layout) 



class VIEW3D_TP_Align_Widget_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Align_Widget_Panel_UI"
    bl_label = "Widget"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_align_widget_tools_panel_layout(self, context, layout) 

