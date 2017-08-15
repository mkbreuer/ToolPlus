__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"

######################################################################################################
# An simple add-on to auto cut in two and mirror an object                                           #
# Actualy partialy uncommented (see further version)                                                 #
# Author: Lapineige                                                                                  #
# License: GPL v3                                                                                    #
######################################################################################################
  
  
############# Add-on description (used by Blender)

#bl_info = {
#    "name": "Auto Mirror",
#    "description": "Super fast cutting and mirroring for mesh",
#    "author": "Lapineige",
#    "version": (2, 4),
#    "blender": (2, 7, 1),
#    "location": "View 3D > Toolbar > Tools tab > AutoMirror (panel)",
#    "warning": "", 
#    "wiki_url": "http://www.le-terrier-de-lapineige.over-blog.com",
#    "tracker_url": "http://blenderlounge.fr/forum/viewtopic.php?f=18&p=7103#p7103",
#    "category": "Mesh"}
############# 

import bpy
from bpy import*
from bpy.props import *
from mathutils import Vector

bpy.types.Scene.AutoMirror_axis = bpy.props.EnumProperty(items = [("x",   "X",   "", 1), ("y",   "Y",   "", 2), ("z",   "Z",   "", 3)], description="Axis used by the mirror modifier")
bpy.types.Scene.AutoMirror_orientation = bpy.props.EnumProperty(items = [("positive", "Positive", "", 1),("negative", "Negative", "", 2)], description="Choose the side along the axis of the editable part (+/- coordinates)")
bpy.types.Scene.AutoMirror_threshold = bpy.props.FloatProperty(default= 0.001, min= 0.001, description="Vertices closer than this distance are merged on the loopcut")
bpy.types.Scene.AutoMirror_toggle_edit = bpy.props.BoolProperty(default= True, description="If not in edit mode, change mode to edit")
bpy.types.Scene.AutoMirror_cut = bpy.props.BoolProperty(default= True, description="If enabeled, cut the mesh in two parts and mirror it. If not, just make a loopcut")
bpy.types.Scene.AutoMirror_clipping = bpy.props.BoolProperty(default=True)
bpy.types.Scene.AutoMirror_use_clip = bpy.props.BoolProperty(default=True, description="Use clipping for the mirror modifier")
bpy.types.Scene.AutoMirror_show_on_cage = bpy.props.BoolProperty(default=True, description="Enable to edit the cage (it's the classical modifier's option)")
bpy.types.Scene.AutoMirror_apply_mirror = bpy.props.BoolProperty(description="Apply the mirror modifier (useful to symmetrise the mesh)")
bpy.types.Scene.AutoMirror_toggle_sculpt = bpy.props.BoolProperty(description="Jump into Sculptmode")

############### Operator

class AlignVertices(bpy.types.Operator):
    """Align Vertices on 1 Axis"""
    bl_idname = "object.align_vertices"
    bl_label = "Align Vertices on 1 Axis"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        x1,y1,z1 = bpy.context.scene.cursor_location
        bpy.ops.view3d.snap_cursor_to_selected()

        x2,y2,z2 = bpy.context.scene.cursor_location

        bpy.context.scene.cursor_location[0],bpy.context.scene.cursor_location[1],bpy.context.scene.cursor_location[2]  = 0,0,0

        #Vertices coordinate to 0 (local coordinate, so on the origin)
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if bpy.context.scene.AutoMirror_axis == 'x':
                    axis = 0
                elif bpy.context.scene.AutoMirror_axis == 'y':
                    axis = 1
                elif bpy.context.scene.AutoMirror_axis == 'z':
                    axis = 2
                vert.co[axis] = 0
        #
        bpy.context.scene.cursor_location = x2,y2,z2

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        bpy.context.scene.cursor_location = x1,y1,z1

        bpy.ops.object.mode_set(mode = 'EDIT')  
        return {'FINISHED'}

