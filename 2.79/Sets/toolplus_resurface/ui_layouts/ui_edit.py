 ##### BEGIN GPL LICENSE BLOCK #####
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


# LOAD UI: PANEL #
icons = load_icons()
types_edit_ui = [("tp_e0"    ," "   ," "  ,"COLLAPSEMENU"    ,0),
                ("tp_e1"    ," "   ," "   , icons["icon_select_mesh"].icon_id ,1), 
                ("tp_e2"    ," "   ," "   ,"SNAP_VOLUME"     ,2), 
                ("tp_e3"    ," "   ," "   , icons["icon_edit_divide"].icon_id ,3), 
                ("tp_e4"    ," "   ," "   ,"SNAP_FACE"       ,4), 
                ("tp_e5"    ," "   ," "   ,"SNAP_EDGE"       ,5),
                ("tp_e6"    ," "   ," "   ,"SNAP_VERTEX"     ,6)]
bpy.types.Scene.types_edit_layout = bpy.props.EnumProperty(name = " ", default = "tp_e0", items = types_edit_ui)


def draw_edit_ui(self, context, layout):

        tp_props = context.window_manager.tp_props_resurface        

        icons = load_icons()
  
        ob = context.object  
        obj = context.object
        scene = context.scene

        col = layout.column(1)

        box = col.box().column(1) 

        row = box.row(1)  
        row.prop(scene, 'types_edit_layout', emboss = False, expand = True) #icon_only=True,


        if scene.types_edit_layout == "tp_e0": 
            pass


        if scene.types_edit_layout == "tp_e1": 

            #box = col.box().column(1)

            #row = box.row(1)          
            #layout.operator_context = 'INVOKE_REGION_WIN'
            #row.operator("mesh.select_mode", text="Vert", icon='VERTEXSEL').type = 'VERT'
            #row.operator("mesh.select_mode", text="Edge", icon='EDGESEL').type = 'EDGE'
            #row.operator("mesh.select_mode", text="Face", icon='FACESEL').type = 'FACE'  
  
            box = col.box().column(1)

            row = box.row(1)
            row.operator("view3d.select_border", text="Border", icon="BORDER_RECT") 
            row.operator("view3d.select_circle", text="Circle", icon="BORDER_LASSO")              
            
            box.separator()   


            box = col.box().column(1)          
             
            row = box.row(1)
            row.operator("mesh.hide", "SelHide", icon = "RESTRICT_VIEW_ON").unselected=False 
            row.operator("mesh.reveal", "Show", icon = "RESTRICT_VIEW_OFF") 
            row.operator("mesh.hide", "InvHide", icon = "RESTRICT_VIEW_ON").unselected=True 

            box.separator()                


            box = col.box().column(1)

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

            box.separator()                             
            box = col.box().column(1)
             
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
           
            box.separator()   
            box = col.box().column(1)
             
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

            box.separator()   
            box = col.box().column(1)

            row = box.row(1)
            if context.scene.tool_settings.mesh_select_mode[2] is False:
                row.operator("mesh.select_non_manifold", text="Non Manifold")      
            row.operator("mesh.select_interior_faces", text="Interior Faces")
            
            box.separator()             


        if scene.types_edit_layout == "tp_e2": 

            box = col.box().column(1)

            row = box.row(1) 
            row.alignment = 'CENTER'                          
            row.label("Transform")
           
            box.separator()  

            row = box.row(1) 
            row.operator("mira.linear_deformer", text="LinearDeformer", icon ="OUTLINER_OB_MESH")
              
            row = box.row(1)
            row.prop(context.scene.mi_ldeformer_settings, "manual_update", text='ManualUpdate')                         
          
            box.separator() 

            row = box.row(1)
            row.operator("mira.noise", text="Noise", icon="RNDCURVE")
            row.operator("mira.deformer", text="Deformer")
                      
            box.separator()  


        if scene.types_edit_layout == "tp_e3": 
                          

            box = col.box().column(1)

            row = box.row(1) 
            row.alignment = 'CENTER'                          
            row.label("Face Fill")
           
            box.separator()            
           
            row = box.row(1)        
            #row.operator("tp_ops.closer", "Quads", icon="LATTICE_DATA").quads = True
            row.operator("mesh.poke", "Poke", icon="MESH_DATA")
            row.operator("tp_ops.build_corner", "Corner", icon="OUTLINER_DATA_MESH")
          
            row = box.row(1)      
            row.operator("mesh.tris_convert_to_quads",text="M-Quads") 
            row.operator("mesh.quads_convert_to_tris",text="M-Tris")
            
            box.separator()  

            box = col.box().column(1)

            row = box.row(1) 
            row.alignment = 'CENTER'                          
            row.label("SubDivide", icon="PARTICLE_POINT")

            box.separator()  
            
            row = box.row(1)                     
            row.operator("mesh.subdivide",text="1").number_cuts=1
            row.operator("mesh.subdivide",text="2").number_cuts=2
            row.operator("mesh.subdivide",text="3").number_cuts=3
            row.operator("mesh.subdivide",text="4").number_cuts=4
            row.operator("mesh.subdivide",text="5").number_cuts=5
            row.operator("mesh.subdivide",text="6").number_cuts=6

            row = box.row(1) 
            row.operator("screen.redo_last", text="", icon="RECOVER_LAST")  
            row.operator("mesh.unsubdivide", text="  UnSubDiv")           
            props = row.operator("mesh.subdivide",text="Smooth 5/5")
            props.number_cuts=5
            props.smoothness=5

            box.separator()                             


            box = col.box().column(1)                     

            row = box.row(1)              
            row.alignment = 'CENTER'
            row.label("Knifes")             
         
            box.separator()  
         
            row = box.row(1) 
            props = row.operator("mesh.knife_tool", text="Knife", icon="LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False            
         
            row.operator("mesh.bisect", icon="SCULPTMODE_HLT")          
           
            row = box.row(1)               
            props = row.operator("mesh.knife_tool", text="Knife Select", icon="LINE_DATA")
            props.use_occlude_geometry = False
            props.only_selected = True
             
            row.operator("mesh.loopcut_slide","Loop Cut", icon="COLLAPSEMENU")             
                                   
            row = box.row(1) 
            row.operator("mesh.knife_project", icon="LINE_DATA")                        
            row.operator("tp_ops.ext_cut_faces", text="Face Cut", icon = "GRIP")             

            box.separator()             

                


        if scene.types_edit_layout == "tp_e4": 

#            box = col.box().column(1)
#            
#            row = box.row(1)          
#            layout.operator_context = 'INVOKE_REGION_WIN'
#            row.operator("mesh.select_mode", text="Select Faces", icon='FACESEL').type = 'FACE'  
#            row.menu("tp_menu.select_multi_menu", text="", icon="LOOPSEL")

#            box.separator() 


            box = col.box().column(1)
                            
            row = box.row(1)
            row.alignment = 'CENTER'
            row.label("Extrude & Fill")

            box.separator()  

            row = box.row(1)
            row.operator("mesh.edge_face_add", "Edge/Face")              
            row.operator("mesh.extrude_reshape", "Push/Pull")                 
                          
            row = box.row(1)
            row.operator("mesh.fill", text="Fill Mesh")    
            row.operator("mesh.fill_grid", "Fill Grid")       
            
            row = box.row(1)            
            row.operator("mesh.beautify_fill", text="Fill Beauty")              
            row.operator("mesh.poke", text="Fill Poke")        

            row = box.row(1)                                   
            row.operator('mesh.face_inset_fillet', text = 'Inset Fillet')                                             
            row.operator("mesh.inset", text="Inset Faces")

            row = box.row(1)                                                         
            row.operator('mesh.fillet_plus', text = 'Fillet Plus')                                                   
            row.operator('object.mextrude', text = 'Multi')         

            box.separator()  
                           
            row = box.row(1)              
            row.operator("mesh.extrude_along_curve", text="Extrude Mesh along Curve", icon ="BLANK1")      
            
            box.separator()            
           
            row = box.column(1)                 
            row.operator("tp_ops.facetube", text="Tube between 2 Faces", icon ="BLANK1")                    

            box.separator() 
            box.separator() 

            row = box.row(1) 
            row.operator("mesh.split") 
            row.operator("mesh.separate",text="Separate")      

            box.separator() 
            
            
            

        if scene.types_edit_layout == "tp_e5": 

#            box = col.box().column(1)
#            
#            row = box.row(1)          
#            layout.operator_context = 'INVOKE_REGION_WIN'
#            row.operator("mesh.select_mode", text="Select Edges", icon='EDGESEL').type = 'EDGE'
#            row.menu("tp_menu.select_multi_menu", text="", icon="LOOPSEL")

#            box.separator() 


            box = col.box().column(1)
            
            row = box.row(1)
            row.alignment = 'CENTER'
            row.label("Extrude")

            box.separator()   

            row = box.row(1)
            row.operator("view3d.edit_mesh_extrude_move_normal", text="Region")             
            row.operator_menu_enum('mesh.offset_edges', 'geometry_mode')   
                    
            row = box.row(1)
            row.operator("view3d.edit_mesh_extrude_individual_move", text="Individual") 
            row.operator("mesh.tca_unbevel", text="Unbevel")  

            box.separator()   
                  
            row = box.row(1)
            row.operator("mesh.spin")
            row.operator("mesh.screw")              

            row = box.row(1)
            row.operator("mesh.solidify", text="Solidify")
            row.operator("mesh.wireframe", text="Wire")      

            box.separator()            
            box.separator()            
           
            row = box.column(1)              
            row.operator("tp_ops.edgetubes", text="Tube to selected Edges", icon ="BLANK1")    
                 
            box.separator() 
            box.separator() 

            row = box.row(1) 
            row.operator("mesh.split") 
            row.operator("mesh.separate",text="Separate")      

            box.separator() 
                        



        if scene.types_edit_layout == "tp_e6": 

#            box = col.box().column(1)
#            
#            row = box.row(1)          
#            layout.operator_context = 'INVOKE_REGION_WIN'
#            row.operator("mesh.select_mode", text="Select Vertices", icon='VERTEXSEL').type = 'VERT'
#            row.menu("tp_menu.select_multi_menu", text="", icon="LOOPSEL")         
#       
#            box.separator()  
          
            box = col.box().column(1)
           
            row = box.row(1)
            row.alignment = 'CENTER'
            row.label("Connect", icon="SOUND")             

            box.separator()   

            row = box.row(1)  
            row.operator("mesh.vert_connect", "Vert Connect") 
            row.operator("mesh.vert_connect_path", "Vert Path") 

            row = box.row(1) 
            row.operator("mesh.bridge_edge_loops", "Bridge Edges")
            row.operator("mesh.edge_face_add", "Edge / Face")           

#            box = layout.box().column(1)    
#             
#            row = box.row(1)              
#            row.alignment = 'CENTER'
#            row.label("Smooth", icon ="SPHERECURVE")

#            row = box.row(1)                      
#            row.operator("mesh.vertices_smooth_laplacian","Laplacian")  
#            row.operator("mesh.vertices_smooth","Smooth")  

#            row = box.row(1)  
#            row.operator("mesh.shrinkwrap_smooth","Shrinkwrap Smooth", icon ="BLANK1")         

            box.separator()              
            
            box = col.box().column(1)                 

            row = box.row(1)              
            row.alignment = 'CENTER'
            row.label("Merge", icon ="AUTOMERGE_ON")

            box.separator()   

            row = box.row(1)
            row.operator_menu_enum("mesh.merge", "type")  
            row.operator("mesh.merge","Merge Center").type='CENTER'   
             
            box.separator()            
             
            row = box.row(1)
            row.prop(context.tool_settings, "use_mesh_automerge", text = "Auto Merge")
        
            row = box.row(1)
            row.prop(context.tool_settings, "double_threshold", text="Double Threshold")

            box.separator()                             
            box.separator()  

            row = box.row(1) 
            row.operator("mesh.split") 
            row.operator("mesh.separate",text="Separate")      

            box.separator() 
            
            


