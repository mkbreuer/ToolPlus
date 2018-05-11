# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
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
#


bl_info = {
    "name": "T+ Load UI",
    "author": "marvin.k.breuer (MKB)",
    "version": (1,1),
    "blender": (2, 7, 7),
    "location": "View3D > Property Shelf [N] > Backround Images Panel",
    "description": "add the 'Load UI' button from User Preferences > File, to the Backround Images Panel in the 3d View Property Shelf.",
    "warning": "",
    "wiki_url": "https://github.com/mkbreuer/ToolPlus",
    "tracker_url": "",
    "category": "Toolplus"}



# LOAD OPERATORS #
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'toolplus_load_ui'))

if "bpy" in locals():
    import imp
    imp.reload(fast_import)
else:
    from . import fast_import                

# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *


# LOAD UI #
def load_ui_to_bg_images(self,context):
    layout = self.layout
    
    col = layout.row(1)
    col.prop(context.user_preferences.filepaths, "use_load_ui", text= "Save & Load UI")
    col.operator("view3d.background_images_fast_import", text= "", icon ="IMAGE_COL")


# REGISTRY #
def register():
    bpy.types.VIEW3D_PT_background_image.append(load_ui_to_bg_images)    
    bpy.utils.register_module(__name__)

def unregister():    
    bpy.types.VIEW3D_PT_background_image.remove(load_ui_to_bg_images)  
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()  




              
