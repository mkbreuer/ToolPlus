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
    "name": "T+ Relax",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "View3D > Tool Shelf [T] or Property Shelf [N]",
    "description": "MeshRelax Panel in Editmode",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


from toolplus_relax.relax_looptools     import (Relax_LoopToolsProps)
from toolplus_relax.relax_menu          import (VIEW3D_TP_Relax_Menu)

from . icons.icons                      import load_icons
from . icons.icons                      import clear_icons

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_relax'))

if "bpy" in locals():
    import imp
    imp.reload(relax_looptools)
    imp.reload(relax_shrinkwrap)

else:
    from . import relax_looptools         
    from . import relax_shrinkwrap         
 
import bpy
from bpy import*
from bpy.props import* 
from bpy.types import AddonPreferences, PropertyGroup


def update_panel_position(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Mesh_Relax_Panel_UI)

        bpy.utils.unregister_class(VIEW3D_TP_Mesh_Relax_Panel_TOOLS)
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Mesh_Relax_Panel_UI)
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':

        VIEW3D_TP_Mesh_Relax_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category

        bpy.utils.register_class(VIEW3D_TP_Mesh_Relax_Panel_TOOLS)
    
    else:
        bpy.utils.register_class(VIEW3D_TP_Mesh_Relax_Panel_UI)
  



addon_keymaps_menu = []

def update_menu(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Relax_Menu)
        
        # Keymapping
        # remove keymaps when add-on is deactivated
        wm = bpy.context.window_manager
        for km in addon_keymaps_menu:
            wm.keyconfigs.addon.keymaps.remove(km)
        del addon_keymaps_menu[:]
        
    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_menu_view == 'menu':
     
        VIEW3D_TP_Relax_Menu.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_menu
    
        bpy.utils.register_class(VIEW3D_TP_Relax_Menu)
    
        # Keymapping 
        wm = bpy.context.window_manager
        
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=True, shift=True) #,alt=True
        kmi.properties.name = "tp_menu.relax_base"


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

    tools_category_menu = bpy.props.BoolProperty(name = "Relax Menu", description = "enable or disable menu", default=True, update = update_menu)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':

            row = layout.column()
            row.label(text="Hello and welcome!")
            row.label(text="This is the meshrelax panel in editmode.")
            row.label(text="Each relax tool poduced a other result on the mesh surface.")
            
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
            row.label("Relax Menu:", icon ="COLLAPSEMENU") 
            
            row.separator()           
            row.label("Menu: CTRL+SHIFT+W")

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
            row.operator('wm.url_open', text = 'Looptools', icon = 'IMAGE_COL').url = "https://plus.google.com/+MarvinKBreuer"
            row.operator('wm.url_open', text = 'Smooth Shrinkwrap', icon = 'IMAGE_COL').url = "http://www.kjartantysdal.com/scripts"
            row.operator('wm.url_open', text = 'Thread', icon = 'IMAGE_COL').url = "https://plus.google.com/+MarvinKBreuer"





def draw_mesh_relax_panel_layout(self, context, layout):
        
        tp = context.window_manager.tp_relax_looptools
        
        icons = load_icons()

        box = layout.box().column(1)    

        row = box.column(1)                      
 
        button_relax_vertices = icons.get("icon_relax_vertices") 
        row.operator("mesh.vertices_smooth","Vertices", icon_value=button_relax_vertices.icon_id) 

        button_relax_laplacian = icons.get("icon_relax_laplacian")
        row.operator("mesh.vertices_smooth_laplacian","Laplacian", icon_value=button_relax_laplacian.icon_id)  

        button_relax_shrinkwrap = icons.get("icon_relax_shrinkwrap")
        row.operator("mesh.shrinkwrap_smooth","Shrinkwrap", icon_value=button_relax_shrinkwrap.icon_id)         

        box.separator()   

        row = box.row(1)              

        button_relax_planar = icons.get("icon_relax_planar")  
        row.operator("mesh.face_make_planar", "Planar Faces", icon_value=button_relax_planar.icon_id) 

        box.separator()    
                     
        row = box.row(1)                 
                     
        # relax - first line
        split = row.split(percentage=0.15, align=True)
        if tp.display_tp_relax:
            button_relax_looptools = icons.get("icon_relax_looptools")
            split.prop(tp, "display_tp_relax", text="", icon_value=button_relax_looptools.icon_id)
            split.operator("edit_mesh.looptools_relax", text="  LoopTool Relax")

        else:
            button_relax_looptools = icons.get("icon_relax_looptools")
            split.prop(tp, "display_tp_relax", text="", icon_value=button_relax_looptools.icon_id)
            split.operator("edit_mesh.looptools_relax", text="  LoopTool Relax")

        # relax - settings
        if tp.display_tp_relax:
            box = layout.box().column(1)    
             
            row = box.column(1)  
            row.prop(tp, "relax_interpolation")
            row.prop(tp, "relax_input")
            row.prop(tp, "relax_iterations")
            row.prop(tp, "relax_regular")

        ###
        box.separator()    



class VIEW3D_TP_Mesh_Relax_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Mesh_Relax_Panel_TOOLS"
    bl_label = "Relax"
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

        draw_mesh_relax_panel_layout(self, context, layout) 



class VIEW3D_TP_Mesh_Relax_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Mesh_Relax_Panel_UI"
    bl_label = "Relax"
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

        draw_mesh_relax_panel_layout(self, context, layout) 




#Register and Unregister all the operators

import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
        
    update_panel_position(None, bpy.context)
    update_menu(None, bpy.context)
    
    bpy.types.WindowManager.tp_relax_looptools = bpy.props.PointerProperty(type = Relax_LoopToolsProps)


def unregister():


    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    try:
        del bpy.types.WindowManager.tp_relax_looptools
    except:
        pass


if __name__ == "__main__":
    register()
        
        
                                   
             
