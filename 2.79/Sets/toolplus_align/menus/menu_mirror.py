# ##### BEGIN GPL LICENSE BLOCK #####
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


# LOAD MODUL #
import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



class VIEW3D_TP_Mirror_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_Mirror_Menu"
    bl_label = "Mirror"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()

        layout.operator_context = 'INVOKE_REGION_WIN'
      
        split = layout.split()
        
        col = split.column(1)  
        
        col.scale_y = 1.3
      
        props = col.operator("transform.mirror", text="X Global")
        props.constraint_axis = (True, False, False)
        props.constraint_orientation = 'GLOBAL'
 
        props = col.operator("transform.mirror", text="Y Global")
        props.constraint_axis = (False, True, False)
        props.constraint_orientation = 'GLOBAL'
  
        props = col.operator("transform.mirror", text="Z Global")
        props.constraint_axis = (False, False, True)
        props.constraint_orientation = 'GLOBAL'


        if context.edit_object:
            
            col = split.column(1)  

            col.scale_y = 1.3
            
            props = col.operator("transform.mirror", text="X Local")
            props.constraint_axis = (True, False, False)
            props.constraint_orientation = 'LOCAL'
         
            props = col.operator("transform.mirror", text="Y Local")
            props.constraint_axis = (False, True, False)
            props.constraint_orientation = 'LOCAL'            
        
            props = col.operator("transform.mirror", text="Z Local")
            props.constraint_axis = (False, False, True)
            props.constraint_orientation = 'LOCAL'



class VIEW3D_TP_ModMirror_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_TP_ModMirror_Menu"
    bl_label = "ModMir"

    def draw(self, context):
        layout = self.layout
    
        icons = load_icons()
       
        layout.operator_context = 'INVOKE_REGION_WIN'

        split = layout.split()

        obj = context.active_object
        if obj:
            mod_list = obj.modifiers
            if mod_list:
                col = split.column(1)                              
                
                col.scale_y = 1.3                    
               
                col.operator("tp_ops.mods_view", text="", icon='RESTRICT_VIEW_OFF') 
                col.operator("tp_ops.remove_mods_mirror", text="", icon='PANEL_CLOSE') 
                col.operator("tp_ops.apply_mods_mirror", text="", icon='FILE_TICK')                                                                   
        else:
            pass

        col = split.column(1)                              

        col.scale_y = 1.3
       
        col.operator("tp_ops.mod_mirror_x",text="X-Axis")
        col.operator("tp_ops.mod_mirror_y",text="Y-Axis")
        col.operator("tp_ops.mod_mirror_z",text="Z-Axis")      
