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



def draw_menu_delete_layout(self, context, layout):
          
        icons = load_icons()   
        
        settings = context.tool_settings
        tp_orphan = context.scene.orphan_props  

        layout.operator_context = 'INVOKE_REGION_WIN'              
       
        if context.mode == 'OBJECT':
           
            layout.operator("object.delete")                

            obj = context.active_object     
            if obj:
               obj_type = obj.type
               if obj_type in {'MESH'}: 
                    layout.operator("tp_ops.remove_double", "Remove Doubles")

            layout.operator("tp_ops.remove_all_material", text = "Delete Material Slots")            
            layout.operator("tp_ops.delete_from_all_scenes", text = "Delete From All Scenes")           
           
            layout.separator()             

            layout.operator("tp_ops.delete_data_obs",text = "Clear unused Orphan")                         
            layout.prop(tp_orphan, "mod_list")

            layout.separator() 

            layout.menu("VIEW3D_MT_object_clear", text="Clear Transform")

            layout.separator() 

            layout.operator("remove.gp", text="Delete GPencil", icon="PANEL_CLOSE")



        if context.mode == 'EDIT_MESH':

            layout.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type="VERT"
            layout.operator("mesh.dissolve_verts")
            layout.operator("mesh.remove_doubles")

            layout.separator()
            
            layout.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type="EDGE"
            layout.operator("mesh.dissolve_edges")
            layout.operator("mesh.delete_edgeloop", text="Remove Edge Loop")            
            layout.separator()
            
            layout.operator("mesh.delete", "Faces", icon="SNAP_FACE").type="FACE"
            layout.operator("mesh.dissolve_faces")
            layout.operator("mesh.delete", "Remove only Faces").type="ONLY_FACE"                        
            
            layout.separator()

            layout.operator("mesh.dissolve_limited", icon="MATCUBE")		
            layout.operator("mesh.dissolve_degenerate")
            layout.operator("mesh.delete", "Remove Edge & Faces").type="EDGE_FACE"
            
            layout.separator() 

            layout.operator("mesh.delete_loose", icon = "GROUP_VERTEX")
            layout.operator("tp_ops.dissolve_edge_loops", text="Ring Dissolve")
            layout.operator("mesh.edge_collapse")  

            layout.separator()
                            
            layout.operator("mesh.fill_holes", icon="MESH_GRID") 

            layout.operator_context = 'INVOKE_DEFAULT'
            layout.operator("tp_ops.build_corner")
            layout.operator("mesh.face_make_planar")
     
            layout.separator()
         
            layout.operator("mesh.decimate", text="Decimate", icon = "MESH_ICOSPHERE")            
            layout.operator("mesh.tris_convert_to_quads")
            layout.operator("mesh.quads_convert_to_tris")

            layout.separator()
        
            layout.operator("mesh.vert_connect_concave")
            layout.operator("mesh.vert_connect_nonplanar")

        if context.mode == 'EDIT_CURVE':

            layout.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            layout.operator("curve.delete", "Segment", icon="IPO_EASE_IN_OUT").type="SEGMENT"

            layout.separator()

            layout.operator("curve.dissolve_verts", "Dissolve Vertices", icon="PANEL_CLOSE")


        if context.mode == 'EDIT_SURFACE':

            layout.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            layout.operator("curve.delete", "Segments", icon="IPO_EASE_IN_OUT").type="SEGMENT"

        if context.mode == 'EDIT_METABALL':
           
            layout.operator("mball.delete_metaelems", icon="META_BALL")
  
        if  context.mode == 'PARTICLE':

            layout.operator("particle.delete")
           
            layout.separator()
           
            layout.operator("particle.remove_doubles")
    
        if context.mode == 'SCULPT':
             
            props = layout.operator("paint.hide_show", text="Clear All Hide", icon = "RESTRICT_VIEW_OFF")
            props.action = 'SHOW'
            props.area = 'ALL'

        if context.mode == 'EDIT_ARMATURE':
            
            layout.operator("armature.delete", text = "Selected Bone(s)", icon = "RIGHTARROW_THIN")

            layout.separator()
            
            layout.operator("sketch.delete", text = "Sketch Delete", icon = "RIGHTARROW_THIN")  
            
            layout.separator()
                         
            layout.operator("armature.parent_clear", icon = "RIGHTARROW_THIN").type='CLEAR'

        if context.mode == 'POSE':
           
            arm = context.active_object.data 

            layout.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")
            layout.operator("pose.paths_clear", text = "Clear Motion Path")

            layout.separator()

            layout.menu("VIEW3D_MT_pose_transform", text="Clear Location")  
            layout.menu("clearparent", text="Clear Parenting")
            layout.operator("pose.constraints_clear", text="Clear Constraint")            





class VIEW3D_TP_Delete_Panel_Menu(bpy.types.Menu):
    bl_label = "Delete"
    bl_idname = "tp_menu.pl_menu_delete"   

    def draw(self, context):
        layout = self.layout

        draw_menu_delete_layout(self, context, layout) 


class VIEW3D_TP_Delete_Menu(bpy.types.Menu):
    bl_label = "Delete"
    bl_idname = "VIEW3D_TP_Delete_Menu"   

    def draw(self, context):
        layout = self.layout

        draw_menu_delete_layout(self, context, layout)