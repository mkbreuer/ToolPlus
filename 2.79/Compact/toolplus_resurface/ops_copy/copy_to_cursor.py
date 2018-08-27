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
from ..caches.cache      import  (toc_settings_load)
from ..caches.cache      import  (toc_settings_write)

# LOAD MODULE #
import bpy
from bpy import*
from bpy.props import *


# OPERATOR # 
def draw_operator(self, context):
    scene = context.scene
    cursor = scene.cursor_location
    obj = scene.objects.active

    for i in range(self.total):
        obj_new = obj.copy()
        scene.objects.link(obj_new)

        factor = i / self.total
        obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

    if self.join == True:
        bpy.ops.object.select_linked(type='OBDATA') 
        bpy.ops.object.join()

    if self.unlink == True: 
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

    return {'FINISHED'}

    
# DRAW PROPS [F6] # 
def draw_props(self, context):
    layout = self.layout.column(1)
   
    box = layout.box().column(1)
    
    row = box.column(1)        
    row.prop(self, 'total', text="Steps")
    
    if context.mode == 'OBJECT':

        obj = context.active_object     
        if obj:
           obj_type = obj.type
                          
           if obj_type in {'MESH'}:            
                row = box.row(1) 
                row.prop(self, 'join', text="Join")
                row.label("or")
                row.prop(self, 'unlink', text="Unlink")



class View3D_TP_Copy2Cursor(bpy.types.Operator):
    """Copy selected object to cursor direction"""
    bl_idname = "tp_ops.copy_to_cursor"
    bl_label = "Copy 2 Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)

    # DRAW PROPS [F6] # 
    def draw(self, context):
        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        toc_settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        toc_settings_write(self)
        
        draw_operator(self, context)
            
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)   



class View3D_TP_Copy2Cursor_panel(bpy.types.Operator):
    """Copy selected object to cursor direction"""
    bl_idname = "tp_ops.copy_to_cursor_panel"
    bl_label = "Copy 2 Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)

    # DRAW PROPS [F6] # 
    def draw(self, context):
        draw_props(self, context)

    # LOAD CUSTOM SETTTINGS #
    def invoke(self, context, event):        
        toc_settings_load(self)
        return self.execute(context)
       
    # EXECUTE MAIN OPERATOR #
    def execute(self, context):

        toc_settings_write(self)
        
        draw_operator(self, context)
            
        return {'FINISHED'}




# PROPERTY GROUP: COPY TO CURSOR #
class ToCursor_Properties(bpy.types.PropertyGroup):
    
    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)



# REGISTRY #
def register():
    bpy.utils.register_module(__name__)
 
    # PROPS TO CURSOR # 
    bpy.types.WindowManager.tocursor_props = PointerProperty(type = ToCursor_Properties)

def unregister():
    bpy.utils.unregister_module(__name__)

    # PROPS TO CURSOR # 
    del bpy.types.WindowManager.tocursor_props

if __name__ == "__main__":
    register()
        
        