class AutoMirror(bpy.types.Operator):
    """ Automatically cut an object along an axis """
    bl_idname = "object.automirror"
    bl_label = "AutoMirror"
    bl_options = {'REGISTER'} # 'UNDO' ?

    @classmethod
    def poll(cls, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        if bpy.context.object and bpy.context.object.type == 'MESH':
            layout.prop(context.scene, "AutoMirror_axis", text="Mirror axis")
            layout.prop(context.scene, "AutoMirror_orientation", text="Orientation")
            layout.prop(context.scene, "AutoMirror_threshold", text="Threshold")
            layout.prop(context.scene, "AutoMirror_toggle_edit", text="Stay in Editmode")
            layout.prop(context.scene, "AutoMirror_cut", text="Cut and mirror")
            if bpy.context.scene.AutoMirror_cut:
                layout.prop(context.scene, "AutoMirror_clipping", text="Clipping")
                layout.prop(context.scene, "AutoMirror_apply_mirror", text="Apply mirror")
        else:
            layout.label(icon="ERROR", text="No mesh selected")
            
    def get_local_axis_vector(self, context, X, Y, Z, orientation):
        loc = context.object.location
        bpy.ops.object.mode_set(mode="OBJECT") # Needed to avoid to translate vertices
        
        v1 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(X*orientation, Y*orientation, Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        v2 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(-X*orientation, -Y*orientation, -Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        
        bpy.ops.object.mode_set(mode="EDIT")
        return v2-v1
    
    def execute(self, context):
        X,Y,Z = 0,0,0
        if bpy.context.scene.AutoMirror_axis == 'x':
            X = 1
        elif bpy.context.scene.AutoMirror_axis == 'y':
            Y = 1
        elif bpy.context.scene.AutoMirror_axis == 'z':
            Z = 1
            
        current_mode = bpy.context.object.mode # Save the current mode
        
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT") # Go to edit mode
        bpy.ops.mesh.select_all(action='SELECT') # Select all the vertices
        
        if bpy.context.scene.AutoMirror_orientation == 'positive':
            orientation = 1
        else:
            orientation = -1
        cut_normal = self.get_local_axis_vector(context, X, Y, Z, orientation)
            
        bpy.ops.mesh.bisect(plane_co=(bpy.context.object.location[0], bpy.context.object.location[1], bpy.context.object.location[2]), plane_no=cut_normal, use_fill= False, clear_inner= bpy.context.scene.AutoMirror_cut, clear_outer= 0, threshold= bpy.context.scene.AutoMirror_threshold) # Cut the mesh
        
        bpy.ops.object.align_vertices() # Use to align the vertices on the origin, needed by the "threshold"
        
        if not bpy.context.scene.AutoMirror_toggle_edit:
            bpy.ops.object.mode_set(mode=current_mode) # Reload previous mode
        
        if not bpy.context.scene.AutoMirror_toggle_sculpt:
            bpy.ops.object.mode_set(mode=current_mode) 
            #bpy.ops.sculpt.sculptmode_toggle()

        if bpy.context.scene.AutoMirror_cut:
            bpy.ops.object.modifier_add(type='MIRROR') # Add a mirror modifier
            bpy.context.object.modifiers[-1].use_x = X # Choose the axis to use, based on the cut's axis
            bpy.context.object.modifiers[-1].use_y = Y
            bpy.context.object.modifiers[-1].use_z = Z
            bpy.context.object.modifiers[-1].use_clip = context.scene.AutoMirror_use_clip
            bpy.context.object.modifiers[-1].show_on_cage = context.scene.AutoMirror_show_on_cage
           
        if bpy.context.scene.AutoMirror_apply_mirror:
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.modifier_apply(apply_as= 'DATA', modifier= bpy.context.object.modifiers[-1].name)
                if bpy.context.scene.AutoMirror_toggle_edit:
                    bpy.ops.object.mode_set(mode='EDIT')
                else:
                    bpy.ops.object.mode_set(mode=current_mode)
            
        return {'FINISHED'}




# t+ customized

bpy.types.Scene.AutoCut_axis = bpy.props.EnumProperty(items = [("x",   "X",   "", 1), ("y",   "Y",   "", 2), ("z",   "Z",   "", 3)], description="Axis used by the mirror modifier")
bpy.types.Scene.AutoCut_orientation = bpy.props.EnumProperty(items = [("positive", "Positive", "", 1),("negative", "Negative", "", 2)], description="Choose the side along the axis of the editable part (+/- coordinates)")
bpy.types.Scene.AutoCut_cut = bpy.props.BoolProperty(default= True, description="If enabeled, cut the mesh in two parts and mirror it. If not, just make a loopcut")
############### Operator

class View3D_TP_Align_Vertices(bpy.types.Operator):
    """Align Vertices on 1 Axis"""
    bl_idname = "tp_ops.align_vertices"
    bl_label = "Align Vertices on 1 Axis"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        x1,y1,z1 = bpy.context.scene.cursor_location
        bpy.ops.view3d.snap_cursor_to_selected()

        x2,y2,z2 = bpy.context.scene.cursor_location

        bpy.context.scene.cursor_location[0],bpy.context.scene.cursor_location[1],bpy.context.scene.cursor_location[2]  = 0,0,0

        #Vertices coordinate to 0 (local coordinate, so on the origin)
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if bpy.context.scene.AutoCut_axis == 'x':
                    axis = 0
                elif bpy.context.scene.AutoCut_axis == 'y':
                    axis = 1
                elif bpy.context.scene.AutoCut_axis == 'z':
                    axis = 2
                vert.co[axis] = 0
        #
        bpy.context.scene.cursor_location = x2,y2,z2

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        bpy.context.scene.cursor_location = x1,y1,z1

        bpy.ops.object.mode_set(mode = 'EDIT')  
        return {'FINISHED'}
    
    
class View3D_TP_AutoCut(bpy.types.Operator):
    """ Automatically cut an object along an axis """
    bl_idname = "tp_ops.autocut"
    bl_label = "AutoCut"
    bl_options = {'REGISTER'} # 'UNDO' ?

    @classmethod
    def poll(cls, context):
        return True
            
    def get_local_axis_vector(self, context, X, Y, Z, orientation):
        loc = context.object.location
        bpy.ops.object.mode_set(mode="OBJECT") # Needed to avoid to translate vertices
        
        v1 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(X*orientation, Y*orientation, Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        v2 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(-X*orientation, -Y*orientation, -Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        
        bpy.ops.object.mode_set(mode="EDIT")
        return v2-v1
    
    def execute(self, context):
        X,Y,Z = 0,0,0
        if bpy.context.scene.AutoCut_axis == 'x':
            X = 1
        elif bpy.context.scene.AutoCut_axis == 'y':
            Y = 1
        elif bpy.context.scene.AutoCut_axis == 'z':
            Z = 1
            
        current_mode = bpy.context.object.mode # Save the current mode
        
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT") # Go to edit mode
        bpy.ops.mesh.select_all(action='SELECT') # Select all the vertices
        
        if bpy.context.scene.AutoCut_orientation == 'positive':
            orientation = 1
        else:
            orientation = -1
        cut_normal = self.get_local_axis_vector(context, X, Y, Z, orientation)
            
        bpy.ops.mesh.bisect(plane_co=(bpy.context.object.location[0], bpy.context.object.location[1], bpy.context.object.location[2]), plane_no=cut_normal, use_fill= False, clear_inner= bpy.context.scene.AutoCut_cut, clear_outer= 0) # Cut the mesh
        
        bpy.ops.tp_ops.align_vertices() # Use to align the vertices on the origin
        
        bpy.ops.object.mode_set(mode=current_mode) # Reload previous mode

        return {'FINISHED'}



class View3D_TP_Apply_Modifier_Mirror(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mods_mirror"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'MIRROR'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")

                        
        return {'FINISHED'}


class View3D_TP_Apply_Modifier_Mirror_EDM(bpy.types.Operator):
    """apply modifier mirror"""
    bl_idname = "tp_ops.apply_mods_mirror_edm"
    bl_label = "Apply Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
       
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        for obj in selected:
            
            for modifier in obj.modifiers:    
                if (modifier.type == 'MIRROR'):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.001")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.002")
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror.003")

        bpy.ops.object.mode_set(mode="EDIT")  
                              
        return {'FINISHED'}


class View3D_TP_Remove_Modifier_Mirror(bpy.types.Operator):
    """remove modifier mirror"""
    bl_idname = "tp_ops.remove_mods_mirror"
    bl_label = "Remove Mirror Modifier"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene = bpy.context.scene
        selected = bpy.context.selected_objects 
        
        if not(selected):    
            for obj in bpy.data.objects:        
                obj = bpy.context.scene.objects.active
                     
                for modifier in obj.modifiers: 
                    if (modifier.type == 'MIRROR'):
                        obj.modifiers.remove(modifier)

        else:
            for obj in selected:
                
                for modifier in obj.modifiers:    
                    if (modifier.type == 'MIRROR'):
                        obj.modifiers.remove(modifier)
                        
        return {'FINISHED'}





class View3D_TP_Batch_AutoMirror(bpy.types.Operator):
    bl_label = 'AutoMirror'
    bl_idname = 'tp_batch.header_autom'
    bl_options = {'REGISTER', 'UNDO'}
     
    def draw(self, context):        
        layout = self.layout
        
        tpw = context.window_manager.tp_collapse_menu_align

        obj = context.active_object
        if obj:
            obj_type = obj.type
            
            if obj.type in {'MESH'}:


                box = layout.box().column(1) 
              
                row = box.row(1)
                row.operator("tp_ops.mod_mirror_x", "", icon ="MOD_MIRROR")

                row.label("AutoMirror")

                obj = context.active_object
                if obj:
                    mod_list = obj.modifiers
                    if mod_list:
                        row.operator("tp_ops.mods_view","", icon = 'RESTRICT_VIEW_OFF')                                                                            
                else:
                    pass


                row.operator("object.automirror", text="", icon="MOD_WIREFRAME")   
                
                box.separator() 
                
                row = box.row(1)                           
                row.prop(context.scene, "AutoMirror_orientation", text="")                                     
                         
                row.prop(context.scene, "AutoMirror_axis", text="")            
                
                box.separator()                  
             
                row = box.row(1)

                if tpw.display_mirror_auto:            
                    row.prop(tpw, "display_mirror_auto", text="Set", icon="PREFERENCES")
                else:
                    row.prop(tpw, "display_mirror_auto", text="Set", icon="PREFERENCES") 
 
                row.prop(context.scene, "AutoMirror_threshold", text="Threshold")      

                box.separator() 

                if tpw.display_mirror_auto:    
                                      
                    box = layout.box().column(1) 
                    row = box.row(1)
                    row.prop(context.scene, "AutoMirror_toggle_edit", text="Editmode")
                    row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
                    
                    row = box.row(1)
                    row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                    row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")            

                    box.separator() 
    
                   
                obj = context.active_object
                if obj:
 
                    mo_types = []            
                    append = mo_types.append



                    for mo in obj.modifiers:
                                                      
                        if mo.type == 'MIRROR':
                            append(mo.type)

                            #box.label(mo.name)

                            row = box.row(1)
                            row.prop(mo, "use_x")
                            row.prop(mo, "use_y")
                            row.prop(mo, "use_z")
                            
                            row = box.row(1)
                            row.prop(mo, "use_mirror_merge", text="Merge")
                            row.prop(mo, "use_clip", text="Clipping")

                            box.separator() 
                else:
                    pass


                obj = context.active_object
                if obj:
                    mod_list = obj.modifiers
                    if mod_list:
                       
                        box.separator()                            

                        row = box.row(1)    
                        
                        row.operator("tp_ops.remove_mod", text="", icon='X') 
                        row.operator("tp_ops.remove_mods_mirror", text="Remove") 
                        row.operator("tp_ops.apply_mod", text="", icon='FILE_TICK') 
                        row.operator("tp_ops.apply_mods_mirror", text="Apply") 

                        box.separator()                                                                      
                else:
                    pass

            else:
                layout.label(icon="ERROR", text="Only for selected Mesh!")
        else:
            pass


        box = layout.box().column(1)    
              
        row = box.row(1)         
        row.operator("ed.undo", text = " ", icon="LOOP_BACK")
        row.operator("ed.redo", text = " ", icon="LOOP_FORWARDS") 
        
        box.separator()        


            
 
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 200)  


    def check(self, context):
        return True



















def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
     
