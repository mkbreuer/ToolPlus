# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****


# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import*




class VIEW3D_TP_Snapset_Grid(bpy.types.Operator):
    """snap to increments of grid """
    bl_idname = "tp_ops.grid"
    bl_label = "Snapset Grid"
    bl_options = {'INTERNAL'}

    def execute(self, context):

        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
        bpy.context.scene.tool_settings.use_snap_grid_absolute = True
        bpy.context.scene.tool_settings.use_snap_align_rotation = False            

        return {'FINISHED'}


class VIEW3D_TP_Snapset_Place(bpy.types.Operator):
    """snap to object surface with normal rotation"""
    bl_idname = "tp_ops.place"
    bl_label = "Place Object"
    bl_options = {'INTERNAL'}

    def execute(self, context):            

        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'FACE'
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        bpy.context.scene.tool_settings.use_snap_align_rotation = True
        bpy.context.scene.tool_settings.use_snap_project = True
                        
        return {'FINISHED'}


class VIEW3D_TP_Snapset_Retopo(bpy.types.Operator):
    """snap to surface of another object"""
    bl_idname = "tp_ops.retopo"
    bl_label = "Mesh Retopo"
    bl_options = {'INTERNAL'}

    def execute(self, context):            

        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'                    
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'FACE'
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        bpy.context.scene.tool_settings.use_snap_align_rotation = False
                    
        return {'FINISHED'}



class VIEW3D_TP_Snapset_Active(bpy.types.Operator):
    """snap selected to active vertex"""
    bl_idname = "tp_ops.active_snap"
    bl_label = "Snap Verts"
    bl_options = {'INTERNAL'}

    def execute(self, context):            
                
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'VERTEX'
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'    
        bpy.context.scene.tool_settings.snap_target = 'ACTIVE'        
        bpy.context.scene.tool_settings.use_snap_align_rotation = False       
 
        return {'FINISHED'}



class VIEW3D_TP_Snapset_Closest(bpy.types.Operator):
    """snap selected to closest median"""
    bl_idname = "tp_ops.closest_snap"
    bl_label = "Snap Closest"
    bl_options = {'INTERNAL'}

    def execute(self, context):            
                
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'VERTEX'
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'                 
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'        
        bpy.context.scene.tool_settings.use_snap_align_rotation = False       
 
        return {'FINISHED'}


class VIEW3D_TP_Snapset_Active_3d_Int(bpy.types.Operator):
    """set 3D cursor >> LMB: to selected / >> RMB: to active """
    bl_idname = "tp_ops.active_3d_int"
    bl_label = "3d Cursor"
    bl_options = {'INTERNAL'}

    mode = bpy.props.StringProperty(default="")

    def execute(self, context):            

        bpy.context.space_data.pivot_point = 'CURSOR'            

        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'VERTEX'
        bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
        bpy.context.scene.tool_settings.use_snap_align_rotation = False   
                        
        if self.mode in "tp_active": 
            bpy.ops.view3d.snap_cursor_to_active()   

        if self.mode in "tp_select": 
            bpy.ops.view3d.snap_cursor_to_selected()            

        return {'FINISHED'}




class VIEW3D_TP_Snapset_Active_3d_Modal(bpy.types.Operator):
    """set 3D cursor >> LMB: to selected / >> RMB: to active """
    bl_idname = "tp_ops.active_3d"
    bl_label = "3d Cursor_modal"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type == 'RIGHTMOUSE':
            bpy.ops.tp_ops.active_3d_int(mode="tp_active")         
        else:
            bpy.ops.tp_ops.active_3d_int(mode="tp_select")        
       
        if event.value == 'PRESS':
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.space_data.type == 'VIEW_3D':
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}



# REGISTER #

def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()
















