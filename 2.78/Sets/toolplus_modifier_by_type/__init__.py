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
    "name": "T+ Modifier by Type",
    "author": "MKB",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "VIEW3D",
    "description": "Apply, Remove, (Un)Hide or exclude Modifier from Render on all selected Object",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "ToolPlus"}


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_modifier_by_type'))

if "bpy" in locals():
    import imp

    imp.reload(mods_copy)
    imp.reload(mods_ops)

else:              
    from . import mods_copy               
    from . import mods_ops               


import bpy
from bpy import*
from bpy.props import*
from bpy.types import AddonPreferences, PropertyGroup


def update_panel_position(self, context):
    try:      
        bpy.utils.unregister_class(VIEW3D_TP_Mod_Type_Panel_UI)       
        bpy.types.DATA_PT_modifiers.remove(menu_func)    
        bpy.utils.unregister_class(VIEW3D_TP_Mod_Type_Panel_TOOLS)   
    except:
        pass
    
    try:
        bpy.utils.unregister_class(VIEW3D_TP_Mod_Type_Panel_UI)
    except:
        pass

    try:
        bpy.types.DATA_PT_modifiers.remove(menu_func) 
    except:
        pass

    if context.user_preferences.addons[__name__].preferences.tab_location == 'tools':
        
        VIEW3D_TP_Mod_Type_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category
        
        bpy.utils.register_class(VIEW3D_TP_Mod_Type_Panel_TOOLS)
    
    if context.user_preferences.addons[__name__].preferences.tab_location == 'ui':
        bpy.utils.register_class(VIEW3D_TP_Mod_Type_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location == 'win':
        bpy.types.DATA_PT_modifiers.prepend(menu_func)

    if context.user_preferences.addons[__name__].preferences.tab_location == 'off':
        pass




#Panel Preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    prefs_tabs = EnumProperty(
        items=(('location',   "Location",   "Location"),  
               ('url',        "URLs",       "URLs")),
               default='location')

    #Tab Location           
    tab_location = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('win', 'Property Modifier', 'place operators in the modifier property tab'),
               ('off', 'Off', 'on or off for panel in the shelfs')),
               default='tools', update = update_panel_position)

    #Panel
    tools_category = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'T+', update = update_panel_position)

    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
             
        #Location
        if self.prefs_tabs == 'location':
            
            box = layout.box().column(1)
             
            row = box.row(1) 
            row.label("Location:")
            
            row = box.row(1)
            row.prop(self, 'tab_location', expand=True)
            
            box.separator()

        #Weblinks
        if self.prefs_tabs == 'url':
            
            box = layout.box().column(1)
            
            row = box.column_flow(2)
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "https://blenderartists.org/forum/showthread.php?433382-T-Modifier-by-Type&p=3212243#post3212243"



def draw_modifier_type_panel_layout(self, context, layout):
          
        box = layout.box().column(1)
 
        row = box.row(1)            
        row.prop(context.scene, "tp_mods_type", text="")
        row.prop(context.scene, "tp_func_type", text="")

        row = box.row(1)
        row.operator("tp_ops.copy_choosen_mods", text="CopyDial", icon='PASTEDOWN') 
        row.operator("tp_ops.mods_by_type", text="RunTypes", icon='FRAME_NEXT')                            
       
        box.separator() 






class VIEW3D_TP_Mod_Type_Panel_TOOLS(bpy.types.Panel):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Mod_Type_Panel_TOOLS"
    bl_label = "Modifier by Type"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'objectmode'
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

        draw_modifier_type_panel_layout(self, context, layout) 




class VIEW3D_TP_Mod_Type_Panel_UI(bpy.types.Panel):
    bl_idname = "VIEW3D_TP_Mod_Type_Panel_UI"
    bl_label = "Modifier by Type"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = 'objectmode'
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

        draw_modifier_type_panel_layout(self, context, layout) 




# operator menu for modifier property tab
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



# register
import traceback

def register():
    
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    update_panel_position(None, bpy.context)


def unregister():


    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
if __name__ == "__main__":
    register()
        
        




              
