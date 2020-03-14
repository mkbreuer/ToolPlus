# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from bpy.app.handlers import persistent

import math
import mathutils
from mathutils import *



class VIEW3D_OT_place_cursor(bpy.types.Operator):
    """Default Snap PlaceCursor > Button I Settings"""
    bl_idname = "tpc_ot.place_cursor"
    bl_label = "PlaceCursor"
    bl_options = {"REGISTER", 'UNDO'}

    depth : BoolProperty(name="Surface Project", description="project onto the surface", default=True)

    orient : bpy.props.EnumProperty(
      items = [("NONE",   "None",      "leave orientation unchanged"             ,1),
               ("VIEW",   "View",      "orient to the viewport"                  ,2),
               ("XFORM",  "Transform", "orient to the current transform setting" ,3), 
               ("GEOM",   "Geometry",   "match the surface normal"               ,4)], 
               name = "Orientation",
               default = "GEOM",
               description="Preset viewpoint to use")

    object_align : bpy.props.EnumProperty(
      items = [("WORLD",   "World",    "align new objects to world cooridnate system"  ,1),
               ("VIEW",   "View",      "align new objects to active 3D view"           ,2),
               ("CURSOR",  "3D Cursor",  "align new objects to 3D cursors rotation"    ,3)], 
               name = "Align to",
               default = "CURSOR",
               description="")
        
    rotation : FloatProperty(name="Rotate Cursor", description="", default=0, min= -360, max = 360, subtype='PERCENTAGE')

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_AREA'
        layout.operator_context = "INVOKE_DEFAULT"       

        box = layout.box().column(align=True) 

        row = box.row(align=True)         
        row.label(text="Surface Project")
        row.prop(self, "depth", text='')

        box.separator()       
       
        row = box.row(align=True)  
        row.label(text="Orientation")       
        row.prop(self, "orient", text='')
     
        box.separator()

        row = box.row(align=True)  
        row.label(text="Align to")
        row.prop(self, "object_align", text='')
 
        box.separator()

        row = box.row(align=True)  
        row.label(text="Rotation")
        row.prop(self, "rotation", text='')
 
        box.separator()


    def execute(self, context):

        addon_prefs = context.preferences.addons[__package__].preferences

        bpy.context.scene.tool_settings.use_snap = addon_prefs.tpc_use_snap

        bpy.context.space_data.overlay.show_cursor = True

        bpy.ops.wm.tool_set_by_id(name="builtin.cursor")
        
        #https://docs.blender.org/api/current/bpy.ops.view3d.html    
        bpy.ops.view3d.cursor3d(use_depth=self.depth, orientation=self.orient)
        bpy.context.preferences.edit.object_align=self.object_align

        bpy.context.scene.tool_settings.transform_pivot_point = addon_prefs.prop_bti_pivot 
               
        #bpy.context.scene.tool_settings.snap_elements = {'VERTEX', 'EDGE', 'FACE'}        
        bpy.context.scene.tool_settings.snap_elements = {addon_prefs.prop_bti_elements}
        
        bpy.context.scene.tool_settings.snap_target = addon_prefs.prop_bti_target
        bpy.context.scene.tool_settings.use_snap_align_rotation = addon_prefs.prop_bti_align_rotation  
     
        bpy.context.scene.tool_settings.use_transform_pivot_point_align = addon_prefs.prop_bti_use_pivot             
        bpy.context.scene.tool_settings.use_snap_grid_absolute = addon_prefs.prop_bti_absolute_grid               
        bpy.context.scene.tool_settings.use_snap_self = addon_prefs.prop_bti_snap_self     
        bpy.context.scene.tool_settings.use_snap_project = addon_prefs.prop_bti_project
        bpy.context.scene.tool_settings.use_snap_peel_object = addon_prefs.prop_bti_peel_object
        bpy.context.scene.tool_settings.use_snap_translate = addon_prefs.prop_bti_translate
        bpy.context.scene.tool_settings.use_snap_rotate = addon_prefs.prop_bti_rotation
        bpy.context.scene.tool_settings.use_snap_scale = addon_prefs.prop_bti_scale
      
        bpy.context.scene.cursor.rotation_euler[2] = self.rotation
        return {'FINISHED'}  





