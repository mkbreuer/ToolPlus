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
import bpy, os
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



def draw_menu_delete_curve(self, context, layout):
          
        icons = load_icons()   
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'              

        layout.scale_y = 1.3
       
        if context.mode == 'OBJECT':

            layout.operator("tp_purge.unused_curves_data",text = "Rem. Orphan Curves")                  

            layout.separator()     

            layout.operator("tp_ops.remove_all_material", text = "Rem. Material Slots")            
            layout.operator("tp_purge.unused_material_data",text = "Rem. Orphan Materials")  
       

        if context.mode == 'EDIT_CURVE':


            layout.operator("curve.delete", "Vertices").type="VERT"
            layout.operator("curve.delete", "Segment").type="SEGMENT"

            layout.separator()      
               
            layout.operator("curvetools2.operatorsplinesremoveshort", text = "Rem. Short Splines")
            layout.operator("curvetools2.operatorsplinesremovezerosegment", text = "Rem. Zero Segments")
           
            layout.separator()      

            layout.operator("curve.dissolve_verts", text="Dissolve Verts") 
            layout.operator("curve.remove_doubles", text="Remove Doubles") 

        
        if context.mode == 'EDIT_SURFACE':

            layout.operator("curve.delete", "Vertices").type="VERT"
            layout.operator("curve.delete", "Segments").type="SEGMENT"




class VIEW3D_TP_Delete_Menu_Curve(bpy.types.Menu):
    bl_label = "Delete"
    bl_idname = "tp_menu.curve_delete"   

    def draw(self, context):
        layout = self.layout

        draw_menu_delete_curve(self, context, layout) 

