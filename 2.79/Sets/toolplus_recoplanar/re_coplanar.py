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


# LOAD MODULE #
import bpy
from bpy import *
from bpy.props import *


# LISTS FOR SELECTED & DUPLICATIONS #
name_list = []
duplicated_list = []

# OPERATOR RELOCATION #
class VIEW3D_TP_ReCenter(bpy.types.Operator):
    """reposition to 3d view center and clear rotation"""
    bl_idname = "tp_ops.recenter"
    bl_label = "ReCenter"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    # clear rotation in center 
    rota_clear = bpy.props.BoolProperty(name = "Rotation", description = "clear rotation in center", default = True)

    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
        box = layout.box().column(1)   

        row = box.row(1)
        row.label(text="Clear: ")
        row.prop(self, "rota_clear")               
        box.separator()  
  
  
    def execute(self, context):
        selected = bpy.context.selected_objects          

        n = len(selected)
        if n == 1:
            
            for obj in selected: 
                bpy.ops.object.duplicate()            
                bpy.context.object.name  = obj.name + "_dummy"
                bpy.context.object.data.name = obj.name + "_dummy"

                bpy.ops.object.select_all(action = 'DESELECT') 
                bpy.data.objects[obj.name + "_dummy"].select = True    
                

            for obj in selected:
                name_list.append(obj.name)

                # keep layer
                layers = []
                for i in obj.layers:
                    layers.append(i)
                bpy.ops.object.move_to_layer(layers = layers)
                
                # hide dummy
                bpy.ops.object.hide_view_set()        
                bpy.data.objects[obj.name + "_dummy"].select = False 

                for obj in selected:
                    bpy.data.objects[obj.name].select = True
                bpy.context.scene.objects.active = selected[0]

                # center selected object       
                bpy.ops.object.transforms_to_deltas(mode='LOC')
                bpy.ops.view3d.snap_cursor_to_center()
                bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

                # do not rotate
                for i in range(self.rota_clear):
                    bpy.ops.object.rotation_clear(clear_delta=False)

        else:
            self.report({'INFO'}, 'Need 1 Selection')
          
        del name_list[:]
        return {'FINISHED'}




# OPERATOR RELOCATE #
class VIEW3D_TP_ReLocate(bpy.types.Operator):
    """set location back to center with offset / Attention: purge all orphaned meshdata"""
    bl_idname = "tp_ops.relocate"
    bl_label = "ReLocate"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
 
    delta_rot = bpy.props.BoolProperty(name = "Delta Rotation", description = "zero all values", default = True)
    delta_scale = bpy.props.BoolProperty(name = "Delta Scale", description = "zero all values", default = True)

    def execute(self, context):
                
        selected = bpy.context.selected_objects

        for obj in selected:    

            # set location back to center with offset
            # store 3d cursor
            bpy.ops.view3d.snap_cursor_to_selected() 

            v3d = context.space_data
            if v3d.type == 'VIEW_3D':
                            
                rv3d = v3d.region_3d
                current_cloc = v3d.cursor_location.xyz         
                #v3d.cursor_location = ()

                bpy.ops.view3d.snap_cursor_to_center()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                                
                bpy.ops.object.transforms_to_deltas(mode='LOC')

                for i in range(self.delta_rot):
                    bpy.ops.object.transforms_to_deltas(mode='ROT')

                for i in range(self.delta_scale):
                    bpy.ops.object.transforms_to_deltas(mode='SCALE')

                
                # reload 3d cursor
                v3d.cursor_location = current_cloc   

                # place origin
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        
        return {'FINISHED'}






