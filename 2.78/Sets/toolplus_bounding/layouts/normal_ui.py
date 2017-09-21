import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



def draw_normal_layout(context, layout):
        tp_props = context.window_manager.bbox_window            
      
        layout.operator_context = 'INVOKE_REGION_WIN'
       
        icons = load_icons()     

        col = layout.column(align=True)

        box = col.box().column(1)  


        if context.mode == 'OBJECT': 

            row = box.column(1)  
            row.operator("tp_ops.rec_normals", text="Recalculate Normals", icon="SNAP_NORMAL")  
            row.operator("tp_ops.purge_mesh_data", text="Purge Unused MeshData", icon="PANEL_CLOSE")
  
         
            box.separator()


        elif context.mode == 'EDIT_CURVE':
            
            row = box.column(1)
            row.operator("curve.normals_make_consistent",text="Recalculate Normals", icon='SNAP_NORMAL')        

            box.separator() 

            row = box.row(1)   
            row.prop(context.object.data, "show_handles", text="Handles", icon='IPO_BEZIER')
            row.prop(context.object.data, "show_normal_face", text="Normals", icon='SNAP_NORMAL')
           
            if context.object.data.show_normal_face == True:  

                row = box.column(1)
                row.prop(context.scene.tool_settings, "normal_size", text="Size")                                   

            box.separator()   



        elif context.mode == 'EDIT_MESH':  

            row = box.row(1)
            row.operator("mesh.normals_make_consistent",text="Rec. Normals", icon='SNAP_NORMAL')
            row.operator("mesh.flip_normals", text="Flip", icon = "FILE_REFRESH")            

            row = box.row(1)
            row.operator("mesh.normals_make_consistent", text="Rec-Inside").inside = True        
            row.operator("mesh.normals_make_consistent", text="Rec-Outside").inside = False             
                   
            row = box.row(1)
            row.prop(context.active_object.data, "show_normal_vertex", text="", icon='VERTEXSEL')
            row.prop(context.active_object.data, "show_normal_loop", text="", icon='LOOPSEL')
            row.prop(context.active_object.data, "show_normal_face", text="", icon='FACESEL')
             
            row.active = context.active_object.data.show_normal_vertex or context.active_object.data.show_normal_face
            row.prop(context.scene.tool_settings, "normal_size", text="Size")  
            
            box.separator()  
            box.separator()  
                 
            row = box.column(1)
            row.operator("mesh.select_similar",text="Select Similar Normals", icon='RESTRICT_SELECT_OFF').type='NORMAL'

            box.separator()  
        

        else:
            pass      