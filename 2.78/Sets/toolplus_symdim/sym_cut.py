__status__ = "toolplus"
__author__ = "mkbreuer"
__version__ = "1.0"
__date__ = "2017"



import bpy
from bpy import*
from bpy.props import *
from mathutils import Vector

    
bpy.types.Scene.tp_edit = bpy.props.BoolProperty(name="EditToggle", description="switch to or stay in editmode", default=False)   
bpy.types.Scene.tp_mirror = bpy.props.BoolProperty(name="Add MirrorModifier", description="add mirror modifier", default=False)    
bpy.types.Scene.tp_apply = bpy.props.BoolProperty(name="Apply MirrorModifier", description="apply mirror modifier", default=False)  
bpy.types.Scene.tp_sculpt = bpy.props.BoolProperty(name="SculptToggle", description="switch to or stay in sculptmode", default=False)  

bpy.types.Scene.sym_cut = bpy.props.BoolProperty(default= True, description="symcut")
bpy.types.Scene.symcut_axis = bpy.props.EnumProperty(items = [("x",   "X",   "", 1), ("y",   "Y",   "", 2), ("z",   "Z",   "", 3)], description="symcut axis")
bpy.types.Scene.sym_orientation = bpy.props.EnumProperty(items = [("positive", "Positive", "", 1),("negative", "Negative", "", 2)], description="sym orientation")


class View3D_TP_Align_Vertices(bpy.types.Operator):
    """align vertices to one axis"""
    bl_idname = "tp_ops.align_vertices"
    bl_label = "Align to Axis"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        x1,y1,z1 = bpy.context.scene.cursor_location
        bpy.ops.view3d.snap_cursor_to_selected()

        x2,y2,z2 = bpy.context.scene.cursor_location

        bpy.context.scene.cursor_location[0],bpy.context.scene.cursor_location[1],bpy.context.scene.cursor_location[2]  = 0,0,0

        #vertices coordinate to local 0 
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if bpy.context.scene.symcut_axis == 'x':
                    axis = 0
                elif bpy.context.scene.symcut_axis == 'y':
                    axis = 1
                elif bpy.context.scene.symcut_axis == 'z':
                    axis = 2
                vert.co[axis] = 0
        
        bpy.context.scene.cursor_location = x2,y2,z2

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        bpy.context.scene.cursor_location = x1,y1,z1

        return {'FINISHED'}


   
class View3D_TP_SymCut(bpy.types.Operator):
    """cut an object along an axis"""
    bl_idname = "tp_ops.symcut"
    bl_label = "SymCut"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True
            
    def get_local_axis_vector(self, context, X, Y, Z, orientation):
        loc = context.object.location
        bpy.ops.object.mode_set(mode="OBJECT") # needed to avoid to translate vertices
        
        v1 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(X*orientation, Y*orientation, Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        v2 = Vector((loc[0],loc[1],loc[2]))
        bpy.ops.transform.translate(value=(-X*orientation, -Y*orientation, -Z*orientation), constraint_axis=((X==1), (Y==1), (Z==1)), constraint_orientation='LOCAL')
        
        bpy.ops.object.mode_set(mode="EDIT")
        return v2-v1
    
    def execute(self, context):
        
        # define axis
        X,Y,Z = 0,0,0
        if bpy.context.scene.symcut_axis == 'x':
            X = 1
        elif bpy.context.scene.symcut_axis == 'y':
            Y = 1
        elif bpy.context.scene.symcut_axis == 'z':
            Z = 1

        bpy.ops.object.mode_set(mode="EDIT") # go to edit mode
        
        bpy.ops.mesh.select_all(action='SELECT') # select all the vertices
        
        if bpy.context.scene.sym_orientation == 'positive':
            orientation = 1
        else:
            orientation = -1
            
        cut_normal = self.get_local_axis_vector(context, X, Y, Z, orientation)
            
        bpy.ops.mesh.bisect(plane_co=(bpy.context.object.location[0], bpy.context.object.location[1], bpy.context.object.location[2]), plane_no=cut_normal, use_fill= False, clear_inner= bpy.context.scene.sym_cut, clear_outer= 0) # Cut the mesh
        
        bpy.ops.tp_ops.align_vertices() # use to align the vertices on the origin

        return {'FINISHED'}



# define operator parts

def sym_editmode(context):

    current_mode = bpy.context.object.mode # Save the current mode

    scene = context.scene
    if bpy.context.scene.tp_edit == True:

        if context.mode == 'EDIT_MESH':                
            bpy.ops.object.editmode_toggle()         
        
        bpy.ops.object.editmode_toggle() 

    else:
        #pass
        if not bpy.context.scene.tp_sculpt:
            bpy.ops.object.mode_set(mode=current_mode) 
        else:
            bpy.ops.sculpt.sculptmode_toggle()


def sym_apply_mod(context):

    if bpy.context.scene.tp_apply == True:
        bpy.ops.tp_ops.apply_mod_mirror()
    else:
        pass

def sym_add_mod(context):
    
    is_mirror = False
    
    for mode in bpy.context.object.modifiers :
        if mode.type == 'MIRROR' :
            is_mirror = True
    
    if is_mirror == True:
        pass

    else:
        bpy.ops.object.modifier_add(type = "MIRROR")

def sym_mod_props(context):

    bpy.context.object.modifiers["Mirror"].use_mirror_merge = True          
    bpy.context.object.modifiers["Mirror"].show_on_cage = True
    bpy.context.object.modifiers["Mirror"].use_clip = True




# AXIS OPERATORS

class VIEW3D_TP_Negativ_X_symcut(bpy.types.Operator):
    """delete negative X side / add X mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_x_symcut"
    bl_label = "Cut -X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = False
                bpy.context.object.modifiers["Mirror"].use_z = False
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)

        return {'FINISHED'}


class VIEW3D_TP_Positiv_X_symcut(bpy.types.Operator):
    """delete positiv X side / add X mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_x_symcut"
    bl_label = "Cut +X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = False
                bpy.context.object.modifiers["Mirror"].use_z = False
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)

        return {'FINISHED'}


