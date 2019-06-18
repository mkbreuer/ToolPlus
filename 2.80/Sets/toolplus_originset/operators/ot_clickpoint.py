# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#snippet from yadoob scripts
#http://blenderlounge.fr/forum/viewtopic.php?f=18&t=1438


# LOAD MODUL #
import bpy, bmesh
from mathutils import Vector
from bpy.props import IntProperty, FloatProperty



class VIEW3D_OT_snap_origin_to_click_point(bpy.types.Operator):
    """[SHIFT] = switch mode / [CRTL] = clear location / [CRTL+SHIFT] = only cursor"""
    bl_idname = "tpc_ops.snap_origin_to_click_point"
    bl_label = "Set Origin Modal"

    # property to define mouse event
    x : bpy.props.IntProperty()
    
    # print info in system console
    def __init__(self):
        # attribute instance
        self._activElem = None
        self._VertList = None
        print("Start")

    def __del__(self):
        print("End")

    def store(self):            
        # store settings
        self.store_select_x_mode : bpy.context.tool_settings.mesh_select_mode[0]  
        self.store_select_y_mode : bpy.context.tool_settings.mesh_select_mode[1] 
        self.store_select_z_mode : bpy.context.tool_settings.mesh_select_mode[2]              
        store_mode : bpy.context.object.mode



    def modal(self, context, event):

        # call event property
        self.x = event.mouse_x
       
        if event.type == 'RIGHTMOUSE': # confirm modal
           
            view_layer = bpy.context.view_layer        
            obj = view_layer.objects.active
            obj_edit = obj.data   

            ok = False

            if obj.type == 'CURVE' and len(obj_edit.splines) > 0:
                ok = True                
    
                splines = obj_edit.splines
                  
                for i in range(len(splines)):                                

                    if bpy.context.object.data.splines[i].type == "POLY":
                        for bp in splines[i].points:
                            if bp.select:

                                if event.ctrl and event.shift:
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    return {'FINISHED'}
                                else:                           
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                    if event.ctrl:
                                        bpy.ops.object.location_clear()  
                                   
                                    bpy.ops.object.mode_set ( mode = self.store_mode )

                                if event.shift:
                                    bpy.ops.object.editmode_toggle()  

                                return {'FINISHED'}   

                    elif bpy.context.object.data.splines[i].type == "NURBS":
                        for bp in splines[i].points:
                            if bp.select:

                                if event.ctrl and event.shift:
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    return {'FINISHED'}
                                else:                           
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                    if event.ctrl:
                                        bpy.ops.object.location_clear()  
                                   
                                    bpy.ops.object.mode_set ( mode = self.store_mode )

                                if event.shift:
                                    bpy.ops.object.editmode_toggle()  

                                return {'FINISHED'}   
                    
                    else:                                     
                        for bp in splines[i].bezier_points:                            
                            if bp.select_control_point or bp.select_right_handle or bp.select_left_handle:
                                #bp.select_control_point = True
                                #bp.select_right_handle = True
                                #bp.select_left_handle = True                               
                               
                                if event.ctrl and event.shift:
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    return {'FINISHED'}
                                else:                           
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                    if event.ctrl:
                                        bpy.ops.object.location_clear()  
                                   
                                    bpy.ops.object.mode_set ( mode = self.store_mode )

                                if event.shift:
                                    bpy.ops.object.editmode_toggle()  

                                return {'FINISHED'}   

   
            if obj.type == 'SURFACE' and len(obj_edit.splines) > 0:
                ok = True                
    
                splines = obj_edit.splines
                  
                for i in range(len(splines)):                                
                    for bp in splines[i].points:
                        if bp.select:

                            if event.ctrl and event.shift:
                                bpy.ops.view3d.snap_cursor_to_selected()
                                return {'FINISHED'}
                            else:                           
                                bpy.ops.view3d.snap_cursor_to_selected()
                                bpy.ops.object.editmode_toggle()
                                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                if event.ctrl:
                                    bpy.ops.object.location_clear()  
                               
                                bpy.ops.object.mode_set ( mode = self.store_mode )

                            if event.shift:
                                bpy.ops.object.editmode_toggle()  

                            return {'FINISHED'}   


   
            if obj.type == 'MESH' and len(obj_edit.vertices) > 0:  
                ok = True                       
                bm = bmesh.from_edit_mesh(obj_edit)
                activElem2Type = bm.select_history.active           
               
                if activElem2Type:               
                    if isinstance(activElem2Type, bmesh.types.BMFace): 
                        print("face")
                        print(activElem2Type)
                        for f in bm.faces :
                            if f.select :
                                
                                if event.ctrl and event.shift:
                                    bpy.ops.view3d.snap_cursor_to_active()
                                    bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                                    bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                                    bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                    #bpy.context.scene.cursor.location = loc
                                    return {'FINISHED'}
                                else:                           
                                    bpy.ops.view3d.snap_cursor_to_active()
                                    bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                                    bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                                    bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                    if event.ctrl:
                                        bpy.ops.object.location_clear()  
                                   
                                    bpy.ops.object.mode_set ( mode = self.store_mode )

                                if event.shift:
                                    bpy.ops.object.editmode_toggle()  

                                return {'FINISHED'}


                    elif isinstance(activElem2Type, bmesh.types.BMEdge):
                        print("edge")
                        listvert = []
                        for e in bm.edges :
                            if e.select :
                                for v in e.verts :
                                    listvert.append(v.co)
                                         
                                activElem2=(listvert[0]+listvert[1])/2
                                mat = obj.matrix_world
                                loc = mat @ activElem2

                                if event.ctrl and event.shift:
                                    bpy.ops.view3d.snap_cursor_to_active()
                                    bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                                    bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                                    bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                    #bpy.context.scene.cursor.location = loc
                                    return {'FINISHED'}
                                else:                           
                                    bpy.context.scene.cursor.location = loc                              
                                    bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                                    bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                                    bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                    if event.ctrl:
                                        bpy.ops.object.location_clear()  
                                   
                                    bpy.ops.object.mode_set ( mode = self.store_mode )

                                if event.shift:
                                    bpy.ops.object.editmode_toggle()  
                                    
                                return {'FINISHED'}

                   
                    elif isinstance(activElem2Type, bmesh.types.BMVert):
                        print("vertex")
                        activElem2=bm.select_history.active.co               
                        for v in bm.verts :
                            if v.select :   
                                mat = obj.matrix_world
                                loc = mat @ activElem2                            
     
                                if event.ctrl and event.shift:
                                    bpy.ops.view3d.snap_cursor_to_selected()
                                    bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                                    bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                                    bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                    #bpy.context.scene.cursor.location = loc
                                    return {'FINISHED'}
                                else:                           
                                    bpy.context.scene.cursor.location = loc                              
                                    bpy.context.tool_settings.mesh_select_mode[0] = self.store_select_x_mode
                                    bpy.context.tool_settings.mesh_select_mode[1] = self.store_select_y_mode
                                    bpy.context.tool_settings.mesh_select_mode[2] = self.store_select_z_mode
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')                                                                               

                                    if event.ctrl:
                                        bpy.ops.object.location_clear()  
                                   
                                    bpy.ops.object.mode_set ( mode = self.store_mode )
                     
                                if event.shift:
                                    bpy.ops.object.editmode_toggle()                        
                          
                                return {'FINISHED'}

                    return {'PASS_THROUGH'}
                        
                else :
                    return {'PASS_THROUGH'}


        if event.type in {'ESC',"TAB"}:
            return {'CANCELLED'}

        return {'PASS_THROUGH'}


    def invoke(self, context, event):
      
        #check if something selected
        if context.space_data.type == 'VIEW_3D':
          
            #check if something active
            if bpy.context.active_object is not None:   
                                             
                self.store_mode = bpy.context.object.mode 
                self.store_select_x_mode = bpy.context.tool_settings.mesh_select_mode[0]  
                self.store_select_y_mode = bpy.context.tool_settings.mesh_select_mode[1] 
                self.store_select_z_mode = bpy.context.tool_settings.mesh_select_mode[2]  
                
                #check if local mode
                if context.space_data.local_view is not None:                                
                    bpy.ops.view3d.localview() 
                else:
                    pass   
              
                if context.mode == "OBJECT":
                    bpy.ops.object.editmode_toggle()
              
           
                view_layer = bpy.context.view_layer        
                obj = view_layer.objects.active             
                if obj.type == 'MESH':
                    bpy.context.tool_settings.mesh_select_mode = (True, True, True)   
                    bpy.ops.mesh.select_all(action='DESELECT')
                else:
                    bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
                    bpy.ops.curve.select_all(action='DESELECT')

                wm = context.window_manager                           
                wm.modal_handler_add(self) 

                # call property
                self.x = event.mouse_x             
                
            else:
                pass   

            return {'RUNNING_MODAL'}

        else:
            self.report({'WARNING'}, "Must be 3D View")  
            return {'CANCELLED'}










