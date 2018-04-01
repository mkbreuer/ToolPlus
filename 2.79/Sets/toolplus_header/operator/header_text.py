
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
# LOAD MODUL #    

import bpy
from bpy import *
from bpy.props import *


from os.path import dirname
from .. import header_append

class View3D_TP_Append_Map(bpy.types.Operator):
    bl_idname = "tp_ops.append_map_header"
    bl_label = "Open Append Map (Text Editor)"
    bl_description = "open file in the text editor"

    def execute(self, context):
        path = header_append.__file__
        bpy.data.texts.load(path)
        return {"FINISHED"}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()    