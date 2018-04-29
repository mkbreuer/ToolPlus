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
#    "name": "Add Tube or Pipe",
#    "author": "Roman Sychev (XArgon)",
#    "version": (1, 1),
#    "blender": (2, 76, 0),
#    "location": "Toolshelf > Create Tab",
#    "description": "Adds customizable Tube or Pipe object",
#    "warning": "",
#    "wiki_url": "",
#    "category": "Add Curve",
#}

if "bpy" in locals():
    import importlib
    importlib.reload(Tube)
    importlib.reload(Pipe)
    importlib.reload(Makemesh)
else:
    import bpy
    from bpy.types import Operator, Panel
    from toolplus_curve.inserts.add_pipe_or_tube import (Tube, Pipe, Makemesh)


#class add_pipe(Panel):
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'TOOLS'
    #bl_category = 'Create'
    #bl_label = "Tubes and Pipes"
    #bl_context = "objectmode"
    #bl_options = {'DEFAULT_CLOSED'}

    #def draw(self, context):
        #layout = self.layout
        #layout.operator(Tube.AddTube.bl_idname, text="Tube")
        #layout.operator(Pipe.AddPipe.bl_idname, text="Pipe")
        #layout.operator(Makemesh.Convert.bl_idname, text="Convert to Mesh")


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()