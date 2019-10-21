import bpy
from bpy import*


#######  Add Geometry   #################

# define operator parts

#def retopo_mesh(context):
    
    


class SINGLEVERTEX_SNAP(bpy.types.Operator):
    """RetopoSnap for Single Vertex"""
    bl_idname = "mesh.singlevertex_snap"
    bl_label = "RetopoSnap"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
                    
        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_element = 'FACE'
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        bpy.context.scene.tool_settings.use_snap_align_rotation = False

        return {'FINISHED'}



types_mesh =  [("tp_m0"    ,"Center"      ," "   ,""   ,0),
               ("tp_m1"    ,"Selected"    ," "   ,""   ,1)] 



class VIEW3D_TP_Set_Retopo_Mesh(bpy.types.Operator):
    """RetopoSnap for Single Vertex"""
    bl_idname = "tp_ops.set_retopo_mesh"
    bl_label = "RetopoMesh"
    bl_options = {'REGISTER', 'UNDO'} 
    
    
    bpy.types.Scene.pl_set_snap = bpy.props.BoolProperty(name="RetopoSnap",  description="retopo surface snapping", default = True) 
    bpy.types.Scene.pl_set_mirror = bpy.props.BoolProperty(name="X-Mirror",  description="add x mirror modifier", default = False) 

           
    bpy.types.Scene.tp_retopo_mesh= bpy.props.EnumProperty(name = " ", default = "tp_m0", items = types_mesh)


    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        
        box = layout.box().column(1)
            
        row = box.column(1)           
        row.prop(scene, 'tp_retopo_mesh', expand = True)        
        row.prop(scene, 'pl_set_mirror')        
        row.prop(scene, 'pl_set_snap')        

        box.separator()

        return
 

    def execute(self, context):
        scene = bpy.context.scene
        
        obj = context.active_object

        if obj:
            if obj.type in {'MESH'}:
 
                second_obj = bpy.context.active_object.name

                if scene.tp_retopo_mesh == "tp_m0":
                    
                    bpy.ops.view3d.snap_cursor_to_center()                        
                    bpy.ops.mesh.primitive_plane_add()
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                    bpy.ops.mesh.delete(type='VERT')
                    bpy.ops.object.editmode_toggle()
   

                if scene.tp_retopo_mesh == "tp_m1":

                    bpy.ops.view3d.snap_cursor_to_selected()
                    bpy.ops.mesh.primitive_plane_add()
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                    bpy.ops.mesh.delete(type='VERT')
                    bpy.ops.object.editmode_toggle()


                context.object.name =  second_obj + "_retopo"
                bpy.ops.tp_ops.copy_name_to_meshdata()                 

                activeObj = context.active_object
                for SelectedObject in context.selected_objects :
                    if SelectedObject != activeObj :
                        
                        
                        SelectedObject.select = False
                activeObj.select = True

                
                bpy.ops.object.editmode_toggle()


            for i in range(scene.pl_set_mirror):
                
                bpy.ops.view3d.fullmirror()                    


            for i in range(scene.pl_set_snap):

                bpy.context.scene.tool_settings.use_snap = True
                bpy.context.scene.tool_settings.use_snap_self = True
                bpy.context.scene.tool_settings.snap_element = 'FACE'
                bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
                bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'

        else:
            pass

        return {'FINISHED'}





class EMPTYROOMCEN(bpy.types.Operator):
    """Add a object without a mesh in editmode to center"""
    bl_idname = "mesh.emptyroom_cen"
    bl_label = "Retopo CenterRoom" 

    def execute(self, context):        
        bpy.ops.view3d.snap_cursor_to_center()                        
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        bpy.context.object.name = "Retopo"
        bpy.ops.tp_ops.copy_name_to_meshdata()

        return {'FINISHED'}  


class EMPTYXROOMCEN(bpy.types.Operator):
    """Add a object without a mesh in editmode and add a x mirror modifier to center"""
    bl_idname = "mesh.emptyxroom_cen"
    bl_label = "Retopo X-CenterRoom"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.view3d.fullmirror()
        bpy.context.object.name = "Retopo"

        bpy.ops.tp_ops.copy_name_to_meshdata()

        return {'FINISHED'} 


class EMPTYROOM(bpy.types.Operator):
    """Add a object without a mesh in editmode to selected"""
    bl_idname = "mesh.emptyroom_sel"
    bl_label = "Retopo SelectRoom" 

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        bpy.context.object.name = "Retopo"
        bpy.ops.tp_ops.copy_name_to_meshdata()
        return {'FINISHED'}  


class EMPTYXROOM(bpy.types.Operator):
    """Add a object without a mesh in editmode and add a x mirror modifier to selected"""
    bl_idname = "mesh.emptyxroom_sel"
    bl_label = "Retopo X-SelectRoom"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.view3d.fullmirror()
        bpy.context.object.name = "Retopo"
        bpy.ops.tp_ops.copy_name_to_meshdata()
        return {'FINISHED'} 



class VIEW3D_TP_Full_X_Mirror(bpy.types.Operator):
    """Add a x mirror modifier with cage and clipping"""
    bl_idname = "view3d.fullmirror"
    bl_label = "X Mirror"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = bpy.context.scene 
        selected = bpy.context.selected_objects 
        object = bpy.ops.object 

        for obj in selected: 
            scene.objects.active = obj 
            
            object.modifier_add(type = "MIRROR")
            
            for mod in obj.modifiers: 
               
                if mod.type == "MIRROR":
                         
                    bpy.context.object.modifiers["Mirror"].use_x = True
                    bpy.context.object.modifiers["Mirror"].use_y = False
                    bpy.context.object.modifiers["Mirror"].use_z = False          
                    bpy.context.object.modifiers["Mirror"].show_on_cage = True
                    bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}





class SINGLEVERTEX(bpy.types.Operator):
    """Add a single Vertex in Editmode"""
    bl_idname = "mesh.singlevertex"
    bl_label = "Single Vertex"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        bpy.context.object.show_x_ray = True
        return {'FINISHED'}


class SINGLEPLANE_X(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.singleplane_x"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}   


class SINGLEPLANE_Y(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.singleplane_y"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}  
    

class SINGLEPLANE_Z(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.singleplane_z"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}  



def register():

    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()



















