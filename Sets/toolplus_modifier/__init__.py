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
    "name": "T+ Modifier",
    "author": "MKB",
    "version": (1, 3, 1),
    "blender": (2, 7, 8),
    "location": "VIEW3D > Tool Shelf [T] or Property Shelf [N] and Properties TAB: Modifier",
    "description": "panels and menu for modifier tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


# LOAD UI #
from toolplus_modifier.mods_ui_menu         import (VIEW3D_TP_Modifier_Menu)

from toolplus_modifier.mods_ui_stack        import (VIEW3D_TP_Modifier_Stack_Panel_UI)
from toolplus_modifier.mods_ui_stack_tools  import (VIEW3D_TP_Modifier_Stack_Panel_TOOLS)

from toolplus_modifier.mods_ui_panel        import (VIEW3D_TP_Modifier_Panel_TOOLS)
from toolplus_modifier.mods_ui_panel        import (VIEW3D_TP_Modifier_Panel_UI)


# LOAD ICONS #
from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons


# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_modifier'))

if "bpy" in locals():
    import imp
    imp.reload(mods_action)
    imp.reload(mods_array)
    imp.reload(mods_batch)
    imp.reload(mods_batch_atm)
    imp.reload(mods_bevel)
    imp.reload(mods_cut_auto)
    imp.reload(mods_display)
    imp.reload(mods_mirror)
    imp.reload(mods_mirror_auto)
    imp.reload(mods_normals)
    imp.reload(mods_pivot)
    imp.reload(mods_remove)
    imp.reload(mods_sdeform)
    imp.reload(mods_show)
    imp.reload(mods_solidifiy)
    imp.reload(mods_subsurf)
    imp.reload(mods_toall)
    imp.reload(mods_tools)


else:
    from . import mods_action         
    from . import mods_array                
    from . import mods_batch                       
    from . import mods_batch_atm                       
    from . import mods_bevel                       
    from . import mods_cut_auto                                              
    from . import mods_display                       
    from . import mods_mirror         
    from . import mods_mirror_auto                
    from . import mods_normals         
    from . import mods_pivot                   
    from . import mods_remove               
    from . import mods_sdeform               
    from . import mods_show               
    from . import mods_solidifiy               
    from . import mods_subsurf               
    from . import mods_toall               
    from . import mods_tools               



# LOAD MODULS #

import bpy
from bpy import*
from bpy.props import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup



# UI REGISTRY #

def update_panel_location(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Panel_UI)     
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_Modifier_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        
        bpy.utils.register_class(VIEW3D_TP_Modifier_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Modifier_Panel_UI)
  

    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass



