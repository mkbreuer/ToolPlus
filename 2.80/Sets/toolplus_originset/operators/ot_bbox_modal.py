# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#based on yadoob script (Pierre Mervaillie)
#http://blenderlounge.fr/forum/viewtopic.php?f=18&t=1438


# LOAD MODUL #
import bpy, bmesh
from bpy.props import IntProperty, FloatProperty


class VIEW3D_OT_snap_origin_to_bbox(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "tpc_ops.snap_to_bbox"
    bl_label = "Snap BBox"
   
    _objRef = None
    _timer = None
    _activElem = None
    _VertList = None
    _CursorPos = None

    def modal(self, context, event):
        global _objRef
       
        if event.type in {'ESC',"TAB"}:
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':                     
            view_layer = bpy.context.view_layer                        

            obj = bpy.context.active_object
            mesh = obj.data
            bm = bmesh.from_edit_mesh(mesh)
            activElem2Type = bm.select_history.active           

            
            if activElem2Type:
               
                if isinstance(activElem2Type, bmesh.types.BMVert):
                    print("vertice")
                    activElem2=bm.select_history.active.co               
                    for v in bm.verts :
                        if v.select :
                            mat = obj.matrix_world
                            loc = mat @ activElem2
                            bpy.context.scene.cursor.location = loc
                            bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                            bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')
                            bpy.context.collection.objects.unlink(obj)
                            bpy.ops.object.delete({"selected_objects": [obj]})
                            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                                                     
                            view_layer.objects.active = _objRef
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
                            bpy.context.scene.cursor.location = loc
                            bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                            bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')
                            bpy.context.collection.objects.unlink(obj)
                            bpy.ops.object.delete({"selected_objects": [obj]})                            
                            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')         

                            view_layer.objects.active = _objRef
                            return {'FINISHED'}
     
     

                elif isinstance(activElem2Type, bmesh.types.BMFace): 
                    print("face")
                    print(activElem2Type)
                    for f in bm.faces :
                        if f.select :
                            mat = obj.matrix_world
                            activElem2 = f.calc_center_bounds()
                            loc = mat @ activElem2                        
                            bpy.context.scene.cursor.location = loc                                        
                            bpy.context.tool_settings.mesh_select_mode = (True, False, False)
                            bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')
                            bpy.context.collection.objects.unlink(obj)                            
                            bpy.ops.object.delete({"selected_objects": [obj]})                           
                            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

                            view_layer.objects.active = _objRef
                            return {'FINISHED'}
    

                
                return {'PASS_THROUGH'}
           
           
            else:
                return {'PASS_THROUGH'}
           
        return {'PASS_THROUGH'}


    def invoke(self, context, event):
        view_layer = bpy.context.view_layer 
        

        #check if something selected
        if view_layer.objects.active is not None:   

            #check if local mode
            if context.space_data.local_view is not None:                                
                bpy.ops.view3d.localview() 
            else:
                pass   

            global _objRef
             
            VertList=[]
            FaceList=[]
            VertBBList=[]

            wm = context.window_manager
            self._timer = wm.event_timer_add(0.1, window=context.window)

            _objRef = bpy.context.object
            _BB = _objRef.bound_box
           
            me = bpy.data.meshes.new('myMesh')
            BBob = bpy.data.objects.new('BBobject', me)
            BBob.show_name = True
           
            BBob.scale = _objRef.scale
            BBob.rotation_euler= _objRef.rotation_euler
            BBob.location = _objRef.location

            bpy.context.collection.objects.link(BBob)
            bm = bmesh.new()
            bm.from_mesh(me)

            for vert in _BB:
                VertBBList.append(vert)
                bm.verts.new((vert[0], vert[1], vert[2]))
           
            for v in bm.verts:           
                VertList.append(v)   
           
            _VertList = VertBBList 
           
            face1 = bm.faces.new((VertList[0], VertList[1], VertList[2],VertList[3]))
            face2 = bm.faces.new((VertList[0], VertList[4], VertList[5],VertList[1]))
            face3 = bm.faces.new((VertList[3], VertList[7], VertList[4],VertList[0]))
            face4 = bm.faces.new((VertList[2], VertList[1], VertList[5],VertList[6]))
            face5 = bm.faces.new((VertList[3], VertList[2], VertList[6],VertList[7]))
            face6 = bm.faces.new((VertList[4], VertList[5], VertList[6],VertList[7]))
                   
            bm.verts.index_update()
            bm.to_mesh(me)
      
            view_layer.objects.active = BBob  
           
            _objRef.select_set(state=False)
            bpy.context.object.display_type = 'WIRE'
            bpy.context.object.show_in_front = True
            bpy.ops.object.editmode_toggle('INVOKE_REGION_WIN')
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
            _objRef.select_set(state=True)
            wm.modal_handler_add(self) 

        else:
            pass   

        return {'RUNNING_MODAL'}
   
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)



def register():
    bpy.utils.register_class(VIEW3D_OT_snap_origin_to_bbox)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_snap_origin_to_bbox)

if __name__ == "__main__":
    register()