def func_cursor_copy(self, context):
    
    view_layer = bpy.context.view_layer  
    selected = bpy.context.selected_objects        
    obj_list = [obj for obj in selected]
    if obj_list:

        for obj in obj_list:  
            view_layer.objects.active = obj   
            obj.select_set(state=True) 
                
            # ROTATION
            if self.copy_rot == True:
                obj.rotation_euler[0] = bpy.context.scene.cursor.rotation_euler[0]
                obj.rotation_euler[1] = bpy.context.scene.cursor.rotation_euler[1]
                obj.rotation_euler[2] = bpy.context.scene.cursor.rotation_euler[2]                
                rot_x = 'X' 
                rot_y = 'Y' 
                rot_z = 'Z' 

            else:
                if self.copy_rot_x == True:
                    obj.rotation_euler[0] = bpy.context.scene.cursor.rotation_euler[0]
                    rot_x = 'X'                   
                else:                        
                    rot_x = '-' 

                if self.copy_rot_y == True:
                    obj.rotation_euler[1] = bpy.context.scene.cursor.rotation_euler[1]         
                    rot_y = 'Y'                                        
                else:                        
                    rot_y = '-' 

                if self.copy_rot_z == True:
                    obj.rotation_euler[2] = bpy.context.scene.cursor.rotation_euler[2]
                    rot_z = 'Z'                    
                else:                        
                    rot_z = '-'                   


            # LOCATION             
            if self.copy_loc == True:
                obj.location[0] = bpy.context.scene.cursor.location[0]
                obj.location[1] = bpy.context.scene.cursor.location[1]
                obj.location[2] = bpy.context.scene.cursor.location[2]                     
                loc_x = 'X' 
                loc_y = 'Y' 
                loc_z = 'Z' 
          
            else:

                if self.copy_loc_x == True:
                    obj.location[0] = bpy.context.scene.cursor.location[0]
                    loc_x = 'X'     
                else:
                    loc_x = '-'                    
 
                if self.copy_loc_y == True:
                    obj.location[1] = bpy.context.scene.cursor.location[1]         
                    loc_y = 'Y'                   
                else:
                    loc_y = '-'   

                if self.copy_loc_z == True:
                    obj.location[2] = bpy.context.scene.cursor.location[2]
                    loc_z = 'Z'                    
                else:
                    loc_z = '-'   

       
          
            message = ("Copy: " + rot_x + rot_y + rot_z + ' Rotation' + ' / ' + loc_x + loc_y + loc_z + ' Location')
            self.report({'INFO'}, message)

    else:
        self.report({'INFO'}, 'No Selection!')       



