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
from . icons.icons import load_icons

EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']

class draw_layout_delete:
    
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

        tp_orphan = context.scene.orphan_props  

        icons = load_icons()    

        box = layout.box().column(1)     

        obj = context       
        if obj.mode == 'OBJECT':
                           
            row = box.column(1)                                           
            row.operator("object.delete", icon = "PANEL_CLOSE")

            box.separator()

            row = box.row(1)                                 
            button_remove_doubles = icons.get("icon_remove_doubles")
            row.operator("tp_ops.remove_doubles", text="Remove Doubles",icon_value=button_remove_doubles.icon_id)         

            box.separator()

            row = box.row(1)               
            row.prop(tp_orphan, "mod_list")
            row.operator("tp_ops.delete_data_obs","Purge", icon ="GHOST_DISABLED")            

            box.separator()
      
            row = box.column(1)   
            row.operator("tp_ops.delete_scene_obs", text="     Clear all Scene")                     
            row.operator("tp_ops.remove_all_material", text="     Clear MAT-Slots")

            row.separator()

            row.menu("VIEW3D_MT_object_clear", text="Clear Location", icon='EMPTY_DATA')

            row.separator()
            
            row.menu("tp_ops.clearparent", text="Clear Parenting", icon='CONSTRAINT')
            row.menu("tp_ops.cleartrack", text="Clear Tracking", icon='BLANK1')
            row.operator("object.constraints_clear", text="     Clear Constraint")

            row.separator()
           
            row.operator("anim.keyframe_clear_v3d", text = "     Clear Keyframe")                        
            row.operator("object.game_property_clear", text = "     Clear Game Props")


        elif obj.mode == 'EDIT_MESH':

            row = box.column(1)   
            
            row.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type="VERT"
            row.operator("mesh.dissolve_verts", icon='BLANK1')
            button_remove_doubles = icons.get("icon_remove_doubles")
            row.operator("mesh.remove_doubles", text="Remove Doubles",icon_value=button_remove_doubles.icon_id)  

            row.separator()
            
            row.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type="EDGE"
            row.operator("mesh.dissolve_edges", icon='BLANK1')
            row.operator("mesh.delete_edgeloop", text="Remove Edge Loop", icon='BLANK1')
            
            row.separator()
            
            row.operator("mesh.delete", "Faces", icon="SNAP_FACE").type="FACE"
            row.operator("mesh.dissolve_faces", icon='BLANK1')
            row.operator("mesh.delete", "Remove only Faces", icon='BLANK1').type="ONLY_FACE"            
                    
            row.separator()

            row.operator("mesh.dissolve_limited", icon="MATCUBE")       
            row.operator("mesh.dissolve_degenerate", icon='BLANK1')
            row.operator("mesh.delete", "Remove Edge & Faces", icon='BLANK1').type="EDGE_FACE"

            row.operator       
                
            row.operator("mesh.fill_holes", icon="RETOPO") 
            row.operator("mesh.delete_loose", icon='BLANK1')
            row.operator("mesh.edge_collapse", icon='BLANK1')            
            row.operator("mesh.vert_connect_nonplanar", icon='BLANK1')    


        if obj.mode == 'EDIT_CURVE':

            row = box.column(1)  
      
            row.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            row.operator("curve.delete", "Segment", icon="IPO_EASE_IN_OUT").type="SEGMENT"

            row.operator
                        
            row.operator("curve.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF")            

       
        if obj.mode == 'EDIT_SURFACE':

            row = box.column(1)                      
            
            row.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            row.operator("curve.delete", "Segments", icon="IPO_EASE_IN_OUT").type="SEGMENT"

            row.operator
                        
            row.operator("curve.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF") 
                              

        if obj.mode == 'EDIT_METABALL':
           
            row = box.column(1)  
            row.operator("mball.delete_metaelems", icon="META_BALL")

            row.operator
            
            row.operator("mball.reveal_metaelems", text="Clear Hide", icon = "RESTRICT_VIEW_OFF") 

       
        if  context.mode == 'PARTICLE':
           
            row = box.column(1)                     
            row.operator("particle.delete")

            row.separator()

            row.operator("particle.remove_doubles")
            
            row.separator()

            row.menu("VIEW3D_MT_particle_showhide", text = "Clear Hide", icon = "RESTRICT_VIEW_OFF")                        

            
        if obj.mode == 'SCULPT':
             
            props = row.operator("paint.hide_show", text="Clear All Hide", icon = "RESTRICT_VIEW_OFF")
            props.action = 'SHOW'
            props.area = 'ALL'
            

        if obj.mode == 'EDIT_ARMATURE':
      
            row = box.column(1)                     
            row.operator("armature.delete", text = "Selected Bone(s)", icon = "RIGHTARROW_THIN")

            row.separator()
            
            row.operator("sketch.delete", text = "Sketch Delete", icon = "RIGHTARROW_THIN")  
            
            row.separator()
                         
            row.operator("armature.parent_clear", icon = "RIGHTARROW_THIN").type='CLEAR'
            
      
        if context.mode == 'POSE':
            arm = context.active_object.data 

            row = box.column(1)                       
           
            row.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")
            row.operator("pose.paths_clear", text = "Clear Motion Path")

            row.separator()

            row.menu("VIEW3D_MT_pose_transform", text="Clear Location")  
            row.menu("clearparent", text="Clear Parenting")
            row.operator("pose.constraints_clear", text="Clear Constraint")            

            box.separator()
              
            row.operator("pose.reveal", text = "Clear Hide", icon = "RESTRICT_VIEW_OFF") 


        box.separator()



# LOAD UI: PANEL #

class VIEW3D_TP_Delete_Panel_TOOLS(bpy.types.Panel, draw_layout_delete):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Delete_Panel_TOOLS"
    bl_label = "Delete"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}

class VIEW3D_TP_Delete_Panel_UI(bpy.types.Panel, draw_layout_delete):
    bl_idname = "VIEW3D_TP_Delete_Panel_UI"
    bl_label = "Delete"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
