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
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
 

# LOAD UI #  
from toolplus_bounding.bound_history    import draw_history_layout
from toolplus_bounding.bound_main       import draw_panel_layout


class VIEW3D_TP_Bound_Menu(bpy.types.Operator):
    """Bounding Menu"""
    bl_idname = "tp_menu.bound_menu"
    bl_label = "Bounding"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):      
        return {'FINISHED'}
           
    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.scene and context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)

    def draw(self, context):

        layout = self.layout
   
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_panel_layout(context, layout)    

        panel_prefs = context.user_preferences.addons[__package__].preferences
        if panel_prefs.tab_display_history == True:
            
            draw_history_layout(context, layout)    
        

    def check(self, context):
        return True


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
