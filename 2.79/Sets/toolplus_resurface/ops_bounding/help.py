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


# HELP OPERATOR #
class TP_BBox_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bbox'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("1.)  Object Type: plane and cubic geometry", icon = "LAYER_USED") 
        layout.label("2.)  Mesh Type: shaded > default mesh geometry", icon = "LAYER_USED") 
        layout.label("3.)  Mesh Type: shade off > transparent mesh", icon = "LAYER_USED") 
        layout.label("4.)  Mesh Type: wire only > deleted faces", icon = "LAYER_USED") 
        layout.label("5.)  Settings: stores last used adjustments", icon = "LAYER_USED") 
        layout.label("6.)  Use redo last [F6] to change settings on the fly", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")     

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 300)



# HELP OPERATOR #
class TP_BCyl_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bcyl'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("1.)  Object Type: circle and cylindric geometry", icon = "LAYER_USED") 
        layout.label("2.)  Mesh Type: shaded > default mesh geometry", icon = "LAYER_USED") 
        layout.label("3.)  Mesh Type: shade off > transparent mesh", icon = "LAYER_USED") 
        layout.label("4.)  Mesh Type: wire only > deleted faces", icon = "LAYER_USED") 
        layout.label("5.)  Settings: stores last used adjustments", icon = "LAYER_USED") 
        layout.label("6.)  Use redo last [F6] to change settings on the fly", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 300)
    

# HELP OPERATOR #
class TP_BSph_Help(bpy.types.Operator):
    bl_idname = 'tp_ops.help_bsph'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout
        layout.label("", icon = "TRIA_DOWN") 
        layout.label("1.)  Object Type: spheric geometry", icon = "LAYER_USED") 
        layout.label("2.)  Mesh Type: shaded > default mesh geometry", icon = "LAYER_USED") 
        layout.label("3.)  Mesh Type: shade off > transparent mesh", icon = "LAYER_USED") 
        layout.label("4.)  Mesh Type: wire only > deleted faces", icon = "LAYER_USED") 
        layout.label("5.)  Settings: stores last used adjustments", icon = "LAYER_USED") 
        layout.label("6.)  Use redo last [F6] to change settings on the fly", icon = "LAYER_USED") 
        layout.label("", icon = "TRIA_UP")  
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 300)




# REGISTRY #
def register():
    bpy.utils.register_module(__name__) 

def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


