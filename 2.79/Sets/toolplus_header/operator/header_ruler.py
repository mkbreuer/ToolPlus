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
from bpy_extras import view3d_utils



# OPERATOR #

class VIEW3D_TP_Header_Event_Set(bpy.types.Operator):
    """click: default ruler / shift+click: np distance point"""
    bl_idname = "tp_ops.event_set"
    bl_label = " Ruler"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def invoke(self, context, event):

        ev = []
        ev.append("Click")  

        if event.shift:
            ev.append("Shift")

            bpy.ops.tp_ops.np_020_point_distance()
        else:
            bpy.ops.view3d.ruler()  

        #self.report({'INFO'}, "+".join(ev))

        return {'FINISHED'}



# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()