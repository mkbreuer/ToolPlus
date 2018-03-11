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
"name": "Visuals", 
"author": "marvin.k.breuer (MKB)",
"version": (0, 1, 1),
"blender": (2, 7, 9),
"location": "3D View",
"description": "display tools for the 3D view",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "ToolPlus"
}



# LOAD UI #
from toolplus_visuals.ui_panel    import (VIEW3D_TP_Visuals_Panel_TOOLS)
from toolplus_visuals.ui_panel    import (VIEW3D_TP_Visuals_Panel_UI)


# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_visuals'))

if "bpy" in locals():
    import imp
    
    imp.reload(autowire)
    imp.reload(delete)     
    imp.reload(display)
    imp.reload(fastnavi)
    imp.reload(navigation)
    imp.reload(material)
    imp.reload(matswitch)
    imp.reload(normals)
    imp.reload(normals_transfer)
    imp.reload(normals_weighted)
    imp.reload(opengl)
    imp.reload(orphan) 
    imp.reload(silhouette)

else:

    from .ops_visuals import autowire
    from .ops_visuals import delete   
    from .ops_visuals import display
    from .ops_visuals import fastnavi
    from .ops_visuals import navigation
    from .ops_visuals import material
    from .ops_visuals import matswitch
    from .ops_visuals import normals
    from .ops_visuals import normals_transfer
    from .ops_visuals import normals_weighted
    from .ops_visuals import opengl    
    from .ops_visuals import orphan  
    from .ops_visuals import silhouette


# LOAD MODULS #
import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
panels_main = (VIEW3D_TP_Visuals_Panel_UI, VIEW3D_TP_Visuals_Panel_TOOLS)

def update_panel_position(self, context):
    message = "T+ Visuals: Updating Panel locations has failed"
    try:
        for panel in panels_main:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels_main:
            if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
             
                VIEW3D_TP_Visuals_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
                bpy.utils.register_class(VIEW3D_TP_Visuals_Panel_TOOLS)
            
            if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
                bpy.utils.register_class(VIEW3D_TP_Visuals_Panel_UI)

            if context.user_preferences.addons[__name__].preferences.tab_location == 'off':  
                pass

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



# TOOLS REGISTRY #
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass        
        
        
        
# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__


    prefs_tabs = EnumProperty(
        items=(('location',   "Location",   "Location"),
               ('toolsets',   "Tools",      "Tools"),
               ('url',        "URLs",       "URLs")),
               default='location')
          
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'enable or disable panel in the shelf')),
               default='tools', update = update_panel_position)

    tab_history = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)


    def draw(self, context):
        layout = self.layout
        
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
            
        # LOCATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_location', expand=True)

            row = box.row()            
            if self.tab_location == 'tools':
                row.prop(self, "tools_category")

            box.separator()
      
       
        # TOOLS #
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)

            row = box.row()
            row.label("Tools in Panel")            

            row = box.column_flow(4)                  
            row.prop(self, 'tab_history', expand=True)

            box.separator() 
            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        # WEB #
        if self.prefs_tabs == 'url':
            row = layout.row()
            row.operator('wm.url_open', text = 'T+ on GitHub', icon = 'INFO').url = "https://github.com/mkbreuer/ToolPlus"





# PROPERTY GROUP #
class Dropdown_TP_Visual_Props(bpy.types.PropertyGroup):

    display_world_set = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_aoccl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_grid = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_fastnav = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_more_mat = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_more = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_lens = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_navi = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    

    mat_mode = bpy.props.StringProperty(default="")
    index_count_sw = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)     
    mat_switch = bpy.props.EnumProperty(
                              items = [("tp_mat_00", "Light", "", 1),
                                       ("tp_mat_01", "Darken",  "", 2)],
                                       name = "",
                                       default = "tp_mat_00",  
                                       description="material index switch") 

    new_swatch = FloatVectorProperty(name = "Color", default=[0.0,1.0,1.0], min = 0, max = 1,  subtype='COLOR')
    index_count = bpy.props.IntProperty(name="MAT-ID",  description="set material index", min=0, max=100, default=0)  
    matrandom = bpy.props.BoolProperty(name="ID-Switch / ID-Random", description="enable random material", default=False)  


