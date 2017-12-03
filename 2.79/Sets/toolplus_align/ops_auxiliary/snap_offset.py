# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****


import bpy, bmesh, os
from bpy import*
from bpy.props import *
from bpy.types import WindowManager


#"name": "Snap to Center (offset)"
#"author": "Spirou4D", "version": (0,2)
###------ Create Snapping Operators -------###
   
class snapcenteroffset(bpy.types.Operator):
    """Snap the currently selected objects to Center with offset"""
    bl_idname = "mesh.snapcenteroffset"
    bl_label = "Selected to Center (offset)"
    bl_options = {'REGISTER', 'UNDO'}     
    
    
    @classmethod        
    def poll(cls, context):
        return len(context.selected_objects) > 0
    
    def execute(self, context):

        scene = bpy.context.scene
        #activeObj = context.active_object
        selected = context.selected_objects

        if selected:
            bpy.ops.view3d.snap_cursor_to_center()
            bpy.ops.view3d.snap_selected_to_cursor()
        else:
            self.report({'INFO'}, "No objects selected") 

        return {"FINISHED"}     

## -----------------------------------SELECT LEFT---------------------
def side (self, nombre, offset):

    bpy.ops.object.mode_set(mode="EDIT", toggle=0)
    OBJECT = bpy.context.active_object
    ODATA = bmesh.from_edit_mesh(OBJECT.data)
    MODE = bpy.context.mode
    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
    for VERTICE in ODATA.verts[:]:
        VERTICE.select = False
    if nombre == False:
        for VERTICES in ODATA.verts[:]:
            if VERTICES.co[0] < (offset):
                VERTICES.select = 1
    else:
        for VERTICES in ODATA.verts[:]:
            if VERTICES.co[0] > (offset):
                VERTICES.select = 1
    ODATA.select_flush(False)
    bpy.ops.object.mode_set(mode="EDIT", toggle=0)

class SelectMenor (bpy.types.Operator):
    bl_idname = "mesh.select_side_osc"
    bl_label = "Select Side"
    bl_options = {"REGISTER", "UNDO"}

    side = bpy.props.BoolProperty(name="Greater than zero", default=False)
    offset = bpy.props.FloatProperty(name="Offset", default=0)
    def execute(self,context):

        side(self, self.side, self.offset)

        return {'FINISHED'}




#"name": "Cursor to Edge Intersection"
#"author": "xxx", "version": (0,0)
####### Operator #######------------------------------------------------------- 

def abs(val):
    if val > 0:
        return val
    return -val

def EdgeIntersect(context, operator):
    from mathutils.geometry import intersect_line_line

    obj = context.active_object

    if (obj.type != "MESH"):
        operator.report({'ERROR'}, "Object must be a mesh")
        return None

    edges = []
    mesh = obj.data
    verts = mesh.vertices

    is_editmode = (obj.mode == 'EDIT')
    if is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT')

    for e in mesh.edges:
        if e.select:
            edges.append(e)

            if len(edges) > 2:
                break

    if is_editmode:
        bpy.ops.object.mode_set(mode='EDIT')

    if len(edges) != 2:
        operator.report({'ERROR'},
                        "Operator requires exactly 2 edges to be selected")
        return

    line = intersect_line_line(verts[edges[0].vertices[0]].co,
                               verts[edges[0].vertices[1]].co,
                               verts[edges[1].vertices[0]].co,
                               verts[edges[1].vertices[1]].co)

    if line is None:
        operator.report({'ERROR'}, "Selected edges do not intersect")
        return

    point = line[0].lerp(line[1], 0.5)
    context.scene.cursor_location = obj.matrix_world * point


class TP_Header_Cursor_to_Edge_Intersection(bpy.types.Operator):
    "Finds the mid-point of the shortest distance between two edges"
    bl_idname = "tp_header.snap_cursor_to_edge_intersection"
    bl_label = "Edge Intersection"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj != None and obj.type == 'MESH'

    def execute(self, context):
        EdgeIntersect(context, self)
        return {'FINISHED'}


    


####### Add Functions to VIEW3D_MT_snap #######------------------------------------------------------- 
def menu_func(self, context):
    layout = self.layout   
     
    layout.separator()     

    if context.mode == 'OBJECT':
        self.layout.operator(snapcenteroffset.bl_idname)
    
    if context.mode == 'EDIT_MESH':         
        self.layout.operator("mesh.circlecentercursor", text="3point Center")
        self.layout.operator(TP_Header_Cursor_to_Edge_Intersection.bl_idname)




#######  Register  #######------------------------------------------------------- 
def register():
    bpy.utils.register_module(__name__)

    bpy.types.VIEW3D_MT_snap.append(menu_func) 


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.VIEW3D_MT_snap.remove(menu_func) 
 
if __name__ == "__main__":
    register()