class VIEW3D_TP_Negativ_Y_symcut(bpy.types.Operator):
    """delete negative Y side / add Y mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_y_symcut"
    bl_label = "Cut -Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = False
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = False
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)

        return {'FINISHED'}


class VIEW3D_TP_Positiv_Y_symcut(bpy.types.Operator):
    """delete positiv Y side / add Y mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_y_symcut"
    bl_label = "Cut +Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = False
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = False
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)    


        return {'FINISHED'}


class VIEW3D_TP_Negativ_Z_symcut(bpy.types.Operator):
    """delete negative Z side / add Z mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_z_symcut"
    bl_label = "Cut -Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
          
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = False
                bpy.context.object.modifiers["Mirror"].use_y = False
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)  

        return {'FINISHED'}


class VIEW3D_TP_Positiv_Z_symcut(bpy.types.Operator):
    """delete positiv Z side / add Z mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_z_symcut"
    bl_label = "Cut +Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':            
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = False
                bpy.context.object.modifiers["Mirror"].use_y = False
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)   

        return {'FINISHED'}






class VIEW3D_TP_Positiv_XY_symcut(bpy.types.Operator):
    """delete positiv XY side / add XY mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_xy_symcut"
    bl_label = "Cut +XY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = False
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)    

        return {'FINISHED'}


class VIEW3D_TP_Negativ_XY_symcut(bpy.types.Operator):
    """delete negativ XY side / add XY mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_xy_symcut"
    bl_label = "Cut -XY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = False
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context) 
                  
        return {'FINISHED'}




class VIEW3D_TP_Positiv_XZ_symcut(bpy.types.Operator):
    """delete positive XZ side / add XZ mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_xz_symcut"
    bl_label = "Cut +XZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = False
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)       
                  
        return {'FINISHED'}    




class VIEW3D_TP_Negativ_XZ_symcut(bpy.types.Operator):
    """delete negativ XZ side / add XZ mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_xz_symcut"
    bl_label = "Cut -XZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()     
        
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = False
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)       

        return {'FINISHED'}



class VIEW3D_TP_Positiv_YZ_symcut(bpy.types.Operator):
    """delete positive YZ side / add YZ mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_yz_symcut"
    bl_label = "Cut +YZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 

        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()            
        
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = False
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)   
                  
        return {'FINISHED'}



class VIEW3D_TP_Negativ_YZ_symcut(bpy.types.Operator):
    """delete negativ YZ side / add YZ mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_yz_symcut"
    bl_label = "Cut -YZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 

        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()            
        
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = False
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)

        return {'FINISHED'}



class VIEW3D_TP_Positiv_XYZ_symcut(bpy.types.Operator):
    """delete positive XYZ side / add XYZ mirror modifier"""
    bl_idname = "tp_ops.mods_positiv_xyz_symcut"
    bl_label = "Cut +XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()            
        
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'positive'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context) 
                  
        return {'FINISHED'}



class VIEW3D_TP_Negativ_XYZ_symcut(bpy.types.Operator):
    """delete negativ XYZ side / add XYZ mirror modifier"""
    bl_idname = "tp_ops.mods_negativ_xyz_symcut"
    bl_label = "Cut -XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.editmode_toggle() 
            
        bpy.context.scene.symcut_axis = 'x'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        bpy.context.scene.symcut_axis = 'y'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()            
        
        bpy.context.scene.symcut_axis = 'z'
        bpy.context.scene.sym_orientation = 'negative'
        bpy.ops.tp_ops.symcut()

        sym_editmode(context)

        if bpy.context.scene.tp_mirror == True:

            sym_add_mod(context)
 
            obj = context.scene.objects.active            
            for mod in obj.modifiers: 
                     
                bpy.context.object.modifiers["Mirror"].use_x = True
                bpy.context.object.modifiers["Mirror"].use_y = True
                bpy.context.object.modifiers["Mirror"].use_z = True
                sym_mod_props(context)
        else:
            pass
        
        sym_apply_mod(context)      

        return {'FINISHED'}




    
class VIEW3D_TP_Boolean_Normal_symcut(bpy.types.Operator):
    """cut mesh at seleted normal and delete opposite (use plane as cutter)"""
    bl_idname = "tp_ops.normal_symcut"
    bl_label = "Normal Cut"
    bl_options = {'REGISTER', 'UNDO'}

    flip = bpy.props.BoolProperty(name="Flip Normals",  description="Flip Normals", default=False) 

    def draw(self, context):
        layout = self.layout   
              
        box = layout.box().column(1)

        row = box.column(1)
        row.prop(self, 'flip')

    def execute(self, context):
        
        bpy.context.space_data.transform_orientation = 'NORMAL'

        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1})
        for i in range(self.flip):
            bpy.ops.mesh.flip_normals()
        bpy.ops.transform.resize(value=(1000, 1000, 0), constraint_axis=(True, True, False))
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 1000), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        
        bpy.ops.mesh.select_linked(delimit={'SEAM'})
        bpy.ops.mesh.intersect_boolean(operation='DIFFERENCE')
                         
        bpy.context.space_data.transform_orientation = 'GLOBAL'

        return {'FINISHED'}



    
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


