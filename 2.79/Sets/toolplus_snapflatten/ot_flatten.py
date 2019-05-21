# LOAD MODUL #
import bpy, bmesh
from bpy.props import IntProperty, FloatProperty


class VIEW3D_OT_SnapFlatten_Modal(bpy.types.Operator):
    """use linked faces and flatt them, after selecting a mesh face"""
    bl_idname = "tpc_ot.snapflatten_modal"
    bl_label = "SnapFlatten Modal"
    
    # print info in system console
    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    _timer = None
    _activElem = None
    _VertList = None
        
    # property to define operator type        
    mode = bpy.props.StringProperty(default="") 

    # get the context arguments     
    def modal(self, context, event):
        
        # stop running modal         
        if event.type in {'ESC',"TAB"}:
            self.cancel(context)
            return {'CANCELLED'}
      
        # run til event   
        if event.type == 'TIMER':
            # snippet from yadoob scripts 
            # http://blenderlounge.fr/forum/viewtopic.php?f=18&t=1438                    
            obj = bpy.context.active_object
            mesh = obj.data
            bm = bmesh.from_edit_mesh(mesh)
            activElem2Type = bm.select_history.active           
           
            if activElem2Type:
               
                if isinstance(activElem2Type, bmesh.types.BMFace): 
                    # print info in system console
                    print("face")
                    print(activElem2Type)
                    for f in bm.faces :
                        if f.select :
                            mat = obj.matrix_world
                            activElem2 = f.calc_center_bounds()
                            loc = mat * activElem2

                            panel_prefs = context.user_preferences.addons[__package__].preferences                            
                            prefs = panel_prefs.threshold                            
                            bpy.ops.mesh.faces_select_linked_flat(sharpness=prefs)
                          
                            if "flatten_lpt" in self.mode: 
                                bpy.ops.mesh.looptools_flatten(influence=100, lock_x=False, lock_y=False, lock_z=False, plane='best_fit', restriction='none')

                            if "flatten_x" in self.mode: 
                                bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                              
                            if "flatten_y" in self.mode: 
                                bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                                
                            if "flatten_z" in self.mode: 
                                bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

                            if "flatten_n" in self.mode: 
                                bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='NORMAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                                
                            bpy.context.tool_settings.mesh_select_mode = (True, False, False)                             
                            
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
          
            # runs its self from a timer
            wm = context.window_manager
            self._timer = wm.event_timer_add(0.1, context.window)

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

