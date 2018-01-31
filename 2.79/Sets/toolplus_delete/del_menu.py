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
from . icons.icons import load_icons



class VIEW3D_TP_CLEARPARENT(bpy.types.Menu):
    bl_label = "Clear Parenting"
    bl_idname = "tp_menu.clearparent"
        
    def draw(self, context):
        layout = self.layout
        
        layout.operator_enum("object.parent_clear", "type")


class VIEW3D_TP_CLEARTRACK(bpy.types.Menu):
    bl_label = "Clear Tracking"
    bl_idname = "tp_menu.cleartrack"
       
    def draw(self, context):
        layout = self.layout
        
        layout.operator_enum("object.track_clear", "type")



def draw_delete_history_tools(context, layout):
    settings = context.tool_settings
    layout.operator_context = 'INVOKE_REGION_WIN'
                                  
    layout.separator()   
      
    layout.operator("ed.undo", text="Undo", icon ="FRAME_PREV")
    layout.operator("ed.redo", text="Redo", icon ="FRAME_NEXT")
    layout.operator("ed.undo_history", text="History", icon ="COLLAPSEMENU") 


class VIEW3D_TP_Delete_Menu(bpy.types.Menu):
    bl_label = "Delete"
    bl_idname = "VIEW3D_TP_Delete_Menu"   

    def draw(self, context):
        layout = self.layout

        icons = load_icons()          
        
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

      
        if context.mode == 'OBJECT':

            layout.menu("VIEW3D_MT_object_showhide", text = "Show Hide", icon = "RESTRICT_VIEW_OFF") 
                           
            layout.separator()             

            layout.operator("object.delete")                

            if context.active_object.type in {'MESH'}:  
                layout.operator("tp_ops.remove_double", "Remove Doubles")

            layout.operator("tp_ops.remove_all_material", text = "Delete Material Slots")            
            layout.operator("tp_ops.delete_from_all_scenes", text = "Delete From All Scenes")           
           
            layout.separator()             

            layout.operator("tp_ops.delete_data_obs",text = "Clear unused Orphan")                   
            layout.prop(context.scene, "mod_list", text = "")

            layout.separator() 

            layout.menu("VIEW3D_MT_object_clear", text="Clear Transform")
            layout.menu("tp_menu.clearparent", text="Clear Parenting")
            layout.menu("tp_menu.cleartrack", text="Clear Tracking")
            
            layout.separator() 

            layout.operator("object.constraints_clear", text="Clear Constraint")
            layout.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")                        
            layout.operator("object.game_property_clear")             
            


        if context.mode == 'EDIT_MESH':

          
            layout.menu("VIEW3D_MT_edit_mesh_showhide", text="Show / Hide", icon = "RESTRICT_VIEW_OFF") 
            
            layout.separator() 
            
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
            layout.operator("tp_ops.dissolve_ring", text="Ring Dissolve")
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
                        
            layout.menu("VIEW3D_MT_edit_curve_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")           
             

        if context.mode == 'EDIT_SURFACE':

            layout.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            layout.operator("curve.delete", "Segments", icon="IPO_EASE_IN_OUT").type="SEGMENT"

            layout.separator() 
                        
            layout.menu("VIEW3D_MT_edit_curve_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF") 
                              

        if context.mode == 'EDIT_METABALL':
           
            layout.operator("mball.delete_metaelems", icon="META_BALL")

            layout.separator() 
            
            layout.menu("VIEW3D_MT_edit_meta_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")  

  
        if  context.mode == 'PARTICLE':

            layout.operator("particle.delete")

            layout.separator()

            layout.operator("particle.remove_doubles")
            
            layout.separator()

            layout.menu("VIEW3D_MT_particle_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")                        

    
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

            layout.separator()
              
            layout.menu("VIEW3D_MT_pose_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")  

           
        display_history = context.user_preferences.addons[__package__].preferences.tab_display_tools
        if display_history == 'on':   
            draw_delete_history_tools(context, layout)        






