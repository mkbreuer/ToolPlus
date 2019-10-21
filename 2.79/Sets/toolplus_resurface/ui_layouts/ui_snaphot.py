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

from toolplus_resurface.ops_editing.snapshot import *


def draw_snapshot_ui(self, context, layout):
        tp_props = context.window_manager.tp_props_resurface        

        layout.operator_context = 'INVOKE_REGION_WIN'

        icons = load_icons()
  
        obj = context.active_object 
        scene = context.scene
        
        col = layout.column(align=True)
        
        box = col.box().column(1)       

        if not tp_props.display_snapshot: 
        
            row = box.row(1)
            row.prop(tp_props, "display_snapshot", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("SnapShot")
         
            row.operator("tp_ops.multires_recopy","", icon ="PASTEDOWN")         
            row.operator("vtools.deletesnapshot","", icon ="DISCLOSURE_TRI_DOWN")         
            row.operator("vtools.capturesnapshot", icon='DISCLOSURE_TRI_RIGHT', text="")

        else:
            
            row = box.row(1)
            row.prop(tp_props, "display_snapshot", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("SnapShot")
           
            row.operator("tp_ops.multires_recopy","", icon ="PASTEDOWN") 
            row.operator("vtools.deletesnapshot","", icon ="DISCLOSURE_TRI_DOWN")         
            row.operator("vtools.capturesnapshot", icon='DISCLOSURE_TRI_RIGHT', text="")

            box.separator() 

            #row = box.row(1)    
            #row.operator("vtools.capturesnapshot", icon='ZOOMIN', text="Add")
            #row.operator("vtools.deletesnapshot", icon='ZOOMOUT', text="Remove")
             
            #box.separator() 
            
            row = box.row(1)               
            row.template_list('UI_UL_list', "snapShotMesh_ID", obj, "snapShotMeshes", obj, "snapShotMesh_ID_index", rows=2)


            box.separator() 
            
            row = box.row(1)      
            row.operator("vtools.recalculatesnapshotfromchildren", icon='BORDERMOVE', text="Refresh")                      
            row.operator("vtools.usesnapshot", icon='OUTLINER_OB_MESH', text="Set Shot")                           
 
            
            box.separator() 
            
            row = box.row(1)      
            row.operator("vtools.deleteallsnapshot", icon='PANEL_CLOSE', text="Del. All") 
            row.operator("vtools.deleteunusedsnapshotlist", icon='PANEL_CLOSE', text="Del. Unused")                     

            box.separator() 