# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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

class VIEW3D_OT_Snapset_Modal(bpy.types.Operator):
        """set origin to a snap point"""
        bl_idname = "tpc_ot.snapset_modal"
        bl_label = "Snapset Modal"
        #bl_options = {'REGISTER', 'UNDO'}
       
        # print info in system console
        def __init__(self):
            print("Start")

        def __del__(self):
            print("End")

        def store(self):
            # get snap settings
            store_pivot : bpy.context.scene.tool_settings.transform_pivot_point                
            store_elements : bpy.context.scene.tool_settings.snap_elements
            store_target : bpy.context.scene.tool_settings.snap_target
            store_rotation : bpy.context.scene.tool_settings.use_snap_align_rotation
            store_project : bpy.context.scene.tool_settings.use_snap_project
            store_snap : bpy.context.scene.tool_settings.use_snap


        # property to define operator type in event
        mode : bpy.props.StringProperty(default="")   

        count = 0  

        # get the context arguments         
        def modal(self, context, event):

            # header info
            #context.area.header_text_set("SnapSet: %s - %s - %s" % (self.mode, event.type, event.value))     

            # do til event 
            self.count += 1
            if self.count == 1:                               
                bpy.ops.transform.translate('INVOKE_DEFAULT')

            # do event 
            elif event.type == 'LEFTMOUSE':

                # reload settings after event
                bpy.context.scene.tool_settings.transform_pivot_point = self.store_pivot
                bpy.context.scene.tool_settings.snap_elements = self.store_elements
                bpy.context.scene.tool_settings.snap_target = self.store_target
                bpy.context.scene.tool_settings.use_snap_align_rotation = self.store_rotation
                bpy.context.scene.tool_settings.use_snap_project = self.store_project
                bpy.context.scene.tool_settings.use_snap = self.store_snap              
                return {'FINISHED'}


            # do event
            elif event.type in {'RIGHTMOUSE', 'ESC'}:              
             
                # reload settings after event
                bpy.context.scene.tool_settings.transform_pivot_point = self.store_pivot
                bpy.context.scene.tool_settings.snap_elements = self.store_elements
                bpy.context.scene.tool_settings.snap_target = self.store_target
                bpy.context.scene.tool_settings.use_snap_align_rotation = self.store_rotation
                bpy.context.scene.tool_settings.use_snap_project = self.store_project
                bpy.context.scene.tool_settings.use_snap = self.store_snap
                return {'CANCELLED'}       

            return {'RUNNING_MODAL'}

     
        # do by execute
        def invoke(self, context, event):  
                    
            # check if something selected          
            if bpy.context.active_object is not None:

                # store exist settings
                self.store_pivot = bpy.context.scene.tool_settings.transform_pivot_point                
                self.store_elements = bpy.context.scene.tool_settings.snap_elements
                self.store_target = bpy.context.scene.tool_settings.snap_target
                self.store_rotation = bpy.context.scene.tool_settings.use_snap_align_rotation
                self.store_project = bpy.context.scene.tool_settings.use_snap_project
                self.store_snap = bpy.context.scene.tool_settings.use_snap


                # change settings: snap active to surfaces               
                if "GRID" in self.mode:   
                    bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
                    bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}
                    bpy.context.scene.tool_settings.use_snap_rotate = True
                    bpy.context.scene.tool_settings.use_snap_rotate = False   
                    bpy.context.scene.tool_settings.use_snap = True   
               
              
                # change settings: snap active to surfaces               
                if "PLACE" in self.mode:  
                    bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
                    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
                    bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
                    bpy.context.scene.tool_settings.use_snap_align_rotation = True
                    bpy.context.scene.tool_settings.use_snap_project = True
                    bpy.context.scene.tool_settings.use_snap = True   

                
                # change settings: snap active to surfaces               
                if "RETOPO" in self.mode:  
                    bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
                    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
                    bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
                    bpy.context.scene.tool_settings.use_snap_align_rotation = False     
                    bpy.context.scene.tool_settings.use_snap_project = True
                    bpy.context.scene.tool_settings.use_snap = True                 
 
               
                # change settings: snap active to surfaces = place 
                if "CUSTOM" in self.mode: 
                            
                    addon_prefs = context.preferences.addons[__package__].preferences
                 
                    bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_btM_pivot     
                    bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_btM_use_pivot 
                    bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_btM_elements}
                    bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_btM_target
                    bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_btM_absolute_grid               
                    bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_btM_snap_self
                    bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_btM_align_rotation       
                    bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_btM_project
                    bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_btM_peel_object
                    bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_btM_translate
                    bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_btM_rotation
                    bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_btM_scale

                    #bpy.context.scene.tool_settings.use_snap = prefs.tpc_use_snap
                    bpy.context.scene.tool_settings.use_snap = True                
                              
                context.window_manager.modal_handler_add(self)          
                return {'RUNNING_MODAL'}
            
            else:
                self.report({'WARNING'}, "Active space must be a 3D View")  
                return {'CANCELLED'}

