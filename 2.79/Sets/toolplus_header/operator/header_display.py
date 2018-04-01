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


bl_info = {
    "name": "T+ Header Display",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 1, 0),
    "blender": (2, 7, 9),
    "location": "3D View",
    "description": "",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer",
    "tracker_url": "",
    "category": "ToolPlus"}
    
    
# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from bpy_extras import view3d_utils



# OPERATOR #

class VIEW3D_TP_Header_Display_Set(bpy.types.Operator):
    """click: x-ray / shift+click: occlude wire / ctrl+click: backface culling / alt+click: draw_type wire or solid"""
    bl_idname = "tp_ops.header_display_set"
    bl_label = " Display"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def invoke(self, context, event):

        ev = []
        ev.append("Click")  

        if event.alt:
            ev.append("Alt")

            active_draw = bpy.context.object.draw_type == 'SOLID'    
            if active_draw == True:    
                bpy.context.object.draw_type = 'WIRE'   
                self.report({'INFO'}, "Draw: Wire")
            else:    
                bpy.context.object.draw_type = 'SOLID'       
                
                self.report({'INFO'}, "Draw: Solid")

        elif event.ctrl:
            ev.append("Ctrl")
            
            active_back = bpy.context.space_data.show_backface_culling    
            if active_back == True:    
                bpy.context.space_data.show_backface_culling  = False
                self.report({'INFO'}, "Backface: Off")

            else:
                bpy.context.space_data.show_backface_culling  = True
                self.report({'INFO'}, "Backface: On")

        elif event.shift:
            ev.append("Shift")

            active_hidden = bpy.context.space_data.show_occlude_wire        
            if active_hidden == True:    
                bpy.context.space_data.show_occlude_wire = False
                self.report({'INFO'}, "Occlude: Off")
            else:
                bpy.context.space_data.show_occlude_wire = True
                self.report({'INFO'}, "Occlude: On")

        else:
            active_xray = bpy.context.object.show_x_ray        
            if active_xray == True:       
                bpy.context.object.show_x_ray = False
                self.report({'INFO'}, "X-Ray: On")
            else:
                bpy.context.object.show_x_ray = True            
                self.report({'INFO'}, "X-Ray: Off")    

        #self.report({'INFO'}, "+".join(ev))

        return {'FINISHED'}



class VIEW3D_TP_Header_Wire_Set(bpy.types.Operator):
    """click: only active / shift+click: wire all / ctrl+click: toggle all edges"""
    bl_idname = "tp_ops.header_set_wire"
    bl_label = " Display"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def invoke(self, context, event):
    
        ev = []
        ev.append("Click")  

#        if event.alt:
#            ev.append("ALT")

        if event.ctrl:
            ev.append("Ctrl")

            for obj in bpy.data.objects:
            
                if obj.show_all_edges == False:
                    obj.show_all_edges = True
                    self.report({'INFO'}, "All Edges: Off")    
                else:
                    obj.show_all_edges = False        
                    self.report({'INFO'}, "All Edges: Off")    

        elif event.shift:
            ev.append("Shift")

            for obj in bpy.data.objects:
                 
                if obj.show_wire:
                    obj.show_wire = False
                    self.report({'INFO'}, "Wire: Off")    
                else:
                    obj.show_wire = True   
                    self.report({'INFO'}, "Wire: Off")    
        else:
            obj = bpy.context.object
                                
            if obj.show_wire:
                obj.show_wire = False
                self.report({'INFO'}, "Wire: Off")   
            else:
                obj.show_wire = True 
                self.report({'INFO'}, "Wire: Off")   
        
        #self.report({'INFO'}, "+".join(ev))

        return {'FINISHED'}




class VIEW3D_TP_Header_Set_Cursor(bpy.types.Operator):
        """set cursor to a snap point"""
        bl_idname = "tp_ops.header_set_cursor"
        bl_label = "Set Cursor"
        #bl_options = {'REGISTER', 'UNDO'}

        count = 0
        def __init__(self):
            print("Start")

        def __del__(self):
            print("End")

            # get the context arguments

        def modal(self, context, event):
            
            self.count += 1

            if self.count == 1:
                bpy.ops.transform.translate('INVOKE_DEFAULT')

            if event.type == 'LEFTMOUSE': # Confirm            
                
                self.selobj = context.active_object              

                bpy.ops.view3d.snap_cursor_to_selected()
                
                # delete empty
                bpy.ops.object.delete()

                # get first active back to set origin
                bpy.context.scene.objects.active = self.selobj
                self.selobj.select = True
                   
                return {'FINISHED'}
 
            elif event.type in {'RIGHTMOUSE', 'ESC'}: # Cancel
                bpy.ops.object.delete()                
                return {'CANCELLED'}

            return {'RUNNING_MODAL'}
 
 
        def invoke(self, context, event):  
            self.target = bpy.context.active_object  
            
            if context.space_data.type == 'VIEW_3D':
              
                self.scene = context.scene
                self.region = context.region
                self.rv3d = context.region_data
                self.mouse_co = event.mouse_region_x, event.mouse_region_y
                self.depth = view3d_utils.region_2d_to_vector_3d(self.region, self.rv3d, self.mouse_co)
                self.emp_co = view3d_utils.region_2d_to_location_3d(self.region, self.rv3d, self.mouse_co, self.depth)
                
                bpy.ops.object.select_all(action='DESELECT')
                
                # add custom objects
                bpy.ops.object.empty_add()
                
                context.object.location = self.emp_co
                context.window_manager.modal_handler_add(self)            

                # need active to set origin
                bpy.context.scene.objects.active = self.target

                return {'RUNNING_MODAL'}
            else:
                self.report({'WARNING'}, "Active space must be a View3d")  
                return {'CANCELLED'}



class VIEW3D_OT_View_Origin_Center(bpy.types.Operator):
    bl_label = "Center view to origin"
    bl_idname = 'view3d.view_origin_center'
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
            v3d = context.space_data
            if v3d.type == 'VIEW_3D':
                rv3d = v3d.region_3d
                current_cloc = v3d.cursor_location.xyz ### store
                v3d.cursor_location = (0, 0, 0)
                bpy.ops.view3d.view_center_cursor()
                v3d.cursor_location = current_cloc ### reload
            return {'FINISHED'}



######################################################



# REGISTRY # 
def register():
    bpy.utils.register_module(__name__)

def unregister():    
    bpy.utils.unregister_module(__name__)
   
if __name__ == "__main__":
    register()  

