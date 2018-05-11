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


bl_info = {
    "name": "T+ Load UI",
    "author": "marvin.k.breuer (MKB)",
    "version": (1,2),
    "blender": (2, 7, 7),
    "location": "View3D > Property Shelf [N] > Backround Images Panel",
    "description": "add the 'Load UI' button from User Preferences > File, to the Backround Images Panel in the 3d View Property Shelf.",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_load_ui'))

if "bpy" in locals():
    import imp
    imp.reload(fast_import)
    imp.reload(fast_transform)
else:
    from . import fast_import                
    from . import fast_transform                

# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from bpy.types import AddonPreferences, PropertyGroup

import rna_keymap_ui
#def get_keymap_item(km, kmi_name, kmi_value):
def get_keymap_item(km, kmi_value):
    for i, km_item in enumerate(km.keymap_items):
#        if km.keymap_items.keys()[i] == kmi_name: 
#            if km.keymap_items[i].properties.name == kmi_value:
            if km.keymap_items.keys()[i] == kmi_value:
                return km_item
    return None

def draw_keymap_item(km, kmi, kc, layout):
    if kmi:
        layout.context_pointer_set("keymap", km)
        rna_keymap_ui.draw_kmi([], kc, km, kmi, layout, 0)

        
        
# ADDON PREFERNECES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    tab_fast_transform = bpy.props.BoolProperty(name="Fast Transform",  description="Add Fast Transform Keys: G = Move, R = Rotate, S = Scale, Mousewheel = Image Select // need blender restart", default=False, options={'SKIP_SAVE'})  

    def draw(self, context):
        layout = self.layout
       
        layout.separator()        
       
        col = layout.row()        
        col.prop(self, 'tab_fast_transform', text= "Add Keys", icon ="AXIS_TOP")
       
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user
        km = kc.keymaps['3D View']
        #kmi = get_keymap_item(km, 'wm.call_menu', 'view3d.background_image_transform')
        kmi = get_keymap_item(km, 'view3d.background_image_transform')
        draw_keymap_item(km, kmi, kc, col) 

        layout.separator()

        layout = layout.column_flow(2)         
        layout.operator('wm.url_open', text = 'Thread', icon = 'INFO').url = "https://blenderartists.org/t/addon-t-load-ui/670951/5"
        layout.operator('wm.url_open', text = 'GitHub', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus"
        layout.operator('wm.url_open', text = 'Fast Import', icon = 'INFO').url = "https://blenderartists.org/t/addon-background-images-fast-import/655653/13"
        layout.operator('wm.url_open', text = 'Fast Transform', icon = 'INFO').url = "https://github.com/LesFeesSpeciales/image-background-transform"



# LOAD UI #
def load_ui_to_bg_images(self,context):
    layout = self.layout
    
    col = layout.row()
    col.prop(context.user_preferences.filepaths, "use_load_ui", text= "Save & Load UI")
    panel_prefs = context.user_preferences.addons[__name__].preferences
    col.prop(panel_prefs, 'tab_fast_transform', text= "", icon ="AXIS_TOP")  
    #col.operator("view3d.background_image_transform")
    col.operator("view3d.background_images_fast_import", text= "", icon ="IMAGE_COL")






# KEY REGISTRY # 
addon_keymaps = []

def update_keymap(self, context):
    try:
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_fast_transform == True:
    
        # Keymapping 
        wm = bpy.context.window_manager        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('view3d.background_image_transform', 'B', 'PRESS', alt=True, shift=True)

    if context.user_preferences.addons[__name__].preferences.tab_fast_transform == False:
        
        wm = bpy.context.window_manager
        for km in addon_keymaps:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps[:]




# REGISTRY #

import traceback
def register():

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.VIEW3D_PT_background_image.append(load_ui_to_bg_images)    

    update_keymap(None, bpy.context)

def unregister():    

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    bpy.types.VIEW3D_PT_background_image.remove(load_ui_to_bg_images)  

if __name__ == "__main__":
    register()  




              
