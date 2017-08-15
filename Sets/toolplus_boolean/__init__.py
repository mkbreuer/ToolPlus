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
    "name": "T+ Boolean",
    "author": "Multi Authors (see URL), MKB",
    "version": (0, 1, 4),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] ",
    "description": "Panel and Menu for Boolean Operator",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


from toolplus_boolean.bool_booltools3    import (BoolTool_Brush_TOOLS)
from toolplus_boolean.bool_booltools3    import (BoolTool_Brush_UI)

from toolplus_boolean.bool_booltools3    import (BoolTool_BViwer_TOOLS)
from toolplus_boolean.bool_booltools3    import (BoolTool_BViwer_UI)

from toolplus_boolean.bool_booltools3    import (BoolTool_Config_TOOLS)
from toolplus_boolean.bool_booltools3    import (BoolTool_Config_UI)

from toolplus_boolean.bool_carver         import (CarverPrefs)

from . icons.icons                  import load_icons
from . icons.icons                  import clear_icons

##################################

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_boolean'))

if "bpy" in locals():
    import imp
    imp.reload(bool_action)
    imp.reload(bool_boolean2d)
    imp.reload(bool_booltools3)
    imp.reload(bool_carver)

else:
    from . import bool_action         
    from . import bool_boolean2d         
    from . import bool_booltools3                                   
    from . import bool_carver                                   

    
    
import bpy
from bpy import*

import bpy.utils.previews
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import* #(StringProperty, BoolProperty, FloatVectorProperty, FloatProperty, EnumProperty, IntProperty)

def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Edit_Boolean_Panel_UI)
        
        bpy.utils.unregister_class(VIEW3D_TP_Edit_Boolean_Panel_TOOLS)
        
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Edit_Boolean_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
     
        VIEW3D_TP_Edit_Boolean_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
    
        bpy.utils.register_class(VIEW3D_TP_Edit_Boolean_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Edit_Boolean_Panel_UI)
  


