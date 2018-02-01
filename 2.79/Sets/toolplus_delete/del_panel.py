# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and/or
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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    


EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_METABALL", "EDIT_ARMATURE", "EDIT_PARTICLE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']


# DRAW UI LAYOUT #
def draw_delete_history_tools(context, layout):
    settings = context.tool_settings
    layout.operator_context = 'INVOKE_REGION_WIN'                                  

    col = layout.column(1)  
    box = col.box().column(1) 

    row = box.row(1)     
    row.operator("ed.undo", text="Undo", icon ="FRAME_PREV")
    row.operator("ed.undo_history", text="History", icon ="COLLAPSEMENU") 
    row.operator("ed.redo", text="Redo", icon ="FRAME_NEXT")



class draw_delete_panel_layout:
    
    @classmethod
    def poll(cls, context):
        isModelingMode = not (
        #context.sculpt_object or 
        context.vertex_paint_object
        or context.weight_paint_object
        or context.image_paint_object)
        obj = context.active_object     
        if obj:
            obj_type = obj.type                                                                
            if obj_type in GEOM:
                return isModelingMode and context.mode in EDIT

    def draw(self, context):
        layout = self.layout.column_flow(1)  
        layout.operator_context = 'INVOKE_REGION_WIN'

        tp_props = context.window_manager.tp_delete_window     
          
        icons = load_icons()

        col = layout.column(1)   

        box = col.box().column(1) 

        if context.mode == "OBJECT":


            row = box.row(1)
            row.menu("VIEW3D_MT_object_showhide", "Show Hide") 
            
            box.separator() 


            row = box.column(1) 
            row.operator("object.delete")                

            if context.active_object.type in {'MESH'}:  
                row.operator("tp_ops.remove_double", "Remove Doubles")

            row.operator("tp_ops.remove_all_material", text = "Delete Material Slots")            
            row.operator("tp_ops.delete_from_all_scenes", text = "Delete From All Scenes")           
           
            box.separator()             

            row = box.column(1)
            row.operator("tp_ops.delete_data_obs","Clear unused Orphan")                   
            row.prop(context.scene, "mod_list")

            box.separator() 

            row = box.column(1)
            row.menu("VIEW3D_MT_object_clear", text="Clear Transform")
            row.menu("tp_menu.clearparent", text="Clear Parenting")
            row.menu("tp_menu.cleartrack", text="Clear Tracking")
            
            box.separator() 

            row = box.column(1)
            row.operator("object.constraints_clear", text="Clear Constraint")
            row.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")                        
            row.operator("object.game_property_clear")             
            
            box.separator() 

            
            
        if context.mode == "EDIT_MESH":

            row = box.column(1)          
            row.operator("mesh.reveal", text="Show Hide", icon = "RESTRICT_VIEW_OFF") 
            row.operator("mesh.hide", text="Hide Selected", icon = "BLANK1").unselected=False
            row.operator("mesh.hide", text="Hide UnSelected", icon = "BLANK1").unselected=True 

            row.separator()  
            
            row.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type="VERT"
            row.operator("mesh.dissolve_verts", icon = "BLANK1")
            row.operator("mesh.remove_doubles", icon = "BLANK1")

            row.separator()
            
            row.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type="EDGE"
            row.operator("mesh.dissolve_edges", icon = "BLANK1")
            row.operator("mesh.delete_edgeloop", text="Remove Edge Loop", icon = "BLANK1")            
           
            row.separator()
            
            row.operator("mesh.delete", "Faces", icon="SNAP_FACE").type="FACE"
            row.operator("mesh.dissolve_faces", icon = "BLANK1")
            row.operator("mesh.delete", "Remove only Faces", icon = "BLANK1").type="ONLY_FACE"            
            
            
            row.separator()

            row.operator("mesh.dissolve_limited", icon="MATCUBE")		
            row.operator("mesh.dissolve_degenerate", icon = "BLANK1")
            row.operator("mesh.delete", "Remove Edge & Faces", icon = "BLANK1").type="EDGE_FACE"
            
            row.separator() 

            row.operator("mesh.delete_loose", icon = "GROUP_VERTEX")
            row.operator("tp_ops.dissolve_ring", text="Ring Dissolve", icon = "BLANK1")
            row.operator("mesh.edge_collapse", icon = "BLANK1")  

            row.separator()
                            
            row.operator("mesh.fill_holes", icon="MESH_GRID") 

            layout.operator_context = 'INVOKE_DEFAULT'
            row.operator("tp_ops.build_corner", icon = "BLANK1")
            row.operator("mesh.face_make_planar", icon = "BLANK1")
     
            row.separator()
         
            row.operator("mesh.decimate", text="Decimate", icon = "MESH_ICOSPHERE")            
            row.operator("mesh.tris_convert_to_quads", icon="BLANK1")
            row.operator("mesh.quads_convert_to_tris", icon="BLANK1")

            row.separator()
        
            row.operator("mesh.vert_connect_concave", icon = "BLANK1")
            row.operator("mesh.vert_connect_nonplanar", icon = "BLANK1")


        if context.mode == 'EDIT_CURVE':
           
            row = box.column(1)     
                        
            row.menu("VIEW3D_MT_edit_curve_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")         
            
            row.separator() 
            
            row.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            row.operator("curve.delete", "Segment", icon="IPO_EASE_IN_OUT").type="SEGMENT"


        if context.mode == 'EDIT_SURFACE':
            
            row = box.column(1) 
                        
            row.menu("VIEW3D_MT_edit_curve_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")

            row.separator() 

            row.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            row.operator("curve.delete", "Segments", icon="IPO_EASE_IN_OUT").type="SEGMENT"


        if context.mode == 'EDIT_METABALL':
           
            row = box.column(1)            
          
            row.menu("VIEW3D_MT_edit_meta_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")    
           
            row.separator() 
           
            row.operator("mball.delete_metaelems", icon="META_BALL")

  
        if  context.mode == 'PARTICLE':
           
            row = box.column(1) 

            row.menu("VIEW3D_MT_particle_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")                        

            row.separator()

            row.operator("particle.delete")

            row.separator()

            row.operator("particle.remove_doubles")
            

        if context.mode == 'SCULPT':
           
            row = box.column(1)              
            props = row.operator("paint.hide_show", text="Show All", icon = "RESTRICT_VIEW_OFF")
            props.action = 'SHOW'
            props.area = 'ALL'

            
        if context.mode == 'EDIT_ARMATURE':
       
            row = box.column(1)             
            row.operator("armature.delete", text = "Selected Bone(s)", icon = "RIGHTARROW_THIN")

            row.separator()
            
            row.operator("sketch.delete", text = "Sketch Delete", icon = "RIGHTARROW_THIN")  
            
            row.separator()
                         
            row.operator("armature.parent_clear", icon = "RIGHTARROW_THIN").type='CLEAR'


        if context.mode == 'POSE':
            
            arm = context.active_object.data 
      
            row = box.column(1) 

            row.menu("VIEW3D_MT_pose_showhide", text = "Show / Hide", icon = "RESTRICT_VIEW_OFF")            

            row.separator()
              
            row.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")
            row.operator("pose.paths_clear", text = "Clear Motion Path")

            row.separator()

            row.menu("VIEW3D_MT_pose_transform", text="Clear Location")  
            row.menu("clearparent", text="Clear Parenting")
            row.operator("pose.constraints_clear", text="Clear Constraint")            


        ###
        box.separator()   

        
        display_history = context.user_preferences.addons[__package__].preferences.tab_history
        if display_history == 'on': 
            
              
            draw_delete_history_tools(context, layout)        






# LOAD UI: PANEL #

class VIEW3D_TP_Delete_Panel_TOOLS(bpy.types.Panel, draw_delete_panel_layout):
    bl_category = "Delete"
    bl_idname = "VIEW3D_TP_Delete_Panel_TOOLS"
    bl_label = "Delete"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}



class VIEW3D_TP_Delete_Panel_UI(bpy.types.Panel, draw_delete_panel_layout):
    bl_idname = "VIEW3D_TP_Delete_Panel_UI"
    bl_label = "Delete"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
