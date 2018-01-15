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

from toolplus_selection.select_meshlint import *

# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons    


# LOAD UI: PANEL #

EDIT = ["OBJECT", "EDIT_MESH", "EDIT_CRUVE", "EDIT_SURFACE", "EDIT_LATTICE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE", "POSE"]
GEOM = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE', 'ARMATURE', 'POSE', 'LAMP', 'CAMERA', 'EMPTY', 'SPEAKER']

class draw_panel_layout_select:
    
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

        tp_props = context.window_manager.tp_props_select 

        icons = load_icons()

        box = layout.box().column(1)      
        
        row = box.row(1)                      
        row.operator("view3d.select_border", text="Border", icon="BORDER_RECT") 
        row.operator("view3d.select_circle", text="Circle", icon="BORDER_LASSO")           

        box.separator() 

        if context.mode == 'OBJECT':

            box = layout.box().column(1)      
        
            row = box.row(1)          
            row.operator("object.move_to_layer", text="Move to Layer")  
            row.menu("VIEW3D_MT_object_showhide", "Hide / Show", icon = "VISIBLE_IPO_ON")

            box.separator() 

            row = box.row(1)

            row = box.row(1)
            sub = row.row()
            sub.scale_x = 0.3
            sub.operator("object.select_more",text="+")
            sub.operator("object.select_all",text="All").action = 'TOGGLE'
            sub.operator("object.select_less",text="-")   

            box.separator() 
     
            row = box.row(1)         
            row.operator("object.select_by_layer", text="All by Layer")
            row.operator("tp_ops.cycle_selected", text="CycleThrough")                       
            
            row = box.row(1)
            sub = row.row(1)
            sub.scale_x = 0.5
            sub.operator("view3d.view_selected"," ", icon = "ZOOM_SELECTED" )
            sub.operator("view3d.view_all"," ", icon = "ZOOM_OUT" )  
            row.operator("object.select_linked", text="Get Active").type='OBDATA'

            box.separator() 

            row = box.row(1)    
            row.operator("object.select_mirror", text="Mirror") 
            row.operator("object.select_all", text="Inverse").action = 'INVERT'

            row = box.row(1)              
            row.operator("object.select_random", text="Random")
            row.operator("object.select_camera", text="Camera")            

            box.separator() 

            row = box.row(1) 
            row.operator("object.select_linked", text="Linked", icon="EXPORT") 
            row.operator("object.select_grouped", text="Group", icon="EXPORT")        
        
            row = box.row(1) 
            row.operator("object.select_by_type", text="Type", icon="EXPORT")        
            row.operator("object.select_pattern", text="Name", icon="EXPORT")  

            box.separator() 

            box = layout.box().column(1)                                      

            row = box.row(1)
            row.operator("tp_ops.unfreeze_selected", text = "UnFreeze All", icon = "RESTRICT_SELECT_OFF")
            row.operator("tp_ops.freeze_selected", text = "Freeze", icon = "FREEZE")

            row = box.row(1)   
            row.operator("object.mesh_all", text= " ", icon="OBJECT_DATAMODE")
            row.operator("object.lamp_all",text=" ", icon="LAMP")
            row.operator("object.curve_all",text=" ", icon="OUTLINER_OB_CURVE")
            row.operator("object.bone_all",text=" ", icon="BONE_DATA")
            row.operator("object.particles_all", text=" ", icon="MOD_PARTICLES")
            row.operator("object.camera_all", text=" ", icon="OUTLINER_DATA_CAMERA")

            box.separator() 



        if context.mode == 'EDIT_MESH':
            
            box = layout.box().column(1)                              

            row = box.row(1)          
            layout.operator_context = 'INVOKE_REGION_WIN'
            row.operator("mesh.select_mode", text="Vert", icon='VERTEXSEL').type = 'VERT'
            row.operator("mesh.select_mode", text="Edge", icon='EDGESEL').type = 'EDGE'
            row.operator("mesh.select_mode", text="Face", icon='FACESEL').type = 'FACE'  

            box = layout.box().column(1)          
             
            row = box.row(1)
            row.menu("VIEW3D_MT_edit_mesh_showhide", "(Un)Hide", icon = "VISIBLE_IPO_ON") 
            row.menu("VIEW3D_TP_MultiMode", text="MultiSelect", icon="UV_SYNC_SELECT")  
             
            box = layout.box().column(1)

            row = box.row(1)
            sub = row.row()
            sub.scale_x = 0.3
            sub.operator("mesh.select_more",text="+")
            sub.operator("mesh.select_all",text="All")
            sub.operator("mesh.select_less",text="-")   
            
            row = box.row(1)
            row.operator("mesh.select_similar",text="Similar")              
            row.operator("mesh.select_similar_region", text="Regions") 

            row = box.row(1)
            row.operator("mesh.select_mirror", text="Mirror")             
            row.operator("mesh.select_all", text="Inverse").action = 'INVERT'
                          
            box = layout.box().column(1)
             
            row = box.row(1)
            row.operator("mesh.loop_multi_select", text="Edge Loops").ring = False
            row.operator("mesh.loop_multi_select", text="Edge Rings").ring = True              

            row = box.row(1)
            row.operator("mesh.grow_loop","Grow")
            row.operator("mesh.shrink_loop","Shrink")
             
            row = box.row(1)
            row.operator("mesh.path_select_ring","RingPath")
            row.operator("mesh.extend_loop","Extend")

            row = box.row(1)
            row.operator("mesh.region_to_loop", "Inner-Loops")   
            row.operator("mesh.loop_to_region", "Boundary-Loop")

            box = layout.box().column(1)
             
            row = box.row(1)
            row.operator("mesh.faces_select_linked_flat", text="Linked Faces")
            row.operator("mesh.select_nth", "Checker") 

            row = box.row(1)             
            row.operator("mesh.select_loose",text="Loose")
            row.operator("mesh.select_linked",text="Linked")             

            row = box.row(1)
            row.operator("mesh.select_axis", text="ActiveSide")             
            row.operator("mesh.select_face_by_sides",text="NSide")   
     
            row = box.row(1)             
            row.operator("mesh.edges_select_sharp", text="Sharp")
            row.operator("mesh.shortest_path_select", text="Shortest") 
             
            row = box.row(1)
            row.operator("mesh.select_ungrouped", text="Ungrouped Verts")
            row.operator("mesh.select_random", text="Random") 


            box = layout.box().column(1)

            row = box.row(1)
            if context.scene.tool_settings.mesh_select_mode[2] is False:
                row.operator("mesh.select_non_manifold", text="Non Manifold")      
            row.operator("mesh.select_interior_faces", text="Interior Faces")
             
            box = layout.box().column(1)         

            row = box.row(1)
            row.operator('meshlint.select', text='Select MeshLint', icon='EDIT')
       
            row = box.row(1)
            
            if tp_props.display_meshlint_toggle:
                row.prop(tp_props, "display_meshlint_toggle", text="Settings", icon='TRIA_DOWN')
            else:
                row.prop(tp_props, "display_meshlint_toggle", text="Settings", icon='TRIA_RIGHT')
          
            if MeshLintVitalizer.is_live:
                live_label = 'Pause!'
                play_pause = 'PAUSE'
            else:
                live_label = 'Live!'
                play_pause = 'PLAY'
            
            row.operator('meshlint.live_toggle', text=live_label, icon=play_pause)


            if tp_props.display_meshlint_toggle:
                
                box = layout.box().column(1)                   
                
                row = box.column(1)

                for lint in MeshLintAnalyzer.CHECKS:
                    prop_name = lint['check_prop']
                    is_enabled = getattr(context.scene, prop_name)
                    label = 'Check ' + lint['label']
                    row.prop(context.scene, prop_name, text=label)


            box = layout.box().column(1)         

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
         
            #name_crits = MeshLintControl.build_object_criticisms(bpy.context.selected_objects, total_problems)
           
            #for crit in name_crits:
                #row.label(crit)

            box.separator()

            box = layout.box().column(1)

            row = box.row(1)
            row.operator("object.mst_sort_mesh_elements", text="MST Sort Mesh Elements")

            row = box.row(1)
            row.operator("addongen.mesh_order_research_operator", text = "VertOrder").type = "Vertices"
            row.operator("addongen.mesh_order_research_operator", text = "EdgeOrder").type = "Edges"
            row.operator("addongen.mesh_order_research_operator", text = "PolyOrder").type = "Polygons"

            box.separator() 



        if context.mode == 'EDIT_CURVE':
            
             box = layout.box().column(1)

             row = box.row(1)
             sub = row.row()
             sub.scale_x = 0.3
             sub.operator("curve.select_more",text="+")
             sub.operator("curve.select_all",text="All").action = 'TOGGLE'  
             sub.operator("curve.select_less",text="-")   

             box.separator()

             row = box.row(1) 
             row.operator("curve.select_all", text="Inverse").action = 'INVERT'
             row.menu("VIEW3D_MT_edit_curve_showhide",  icon = "VISIBLE_IPO_ON") 

             row = box.row(1) 
             row.operator("curve.select_random", text="Random") 
             row.operator("curve.select_similar", text="Similar") 

             row = box.row(1)
             row.operator("curve.select_linked", text="Linked")             
             row.operator("curve.select_nth", text="Checker")
            
             box.separator()
             
             row = box.row(1) 
             row.operator("curve.de_select_first", text="First")
             row.operator("curve.de_select_last", text="Last")
            
             row = box.row(1)             
             row.operator("curve.select_next", text="Next")
             row.operator("curve.select_previous", text="Previous")

             box.separator() 



        if context.mode == 'EDIT_SURFACE':

             box = layout.box().column(1)

             row = box.row(1)
             sub = row.row()
             sub.scale_x = 0.3
             sub.operator("curve.select_more",text="+")
             sub.operator("curve.select_all",text="All").action = 'TOGGLE'
             sub.operator("curve.select_less",text="-")   

             box.separator()

             row = box.row(1) 
             row.operator("curve.select_all", text="Inverse").action = 'INVERT'
             row.menu("VIEW3D_MT_edit_curve_showhide",  icon = "VISIBLE_IPO_ON") 

             row = box.row(1) 
             row.operator("curve.select_random", text="Random") 
             row.operator("curve.select_similar", text="Similar") 

             row = box.row(1)
             row.operator("curve.select_linked", text="Linked")             
             row.operator("curve.select_nth", text="Checker")

             box.separator()
             
             row = box.row(1) 
             row.operator("curve.select_row", text="Control Point Row") 
        


        if context.mode == 'EDIT_LATTICE':
            
             box = layout.box().column(1)
           
             row = box.row(1) 
             row.operator("lattice.select_all", text="All").action = 'TOGGLE'
             row.operator("lattice.select_all", text="Inverse").action = 'INVERT'

             row = box.row(1)
             row.operator("lattice.select_random", text="Random") 
             row.operator("lattice.select_mirror", text="Mirror") 

             box.separator()

             row = box.row(1)
             row.operator("lattice.select_ungrouped", text="Select Ungrouped")             



        if context.mode == 'EDIT_METABALL':        
            
             box = layout.box().column(1)
           
             row = box.row(1) 
             row.operator("mball.select_all", text="All").action = 'TOGGLE'

             box.separator()
             
             row = box.row(1)
             row.operator("mball.select_random_metaelems", text="Random") 
             row.operator("mball.select_all", text="Inverse").action = 'INVERT'

             row = box.row(1)
             row.operator("mball.select_similar", text="Type").type='TYPE'
             row.operator("mball.select_similar", text="Radius").type='RADIUS' 
        
             box.separator()
             row = box.row(1)
             row.operator("mball.select_similar", text="Stiffness").type='STIFFNESS'   
             row.operator("mball.select_similar", text="Rotation").type='ROTATION'    
             


        if context.mode == 'EDIT_ARMATURE':          
                
             box = layout.box().column(1)

             row = box.row(1)
             sub = row.row()
             sub.scale_x = 0.3
             sub.operator("armature.select_more",text="+")
             sub.operator("armature.select_all",text="All").action = 'TOGGLE'
             sub.operator("armature.select_less",text="-")   

             box.separator()

             row = box.row(1) 
             row.operator("armature.select_mirror", text="Mirror").extend = False
             row.operator("armature.select_all", text="Inverse").action = 'INVERT'            
            
             row = box.row(1)   
             row.operator("armature.select_hierarchy", text="Parent").direction = 'PARENT'
             row.operator("armature.select_hierarchy", text="Child").direction = 'CHILD'

             row = box.row(1)     
             props = row.operator("armature.select_hierarchy", text="Extend Parent")
             props.extend = True
             props.direction = 'PARENT'

             props = row.operator("armature.select_hierarchy", text="Extend Child")
             props.extend = True
             props.direction = 'CHILD'

             box.separator()

             row = box.row(1)                           
             row.operator_menu_enum("armature.select_similar", "type", text="Similar")
             row.operator("object.select_pattern", text="Pattern...")



        if context.mode == 'POSE':    

             box = layout.box().column(1)

             row = box.row(1)
             sub = row.row()
             sub.scale_x = 0.3
             sub.operator("pose.select_hierarchy",text="+").direction = 'CHILD'
             sub.operator("pose.select_all",text="All").action = 'TOGGLE'
             sub.operator("pose.select_hierarchy",text="-").direction = 'PARENT'   

             box.separator()

             row = box.row(1)      
             row.operator("pose.select_mirror", text="Flip Active")
             row.operator("pose.select_all", text="Inverse").action = 'INVERT'
     
             row = box.row(1)            
             row.operator("pose.select_constraint_target", text="Constraint Target")
             row.operator("pose.select_linked", text="Linked")

             row = box.row(1)
             row.operator("pose.select_hierarchy", text="Parent").direction = 'PARENT'
             row.operator("pose.select_hierarchy", text="Child").direction = 'CHILD'

             row = box.row(1)
             props = row.operator("pose.select_hierarchy", text="Extend Parent")
             props.extend = True
             props.direction = 'PARENT'
            
             props = row.operator("pose.select_hierarchy", text="Extend Child")
             props.extend = True
             props.direction = 'CHILD'
                
             box.separator()

             row = box.row(1) 
             row.operator_menu_enum("pose.select_grouped", "type", text="Grouped...")
             row.operator("object.select_pattern", text="Pattern...")



        if  context.mode == 'PARTICLE':
      
             box = layout.box().column(1)

             row = box.row(1)
             sub = row.row()
             sub.scale_x = 0.3
             sub.operator("particle.select_more",text="+")
             sub.operator("particle.select_all",text="All").action = 'TOGGLE'
             sub.operator("particle.select_less",text="-") 

             box.separator()

             row = box.row(1)   
             row.operator("particle.select_linked", text="Linked", icon = "LINKED") 
             row.operator("particle.select_all", text="Inverse").action = 'INVERT'

             row = box.row(1)  
             row.operator("particle.select_tips", text = "Tips", icon = "IPO_EASE_OUT")  
             row.operator("particle.select_roots", text = "Roots")





class VIEW3D_TP_Selection_Panel_TOOLS(bpy.types.Panel, draw_panel_layout_select):
    bl_category = "T+"
    bl_idname = "VIEW3D_TP_Selection_Panel_TOOLS"
    bl_label = "Select"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}
    

class VIEW3D_TP_Selection_Panel_UI(bpy.types.Panel, draw_panel_layout_select):
    bl_idname = "VIEW3D_TP_Selection_Panel_UI"
    bl_label = "Select"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