def update_panel_position_brush(self, context):
    try:
        bpy.utils.unregister_class(BoolTool_Brush_UI)
        bpy.utils.unregister_class(BoolTool_BViwer_UI)
        bpy.utils.unregister_class(BoolTool_Config_UI)
        
        bpy.utils.unregister_class(BoolTool_Brush_TOOLS)
        bpy.utils.unregister_class(BoolTool_BViwer_TOOLS)
        bpy.utils.unregister_class(BoolTool_Config_TOOLS)        
    except:
        pass
    
    try:
        bpy.utils.unregister_class(BoolTool_Brush_UI)
        bpy.utils.unregister_class(BoolTool_BViwer_UI)
        bpy.utils.unregister_class(BoolTool_Config_UI)
    except:
        pass
    
    try:
        pass
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_location_brush == 'tools':
     
        BoolTool_Brush_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_brush
        BoolTool_BViwer_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_brush
        BoolTool_Config_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_brush
    
        bpy.utils.register_class(BoolTool_Brush_UI)
        bpy.utils.register_class(BoolTool_BViwer_TOOLS)
        bpy.utils.register_class(BoolTool_Config_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_brush == 'ui':
        bpy.utils.register_class(BoolTool_Brush_UI)
        bpy.utils.register_class(BoolTool_BViwer_UI)
        bpy.utils.register_class(BoolTool_Config_UI)
    
    if context.user_preferences.addons[__name__].preferences.tab_location_brush == 'off':
        pass




def update_tools(self, context):
   
    if context.user_preferences.addons[__name__].preferences.tab_optimize == 'on':
        return
    
    if context.user_preferences.addons[__name__].preferences.tab_optimize == 'off':
        pass 





addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(BoolTool_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        BoolTool_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(BoolTool_Menu)
    
        # booltool: create the booleanhotkey in opjectmode
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

        kmi = km.keymap_items.new('wm.call_menu', 'T', 'PRESS', shift=True) #ctrl=True, alt=True, 
        kmi.properties.name = 'OBJECT_MT_BoolTool_Menu'


    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass



# booltool: Fast Transformations
def UpdateBoolTool_Pref(self, context):
    if self.fast_transform:
        RegisterFastT()
    else:
        UnRegisterFastT()


#Panel preferences
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
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position)

    tab_location_brush = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'enable or disable panel in the shelf')),
               default='off', update = update_panel_position_brush)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)


    tab_optimize = EnumProperty(name = 'Display Tools', description = 'on / off',
                  items=(('on', 'Optimize on', 'enable optimize tools'), ('off', 'Optimize off', 'disable optimize tools')), default='off', update = update_tools)
 

    tools_category_menu = bpy.props.BoolProperty(name = "Boolean Menu", description = "enable or disable menu", default=True, update = update_menu)
    
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)
    tools_category_brush = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position_brush)

    fast_transform = bpy.props.BoolProperty(name="Fast Transformations", default=False, update=UpdateBoolTool_Pref, description="Replace the Transform HotKeys (G,R,S) for a custom version that can optimize the visualization of Brushes")
    make_vertex_groups = bpy.props.BoolProperty(name="Make Vertex Groups", default=False, description="When Apply a Brush to de Object it will create a new vertex group of the new faces" )
    make_boundary = bpy.props.BoolProperty(name="Make Boundary", default=False, description="When Apply a Brush to de Object it will create a new vertex group of the bondary boolean area")
    use_wire = bpy.props.BoolProperty(name="Use Bmesh", default=False, description="Use The Wireframe Instead Of Boolean")


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            row = layout.row()
            row.label(text="Welcome to the T+ Boolean Collection!")

            row = layout.column()
            row.label(text="This is a coolection of  different boolean operators.")
            row.label(text="It allows you to boolean more directly.")
            row.label(text="You have the abiltiy to enabel or disable the Panel or the Menu and with HotKey.")
            row.label(text="You can also choose between toolshelf [T] or property shelf [N] for the Panel.")
            row.label(text="Have Fun! ;)")

        #Tools
        if self.prefs_tabs == 'toolset':

            box = layout.box().column(1)

            row = box.row()
            row.prop(self, 'tab_optimize', expand=True)

            row = layout.row()
            row.label(text="! save user settings for permant on/off !", icon ="INFO")

            box.separator() 


        #Location
        if self.prefs_tabs == 'location':
            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location Direct Boolean: ")
            
            row= box.row(1)
            row.prop(self, 'tab_location', expand=True)
                                   
            if self.tab_location == 'tools':
                
                row = box.row(1)                                                
                row.prop(self, "tools_category")

            box = layout.box().column(1)
             
            row = box.row(1)  
            row.label("Location Brush Boolean: ")
            
            row= box.row(1)
            row.prop(self, 'tab_location_brush', expand=True)
                       
            if self.tab_location_brush == 'tools':
                
                row = box.row(1)                
                row.prop(self, "tools_category_brush")
                
            if self.tab_location_brush == 'off':                

                row = box.row()
                row.label(text="! keys hidden with next reboot !", icon ="INFO")

            row = layout.row()
            row.label(text="! please reboot blender after changing the panel location !", icon ="INFO")


        #Keys
        if self.prefs_tabs == 'keys':
            box = layout.box().column(1)
             
            row = box.column(1)  
            
            row.label("Experimental Features:")
            
            row.separator()
                       
            row.prop(self, "fast_transform")
            row.prop(self, "use_wire", text="Use Wire Instead Of Bbox")

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Boolean Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: 'T', 'PRESS', shift=True")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':

                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box = layout.box().column(1)
             
            row = box.column(1)              
            row.label("Direct Operators:", icon ="MOD_WIREFRAME")
            
            row.separator()
            
            row.label("Direct_Union: 'NUMPAD_PLUS', 'PRESS', ctrl=True")
            row.label("Direct_Difference: 'NUMPAD_MINUS', 'PRESS', ctrl=True")
            row.label("Direct_Intersect: 'NUMPAD_ASTERIX', 'PRESS', ctrl=True")
            row.label("Direct_Slice: 'NUMPAD_SLASH', 'PRESS', ctrl=True")
            
            row.separator()
            
            row.label("Editmode:")
            row.separator()

            row.label("Direct_Union: 'NUMPAD_PLUS', 'PRESS', shift=True")
            row.label("Direct_Difference: 'NUMPAD_MINUS', 'PRESS', shift=True")
            row.label("Direct_Intersect: 'NUMPAD_ASTERIX', 'PRESS', shift=True")
            row.label("Direct_Slice: 'NUMPAD_SLASH', 'PRESS', shift=True")

            box = layout.box().column(1)
             
            row = box.column(1)              
            row.label("Brush Operators:", icon ="MOD_MESHDEFORM")
                                   
            row.separator()
            
            row.label("Union: 'NUMPAD_PLUS', 'PRESS', ctrl=True, shift=True")
            row.label("Diff: 'NUMPAD_MINUS', 'PRESS', ctrl=True, shift=True")
            row.label("Intersect: 'NUMPAD_ASTERIX', 'PRESS', ctrl=True, shift=True")
            row.label("Slice Rebool: 'NUMPAD_SLASH', 'PRESS', ctrl=True, shift=True")
          
            row.separator()
            
            row.label("BTool_BrushToMesh: 'NUMPAD_ENTER', 'PRESS', ctrl=True")
            row.label("BTool_AllBrushToMesh: 'NUMPAD_ENTER', 'PRESS', ctrl=True, shift=True")


        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.row()
            row.operator('wm.url_open', text = 'Booltron', icon = 'HELP').url = "https://github.com/mrachinskiy/blender-addon-booltron"
            row.operator('wm.url_open', text = 'BoolTools', icon = 'HELP').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/BoolTool"
            row.operator('wm.url_open', text = 'Boolean 2D Union', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?338703-Addon-Boolean-2D-Union"
            row.operator('wm.url_open', text = 'Carver', icon = 'HELP').url = "https://blenderartists.org/forum/showthread.php?400038-Carver"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?410098-Addon-T-Boolean&p=3118012#post3118012"




def draw_boolean_panel_layout(self, context, layout):

        icons = load_icons()

        if context.mode == "OBJECT":

            box = layout.box().column(1)                                                   

            row = box.column(1) 
            
            button_boolean_union = icons.get("icon_boolean_union")
            row.operator("btool.direct_union", text="Union", icon_value=button_boolean_union.icon_id)

            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.operator("btool.direct_intersect", text="Intersect", icon_value=button_boolean_intersect.icon_id)

            button_boolean_difference = icons.get("icon_boolean_difference")
            row.operator("btool.direct_difference", text="Difference", icon_value=button_boolean_difference.icon_id)
                        
            row.separator()  

            button_boolean_substract = icons.get("icon_boolean_substract")
            row.operator("btool.direct_subtract", icon_value=button_boolean_substract.icon_id)              

            button_boolean_rebool = icons.get("icon_boolean_rebool")
            row.operator("btool.direct_slice", "Slice Rebool", icon_value=button_boolean_rebool.icon_id)        

            Display_Optimize = context.user_preferences.addons[__name__].preferences.tab_optimize
            if Display_Optimize == 'on':  

                box.separator()         

                box = layout.box().column(1)   

                row = box.column(1) 
                
                button_origin_obm = icons.get("icon_origin_obm")
                row.operator("object.origin_set", "Set Origin", icon_value=button_origin_obm.icon_id).type='ORIGIN_GEOMETRY'
            
            box.separator()         

            box = layout.box().column(1)               

            row = box.column(1)   

            button_boolean_carver = icons.get("icon_boolean_carver")
            row.operator("object.carver", text="3d Carver", icon_value=button_boolean_carver.icon_id)

            ###
            box.separator()         
  


        if context.mode == "EDIT_MESH":


            box = layout.box().column(1)                     

            row = box.column(1)                        

            button_boolean_union = icons.get("icon_boolean_union")
            row.operator("tp_ops.bool_union", text="Union", icon_value=button_boolean_union.icon_id) 

            button_boolean_intersect = icons.get("icon_boolean_intersect")
            row.operator("tp_ops.bool_intersect",text="Intersect", icon_value=button_boolean_intersect.icon_id) 

            button_boolean_difference = icons.get("icon_boolean_difference")
            row.operator("tp_ops.bool_difference",text="Difference", icon_value=button_boolean_difference.icon_id)  

            box.separator()  

            box = layout.box().column(1)                     

            row = box.column(1)  

            button_boolean_weld = icons.get("icon_boolean_weld")
            row.operator("mesh.intersect", "Weld", icon_value=button_boolean_weld.icon_id).use_separate = False

            button_boolean_isolate = icons.get("icon_boolean_isolate")
            row.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).use_separate = True   
            
            box.separator()          
            
            row = box.row(1)           
            row.label("Planes")         

            button_axis_x = icons.get("icon_axis_x")
            row.operator("tp_ops.plane_x",text="", icon_value=button_axis_x.icon_id)      
          
            button_axis_y = icons.get("icon_axis_y")
            row.operator("tp_ops.plane_y",text="", icon_value=button_axis_y.icon_id)       

            button_axis_z = icons.get("icon_axis_z")
            row.operator("tp_ops.plane_z",text="", icon_value=button_axis_z.icon_id) 

            box.separator() 

            box = layout.box().column(1)                     

            row = box.row(1) 
            
            button_boolean_facemerge = icons.get("icon_boolean_facemerge")
            row.operator("bpt.boolean_2d_union", text= "2d Union", icon_value=button_boolean_facemerge.icon_id)        

            ###
            box.separator() 


            Display_Optimize = context.user_preferences.addons[__name__].preferences.tab_optimize
            if Display_Optimize == 'on':   

                box = layout.box().column(1)                          

                row = box.column(1)  
                
                button_select_link = icons.get("icon_select_link")
                row.operator("mesh.select_linked",text="Select Linked", icon_value=button_select_link.icon_id)

                button_remove_double = icons.get("icon_remove_double")
                row.operator("mesh.remove_doubles",text="Remove Doubles", icon_value=button_remove_double.icon_id)             

                row.operator("mesh.normals_make_consistent", text="Recalc. Normals", icon="SNAP_NORMAL")

                row.separator() 

                button_origin_edm = icons.get("icon_origin_edm")
                row.operator("tp_ops.origin_edm",text="Set Origin", icon_value=button_origin_edm.icon_id)

                ###                   
                box.separator()




