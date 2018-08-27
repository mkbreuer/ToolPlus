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
from .. icons.icons import load_icons

from toolplus_resurface.ops_editing.meshlint   import *
from toolplus_resurface.ops_editing.meshcheck  import *


def draw_check_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)

        box = col.box().column(1)  

        if not tp_props.display_mcheck: 
            row = box.row(1)   
            row.prop(tp_props, "display_mcheck", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("MCheck")
           
            button_tris = icons.get("icon_check_triangle")                
            row.operator("object.face_type_select", text="", icon_value=button_tris.icon_id).face_type = 'tris'

            button_ngon = icons.get("icon_check_ngon")                
            row.operator("object.face_type_select", text="",icon_value=button_ngon.icon_id).face_type = 'ngons'
           
            #row.operator('meshlint.select', text='', icon='LAMP')
            mesh_check = bpy.context.window_manager.mesh_check
            row.prop(mesh_check, "display_faces", text='', icon='GROUP_VCOL')
            
        else:
            row = box.row(1)   
            row.prop(tp_props, "display_mcheck", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("MCheck")   

            button_tris = icons.get("icon_check_triangle")                
            row.operator("object.face_type_select", text="", icon_value=button_tris.icon_id).face_type = 'tris' 
 
            button_ngon = icons.get("icon_check_ngon")                
            row.operator("object.face_type_select", text="",icon_value=button_ngon.icon_id).face_type = 'ngons'

            #row.operator('meshlint.select', text='', icon='LAMP')
            row.prop(context.window_manager.mesh_check, "display_faces", text='', icon='GROUP_VCOL')


            box = col.box().column(1)
            
            row = box.row(1)
            row.prop(context.active_object.data, "show_extra_edge_length", text="Edge Length")
            row.prop(context.active_object.data, "show_extra_face_area", text="Face Area")

            row = box.row(1)
            row.prop(context.active_object.data, "show_extra_edge_angle", text="Edge Angle")
            row.prop(context.active_object.data, "show_extra_face_angle", text="Face Angle")

            box.separator()   

                       
            box = col.box().column(1)         

            row = box.row(1)
            row.operator('meshlint.select', text='Select MeshLint', icon='EDIT')
       
            row = box.row(1)
            
            if tp_props.display_meshlint_toggle:
                row.prop(tp_props, "display_meshlint_toggle", text="Settings", icon='TRIA_DOWN_BAR')
            else:
                row.prop(tp_props, "display_meshlint_toggle", text="Settings", icon='TRIA_UP_BAR')
          
            if MeshLintVitalizer.is_live:
                live_label = 'Pause!'
                play_pause = 'PAUSE'
            else:
                live_label = 'Live!'
                play_pause = 'PLAY'
            
            row.operator('meshlint.live_toggle', text=live_label, icon=play_pause)

            box.separator() 

            if tp_props.display_meshlint_toggle:
                
                box = col.box().column(1)                   
                
                row = box.column(1)

                for lint in MeshLintAnalyzer.CHECKS:
                    prop_name = lint['check_prop']
                    is_enabled = getattr(context.scene, prop_name)
                    label = 'Check ' + lint['label']
                    row.prop(context.scene, prop_name, text=label)
              
                box.separator() 
                box = col.box().column(1)      

            
            row = box.column(1)
            active = context.active_object

            if not has_active_mesh(context):
                return

            total_problems = 0

            for lint in MeshLintAnalyzer.CHECKS:
                count = lint['count']
                
                if count in (TBD_STR, N_A_STR):
                    label = str(count) + ' ' + lint['label']
                    reward = 'SOLO_OFF'
                elif 0 == count:
                    label = 'No %s!' % lint['label']
                    reward = 'SOLO_ON'
                else:
                    total_problems += count
                    label = str(count) + 'x ' + lint['label']
                    label = depluralize(count=count, string=label)
                    reward = 'ERROR'
         
                row.label(text=label, icon=reward)

            box.separator()
           

            box = col.box().column(1)   

            row = box.row(1)
            button_tris = icons.get("icon_check_triangle")                
            row.operator("object.face_type_select", text="Tris", icon_value=button_tris.icon_id).face_type = 'tris'
            
            button_ngon = icons.get("icon_check_ngon")                
            row.operator("object.face_type_select", text="Ngons",icon_value=button_ngon.icon_id).face_type = 'ngons'

            box.separator()


            row = box.row()
            mesh_check = bpy.context.window_manager.mesh_check
            #row.prop(mesh_check, "mesh_check_use", text="UseMeshCheck")
            row.prop(mesh_check, "display_faces", text="MeshCheck")            

            if mesh_check.display_faces:
                
                col = box.column(align=True)
                col.prop(mesh_check, "edge_width")
                col.prop(mesh_check, "face_opacity")

                row = box.row()
                row.label(text="Custom Colors:", icon="COLOR")

                col = box.column().split(percentage=0.1, align=True)
                col.label(text="", icon_value=button_tris.icon_id)
                col.prop(mesh_check, "custom_tri_color", text="")

                col = box.column().split(percentage=0.1, align=True)
                col.label(text="", icon_value=button_ngon.icon_id)
                col.prop(mesh_check, "custom_ngons_color", text="")

                box.separator()

                row = box.row(align=True)
                if bpy.app.debug:
                    obj_data = getattr(context.active_object, "data", None)
                    if obj_data:
                        row.prop(obj_data, "show_extra_indices",
                                 icon="LINENUMBERS_ON", toggle=True)

                if context.mode == 'EDIT_MESH' and not context.space_data.use_occlude_geometry:
                    row.prop(mesh_check, "finer_lines_behind_use", icon="ORTHO")
