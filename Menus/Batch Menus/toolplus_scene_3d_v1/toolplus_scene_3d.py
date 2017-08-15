# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "T+ 3D Scene",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "View3D > Shortcut [M]",
    "description": "Replacement for Move-to-Layer with Move-to-Layer and Visible Scene",
    "warning": "",
    "wiki_url": "",
    "category": "ToolPlus",
}


import bpy
from bpy import *
from bpy.props import*
from bpy.types import AddonPreferences


#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__

    #Tab Prop
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('url',        "URLs",       "URLs")),
               default='info')


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="T+ 3D Scene")  
            row.label(text="Replacement for Move-to-Layer [M]")  
            row.label(text="include: Move-to-Layer and Visible Scene (Layer Properties)")  
            row.label(text="Deactivate the Move-to-Layer Shortcut [M] in TAB INPUT")  
            row.label(text="Search M with key binding > Object Mode")  
            row.label(text="Saver User Setttings and restart Blender")  
                            
            row.label(text="Happy Blending! :)")  


        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?418914-Addon-T-3D-Scene&p=3169536#post3169536"




class View3D_TP_Scene_Batch(bpy.types.Operator):
    """T+ 3D Scene :)"""
    bl_label = "T+ 3D Scene :)"
    bl_idname = "tp_batch.scene_batch"               
    bl_options = {'REGISTER', 'UNDO'}          
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object
        or context.edit_object)
        return (context.mode == 'OBJECT' and isModelingMode)

    def draw(self, context):
        layout = self.layout.column(1)

        scene = context.scene 
        layout.operator_context = 'INVOKE_REGION_WIN'
    
        box = layout.box().column(1)  
                   
        row = box.column(1)

        row.prop(context.object, "layers", text="Move")

        row.separator()
        
        row.prop(context.scene, "layers", text="Scene")

        box.separator()
        box.separator()
        

    def execute(self, context):   
        return {'FINISHED'}

    def check(self, context):
        return True

    def invoke(self, context, event):
        dpi_value = bpy.context.user_preferences.system.dpi        
        return context.window_manager.invoke_props_dialog(self, width=dpi_value*3, height=300)




# Registry
addon_keymaps = []

def register():
   
    bpy.utils.register_module(__name__)

    #KeyMap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('tp_batch.scene_batch', 'M', 'PRESS')
    kmi.active = True
    addon_keymaps.append((km, kmi))
    
    
def unregister():
   
    bpy.utils.unregister_module(__name__)
    
    #KeyMap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)        
    addon_keymaps.clear()  

   
if __name__ == "__main__":
    register()  