class VIEW3D_TP_Edit_Boolean_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Edit_Boolean_Panel_TOOLS"
    bl_label = "Boolean"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_boolean_panel_layout(self, context, layout) 
        
                

class VIEW3D_TP_Edit_Boolean_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Edit_Boolean_Panel_UI"
    bl_label = "Boolean"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_boolean_panel_layout(self, context, layout) 


# Hide boolean objects
def update_BoolHide(self, context):
    ao = context.scene.objects.active
    objs = [i.object for i in ao.modifiers if i.type == 'BOOLEAN']
    hide_state = context.scene.BoolHide

    for o in objs:
        o.hide = hide_state

# Object is a Canvas
def isCanvas(_obj):
    try:
        if _obj["BoolToolRoot"]:
            return True
    except:
        return False


# Object is a Brush Tool Bool
def isBrush(_obj):
    try:
        if _obj["BoolToolBrush"]:
            return True
    except:
        return False

# 3Dview Header Menu
class BoolTool_Menu(bpy.types.Menu):
    bl_label = "Boolean :)"
    bl_idname = "OBJECT_MT_BoolTool_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        icons = load_icons()
        
        if context.mode == 'OBJECT':

            button_boolean_union = icons.get("icon_boolean_union")
            layout.operator("tp_ops.bool_union_obm_menu", text="Union", icon_value=button_boolean_union.icon_id)

            button_boolean_intersect = icons.get("icon_boolean_intersect")
            layout.operator("tp_ops.bool_intersect_obm_menu", text="Intersect", icon_value=button_boolean_intersect.icon_id)

            button_boolean_difference = icons.get("icon_boolean_difference")
            layout.operator("tp_ops.bool_difference_obm_menu", text="Difference", icon_value=button_boolean_difference.icon_id)
                        
            layout.separator() 

            button_boolean_substract = icons.get("icon_boolean_substract")
            layout.operator("btool.direct_subtract", icon_value=button_boolean_substract.icon_id)              

            button_boolean_rebool = icons.get("icon_boolean_rebool")
            layout.operator("tp_ops.bool_rebool_obm_menu", "Slice Rebool", icon_value=button_boolean_rebool.icon_id)

            layout.separator() 

            button_boolean_carver = icons.get("icon_boolean_carver")
            layout.operator("object.carver", text="3d Carver", icon_value=button_boolean_carver.icon_id)

            Display_Optimize = context.user_preferences.addons[__name__].preferences.tab_optimize
            if Display_Optimize == 'on':  

                layout.separator()
                
                button_origin_obm = icons.get("icon_origin_obm")
                layout.operator("tp_ops.origin_obm", "", icon_value=button_origin_obm.icon_id)


            active_brush = context.user_preferences.addons[__name__].preferences.tab_location_brush 
            if active_brush == 'tools' or active_brush == 'ui':

                layout.separator()

                layout.operator("btool.boolean_union", icon="ROTATECOLLECTION")
                layout.operator("btool.boolean_diff", icon="ROTACTIVE")
                layout.operator("btool.boolean_inters", icon="ROTATECENTER")
            
                layout.separator()

                layout.operator("btool.boolean_slice", text="Brush Slice Rebool", icon="ROTATECENTER")

                layout.separator()
                layout.operator_context = 'INVOKE_REGION_WIN'
                #layout.operator_context = 'EXEC_REGION_WIN'
                layout.operator("btool.draw_polybrush", icon="LINE_DATA")

                if (isCanvas(context.active_object)):
                    layout.separator()
                    layout.operator("btool.to_mesh", icon="MOD_LATTICE", text="Apply All")
                    Rem = layout.operator("btool.remove", icon="CANCEL", text="Remove All")
                    Rem.thisObj = ""
                    Rem.Prop = "CANVAS"

                if (isBrush(context.active_object)):
                    layout.separator()
                    layout.operator("btool.brush_to_mesh", icon="MOD_LATTICE", text="Apply Brush")
                    Rem = layout.operator("btool.remove", icon="CANCEL", text="Remove Brush")
                    Rem.thisObj = ""
                    Rem.Prop = "BRUSH"

            else:
                pass



        if context.mode == 'EDIT_MESH':
                      
            button_boolean_union = icons.get("icon_boolean_union")
            layout.operator("tp_ops.bool_union_edm_menu", text="Union", icon_value=button_boolean_union.icon_id) 

            button_boolean_intersect = icons.get("icon_boolean_intersect")
            layout.operator("tp_ops.bool_intersect_edm_menu",text="Intersect", icon_value=button_boolean_intersect.icon_id) 

            button_boolean_difference = icons.get("icon_boolean_difference")
            layout.operator("tp_ops.bool_difference_edm_menu",text="Difference", icon_value=button_boolean_difference.icon_id)  

            layout.separator()  

            button_boolean_weld = icons.get("icon_boolean_weld")
            layout.operator("mesh.intersect", "Weld", icon_value=button_boolean_weld.icon_id).use_separate = False

            button_boolean_isolate = icons.get("icon_boolean_isolate")
            layout.operator("mesh.intersect", "Isolate", icon_value=button_boolean_isolate.icon_id).use_separate = True   
            
            button_axis_xyz_planes = icons.get("icon_axis_xyz_planes")
            layout.menu("tp_menu.intersetion_planes", text ="Planes", icon_value=button_axis_xyz_planes.icon_id)      

            layout.separator()          
           
            button_boolean_facemerge = icons.get("icon_boolean_facemerge")
            layout.operator("tp_ops.boolean_2d_union_edm_menu", text= "2d Union", icon_value=button_boolean_facemerge.icon_id)      


            Display_Optimize = context.user_preferences.addons[__name__].preferences.tab_optimize
            if Display_Optimize == 'on':  

                layout.separator()
                                    
                button_select_link = icons.get("icon_select_link")
                layout.operator("tp_ops.select_linked_edm",text="Select Linked", icon_value=button_select_link.icon_id)

                button_remove_double = icons.get("icon_remove_double")
                layout.operator("mesh.remove_doubles",text="Remove Doubles", icon_value=button_remove_double.icon_id)             

                layout.operator("mesh.normals_make_consistent", text="Recalc. Normals", icon="SNAP_NORMAL")

                layout.separator()          

                button_origin_edm = icons.get("icon_origin_edm")
                layout.operator("tp_ops.origin_edm",text="Set Origin", icon_value=button_origin_edm.icon_id)



        
