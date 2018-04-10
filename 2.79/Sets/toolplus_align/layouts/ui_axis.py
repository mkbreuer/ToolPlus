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

def draw_axis_tools(context, layout):
    icons = load_icons()

    col = layout.column(align=True)

    box = col.box().row()   
    
    row = box.column(1) 
    row.label("Align") 
    row.label("to..") 
    row.label("Axis") 

    row = box.column(1)

    button_align_xy = icons.get("icon_align_xy") 
    row.operator("tp_ops.align_transform", "Xy", icon_value=button_align_xy.icon_id).tp_axis='axis_xy'

    button_align_zx = icons.get("icon_align_zx")
    row.operator("tp_ops.align_transform", "Zx", icon_value=button_align_zx.icon_id).tp_axis='axis_zx'

    button_align_zy = icons.get("icon_align_zy") 
    row.operator("tp_ops.align_transform", "Zy", icon_value=button_align_zy.icon_id).tp_axis='axis_zy'           

    row = box.column(1)

    button_align_x = icons.get("icon_align_x") 
    row.operator("tp_ops.align_transform", "X", icon_value=button_align_x.icon_id).tp_axis='axis_x'

    button_align_y = icons.get("icon_align_y") 
    row.operator("tp_ops.align_transform", "Y", icon_value=button_align_y.icon_id).tp_axis='axis_y'           

    button_align_z = icons.get("icon_align_z") 
    row.operator("tp_ops.align_transform", "Z", icon_value=button_align_z.icon_id).tp_axis='axis_z'

    row.separator() 


    box = col.box().column(1)               
    
    row = box.row(1)   

    button_align_mirror_obm = icons.get("icon_align_mirror_obm")              
    row.label("Mirror", icon_value=button_align_mirror_obm.icon_id) 
             
    sub = row.row(1)
    sub.scale_x = 0.3                   
    sub.operator("tp_ops.mirror1",text="X")
    sub.operator("tp_ops.mirror2",text="Y")
    sub.operator("tp_ops.mirror3",text="Z")            

    box.separator() 

    row = box.row(1)               
    row.label("Mody", icon ="MOD_MIRROR")                 

    sub = row.row(1)
    sub.scale_x = 0.3                               
    sub.operator("tp_ops.mod_mirror_x",text="X")
    sub.operator("tp_ops.mod_mirror_y",text="Y")
    sub.operator("tp_ops.mod_mirror_z",text="Z")      

    box.separator()   

    obj = context.active_object
    if obj:
 
        mo_types = []            
        append = mo_types.append

        for mo in obj.modifiers:
                                          
            if mo.type == 'MIRROR':
                append(mo.type)

                #box.label(mo.name)

                row = box.row(1)
                row.prop(mo, "use_x")
                row.prop(mo, "use_y")
                row.prop(mo, "use_z")
                
                row = box.row(1)
                row.prop(mo, "use_clip", text="Clip")
                row.prop(mo, "use_mirror_merge", text="Merge")               
                if mo.use_mirror_merge is True:
                    row.prop(mo, "merge_threshold", text="Limit")

                box.separator() 
    else:
        pass


    obj = context.active_object
    if obj:
        mod_list = obj.modifiers
        if mod_list:
           
            box.separator()                            

            row = box.row()    
            row.alignment = 'CENTER'                      
            row.operator("tp_ops.mods_view", text="", icon='RESTRICT_VIEW_OFF') 
            row.operator("tp_ops.remove_mods_mirror", text="", icon='PANEL_CLOSE') 
            row.operator("tp_ops.apply_mods_mirror_edm", text="", icon='FILE_TICK') 

            box.separator()                                                                      
    else:
        pass



