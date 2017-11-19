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
    "name": "CopyShop",
    "author": "marvin.k.breuer",
    "version": (1, 4, 2),
    "blender": (2, 7, 9),
    "location": "View3D / Properties",
    "description": "Tools for duplication",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #
from .copy_ui_menu      import (View3D_TP_Copy_Menu)
from .copy_ui_panel     import (VIEW3D_TP_Copy_Panel_UI)
from .copy_ui_panel     import (VIEW3D_TP_Copy_Panel_TOOLS)
from .copy_ui_panel     import (VIEW3D_TP_Copy_Panel_PROPS)

# LOAD PROPS #
from toolplus_copyshop.copy_mifthcloning    import (MFTCloneProperties)
from toolplus_copyshop.copy_to_meshtarget    import (ToTarget_Properties)

# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_copyshop'))

if "bpy" in locals():
    import importlib
    importlib.reload(copy_action)
    importlib.reload(copy_attributes)
    importlib.reload(copy_dupliset)
    importlib.reload(copy_mifthcloning)
    importlib.reload(copy_multilinked)
    importlib.reload(copy_replicator)
    importlib.reload(copy_fpath)
    importlib.reload(copy_to_all)
    importlib.reload(copy_to_cursor)
    importlib.reload(copy_to_meshtarget)
    importlib.reload(copy_origin)



else:
    from . import copy_action         
    from . import copy_attributes                          
    from . import copy_dupliset                          
    from . import copy_mifthcloning              
    from . import copy_multilinked           
    from . import copy_replicator           
    from . import copy_fpath                 
    from . import copy_to_all       
    from . import copy_to_cursor       
    from . import copy_to_meshtarget    
    from . import copy_origin       
   
    

# LOAD MODULS #

import bpy
from bpy import *
from bpy.props import* 

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
panels_main = (VIEW3D_TP_Copy_Panel_UI, VIEW3D_TP_Copy_Panel_TOOLS, VIEW3D_TP_Copy_Panel_PROPS)

