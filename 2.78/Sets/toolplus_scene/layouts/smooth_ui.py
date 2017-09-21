import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons



def draw_smooth_layout(self, context, layout):

    layout.operator_context = 'INVOKE_REGION_WIN'
   
    icons = load_icons()     

    col = layout.column(align=True)

    box = col.box().column(1)  


    if context.mode == 'OBJECT': 
        
        row = box.row(1)  
        row.operator("object.shade_flat", text="Flat", icon="MESH_CIRCLE")
        row.operator("object.shade_smooth", text="Smooth", icon="SMOOTH")  
   
        box.separator() 
        
        obj = context.active_object     
        if obj:
           obj_type = obj.type
                          
           if obj and obj_type in {'MESH'}:

               row = box.row(1)  
               row.prop(context.active_object.data, "use_auto_smooth", text="AutoSmooth",icon="AUTO")
            
               row = box.row(1)
               row.active = context.active_object.data.use_auto_smooth
               row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")   
          
               box.separator() 
               
               row = box.row(1)
               row.prop(context.active_object.data, "show_double_sided", text="DoubleSide",icon="GHOST")   

           else:
               pass                            

        box.separator() 


    if context.mode == 'EDIT_CURVE':
        
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


    if context.mode == 'EDIT_MESH':          

        row = box.row(1) 
        row.operator("mesh.faces_shade_flat", text="Flat", icon="MESH_CIRCLE") 
        row.operator("mesh.faces_shade_smooth", text="Smooth", icon="SMOOTH") 

        box.separator() 
        box.separator() 
        
        row = box.row(1)  
        row.prop(context.active_object.data, "use_auto_smooth",icon="AUTO")
    
        row = box.row(1)
        row.active = context.active_object.data.use_auto_smooth
        row.prop(context.active_object.data, "auto_smooth_angle", text="Angle")  

        box.separator() 
       
        row = box.row(1)
        row.prop(context.active_object.data, "show_double_sided",icon="GHOST")   

        box.separator()   
        box.separator()   

        row = box.row(1) 
        row.operator("mesh.mark_sharp", text="SharpVerts", icon='SNAP_VERTEX').use_verts = True          
        props = row.operator("mesh.mark_sharp", text="", icon='X')
        props.use_verts = True
        props.clear = True
        
        row = box.row(1)  
        row.operator("mesh.mark_sharp", text="SharpEdges", icon='SNAP_EDGE')
        row.operator("mesh.mark_sharp", text="", icon='X').clear = True

        box.separator()   
