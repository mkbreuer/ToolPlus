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
#

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *   
from .. icons.icons import load_icons


def draw_custom_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        

        icons = load_icons()


        col = layout.column(align=True)
                
        if not tp_props.display_custom: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_custom", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Custom")               
          
            row.operator("render.render", text="", icon='RENDER_STILL')
            row.operator("render.render", text="", icon='RENDER_ANIMATION').animation = True
            #row.operator("sound.mixdown", text="", icon='PLAY_AUDIO')
            row.operator("tp_ops.render_wireframe", text="", icon='MOD_WIREFRAME')
            row.operator("render.opengl", text="", icon='RENDER_STILL')
            row.operator("render.opengl", text="", icon='RENDER_ANIMATION').animation = True
            

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_custom", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("Render")  
            row.operator("tp_ops.render_wireframe", text="", icon='MOD_WIREFRAME')
            
            
            box.separator()
            
            row = box.row(1)               
            row.scale_y = 3
            row.operator("render.render", text="Scene", icon='RENDER_STILL')

            row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True

            box.separator()
            
            row = box.row(1)               
            row.scale_y = 3
            row.operator("render.opengl", text="OpenGL", icon='RENDER_STILL')

            row.operator("render.opengl", text="Animation", icon='RENDER_ANIMATION').animation = True

            box.separator()
            
            row = box.row(1)
            row.prop(context.scene.render, "display_mode", text="")                                                                 
            row.menu("INFO_MT_opengl_render", "OpenGl Opt.")              

            
            box.separator()

        

#            # OBJECT #     
#            if context.mode == 'OBJECT':

#            # MESH #     
#            if context.mode == 'EDIT_MESH': 
          
#            # CURVE #     
#            if context.mode == 'EDIT_CURVE' or context.mode == 'EDIT_SURFACE': 

#            # SCULPT #      
#            if context.mode == 'SCULPT':         
                
 

                   