def update_panel_position(self, context):
    message = "CopySHop: Updating Panel locations has failed"
    try:
        for panel in panels_main:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
         
            VIEW3D_TP_Copy_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
            bpy.utils.register_class(VIEW3D_TP_Copy_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Copy_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'props':
            bpy.utils.register_class(VIEW3D_TP_Copy_Panel_PROPS)

        if context.user_preferences.addons[__name__].preferences.tab_location == 'off':  
            return None

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



# MENUS REGISTRY #

addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(View3D_TP_Copy_Menu)
        
        # KEYMAP #
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        View3D_TP_Copy_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(View3D_TP_Copy_Menu)
    
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', shift=True, alt=True) #,ctrl=True 
        kmi.properties.name = 'tp_menu.copyshop_menu'

    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass
    


# ADDON PREFERENCES #

class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolsets',   "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),               
               ('url',        "URLs",       "URLs")),
               default='info')


    # PANEL LOCATION #           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools',    'Tool Shelf',           'place panel in the tool shelf [T]'),
               ('ui',       'Property Shelf',       'place panel in the property shelf [N]'),
               ('props',    'Properties Object',    'place panel in the object properties tab'),
               ('off',      'Off',                  'hide panel')),
               default='tools', update = update_panel_position)

    # MENU # 
    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)



    # PANEL #
    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_pivot = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pivot on', 'enable tools in panel'), ('off', 'Pivot off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_duplicate = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Duplicate on', 'enable tools in panel'), ('off', 'Duplicate off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_radial = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Radial Clone on', 'enable tools in panel'), ('off', 'Radial Clone off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_cursor = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy to Cursor on', 'enable tools in panel'), ('off', 'Copy to Cursor off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_copy_to_mesh = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy to Mesh on', 'enable tools in panel'), ('off', 'Copy to Mesh off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_dupli = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Dupli on', 'enable tools in panel'), ('off', 'Dupli off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_arewo = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ARewO on', 'enable tools in panel'), ('off', 'ARewO off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_array = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Array on', 'enable tools in panel'), ('off', 'Array off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_advance = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Advance Copy on', 'enable tools in panel'), ('off', 'Advance Copy off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_instances = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Instances on', 'enable tools in panel'), ('off', 'Instances off', 'disable tools in panel')), default='on', update = update_display_tools)


    # MENU #
    tab_menu_copy = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Copy on', 'enable tools in panel'), ('off', 'Copy off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_arewo = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Arewo on', 'enable tools in panel'), ('off', 'Arewo off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_array = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Array on', 'enable tools in panel'), ('off', 'Array off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_optimize = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Optimize on', 'enable tools in panel'), ('off', 'Optimize off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_menu_origin = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Origin on', 'enable tools in panel'), ('off', 'Origin off', 'disable tools in panel')), default='on', update = update_display_tools)


    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)
    tools_category_menu = bpy.props.BoolProperty(name = "CopyShop Menu", description = "enable or disable menu", default=True, update = update_menu)


    def draw(self, context):
        layout = self.layout
        
        # INFO #
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to CopyShop!")  
            row.label(text="This addon is for object duplication.")
           
            row.separator()           
           
            row.label(text="The Panels are adaptable can be place in the toolshelf [T] or property shelf [N]")
            row.label(text="Or placed to Properties: 'Object' TAB")
            row.label(text="A included Menu have ALT+SHIFT+Q as shortcut")
           
            row.separator()        
                        
            row.label(text="Have Fun! :)")  
       

        # TOOLS #
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
          
            row = box.row()
            row.label(text="Panel Tools")
           
            row = box.column_flow(5)
            row.prop(self, 'tab_duplicate', expand=True)
            row.prop(self, 'tab_radial', expand=True)
            row.prop(self, 'tab_cursor', expand=True)
            row.prop(self, 'tab_copy_to_mesh', expand=True)
            row.prop(self, 'tab_dupli', expand=True)
            row.prop(self, 'tab_array', expand=True)
            row.prop(self, 'tab_advance', expand=True)
            row.prop(self, 'tab_instances', expand=True)

            box.separator() 
            
            box = layout.box().column(1)
          
            row = box.row()
            row.label(text="Menu Tools")
           
            row = box.column_flow(5)
            row.prop(self, 'tab_menu_copy', expand=True)
            row.prop(self, 'tab_menu_arewo', expand=True)
            row.prop(self, 'tab_menu_array', expand=True)
            row.prop(self, 'tab_menu_optimize', expand=True)
            row.prop(self, 'tab_menu_origin', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for a durably on or off !", icon ="INFO")

            box.separator() 


        # LOCATION #
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location CopyShop:")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for a durably new panel location !", icon ="INFO")

            box.separator()  
            
        # KEYMAP #
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Menu: ALT+SHIFT+Q", icon ="COLLAPSEMENU") 

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
             
            row.operator('wm.url_open', text = '!Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"


            box.separator() 
            
            row = layout.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")


        # WEBLINKS #
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
             
            row = box.column_flow(2) 
            row.operator('wm.url_open', text = 'MifthTools', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?346588-MifthTools-Addon"
            row.operator('wm.url_open', text = 'ARewO', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Animation/ARewO"
            row.operator('wm.url_open', text = 'To All', icon = 'HELP').url = "https://www.artunchained.de/tiny-new-addon-to-all/"
            row.operator('wm.url_open', text = 'Follow Path', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?325179-Follow-Path-Array"
            row.operator('wm.url_open', text = 'Copy2', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?347973-add-on-Copy2-vertices-edges-or-faces"
            row.operator('wm.url_open', text = 'Copy Attributes', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Copy_Attributes_Menu"
            row.operator('wm.url_open', text = 'Dupli Multi Linked', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?229346-AddOn-Duplicate-Multiple-Linked"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?409893-Addon-T-CopyShop&p=3116714#post3116714"


# PROPERTY GROUP #
class Dropdown_TP_CopyShop_Props(bpy.types.PropertyGroup):

    display_copy_to_faces = bpy.props.BoolProperty(name = "Copy to Faces Tools", description = "open / close props", default = False)
    display_toall = bpy.props.BoolProperty(name = "Copy to All", description = "open / close props", default = False)
    display_pfath = bpy.props.BoolProperty(name = "Follow Path Array", description = "open / close props", default = False)
    display_empty = bpy.props.BoolProperty(name = "Empty Array", description = "open / close props", default = False)
    display_array = bpy.props.BoolProperty(name = "Curve Array", description = "open / close props", default = False)
    display_axis_array = bpy.props.BoolProperty(name = "Axis Array", description = "open / close props", default = False)
    display_array_tools = bpy.props.BoolProperty(name = "Array Tools", description = "open / close props", default = False)
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_dupli = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_optimize_tools = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_copy_to_cursor = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    



# PROPERTY GROUP: MIFTHTOOLS #
class MFTCloneProperties(bpy.types.PropertyGroup):

    # RADIAL CLONE #
    mft_create_last_clone = BoolProperty(name="Create Last Clone",description="create last clone...",default=False)
    mft_radialClonesAngle = FloatProperty(default=360.0, min=-360.0,max=360.0)
    mft_clonez = IntProperty(default=8,min=2, max=300)
    mft_radialClonesAxis = EnumProperty(items=(('X', 'X', ''),('Y', 'Y', ''),('Z', 'Z', '')),default = 'Z')
    mft_radialClonesAxisType = EnumProperty(items=(('Global', 'Global', ''),('Local', 'Local', '')),default = 'Global')

    # RELATIONS #    
    mft_single = bpy.props.BoolProperty(name="Unlink",  description="Unlink Clones", default=False)    
    mft_join = bpy.props.BoolProperty(name="Join",  description="Join Clones", default=False)    
    mft_edit = bpy.props.BoolProperty(name="Edit",  description="Editmode", default=False)    

    # TRANSFORM #
    copy_transform_use = bpy.props.BoolProperty(name="Transform",  description="enable transform tools", default=False)  
    mft_origin = bpy.props.BoolProperty(name="Set Origin back",  description="set origin back to previuos postion", default=False)  

    # TRANSFORM LOCATION #
    copy_location_x = bpy.props.FloatProperty(name="X", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_y = bpy.props.FloatProperty(name="Y", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})
    copy_location_z = bpy.props.FloatProperty(name="Z", description="set location value", default=0.00, min=-100, max=100, options={'SKIP_SAVE'})

    # TRANSFORM ROTATE #
    copy_rotate_x = bpy.props.FloatProperty(name="X", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_y = bpy.props.FloatProperty(name="Y ", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})
    copy_rotate_z = bpy.props.FloatProperty(name="Z", description="set rotation value", default=0.00, min=-3.60, max=3.60, options={'SKIP_SAVE'})

    # TRANSFORM SCALE #
    copy_scale_x = bpy.props.FloatProperty(name="X", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_y = bpy.props.FloatProperty(name="Y", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})
    copy_scale_z = bpy.props.FloatProperty(name="Z", description="set scale value", default=1.00, min=0.00, max=100, options={'SKIP_SAVE'})


# PROPERTY GROUP: COPY TO CURSOR #
class ToCursor_Properties(bpy.types.PropertyGroup):
    
    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)
    unlink = bpy.props.BoolProperty(name="Unlink Copies", description ="Unlink Copies" , default = False)
    join = bpy.props.BoolProperty(name="Join Copies", description ="Join Copies" , default = False)



# PROPERTY GROUP: DUPLISET #
class DupliSet_Properties(bpy.types.PropertyGroup):
    
    dupli_align = bpy.props.BoolProperty(name="Align Source",  description="Align Object Location", default=False)       
    dupli_single = bpy.props.BoolProperty(name="Make Real",  description="Single Dupli-Instances", default=False)    
    dupli_separate = bpy.props.BoolProperty(name="Separate all",  description="Separate Objects", default=False)    
    dupli_link = bpy.props.BoolProperty(name="Link separted",  description="Link separated Objects", default=False)   



# REGISTRY #
import traceback

def register():
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position(None, bpy.context)
    update_menu(None, bpy.context)
    update_display_tools(None, bpy.context)

    # PROPS #  
    bpy.types.WindowManager.tp_collapse_copyshop_props = bpy.props.PointerProperty(type = Dropdown_TP_CopyShop_Props)
    
    # PROPS TO CURSOR # 
    bpy.types.WindowManager.tocursor_props = PointerProperty(type = ToCursor_Properties)

    # PROPS DUPLISET # 
    bpy.types.WindowManager.dupliset_props = PointerProperty(type = DupliSet_Properties)

    # PROPS MIFTHTOOLS #
    bpy.types.WindowManager.mifth_clone_props = PointerProperty(type = MFTCloneProperties)

    # PROPS COPY TO TARGET # 
    bpy.types.WindowManager.totarget_props = PointerProperty(type = ToTarget_Properties)



def unregister():
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
   
    # PROPS #
    del bpy.types.WindowManager.tp_collapse_copyshop_props 

    # PROPS TO CURSOR # 
    del bpy.types.WindowManager.tocursor_props
   
    # PROPS DUPLISET # 
    del bpy.types.WindowManager.dupliset_props

    # PROPS MIFTHTOOLS #
    del bpy.types.WindowManager.mifth_clone_props      

    # PROPS COPY TO TARGET # 
    del bpy.types.WindowManager.totarget_props 

if __name__ == "__main__":
    register()
        
        







