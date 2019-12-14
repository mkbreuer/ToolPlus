# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2019 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
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
#

bl_info = {
    "name": "Outline Renamer",
    "author": "marvin.k.breuer (MKB)",
    "version": (0, 0, 1),
    "blender": (2, 81, 0),
    "location": "Outliner > Header: Button",
    "description": "add buttons to outliner header: batch rename, copy name to data name and vice versa",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer",
    "tracker_url": "",
    "category": "User Tools"}


# LOAD MODUL #    
import bpy
from bpy.props import BoolProperty


class VIEW3D_OT_copy_object_name_to_data_name(bpy.types.Operator):
    """copy object-name to data-name"""
    bl_idname = "tpc_ops.copy_object_name_to_data_name"
    bl_label = "Copy Object-Name to Data-Name"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        selected = bpy.context.selected_objects 
        for obj in selected:     
            obj.data.name = obj.name            
        return{'FINISHED'}
    
class VIEW3D_OT_copy_data_name_to_object_name(bpy.types.Operator):
    """copy data-name to object-name"""
    bl_idname = "tpc_ops.copy_data_name_to_object_name"
    bl_label = "Copy Data-Name to Object-Name"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        selected = bpy.context.selected_objects 
        for obj in selected:     
            obj.name = obj.data.name
        return {'FINISHED'}

def draw_buttons(self, context):	
    layout = self.layout
   
    row = layout.row(align=True)   
    row.operator("wm.batch_rename", text="", icon='COPY_ID') 
    row.operator("tpc_ops.copy_data_name_to_object_name", text="", icon='COPYDOWN') 
    row.operator("tpc_ops.copy_object_name_to_data_name", text="", icon='PASTEDOWN') 


def update_layout_callback(self, context):
    try:     
        bpy.types.OUTLINER_HT_header.remove(draw_buttons)   
    except:
        pass
    
    addon_prefs = context.preferences.addons[__name__].preferences    
  
    if addon_prefs.toggle_location == True: # top        
        bpy.types.OUTLINER_HT_header.prepend(draw_buttons)  

    if addon_prefs.toggle_location == False: # bottom
        bpy.types.OUTLINER_HT_header.append(draw_buttons)  


# ADDON PREFERENCES #
class Addon_Preferences_Outline_Renamer(bpy.types.AddonPreferences):
    bl_idname = __name__

    toggle_location : BoolProperty(name="Top/Bottom", default=True, description="menu layout position", update = update_layout_callback)

    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)                                                
        row.label(text="Buttons in Outliner:")
        row.prop(self, "toggle_location", text="")


# REGISTER #
classes = (
    Addon_Preferences_Outline_Renamer,
    VIEW3D_OT_copy_object_name_to_data_name,
    VIEW3D_OT_copy_data_name_to_object_name,
    )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
   
    update_layout_callback(None, bpy.context)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