class Display_Tools_Props(bpy.types.PropertyGroup):
    
    Delay = BoolProperty(default=False, description="Activate delay return to normal viewport mode")
    DelayTime = IntProperty(default=30, min=0, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    DelayTimeGlobal = IntProperty(default=30, min=1, max=500, soft_min=10, soft_max=250, description="Delay time to return to normal viewportmode after move your mouse cursor")
    EditActive = BoolProperty(default=True, description="Activate for fast navigate in edit mode too")
    FastNavigateStop = BoolProperty(name="Fast Navigate Stop", description="Stop fast navigate mode", default=False)    
    ShowParticles = BoolProperty(name="Show Particles", description="Show or hide particles on fast navigate mode", default=True)  
    ParticlesPercentageDisplay = IntProperty(name="Display", default=25, min=0, max=100, soft_min=0, soft_max=100, subtype='FACTOR', description="Display only a percentage of particles")
    InitialParticles = IntProperty( name="Count for initial particle setting before entering fast navigate", description="Display a percentage value of particles", default=100, min=0, max=100, soft_min=0, soft_max=100)
    ScreenStart = IntProperty(name="Left Limit", default=0, min=0, max=1024, subtype='PIXEL', description="Limit the screen active area width from the left side\n changed values will take effect on the next run")
    ScreenEnd = IntProperty( name="Right Limit", default=0, min=0, max=1024, subtype='PIXEL', description="Limit the screen active area width from the right side\n changed values will take effect on the next run")
    FastMode = EnumProperty(items=[('WIREFRAME', 'Wireframe', 'Wireframe display'), ('BOUNDBOX', 'Bounding Box', 'Bounding Box display')], name="Fast")
    OriginalMode = EnumProperty(items=[('TEXTURED', 'Texture', 'Texture display mode'), ('SOLID', 'Solid', 'Solid display mode')], name="Normal", default='SOLID')

    WT_handler_enable = BoolProperty(default=False)
    WT_handler_previous_object = StringProperty(default="")

class Orphan_Tools_Props(bpy.types.PropertyGroup):
   
    mod_list = bpy.props.EnumProperty(
                       items = [tuple(["meshes"]*3),        tuple(["armatures"]*3), 
                                tuple(["cameras"]*3),       tuple(["curves"]*3),
                                tuple(["fonts"]*3),         tuple(["grease_pencil"]*3),
                                tuple(["groups"]*3),        tuple(["images"]*3),
                                tuple(["lamps"]*3),         tuple(["lattices"]*3),
                                tuple(["libraries"]*3),     tuple(["materials"]*3),
                                tuple(["actions"]*3),       tuple(["metaballs"]*3),
                                tuple(["node_groups"]*3),   tuple(["objects"]*3),
                                tuple(["sounds"]*3),        tuple(["texts"]*3), 
                                tuple(["textures"]*3),      tuple(["speakers"]*3)],
                                name = "",
                                default = "meshes", 
                                description="Target: Module choice made for orphan deletion")



    
# REGISTRY #
import traceback

def register():  

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_display_tools(None, bpy.context)
    update_panel_position(None, bpy.context)

    # PROPS #  
    bpy.types.WindowManager.tp_props_visual = bpy.props.PointerProperty(type = Dropdown_TP_Visual_Props)      
    bpy.types.Scene.display_props = bpy.props.PointerProperty(type=Display_Tools_Props)
    bpy.types.Scene.orphan_props = bpy.props.PointerProperty(type=Orphan_Tools_Props)

    
def unregister():
    
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # PROPS #  
    del bpy.types.WindowManager.tp_props_visual
    del bpy.types.Scene.display_props
    del bpy.types.Scene.orphan_props

    
if __name__ == "__main__":
    register()      
    

                 




