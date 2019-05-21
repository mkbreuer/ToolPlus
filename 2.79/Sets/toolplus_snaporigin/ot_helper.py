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
from bpy_extras import view3d_utils

class VIEW3D_OT_Snap_Origin_to_Helper(bpy.types.Operator):
        """set origin to a snap point"""
        bl_idname = "tpc_ot.snap_to_helper"
        bl_label = "Snap Helper"
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
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')  
                   
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
