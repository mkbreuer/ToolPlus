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
#from .. icons.icons import load_icons  

#EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
#GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']


class VIEW3D_TP_Header_Display_Menu(bpy.types.Menu):
    bl_label = "Display"
    bl_idname = "VIEW3D_TP_Header_Display_Menu"

    def draw(self, context):
        layout = self.layout
       
        #icons = load_icons()   

        #button_snap_place = icons.get("icon_snap_place")
        #layout.operator("tp_ops.place", text="Place", icon_value=button_snap_place.icon_id)

        #if context.mode in EDIT:

#        obj = context.active_object     
#        if obj:
#            obj_type = obj.type                                                                
#            if obj_type in GEOM and 

#        if context.mode == 'OBJECT':
#        else:
 
 
        view = context.space_data        
        obj = context.object
        obj_type = obj.type

        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
        is_dupli = (obj.dupli_type != 'NONE')

        layout.scale_y = 1.2
        
        layout.prop(obj, "show_x_ray", text="X-Ray")

        if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
            if obj and obj.mode == 'EDIT':
                layout.prop(view, "show_occlude_wire")

        layout.prop(view, "show_backface_culling")
 
        layout.separator() 
 
        if obj_type == 'MESH' or is_dupli:
            layout.prop(obj, "show_all_edges")

        if is_geometry or is_dupli:
            layout.prop(obj, "show_wire", text="Wire")
  
        layout.separator() 
              
        #layout.active = obj.show_bounds
        layout.prop(obj, "draw_bounds_type", text="")
        layout.prop(obj, "show_bounds", text="Bounds")

        layout.separator() 

        layout.prop(obj, "show_name", text="Name")
        layout.prop(obj, "show_axis", text="Axis")

        layout.separator()                
        
        layout.label("Display Tools")        