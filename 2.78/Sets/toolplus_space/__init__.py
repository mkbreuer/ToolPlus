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
    "name": "T+ Space",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N] and Menu",
    "description": "MeshSpace Panel and Menu in Editmode",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


from toolplus_space.space_looptools     import (Space_LoopToolsProps)
from toolplus_space.space_menu          import (VIEW3D_TP_Space_Menu)

from . icons.icons                      import load_icons
from . icons.icons                      import clear_icons

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_space'))

if "bpy" in locals():
    import imp
    imp.reload(space_looptools)
    imp.reload(space_straighten)
    imp.reload(space_vertices) 
else:
          
    from . import space_looptools                                         
    from . import space_straighten                             
    from . import space_vertices          
     
 
import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup


def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Mesh_Space_Panel_UI)

        bpy.utils.unregister_class(VIEW3D_TP_Mesh_Space_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Mesh_Space_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':

        VIEW3D_TP_Mesh_Space_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category

        bpy.utils.register_class(VIEW3D_TP_Mesh_Space_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Mesh_Space_Panel_UI)
  

addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Space_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        VIEW3D_TP_Space_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Space_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True, alt=True)
        kmi.properties.name = "tp_menu.space_base"


    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'off':
        pass




#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),   
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]')),
               default='tools', update = update_panel_position)

    tab_menu_view = EnumProperty(
        name = '3d View Menu',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('menu', 'Menu on', 'enable menu for 3d view'),
               ('off', 'Menu off', 'enable or disable menu for 3d view')),
               default='menu', update = update_menu)

    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)

    tools_category_menu = bpy.props.BoolProperty(name = "Space Menu", description = "enable or disable menu", default=True, update = update_menu)

    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            row = layout.column()
            row.label(text="Hello and welcome!")
            row.label(text="This is the space panel and space menu in editmode.")
            row.label(text="Each meshspace tool align vertices, edges or faces with a other result.")
            row.label(text="For more information follow the links in the URLs TAB.")
            row.label(text="Have Fun ! :)")
            
        #Location
        if self.prefs_tabs == 'location':
            row = layout.row()
            row.separator()
            
            row = layout.row()
            row.label("Location: ")
            
            row= layout.row(align=True)
            row.prop(self, 'tab_location', expand=True)
            row = layout.row()
            
            if self.tab_location == 'tools':
                row.prop(self, "tools_category")

        #Keymap
        if self.prefs_tabs == 'keymap':

            box = layout.box().column(1)
             
            row = box.column(1)  
            row.label("Space Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: CTRL+ALT+A")

            row = box.row(1)          
            row.prop(self, 'tab_menu_view', expand=True)
            
            if self.tab_menu_view == 'off':
                
                box.separator() 
                
                row = box.row(1) 
                row.label(text="! menu hidden with next reboot durably!", icon ="INFO")

            box.separator() 
             
            row.operator('wm.url_open', text = '! tip: is key free', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"

            box.separator() 
            
            row = layout.row(1) 
            row.label(text="! for key change go to > User Preferences > TAB: Input !", icon ="INFO")


        #Weblinks
        if self.prefs_tabs == 'url':
            row = layout.row()
            row = layout.column_flow(2)
            row.operator('wm.url_open', text = 'LoopTools', icon = 'INFO').url = "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Modeling/LoopTools"
            row.operator('wm.url_open', text = 'Kjartans', icon = 'INFO').url = "http://www.kjartantysdal.com/scripts"
            row.operator('wm.url_open', text = 'VertexTools', icon = 'INFO').url = "http://airplanes3d.net/scripts-254_e.xml"
            row.operator('wm.url_open', text = 'THREAD', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?416369-Addon-T-MeshSpace&p=3154665#post3154665"





def draw_mesh_space_panel_layout(self, context, layout):
    
        icons = load_icons()
        
        tp = context.window_manager.tp_space_looptools
                  
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        box = layout.box().row()
        
        row = box.column(1) 
        row.label("Align") 
        row.label("to") 
        row.label("Axis") 

        row = box.column(1)

        button_space_xy = icons.get("icon_space_xy") 
        row.operator("tp_ops.face_align_xy", "Xy", icon_value=button_space_xy.icon_id)

        button_space_zx = icons.get("icon_space_zx")
        row.operator("tp_ops.face_align_xz", "Zx", icon_value=button_space_zx.icon_id)

        button_space_zy = icons.get("icon_space_zy") 
        row.operator("tp_ops.face_align_yz", "Zy", icon_value=button_space_zy.icon_id)           

        row = box.column(1)

        button_space_x = icons.get("icon_space_x") 
        row.operator("tp_ops.face_align_x", "X", icon_value=button_space_x.icon_id)

        button_space_y = icons.get("icon_space_y") 
        row.operator("tp_ops.face_align_y", "Y", icon_value=button_space_y.icon_id)           

        button_space_z = icons.get("icon_space_z") 
        row.operator("tp_ops.face_align_z", "Z", icon_value=button_space_z.icon_id)

        box.separator()          
                     
        box = layout.box().column(1)    

        row = box.column(1)                  
        
        button_space_align_to_normal = icons.get("icon_space_align_to_normal") 
        row.operator("tp_ops.align_to_normal", "Align to Normal", icon_value=button_space_align_to_normal.icon_id)    

        box.separator() 
                  
        box = layout.box().column(1)   
                     
        row = box.column(1)                                                         

        button_space_straigten = icons.get("icon_space_straigten") 
        row.operator("mesh.vertex_align",text="Straighten", icon_value=button_space_straigten.icon_id) 

        button_space_distribute = icons.get("icon_space_distribute")  
        row.operator("mesh.vertex_distribute",text="Distribute", icon_value=button_space_distribute.icon_id)                                        
  
        box.separator() 
        
        box = layout.box().column(1)              
        
        row = box.row(1)  
        # space - first line
        split = row.split(percentage=0.15, align=True)

        button_space_space = icons.get("icon_space_space") 
        if tp.display_space:
            split.prop(tp, "display_space", text="", icon_value=button_space_space.icon_id)
        else:
            split.prop(tp, "display_space", text="", icon_value=button_space_space.icon_id)
        
        split.operator("mesh.looptools_space", text="LoopTools Space", icon='BLANK1')

        # space - settings
        if tp.display_space:
            box = layout.box().column(1)              
            
            row = box.column(1) 
            row.prop(tp, "space_interpolation")
            row.prop(tp, "space_input")

            box.separator()

            col_move = box.column(align=True)
            row = col_move.row(align=True)
            if tp.space_lock_x:
                row.prop(tp, "space_lock_x", text = "X", icon='LOCKED')
            else:
                row.prop(tp, "space_lock_x", text = "X", icon='UNLOCKED')
            if tp.space_lock_y:
                row.prop(tp, "space_lock_y", text = "Y", icon='LOCKED')
            else:
                row.prop(tp, "space_lock_y", text = "Y", icon='UNLOCKED')
            if tp.space_lock_z:
                row.prop(tp, "space_lock_z", text = "Z", icon='LOCKED')
            else:
                row.prop(tp, "space_lock_z", text = "Z", icon='UNLOCKED')
            col_move.prop(tp, "space_influence")

            box.separator() 
            box = layout.box().column(1)   


        row = box.row(1)  
        # curve - first line
        split = row.split(percentage=0.15, align=True)

        button_space_curve = icons.get("icon_space_curve") 
        if tp.display_curve:
            split.prop(tp, "display_curve", text="", icon_value=button_space_curve.icon_id)
        else:
            split.prop(tp, "display_curve", text="", icon_value=button_space_curve.icon_id)

        split.operator("mesh.looptools_curve", text="LoopTools Curve", icon='BLANK1')

        # curve - settings
        if tp.display_curve:
            box = layout.box().column(1)              
            
            row = box.column(1) 
            row.prop(tp, "curve_interpolation")
            row.prop(tp, "curve_restriction")
            row.prop(tp, "curve_boundaries")
            row.prop(tp, "curve_regular")
            
            box.separator()

            col_move = box.column(align=True)
            row = col_move.row(align=True)
            if tp.curve_lock_x:
                row.prop(tp, "curve_lock_x", text = "X", icon='LOCKED')
            else:
                row.prop(tp, "curve_lock_x", text = "X", icon='UNLOCKED')
            if tp.curve_lock_y:
                row.prop(tp, "curve_lock_y", text = "Y", icon='LOCKED')
            else:
                row.prop(tp, "curve_lock_y", text = "Y", icon='UNLOCKED')
            if tp.curve_lock_z:
                row.prop(tp, "curve_lock_z", text = "Z", icon='LOCKED')
            else:
                row.prop(tp, "curve_lock_z", text = "Z", icon='UNLOCKED')
            col_move.prop(tp, "curve_influence")

            box.separator() 
            box = layout.box().column(1)    


        row = box.row(1)  
        # circle - first line
        split = row.split(percentage=0.15, align=True)

        button_space_circle = icons.get("icon_space_circle") 
        if tp.display_circle:
            split.prop(tp, "display_circle", text="", icon_value=button_space_circle.icon_id)
        else:
            split.prop(tp, "display_circle", text="", icon_value=button_space_circle.icon_id)

        split.operator("mesh.looptools_circle", text="LoopTools Circle", icon='BLANK1')

        # circle - settings
        if tp.display_circle:
            box = layout.box().column(1)              
            
            row = box.column(1) 
            row.prop(tp, "circle_fit")
            
            row.separator()

            row.prop(tp, "circle_flatten")
            
            row = box.row(align=True)
            row.prop(tp, "circle_custom_radius")
            
            row_right = row.row(align=True)
            row_right.active = tp.circle_custom_radius
            row_right.prop(tp, "circle_radius", text="")                
            box.prop(tp, "circle_regular")
            
            box.separator()

            col_move = box.column(align=True)
            row = col_move.row(align=True)
            if tp.circle_lock_x:
                row.prop(tp, "circle_lock_x", text = "X", icon='LOCKED')
            else:
                row.prop(tp, "circle_lock_x", text = "X", icon='UNLOCKED')
            if tp.circle_lock_y:
                row.prop(tp, "circle_lock_y", text = "Y", icon='LOCKED')
            else:
                row.prop(tp, "circle_lock_y", text = "Y", icon='UNLOCKED')
            if tp.circle_lock_z:
                row.prop(tp, "circle_lock_z", text = "Z", icon='LOCKED')
            else:
                row.prop(tp, "circle_lock_z", text = "Z", icon='UNLOCKED')
            col_move.prop(tp, "circle_influence")

            box.separator() 
            box = layout.box().column(1)    
            

        row = box.row(1) 
        # flatten - first line
        split = row.split(percentage=0.15, align=True)

        button_space_flatten = icons.get("icon_space_flatten") 
        if tp.display_flatten:
            split.prop(tp, "display_flatten", text="", icon_value=button_space_flatten.icon_id)
        else:
            split.prop(tp, "display_flatten", text="", icon_value=button_space_flatten.icon_id)

        split.operator("mesh.looptools_flatten", text="LoopTool Flatten", icon ="BLANK1")

        # flatten - settings
        if tp.display_flatten:
            box = layout.box().column(1)    
             
            row = box.column(1)  
            row.prop(tp, "flatten_plane")

            box.separator()

            col_move = box.column(align=True)
            row = col_move.row(align=True)
            if tp.flatten_lock_x:
                row.prop(tp, "flatten_lock_x", text = "X", icon='LOCKED')
            else:
                row.prop(tp, "flatten_lock_x", text = "X", icon='UNLOCKED')
            if tp.flatten_lock_y:
                row.prop(tp, "flatten_lock_y", text = "Y", icon='LOCKED')
            else:
                row.prop(tp, "flatten_lock_y", text = "Y", icon='UNLOCKED')
            if tp.flatten_lock_z:
                row.prop(tp, "flatten_lock_z", text = "Z", icon='LOCKED')
            else:
                row.prop(tp, "flatten_lock_z", text = "Z", icon='UNLOCKED')
            col_move.prop(tp, "flatten_influence")

            box.separator() 

        ### 
        box.separator()     




class VIEW3D_TP_Mesh_Space_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Space_Panel_TOOLS"
    bl_label = "Space"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'mesh_edit'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        draw_mesh_space_panel_layout(self, context, layout) 



class VIEW3D_TP_Mesh_Space_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Mesh_Space_Panel_UI"
    bl_label = "Space"
    bl_space_type = 'VIEW_3D'
    bl_context = 'mesh_edit'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        return (context.object is not None and isModelingMode)
    
    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'   

        draw_mesh_space_panel_layout(self, context, layout) 




#Register and Unregister all the operators

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position(None, bpy.context)
    update_menu(None, bpy.context)
    
    bpy.types.WindowManager.tp_space_looptools = bpy.props.PointerProperty(type = Space_LoopToolsProps)


def unregister():


    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    try:
        del bpy.types.WindowManager.tp_space_looptools
    except:
        pass


if __name__ == "__main__":
    register()
        
        
                                   
             