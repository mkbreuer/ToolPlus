# ##### BEGIN GPL LICENSE BLOCK #####
#
#Copyright (C) 2017  Marvin.K.Breuer (MKB)]
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
    "name": "T+ Scene",
    "author": "MKB",
    "version": (0, 2, 3),
    "blender": (2, 7, 8),
    "location": "VIEW3D",
    "description": "Restrict, Apply, Remove, (Un)Hide or Rename object with group layer system",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD: PROPS #
from toolplus_scene.ops_layer  import apply_layer_settings


# LOAD: UI #
from toolplus_scene.gui_panel  import (VIEW3D_TP_Scene_Panel_TOOLS)
from toolplus_scene.gui_panel  import (VIEW3D_TP_Scene_Panel_UI)

# LOAD PRESETS #
from toolplus_scene.operators.opengl    import (opengl_setup)

# LOAD: ICONS #
from . icons.icons  import load_icons
from . icons.icons  import clear_icons


# LOAD: FILES # 
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_scene'))

if "bpy" in locals():
    import imp

    imp.reload(ops_layer)

    imp.reload(copy)
    imp.reload(rename)
    imp.reload(mods_type)

    imp.reload(action)
    imp.reload(display)
    imp.reload(fast_navigate)
    imp.reload(material)
    imp.reload(opengl)
    imp.reload(silhouette)
    imp.reload(smartjoin)
    imp.reload(toall)


else:              
             
    from . import ops_layer               

    from .operators import copy  
    from .operators import rename               
    from .operators import mods_type               

    from .operators import action
    from .operators import display
    from .operators import fast_navigate
    from .operators import material
    from .operators import opengl
    from .operators import silhouette
    from .operators import smartjoin
    from .operators import toall




# LOAD: MODULS # 
import bpy
from bpy import*
from bpy.props import*
from bpy.types import AddonPreferences, PropertyGroup



