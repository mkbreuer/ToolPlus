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
from . icons.icons import load_icons    



# UI: SUB MENU # 
def draw_header_item_view(self, context):
    layout = self.layout

    icons = load_icons()

    button_fun = icons.get("icon_fun")                      
    layout.label("Custom", icon_value=button_fun.icon_id)



def draw_header_item_select(self, context):
    layout = self.layout

    icons = load_icons()
    
    button_fun = icons.get("icon_fun")                      
    layout.label("Custom", icon_value=button_fun.icon_id)



def draw_header_item_add(self, context):
    layout = self.layout

    icons = load_icons()
    
    button_fun = icons.get("icon_fun")                      
    layout.label("Custom", icon_value=button_fun.icon_id) 



def draw_header_item_object(self, context):
    layout = self.layout

    icons = load_icons()
    
    button_fun = icons.get("icon_fun")                      
    layout.label("Custom", icon_value=button_fun.icon_id)             