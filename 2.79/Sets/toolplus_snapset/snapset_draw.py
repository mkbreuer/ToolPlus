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
import blf
import bgl

def draw_callback_px_grid(self, context):
    
    addon_key   = __package__.split(".")[0]
    addon_prefs = bpy.context.user_preferences.addons[addon_key].preferences 

    text_width  = addon_prefs.text_width
    text_height = addon_prefs.text_height

    text_pos_x = addon_prefs.text_pos_x
    text_pos_y = addon_prefs.text_pos_y
    
    text_color = addon_prefs.text_color

    font_id_0 = 0  
    font_id_1 = 0     
    font_id_2 = 0  
    font_id_3 = 0  

    bgl.glColor3f(*text_color)

    blf.position(font_id_0, (text_pos_x), (text_pos_y+60), 0)    
    blf.size(font_id_0, text_width, text_height+25)
    blf.draw(font_id_0, "Preset: Grid")

    blf.position(font_id_1, (text_pos_x), (text_pos_y+40), 0)    
    blf.size(font_id_1, text_width, text_height)
    blf.draw(font_id_1, "Snap:   Increment")

    blf.position(font_id_2, (text_pos_x), (text_pos_y+20), 0)    
    blf.size(font_id_2, text_width, text_height)
    blf.draw(font_id_2, "Pivot:  Bounding Box Center")


    blf.position(font_id_3, (text_pos_x), (text_pos_y+0), 0)    
    blf.size(font_id_3, text_width, text_height)
    blf.draw(font_id_3, "Active: Grid Absolute")

    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0, 1.0)


class VIEW3D_TP_Snapset_Grid_Modal(bpy.types.Operator):
    """snap to increments of grid"""
    bl_idname = "tp_ops.grid_modal"
    bl_label = "Absolute Grid"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        bpy.ops.tp_ops.grid()
        
        if event.value == 'PRESS':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'FINISHED'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_grid, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}




def draw_callback_px_place(self, context):
    
    addon_key   = __package__.split(".")[0]
    addon_prefs = bpy.context.user_preferences.addons[addon_key].preferences 

    text_width  = addon_prefs.text_width
    text_height = addon_prefs.text_height

    text_pos_x = addon_prefs.text_pos_x
    text_pos_y = addon_prefs.text_pos_y
    
    text_color = addon_prefs.text_color

    font_id_0 = 0  
    font_id_1 = 0     
    font_id_2 = 0  
    font_id_3 = 0  
    font_id_4 = 0  
    font_id_5 = 0  

    bgl.glColor3f(*text_color)

    blf.position(font_id_0, (text_pos_x), (text_pos_y+100), 0)    
    blf.size(font_id_0, text_width, text_height+25)
    blf.draw(font_id_0, "Preset: Place")

    blf.position(font_id_1, (text_pos_x), (text_pos_y+80), 0)    
    blf.size(font_id_1, text_width, text_height)
    blf.draw(font_id_1, "Snap: Face")

    blf.position(font_id_2, (text_pos_x), (text_pos_y+60), 0)    
    blf.size(font_id_2, text_width, text_height)
    blf.draw(font_id_2, "Pivot: Active Element")

    blf.position(font_id_3, (text_pos_x), (text_pos_y+40), 0)    
    blf.size(font_id_3, text_width, text_height)
    blf.draw(font_id_3, "Target: Closest")

    blf.position(font_id_4, (text_pos_x), (text_pos_y+20), 0)    
    blf.size(font_id_4, text_width, text_height)
    blf.draw(font_id_4, "Active: Align Rotation")

    blf.position(font_id_5, (text_pos_x), (text_pos_y+0), 0)    
    blf.size(font_id_5, text_width, text_height)
    blf.draw(font_id_5, "Active: Snap Project")
    
    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0, 1.0)



class VIEW3D_TP_Snapset_Place_Modal(bpy.types.Operator):
    """snap to object surface with normal rotation"""
    bl_idname = "tp_ops.place_modal"
    bl_label = "Place Object"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        bpy.ops.tp_ops.place()
        
        if event.value == 'PRESS':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_place, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}



def draw_callback_px_retopo(self, context):
    
    addon_key   = __package__.split(".")[0]
    addon_prefs = bpy.context.user_preferences.addons[addon_key].preferences 

    text_width  = addon_prefs.text_width
    text_height = addon_prefs.text_height

    text_pos_x = addon_prefs.text_pos_x
    text_pos_y = addon_prefs.text_pos_y
    
    text_color = addon_prefs.text_color

    font_id_0 = 0  
    font_id_1 = 0     
    font_id_2 = 0  
    font_id_3 = 0  

    bgl.glColor3f(*text_color)

    blf.position(font_id_0, (text_pos_x), (text_pos_y+60), 0)    
    blf.size(font_id_0, text_width, text_height+25)
    blf.draw(font_id_0, "Preset: Retopo")

    blf.position(font_id_1, (text_pos_x), (text_pos_y+40), 0)    
    blf.size(font_id_1, text_width, text_height)
    blf.draw(font_id_1, "Snap:   Face")

    blf.position(font_id_2, (text_pos_x), (text_pos_y+20), 0)    
    blf.size(font_id_2, text_width, text_height)
    blf.draw(font_id_2, "Pivot:  Bounding Box Center")

    blf.position(font_id_3, (text_pos_x), (text_pos_y+0), 0)    
    blf.size(font_id_3, text_width, text_height)
    blf.draw(font_id_3, "Target: Closest")

    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0, 1.0)