def update_panel_location_stack(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Stack_Panel_UI)
       
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Stack_Panel_TOOLS)
   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Stack_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_stack == 'tools':
        
        VIEW3D_TP_Modifier_Stack_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_stack
        
        bpy.utils.register_class(VIEW3D_TP_Modifier_Stack_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_stack == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Modifier_Stack_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_stack == 'off':
        pass



# TOOL REGISTRY #

def update_display_tools(self, context):

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return 

    else:        
        if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
            pass
 


def update_tools_modifier(self, context):

    try:                
        bpy.types.DATA_PT_modifiers.remove(menu_func)                   

    except:
        pass
    
    try:
        bpy.types.DATA_PT_modifiers.remove(menu_func)

    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_tools_modifier == 'win':

        bpy.types.DATA_PT_modifiers.prepend(menu_func)

    if context.user_preferences.addons[__name__].preferences.tab_tools_modifier == 'off':
        pass



# MENU REGISTRY #

addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Modifier_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        VIEW3D_TP_Modifier_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Modifier_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS', shift=True) #,ctrl=True, alt=True, 
        kmi.properties.name = 'VIEW3D_TP_Modifier_Menu'

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

    #Tab Location           

    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location)

    tab_location_stack = EnumProperty(
        name = 'Panel Location',
        description = 'location switch',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_location_stack)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'location switch',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)


    # Tools  
    
    tab_tools_modifier = EnumProperty(
        name = 'Panel Location',
        description = 'tool switch',
        items=(('win', 'Properties: Modifier', 'enable tools in properties: modifier'),
               ('off', 'Off', 'disable tools in properties: modifier')),
               default='win', update = update_tools_modifier)



    # Shelf Panel
    tab_title = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Title on', 'enable tools in panel'), ('off', 'Title off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_pivot= EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Pivot on', 'enable tools in panel'), ('off', 'Pivot off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_display_tools = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Display Tools on', 'enable tools in panel'), ('off', 'Display Tools off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_automirror = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in panel'), ('off', 'AutoMirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_mirror_cut = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'MirrorCut on', 'enable tools in panel'), ('off', 'MirrorCut off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_mirror = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Mirror on', 'enable tools in panel'), ('off', 'Mirror off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_bevel = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Bevel on', 'enable tools in panel'), ('off', 'Bevel off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_subsurf = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Subsurf on', 'enable tools in panel'), ('off', 'Subsurf off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_solidify = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Solidify on', 'enable tools in panel'), ('off', 'Solidify off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_simple = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'SDeform on', 'enable tools in panel'), ('off', 'SDeform off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_array = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Array on', 'enable tools in panel'), ('off', 'Array off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_transform = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Transform on', 'enable tools in panel'), ('off', 'Transform off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_shade = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Shade on', 'enable tools in panel'), ('off', 'Shade off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_remove_type = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Remove Type on', 'enable tools in panel'), ('off', 'Remove Type off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_toall = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ToAll on', 'enable tools in panel'), ('off', 'ToAll off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_history = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'History on', 'enable tools in panel'), ('off', 'History off', 'disable tools in panel')), default='on', update = update_display_tools)


    # Modifier Properties
    tab_props_remove_type = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Remove Type on', 'enable tools in panel'), ('off', 'Remove Type off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_props_toall = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ToAll on', 'enable tools in panel'), ('off', 'ToAll off', 'disable tools in panel')), default='on', update = update_display_tools)

    tab_props_osd = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Display Tools on', 'enable tools in panel'), ('off', 'Display Tools off', 'disable tools in panel')), default='on', update = update_display_tools)


    # Menu
    tab_tp_menus = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Menus on', 'enable tools in menu'), ('off', 'Menus off', 'disable tools in menu')), default='on', update = update_display_tools)

    tab_tp_menus = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Menus on', 'enable tools in menu'), ('off', 'Menus off', 'disable tools in menu')), default='on', update = update_display_tools)

    tab_automirror_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'AutoMirror on', 'enable tools in menu'), ('off', 'AutoMirror off', 'disable tools in menu')), default='on', update = update_display_tools)

    tab_modstack_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ModifierStack on', 'enable tools in menu'), ('off', 'ModifierStack off', 'disable tools in menu')), default='on', update = update_display_tools)

    tab_clear_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'ClearTools on', 'enable tools in menu'), ('off', 'ClearTools off', 'disable tools in menu')), default='on', update = update_display_tools)

    tab_hover_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'HoverTools on', 'enable tools in menu'), ('off', 'HoverTools off', 'disable tools in menu')), default='on', update = update_display_tools)


    # Tab
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location)
    tools_category_stack = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_location_stack)
    tools_category_menu = bpy.props.BoolProperty(name = "Modifier Menu", description = "enable or disable menu", default=True, update = update_menu)


    # DRAW PREFERENCES #
    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            
            box = layout.box().column(1)
            
            row = box.column(1)   
            row.label(text="Welcome to T+ Modifier!")  
            row.label(text="This addon is for editing mesh objects with modifier.")
           
            row.separator()           
           
            row.label(text="The Panels are adaptable can be place in the toolshelf [T] or property shelf [N]")
            row.label(text="A included Menu have SHIFT+V﻿ as shortcut")
            row.label(text="Tools for Properties: 'Modifier' can also be activated")
           
            row.separator()        
         
            row.label("To use the Menu in editmode disable Vertex Slide!") 
            row.label("Pressing Transform Grab/Move (G) twice do the same job!") 
            row.label("go to TAB: Input > Key-Binding > Mesh > Vertex Slide > deactivate it") 

            row.separator()
                        
            row.label(text="Have Fun! :)")         


        #Tools
        if self.prefs_tabs == 'toolsets':
          
            box = layout.box().column(1)
            
            row = box.column(1)
            row.label(text="Panel Tools: 3D Viewport", icon ="INFO")

            box.separator() 
            
            row = box.column_flow(4)
            row.prop(self, 'tab_title', expand=True)
            row.prop(self, 'tab_pivot', expand=True)
            row.prop(self, 'tab_subsurf', expand=True)
            row.prop(self, 'tab_automirror', expand=True)
            row.prop(self, 'tab_mirror_cut', expand=True)
            row.prop(self, 'tab_mirror', expand=True)
            row.prop(self, 'tab_bevel', expand=True)
            row.prop(self, 'tab_solidify', expand=True)
            row.prop(self, 'tab_simple', expand=True)
            row.prop(self, 'tab_array', expand=True)
            row.prop(self, 'tab_transform', expand=True)
            row.prop(self, 'tab_shade', expand=True)
            row.prop(self, 'tab_remove_type', expand=True)
            row.prop(self, 'tab_toall', expand=True)
            row.prop(self, 'tab_history', expand=True)

            box.separator() 

            box = layout.box().column(1)
            
            row = box.column(1)
            row.label(text="Tools Properties: Modifier", icon ="INFO")

            box.separator() 
            
            row = box.column_flow(4)
            row.prop(self, 'tab_props_remove_type', expand=True)
            row.prop(self, 'tab_props_toall', expand=True)
            row.prop(self, 'tab_props_osd', expand=True)

            box.separator() 


            row = layout.row()
            row.label(text="! save user settings for a durably on or off !", icon ="INFO")

            box.separator() 
            

        #Location
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location 3D View: Main Panel")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
            
            box.separator()

            row = box.row(1)            
            if self.tab_location == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category")

            box.separator()

            row = box.row(1) 
            row.label("Location 3D View: Modifier Stack:")            
         
            row = box.row(1)             
            row.prop(self, 'tab_location_stack', expand=True)
          
            box.separator() 
        
            row = box.row(1)            
            if self.tab_location_stack == 'tools':
                
                box.separator() 
                
                row.prop(self, "tools_category_stack")

            box.separator()

            box = layout.box().column(1)             

            row = box.row(1) 
            row.label("Tools for Properties: Modifier")
            
            row = box.row(1)
            row.prop(self, 'tab_tools_modifier', expand=True)

            box.separator()

            row = layout.row()
            row.label(text="! save user settings for a durably new panel location !", icon ="INFO")

            box.separator() 


        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Modifier Menu:[SHIFT+V]", icon ="COLLAPSEMENU") 
       
            row.separator()                         

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next restart durably!", icon ="INFO")

            box.separator() 
            
            row = box.row(1) 
            row.label(text="! if needed change keys durably in TAB Input !", icon ="INFO")
            row.operator('wm.url_open', text = 'Tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"
          
            box.separator()


            box = layout.box().column(1)

            row = box.column_flow(3)
            row.prop(self, 'tab_tp_menus', expand=True)
            row.prop(self, 'tab_automirror_menu', expand=True)
            row.prop(self, 'tab_modstack_menu', expand=True)
            row.prop(self, 'tab_clear_menu', expand=True)
            row.prop(self, 'tab_hover_menu', expand=True)

            box.separator()
            
            row = layout.row()
            row.label(text="! save user settings for a durably on or off !", icon ="INFO")

            box.separator() 


        #Weblinks
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column_flow(2)
            row.operator('wm.url_open', text = 'AutoMirror', icon = 'HELP').url = "http://le-terrier-de-lapineige.over-blog.com/2014/07/automirror-mon-add-on-pour-symetriser-vos-objets-rapidement.html"
            row.operator('wm.url_open', text = 'Copy To All', icon = 'HELP').url = "https://www.artunchained.de/tiny-new-addon-to-all/"
            row.operator('wm.url_open', text = 'Display Tools', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Display_Tools"
            row.operator('wm.url_open', text = 'Modifier Tools', icon = 'HELP').url = "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/modifier_tools"
            row.operator('wm.url_open', text = 'BlenderArtist', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?411265-Addon-T-Modifier&p=3124733#post3124733"




# PROPERTY GROUP #
class Dropdown_TP_Modifier_Props(bpy.types.PropertyGroup):


    display_subsurf = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_automirror = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_mirror = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_bevel = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_solidify = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_sdeform = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_array = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=True)    
    display_apply = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    
    display_display = bpy.props.BoolProperty(name="Open / Close", description="Open / Close", default=False)    




#TAB MODIFIER IN PROPERTIES #

def menu_func(self, context):
    if (context.active_object):
        if (len(context.active_object.modifiers)):
            col = self.layout.column(1)

            display_toall = context.user_preferences.addons[__package__].preferences.tab_props_toall
            if display_toall == 'on':

                if context.mode == 'OBJECT':

                    row = col.row(1)
                    row.operator("scene.to_all", text="Copy to Childs", icon='LINKED').mode = "modifier, children" 
                    row.operator("scene.to_all", text="Copy to Selected", icon='FRAME_NEXT').mode = "modifier, selected"

            display_RemoveType = context.user_preferences.addons[__package__].preferences.tab_props_remove_type
            if display_RemoveType == 'on':

                row = col.row(1)
                row.prop(context.scene, "tp_mods_type", text="")
                row.operator("tp_ops.remove_mods_type", text="Remove Type", icon='ZOOMOUT')    


            display_osd = context.user_preferences.addons[__package__].preferences.tab_props_osd
            if display_osd == 'on':
              
                col.separator()
                
                row = col.row(1)
                
                obj = context.active_object
                if obj:               
                    if obj.draw_type == 'WIRE':
                        row.operator("tp_ops.draw_solid", text=" ", icon='GHOST_DISABLED')     
                    else:
                        row.operator("tp_ops.draw_wire", text=" ", icon='GHOST_ENABLED')        
                else:
                    row.label("", icon="BLANK1")  

                row.operator("tp_ops.wire_all", text=" ", icon='WIRE')

                obj = context.active_object
                if obj:
                    active_wire = obj.show_wire 
                    if active_wire == True:
                        row.operator("tp_ops.wire_off", " ", icon = 'MESH_PLANE')              
                    else:                       
                        row.operator("tp_ops.wire_on", " ", icon = 'MESH_GRID')
                else:
                    row.label("", icon="BLANK1")  
                
                row.prop(context.object, "show_bounds", text=" ", icon='STICKY_UVS_LOC') 


                if context.mode == 'EDIT_MESH':          

                    row.operator("mesh.faces_shade_flat", text=" ", icon="MESH_CIRCLE") 
                    row.operator("mesh.faces_shade_smooth", text=" ", icon="SMOOTH")  
                    row.operator("mesh.normals_make_consistent", text=" ", icon="SNAP_NORMAL")  
                
                if context.mode == 'OBJECT':             
      
                    row.operator("object.shade_flat", text=" ", icon="MESH_CIRCLE")
                    row.operator("object.shade_smooth", text=" ", icon="SMOOTH")  
                    row.operator("tp_ops.rec_normals", text=" ", icon="SNAP_NORMAL") 



            col.separator()
            
            row = col.row(1)
            row.operator("tp_ops.mods_render"," ", icon = 'RESTRICT_RENDER_OFF')                                                                       
            row.operator("object.toggle_apply_modifiers_view", text=" ", icon='RESTRICT_VIEW_OFF') 
            row.operator("tp_ops.mods_edit"," ", icon='EDITMODE_HLT')                                                    
            row.operator("tp_ops.mods_cage"," ", icon='OUTLINER_OB_MESH')                  
            row.operator("object.apply_all_modifiers", text=" ", icon='FILE_TICK') 
            row.operator("object.delete_all_modifiers", text=" ", icon='X')   
            row.operator("wm.toggle_all_show_expanded", text=" ", icon='FULLSCREEN_ENTER') 
      






# REGISTRY #

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.WindowManager.tp_collapse_menu_modifier = bpy.props.PointerProperty(type = Dropdown_TP_Modifier_Props)
       
    update_menu(None, bpy.context)
    update_panel_location(None, bpy.context)
    update_tools_modifier(None, bpy.context)
    update_panel_location_stack(None, bpy.context)



def unregister():

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    del bpy.types.WindowManager.tp_collapse_menu_modifier
    
if __name__ == "__main__":
    register()
        
        




              
