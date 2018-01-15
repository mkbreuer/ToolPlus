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
    "name": "Boolean",
    "author": "marvin.k.breuer (MKB)",
    "version": (1, 9, 0),
    "blender": (2, 7, 9),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] ",
    "description": "Collection of Boolean Tools",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "ToolPlus"}



# LOAD UI #
from toolplus_boolean.bool_gui_main         import (VIEW3D_TP_Edit_Boolean_Panel_TOOLS)
from toolplus_boolean.bool_gui_main         import (VIEW3D_TP_Edit_Boolean_Panel_UI)

from toolplus_boolean.bool_gui_btools       import (VIEW3D_TP_BoolTool_Brush_TOOLS)
from toolplus_boolean.bool_gui_btools       import (VIEW3D_TP_BoolTool_Brush_UI)

from toolplus_boolean.bool_gui_btprops      import (VIEW3D_TP_BoolTool_BViewer_TOOLS)
from toolplus_boolean.bool_gui_btprops      import (VIEW3D_TP_BoolTool_BViewer_UI)

#from toolplus_boolean.bool_gui_btprops      import (VIEW3D_TP_BoolTool_Config_TOOLS)
#from toolplus_boolean.bool_gui_btprops      import (VIEW3D_TP_BoolTool_Config_UI)

from toolplus_boolean.bool_menu             import (VIEW3D_TP_Boolean_Menu)

from toolplus_boolean.bool_multi            import (VIEW3D_TP_MultiBool_Panel_TOOLS)
from toolplus_boolean.bool_multi            import (VIEW3D_TP_MultiBool_Panel_UI)


# LOAD PROPS #
from toolplus_boolean.bool_carver         import (CarverPrefs)
from toolplus_boolean.bool_multi          import (VIEW3D_TP_Multi_Bool_Props)


# LOAD ICONS #
from . icons.icons   import load_icons
from . icons.icons   import clear_icons

##################################

# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_boolean'))

if "bpy" in locals():
    import imp
    imp.reload(bool_action)
    imp.reload(bool_autowire)
    imp.reload(bool_bevel)
    imp.reload(bool_boolean2d)
    imp.reload(bool_booltools3)
    imp.reload(bool_carver)
    imp.reload(bool_multi)
    imp.reload(bool_planefit)

else:
    from . import bool_action         
    from . import bool_autowire        
    from . import bool_bevel        
    from . import bool_boolean2d         
    from . import bool_booltools3                                   
    from . import bool_carver                                   
    from . import bool_multi                                   
    from . import bool_planefit                                   

    
# LOAD MODULS #   
import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup


# UI REGISTRY #
panels_main = (VIEW3D_TP_Edit_Boolean_Panel_UI, VIEW3D_TP_Edit_Boolean_Panel_TOOLS)