# OPERATOR REPOSITION #
class VIEW3D_TP_RePosition(bpy.types.Operator):
    """reposition to previous location with unapplied rotation / Attention: purge all orphaned meshdata"""
    bl_idname = "tp_ops.reposition"
    bl_label = "RePosition"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    get_rota = bpy.props.BoolProperty(name="Rotation",  description="set previous rotation", default=True)    
    get_scale = bpy.props.BoolProperty(name="Scale",  description="set previous dimension", default=False)   
    get_local = bpy.props.EnumProperty(
        items=[("tp_0"    ,"None"      ,"" ),
               ("tp_1"    ,"Local"     ,"" ),
               ("tp_2"    ,"Global"    ,"" )],
               name = "Set Local Widget",
               default = "tp_0",    
               description = "widget orientation")
               

    # DRAW PROPS [F6] # 
    def draw(self, context):
        layout = self.layout
        box = layout.box().column(1)   

        row = box.row(1)
        row.label(text="Preserve: ")
        row.prop(self, "get_rota")        
        row.prop(self, "get_scale")        
       
        box.separator()  
        box.separator()  
      
        row = box.row(1)
        row.label(text="Widget: ")
        row.prop(self, "get_local", expand = True)        
       
        box.separator()         
 
    def execute(self, context):

        active = bpy.context.active_object            
        selected = bpy.context.selected_objects
           
        n = len(selected)
        if n == 1:

            for obj in selected:
                name_list.append(obj.name)

                # reposition object
                bpy.ops.view3d.snap_cursor_to_center()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')    
        
                # get location constraint from dummy                     
                bpy.ops.object.constraint_add(type='COPY_LOCATION')
                bpy.context.object.constraints["Copy Location"].target = bpy.data.objects[obj.name + "_dummy"]
                bpy.ops.object.visual_transform_apply()      
                          
                # get rotation constraint from dummy
                for i in range(self.get_rota):                
                    bpy.ops.object.constraint_add(type='COPY_ROTATION')
                    bpy.context.object.constraints["Copy Rotation"].target = bpy.data.objects[obj.name + "_dummy"]
                    bpy.ops.object.visual_transform_apply()           

                # get scale constraint from dummy  
                for i in range(self.get_scale):                          
                    bpy.ops.object.constraint_add(type='COPY_SCALE')
                    bpy.context.object.constraints["Copy Scale"].target = bpy.data.objects[obj.name + "_dummy"]
                    bpy.ops.object.visual_transform_apply()  
               
                # delete rotation constraint        
                bpy.ops.object.constraints_clear() 

                # select dummy and copy datas
                bpy.data.objects[obj.name + "_dummy"].hide = False         
                bpy.data.objects[obj.name + "_dummy"].select = True 
                bpy.context.scene.objects.active = selected[0]

                #for obj in selected:
                active = bpy.context.active_object 
                obj.dimensions = active.dimensions
                obj.location = active.location
                obj.rotation_euler = active.rotation_euler
      
                # delete dummy
                bpy.ops.object.select_all(action="DESELECT")
                bpy.data.objects[obj.name + "_dummy"].select = True 
                bpy.ops.object.delete(use_global=False)
                
                # set first in list active
                bpy.data.objects[obj.name].select = True 
                bpy.context.scene.objects.active = selected[0]
                            
                # set location back to center with offset
                # store 3d cursor
                bpy.ops.view3d.snap_cursor_to_selected() 

                v3d = context.space_data
                if v3d.type == 'VIEW_3D':
                                
                    rv3d = v3d.region_3d
                    current_cloc = v3d.cursor_location.xyz         
                    #v3d.cursor_location = ()

                    bpy.ops.view3d.snap_cursor_to_center()
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                    bpy.ops.object.transforms_to_deltas(mode='LOC')

                    # reload 3d cursor
                    v3d.cursor_location = current_cloc   

                    # place origin
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                          
        else:
            self.report({'INFO'}, 'select only 1 object')


        # set widget orientation
        if self.get_local == "tp_0":
            pass            
        elif self.get_local == "tp_1":
            bpy.ops.tp_ops.space_local()               
        else:
            bpy.ops.tp_ops.space_global()   


        # purge unused all mesh data! / single one?
        target = eval("bpy.data.meshes")
        for item in target:
            if item.users == 0:
                target.remove(item)

        del name_list[:]

        return {'FINISHED'}




# OPERATOR DELETE ORPHANED DUMMIES #
class VIEW3D_TP_DELETE_ORPHANED_DUMMIES(bpy.types.Operator):
    """delete ophaned dummies"""
    bl_idname = "tp_ops.delete_dummy"
    bl_label = "Delete Dummies"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):

        bpy.ops.object.hide_view_clear()

        bpy.ops.object.select_all(action="SELECT")
        
        for obj in bpy.context.selected_objects:
            if "_dummy" not in obj.name:
                obj.select = False
        
        bpy.ops.object.delete()

        return {'FINISHED'}




# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()