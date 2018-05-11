# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

#bl_info = {
#    "name": "Background Images Fast Import",
#    "author": "Roman Sychev (XArgon)",
#    "version": (1, 1),
#    "blender": (2, 76, 0),
#    "location": "Toolshelf > Create Tab",
#    "description": "Imports a batch of background images from folder, automatically assigning them to different views based on file name",
#    "warning": "",
#    "wiki_url": "",
#    "category": "3D View",
#}

import bpy
import os

def ImportFunction(path, only_cardinal, ppu, size, opacity):
    if len(path)>0:
        view = bpy.context.space_data
        i=0
        for b in view.background_images:
            i+=1
        for r in range(0,i):
            bpy.ops.view3d.background_image_remove()
        for a in bpy.context.screen.areas:
            if a.type == 'VIEW_3D':
                space = a.spaces.active
                files = os.listdir(path)
                for f in files:
                    ext = f[-4:].lower()
                    if (ext==".jpg") or (f[-5:].lower()==".jpeg") or (ext==".png"):
                        ucf = f.upper()
                        res = -1
                        for i in range(0,8):
                            if i==0:
                                comp = 'FRONT'
                            elif i==1:
                                comp = 'RIGHT'
                            elif i==2:
                                comp = 'TOP'
                            elif i==3:
                                comp = 'BACK'
                            elif i==4:
                                comp = 'LEFT'
                            elif i==5:
                                comp = 'BOTTOM'
                            elif i==6:
                                comp = 'CAMERA'
                            else:
                                comp = 'ALL'
                            res = ucf.find(comp)
                            if res>=0:
                                break
                        if (comp!='ALL') or (only_cardinal==0):
                            img = bpy.data.images.load(path+f)
                            bg = space.background_images.new()
                            bg.image = img
                            bg.view_axis = comp
                            if ppu:
                                set_size = img.size[0]/size
                                # bpy.context.scene.scale_length
                                #bpy.context.space_data.context = 'SCENE'
                                if (bpy.data.scenes[0].unit_settings.system == 'IMPERIAL'):
                                    set_size /= 3.281
                            else:
                                set_size = size
                            bg.size = set_size
                            bg.opacity = opacity
                bpy.context.space_data.show_background_images = True
                break

class BackgroundFastImport(bpy.types.Operator):
    """Fast Images Upload > name must be RIGHT-LEFT-TOP-BOTTOM-FRONT-BACK / CAMERA / ALL"""
    bl_idname = "view3d.background_images_fast_import"
    bl_label = "Fast image import to background"
    bl_options = {'REGISTER', 'UNDO'}

    only_cardinal = bpy.props.BoolProperty(name="Only cardinal directions",
        description="Only images with Right/Left/Top/Bottom/Front/Back in their name will be loaded",
        default=1)

    path = bpy.props.StringProperty(name="Path to folder",
        description="The folder containing the images to be used as backgrounds",
        subtype="DIR_PATH")

    ppu = bpy.props.BoolProperty(name="Scale as Pixels-per-Unit",
        description="If disabled, will use vanilla scaling (number of units for whole image width)",
        default=1)

    size = bpy.props.FloatProperty(name="Scale",
        description="Size property for all images",
        min=0.01,
        max=9999.0,
        default=72.0)

    opacity = bpy.props.FloatProperty(name="opacity",
        description="Opacity for all images",
        min=0.0,
        max=1.0,
        default=0.5)

    def execute(self, context):
        ImportFunction(self.path, self.only_cardinal, self.ppu, self.size, self.opacity)
        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()