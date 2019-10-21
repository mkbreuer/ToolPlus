import bpy
from bpy import *
from bpy.props import *
from .. icons.icons import load_icons


def draw_xtras_layout(self, context, layout):
        tp_props = context.window_manager.tp_collapse_menu_retopo        
        layout.operator_context = 'INVOKE_REGION_WIN'
        icons = load_icons()

        col = layout.column(align=True)
                
        if not tp_props.display_xtras: 
          
            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_xtras", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Specials")

            if context.mode == 'EDIT_MESH':  
                row.operator("mesh.wplsmthdef_apply", text="", icon="NORMALIZE_FCURVES")
                row.operator("tp_ops.endbow", text="", icon="ROOTCURVE")  
                row.operator("mesh.tca_unbevel", text="", icon="LINCURVE")
            
            else:            
                row.operator("view3d.modal_arch_tool", text="", icon="PLUS")   
                row.operator("view3d.modal_arch_tool", text="", icon="SPHERECURVE")   
                row.operator("mesh.wplsmthdef_snap", text="", icon="SHAPEKEY_DATA")

        else:

            box = col.box().column(1)
            
            row = box.row(1)   
            row.prop(tp_props, "display_xtras", text="", icon="TRIA_RIGHT", emboss = False)                
            row.label("Specials")   

            if context.mode == 'EDIT_MESH':  
                row.operator("mesh.wplsmthdef_apply", text="", icon="NORMALIZE_FCURVES")
                row.operator("tp_ops.endbow", text="", icon="ROOTCURVE")  
                row.operator("mesh.tca_unbevel", text="", icon="LINCURVE")
            
            else:            
                row.operator("view3d.modal_arch_tool", text="", icon="PLUS")   
                row.operator("view3d.modal_arch_tool", text="", icon="SPHERECURVE")   
                row.operator("mesh.wplsmthdef_snap", text="", icon="SHAPEKEY_DATA")



            box = col.box().column(1)

            if context.mode == 'EDIT_MESH':  
               
                row = box.row(1)
                row.operator("mesh.tca_unbevel", "Unbevel", icon="LINCURVE")
                row.operator("tp_ops.endbow", icon="ROOTCURVE")

                row = box.row(1)
                row.operator("tp_ops.loopgap")
                row.operator("tp_ops.tubehole")


                box.separator()  

                row = box.column(1)
                row.label("Close")
              
                row = box.row(1)        
                row.operator("mesh.poke", "Tris")
                row.operator("mesh.closer", "Quad").quads = True
                row.operator("mesh.build_corner", "Modal")
               
                box.separator()  
               
                row = box.column(1) 
                row.label("Smooth Deform")              
              
                row = box.column(1)    
                row.operator("mesh.wplsmthdef_apply", text="2. Apply Mesh Deform", icon ="NORMALIZE_FCURVES")

                box.separator()   
                
            else:    
                row = box.column(1) 
                row.label("Modal Tools: ")   
                  
                row = box.column(1)
                row.operator("view3d.modal_arch_tool", "3Point Circle", icon="SPHERECURVE")        
               
                box.separator()   
                
                row = box.column(1) 
                row.label("Smooth Deform")              
              
                row = box.column(1)    
                row.operator("mesh.wplsmthdef_snap", text="1. Save Mesh State", icon ="SHAPEKEY_DATA")
       
                box.separator()   

