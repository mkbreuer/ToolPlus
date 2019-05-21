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
from bpy.props import IntProperty, FloatProperty


class VIEW3D_OT_Snap_Origin_Modal_Multi(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "tpc_ot.snaporigin_modal"
    bl_label = "Origin Modal Multi"
    
    # print info in system console
    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    # separate event types
    mode = bpy.props.StringProperty(default="")   

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
                            #loc = mat * activElem2                        
                            
                            if "cursor" in self.mode: 
                                #bpy.context.scene.cursor_location = loc
                                bpy.ops.view3d.snap_cursor_to_active()
                           
                                if "obm" in self.mode:  
                                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

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
                            loc = mat * activElem2

                            if "cursor" in self.mode: 
                                bpy.context.scene.cursor_location = loc
     
                                if "obm" in self.mode:                    
                                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)                           
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                          
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
                            loc = mat * activElem2                            
 
                            if "cursor" in self.mode:  
                                bpy.context.scene.cursor_location = loc                            
                                
                                if "obm" in self.mode:                           
                                    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                                    bpy.ops.object.editmode_toggle()
                                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                               
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
            self._timer = wm.event_timer_add(0.1, context.window)

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

