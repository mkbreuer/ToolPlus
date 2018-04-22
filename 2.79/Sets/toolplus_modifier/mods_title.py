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


def draw_mods_title_layout(self, context, layout):

    col = layout.column(align=True)  

    box = col.box().column(1)  
   
    row = box.row(1)                                        
    row.alignment = "CENTER"

    obj = context.active_object     
    if obj:
       obj_type = obj.type
                      
       if obj_type in {'MESH'}:
           row.label("MESH") 
                              
       if obj_type in {'LATTICE'}:
           row.label("LATTICE") 

       if obj_type in {'CURVE'}:
           row.label("CURVE")               
           
       if obj_type in {'SURFACE'}:
           row.label("SURFACE")                 
           
       if obj_type in {'META'}:
           row.label("MBall")                 
           
       if obj_type in {'FONT'}:
           row.label("FONT")  
                                          
       if obj_type in {'ARMATURE'}:
           row.label("ARMATURE") 

       if obj_type in {'EMPTY'}:
           row.label("EMPTY") 

       if obj_type in {'CAMERA'}:
          row.label("CAMERA") 

       if obj_type in {'LAMP'}:
           row.label("LAMP") 

       if obj_type in {'SPEAKER'}:
           row.label("SPEAKER") 