class VIEW3D_TP_Snapset_Retopo_Modal(bpy.types.Operator):
    """snap to surface of another object"""
    bl_idname = "tp_ops.retopo_modal"
    bl_label = "Mesh Retopo"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        bpy.ops.tp_ops.retopo()
        
        if event.value == 'PRESS':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_retopo, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}





def draw_callback_px_active(self, context):
    
    addon_key   = __package__.split(".")[0]
    addon_prefs = bpy.context.user_preferences.addons[addon_key].preferences 

    text_width  = addon_prefs.text_width
    text_height = addon_prefs.text_height

    text_pos_x = addon_prefs.text_pos_x
    text_pos_y = addon_prefs.text_pos_y
    
    text_color = addon_prefs.text_color

    font_id_0 = 0  
    font_id_1 = 0     
    font_id_2 = 0  
    font_id_3 = 0  

    bgl.glColor3f(*text_color)

    blf.position(font_id_0, (text_pos_x), (text_pos_y+60), 0)    
    blf.size(font_id_0, text_width, text_height+25)
    blf.draw(font_id_0, "Preset: Active")

    blf.position(font_id_1, (text_pos_x), (text_pos_y+40), 0)    
    blf.size(font_id_1, text_width, text_height)
    blf.draw(font_id_1, "Snap:   Vertex")

    blf.position(font_id_2, (text_pos_x), (text_pos_y+20), 0)    
    blf.size(font_id_2, text_width, text_height)
    blf.draw(font_id_2, "Pivot:  Median Point")

    blf.position(font_id_3, (text_pos_x), (text_pos_y+0), 0)    
    blf.size(font_id_3, text_width, text_height)
    blf.draw(font_id_3, "Target: Active")

    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0, 1.0)
    


class VIEW3D_TP_Snapset_Active_Modal(bpy.types.Operator):
    """snap selected to active vertex"""
    bl_idname = "tp_ops.active_snap_modal"
    bl_label = "Snap Verts"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        bpy.ops.tp_ops.active_snap()
        
        if event.value == 'PRESS':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_active, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}




def draw_callback_px_closest(self, context):
    
    addon_key   = __package__.split(".")[0]
    addon_prefs = bpy.context.user_preferences.addons[addon_key].preferences 

    text_width  = addon_prefs.text_width
    text_height = addon_prefs.text_height

    text_pos_x = addon_prefs.text_pos_x
    text_pos_y = addon_prefs.text_pos_y
    
    text_color = addon_prefs.text_color

    font_id_0 = 0  
    font_id_1 = 0     
    font_id_2 = 0  
    font_id_3 = 0  

    bgl.glColor3f(*text_color)

    blf.position(font_id_0, (text_pos_x), (text_pos_y+60), 0)    
    blf.size(font_id_0, text_width, text_height+25)
    blf.draw(font_id_0, "Preset: Closest")

    blf.position(font_id_1, (text_pos_x), (text_pos_y+40), 0)    
    blf.size(font_id_1, text_width, text_height)
    blf.draw(font_id_1, "Snap:   Vertex")

    blf.position(font_id_2, (text_pos_x), (text_pos_y+20), 0)    
    blf.size(font_id_2, text_width, text_height)
    blf.draw(font_id_2, "Pivot:  Median Point")

    blf.position(font_id_3, (text_pos_x), (text_pos_y+0), 0)    
    blf.size(font_id_3, text_width, text_height)
    blf.draw(font_id_3, "Target: Closest")

    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0, 1.0)



class VIEW3D_TP_Snapset_Closest_Modal(bpy.types.Operator):
    """snap selected to closest median"""
    bl_idname = "tp_ops.closest_snap_modal"
    bl_label = "Snap Closest"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        bpy.ops.tp_ops.closest_snap()
        
        if event.value == 'PRESS':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_closest, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}




def draw_callback_px_cursor(self, context):
    
    addon_key   = __package__.split(".")[0]
    addon_prefs = bpy.context.user_preferences.addons[addon_key].preferences 

    text_width  = addon_prefs.text_width
    text_height = addon_prefs.text_height

    text_pos_x = addon_prefs.text_pos_x
    text_pos_y = addon_prefs.text_pos_y
    
    text_color = addon_prefs.text_color

    font_id_0 = 0  
    font_id_1 = 0     
    font_id_2 = 0  
    font_id_3 = 0  

    bgl.glColor3f(*text_color)

    blf.position(font_id_0, (text_pos_x), (text_pos_y+60), 0)    
    blf.size(font_id_0, text_width, text_height+25)
    blf.draw(font_id_0, "Preset: 3D Cursor")

    blf.position(font_id_1, (text_pos_x), (text_pos_y+40), 0)    
    blf.size(font_id_1, text_width, text_height)
    blf.draw(font_id_1, "Snap:   Vertex")

    blf.position(font_id_2, (text_pos_x), (text_pos_y+20), 0)    
    blf.size(font_id_2, text_width, text_height)
    blf.draw(font_id_2, "Pivot:  Median Point")

    blf.position(font_id_3, (text_pos_x), (text_pos_y+0), 0)    
    blf.size(font_id_3, text_width, text_height)
    blf.draw(font_id_3, "Target: Closest")

    # restore opengl defaults
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor3f(0.0, 0.0, 0.0, 1.0)
    


class VIEW3D_TP_Snapset_Active_3d_Modal(bpy.types.Operator):
    """set 3D cursor >> LMB: to selected / >> RMB: to active """
    bl_idname = "tp_ops.active_3d_modal"
    bl_label = "3d Cursor_modal"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type == 'RIGHTMOUSE':

            bpy.ops.tp_ops.active_3d_int(mode="tp_active")

        else:
            bpy.ops.tp_ops.active_3d_int(mode="tp_select")
        

        if event.value == 'PRESS':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_cursor, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}





# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
