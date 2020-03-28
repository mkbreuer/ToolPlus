# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from mathutils import Vector

EDIT = ["EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]  


class VIEW3D_OT_align_mesh_to_axis(bpy.types.Operator):
    """align vertices to one axis"""
    bl_idname = "tpc_ot.align_mesh_to_axis"
    bl_label = "Align to Axis"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    use_align_axis_x : BoolProperty(name="X",  description=" ", default=True)    
    use_align_axis_y : BoolProperty(name="Y",  description=" ", default=False)    
    use_align_axis_z : BoolProperty(name="Z",  description=" ", default=False)   

    use_remove_doubles : BoolProperty(name="Merge By Distance",  description="enable/disable", default=True)   
    remove_doubles : FloatProperty(name = "Value", description = "remove doubles", default = 0.0001, min = 0.0001, max = 10.0000, precision=4)

    def draw(self, context):
        layout = self.layout   

        box = layout.box().column(align=True) 
        box.separator() 

        row = box.row(align=True)  
        row.label(text='Axis:') 
        row.prop(self, 'use_align_axis_x')  
        row.prop(self, 'use_align_axis_y')  
        row.prop(self, 'use_align_axis_z')  

        box.separator() 
        
        row = box.row(align=True)  
        row.prop(self, 'use_remove_doubles', text='')
        row.label(text='Merge By Distance:') 

        if self.use_remove_doubles == True: 
            row.prop(self, 'remove_doubles')   

        box.separator() 


    def execute(self, context):   

        current_mode = bpy.context.object.mode 
        bpy.ops.object.mode_set(mode = 'OBJECT')
    
        x1,y1,z1 = bpy.context.scene.cursor.location
        bpy.ops.view3d.snap_cursor_to_selected()
        x2,y2,z2 = bpy.context.scene.cursor.location

        scene = bpy.context.scene
        scene.cursor.location[0], scene.cursor.location[1], scene.cursor.location[2] = 0,0,0
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

        # align vertices to local 0 
        for vert in bpy.context.object.data.vertices:
            if vert.select:
               
                #axis_x = 0
                #axis_y = 1
                #axis_z = 2

                if self.use_align_axis_x == True and self.use_align_axis_y == False and self.use_align_axis_z == False:   
                    vert.co[0] = 0               

                if self.use_align_axis_x == False and self.use_align_axis_y == True and self.use_align_axis_z == False:   
                    vert.co[1] = 0
               
                if self.use_align_axis_x == False and self.use_align_axis_y == False and self.use_align_axis_z == True:   
                    vert.co[2] = 0

                if self.use_align_axis_x == True and self.use_align_axis_y == True and self.use_align_axis_z == False:   
                    vert.co[0] = 0
                    vert.co[1] = 0       

                if self.use_align_axis_x == True and self.use_align_axis_y == False and self.use_align_axis_z == True:   
                    vert.co[0] = 0
                    vert.co[2] = 0          

                if self.use_align_axis_x == False and self.use_align_axis_y == True and self.use_align_axis_z == True:   
                    vert.co[1] = 0
                    vert.co[2] = 0

                if self.use_align_axis_x == True and self.use_align_axis_y == True and self.use_align_axis_z == True:   
                    vert.co[0] = 0
                    vert.co[1] = 0
                    vert.co[2] = 0

   
        if context.mode == 'EDIT_MESH':    
            if self.use_remove_doubles == True: 
                bpy.ops.mesh.remove_doubles(threshold=self.remove_doubles)

        bpy.context.scene.cursor.location = x2,y2,z2
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.context.scene.cursor.location = x1,y1,z1

        bpy.ops.object.mode_set(mode=current_mode) 
        return {'FINISHED'}

