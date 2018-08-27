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
                               

class VIEW3D_TP_MultiMode(bpy.types.Menu):
    """Multi Mode Selection"""
    bl_label = "Multi Mode Selection"
    bl_label = "VIEW3D_TP_MultiMode"
    
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Vertex Select", icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge Select", icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Face Select", icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge Select", icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Vertex & Face Select", icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge & Face Select", icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge & Face Select", icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"


        row.prop_search(scene, "mychosenObject", bpy.data, "objects")



class VIEW3D_TP_Select_Menu(bpy.types.Menu):
    bl_label = "Select"
    bl_idname = "VIEW3D_TP_Select_Menu"   

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        if context.mode == 'SCULPT':
            layout.template_ID(context.scene.objects, "active")    

        if context.mode == 'OBJECT':

            layout.operator("object.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='SELECT'
            layout.operator("object.select_all", text = "Deselect").action='DESELECT'
            layout.operator("object.select_all", text = "Invert").action='INVERT'

            layout.separator()

            layout.operator_menu_enum("object.select_linked", "type", text="Linked", icon = "LINKED")    
            layout.operator_menu_enum("object.select_grouped", "type", text="Grouped")
            layout.operator_menu_enum("object.select_by_type", "type", text="byType")        

            layout.separator()

            layout.operator("object.select_by_layer", text="Layer", icon = "SEQ_SEQUENCER")
            layout.operator("object.select_camera", text="Camera")
            layout.operator("object.select_pattern", text="Pattern")
       
            layout.separator()

            layout.operator("object.select_random", text="Random", icon = "RNDCURVE")            
            layout.operator("object.select_all", text="Inverse").action = 'INVERT'
            layout.operator("object.select_mirror", text="Mirror")

            layout.separator() 
            layout.operator("tp_ops.unfreeze_selected", text = "Freeze", icon = "FREEZE")
            layout.operator("tp_ops.freeze_selected", text = "Unfreeze")             
            layout.menu("tp_menu.freezeall", text = "FreezeType")             
           
            layout.separator()

            layout.operator("object.select_more", text="More", icon="ZOOMIN") 
            layout.operator("object.select_less", text="Less", icon="ZOOMOUT")



        if context.mode == 'EDIT_MESH':

            layout.operator("mesh.select_all",text="GetAll", icon = "UV_SYNC_SELECT").action='SELECT'   
            layout.operator("mesh.select_all", text = "Deselect").action='DESELECT'
            layout.operator("mesh.select_all", text = "Invert").action='INVERT'
            layout.menu("VIEW3D_TP_MultiMode", text="Multi")       
            
            layout.separator()

            layout.operator("mesh.select_linked",text="Linked", icon = "LINKED")                            
            layout.menu("VIEW3D_MT_edit_mesh_select_similar",text="Similar")                         

            layout.separator()
                        
            layout.operator("mesh.select_face_by_sides",text="By Side", icon = "SNAP_FACE")
            layout.operator("mesh.select_axis", text="Active Side")
            layout.operator("mesh.faces_select_linked_flat", text="Linked Faces")

            layout.separator()
            
            layout.operator("mesh.select_loose",text="Loose", icon="STICKY_UVS_DISABLE")
            if context.scene.tool_settings.mesh_select_mode[2] is False:
                layout.operator("mesh.select_non_manifold", text="Non Manifold")  
            layout.operator("mesh.select_interior_faces", text="Interior Faces")                            
           
            layout.separator()

            layout.operator("mesh.edges_select_sharp", text="Sharp", icon="SNAP_EDGE")                          
            layout.operator("mesh.select_random", text="Random")
            layout.operator("mesh.select_nth")                            

            layout.separator()
                            
            layout.operator("mesh.loop_multi_select",text="Edge Loop", icon="ZOOMOUT").ring=False         
            layout.operator("mesh.loop_multi_select",text="Edge Ring", icon="COLLAPSEMENU").ring=True

            layout.separator()

            layout.operator("mesh.region_to_loop", text = "Edge Boundary Loop")
            layout.operator("mesh.loop_to_region", text = "Edge Loop Inner-Region")

            layout.separator()

            layout.operator('tp_meshlint.select', text='Select MeshLint', icon='EDIT')         

            layout.separator()

            layout.operator("mesh.select_more", text="More", icon="ZOOMIN") 
            layout.operator("mesh.select_less", text="Less", icon="ZOOMOUT")



        if context.mode == 'EDIT_CURVE':            

            layout.operator("curve.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='SELECT'
            layout.operator("curve.select_all", text = "Deselect").action='DESELECT'
            layout.operator("curve.select_all", text = "Invert").action='INVERT'           
        
            layout.separator()
            
            layout.operator("curve.select_linked", text="Linked", icon = "LINKED") 
            layout.operator("curve.select_nth",text="Nth Selected") 
            layout.operator("curve.select_random") 
            
            layout.separator()

            layout.operator("curve.de_select_first", text = "Select First", icon = "TRIA_UP") 
            layout.operator("curve.de_select_last", text = "Select Last", icon = "TRIA_DOWN") 
    
            layout.separator()
                        
            layout.operator("curve.select_next", icon = "TRIA_RIGHT") 
            layout.operator("curve.select_previous", icon = "TRIA_LEFT") 

            layout.separator()

            layout.operator("curve.select_more", text="More", icon="ZOOMIN") 
            layout.operator("curve.select_less", text="Less", icon="ZOOMOUT")


       
        if context.mode == 'EDIT_SURFACE':
            
            layout.operator("curve.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='SELECT'
            layout.operator("curve.select_all", text = "Deselect").action='DESELECT'
            layout.operator("curve.select_all", text = "Invert").action='INVERT'       
           
            layout.separator()
                        
            layout.operator("curve.select_linked", text="Linked", icon = "LINKED") 
            layout.operator("curve.select_nth",text="Nth Selected") 
            layout.operator("curve.select_random") 
            
            layout.separator()

            layout.operator("curve.select_more", text="More", icon="ZOOMIN") 
            layout.operator("curve.select_less", text="Less", icon="ZOOMOUT")

         

        if context.mode == 'EDIT_METABALL':
            
            layout.operator("mball.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='SELECT'
            layout.operator("mball.select_all", text = "Deselect").action='DESELECT'
            layout.operator("mball.select_all", text = "Invert").action='INVERT'

            layout.separator()
                        
            layout.operator_menu_enum("mball.select_similar", "type", text="Similar") 
            layout.operator("mball.select_random_metaelems") 


   
        if context.mode == 'EDIT_LATTICE':
            
            layout.operator("lattice.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='SELECT'
            layout.operator("lattice.select_all", text = "Deselect").action='DESELECT'
            layout.operator("lattice.select_all", text="Inverse").action = 'INVERT'

            layout.separator()
                                   
            layout.operator("lattice.select_mirror", text="Mirror", icon = "ARROW_LEFTRIGHT")
            layout.operator("lattice.select_random") 

            layout.separator()

            layout.operator("lattice.select_ungrouped", text="Ungrouped Verts")
                     


        if  context.mode == 'PARTICLE':

            layout.operator("particle.select_all", text = "GetAll", icon="RESTRICT_SELECT_OFF").action = 'SELECT'
            layout.operator("particle.select_all", text = "Deselect").action = 'DESELECT'
            layout.operator("particle.select_all", text="Inverse").action = 'INVERT'
            
            layout.separator()
           
            layout.operator("particle.select_linked", text="Linked", icon = "LINKED")
            layout.operator("particle.select_tips", text = "Tips", icon = "IPO_EASE_OUT")  
            layout.operator("particle.select_roots", text = "Roots")

            layout.separator()

            layout.operator("particle.select_more", text="More", icon="ZOOMIN")
            layout.operator("particle.select_less", text="Less", icon="ZOOMOUT")

            

        if context.mode == 'EDIT_ARMATURE':

            arm = context.active_object.data 
          
            layout.operator("armature.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='TOGGLE'
            layout.operator("armature.select_all", text = "Deselect").action = 'DESELECT'
            layout.operator("armature.select_all", text="Inverse").action = 'INVERT'
           
            layout.separator()
                   
            layout.operator("armature.select_mirror", text="Mirror", icon = "ARROW_LEFTRIGHT").extend = False

            layout.separator()
            
            layout.operator("armature.select_hierarchy", text="Parent", icon="BONE_DATA").direction = 'PARENT'
 
            props = layout.operator("armature.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'
                        
            layout.operator("armature.select_hierarchy", text="Child", icon="CONSTRAINT_BONE").direction = 'CHILD'

            props = layout.operator("armature.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            layout.separator()  

            layout.operator_menu_enum("armature.select_similar", "type", text="Similar")
            layout.operator("object.select_pattern", text="Select Pattern...")
            
            layout.separator()

            layout.operator("armature.select_more", text="More", icon="ZOOMIN")
            layout.operator("armature.select_less", text="Less", icon="ZOOMOUT")
            


        if context.mode == 'POSE':

            arm = context.active_object.data   
        
            layout.operator("pose.select_all", text = "GetAll", icon = "RESTRICT_SELECT_OFF").action='TOGGLE'
            layout.operator("pose.select_all", text = "Deselect").action = 'DESELECT'
            layout.operator("pose.select_all", text="Inverse").action = 'INVERT'
            
            layout.separator()
                       
            layout.operator("pose.select_mirror", text="Flip Active", icon = "ARROW_LEFTRIGHT")
        
            layout.separator()

            layout.operator("pose.select_constraint_target", text="Constraint Target", icon ="LINK_AREA")
            layout.operator("pose.select_linked", text="CONSTRAINT_BONE", icon="CONSTRAINT") 

            layout.separator()

            layout.operator("pose.select_hierarchy", text="Parent", icon ="BONE_DATA").direction = 'PARENT'
            props = layout.operator("pose.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'
            
            layout.separator()
                                    
            layout.operator("pose.select_hierarchy", text="Child", icon ="CONSTRAINT_BONE").direction = 'CHILD'

            props = layout.operator("pose.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            layout.separator()

            layout.operator_menu_enum("pose.select_grouped", "type", text="Grouped", icon ="GROUP_BONE")
            layout.operator("object.select_pattern", text="Select Pattern...")

