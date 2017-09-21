__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons


def draw_align_navi_tools_panel_layout(self, context, layout):
        tp = context.window_manager.tp_align_looptools
        
        icons = load_icons()
                  
        layout = self.layout  
        layout.operator_context = 'INVOKE_REGION_WIN'

        row = layout.row(1)

        box = row.box()

        box.label(text='Pan:')
        rowr = box.row(1)
        rowr.operator('opr.pan_up_view1', text='', icon='TRIA_DOWN')
        rowr.operator('opr.pan_down_view1', text='', icon='TRIA_UP')

        rowr = box.row(1)
        rowr.operator('opr.pan_right_view1', text='', icon='BACK')
        rowr.operator('opr.pan_left_view1', text='', icon='FORWARD')

        rowr = box.row(1)
        rowr.label(text='Zoom:')
        
        rowr = box.row(1)
        rowr.operator('opr.zoom_in_view1', text='', icon='ZOOMIN')
        rowr.operator('opr.zoom_out_view1', text='', icon='ZOOMOUT')

        rowr = box.row(1)

        rowr = box.row()

        box = row.box()
        box.label(text='Orbit:')

        rowr = box.row(1)
        rowr.operator('opr.orbit_up_view1', text='', icon='TRIA_DOWN')
        rowr.operator('opr.orbit_down_view1', text='', icon='TRIA_UP')  

        rowr = box.row(1)
        rowr.operator('opr.orbit_right_view1', text='', icon='BACK')
        rowr.operator('opr.orbit_left_view1', text='', icon='FORWARD')

        rowr = box.row(1)
        rowr.label(text='Roll:')
        
        rowr = box.row(1)
        rowr.operator('opr.roll_left_view1', text='', icon='ZOOMIN')
        rowr.operator('opr.roll_right_view1', text='', icon='ZOOMOUT')
      
        rowr = box.row(1)

        rowr = box.row()

        box = row.box()
        box.label(text='View:')
        
        rowr = box.column(1)        
        rowr.operator("view3d.viewnumpad", text="Front").type='FRONT'
        rowr.operator("view3d.viewnumpad", text="Back").type='BACK'
        rowr.operator("view3d.viewnumpad", text="Left").type='LEFT'
        rowr.operator("view3d.viewnumpad", text="Right").type='RIGHT'
        rowr.operator("view3d.viewnumpad", text="Top").type='TOP'
        rowr.operator("view3d.viewnumpad", text="Bottom").type='BOTTOM'

        box = layout.box().column(1)           

        row = box.row(1)  
        row.operator("view3d.localview", text="Global/Local", icon='WORLD')
        row.operator("view3d.view_persportho", text="Persp/Ortho", icon='VIEW3D')             

        row = box.row(1) 
        row.operator("view3d.viewnumpad", text="Camera", icon='CAMERA_DATA').type = 'CAMERA'
        row.operator("view3d.view_selected", text="Selected", icon='ZOOM_SELECTED')

        row = box.row(1)

        button_cursor = icons.get("icon_cursor")
        row.operator("view3d.view_center_cursor", text="Cursor", icon_value=button_cursor.icon_id)
        
        button_cursor_center = icons.get("icon_cursor_center")
        row.operator("view3d.view_all", text="Center", icon_value=button_cursor_center.icon_id).center = True

        box.separator()                         


        box = layout.box().column(1)           

        row = box.column(1)
        row.label(text="View to Object:")
        row.prop(context.space_data, "lock_object", text="")


        box.separator() 
        


class VIEW3D_TP_Align_Navi_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Align_Navi_Panel_TOOLS"
    bl_label = "Navigation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_context = 'mesh_edit'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_align_navi_tools_panel_layout(self, context, layout) 



class VIEW3D_TP_Align_Navi_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Align_Navi_Panel_UI"
    bl_label = "Navigation"
    bl_space_type = 'VIEW_3D'
    #bl_context = 'mesh_edit'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'   

        draw_align_navi_tools_panel_layout(self, context, layout) 