class VIEW3D_OT_snap_origin_to_click_point_mode(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "tpc_ops.click_point_mode"
    bl_label = "Origin Modal Multi"
    
    # print info in system console
    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    # separate event types
    mode : bpy.props.StringProperty(default="")   

    _timer = None
    _activElem = None
    _VertList = None
   
    def modal(self, context, event):
          
        if event.type in {'ESC',"TAB"}:
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':                     
            obj = bpy.context.active_object
            mesh = obj.data
            bm = bmesh.from_edit_mesh(mesh)
            activElem2Type = bm.select_history.active           
           
            if activElem2Type:
               
                if isinstance(activElem2Type, bmesh.types.BMFace): 
                    print("face")
                    print(activElem2Type)
                    for f in bm.faces :
                        if f.select :
                            #mat = obj.matrix_world
                            #activElem2 = f.calc_center_bounds()
                            #loc = mat @ activElem2                        
                            
                            if "cursor" in self.mode: 
                                #bpy.context.scene.cursor.location = loc
                                bpy.ops.view3d.snap_cursor_to_active()
                           
                                if "obm" in self.mode:  
                                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

                                    if "clear" in self.mode:
                                        bpy.ops.object.location_clear()  

                                    if "edm" in self.mode:
                                        bpy.ops.object.editmode_toggle()  

                            return {'FINISHED'}


                elif isinstance(activElem2Type, bmesh.types.BMEdge):
                    print("edge")
                    listvert = []
                    for e in bm.edges :
                        if e.select :
                            for v in e.verts :
                                listvert.append(v.co)
                                     
                            activElem2=(listvert[0]+listvert[1])/2
                            mat = obj.matrix_world
                            loc = mat @ activElem2

                            if "cursor" in self.mode: 
                                bpy.context.scene.cursor.location = loc
     
                                if "obm" in self.mode:                    
                                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)                           
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                          
                                    if "clear" in self.mode:
                                        bpy.ops.object.location_clear()  

                                    if "edm" in self.mode:
                                        bpy.ops.object.editmode_toggle()  
                               
                            return {'FINISHED'}

               
                elif isinstance(activElem2Type, bmesh.types.BMVert):
                    print("vertex")
                    activElem2=bm.select_history.active.co               
                    for v in bm.verts :
                        if v.select :
                            mat = obj.matrix_world
                            loc = mat @ activElem2                            
 
                            if "cursor" in self.mode:  
                                bpy.context.scene.cursor.location = loc                            
                                
                                if "obm" in self.mode:                           
                                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
                               
                                    if "clear" in self.mode:
                                        bpy.ops.object.location_clear()  

                                    if "edm" in self.mode:
                                        bpy.ops.object.editmode_toggle()                          
                          
                            return {'FINISHED'}
   
                return {'PASS_THROUGH'}
                    
            else :
                return {'PASS_THROUGH'}
           
        return {'PASS_THROUGH'}


    def invoke(self, context, event):
      
        #check if something selected
        if bpy.context.active_object is not None:   
                                         
            #check if it's in local mode
            if context.space_data.local_view is not None:                                
                bpy.ops.view3d.localview() 
            else:
                pass   
          
            wm = context.window_manager
            self._timer = wm.event_timer_add(0.1, window=context.window)

            if context.mode == "OBJECT":
                bpy.ops.object.editmode_toggle()
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)   
            bpy.ops.mesh.select_all(action='DESELECT')
                       
            wm.modal_handler_add(self) 
            
        else:
            pass   

        return {'RUNNING_MODAL'}
   
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)



def register():
    bpy.utils.register_class(VIEW3D_OT_snap_origin_to_click_point)
    bpy.utils.register_class(VIEW3D_OT_snap_origin_to_click_point_mode)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_snap_origin_to_click_point)
    bpy.utils.unregister_class(VIEW3D_OT_snap_origin_to_click_point_mode)

if __name__ == "__main__":
    register()
