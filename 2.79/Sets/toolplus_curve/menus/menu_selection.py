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


class VIEW3D_TP_Selection_Menu(bpy.types.Menu):
    bl_label = "Select"
    bl_idname = "tp_menu.curve_select"   

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
     

        ob = context
        if ob.mode == 'OBJECT':

            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
              
            layout.operator("object.select_all")             

            layout.separator()

            layout.operator("object.select_linked", text="Linked") 
            layout.operator("object.select_grouped", text="Group")        
            layout.operator("object.select_by_type", text="Type")        

            layout.separator()

            layout.operator("object.select_by_layer", text="Layer")
            layout.operator("object.select_pattern", text="Name")
            layout.operator("object.select_camera", text="Camera")

            layout.separator()

            layout.operator("object.select_random", text="Random")            
            layout.operator("object.select_all", text="Inverse").action = 'INVERT'
            layout.operator("object.select_mirror", text="Mirror")


        if ob.mode == 'EDIT_CURVE':
            
            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                          
            layout.operator("curve.select_all").action = 'TOGGLE'            

            layout.separator()

            layout.operator("curve.select_linked", text="Linked") 
            layout.operator("curve.select_all", text="Inverse").action = 'INVERT'
            layout.operator("curve.select_nth",text="Nth Selected") 
            layout.operator("curve.select_random") 
            
            layout.separator()

            layout.operator("curve.de_select_first", text = "Select First") 
            layout.operator("curve.de_select_last", text = "Select Last") 
    
            layout.separator()
                        
            layout.operator("curve.select_next") 
            layout.operator("curve.select_previous") 

            layout.separator()

            layout.operator("curve.select_more", text="More") 
            layout.operator("curve.select_less", text="Less")


       
        if ob.mode == 'EDIT_SURFACE':
            
            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                          
            layout.operator("curve.select_all").action = 'TOGGLE'            

            layout.separator()

            layout.operator("curve.select_linked", text="Linked") 
            layout.operator("curve.select_all", text="Inverse").action = 'INVERT'
            layout.operator("curve.select_nth",text="Nth Selected") 
            layout.operator("curve.select_random") 
            
            layout.separator()

            layout.operator("curve.select_more", text="More") 
            layout.operator("curve.select_less", text="Less")



        if ob.mode == 'EDIT_MESH':

            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                          
            layout.operator("mesh.select_all") 
            layout.menu("tp_display.selection_modes") 
            
            layout.separator()
        
            layout.operator("mesh.select_linked",text="Linked")
            layout.operator("mesh.select_similar",text="Similar")              
            layout.operator("mesh.select_all", text="Inverse").action = 'INVERT'  

            layout.separator()
            
            layout.operator("mesh.select_axis", text="Active Side")                        
            layout.operator("mesh.select_face_by_sides",text="Face by Side")
            layout.operator("mesh.faces_select_linked_flat", text="Linked Faces")
            
            layout.separator()
            
            layout.operator("mesh.select_nth") 

            layout.separator()                        
            
            layout.operator("mesh.loop_multi_select",text="Edge Loop").ring=False          
            layout.operator("mesh.loop_multi_select",text="Edge Ring").ring=True

            layout.separator()
            
            layout.operator("mesh.select_loose",text="Loose")
            layout.operator("meshlint.select", "Meshlint")

            if context.scene.tool_settings.mesh_select_mode[2] is False:
                layout.operator("mesh.select_non_manifold", text="Non Manifold")  
            layout.operator("mesh.select_interior_faces", text="Interior Faces") 

            
            layout.separator()
            layout.operator("mesh.edges_select_sharp", text="Sharp")                          
            layout.operator("mesh.select_random", text="Random")
                                                    
            layout.separator()

            layout.operator("mesh.region_to_loop", text = "Edge Boundry Loop")
            layout.operator("mesh.loop_to_region", text = "Edge Loop Inner-Region")



        if ob.mode == 'EDIT_METABALL':
            
            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                          
            layout.operator("mball.select_all").action = 'TOGGLE'
            
            layout.separator()
            
            layout.operator_menu_enum("mball.select_similar", "type", text="Similar") 
            layout.operator("mball.select_all", text="Inverse").action = 'INVERT'
            layout.operator("mball.select_random_metaelems") 


   
        if ob.mode == 'EDIT_LATTICE':
            
            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                          
            layout.operator("lattice.select_all").action = 'TOGGLE'
            
            layout.separator()

            layout.operator("lattice.select_mirror", text="Mirror")
            layout.operator("lattice.select_all", text="Inverse").action = 'INVERT'
            layout.operator("lattice.select_random") 

            layout.separator()

            layout.menu("vgroupmenu")   
            
            layout.separator()

            layout.operator("lattice.select_ungrouped", text="Ungrouped Verts")
            
                 

        if  context.mode == 'PARTICLE':
       
            layout.operator("view3d.select_border")

            layout.separator()
            
            layout.operator("particle.select_all").action = 'TOGGLE'

            layout.separator()

            layout.operator("particle.select_tips", text = "Tips")  
            layout.operator("particle.select_roots", text = "Roots")

            layout.separator()

            layout.operator("particle.select_linked", text="Linked") 
            layout.operator("particle.select_all", text="Inverse").action = 'INVERT'

            layout.separator()

            layout.operator("particle.select_more", text="More")
            layout.operator("particle.select_less", text="Less")


        if ob.mode == 'EDIT_ARMATURE':

            arm = context.active_object.data 

            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                          
            layout.operator("armature.select_all").action = 'TOGGLE'
            
            layout.separator()
            
            layout.operator("armature.select_mirror", text="Mirror").extend = False
            layout.operator("armature.select_all", text="Inverse").action = 'INVERT'

            layout.separator()

            layout.operator("armature.select_hierarchy", text="Parent").direction = 'PARENT'
 
            props = layout.operator("armature.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'
                        
            layout.operator("armature.select_hierarchy", text="Child").direction = 'CHILD'

            props = layout.operator("armature.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            layout.separator()  

            layout.operator_menu_enum("armature.select_similar", "type", text="Similar")
            layout.operator("object.select_pattern", text="Select Pattern...")
            
            layout.separator()

            layout.operator("armature.select_more", text="More")
            layout.operator("armature.select_less", text="Less")
            

        if context.mode == 'POSE':

            arm = context.active_object.data   
    
            layout.operator("view3d.select_circle")
            layout.operator("view3d.select_border")

            layout.separator()
                        
            layout.operator("pose.select_all").action = 'TOGGLE'
            
            layout.separator()

            layout.operator("pose.select_all", text="Inverse").action = 'INVERT'
            layout.operator("pose.select_mirror", text="Flip Active")
            layout.operator("pose.select_constraint_target", text="Constraint Target")
            layout.operator("pose.select_linked", text="CONSTRAINT_BONE") 

            layout.separator()

            layout.operator("pose.select_hierarchy", text="Parent").direction = 'PARENT'
            props = layout.operator("pose.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'
            
            layout.separator()
                                    
            layout.operator("pose.select_hierarchy", text="Child").direction = 'CHILD'

            props = layout.operator("pose.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            layout.separator()

            layout.operator_menu_enum("pose.select_grouped", "type", text="Grouped")
            layout.operator("object.select_pattern", text="Select Pattern...")














