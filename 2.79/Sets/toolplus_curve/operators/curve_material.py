# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#

# LOAD MODUL #
import bpy, bmesh, os
from bpy import*
from bpy.props import *
from bpy.types import WindowManager

    
class VIEW3D_TP_Object_Materials(bpy.types.Operator):
    """Add a new Material and enable Color Object"""
    bl_idname = "tp_ops.material_color"
    bl_label = "Object Material Color"
    bl_options = {'REGISTER', 'UNDO'}
    
    obj_color = bpy.props.BoolProperty(name="Use Object Color", description="Value", default=False)

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
    bl_idname="tp_purge.unused_material"
    bl_label="Purge Materials"
    
    def execute(self, context):

        target_coll = eval("bpy.data.materials")

        num_deleted = len([x for x in target_coll if x.users==0])
        num_kept = len([x for x in target_coll if x.users==1])

        for item in target_coll:
            if item.users == 0:
                target_coll.remove(item)

        msg = "Materials: %d removed & %d kept" % (num_deleted, num_kept)
        self.report( { 'INFO' }, msg  )


import random

class VIEW3D_TP_Material_NEW(bpy.types.Operator):
    """add material to object"""
    bl_idname = "tp_ops.material_new"
    bl_label = "Random Material / Object Color"
    bl_options = {"REGISTER", "UNDO"}

    # MATERIAL #
    add_mat = bpy.props.BoolProperty(name="Add Material",  description="add material and enable object color", default=False)        
    add_random = bpy.props.BoolProperty(name="Add Random",  description="add random material", default=False, options={'SKIP_SAVE'})    
    add_objmat = bpy.props.BoolProperty(name="Add Material",  description="add material", default=False, options={'SKIP_SAVE'})    
    add_color = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0,1.0], size = 4, min = 0.0, max = 1.0)
    add_cyclcolor = FloatVectorProperty(name="Object Color", subtype='COLOR',  default=[0.0,1.0,1.0])

    def draw(self, context):      
        layout = self.layout

        col = layout.column(align=True)

        box = col.box().column(1)             

        row = box.row(1) 
        row.prop(self, "add_mat", text ="")                    
        row.label(text="Color:") 
     
        row.prop(self, "add_objmat", text ="", icon="GROUP_VCOL")
        if self.add_random == False:                   
            if self.add_objmat == False:
                if bpy.context.scene.render.engine == 'CYCLES':
                    row.prop(self, "add_cyclcolor", text ="")        
                else:
                    row.prop(self, "add_color", text ="")          
            else:
                row.prop(context.object.active_material, "diffuse_color", text="")  
        else:
            row.prop(context.object.active_material, "diffuse_color", text="")
       
        row.prop(self, "add_random", text ="", icon="FILE_REFRESH")
       
        box.separator()



#    def invoke(self, context, event):
#        dpi_value = bpy.context.user_preferences.system.dpi        
#        return context.window_manager.invoke_props_dialog(self, width=dpi_value*2.5, height=150)
    
    
    # without ok button
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)      
    



    def execute(self, context):

        # add material
        for i in range(self.add_mat):
            bpy.ops.object.mode_set(mode = 'OBJECT')
           
            # Get material
            active = bpy.context.active_object
            mat = bpy.data.materials.get("Mat_Lathe")
            if mat is None:
                # create material
                mat = bpy.data.materials.new(name="Mat_Lathe")
            else:
                bpy.ops.object.material_slot_remove()
                mat = bpy.data.materials.new(name="Mat_Lathe")
                     
            # Assign it to object
            if len(active.data.materials):
                # assign to 1st material slot
                active.data.materials[0] = mat
            else:
                # no slots
                active.data.materials.append(mat)
                        

            # toggle random
            if self.add_random == False:            
                                
                # toggle color target
                if self.add_objmat == False: 
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        mat.diffuse_color = (self.add_cyclcolor)                        
                    else:
                        mat.use_object_color = True
                        bpy.context.object.color = (self.add_color)
                else:                                      
                    # regular material
                    pass
          
            else: 
                
                # toggle color target
                if self.add_objmat == False:   
                    
                    # object color
                    if bpy.context.scene.render.engine == 'CYCLES':
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            mat.diffuse_color = RGB                       
                    else:
                        mat.use_object_color = True
                        for i in range(3):
                            RGB = (random.random(),random.random(),random.random(),1)
                            bpy.context.object.color = RGB
               
                else:        
                    # regular material    
                    if bpy.context.scene.render.engine == 'CYCLES':
                        node=mat.node_tree.nodes['Diffuse BSDF']
                        for i in range(3):
                            node.inputs['Color'].default_value[i] *= random.random()             
                    else:
                        for i in range(3):
                            mat.diffuse_color[i] *= random.random()   

        return {'FINISHED'}




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
