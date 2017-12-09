# ##### BEGIN GPL LICENSE BLOCK #####
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

# LOAD CACHE #
from .caches.cache      import  (dpl_settings_load)
from .caches.cache      import  (dpl_settings_write)

# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import *


# DRAW PROPS [F6] # 
def draw_props(self, context):
    layout = self.layout.column(1)
    
    if len(bpy.context.selected_objects) == 2:   

        box = layout.box().column(1)
        
        row = box.row(1)   
        row.prop(self, 'dupli_align')       
        row.prop(self, 'dupli_single')

        row = box.row(1)   
        row.prop(self, 'dupli_separate')        
        row.prop(self, 'dupli_link')
        
        box.separator()

        row = box.row(1)          
        box.separator()
        row.scale_x = 0.5        
        row.operator('wm.operator_defaults', text="Reset", icon ="RECOVER_AUTO")

    else:
        box = layout.box().column(1)

        row = box.row(1)  
        row.label("need a source and a target", icon ="INFO")  



class View3D_TP_Dupli_Set_Panel(bpy.types.Operator):
    """Duplication on active Object"""
    bl_idname = "tp_ops.dupli_set_panel"
    bl_label = "Duplication Set :)"
    bl_options = {'REGISTER', 'UNDO'}
    
    dupli_align = bpy.props.BoolProperty(name="Align Source",  description="Align Object Location", default=False)       
    dupli_single = bpy.props.BoolProperty(name="Make Real",  description="Single Dupli-Instances", default=False)    
    dupli_separate = bpy.props.BoolProperty(name="Separate all",  description="Separate Objects", default=False)    
    dupli_link = bpy.props.BoolProperty(name="Link separted",  description="Link separated Objects", default=False)    

    # DRAW PROPS [F6] # 
    def draw(self, context):        
        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        dpl_settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        dpl_settings_write(self)
        
        if len(bpy.context.selected_objects) == 2:

            first_obj = bpy.context.active_object

            obj_a, obj_b = context.selected_objects

            second_obj = obj_a if obj_b == first_obj else obj_b  

            for i in range(self.dupli_align):             

                #copy dimensions to it
                active = bpy.context.active_object
                selected = bpy.context.selected_objects

                for obj in selected:                                        
                    obj.location = active.location
          
            bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]            
            bpy.data.objects[first_obj.name].select=True  
           
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)              

            for i in range(self.dupli_single):   
                bpy.context.scene.objects.active = bpy.data.objects[first_obj.name]            
                bpy.data.objects[first_obj.name].select=True  
               
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

                bpy.ops.object.duplicates_make_real()
                bpy.ops.object.parent_clear(type='CLEAR')

                bpy.data.objects[first_obj.name].select=False                  
                
                bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]            
                bpy.data.objects[second_obj.name].select=True  
               
                bpy.ops.object.select_linked(type='OBDATA')
                bpy.ops.object.join()                
                
                for i in range(self.dupli_separate):                
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.separate(type='LOOSE')
                    bpy.ops.object.editmode_toggle()

                    for i in range(self.dupli_link):
                        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY') 
                        bpy.ops.object.make_links_data(type='OBDATA')                   
        else:
            print(self)
            self.report({'INFO'}, "need a source and a target")  
            
        return {'FINISHED'}



# PROPERTY GROUP: DUPLISET #
class DupliSet_Properties(bpy.types.PropertyGroup):
    
    dupli_align = bpy.props.BoolProperty(name="Align Source",  description="Align Object Location", default=False)       
    dupli_single = bpy.props.BoolProperty(name="Make Real",  description="Single Dupli-Instances", default=False)    
    dupli_separate = bpy.props.BoolProperty(name="Separate all",  description="Separate Objects", default=False)    
    dupli_link = bpy.props.BoolProperty(name="Link separted",  description="Link separated Objects", default=False)   



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)

    # PROPS DUPLISET # 
    bpy.types.WindowManager.dupliset_props = PointerProperty(type = DupliSet_Properties)

def unregister():
    bpy.utils.unregister_module(__name__)

    # PROPS DUPLISET # 
    del bpy.types.WindowManager.dupliset_props

if __name__ == "__main__":
    register()
        
        



