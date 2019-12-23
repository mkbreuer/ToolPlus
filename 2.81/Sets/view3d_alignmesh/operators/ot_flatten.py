# LOAD MODUL #
import bpy, bmesh, os
from bpy.props import IntProperty, FloatProperty

def get_addon_prefs():
    addon_name = os.path.splitext(__package__)[0]
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[addon_name].preferences
    return (addon_prefs)

class VIEW3D_OT_modal_snapflat(bpy.types.Operator):
    """modal flatten: face selections with use of select linked faces by threshold"""
    bl_idname = "tpc_ops.snapflat_modal"
    bl_label = "SnapFlat"
    
    # print info in system console
    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")
    
    _timer = None
    _activElem = None
    _VertList = None
        
    # property to define operator type        
    mode : bpy.props.StringProperty(default="") 

    threshold : bpy.props.FloatProperty(name="Threshold",  description="angle value to select linked face", default=0.0174533, min=0.0174533, max=3.14159, subtype='ANGLE')

    mesh_select_mode : bpy.props.EnumProperty(
      items = [("vertices", "Vertex", "enable vertex selection", 1),
               ("edges",    "Edge",   "enable edge selection"  , 2), 
               ("faces",    "Face",   "enable face selection"  , 3)], 
               name = "Mesh Select Mode",
               default = "vertices",
               description="type of mesh select mode when finish")

    # get the context arguments     
    def modal(self, context, event):
        prefs = get_addon_prefs()
        custom_threshold = prefs.threshold
        custom_mesh_select_mode = prefs.mesh_select_mode
        
        # stop running modal         
        if event.type in {'ESC',"TAB"}:
            self.cancel(context)
            return {'CANCELLED'}
      
        # run til event   
        if event.type == 'TIMER':                     
            view_layer = bpy.context.view_layer         
            obj = view_layer.objects.active 

            mesh = obj.data
            bm = bmesh.from_edit_mesh(mesh)
            activElem2Type = bm.select_history.active           
           
            if activElem2Type:               
                if isinstance(activElem2Type, bmesh.types.BMFace): 
                    #print info in system console
                    #print("face")
                    #print(activElem2Type)
                    for f in bm.faces :
                        if f.select :

                            bpy.ops.mesh.faces_select_linked_flat(sharpness=custom_threshold or self.custom_threshold)
                          
                            if "flatten_lpt" in self.mode: 
                                bpy.ops.mesh.looptools_flatten(influence=100, lock_x=False, lock_y=False, lock_z=False, plane='best_fit', restriction='none')

                            if "flatten_x" in self.mode: 
                                bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), orient_type='GLOBAL')
                              
                            if "flatten_y" in self.mode: 
                                bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), orient_type='GLOBAL')
                                
                            if "flatten_z" in self.mode: 
                                bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), orient_type='GLOBAL')

                            if "flatten_n" in self.mode: 
                                bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), orient_type='NORMAL')
                                
                            if "snap_for_select" in self.mode:                                                                 
                                bpy.ops.mesh.region_to_loop()

                            if "snap_for_uvs" in self.mode:                                                                 
                                bpy.ops.mesh.region_to_loop()
                                bpy.ops.mesh.mark_seam(clear=False)                                     

                            if "snap_for_sharp" in self.mode: 
                                bpy.ops.mesh.region_to_loop()                                 
                                bpy.ops.mesh.mark_sharp()                                                                                  
                           
                            if custom_mesh_select_mode == 'vertices' or self.mesh_select_mode == 'vertices':                             
                                bpy.context.tool_settings.mesh_select_mode = (True, False, False)                                                         
                            
                            if custom_mesh_select_mode == 'edges' or self.mesh_select_mode == 'edges':                           
                                bpy.context.tool_settings.mesh_select_mode = (False, True, False)                                                         
                           
                            if custom_mesh_select_mode == 'faces' or self.mesh_select_mode == 'faces':                                                         
                                bpy.context.tool_settings.mesh_select_mode = (False, False, True)                                                         
                            
                            return {'FINISHED'}

   
                return {'PASS_THROUGH'}
                    
            else :
                return {'PASS_THROUGH'}
           
        return {'PASS_THROUGH'}


    def invoke(self, context, event):
        view_layer = bpy.context.view_layer         
        obj = view_layer.objects.active       

        #check if something selected
        if obj is not None:   
                                         
            #check if it's in local mode
            if context.space_data.local_view is not None:                                
                bpy.ops.view3d.localview() 
            else:
                pass   
          
            # runs its self from a timer
            wm = context.window_manager
            self._timer = wm.event_timer_add(0.1, window=bpy.context.window)

            # do before modal
            if context.mode == "OBJECT":
                bpy.ops.object.editmode_toggle()
                
            bpy.context.tool_settings.mesh_select_mode = (False, False, True)   
            bpy.ops.mesh.select_all(action='DESELECT')
                       
            wm.modal_handler_add(self) 
            
        else:
            pass   

        return {'RUNNING_MODAL'}
   
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