# REGISTRY: 3D VIEW PANEL # 
def update_panel_position(self, context):
    try:      
        bpy.utils.unregister_class(VIEW3D_TP_Scene_Panel_UI)       
        bpy.utils.unregister_class(VIEW3D_TP_Scene_Panel_TOOLS)   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Scene_Panel_UI)
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_Scene_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category        
        bpy.utils.register_class(VIEW3D_TP_Scene_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Scene_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass


# REGISTRY: STACK TOOLS # 
def update_modtools_position(self, context):
    try:           
        bpy.types.DATA_PT_modifiers.remove(menu_func)    
    except:
        pass
    try:
        bpy.types.DATA_PT_modifiers.remove(menu_func) 
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_location_mod == 'win':
        bpy.types.DATA_PT_modifiers.prepend(menu_func)

    if context.user_preferences.addons[__name__].preferences.tab_location_mod == 'off':
        pass


# REGISTRY: PANEL TOOLS # 
def update_display_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        pass     



# PANEL PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',     "Info",       "Info"),  
               ('location', "Location",   "Location"),  
               ('tools',   "Tools",      "Tools"),
               ('url',      "URLs",       "URLs")),
               default='location')

    # PROPS: PANEL #         
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Panel Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_position)

    # PROPS: TOOLS #          
    tab_location_mod = EnumProperty(
        name = 'Properties: Modifier',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('win', 'Tools On', 'place operators over the modifier stack'),
               ('off', 'Tools Off', 'on or off for panel in the shelfs')),
               default='off', update = update_modtools_position)



    # UPADTE: TOOLSETS #
    tab_display_modly = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Layers on', 'enable tools in panel'), ('off', 'Layers off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_display_modtl = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Modifier by Type on', 'enable tools in panel'), ('off', 'Modifier by Type off', 'disable tools in panel')), default='off', update = update_display_tools)

    tab_display_smjoint = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SmartJoin on', 'enable tools in panel'), ('off', 'SmartJoin off', 'disable tools in panel')), default='off', update = update_display_tools)

    tab_display_visual = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Visual on', 'enable tools in panel'), ('off', 'Visual off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_display_advance = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Advance on', 'enable more tools in panel'), ('off', 'Advance off', 'disable more tools in panel')), default='off', update = update_display_tools)


    # UPADTE: PANEL #
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)

    def draw(self, context):
        layout = self.layout
        
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
             

        # INFO #
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
             
            row = box.column(1) 
            row.label("T+ Layers")
            row.label("> it restrict objects in the 3D Viewport")
            row.label("> and modifier by type on assigned layers")

            box.separator()
            box.separator()
            
            row.label("How to restrict:")
            row.label("1. Add a Layer")
            row.label("2. Select a group of objects and assign it to the layer")
            row.label("3. enable or disable the restriction for the layers: visibility, render, wire and selection")
 
            box.separator() 
            box.separator() 
            
            row.label("How to: modifiere by type")
            row.label("4. choose a modifier type")
            row.label("5. choose a modifier function type")
            row.label("6. enable or disable the restrict for the modifier")
            row.label("7. or move, delete or apply modifier")
            row.label("8. the latter can only be reversed with [CTRL+Z]")

            box.separator() 
            box.separator() 

            row.label("Happy Blending!")

                        


        # LOACATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location: 3D View Panel")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
            
            box.separator()

            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location: Modifier Stack")
            
            row = box.row(1)
            row.prop(self, 'tab_location_mod', expand=True)
            
            box.separator()


        # TOOLS #
        if self.prefs_tabs == 'tools':

            box = layout.box().column(1)

            row = box.row()
            row.label(text="ToolSet in Panel", icon ="INFO")

            row = box.column_flow(4)
            row.prop(self, 'tab_display_modly', expand=True)
            row.prop(self, 'tab_display_modtl', expand=True)
            row.prop(self, 'tab_display_smjoint', expand=True)
            row.prop(self, 'tab_display_visual', expand=True)
            row.prop(self, 'tab_display_advance', expand=True) 

            box.separator() 
            box.separator()

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        # WEB #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column_flow(2)
            row.operator('wm.url_open', text = 'Display Tools', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Display_Tools"
            row.operator('wm.url_open', text = 'SmartJoin', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?370664-Non-destructive-joining-grouping-addon"
            row.operator('wm.url_open', text = 'Renaming Objects', icon = 'INFO').url = "https://www.youtube.com/watch?v=ztnfo6eKtL8"
            row.operator('wm.url_open', text = 'Display Layers', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?388166-Addon-Display-Layers-(unlimited)&highlight="
            row.operator('wm.url_open', text = 'Copy Attributes', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Copy_Attributes_Menu"
            row.operator('wm.url_open', text = 'OpenGL', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?346612-The-most-efficient-OpenGL-Lights-panel-(with-presets-system)"
            row.operator('wm.url_open', text = 'Thread', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?409425-Addon-T-Scene&highlight="
            row.operator('wm.url_open', text = 'GitHub', icon = 'PACKAGE').url = "https://github.com/mkbreuer"
            row.operator('wm.url_open', text = 'DEMO', icon = 'CLIP').url = "https://youtu.be/gR-8uHGESG4"



# OPERATOR MENU #
def menu_func(self, context):
    layout = self.layout
    
    obj = context.active_object

    if obj:                       
        mod_list = obj.modifiers
        if mod_list:
                                           
            row = layout.row(1)        
            row.operator("tp_ops.copy_choosen_mods", text="CopyDial", icon='PASTEDOWN') 
            row.prop(context.scene, "tp_mods_type", text="")
            row.prop(context.scene, "tp_func_type", text="")
            row.operator("tp_ops.mods_by_type", text="RunTypes", icon='FRAME_NEXT')                       
            

        else:
            pass



# LAYER: CALL BACK #
def display_toggle_callback(self, context):
    apply_layer_settings(context)

# LAYER: CUSTOM PROPERTIES #
class property_collection_display_layers(bpy.types.PropertyGroup):
    # assign a collection

    name = bpy.props.StringProperty(name="Layer name", default="Layer"),
    display = bpy.props.BoolProperty(name="Display", default=True, update=display_toggle_callback)
    select = bpy.props.BoolProperty(name="Select", default=True, update=display_toggle_callback)
    render = bpy.props.BoolProperty(name="Render", default=True, update=display_toggle_callback)
    wire = bpy.props.BoolProperty(name="Wire", default=False, update=display_toggle_callback)
    mody = bpy.props.BoolProperty(name="Modifier", default=False, update=display_toggle_callback)

# LAYER: PROPERTY #
class multilight_properties(bpy.types.PropertyGroup):

    bpy.types.Object.display_layer = bpy.props.IntProperty(name="Layer ID", description="", default=0, min=0, update=display_toggle_callback)
    bpy.types.Object.use_display_layer = bpy.props.BoolProperty(name="Use Layer", description="", default=0, update=display_toggle_callback)    
    bpy.types.Scene.display_layers_collection_index = bpy.props.IntProperty(name="Layer Scene Index", description="---", default=0, min=0)





# OPERATOR: SELECT OBJECTS IN LAYER #
class layers_select_objects(bpy.types.Operator):
    bl_idname = "select_objects.btn"
    bl_label = "Select"
    bl_description = "Select objects"

    @classmethod
    def poll(cls, context):
        return context.object and context.scene.display_layers_collection.items()

    def execute(self, context):
        active_layer_index = context.scene.display_layers_collection_index

        for obj in context.scene.objects:
            if obj.use_display_layer and obj.display_layer == active_layer_index:                    
                    obj.select = True
                    obj.select = True


        return{'FINISHED'}



# PROPERTY GROUP #
class Dropdown_ModTool_Props(bpy.types.PropertyGroup):

    display_layer_id = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)  

    display_smooth = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_visual = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_grid = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_aoccl = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_world_set = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    




# REGISTER #
import traceback

def register():
    
    # PRESETS #
    opengl_setup()

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_display_tools(None, bpy.context)
    update_panel_position(None, bpy.context)
    update_modtools_position(None, bpy.context)

    bpy.types.WindowManager.tp_collapse_menu_layer = bpy.props.PointerProperty(type = Dropdown_ModTool_Props)

    # LAYERS #
    bpy.types.Scene.display_layers_collection = bpy.props.CollectionProperty(type=property_collection_display_layers)
    bpy.types.Scene.display_layers_collection_index = bpy.props.IntProperty(name = "Layer Scene Index", description = "---", default = 0, min = 0)

    # RENAME #
    bpy.types.Scene.rno_list_selection_ordered = bpy.props.EnumProperty(name="selection orderer", items=[])    
    bpy.types.Scene.rno_str_new_name = bpy.props.StringProperty(name="New name", default='')
    bpy.types.Scene.rno_str_old_string = bpy.props.StringProperty(name="Old string", default='')
    bpy.types.Scene.rno_str_new_string = bpy.props.StringProperty(name="New string", default='')
    bpy.types.Scene.rno_str_numFrom = bpy.props.StringProperty(name="from", default='')
    bpy.types.Scene.rno_str_prefix = bpy.props.StringProperty(name="Prefix", default='')
    bpy.types.Scene.rno_str_subfix = bpy.props.StringProperty(name="Subfix", default='')    
    bpy.types.Scene.rno_bool_numbered = bpy.props.BoolProperty(name='numbered', default=True)
    bpy.types.Scene.rno_bool_keepOrder = bpy.props.BoolProperty(name='keep selection order')
    bpy.types.Scene.rno_bool_keepIndex = bpy.props.BoolProperty(name='keep object Index', default=True)

    # SMARTJOIN #
    bpy.types.Mesh.is_sjoin = BoolProperty(default=False)
    bpy.types.Mesh.sjoin_link_name = StringProperty()
    bpy.types.Mesh.expanded_obj = StringProperty()
    bpy.types.Object.sjoin_mesh = StringProperty(default = '')



# UNREGISTER #
def unregister():

    # LAYERS #  
    del bpy.types.Scene.display_layers_collection
    del bpy.types.Scene.display_layers_collection_index  

    # RENAME # 
    del bpy.types.Scene.rno_str_new_name
    del bpy.types.Scene.rno_str_old_string
    del bpy.types.Scene.rno_str_new_string
    del bpy.types.Scene.rno_bool_keepOrder
    del bpy.types.Scene.rno_bool_numbered
    del bpy.types.Scene.rno_list_selection_ordered
    del bpy.types.Scene.rno_str_prefix
    del bpy.types.Scene.rno_str_subfix
    del bpy.types.Scene.rno_bool_keepIndex 

    # SMARTJOIN #
    del bpy.types.Mesh.is_sjoin
    del bpy.types.Object.sjoin_mesh

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
if __name__ == "__main__":
    register()
        
        




              









