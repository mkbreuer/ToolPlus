
import bpy, bmesh, os
from bpy import*
from bpy.props import *
from bpy.types import WindowManager

    
class VIEW3D_TP_Object_Materials(bpy.types.Operator):
    """Add a new Material and enable Color Object"""
    bl_idname = "tp_ops.material_color"
    bl_label = "Object Material Color"
    bl_options = {'REGISTER', 'UNDO'}
    
    obj_color = bpy.props.BoolProperty(name="Use Object Color", description="Value", default=True)

    def execute(self, context):
        obj = bpy.context.active_object
 
        mat_name = [obj.name]
        mat = bpy.data.materials.new(obj.name)

        if len(obj.data.materials):
            obj.data.materials[0] = mat
        else:
            obj.data.materials.append(mat)

        for  i in range(self.obj_color):
            bpy.context.object.active_material.use_object_color = True

        return {'FINISHED'}


class VIEW3D_TP_List_Materials(bpy.types.Menu): 
    """apply material to object or mesh"""
    bl_idname = "tp_ops.material_list"
    bl_label = "Material List"

    def draw(self, context):
        layout = self.layout

        for mat in bpy.data.materials:  
            name = mat.name
            try:
                icon_val = layout.icon(mat)
            except:
                icon_val = 1
                print ("WARNING [Mat Panel]: Could not get icon value for %s" % name)
            op = layout.operator("tp_ops.assign_material", text=name, icon_value=icon_val)
            op.mat_to_assign = name
            

        
class VIEW3D_TP_Assign_Materials(bpy.types.Operator):
    bl_idname = "tp_ops.assign_material"
    bl_label = "Assign Material"
 
    mat_to_assign = bpy.props.StringProperty(default="")
 
    def execute(self, context):

        if context.mode == 'EDIT_MESH':
            obj = context.object
            bm = bmesh.from_edit_mesh(obj.data)
 
            selected_face = [f for f in bm.faces if f.select]          
 
            mat_name = [mat.name for mat in bpy.context.object.material_slots if len(bpy.context.object.material_slots)]
 
            if self.mat_to_assign in mat_name:
                context.object.active_material_index = mat_name.index(self.mat_to_assign) 
                bpy.ops.object.material_slot_assign() 
            else: 
                bpy.ops.object.material_slot_add()
                bpy.context.object.active_material = bpy.data.materials[self.mat_to_assign] 
                bpy.ops.object.material_slot_assign() 
            return {'FINISHED'}

        elif context.object.mode == 'OBJECT':
 
            obj_list = [obj.name for obj in context.selected_objects]
 
            for obj in obj_list:
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[obj].select = True                
                bpy.context.scene.objects.active = bpy.data.objects[obj]
                bpy.context.object.active_material_index = 0
 
                if self.mat_to_assign == bpy.data.materials:
                    bpy.context.active_object.active_material = bpy.data.materials[mat_name]
 
                else:
                    if not len(bpy.context.object.material_slots):
                        bpy.ops.object.material_slot_add()
 
                    bpy.context.active_object.active_material = bpy.data.materials[self.mat_to_assign]
 
            for obj in obj_list:
                bpy.data.objects[obj].select = True
 
            return {'FINISHED'}   
                                               
        elif context.mode == 'EDIT_CURVE': 
            obj = context.object        
            
            bpy.ops.object.material_slot_add()
            bpy.context.object.active_material = bpy.data.materials[self.mat_to_assign] 
            bpy.ops.object.material_slot_assign() 
            return {'FINISHED'}



class VIEW3D_TP_Delete_Materials(bpy.types.Operator):
    """Remove all materials slots / Value Slider"""
    bl_idname = "tp_ops.remove_all_material"
    bl_label = "Delete all Material"
    bl_options = {'REGISTER', 'UNDO'}

    deleteMat = bpy.props.IntProperty(name="Delete Material-Slots", description="Value", default=1, min=1, soft_max=500, step=1)
    
    def draw(self, context):
        layout = self.layout

        box = layout.box().column(1)   

        row = box.row(1)                
        row.prop(self,'deleteMat', text="Delete Material-Slots")         

        
    def execute(self, context):                

        if context.object.mode == 'EDIT':
                bpy.ops.object.editmode_toggle()      
                bpy.ops.object.material_slot_remove()
                bpy.ops.object.editmode_toggle()
        else:
            for i in range(self.deleteMat):
                bpy.ops.object.material_slot_remove()

        return {'FINISHED'}



class VIEW3D_TP_Purge_Materials(bpy.types.Operator):
    '''Purge orphaned materials'''
    bl_idname="tp_purge.unused_material_data"
    bl_label="Purge Materials"
    
    def execute(self, context):

        target_coll = eval("bpy.data.materials")

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        return {'FINISHED'}




def register():
    
    bpy.utils.register_module(__name__)

def unregister():
   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()