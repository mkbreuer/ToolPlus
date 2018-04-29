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

from toolplus_curve.menus.menu_add  import *


# ITEM APPEND #

def draw_item_curve(self, context):
    layout = self.layout
  
    if context.mode =='OBJECT':
        self.layout.separator()
        self.layout.menu("tp_menu.curve_add_2d", text="2D", icon = "MOD_CURVE")
        self.layout.menu("tp_menu.curve_add_3d", text="3D ", icon = "MOD_CURVE")        
        self.layout.menu("tp_menu.curve_add_knots", text="Knots", icon = "MOD_CURVE")  
        self.layout.menu("tp_menu.curve_add_plants", text="Plants", icon = "MOD_CURVE")   
      
        obj = context.active_object
        if obj:
            obj_type = obj.type                
            if obj.type in {'CURVE'}: 
                self.layout.separator()
                self.layout.operator("curve.simplify", text="Simplify", icon = "MOD_CURVE")
                
        self.layout.separator()
        self.layout.operator("tp_ops.bevel_set","Beveled", icon = "MOD_CURVE") 

   
    if context.mode =='EDIT_CURVE':            
        
        self.layout.separator()
        self.layout.operator("curve.simplify", text="Simplify", icon = "MOD_CURVE")

        self.layout.separator()
        self.layout.operator("tp_ops.bevel_set","Beveled", icon = "MOD_CURVE") 


def draw_item_special(self, context):
    layout = self.layout
    
    obj = context.active_object
    if obj:
        obj_type = obj.type                
        if obj.type in {'CURVE'}: 
            self.layout.operator("tp_batch.bevel_props") 


def draw_item_surface(self, context):
    layout = self.layout
    
    self.layout.separator()
    self.layout.menu("tp_menu.curve_add_factory")    



def draw_item_mesh(self, context):
    layout = self.layout
    
    if context.mode == "EDIT_MESH":
        self.layout.separator()    
        self.layout.operator("mesh.add_curvebased_tube", text="2-Face-Tube", icon="CURVE_DATA") 



def draw_item_editor_dopesheet(self, context):
    layout = self.layout
    self.layout.operator("curve.simplify", text="Curve Simplify", icon="CURVE_DATA")



def draw_item_editor_graph(self, context):
    layout = self.layout
    self.layout.operator("graph.simplify", text="Simplifiy F-Curves", icon="CURVE_DATA")



def draw_item_delete(self, context):
    layout = self.layout

    self.layout.separator() 
    
    self.layout.operator("curvetools2.operatorsplinesremoveshort", text = "Rem. Short Splines")
    self.layout.operator("curvetools2.operatorsplinesremovezerosegment", text = "Rem. Zero Segments")
   
    self.layout.separator()      

    self.layout.operator("curve.remove_doubles", text="Remove Doubles") 
 


def draw_item_SVG(self, context):
    layout = self.layout
    layout.separator()
    layout.operator('wm.url_open',  text = 'Online SVG Converter', icon = 'FILESEL').url = "http://image.online-convert.com/convert-to-svg"






