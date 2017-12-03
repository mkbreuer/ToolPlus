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
from bpy import*
from bpy.props import *
from bpy.types import WindowManager
from . icons.icons import load_icons


class TP_Header_Snap_to_Cursor(bpy.types.Menu):
    """Snap Cursor to..."""
    bl_label = "Snap to Menu"
    bl_idname = "tp_header.snap_to_cursor"
    
    def draw(self, context):

        layout = self.layout
        icons = load_icons()
       
        layout.operator_context = 'INVOKE_REGION_WIN'
         
        layout.label("Cursor to...")
        layout.separator()


        button_cursor_object = icons.get("icon_cursor_object")
        layout.operator("view3d.snap_cursor_to_selected", text="Selected", icon_value=button_cursor_object.icon_id)

        button_cursor_center = icons.get("icon_cursor_center")
        layout.operator("view3d.snap_cursor_to_center", text="Center", icon_value=button_cursor_center.icon_id)

        button_cursor_grid = icons.get("icon_cursor_grid")
        layout.operator("view3d.snap_cursor_to_grid", text="Grid", icon_value=button_cursor_grid.icon_id)

        button_cursor_active_obm = icons.get("icon_cursor_active_obm")
        layout.operator("view3d.snap_cursor_to_active", text="Active", icon_value=button_cursor_active_obm.icon_id)

        obj = context
        if obj and obj.mode == "EDIT_MESH":
            layout.separator()           
            
            button_cursor_3point_center = icons.get("icon_cursor_3point_center")           
            layout.operator("mesh.circlecentercursor", text="3-Verts Center", icon_value=button_cursor_3point_center.icon_id)   
            
            layout.operator("tp_header.snap_cursor_to_edge_intersection", text="Edges Intersection", icon ="PLUS")     
           



class TP_Header_Snap_to_Select(bpy.types.Menu):
    """Snap Selection to..."""
    bl_label = "Snap to Menu"
    bl_idname = "tp_header.snap_to_select"
    
    def draw(self, context):

        layout = self.layout
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.label("Select to...")
        layout.separator()

        button_select_grid = icons.get("icon_select_grid")
        layout.operator("view3d.snap_selected_to_grid", text="Grid", icon_value=button_select_grid.icon_id)

        button_select_center = icons.get("icon_select_center")
        layout.operator("tp_ops.zero_all_axis", text="Center", icon_value=button_select_center.icon_id)

        button_select_cursor = icons.get("icon_select_cursor")           
        layout.operator("view3d.snap_selected_to_cursor", text="Cursor", icon_value=button_select_cursor.icon_id).use_offset=False

        button_select_cursor_offset_obm = icons.get("icon_select_cursor_offset_obm")           
        layout.operator("view3d.snap_selected_to_cursor", text="C-Offset", icon_value=button_select_cursor_offset_obm.icon_id).use_offset=True

        button_select_active_obm = icons.get("icon_select_active_obm")
        layout.operator("view3d.snap_selected_to_active", text="Active", icon_value=button_select_active_obm.icon_id)



class TP_Header_Snap_Setup(bpy.types.Operator):
    """Setups for Snapping"""
    bl_idname = "tp_header.snap_setup"
    bl_label = "Snap Sets :)"
    bl_options = {'REGISTER', 'UNDO'}


    tp_snap = bpy.props.EnumProperty(
                             items=[("tp_retopo"        ,"Mesh Retopo"          ,"Mesh Retopo"        ,"" , 1),                                     
                                    ("tp_place"         ,"Place Object"         ,"Place Object"       ,"" , 2),
                                    ("tp_grid"          ,"Absolute Grid"        ,"Absolute Grid"      ,"" , 3),                                    
                                    ("tp_active_vert"   ,"Active Vertex"        ,"Active Vertex"      ,"" , 4),
                                    ("tp_closest"       ,"Closest Vertex"       ,"Closest Vertex"     ,"" , 5),
                                    ("tp_active_3d"     ,"3d Cursor Active"     ,"3d CursorActive"    ,"" , 6),
                                    ("tp_selected_3d"   ,"3d Cursor Selected"   ,"3d CursorSelected"  ,"" , 7)],
                                    name = "SnapSets", 
                                    default = "tp_grid")

    def draw(self, context):
        layout = self.layout.column(1)  

        box = layout.box().column(1)  
        
        row = box.column(1)
        row.alignment = 'CENTER'        
        row.prop(self, 'tp_snap',text=" ", expand =True)                                            
                                         
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*1.75, height=300)



    def execute(self, context):
  
        if self.tp_snap == "tp_grid":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
            bpy.context.scene.tool_settings.use_snap_grid_absolute = True
            bpy.context.scene.tool_settings.use_snap_align_rotation = False            
            
        elif self.tp_snap == "tp_place":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = True
            bpy.context.scene.tool_settings.use_snap_project = True
                        
        elif self.tp_snap == "tp_retopo":
            bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
                        
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False
            
            
        elif self.tp_snap == "tp_active_vert":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False       
  
        elif self.tp_snap == "tp_closest":
            bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'            
            
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False    


        elif self.tp_snap == "tp_active_3d":
            bpy.context.space_data.pivot_point = 'CURSOR'            

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   
            bpy.ops.view3d.snap_cursor_to_active()
                        
            
        elif self.tp_snap == "tp_selected_3d":
            bpy.context.space_data.pivot_point = 'CURSOR'  

            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
            bpy.context.scene.tool_settings.use_snap_align_rotation = False   

            bpy.ops.view3d.snap_cursor_to_selected()

        return {'FINISHED'}



# REGISTRY #

def register():
    bpy.utils.register_module(__name__)
     
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