def update_panel_position(self, context):
    try:
        for panel in panels_main:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
  
        if context.user_preferences.addons[__name__].preferences.tab_location_main == 'tools':
         
            VIEW3D_TP_Edit_Boolean_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
            bpy.utils.register_class(VIEW3D_TP_Edit_Boolean_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_main == 'ui':
            bpy.utils.register_class(VIEW3D_TP_Edit_Boolean_Panel_UI)

        if context.user_preferences.addons[__name__].preferences.tab_location_main == 'off':  
            return None

    except:
        pass



panels_bt = (VIEW3D_TP_BoolTool_Brush_UI, VIEW3D_TP_BoolTool_Brush_TOOLS)

def update_panel_position_brush(self, context):

    try:
        for panel in panels_bt:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
   
        if context.user_preferences.addons[__name__].preferences.tab_location_brush == 'tools':
         
            VIEW3D_TP_BoolTool_Brush_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_brush
            bpy.utils.register_class(VIEW3D_TP_BoolTool_Brush_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_brush == 'ui':
            bpy.utils.register_class(VIEW3D_TP_BoolTool_Brush_UI)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_brush == 'off':
            return None

    except:
        pass



panels_vw = (VIEW3D_TP_BoolTool_BViewer_UI, VIEW3D_TP_BoolTool_BViewer_TOOLS)#, VIEW3D_TP_BoolTool_Config_UI, VIEW3D_TP_BoolTool_Config_TOOLS)

def update_panel_position_props(self, context):

    try:
        for panel in panels_vw:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        if context.user_preferences.addons[__name__].preferences.tab_location_props == 'tools':
         
            VIEW3D_TP_BoolTool_BViewer_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_props
            #VIEW3D_TP_BoolTool_Config_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_props
        
            bpy.utils.register_class(VIEW3D_TP_BoolTool_BViewer_TOOLS)
            #bpy.utils.register_class(VIEW3D_TP_BoolTool_Config_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_props == 'ui':
            bpy.utils.register_class(VIEW3D_TP_BoolTool_BViewer_UI)
            #bpy.utils.register_class(VIEW3D_TP_BoolTool_Config_UI)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_props == 'off':
            return None

    except:
        pass


panels_mb = (VIEW3D_TP_MultiBool_Panel_UI, VIEW3D_TP_MultiBool_Panel_TOOLS)
def update_panel_position_multi(self, context):
    try:
        for panel in panels_mb:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)
   
        if context.user_preferences.addons[__name__].preferences.tab_location_multi == 'tools':
         
            VIEW3D_TP_MultiBool_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_multi
            bpy.utils.register_class(VIEW3D_TP_MultiBool_Panel_TOOLS)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_multi == 'ui':
            bpy.utils.register_class(VIEW3D_TP_MultiBool_Panel_UI)
        
        if context.user_preferences.addons[__name__].preferences.tab_location_multi == 'off':
            return None

    except:
        pass

    
    
# TOOLS REGISTRY #
def update_tools(self, context):

    try:
        return True
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'on':
        return True

    if context.user_preferences.addons[__name__].preferences.tab_display_tools == 'off':
        return None    



# MENU REGISTRY #
addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Boolean_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        VIEW3D_TP_Boolean_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Boolean_Menu)
    
        # booltool: create the booleanhotkey in opjectmode
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'T', 'PRESS', shift=True) #ctrl=True, alt=True, 
        kmi.properties.name = 'VIEW3D_TP_Boolean_Menu'


    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        return None



# booltool: Fast Transformations
def UpdateBoolTool_Pref(self, context):
    if self.fast_transform:
        RegisterFastT()
    else:
        UnRegisterFastT()


