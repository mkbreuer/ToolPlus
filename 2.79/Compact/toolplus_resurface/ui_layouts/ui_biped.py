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


def draw_biped_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        

        icons = load_icons()


        col = layout.column(1)
                
        if not tp_props.display_skin: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_skin", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("BipedSkin")               
            
            button_skin_human = icons.get("icon_skin_human")                      
            row.operator("tp_ops.add_skin_human",text="", icon_value=button_skin_human.icon_id)

            button_skin_animal = icons.get("icon_skin_animal")  
            row.operator("tp_ops.add_skin_animal",text="", icon_value=button_skin_animal.icon_id)          
           
            #button_skin_empty = icons.get("icon_skin_empty")  
            #row.operator("tp_ops.add_skin_empty",text="", icon_value=button_skin_empty.icon_id)   
            row.operator("tp_ops.add_skin_empty",text="", icon ="MOD_SKIN")   

        else:
           
            box = col.box().column(1)
            
            row = box.row(1)  
            row.prop(tp_props, "display_skin", text="", icon="TRIA_DOWN", emboss = False)            
            row.label("BipedSkin")  

            box.separator()            

            split = box.split()

            row.scale_y = 1.2
            row = box.row(1)

            row.operator("tp_ops.add_skin_empty",text="Vertex", icon ="MOD_SKIN")    
           
            button_skin_human = icons.get("icon_skin_human")                      
            row.operator("tp_ops.add_skin_human",text="Human", icon_value=button_skin_human.icon_id)

            button_skin_animal = icons.get("icon_skin_animal")  
            row.operator("tp_ops.add_skin_animal",text="Animal", icon_value=button_skin_animal.icon_id)         
       
            
            box.separator()   

            obj = context.active_object
            if obj:
 
                mo_types = []            
                append = mo_types.append

                for mo in context.active_object.modifiers:
                                                  
                    if mo.type == "SKIN":# and bpy.context.object.mode == "EDIT":
                        append(mo.type)
                        #box.label(mo.name)

                        box.separator() 

                        row = box.row()
                        
                        ob = context.object
                        for mod in [m for m in ob.modifiers if m.type == 'MIRROR']:   
                            row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="Mirror")   
                            
                        for mod in [m for m in ob.modifiers if m.type == 'SUBSURF']:   
                            row.prop(bpy.context.active_object.modifiers[mod.name], "show_viewport", text="SubSurf")                                                                         

                        box.separator() 
                        
                        row = box.row()
                        row.operator("object.skin_armature_create", text="Create Armature")
                        row.operator("mesh.customdata_skin_add")

                        box.separator()

                        row = box.row(align=True)
                        row.prop(mo, "branch_smoothing")
                        row.prop(mo, "use_smooth_shade")

                        split = box.split()

                        col = split.column()                       
                        col.label(text="Selected Vertices:")
                        
                        sub = col.column(align=True)
                        sub.operator("object.skin_root_mark", text="Mark Root")
                        sub.operator("object.skin_radii_equalize", text="Equalize Radii")
                        sub.operator("object.skin_loose_mark_clear", text="Mark Loose").action = 'MARK'
                        sub.operator("object.skin_loose_mark_clear", text="Clear Loose").action = 'CLEAR'


                        col = split.column()
                        col.label(text="Symmetry Axes:")
                        col.prop(mo, "use_x_symmetry")
                        col.prop(mo, "use_y_symmetry")
                        col.prop(mo, "use_z_symmetry")
                        
                        box.separator()                          