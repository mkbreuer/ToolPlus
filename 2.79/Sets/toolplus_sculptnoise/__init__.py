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


bl_info = {
    "name": "T+ SculptNoise",
    "author": "Marvin.K.Breuer (MKB)",
    "version": (0, 1),
    "blender": (2, 7, 9),
    "location": "View3D > Sculptmode > Tool Shelf [T] or Property Shelf [N] > Panel: SculptNoise",
    "description": "paint noise to sculpt mesh",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD ICONS #
from . icons.icons              import load_icons
from . icons.icons              import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_sculptnoise'))


if "bpy" in locals():
    import imp

    imp.reload(ops_action)          
    imp.reload(ops_displace)                    
    imp.reload(ops_modifier)                    
  

    print("Reloaded multifiles")
    
else:

    from . import ops_action        
    from . import ops_displace        
    from . import ops_modifier        

    from .ui_map import* 

    print("Imported multifiles")


# LOAD MODULS #  
import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup


# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    # TAB LOACATION #         
    tab_location_sculptnoise = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_sculptnoise)


    # UPADTE: PANEL #
    tools_category_sculptnoise = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_sculptnoise)


    def draw(self, context): 

        layout = self.layout

        box = layout.box().column(1)
         
        row = box.row(1) 
        row.label("Panel Location:")
        
        row = box.row(1)
        row.prop(self, 'tab_location_sculptnoise', expand=True)
      
        box.separator() 
    
        row = box.row(1)            
        if self.tab_location_sculptnoise == 'tools':
            
            box.separator() 
            
            row.prop(self, "tools_category_sculptnoise")

        box.separator() 
        box.separator() 

        row = box.row()
        row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/t/addon-sculptnoise/1124359"
        row.operator('wm.url_open', text = 'GitHub', icon = 'BLENDER').url = "https://github.com/mkbreuer/ToolPlus"




# PROPS FOR PANEL #
class Dropdown_SculptNoise_Panel_Props(bpy.types.PropertyGroup):

    display_sculpt_noise = bpy.props.BoolProperty(name="Show Displace Settings", description="open / close properties", default=False)




# REGISTRY #
import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    
    # PROPS #
    bpy.types.WindowManager.tp_sculptnoise_props = bpy.props.PointerProperty(type = Dropdown_SculptNoise_Panel_Props)

    update_panel_sculptnoise(None, bpy.context)


def unregister():

    # PROPS #
    del bpy.types.WindowManager.tp_sculptnoise_props

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()



    
if __name__ == "__main__":
    register()
        
        



            



