# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
        'name': "Kjartans Scripts",
        'author': "Kjartan Tysdal",
        'location': '"Shift+Q" and also in EditMode "W-Specials/ KTools"',
        'description': "Adds my personal collection of small handy scripts (mostly modeling tools)",
        'category': "Mesh",
        'blender': (2, 7, 6),
        'version': (0, 2, 7),
        'wiki_url': 'http://www.kjartantysdal.com/scripts',
}


import bpy
from bpy import*
from bpy.props import *

class toggleSilhouette(bpy.types.Operator):
    """Turns everything black so that you can evaluate the overall shape. Useful when designing"""
    bl_idname = "tp_ops.toggle_silhouette"
    bl_label = "Toggle Silhouette"

    
    diff_col = FloatVectorProperty(default = (0.226, 0.179, 0.141))
    disp_mode = StringProperty(default = 'SOLID')
    matcap = BoolProperty(default = False)
    only_render = BoolProperty(default = False)
    
    def execute(self, context):
        
        
        light_check = bpy.context.user_preferences.system.solid_lights[0].use

        if light_check == True:
            # Set Lights to Off
            bpy.context.user_preferences.system.solid_lights[0].use = False
            bpy.context.user_preferences.system.solid_lights[1].use = False
            
            # Store variables
            self.diff_col = bpy.context.user_preferences.system.solid_lights[2].diffuse_color
            self.disp_mode = bpy.context.space_data.viewport_shade
            self.matcap = bpy.context.space_data.use_matcap
            self.only_render = bpy.context.space_data.show_only_render
            
            bpy.context.user_preferences.system.solid_lights[2].diffuse_color = 0,0,0
            bpy.context.space_data.viewport_shade = 'SOLID'
            bpy.context.space_data.use_matcap = False
            bpy.context.space_data.show_only_render = True
            
        else:
            bpy.context.user_preferences.system.solid_lights[0].use = True
            bpy.context.user_preferences.system.solid_lights[1].use = True
            bpy.context.user_preferences.system.solid_lights[2].diffuse_color = self.diff_col
            bpy.context.space_data.viewport_shade = self.disp_mode
            bpy.context.space_data.use_matcap = self.matcap
            bpy.context.space_data.show_only_render = self.only_render
        
        return {'FINISHED'}


        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