# ADDON PREFERENCES #
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('toolset',    "Tools",      "Tools"),
               ('location',   "Location",   "Location"),
               ('keys',       "Keys",       "Keys"),
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location_main = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'enable or disable panel in the shelf')),
               default='tools', update = update_panel_position)

    tab_location_brush = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'enable or disable panel in the shelf')),
               default='off', update = update_panel_position_brush)

    tab_location_props = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'enable or disable panel in the shelf')),
               default='tools', update = update_panel_position_props)

    tab_location_multi = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'enable or disable panel in the shelf')),
               default='off', update = update_panel_position_multi)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)



    tab_bool_direct = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Direct Boolean on', 'enable tools'), ('off', 'Direct Boolean off', 'disable tools')), default='on', update = update_tools)

    tab_btbool_brush = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Brush Boolean on', 'enable tools'), ('off', 'Brush Boolean off', 'disable tools')), default='on', update = update_tools)

    tab_btbool_brush_simple = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'All Boolean Brushes on', 'enable tools'), ('off', 'All Boolean Brushes off', 'disable tools')), default='on', update = update_tools)

    tab_btbool_brush_simple_pl = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'All Boolean Brushes on', 'enable tools'), ('off', 'All Boolean Brushes off', 'disable tools')), default='on', update = update_tools)

    tab_btbool_props = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Brush Props on', 'enable tools'), ('off', 'Brush Props off', 'disable tools')), default='off', update = update_tools)

    tab_bool_intersect = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Edit Intersection on', 'enable tools'), ('off', 'Edit Intersection off', 'disable tools')), default='on', update = update_tools)

    tab_optimize = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Optimize on', 'enable tools'), ('off', 'Optimize off', 'disable tools')), default='off', update = update_tools)
 
    tab_direct_keys = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'HotKeys on', 'enable tools'), ('off', 'HotKeys off', 'disable tools')), default='on', update = update_tools)

    tab_brush_keys = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'HotKeys on', 'enable tools'), ('off', 'HotKeys off', 'disable tools')), default='on', update = update_tools)

    tab_to_menu = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Add to Add Menu', 'enable'), ('off', 'Remove from Add Menu', 'disable')), default='on', update = update_tools)



    tools_category_menu = bpy.props.BoolProperty(name = "Boolean Menu", description = "enable or disable menu", default=True, update = update_menu)
    
    tools_category_main  = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)
    tools_category_brush = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_brush)
    tools_category_props = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_props)
    tools_category_multi = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_multi)

    fast_transform     = bpy.props.BoolProperty(name="Fast Transformations", default=False, update=UpdateBoolTool_Pref, description="Replace the Transform HotKeys (G,R,S) for a custom version that can optimize the visualization of Brushes")
    make_vertex_groups = bpy.props.BoolProperty(name="Make Vertex Groups", default=False, description="When Apply a Brush to de Object it will create a new vertex group of the new faces" )
    make_boundary      = bpy.props.BoolProperty(name="Make Boundary", default=False, description="When Apply a Brush to de Object it will create a new vertex group of the bondary boolean area")
    use_wire           = bpy.props.BoolProperty(name="Use Bmesh", default=False, description="Use The Wireframe Instead Of Boolean")


    def draw(self, context):
        layout = self.layout
        icons = load_icons()   
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="Welcome to T+ Boolean!")

            row = layout.column()
            row.label(text="This is a collection of different boolean addons.")
            row.label(text="BoolTron / BoolTools / Bevel after Boolean / 2D Union / MultiBool")
            row.label(text="It allows you to boolean directly or with booltool brushes and bevel it after.")
            row.label(text="You can enabel and disable all Panel separatly or choose between toolshelf [T] or property shelf [N].")
            row.label(text="For a faster workflow reduced the tools in menu or panel or activate the NUMPAD HotKeys.")
            row.label(text="Need more Informations: please follow the links in the urls tab")
            row.label(text="And don't forget: Have Fun! ;)")

        #Tools
        if self.prefs_tabs == 'toolset':

            box = layout.box().column(1)

            row = box.row(1)
            row.label(text="Menu Axis Plane:")
            row.prop(self, 'tab_to_menu', expand=True)   

            box.separator() 
            box.separator() 

            box = layout.box().column(1)
           
            row = box.row(1)
            row.label(text="Menu Tools:")
            row.prop(self, 'tab_bool_direct', expand=True)

            box.separator()  
            box.separator()  

            row = box.row(1)
            row.label(text="")
            row.prop(self, 'tab_bool_intersect', expand=True)

            box.separator()  
            box.separator()  

            row = box.row(1)
            row.label(text="")
            row.prop(self, 'tab_btbool_brush', expand=True)

            box.separator()  
            box.separator()  

            row = box.row(1)
            row.label(text="")
            row.prop(self, 'tab_btbool_props', expand=True)
             
            box.separator()  
            box.separator()  

            box = layout.box().column(1)

            row = box.row(1)
            row.label(text="Panel & Menu Tools:")
            row.prop(self, 'tab_optimize', expand=True) 

            box.separator()    
            box.separator()    
                            
            box = layout.box().column(1)

            row = box.row(1)
            row.label(text="Menu Tools:")
            row.prop(self, 'tab_btbool_brush_simple', expand=True)   

            box.separator()  
            box.separator()  

            box = layout.box().column(1)

            row = box.row(1)            
            row.label(text="Panel Tools: Boolean BT")
            row.prop(self, 'tab_btbool_brush_simple_pl', expand=True)         

            box.separator()  
            box.separator()  
       
            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        #Location
        if self.prefs_tabs == 'location':
            
           
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location Direct Boolean: ")
            
            row= box.row(1)
            row.prop(self, 'tab_location_main', expand=True)
                                   
            if self.tab_location_main == 'tools':
                
                box.separator()
                
                row = box.row(1)                                                
                row.prop(self, "tools_category_main")

            box.separator()
            
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location Brush Boolean: ")
            
            row= box.row(1)
            row.prop(self, 'tab_location_brush', expand=True)
                       
            if self.tab_location_brush == 'tools':
                
                box.separator()
                
                row = box.row(1)                
                row.prop(self, "tools_category_brush")
                
            box.separator()
            

            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location Brush Properties: ")
            
            row= box.row(1)
            row.prop(self, 'tab_location_props', expand=True)
                       
            if self.tab_location_props == 'tools':
                
                box.separator()
                
                row = box.row(1)                
                row.prop(self, "tools_category_props")
                
            box.separator()                

           
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location MultiBool: ")
            
            row= box.row(1)
            row.prop(self, 'tab_location_multi', expand=True)
                       
            if self.tab_location_multi == 'tools':
                
                box.separator()
                
                row = box.row(1)                
                row.prop(self, "tools_category_multi")

            box.separator()


            box.separator() 
          
            row = layout.row()
            row.label(text="! save user settings for permant location change !", icon ="INFO")

            box.separator() 
            


        #Keys
        if self.prefs_tabs == 'keys':

            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("BoolMenu: [SHIFT+T]", icon ="COLLAPSEMENU")         
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':

                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator()

            box = layout.box().column(1)
             
            row = box.row(1)              
            row.label("Direct Boolean:", icon ="INFO") 
            row.prop(self, 'tab_direct_keys', expand=True)
                                   
            box.separator()
            box.separator()

            row = box.column_flow(2)              
            
            # column 1
            row.label("Objectmode:")
            
            button_boolean_union = icons.get("icon_boolean_union")            
            row.label("Direct_Union: [CTR+NUMPAD PLUS]", icon_value=button_boolean_union.icon_id)
            
            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.label("Intersect: [CTRL+NUMPAD ASTERIX]", icon_value=button_boolean_intersect.icon_id)

            button_boolean_difference = icons.get("icon_boolean_difference")
            row.label("Difference: [CTRL+NUMPAD MINUS]", icon_value=button_boolean_difference.icon_id)

            button_boolean_rebool = icons.get("icon_boolean_rebool")
            row.label("SliceRebool: [CTRL+NUMPAD_SLASH]", icon_value=button_boolean_rebool.icon_id)

            # column 2
            row.label("Editmode:")
     
            button_boolean_union = icons.get("icon_boolean_union")
            row.label("Union: [SHIFT+NUMPAD _PLUS]", icon_value=button_boolean_union.icon_id)
            
            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.label("Intersect: [SHIFT+NUMPAD_ASTERIX]", icon_value=button_boolean_intersect.icon_id)
            
            button_boolean_difference = icons.get("icon_boolean_difference")
            row.label("Difference: [SHIFT+NUMPAD_MINUS]", icon_value=button_boolean_difference.icon_id)
            
            button_boolean_rebool = icons.get("icon_boolean_rebool")
            row.label("SliceRebool: [SHIFT+NUMPAD_SLASH]", icon_value=button_boolean_rebool.icon_id)
       
            box.separator()


            box = layout.box().column(1)

            row = box.row(1)              
            row.label("Brush Boolean", icon ="INFO") 
            row.prop(self, 'tab_brush_keys', expand=True)
                                   
            box.separator()
            box.separator()

 
            # column 1
            row = box.column(1)               
            split = row.split(percentage=0.5)

            col = split.column()            
            button_boolean_union_brush = icons.get("icon_boolean_union_brush")
            col.label("BT-Union: [CTRL+SHIFT+NUMPAD PLUS]", icon_value=button_boolean_union_brush.icon_id)
            
            button_boolean_intersect_brush = icons.get("icon_boolean_intersect_brush")
            col.label("BT-Intersect: [CTRL+SHIFT+NUMPAD ASTERIX]", icon_value=button_boolean_intersect_brush.icon_id)
            
            button_boolean_difference_brush = icons.get("icon_boolean_difference_brush")
            col.label("BT-Difference: [CTRL+SHIFT+NUMPAD MINUS]", icon_value=button_boolean_difference_brush.icon_id)
            
            button_boolean_rebool_brush = icons.get("icon_boolean_rebool_brush")
            col.label("BT-SliceRebool: [CTRL+SHIFT+NUMPAD SLASH]", icon_value=button_boolean_rebool_brush.icon_id)
                      
            col.separator()

            col.label("Apply Brush: [CTRL+NUMPAD ENTER]", icon = 'MOD_LATTICE')
            col.label("Apply All: [CTRL+SHIFT+NUMPAD ENTER]", icon = 'MOD_LATTICE')

            
            # column 2
            split = split.split(percentage=0.5)
           
            col = split.column()              
            col.label("Experimental BoolTool Features:")
            
            col.separator()
                       
            col.prop(self, "fast_transform")
            col.prop(self, "use_wire", text="Use Wire instead Of BoundBox")
         
            box.separator()

            # TIP #
            box.separator()
            
            row = layout.row(1)             
            row.label(text="! For key change go to > User Preferences > TAB: Input !", icon ="INFO")

            row = layout.column(1) 
            row.label(text="1 > Change search to key-bindig and insert the hotkey, eg. bool menu: shift t !", icon ="BLANK1")
            row.label(text="2 > Under 3D View you find the call menu, name: VIEW3D_TP_Boolean_Menu !", icon ="BLANK1")
            row.label(text="3 > Choose a new key configuration and save user settings !", icon ="BLANK1")

            row.separator() 
            
            row.label(text="(4) > Use the 'is key free' addon under User Interface to finde a free shortcut !", icon ="BLANK1")
        
            box.separator()  



        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.column_flow(2)
       
            # column 1
            row.operator('wm.url_open', text = 'Booltron', icon = 'INFO').url = "https://github.com/mrachinskiy/blender-addon-booltron"
            row.operator('wm.url_open', text = 'BoolTools', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/BoolTool"
            row.operator('wm.url_open', text = 'PlaneFit', icon = 'INFO').url = "http://blog.michelanders.nl/2017/12/planefit-blender-add-on-to-fit-plane.html"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?410098-Addon-T-Boolean&p=3118012#post3118012"

            # column 2
            row.operator('wm.url_open', text = '2D Union', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?338703-Addon-Boolean-2D-Union"
            row.operator('wm.url_open', text = 'Bevel after Boolean', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?434699-Bevel-after-Boolean"
            row.operator('wm.url_open', text = 'Multi Machine', icon = 'INFO').url = "https://blenderartists.org/forum/showthread.php?442162-AddOn-MultiMachine-repeat-a-pattern-of-boolena-diff-or-unions"
            row.operator('wm.url_open', text = 'GitHub', icon = 'RECOVER_LAST').url = "https://github.com/mkbreuer/ToolPlus"



class Display_Tools_Props(bpy.types.PropertyGroup):

    WT_handler_enable = BoolProperty(default=False)
    WT_handler_previous_object = StringProperty(default="")


# BOOLTOOL: Hide boolean objects #
def update_BoolHide(self, context):
    ao = context.scene.objects.active
    objs = [i.object for i in ao.modifiers if i.type == 'BOOLEAN']
    hide_state = context.scene.BoolHide

    for o in objs:
        o.hide = hide_state


        
# REGISTRY KEYMAPS #
addon_keymaps = []
addon_keymapsFastT = []

# BOOLTOOL: Fast Transform HotKeys Register #
def RegisterFastT():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

    kmi = km.keymap_items.new("btool.fast_transform", 'G', 'PRESS')
    kmi.properties.operator = "Translate"
    addon_keymapsFastT.append((km, kmi))

    kmi = km.keymap_items.new("btool.fast_transform", 'R', 'PRESS')
    kmi.properties.operator = "Rotate"
    addon_keymapsFastT.append((km, kmi))

    kmi = km.keymap_items.new("btool.fast_transform", 'S', 'PRESS')
    kmi.properties.operator = "Scale"
    addon_keymapsFastT.append((km, kmi))


# BOOLTOOL: Fast Transform HotKeys UnRegister #
def UnRegisterFastT():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

    for km, kmi in addon_keymapsFastT:
        km.keymap_items.remove(kmi)
    addon_keymapsFastT.clear()


def menu_func(self, context):       

    icons = load_icons()
    
    display_menu = context.user_preferences.addons[__package__].preferences.tab_to_menu
    if display_menu == 'on':  

        if context.mode == 'EDIT_MESH':
            
            button_axis_xyz_planes = icons.get("icon_axis_xyz_planes")
            self.layout.menu("tp_menu.intersetion_planes", text ="Planes", icon_value=button_axis_xyz_planes.icon_id)   

            self.layout.separator()


# RIGHT CLICK BUTTON TO ONLINE MANUAL
def add_default_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/dev/modeling"
    url_manual_mapping = (
        ("bpy.ops.tp_ops.bool_union"        , "/modifiers/generate/booleans.html"),
        ("bpy.ops.tp_ops.bool_intersect"    , "/modifiers/generate/booleans.html"),
        ("bpy.ops.tp_ops.bool_difference"   , "/modifiers/generate/booleans.html"),
        ("bpy.ops.mesh.intersect"           , "/meshes/editing/faces.html"),
        ("bpy.ops.mesh.intersect"           , "/meshes/editing/faces.html"),
        )
    return url_manual_prefix, url_manual_mapping

def add_bt_manual_map():
    url_manual_prefix = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts"
    url_manual_mapping = (
        ("bpy.ops.tp_ops.tboolean_union"    , "/Object/BoolTool"),
        ("bpy.ops.tp_ops.tboolean_inters"   , "/Object/BoolTool"),
        ("bpy.ops.tp_ops.tboolean_diff"     , "/Object/BoolTool"),
        ("bpy.ops.tp_ops.tboolean_slice"    , "/Object/BoolTool"),
        ("bpy.ops.tp_ops.draw_polybrush"    , "/Object/BoolTool"),
        
        ("bpy.ops.btool.direct_union"       , "/Object/BoolTool"),
        ("bpy.ops.btool.direct_intersect"   , "/Object/BoolTool"),
        ("bpy.ops.btool.direct_difference"  , "/Object/BoolTool"),
        ("bpy.ops.btool.direct_subtract"    , "/Object/BoolTool"),
        ("bpy.ops.btool.direct_slice"       , "/Object/BoolTool"),
        )
    return url_manual_prefix, url_manual_mapping


# REGISTRY #
import traceback

def register():

    # carver
    bpy.types.Scene.DepthCursor = bpy.props.BoolProperty(name="DepthCursor", default=False)
    bpy.types.Scene.OInstanciate = bpy.props.BoolProperty(name="Obj_Instantiate", default=False)
    bpy.types.Scene.ORandom = bpy.props.BoolProperty(name="Random_Rotation", default=False)
    bpy.types.Scene.DontApply = bpy.props.BoolProperty(name="Dont_Apply", default=False)
    bpy.types.Scene.nProfile = bpy.props.IntProperty(name="Num_Profile", default=0)

    # booltool: Scene variables
    bpy.types.Scene.BoolHide = bpy.props.BoolProperty(default=False, description='Hide boolean objects', update=update_BoolHide)
       
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    bpy.types.INFO_MT_mesh_add.prepend(menu_func)
    bpy.utils.register_manual_map(add_default_manual_map)
    bpy.utils.register_manual_map(add_bt_manual_map)

    # PROPS #  
    bpy.types.Scene.display_props = bpy.props.PointerProperty(type=Display_Tools_Props)
 
    # multibool  
    bpy.types.WindowManager.tp_props_multibool = bpy.props.PointerProperty(type = VIEW3D_TP_Multi_Bool_Props)

       
    # direct bool: create the hotkey for objectmode and editmode
    bool_direct_keys = context.user_preferences.addons[__name__].preferences.tab_direct_keys
    if bool_direct_keys == 'on':

        wm = bpy.context.window_manager

        # objectmode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new("btool.direct_union", 'NUMPAD_PLUS', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.direct_difference", 'NUMPAD_MINUS', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.direct_intersect", 'NUMPAD_ASTERIX', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.direct_slice", 'NUMPAD_SLASH', 'PRESS', ctrl=True)
               
        # editmode
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new("tp_ops.bool_union", 'NUMPAD_PLUS', 'PRESS', shift=True)
        kmi = km.keymap_items.new("tp_ops.bool_difference", 'NUMPAD_MINUS', 'PRESS', shift=True)
        kmi = km.keymap_items.new("tp_ops.bool_intersect", 'NUMPAD_ASTERIX', 'PRESS', shift=True)
        kmi = km.keymap_items.new("bpt.boolean_2d_union", 'NUMPAD_SLASH', 'PRESS', shift=True)


    # brush bool: create the hotkey for objectmode
    bool_brush_keys = context.user_preferences.addons[__name__].preferences.tab_brush_keys
    if bool_brush_keys == 'on':

        wm = bpy.context.window_manager

        # objectmode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')        
        kmi = km.keymap_items.new("btool.boolean_union", 'NUMPAD_PLUS', 'PRESS', ctrl=True, shift=True)
        kmi = km.keymap_items.new("btool.boolean_diff", 'NUMPAD_MINUS', 'PRESS', ctrl=True, shift=True)
        kmi = km.keymap_items.new("btool.boolean_inters", 'NUMPAD_ASTERIX', 'PRESS', ctrl=True, shift=True)
        kmi = km.keymap_items.new("btool.boolean_slice", 'NUMPAD_SLASH', 'PRESS', ctrl=True, shift=True)

        kmi = km.keymap_items.new("btool.brush_to_mesh", 'NUMPAD_ENTER', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new("btool.to_mesh", 'NUMPAD_ENTER', 'PRESS', ctrl=True, shift=True)


    addon_keymaps.append(km)

    update_tools(None, bpy.context)
    update_menu(None, bpy.context)
    update_panel_position(None, bpy.context)
    update_panel_position_brush(None, bpy.context)
    update_panel_position_props(None, bpy.context)
    update_panel_position_multi(None, bpy.context)



def unregister():

    bpy.types.INFO_MT_mesh_add.remove(menu_func)
    bpy.utils.unregister_manual_map(add_default_manual_map)
    bpy.utils.unregister_manual_map(add_bt_manual_map)
 
    # PROPS #  
    del bpy.types.Scene.display_props 

    # carver
    del bpy.types.Scene.DepthCursor
    del bpy.types.Scene.OInstanciate
    del bpy.types.Scene.ORandom
    del bpy.types.Scene.DontApply
    del bpy.types.Scene.nProfile

    # booltool
    del bpy.types.Scene.BoolHide

    # multibool  
    del bpy.types.WindowManager.tp_props_multibool

    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    # Keymapping
    # remove keymaps when add-on is deactivated
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    del addon_keymaps[:]



if __name__ == "__main__":
    register()
        
        








