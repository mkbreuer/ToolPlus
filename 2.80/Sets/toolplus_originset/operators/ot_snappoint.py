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
#https://docs.blender.org/api/blender2.8/bpy.ops.html
#https://docs.blender.org/api/blender_python_api_2_77_0/bpy.types.Operator.html?highlight=modal#bpy.types.Operator.modal
#https://blender.stackexchange.com/questions/8796/custom-modal-operator-event-timing
#https://docs.blender.org/api/blender_python_api_2_77_0/bpy_extras.view3d_utils.html?highlight=view3d_utils#module-bpy_extras.view3d_utils
#https://blender.stackexchange.com/questions/7631/python-make-an-operator-update-ui-after-executed
#



# LOAD MODULS & PROPERTIES #    
import bpy
from bpy.props import (BoolProperty, IntProperty)
from bpy_extras import view3d_utils


class VIEW3D_OT_origin_to_snap_point(bpy.types.Operator):
        """[LMB] = Vertex // [+SHIFT] = Edge // [+CTRL] = Face // [ALT]=  Grid // [LMB+] than [ALT+LMB] = only Cursor"""
        bl_idname = "tpc_ops.origin_to_snap_point"
        bl_label = "SnapPoint"
        #bl_options = {'REGISTER', 'UNDO'}

        # property to enable wire display
        use_wire_all : bpy.props.BoolProperty(name="Wire All", default=False)  

        # property to define mouse event
        x : bpy.props.IntProperty()
        
        # store global static member
        #count = 0
        
        # show info in system console
        def __init__(self):
            # attribute instance
            self.count = 0
            print("Start")

        def __del__(self):
            print("End")

        def store(self):            
            # store settings
            store_pivot : bpy.context.scene.tool_settings.transform_pivot_point                
            store_elements : bpy.context.scene.tool_settings.snap_elements
            store_target : bpy.context.scene.tool_settings.snap_target
            store_rotation : bpy.context.scene.tool_settings.use_snap_align_rotation
            store_project : bpy.context.scene.tool_settings.use_snap_project
            store_snap : bpy.context.scene.tool_settings.use_snap

        # get the context arguments
        def modal(self, context, event):
            
            self.count += 1
            if self.count == 1:
                # call standard operator one time and keep it til event
                # all properties are available in the header
                bpy.ops.transform.translate('INVOKE_DEFAULT')                                              

            if event.type == 'LEFTMOUSE': # confirm modal

                view_layer = bpy.context.view_layer                        
                self.target = view_layer.objects.active             

                # cursor to selected
                bpy.ops.view3d.snap_cursor_to_selected()
                
                # delete empty helper
                bpy.ops.object.delete()
                
                # use modal keymap after leftmouse event
                if event.alt:
                    # set only cursor
                    pass
                else:  
                    # get first active back to set origin
                    view_layer.objects.active = self.target
                    self.target.select_set(state = True, view_layer = None)
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')  
              
                # call event property
                self.x = event.mouse_x

                # disable wire display 
                if self.use_wire_all == True:
                    for obj in bpy.data.objects:
                        obj.show_all_edges = False                              
                        obj.show_wire = False   

                # reload stored settings after confirm event
                bpy.context.scene.tool_settings.transform_pivot_point = self.store_pivot
                bpy.context.scene.tool_settings.snap_elements = self.store_elements
                bpy.context.scene.tool_settings.snap_target = self.store_target
                bpy.context.scene.tool_settings.use_snap_align_rotation = self.store_rotation
                bpy.context.scene.tool_settings.use_snap_project = self.store_project
                bpy.context.scene.tool_settings.use_snap = self.store_snap

                return {'FINISHED'}
 
          
            elif event.type in {'RIGHTMOUSE', 'ESC'}: # cancel modal
              
                # remove empty helper
                bpy.ops.object.delete()                
              
                # disable wire display 
                if self.use_wire_all == True:
                    for obj in bpy.data.objects:
                        obj.show_all_edges = False                              
                        obj.show_wire = False   

                # reload stored settings after cancle event
                bpy.context.scene.tool_settings.transform_pivot_point = self.store_pivot
                bpy.context.scene.tool_settings.snap_elements = self.store_elements
                bpy.context.scene.tool_settings.snap_target = self.store_target
                bpy.context.scene.tool_settings.use_snap_align_rotation = self.store_rotation
                bpy.context.scene.tool_settings.use_snap_project = self.store_project
                bpy.context.scene.tool_settings.use_snap = self.store_snap

                return {'CANCELLED'}

            return {'RUNNING_MODAL'}
 
 
        def invoke(self, context, event):  
            view_layer = bpy.context.view_layer 
            self.target = view_layer.objects.active  
                
            if context.space_data.type == 'VIEW_3D':
                if context.object is not None :
             
                    # store exist snap settings
                    self.store_pivot = bpy.context.scene.tool_settings.transform_pivot_point                
                    self.store_elements = bpy.context.scene.tool_settings.snap_elements
                    self.store_target = bpy.context.scene.tool_settings.snap_target
                    self.store_rotation = bpy.context.scene.tool_settings.use_snap_align_rotation
                    self.store_project = bpy.context.scene.tool_settings.use_snap_project
                    self.store_snap = bpy.context.scene.tool_settings.use_snap 

                    # get submodule
                    self.scene = context.scene
                    self.region = context.region
                    self.rv3d = context.region_data
                    self.mouse_co = event.mouse_region_x, event.mouse_region_y
                    
                    # return a direction vector from the viewport at the specific 2d region coordinate.
                    self.depth = view3d_utils.region_2d_to_vector_3d(self.region, self.rv3d, self.mouse_co)
                    
                    # return a 3d location from the region relative 2d coords, aligned with depth_location
                    self.emp_co = view3d_utils.region_2d_to_location_3d(self.region, self.rv3d, self.mouse_co, self.depth)

                    # enable wire display 
                    if self.use_wire_all == True:
                        for obj in bpy.data.objects:
                            obj.show_all_edges = True                              
                            obj.show_wire = True    
                    
                    # use snap presets with modal keymap
                    ev = []
                    if event.ctrl:
                        print('CRTL: Snap Face')                       
                        bpy.context.scene.tool_settings.use_snap = True    
                        bpy.context.scene.tool_settings.snap_elements = {'FACE'}
                        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT' 

                    elif event.shift:
                        print('SHIFT: Snap Edge')             
                        bpy.context.scene.tool_settings.use_snap = True   
                        bpy.context.scene.tool_settings.snap_elements = {'EDGE'} 
                        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'                     

                    elif event.alt:
                        print("ALT: Snap Incremental")            
                        bpy.context.scene.tool_settings.use_snap = True
                        bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}
                        bpy.context.scene.tool_settings.use_snap_grid_absolute = True            
                  
                    else:
                        print("LMB: Snap Vertex")
                        bpy.context.scene.tool_settings.use_snap = True           
                        bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}          
               
                        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'                    
                  
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.ops.object.empty_add()

                    # move origin with emtpy 
                    context.object.location = self.emp_co
                    context.window_manager.modal_handler_add(self) 
                    
                    # call property
                    self.x = event.mouse_x                
                               
                    # reload active
                    view_layer.objects.active = self.target
                  
                    # show system console info               
                    self.report({'INFO'}, "+".join(ev)) 

                    return {'RUNNING_MODAL'}
             
                else:
                    self.report({'WARNING'}, "No active object, could not finish")
                    return {'CANCELLED'}
            else:
                self.report({'WARNING'}, "Must be 3D View")  
                return {'CANCELLED'}








def register():
    bpy.utils.register_class(VIEW3D_OT_origin_to_snap_point)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_origin_to_snap_point)

if __name__ == "__main__":
    register()
