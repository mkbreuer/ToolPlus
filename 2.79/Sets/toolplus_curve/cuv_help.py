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
import bpy
from bpy import *
from bpy.props import *
#from . icons.icons import load_icons    



class VIEW3D_TP_Curve_Help_Prefs(bpy.types.Operator):
    bl_idname = 'tp_ops.help_curve_prefs'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout

        addon_key = __package__.split(".")[0]    

        layout.label("", icon = "TRIA_DOWN") 

        if context.user_preferences.addons[addon_key].preferences.tab_location_option_switch == 'panels':
         
            layout.label("Choose between 3 layout styles", icon = "LAYER_USED") 
            layout.label("For durable use: save user settings ", icon = "LAYER_USED") 
            layout.label("No changes?: restart blender!", icon = "LAYER_USED") 


        if context.user_preferences.addons[addon_key].preferences.tab_location_option_switch == 'menus':

            layout.label("To adjust hotkey go to", icon = "LAYER_USED") 
            layout.operator("screen.userpref_show", text="Addon Preferences...", icon='PREFERENCES')

        if context.user_preferences.addons[addon_key].preferences.tab_location_option_switch == 'tools':

            layout.label("Tools activation in panel / menu", icon = "LAYER_USED") 
        
        layout.label("", icon = "TRIA_UP") 

    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 200)
    


class VIEW3D_TP_Curve_Help_Append(bpy.types.Operator):
    bl_idname = 'tp_ops.help_curve_append'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout

        addon_key = __package__.split(".")[0]    

        layout.label("") 

        layout.label("Need a restart to see a effect", icon = "LAYER_USED")         

        layout.label("") 
    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 200)
    
    
    

class VIEW3D_TP_Curve_Help_Custom(bpy.types.Operator):
    bl_idname = 'tp_ops.help_curve_custom'
    bl_label = ''
    bl_options = {'REGISTER', 'UNDO'}  

    def draw(self, context):
        layout = self.layout

        addon_key = __package__.split(".")[0]    

        layout.label("") 

        layout.label("Custom Layout", icon = "SPACE3")         
        layout.label("To open the custom layout press on the gear/script button", icon = "LAYER_USED") 
        layout.label("It opens the lauyout file in the text editor", icon = "LAYER_USED") 
        layout.label("Open text editor and open the dropdown menu in the header", icon = "LAYER_USED") 
        layout.label("Browse the python file > name: ui_custom.py (red highlighted)", icon = "LAYER_USED") 
      
        layout.label("")        
                
        layout.label("Adding new Functions ", icon = "SPACE3") 
        layout.label("Go to a needed Function-Button and click with right-mouse.", icon = "LAYER_USED") 
        layout.label("In the context menu press on the 'edit source' function.", icon = "LAYER_USED") 
        layout.label("It opens files from other addons in the text editor, too. ", icon = "LAYER_USED") 
        layout.label("Than copy and past the needed into the custom layout script.", icon = "LAYER_USED") 
        layout.label("Be aware that you use the right formats and correct row indent.", icon = "LAYER_USED") 
        layout.label("After adding new function in, save the file and restart blender", icon = "LAYER_USED") 

        layout.label("") 

    
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width = 350)
    


    
# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()