class VIEW3D_OT_3d_cursor_copy(bpy.types.Operator):
    """copy 3d cursor rotation to selected"""
    bl_idname = "tpc_ot.cursor_copy"
    bl_label = "Cursor Copy"
    bl_options = {"REGISTER", 'UNDO'}

    copy_loc : BoolProperty(name="XYZ",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 
    copy_loc_x : BoolProperty(name="X",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 
    copy_loc_y : BoolProperty(name="Y",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 
    copy_loc_z : BoolProperty(name="Z",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 

    copy_rot : BoolProperty(name="XYZ",  description="toggle axis", default=True, options={'SKIP_SAVE'}) 
    copy_rot_x : BoolProperty(name="X",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 
    copy_rot_y : BoolProperty(name="Y",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 
    copy_rot_z : BoolProperty(name="Z",  description="toggle axis", default=False, options={'SKIP_SAVE'}) 

    def draw(self, context):
        layout = self.layout
       
        box = layout.box().column(align=True)   

        row = box.row(align=True)
        row.label(text="Rotation:") 

        sub1 = row.column(align=True)
        display_rota = not self.copy_rot  
        sub1.prop(self, "copy_rot")        
        row.label(text=" ")      
        row.label(text=" ")      
        
        row = box.row(align=True)
        row.label(text="Axis") 

        sub1 = row.row(align=True)
        sub1.active = display_rota  
        #sub1.scale_x = 0.5
        sub1.prop(self, "copy_rot_x")        
        sub1.prop(self, "copy_rot_y")        
        sub1.prop(self, "copy_rot_z")        

        box.separator()

        row = box.row(align=True)
        row.label(text="Location:") 

        sub1 = row.column(align=True)
        display_loc = not self.copy_loc  
        sub1.prop(self, "copy_loc")        
        row.label(text=" ")      
        row.label(text=" ")      
        
        row = box.row(align=True)
        row.label(text="Axis") 

        sub1 = row.row(align=True)
        sub1.active = display_loc  
        #sub1.scale_x = 0.5
        sub1.prop(self, "copy_loc_x")        
        sub1.prop(self, "copy_loc_y")        
        sub1.prop(self, "copy_loc_z") 
        
        box.separator()


    def execute(self, context):
        func_cursor_copy(self, context)
        return {'FINISHED'}  


    #def invoke(self, context, event):
        #return context.window_manager.invoke_props_popup(self, event)  


class VIEW3D_OT_place_cursor_modal(bpy.types.Operator):
        """use of a function and reload previous toolsettings when finished"""
        bl_idname = "tpc_ot.place_cursor_modal"
        bl_label = "PlaceCursor"
        bl_options = {'REGISTER', 'UNDO'}
       
        depth : BoolProperty(name="Surface Project", description="project onto the surface", default=True)

        orient : bpy.props.EnumProperty(
          items = [("NONE",   "None",      "leave orientation unchanged"             ,1),
                   ("VIEW",   "View",      "orient to the viewport"                  ,2),
                   ("XFORM",  "Transform", "orient to the current transform setting" ,3), 
                   ("GEOM",   "Geometry",   "match the surface normal"               ,4)], 
                   name = "Orientation",
                   default = "GEOM",
                   description="Preset viewpoint to use")

        object_align : bpy.props.EnumProperty(
          items = [("WORLD",   "World",    "align new objects to world cooridnate system"  ,1),
                   ("VIEW",   "View",      "align new objects to active 3D view"           ,2),
                   ("CURSOR",  "3D Cursor",  "align new objects to 3D cursors rotation"    ,3)], 
                   name = "Align to",
                   default = "CURSOR",
                   description="")

        rotation : FloatProperty(name="Rotate Cursor", description="", default=0, min= -360, max = 360, subtype='PERCENTAGE')      

        def modal(self, context, event):
            context.area.tag_redraw()
            context.area.header_text_set("Leftclick+Press: Snap Cursor, + Mousewheel: Rotate Cursor, Rightclick/ESC: Cancel")

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
        
        running = False
       
        # get the context arguments         
        def modal(self, context, event):
                                      
            if event.value == "RELEASE" and self.running:               
                # reload settings after event
                bpy.context.scene.tool_settings.transform_pivot_point = self.store_pivot
                bpy.context.scene.tool_settings.snap_elements = self.store_elements
                bpy.context.scene.tool_settings.snap_target = self.store_target
                bpy.context.scene.tool_settings.use_snap_align_rotation = self.store_rotation
                bpy.context.scene.tool_settings.use_snap_project = self.store_project
                bpy.context.scene.tool_settings.use_snap = self.store_snap              

                bpy.ops.wm.tool_set_by_id(name="builtin.move")                          
                self.running = False   
                return {'FINISHED'}
         
            elif event.type == 'LEFTMOUSE' and event.value =="PRESS" and not self.running:           
                self.running = True   
                bpy.ops.wm.tool_set_by_id(name="builtin.cursor") 

                if event.type == 'WHEELUPMOUSE':
                    bpy.context.scene.cursor.rotation_euler[2] = -self.rotation
                
                if event.type == 'WHEELDOWNMOUSE': 
                    bpy.context.scene.cursor.rotation_euler[2] = self.rotation

            # do event
            elif event.type in {'RIGHTMOUSE', 'ESC'}:              
                # reload settings after event
                bpy.context.scene.tool_settings.transform_pivot_point = self.store_pivot
                bpy.context.scene.tool_settings.snap_elements = self.store_elements
                bpy.context.scene.tool_settings.snap_target = self.store_target
                bpy.context.scene.tool_settings.use_snap_align_rotation = self.store_rotation
                bpy.context.scene.tool_settings.use_snap_project = self.store_project
                bpy.context.scene.tool_settings.use_snap = self.store_snap
                
                bpy.ops.wm.tool_set_by_id(name="builtin.move")
                return {'CANCELLED'}       
            
            return {'PASS_THROUGH'}

            #return {'RUNNING_MODAL'}

     
        # do by execute
        def invoke(self, context, event):  
                                                              
            if context.mode in "OBJECT":           
                bpy.ops.object.select_all(action='DESELECT')
                    
            # check if something selected          
            if bpy.context.area.ui_type == 'VIEW_3D':

                # store exist settings
                self.store_pivot = bpy.context.scene.tool_settings.transform_pivot_point                
                self.store_elements = bpy.context.scene.tool_settings.snap_elements
                self.store_target = bpy.context.scene.tool_settings.snap_target
                self.store_rotation = bpy.context.scene.tool_settings.use_snap_align_rotation
                self.store_project = bpy.context.scene.tool_settings.use_snap_project
                self.store_snap = bpy.context.scene.tool_settings.use_snap

                bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
                bpy.context.scene.tool_settings.use_snap = True                
                bpy.context.scene.tool_settings.snap_elements = {'VERTEX', 'EDGE', 'FACE'}
                bpy.context.scene.tool_settings.snap_target = 'MEDIAN'
                bpy.context.scene.tool_settings.use_snap_align_rotation = True      
              
                bpy.context.space_data.overlay.show_cursor = True                
                #https://docs.blender.org/api/current/bpy.ops.view3d.html    
                bpy.ops.view3d.cursor3d(use_depth=self.depth, orientation=self.orient)
                bpy.context.preferences.edit.object_align=self.object_align                
                bpy.context.scene.cursor.rotation_euler[2] = self.rotation                          
                #bpy.ops.wm.tool_set_by_id(name="builtin.cursor")                  
                              
                context.window_manager.modal_handler_add(self)          
                return {'RUNNING_MODAL'}
            
            else:
                self.report({'WARNING'}, "Must be in 3D View")  
                return {'CANCELLED'}




# REGISTER #
classes = (
    VIEW3D_OT_3d_cursor_copy,
    VIEW3D_OT_place_cursor,
    VIEW3D_OT_place_cursor_modal,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()