# register Keymaps
addon_keymaps = []
addon_keymapsFastT = []

# booltool: Fast Transform HotKeys Register
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


# booltool: Fast Transform HotKeys UnRegister
def UnRegisterFastT():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

    for km, kmi in addon_keymapsFastT:
        km.keymap_items.remove(kmi)
    addon_keymapsFastT.clear()


# register

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
    
    # booltool: Handlers
    #bpy.app.handlers.scene_update_post.append(HandleScene)

    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    # booltool: create the booleanhotkey in opjectmode
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')

    # booltool: Direct Operators
    kmi = km.keymap_items.new("btool.direct_union", 'NUMPAD_PLUS', 'PRESS', ctrl=True)
    kmi = km.keymap_items.new("btool.direct_difference", 'NUMPAD_MINUS', 'PRESS', ctrl=True)
    kmi = km.keymap_items.new("btool.direct_intersect", 'NUMPAD_ASTERIX', 'PRESS', ctrl=True)
    kmi = km.keymap_items.new("btool.direct_slice", 'NUMPAD_SLASH', 'PRESS', ctrl=True)
    
    
    # edit: create the boolean menu hotkey in editmode
    km = wm.keyconfigs.addon.keymaps.new(name='Mesh')

    # edit: Direct Operators
    kmi = km.keymap_items.new("tp_ops.bool_union", 'NUMPAD_PLUS', 'PRESS', shift=True)
    kmi = km.keymap_items.new("tp_ops.bool_difference", 'NUMPAD_MINUS', 'PRESS', shift=True)
    kmi = km.keymap_items.new("tp_ops.bool_intersect", 'NUMPAD_ASTERIX', 'PRESS', shift=True)
    kmi = km.keymap_items.new("bpt.boolean_2d_union", 'NUMPAD_SLASH', 'PRESS', shift=True)


    #km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')

    #kmi = km.keymap_items.new('wm.call_menu', 'T', 'PRESS', shift=True) #ctrl=True, alt=True, 
    #kmi.properties.name = 'OBJECT_MT_BoolTool_Menu'


    active_brush = context.user_preferences.addons[__name__].preferences.tab_location_brush 
    if active_brush == 'tools' or active_brush == 'ui':

        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')

        # booltool: Brush Operators
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



def unregister():

    # carver
    del bpy.types.Scene.DepthCursor
    del bpy.types.Scene.OInstanciate
    del bpy.types.Scene.ORandom
    del bpy.types.Scene.DontApply
    del bpy.types.Scene.nProfile

    # booltool
    del bpy.types.Scene.BoolHide

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
        
        





