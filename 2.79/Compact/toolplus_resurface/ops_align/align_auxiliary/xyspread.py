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
#

"""
bl_info = {
    "name": "Nikitron tools",
    "version": (0, 1, 3),
    "blender": (2, 6, 9), 
    "author": "Nikita Gorodetskiy",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/Nikitron_tools",          
    "tracker_url": "http://www.blenderartists.org/forum/showthread.php?272679-Addon-WIP-Sverchok-parametric-tool-for-architects",  
}
"""

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
 
import re

import math
from math import radians

import mathutils
from mathutils import Vector
from mathutils.geometry import intersect_line_plane


class VIEW3D_TP_XY_Spread(bpy.types.Operator):
    """spread all objects on sheet for farthere use in dxf layout export / +xy axis"""
    bl_idname = "tp_ops.xy_spread"
    bl_label = "XY-Spread"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        count = len(obj) - 1                # items number
        row = math.modf(math.sqrt(count))[1] or 1 #optimal number of rows and columns !!! temporery solution
        locata = mathutils.Vector()    # while veriable 
        dx, dy, ddy = 0, 0, 0                       # distance
        while count > -1:   # iterations X
            locata[2] = 0               # Z = 0
            row1 = row
            x_curr = []                     # X bounds collection
            locata[1] = 0              # Y = 0
            while row1:         # iteratiorns Y
                # counting bounds
                bb = obj[count].bound_box
                mwscale = obj[count].matrix_world.to_scale()
                mwscalex = mwscale[0]
                mwscaley = mwscale[1]
                x0 = bb[0][0]
                x1 = bb[4][0]
                y0 = bb[0][1]
                y1 = bb[2][1]
                ddy = dy            # secondary distance to calculate avverage
                dx = mwscalex*(max(x0,x1)-min(x0,x1)) + 0.03        # seek for distance !!! temporery solution
                dy = mwscaley*(max(y0,y1)-min(y0,y1)) + 0.03        # seek for distance !!! temporery solution
                # shift y
                locata[1] += ((dy + ddy) / 2)
                # append x bounds
                x_curr.append(dx)
                bpy.ops.object.rotation_clear()
                bpy.context.selected_objects[count].location = locata
                row1 -= 1
                count -= 1
            locata[0] += max(x_curr)        # X += 1
            #dx, dy, ddy = 0, 0, 0
            del(x_curr)
        return {'FINISHED'}


# REGISTRY #        
def register():    
    bpy.utils.register_module(__name__)

def unregister():   
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()